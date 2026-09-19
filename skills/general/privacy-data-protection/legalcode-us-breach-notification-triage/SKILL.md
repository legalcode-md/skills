---
name: legalcode-us-breach-notification-triage
description: 'Multi-state US breach notification triage covering all 50 states, DC, Puerto Rico, Guam,
  US Virgin Islands, and American Samoa. Use when a security incident involves personal information of
  US residents and you need to determine notification obligations: which states require notice, to whom,
  by when, with what content, and whether any safe harbor (encryption, good-faith acquisition, HIPAA compliance)
  applies.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Multi-state US breach notification triage covering all 50 states, DC, Puerto Rico, Guam, US Virgin Islands, and American Samoa. Use when a security incident involves personal information of US residents and you need to determine notification obligations: which states require notice, to whom, by when, with what content, and whether any safe harbor (encryption, good-faith acquisition, HIPAA compliance) applies. Covers the full triage lifecycle — PI definition matching, breach definition analysis, clock-start normalization, notification deadline calculation, AG filing thresholds, notice content requirements, substitute notice triggers, credit monitoring obligations, and federal overlay requirements (HIPAA Breach Notification Rule, GLBA Safeguards Rule, SEC Form 8-K Item 1.05, FCC telecom rules, CIRCIA). Produces a prioritized notification timeline with per-state checklists, template notice letters, AG filing guidance, and a Glass Box audit trail. Integrates with legalcode-breach-severity-assessment for upstream harm triage.


# Legalcode US Breach Notification Triage

> **Disclaimer**: This skill provides a framework for AI-assisted breach notification triage
> for US jurisdictions. It does not constitute legal advice. All outputs must be reviewed by
> qualified legal counsel licensed in the relevant jurisdiction(s) before any notice is
> dispatched. US breach notification laws are amended frequently — verify current statutory
> text and AG guidance before relying on any provision described here. Statutory citations
> and timelines in this skill are based on research as of early 2026 and carry hallucination
> risk; mark any unverified claim [VERIFY] and cross-check against official sources. Failing
> to notify a required jurisdiction on time can result in civil penalties, AG enforcement
> actions, and private litigation.

---

## Purpose and Scope

This skill performs multi-state US breach notification triage for legal, privacy, and
incident-response teams. It determines which US jurisdictions require notice, to whom, by
when, with what content, and whether any safe harbor or exemption applies.

**Covers:**

- Per-jurisdiction applicability (all 50 states + DC + Puerto Rico + Guam + US Virgin
  Islands + American Samoa)
- Personal information (PI) definition matching per state
- Breach definition analysis (unauthorized access vs. unauthorized acquisition)
- Clock-start normalization (discovery vs. awareness vs. determination)
- Notification deadline calculation (calendar vs. business days; ASAP vs. set timeframe)
- AG filing thresholds and content requirements
- Safe harbor analysis (encryption, good-faith acquisition, risk of no harm)
- Substitute notice triggers and requirements
- Credit monitoring obligations
- Federal overlay: HIPAA, GLBA Safeguards Rule, SEC Form 8-K, FCC telecom, CIRCIA
- Notification timeline priority sequencing (strictest clock first)
- Per-state notice content checklists
- Template individual notice and AG filing letters

**Does not:**

- Perform forensic root-cause analysis or determine whether a breach actually occurred
- Resolve GDPR, UK GDPR, or non-US breach notification obligations (see
  `legalcode-breach-severity-assessment` for global triage)
- Provide legal advice or replace qualified counsel
- Promise regulatory outcome or guarantee AG non-enforcement

**Upstream skill**: Use `legalcode-breach-severity-assessment` first to assess harm
likelihood and severity. This skill handles the downstream US notification planning.

---

## Jurisdiction and Governing Law

This skill covers breach notification obligations under the laws of all 50 US states, the
District of Columbia, Puerto Rico, Guam, the US Virgin Islands, and American Samoa. All
50 states have enacted security breach notification statutes. Puerto Rico, Guam, and the
US Virgin Islands have enacted their own laws. American Samoa has limited dedicated
legislation; federal law governs as a floor.

There is **no single comprehensive federal data breach notification law** for general
commercial purposes. Federal sector-specific laws (HIPAA, GLBA Safeguards Rule, FCC rules,
SEC rules) apply as overlays and interact with state law — usually satisfying state law
through compliance, but sometimes imposing stricter requirements.

[JURISDICTION-SPECIFIC] Before finalizing any triage analysis:

1. Verify current statutory text for each implicated state at the official legislative source
2. Confirm current AG guidance on portal or website of each affected state AG
3. Check for statutory amendments enacted after this skill's training cutoff (early 2026)
4. Identify applicable sector-specific overlays (HIPAA, GLBA, banking, telecom)
5. Identify whether any state has a HIPAA or GLBA "safe harbor" that substitutes federal
   compliance for state notification compliance

---

## Interactive Clarification

This skill uses **CLARIFY** blocks at decision points where the user's answer materially
changes the analysis. If context is already provided, skip the question and proceed.
When proceeding without clarification, **state your assumptions explicitly**.

---

## Workflow

### Step 1: Accept the Incident Description

Accept input in any of these formats:

- **Incident description**: narrative of what occurred, when, what data was involved
- **Incident report**: formal IR document, forensic report, or security incident ticket
- **Partial facts**: even preliminary information (data type, rough affected population)

If no incident description is provided, prompt the user to supply one.

### Step 2: Gather Context

**CLARIFY** — Before beginning the triage, ask the user (skip questions already answered):

1. **Entity role**: How is your organization related to the data?
   - Options: Data owner/controller (you collected the data directly), Data processor/vendor
     (you process data on behalf of a client), Both controller and processor for different
     datasets, Unknown
   - _Why this matters_: Processors typically must notify the data owner/controller (not
     individuals directly) within a contractual or statutory deadline; controllers must
     notify individuals and AGs.

2. **Incident state**: What is known about the incident?
   - Options: Suspected (not yet confirmed), Confirmed technical incident (breach of system
     confirmed, but PI exposure unclear), Confirmed PI exposure (know that PI was accessed
     or acquired), Ongoing/active incident, Resolved (investigation complete)
   - _Why this matters_: The legal clock in most states starts on "discovery" or
     "determination," not necessarily on first suspicion. Facts at this stage determine
     whether clocks have started.

3. **Affected data profile**: What categories of data were involved?
   - Options (multiselect): Social Security Numbers / Tax ID numbers, Financial account
     numbers (with access codes/PINs), Payment card data, Driver's license / state ID
     numbers, Medical / health information, Health insurance information, Biometric data
     (fingerprints, retina scans, facial geometry, voice prints), Login credentials
     (username + password or security Q&A), Geolocation data, Passport numbers,
     Government ID numbers, Date of birth (standalone or in combination), Name + address +
     phone (contact info only, no sensitive data)
   - _Why this matters_: State PI definitions vary significantly. Some states trigger on
     SSNs alone; others require a name + one more data element; some now include biometrics
     or login credentials as separate triggers.

4. **Affected population**: How many individuals are affected, and in which states?
   - Options: Known count by state (preferred), Estimated total (no state breakdown),
     Unknown at this time
   - _Why this matters_: AG notification thresholds in most states trigger only above a
     defined resident count (e.g., 500 Florida residents). Without state-by-state counts,
     conservative default is to assume all thresholds are met.

5. **Sector/industry**: Does your organization operate in a regulated sector?
   - Options: Healthcare (HIPAA-covered entity or Business Associate), Financial services
     (GLBA-regulated), Telecom carrier, Publicly traded company (SEC-reporting), Credit
     reporting / data broker, Multiple regulated sectors, None / General commercial
   - _Why this matters_: HIPAA, GLBA, FCC, and SEC rules are federal overlays that may
     preempt or supplement state notification obligations.

**Default assumptions** (if user cannot answer): Entity is a controller; incident is
confirmed PI exposure; data includes SSNs and financial account numbers; total affected
population in each state is unknown (assume all AG thresholds are met); entity is general
commercial (no sector-specific overlay). **State these assumptions explicitly** and note
they represent a conservative, over-notification posture.

### Step 3: Load the Breach Response Playbook

If the organization has a pre-existing breach response playbook, attempt to load it:

1. Ask the user to specify the playbook location (file path, URL, or paste content)
2. If provided, extract: incident classification thresholds, AG contact information,
   pre-approved notice templates, escalation chains, credit monitoring vendor contracts,
   law enforcement liaison contacts
3. If no playbook: proceed with the statutory defaults and mark triage outputs as
   requiring playbook alignment before dispatch

**CLARIFY** — Does your organization have a breach response playbook?

- Options: Yes — I'll provide it now, Yes — it exists but is not accessible, No — use
  statutory defaults, Not sure
- _Why this matters_: A pre-approved playbook with AG pre-notification contacts and
  approved language can dramatically reduce dispatch time.

### Step 4: Federal Overlay Assessment

Before analyzing state law, determine which federal regimes apply. Federal law does not
generally preempt state breach notification law (each applies independently), but federal
compliance may satisfy state notice requirements in some states that recognize HIPAA or
GLBA compliance as a safe harbor.

#### 4a. HIPAA Breach Notification Rule (45 CFR §§ 164.400–164.414)

**Applies if**: The entity is a HIPAA-covered entity (healthcare provider, health plan,
healthcare clearinghouse) or a Business Associate that handles Protected Health Information
(PHI).

**Trigger**: Impermissible use or disclosure of **unsecured PHI** is presumed to be a
notifiable breach unless the covered entity demonstrates a low probability of compromise
via a 4-factor risk assessment.

**4-Factor Risk Assessment** (rebutting presumption of breach):

1. Nature and extent of PHI involved (identifiers, clinical severity, financial data)
2. Identity of the unauthorized person — likelihood they could use the PHI harmfully
3. Whether PHI was actually acquired or viewed (vs. merely accessible)
4. Extent to which risk has been mitigated (e.g., recipient returned or destroyed data)

**Safe Harbor (No Notification Required):**

- PHI encrypted using NIST-approved methods (FIPS 140-2; NIST SP 800-111 for at-rest;
  SP 800-52/TLS for in-transit) AND the decryption key was not also compromised
- PHI destroyed so it cannot reasonably be reconstructed
- Applies at time of breach, not at time of discovery

**Notification Timelines:**
| Recipient | Timing | Notes |
|-----------|--------|-------|
| Individuals | Without unreasonable delay; no later than 60 calendar days after discovery | First-class mail or email (if agreed); substitute notice if contact info insufficient |
| HHS (500+ in a state) | No later than 60 days after breach discovery | Simultaneous with individual notice via HHS web portal |
| HHS (<500 in a state) | Annual log; no later than 60 days after year-end | Maintain log; submit annually |
| Prominent media (500+ in same state) | No later than 60 days after discovery | "Prominent media outlets" in the state where affected residents live |

**Business Associate Obligation**: Must notify covered entity within 60 days of discovery.
The covered entity's 60-day clock starts from when the Business Associate discovers the
breach (not when the covered entity learns of it).

**Notice Content Requirements** (45 CFR § 164.404(c)):

- [ ] Brief description of the breach, including date (if known)
- [ ] Description of PHI involved (types, not individual records)
- [ ] Steps individuals should take to protect themselves
- [ ] Brief description of investigation/mitigation steps
- [ ] Contact information: toll-free number, email, website, or postal address

**HIPAA as State Safe Harbor**: Several states (including Arkansas, Georgia, Louisiana,
New Mexico, Tennessee, and others [VERIFY]) provide that entities subject to and complying
with HIPAA breach notification requirements are deemed compliant with state law. If
applicable, note this and mark for counsel confirmation. [CHECK CURRENCY]

#### 4b. GLBA Safeguards Rule — FTC Breach Notification (16 CFR Part 314)

**Applies if**: The entity is a non-banking financial institution subject to the FTC's
GLBA Safeguards Rule — including mortgage brokers, auto dealers, payday lenders,
investment advisors not subject to SEC, and other non-bank financial services companies.
(Banking institutions have separate requirements under OCC, FDIC, and Federal Reserve rules;
New York banking entities face NYDFS 72-hour requirements [VERIFY].)

**Trigger**: A "notification event" — unauthorized acquisition of unencrypted customer
information of at least **500 consumers**. No risk-of-harm threshold; all unauthorized
acquisitions meeting the threshold must be reported even if no harm is apparent.

**Timeline**: As soon as possible; **no later than 30 days** after the date the institution
"discovers" the notification event. Discovery = first day any employee, officer, or agent
of the institution knows of the event.

**Notification Recipient**: FTC, via online portal (ftc.gov/datasecurity). Notification is
made public in an FTC database.

**Notice Content** (16 CFR § 314.9):

- [ ] Name and contact information of the reporting financial institution
- [ ] Types of information involved
- [ ] Date or date range of the notification event (if known)
- [ ] Number of consumers affected or potentially affected
- [ ] General description of the event
- [ ] Whether law enforcement has indicated public notification would impede investigation

**Law Enforcement Delay**: A supervisory agency or law enforcement may request delayed
notification. The delay is reasonable for the period requested by law enforcement.

#### 4c. SEC Cybersecurity Incident Disclosure — Form 8-K Item 1.05

**Applies if**: The entity is an SEC-reporting public company (domestic registrant or
foreign private issuer filing Form 6-K equivalents).

**Trigger**: A cybersecurity incident that the company has **determined to be material**.
Materiality = substantial likelihood that a reasonable investor would consider the
information significant in making an investment decision.

**Timeline**: **4 business days** from the date the materiality determination is made.
If law enforcement determines disclosure would present national security or public safety
risk, the company may request a delay (up to additional 60 days, via written notice to SEC).

**Notice Content**: Nature, scope, and timing of the incident; actual or reasonably likely
material impact on financial condition and results of operations.

**Important**: Item 1.05 is for material incidents only. Non-material incidents (or those
for which materiality has not yet been determined) may be reported under Item 8.01. If a
subsequently-disclosed incident is later determined to be material, file Item 1.05 within 4
business days of that determination.

#### 4d. FCC Data Breach Notification Rules (Telecom Carriers)

**Applies if**: The entity is a telecommunications carrier subject to FCC jurisdiction.

**Rules**: Updated 2024 (47 CFR Part 64); upheld by the Sixth Circuit in August 2025.

**Scope**: Breaches of any customer personally identifiable information (PII) or customer
proprietary network information (CPNI), including both intentional and inadvertent breaches.

**Notification Timelines:**
| Recipient | Timing | Notes |
|-----------|--------|-------|
| Federal agencies (FCC, FBI, Secret Service) | 7 business days after reasonable determination | Per-breach notification; 500+ customer threshold |
| Customers | No later than 30 days after notifying federal agencies; without unreasonable delay | |
| Annual report | Regardless of threshold | All breaches; describe in annual report to FCC |

**Exceptions**:

- No customer notification required if carrier reasonably determines no harm is reasonably
  likely to occur
- No notification required if breach involves only encrypted data and the carrier confirms
  the encryption key was not compromised

#### 4e. CIRCIA — Cyber Incident Reporting for Critical Infrastructure

**Applies if**: The entity is a "covered entity" in one of the 16 critical infrastructure
sectors (energy, water, transportation, financial, healthcare, defense industrial base,
etc.) as defined by CISA.

**Status as of early 2026**: CISA published proposed rules in March 2024. Final regulations
were not fully effective at this skill's training cutoff. Monitor CISA's rulemaking portal
for final rule effective dates. [CHECK CURRENCY]

**Proposed requirements** (subject to change):

- **72 hours** for covered entities to report significant cyber incidents to CISA
- **24 hours** for ransom payment reports
- **Supplemental reports** if new material information emerges

**Action**: If the entity operates critical infrastructure, flag CIRCIA applicability for
legal monitoring and engage specialized counsel. Include a [CHECK CURRENCY] marker in all
CIRCIA-related analysis. Do not treat proposed rules as final.

#### 4f. Other Federal Sector-Specific Rules [VERIFY]

- **Banking institutions** (OCC/FDIC/Federal Reserve): Notification to banking regulator
  within 36 hours of a "computer-security incident" (banking supervision terminology);
  service providers notify banking clients ASAP [VERIFY timeline]
- **FTC Health Breach Notification Rule** (16 CFR Part 318): Applies to vendors of personal
  health records and related entities not covered by HIPAA; 60 days to individuals, 10
  business days to FTC for 500+ [VERIFY]
- **FERPA** (educational records): No specific breach notification rule but unauthorized
  disclosure may trigger reporting; sector-specific analysis required [VERIFY]
- **NYDFS Cybersecurity Regulation** (23 NYCRR 500): 72-hour notification to NYDFS for
  cybersecurity events meeting specific criteria; applies to NYDFS-regulated entities [VERIFY]

### Step 5: Multi-State Applicability Matrix

Map the incident to each jurisdiction's breach notification statute. For each state:

1. Confirm that **personal information was involved** (PI definition met)
2. Confirm that a **breach occurred** (breach definition met)
3. Determine whether a **risk of harm threshold** applies and whether it is met
4. Determine whether a **safe harbor** exempts notification

#### 5a. Personal Information Definition — Key Categories

Most state breach notification laws define PI as a person's **first name or first initial
and last name** combined with one or more of the following "data elements":

| Category                                    | Common Abbreviation | States That Include It                              |
| ------------------------------------------- | ------------------- | --------------------------------------------------- |
| Social Security Number                      | SSN                 | All 50 states + DC + territories                    |
| Driver's license or state ID number         | DL                  | All 50 states + DC + territories                    |
| Financial account number + access code/PIN  | Fin Acct            | All 50 states + DC + territories                    |
| Payment card number + security code         | CC                  | Most states (some require separate tracking)        |
| Medical/health information                  | Med                 | ~40+ states [VERIFY count]                          |
| Health insurance information                | HI                  | ~30+ states [VERIFY count]                          |
| Biometric data                              | Bio                 | ~25+ states — growing category [VERIFY count]       |
| Username / email + password or security Q&A | Creds               | ~20+ states — rapidly expanding [VERIFY count]      |
| Geolocation data (precise)                  | Geo                 | ~10+ states [VERIFY count]                          |
| Passport number                             | Pass                | ~15+ states [VERIFY count]                          |
| Date of birth (DOB) alone                   | DOB                 | Fewer states; usually requires combination [VERIFY] |
| Tax ID / Individual Taxpayer ID             | TIN                 | ~10+ states [VERIFY count]                          |
| Military ID                                 | Mil                 | Select states [VERIFY]                              |
| DNA / genetic data                          | DNA                 | Select states [VERIFY]                              |

**Exception: Some states define PI without requiring name combination.** California (Civ.
Code § 1798.82) defines PI to include username/password combos and medical/health info
**without requiring name combination** when the data alone is sufficient for identity theft.
[VERIFY current CA statutory text after SB 446]

**Standalone triggers (no name required in some states)**: Usernames alone, SSNs alone,
or payment card numbers alone in specific high-risk contexts [VERIFY per-state].

#### 5b. Breach Definition — Unauthorized Access vs. Acquisition

The breach trigger varies by state:

| Definition Type                                                   | States (Select Examples)              | Impact                                                        |
| ----------------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------- |
| **Unauthorized acquisition** (stronger standard for notification) | Many older statutes                   | Must show data was actually taken, not just accessed          |
| **Unauthorized access** (lower standard — mere access triggers)   | CA, CO, FL, NY, WA (SB/HB amendments) | Access alone can trigger, even without confirmed exfiltration |
| **Access + compromise of security or confidentiality**            | VA § 18.2-186.6                       | Requires that access compromises security/confidentiality     |
| **Unauthorized access OR acquisition**                            | Most modern statutes                  | Broader trigger — either suffices                             |

**Operational implication**: When "access" is the trigger (not "acquisition"), inability to
confirm exfiltration does not eliminate the notification obligation in those states.

#### 5c. Risk of Harm Threshold

Approximately half of states include a "risk of harm" or "likelihood of harm" threshold —
notification is only required if the breach creates a material risk of harm (typically
identity theft or financial harm) to the affected individuals. Key examples:

| State       | Threshold Language                                                                                                                                       | Documentation Required                       |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Alaska      | "Reasonable likelihood that harm to consumers has or will result" — no notification if AG notified in writing of no-harm determination                   | Written, maintained 5 years                  |
| Arizona     | Breach "does not materially compromise the security or confidentiality" — no notification required                                                       | Investigation + law enforcement consultation |
| Connecticut | After appropriate investigation + law enforcement consultation, breach "likely will not result in harm"                                                  | Appropriate investigation documented         |
| Delaware    | "Reasonable likelihood that harm to consumers... has resulted or will result" — no notification if AG notified in writing                                | Written, maintained 5 years                  |
| Florida     | After investigation, covered entity "reasonably determines that breach has not and will not likely result in identity theft or any other financial harm" | Written, maintained 5 years                  |
| Iowa        | Harm threshold; entity may decide not to notify                                                                                                          | Investigation required [VERIFY]              |
| Louisiana   | Risk of harm assessment [VERIFY]                                                                                                                         | [VERIFY]                                     |
| Nebraska    | Risk of harm assessment [VERIFY]                                                                                                                         | [VERIFY]                                     |
| Wisconsin   | Potential harm standard [VERIFY]                                                                                                                         | [VERIFY]                                     |

**Conservative default**: If the investigation cannot affirmatively rule out harm, assume
notification is required. The risk of harm threshold is an **exception** to notification,
not a prerequisite for it. The burden of establishing no-harm is on the entity.

**Documentation**: Where a no-harm determination is made, document it thoroughly and
retain for the statutory period (usually 5 years). Some states require written notice to
the AG of the no-harm determination.

### Step 6: State-by-State Breach Notification Matrix

Build the following matrix for all states where affected residents live. Apply conservative
defaults where facts are uncertain.

The table below provides statutory baselines for all 50 states + DC + territories as of
early 2026. **[CHECK CURRENCY] for all entries — state laws are amended frequently.**

| Jurisdiction             | Key Statute Citation                                                                  | Indiv. Notice Deadline                                                                                                 | AG Notification                                                                 | AG Threshold                                                                  | Safe Harbor                                                                                    | Credit Monitoring                                              | Risk of Harm Threshold                                                             | PI Categories                                                                                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Alabama**              | Ala. Code § 8-38-1 et seq.                                                            | Without undue delay                                                                                                    | Required                                                                        | >1 resident                                                                   | Encrypted + key not compromised                                                                | Not specified                                                  | Yes [VERIFY]                                                                       | SSN, DL, financial, medical, health insurance, email+password [VERIFY]                                                                                    |
| **Alaska**               | Alaska Stat. § 45.48.010 et seq.                                                      | Expedient time, without unreasonable delay                                                                             | Required (if harm, notify residents; if no harm, notify AG)                     | None specified                                                                | Encrypted + key not compromised; good faith employee acquisition                               | Not specified                                                  | Yes — written AG notice if no harm                                                 | SSN, DL, financial [VERIFY full list]                                                                                                                     |
| **Arizona**              | Ariz. Rev. Stat. § 44-7501                                                            | Expedient time possible                                                                                                | Required                                                                        | 1,000 residents or if breach involves 100 residents + notification cost >$50K | Encrypted + key not compromised; good faith employee acquisition                               | Not specified                                                  | Yes — investigation + law enforcement                                              | SSN, DL, financial, medical, passwords [VERIFY]                                                                                                           |
| **Arkansas**             | Ark. Code § 4-110-108                                                                 | Within 45 days after discovery                                                                                         | Required [VERIFY]                                                               | [VERIFY threshold]                                                            | Encrypted; good faith employee; HIPAA safe harbor [VERIFY]                                     | Not specified                                                  | Yes — 45 days or determination, whichever first                                    | SSN, DL, financial, medical [VERIFY]                                                                                                                      |
| **California**           | Cal. Civ. Code § 1798.82; 1798.29                                                     | 30 calendar days (SB 446, eff. Jan 1, 2026; prior = "most expedient time")                                             | Yes — notify AG within 15 days of notifying individuals; sample notice required | >500 California residents                                                     | Encrypted + key not compromised; good faith employee; redacted                                 | Not specified                                                  | No — notification required without harm assessment                                 | SSN, DL, financial, medical, health insurance, passwords, biometric, geolocation, passport, TIN, name+DOB+address alone [VERIFY current list post-SB 446] |
| **Colorado**             | Colo. Rev. Stat. § 6-1-716                                                            | 30 days from determination                                                                                             | Required for 500+                                                               | >500 residents                                                                | Encrypted + key not compromised; good faith employee                                           | 12 months free credit monitoring if SSN breached [VERIFY]      | No                                                                                 | SSN, DL, financial, medical, biometric, passwords, student ID, tax ID [VERIFY]                                                                            |
| **Connecticut**          | Conn. Gen. Stat. § 36a-701b                                                           | Within 60 days of discovery [VERIFY — some sources report 60-day deadline]                                             | Required                                                                        | No threshold specified [VERIFY]                                               | Encrypted; cybersecurity safe harbor (§ 42-516); good faith employee                           | 24 months identity theft protection if SSN breached [VERIFY]   | Yes — appropriate investigation + law enforcement                                  | SSN, DL, financial, medical, passwords, biometric [VERIFY]                                                                                                |
| **Delaware**             | Del. Code tit. 6, § 12B-101 et seq.                                                   | Within 60 days after determination                                                                                     | Required                                                                        | >500 residents                                                                | Encrypted + key not compromised; good faith employee                                           | Identity theft protection required for 1+ year if SSN breached | Yes — written AG notice if no harm                                                 | SSN, DL, financial, medical, passwords, biometric, geolocation [VERIFY]                                                                                   |
| **Florida**              | Fla. Stat. § 501.171                                                                  | 30 days from determination; 15-day extension available with good cause                                                 | Required simultaneously                                                         | >500 residents                                                                | Encrypted; redacted; good faith employee                                                       | Offer if services provided (notice must describe)              | Yes — documented determination                                                     | SSN, DL, financial, medical, email+password, biometric [VERIFY]                                                                                           |
| **Georgia**              | Ga. Code Ann. § 10-1-912                                                              | "Expedient time possible, without unreasonable delay"                                                                  | Not required [VERIFY]                                                           | N/A                                                                           | Encrypted; good faith employee                                                                 | Not specified                                                  | Yes [VERIFY]                                                                       | SSN, DL, financial [VERIFY full list]                                                                                                                     |
| **Hawaii**               | Haw. Rev. Stat. § 487N-2                                                              | "Expedient time possible"                                                                                              | Required                                                                        | No threshold [VERIFY]                                                         | Encrypted + key not compromised; good faith employee                                           | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical, passwords [VERIFY]                                                                                                           |
| **Idaho**                | Idaho Code § 28-51-101 et seq.                                                        | "Most expedient time possible, without unreasonable delay"                                                             | Required                                                                        | No threshold [VERIFY]                                                         | Encrypted + key not compromised; good faith employee                                           | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical [VERIFY]                                                                                                                      |
| **Illinois**             | 815 ILCS 530/10                                                                       | "Most expedient time possible, without unreasonable delay"                                                             | Required                                                                        | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical, biometric (BIPA separately covers biometric collection) [VERIFY]                                                             |
| **Indiana**              | Ind. Code § 24-4.9-3-1 et seq.                                                        | "Most expedient time possible, without unreasonable delay"                                                             | Required                                                                        | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical [VERIFY]                                                                                                                      |
| **Iowa**                 | Iowa Code § 715C.2                                                                    | "Most expedient time possible, without unreasonable delay"                                                             | Required [VERIFY]                                                               | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | Yes [VERIFY]                                                                       | SSN, DL, financial, medical [VERIFY]                                                                                                                      |
| **Kansas**               | Kan. Stat. Ann. § 50-7a01 et seq.                                                     | "Most expedient time possible, without unreasonable delay"                                                             | Not required [VERIFY]                                                           | N/A                                                                           | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial [VERIFY]                                                                                                                               |
| **Kentucky**             | Ky. Rev. Stat. Ann. § 365.732                                                         | "Most expedient time possible, without unreasonable delay"                                                             | Not required [VERIFY]                                                           | N/A                                                                           | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial [VERIFY]                                                                                                                               |
| **Louisiana**            | La. Rev. Stat. Ann. § 51:3071 et seq.                                                 | Within 60 days after discovery                                                                                         | Required                                                                        | No threshold [VERIFY]                                                         | Encrypted; good faith employee; HIPAA safe harbor [VERIFY]                                     | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical [VERIFY]                                                                                                                      |
| **Maine**                | Me. Rev. Stat. tit. 10, § 1347 et seq.                                                | Within 30 days of determination [VERIFY — some sources report 30-day deadline]                                         | Required                                                                        | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical, passwords [VERIFY]                                                                                                           |
| **Maryland**             | Md. Code, Com. Law § 14-3501 et seq.                                                  | "Most expedient time possible, without unreasonable delay"                                                             | Required                                                                        | No threshold [VERIFY]                                                         | Encrypted + key not compromised; good faith employee                                           | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical, passwords [VERIFY]                                                                                                           |
| **Massachusetts**        | Mass. Gen. Laws ch. 93H, § 3                                                          | "As soon as reasonably possible, without unreasonable delay"                                                           | Required — simultaneously to AG and OCABR                                       | No threshold                                                                  | Encrypted; good faith employee                                                                 | 18 months free credit monitoring if SSN breached [VERIFY]      | No                                                                                 | SSN, DL, financial, medical [VERIFY]                                                                                                                      |
| **Michigan**             | Mich. Comp. Laws § 445.72 et seq.                                                     | "Most expedient time possible, without unreasonable delay"                                                             | Not required [VERIFY]                                                           | N/A                                                                           | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical [VERIFY]                                                                                                                      |
| **Minnesota**            | Minn. Stat. § 325E.61 et seq.                                                         | "Most expedient time possible"                                                                                         | Required [VERIFY]                                                               | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical [VERIFY]                                                                                                                      |
| **Mississippi**          | Miss. Code Ann. § 75-24-29                                                            | Within 45 days of discovery                                                                                            | Required [VERIFY]                                                               | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | Yes [VERIFY]                                                                       | SSN, DL, financial [VERIFY]                                                                                                                               |
| **Missouri**             | Mo. Rev. Stat. § 407.1500                                                             | "Most expedient time possible, without unreasonable delay"                                                             | Required [VERIFY]                                                               | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical [VERIFY]                                                                                                                      |
| **Montana**              | Mont. Code Ann. § 30-14-1704                                                          | "Most expedient time possible, without unreasonable delay"                                                             | Required [VERIFY]                                                               | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical [VERIFY]                                                                                                                      |
| **Nebraska**             | Neb. Rev. Stat. § 87-801 et seq.                                                      | "Most expedient time possible, without unreasonable delay"                                                             | Required [VERIFY]                                                               | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | Yes [VERIFY]                                                                       | SSN, DL, financial [VERIFY]                                                                                                                               |
| **Nevada**               | Nev. Rev. Stat. § 603A.220 et seq.                                                    | "Most expedient time possible, without unreasonable delay"                                                             | Required [VERIFY]                                                               | No threshold [VERIFY]                                                         | Encrypted; good faith employee; HIPAA safe harbor [VERIFY]; PCI DSS for payment cards [VERIFY] | 12 months if SSN breached [VERIFY]                             | No [VERIFY]                                                                        | SSN, DL, financial, medical, email+password [VERIFY]                                                                                                      |
| **New Hampshire**        | N.H. Rev. Stat. Ann. § 359-C:19 et seq.                                               | "Most expedient time possible, without unreasonable delay"                                                             | Required                                                                        | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | Yes [VERIFY]                                                                       | SSN, DL, financial, medical [VERIFY]                                                                                                                      |
| **New Jersey**           | N.J. Stat. Ann. § 56:8-161 et seq.                                                    | "Most expedient time possible, without unreasonable delay"                                                             | Required                                                                        | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical, email+password [VERIFY]                                                                                                      |
| **New Mexico**           | N.M. Stat. Ann. § 57-12C-1 et seq.                                                    | Within 45 calendar days after discovery or determination                                                               | Required                                                                        | >1,000 residents                                                              | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical, biometric, passwords [VERIFY]                                                                                                |
| **New York**             | N.Y. Gen. Bus. Law § 899-aa (SHIELD Act, amended Dec 2024)                            | 30 days from discovery (amendment eff. late 2024; prior = "most expedient time")                                       | Required — simultaneously                                                       | No threshold                                                                  | Encrypted; good faith employee                                                                 | Not specified                                                  | No                                                                                 | SSN, DL, financial, medical, biometric, email+password, credit/debit card + security code [VERIFY current list]                                           |
| **North Carolina**       | N.C. Gen. Stat. § 75-65                                                               | "Expedient time possible, without unreasonable delay"                                                                  | Required                                                                        | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | Yes [VERIFY]                                                                       | SSN, DL, financial, medical, passwords [VERIFY]                                                                                                           |
| **North Dakota**         | N.D. Cent. Code § 51-30-01 et seq.                                                    | "Most expedient time possible, without unreasonable delay"                                                             | Required                                                                        | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical [VERIFY]                                                                                                                      |
| **Ohio**                 | Ohio Rev. Code Ann. § 1347.12                                                         | "Most expedient time possible, without unreasonable delay"                                                             | Not required [VERIFY]                                                           | N/A                                                                           | Encrypted; good faith employee; NIST/ISO/PCI safe harbor for litigation only (§ 1354.02)       | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical, passwords [VERIFY]                                                                                                           |
| **Oklahoma**             | Okla. Stat. tit. 74, § 3113.1 et seq. (SB 626 effective Jan 1, 2026 — major revision) | Under revised law: within 45 days [VERIFY post-SB 626]                                                                 | Required [VERIFY]                                                               | No threshold [VERIFY]                                                         | Encrypted; good faith employee [VERIFY SB 626 terms]                                           | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial [VERIFY SB 626 additions]                                                                                                              |
| **Oregon**               | Or. Rev. Stat. § 646A.600 et seq.                                                     | Within 45 days after discovery                                                                                         | Required                                                                        | >250 residents                                                                | Encrypted + key not compromised; good faith employee                                           | Not specified                                                  | No                                                                                 | SSN, DL, financial, medical, biometric, passwords, geographic location [VERIFY]                                                                           |
| **Pennsylvania**         | 73 Pa. Stat. §§ 2301–2329                                                             | "Most expedient time possible, without unreasonable delay"                                                             | Required                                                                        | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical, biometric, passwords [VERIFY]                                                                                                |
| **Rhode Island**         | R.I. Gen. Laws § 11-49.3 et seq.                                                      | Within 45 calendar days after discovery                                                                                | Required                                                                        | No threshold [VERIFY]                                                         | Encrypted; good faith employee; HIPAA safe harbor [VERIFY]                                     | 18 months if SSN breached                                      | No [VERIFY]                                                                        | SSN, DL, financial, medical, email+password, biometric [VERIFY]                                                                                           |
| **South Carolina**       | S.C. Code Ann. § 39-1-90                                                              | Within 60 days of discovery                                                                                            | Required [VERIFY]                                                               | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical [VERIFY]                                                                                                                      |
| **South Dakota**         | S.D. Codified Laws § 22-40-20 et seq.                                                 | Within 60 days of discovery                                                                                            | Required                                                                        | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical [VERIFY]                                                                                                                      |
| **Tennessee**            | Tenn. Code Ann. § 47-18-2107                                                          | "Most expedient time possible, without unreasonable delay"                                                             | Not required [VERIFY]                                                           | N/A                                                                           | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial [VERIFY]                                                                                                                               |
| **Texas**                | Tex. Bus. & Com. Code § 521.053 (amended by SB 768, eff. Sept 1, 2023)                | 60 calendar days for individuals [VERIFY — some sources report 30 days; verify SB 768 current text]                    | Required                                                                        | >250 Texas residents (post-SB 768) [VERIFY]                                   | Encrypted; good faith employee; HIPAA safe harbor [VERIFY]                                     | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical, biometric, passwords, government ID [VERIFY]                                                                                 |
| **Utah**                 | Utah Code Ann. § 13-44-101 et seq.                                                    | Within 30 days of discovery                                                                                            | Required [VERIFY]                                                               | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical, passwords [VERIFY]                                                                                                           |
| **Vermont**              | Vt. Stat. Ann. tit. 9, § 2430 et seq.                                                 | "Most expedient time possible, without unreasonable delay"                                                             | Required — within 14 days of notifying individuals                              | No threshold [VERIFY]                                                         | Encrypted; good faith employee; HIPAA/GLBA safe harbor [VERIFY]                                | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial, medical, passwords, biometric, health insurance [VERIFY]                                                                              |
| **Virginia**             | Va. Code Ann. § 18.2-186.6                                                            | "Without unreasonable delay"                                                                                           | Required — simultaneously                                                       | >1,000 residents notified at one time                                         | Encrypted + unredacted data not acquired; good faith employee                                  | Not specified                                                  | Yes — risk/likelihood of identity theft or fraud required for notification trigger | SSN, DL, financial [VERIFY full list]                                                                                                                     |
| **Washington**           | Wash. Rev. Code § 19.255.010                                                          | Within 30 calendar days after discovery                                                                                | Required                                                                        | >500 residents                                                                | Encrypted + key not compromised; good faith employee                                           | Not specified                                                  | Yes — "not reasonably likely to subject consumers to a risk of harm" [VERIFY]      | SSN, DL, financial, medical, biometric, passwords, full DOB [VERIFY]                                                                                      |
| **West Virginia**        | W. Va. Code § 46A-2A-101 et seq.                                                      | "Most expedient time possible, without unreasonable delay"                                                             | Not required [VERIFY]                                                           | N/A                                                                           | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial [VERIFY]                                                                                                                               |
| **Wisconsin**            | Wis. Stat. § 134.98                                                                   | "Most expedient time possible, without unreasonable delay"                                                             | Not required [VERIFY]                                                           | N/A                                                                           | Encrypted; good faith employee                                                                 | Not specified                                                  | Yes [VERIFY]                                                                       | SSN, DL, financial [VERIFY]                                                                                                                               |
| **Wyoming**              | Wyo. Stat. Ann. § 40-12-502 et seq.                                                   | "Most expedient time possible, without unreasonable delay"                                                             | Required [VERIFY]                                                               | No threshold [VERIFY]                                                         | Encrypted; good faith employee                                                                 | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial [VERIFY]                                                                                                                               |
| **District of Columbia** | D.C. Code § 28-3851 et seq.                                                           | "Most expedient time possible, without unreasonable delay"                                                             | Required                                                                        | >50 DC residents [VERIFY]                                                     | Encrypted; good faith employee                                                                 | 18 months identity theft protection if SSN breached [VERIFY]   | No [VERIFY]                                                                        | SSN, DL, financial, medical, biometric, passwords [VERIFY]                                                                                                |
| **Puerto Rico**          | P.R. Laws tit. 10, § 4051 et seq. (Citizen Information on Data Banks Security Act)    | Most expedient time for individuals; Department of Consumer Affairs: **within 10 non-extendable days** after discovery | Required — 10 days to Department of Consumer Affairs                            | No threshold                                                                  | Encrypted [VERIFY]                                                                             | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial [VERIFY]                                                                                                                               |
| **Guam**                 | Guam Code Ann. tit. 9, § 48 et seq. [VERIFY citation]                                 | Most expedient time possible [VERIFY]                                                                                  | Required [VERIFY]                                                               | No threshold [VERIFY]                                                         | Encrypted; own-procedure compliance [VERIFY]                                                   | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial [VERIFY]                                                                                                                               |
| **US Virgin Islands**    | V.I. Code Ann. tit. 14, § 2208 et seq. [VERIFY citation]                              | Most expedient time possible [VERIFY]                                                                                  | Required [VERIFY]                                                               | No threshold [VERIFY]                                                         | Encrypted [VERIFY]                                                                             | Not specified                                                  | No [VERIFY]                                                                        | SSN, DL, financial [VERIFY]                                                                                                                               |
| **American Samoa**       | Limited specific legislation; federal law governs as floor [VERIFY]                   | Federal standards apply [VERIFY]                                                                                       | Federal regulators [VERIFY]                                                     | Per federal law                                                               | Federal safe harbors                                                                           | Per federal law                                                | Per federal law                                                                    | Per federal law [VERIFY]                                                                                                                                  |

---

### Step 7: Deep Dives — Highest-Complexity States

Apply the following jurisdiction-specific analysis for states with unusual requirements,
strict deadlines, or significant enforcement activity.

#### California (Cal. Civ. Code § 1798.82 / 1798.29)

**Why it matters**: Largest state economy; most active AG enforcement; most expansive PI
definition; private right of action under CCPA for certain breaches.

**Key requirements:**

- **Individual notice**: 30 calendar days from discovery (SB 446, effective January 1, 2026;
  prior law: "most expedient time possible, without unreasonable delay")
- **AG notice**: Notify California AG within 15 calendar days of notifying individuals if
  breach affects 500+ California residents; provide a sample copy of the notice
- **PI definition**: Among the broadest — includes SSN, DL, account numbers, medical info,
  health insurance, biometric, email+password combos, geolocation, passport numbers, tax
  IDs, and name combined with DOB + address [VERIFY current list after SB 446]
- **CCPA overlay**: Unauthorized access and disclosure, theft, or disclosure of personal
  information defined under the CCPA (broader than § 1798.82 PI) can trigger a private
  civil action by affected individuals (not a notice obligation, but a litigation risk)
- **Format requirements**: Notice must be written in plain language; title must include
  "Notice of Data Breach"; specific sections required: list of data types, timeline,
  what happened, what business is doing, what affected individuals can do, contact
  information
- **Electronic notice**: Permitted only if primary relationship is electronic, and following
  electronic consent requirements
- **Encryption safe harbor**: Data encrypted AND decryption key not also compromised

[JURISDICTION-SPECIFIC] Verify updated California AG guidance after SB 446 implementation.
Confirm whether § 1798.29 (government agencies) or § 1798.82 (businesses) applies. The 15-day
AG notification clock runs from the date individual notices are dispatched, not from discovery.

#### New York (N.Y. Gen. Bus. Law § 899-aa; NY SHIELD Act)

**Why it matters**: 2024 amendment created firm 30-day deadline; SHIELD Act expanded PI
definition and security program requirements; significant financial services overlay (NYDFS).

**Key requirements:**

- **Individual notice**: 30 days from discovery (amendment signed December 24, 2024)
- **AG notice**: Required simultaneously with individual notice; sample notice to AG
- **Private sector and government**: Both covered
- **PI definition (post-SHIELD)**: SSN, DL, account numbers, biometric, email+password,
  credit/debit card number + security code, date of birth, mother's maiden name, and
  others [VERIFY current list]
- **SHIELD Act**: Requires "reasonable security" program (size-appropriate); breach of
  reasonable security triggers notification analysis
- **NYDFS overlay** (23 NYCRR Part 500): NYDFS-regulated financial services entities must
  notify the Superintendent of Financial Services within 72 hours of a cybersecurity event.
  This runs in parallel with — not instead of — § 899-aa obligations. [VERIFY]

[JURISDICTION-SPECIFIC] Verify whether the 30-day deadline applies to all covered entities
or only those subject to specific sectors under NY law. The NYDFS 72-hour clock is separate
and applies only to NYDFS-regulated entities.

#### Florida (Fla. Stat. § 501.171)

**Why it matters**: Strict 30-day deadline with monetary penalties ($1,000/day for first
30 days, then $50,000/30-day period); credit monitoring content required in notice.

**Key requirements:**

- **Individual notice**: 30 days from determination; 15-day extension available with written
  good cause submitted to AG within 30 days
- **AG notice**: 30 days from determination; required if 500+ Florida residents affected;
  simultaneous with individual notice
- **Penalties**: $1,000/day for each day of non-disclosure up to 30 days; then $50,000
  per each 30-day period or portion thereafter; maximum penalty $500,000 per breach
- **AG filing content**: Incident description, type of PI involved, number of affected
  Floridians, steps taken (including notice to individuals if applicable), name/contact of
  reporting entity
- **Credit monitoring**: Notice must describe any services offered (at no charge) to
  affected individuals; does not mandate credit monitoring but mandates description if
  offered
- **Risk of harm**: After appropriate investigation and law enforcement consultation, if
  entity reasonably determines no harm risk — no notification required; must document in
  writing and maintain for 5 years
- **30-day extension**: Submit written good cause to Florida AG within 30 days; extension
  of 15 additional days granted

[JURISDICTION-SPECIFIC] Florida's penalty structure is among the strictest in the US.
Engage Florida counsel early. The 15-day extension must be requested before the 30-day
clock expires, not after.

#### Massachusetts (Mass. Gen. Laws ch. 93H; 201 CMR 17.00)

**Why it matters**: No fixed deadline but requires WISP (written information security
program); notice to AG AND Office of Consumer Affairs and Business Regulation (OCABR);
expansive content requirements.

**Key requirements:**

- **Individual notice**: "As soon as reasonably possible, without unreasonable delay";
  no fixed calendar-day deadline
- **AG notice**: Simultaneously to AG and OCABR; no threshold for filing
- **Content to AG**: Nature of breach, number of residents affected, name/address of
  reporting entity, name/title/relationship of reporting person, type of entity, known
  responsible party, type of PI compromised; plus sample consumer notice
- **WISP requirement**: Entities owning/licensing PI of MA residents must have a Written
  Information Security Plan; breach without a WISP is a separate regulatory violation
- **201 CMR 17.00**: Comprehensive security regulation prescribing technical and
  administrative security standards; non-compliance is independent violation

[JURISDICTION-SPECIFIC] Massachusetts's AG is active in breach enforcement. The WISP
requirement means breach notification triggers a secondary review of whether a compliant
WISP was in place. Engage MA counsel for incidents affecting large numbers of MA residents.

#### Texas (Tex. Bus. & Com. Code § 521.053, amended by SB 768 eff. Sept 1, 2023)

**Why it matters**: Post-SB 768 two-track requirement — individual notice and AG notice
have different deadlines; AG threshold tightened to 250 residents; expansive PI definition.

**Key requirements:**

- **Individual notice**: Within 60 calendar days from determination that PI was or is
  reasonably believed to have been acquired [VERIFY — some sources report 30 days;
  verify SB 768 current text against official sources]
- **AG notice**: Within 30 days if 250+ Texas residents affected (SB 768 tightened from
  prior threshold; verify current count) [VERIFY]
- **Consumer credit reporting agencies**: Notify consumer reporting agencies if 10,000+
  Texans affected [VERIFY]
- **HIPAA safe harbor**: HIPAA-covered entities complying with HIPAA Breach Notification
  Rule may satisfy Texas requirements [VERIFY current status]
- **Risk of harm**: No statutory risk of harm threshold [VERIFY]
- **Texas Data Privacy and Security Act (TDPSA)**: Enacted 2023; creates comprehensive
  consumer privacy obligations including security requirements that may interact with
  § 521.053 breach reporting [VERIFY]

[JURISDICTION-SPECIFIC] The interplay between pre- and post-SB 768 Texas law creates a
[VERIFY] priority item — confirm current individual vs. AG notice deadlines from official
Texas legislative sources before planning notifications. Texas AG enforcement has
historically been active on data breach and privacy matters.

#### Colorado (Colo. Rev. Stat. § 6-1-716)

**Why it matters**: 30-day deadline; 30-day third-party/service provider notice obligation;
detailed content requirements.

**Key requirements:**

- **Individual notice**: Within 30 days after determination that PI was or is reasonably
  believed to have been acquired
- **AG notice**: Required within 30 days; if 500+ Colorado residents affected
- **Third-party/service provider**: Service providers that maintain data on behalf of a
  covered entity must notify the covered entity within 30 days of discovering a breach
- **Content requirements**: Description of the incident, type of PI breached, contact
  information, toll-free number for inquiry, description of steps taken by covered entity
  to investigate, steps affected can take to protect themselves
- **Enhanced PI definition**: Includes biometric data, student ID numbers in combination
  with security code, tax ID numbers

[JURISDICTION-SPECIFIC] Colorado's 30-day third-party notice requirement creates a cascading
obligation. If a service provider discovers a breach at a client, the 30-day clock for
both the service provider's notice to client and the client's notice to residents runs
from the service provider's discovery.

#### Washington (Wash. Rev. Code § 19.255.010)

**Key requirements:**

- **Individual notice**: 30 calendar days after breach was discovered (HB 1071, effective
  March 1, 2020)
- **AG notice**: Within 30 days; required if 500+ Washington residents affected; include
  number of residents, types of PI, time frame of exposure, summary of steps taken, sample
  notice copy
- **Risk of harm**: Notification not required if "not reasonably likely to subject consumers
  to a risk of harm" — entity bears burden of documenting determination [VERIFY]
- **Expanded PI definition**: First name or initial + last name + account number, medical
  info, biometric data, full DOB, electronic signature, or government ID [VERIFY]

---

### Step 8: Cross-Cutting Analysis

#### 8a. Safe Harbor Provisions

**Encryption Safe Harbor** (most states):

- Applies when: Data was rendered unreadable/unusable through encryption AND the decryption
  key was not also acquired by the unauthorized person
- Standard: Most states do not specify an encryption algorithm standard; NIST-standard
  encryption (FIPS 140-2/3 validated modules) provides strongest defensibility
- Key not compromised: If the attacker obtained both the encrypted data and the decryption
  key, the safe harbor does not apply

**Good Faith Acquisition Exception** (most states):

- Applies when: An employee or agent of the company accessed PI for a legitimate business
  purpose, without further unauthorized use or disclosure
- Limitation: The exemption is narrow — requires the access was in good faith, for a
  legitimate business purpose, and that no unauthorized use or disclosure followed
- Does NOT apply to: External attackers; contractors acting outside their scope;
  employees accessing data for personal purposes

**Risk of No Harm** (select states — see § 5c above):

- Applies when: After appropriate investigation, the entity determines there is no
  reasonable likelihood of harm to affected individuals
- Requirement: Document the determination in writing; retain for statutory period; in
  some states notify the AG of the no-harm finding
- Practice note: Use this exemption conservatively; the harm threshold applies when harm
  is genuinely absent (e.g., encrypted data accessed without key; access was by researcher
  who did not retain data)

**HIPAA Compliance Safe Harbor** (select states [VERIFY]):

- Some states provide that HIPAA-covered entities that comply with the HIPAA Breach
  Notification Rule are deemed to have complied with state law
- Examples: Arkansas, Georgia, Louisiana, New Mexico, Tennessee, others [VERIFY each]
- Important: This exemption typically requires actual compliance with HIPAA notification
  (including timely individual and HHS notification) — not mere HIPAA coverage

**NIST Framework Safe Harbor** (Ohio — litigation only, not notification):

- Ohio Data Protection Act (§ 1354.02): Entities maintaining a written cybersecurity program
  conforming to NIST CSF, NIST SP 800-171/53, FedRAMP, CIS Controls, or ISO 27000 family
  are afforded an affirmative defense in data breach tort litigation
- This is a litigation defense, not a notification exemption — Ohio's notification
  requirements (§ 1347.12) still apply

#### 8b. Substitute Notice

**Trigger** (most states): Substitute notice is permitted when direct individual notice is
impractical because:

- The cost of notice would exceed $250,000 (typical threshold; varies by state)
- The number of affected individuals is 500,000 or more (typical threshold; varies by state)
- The entity does not have sufficient contact information to provide direct notice

**What constitutes substitute notice** (must provide ALL three):

1. Email notice (if email addresses available)
2. Conspicuous posting on the entity's website for at least 30–90 days (varies)
3. Notification to major statewide media outlets (TV, radio, newspapers)

**State variations**: Some states have different thresholds or methods. Check the specific
statute for each state where substitute notice is contemplated. [CHECK CURRENCY]

**Practice note**: Substitute notice is a last resort. Even when the threshold is met,
direct individual notice is always preferred where contact information is available. Combine
direct notice for known contacts with substitute notice for unknown contacts.

#### 8c. Credit Monitoring Obligations

| State                | When Required                                            | Duration                     | Cost Bearer    |
| -------------------- | -------------------------------------------------------- | ---------------------------- | -------------- |
| California           | Not mandated; must offer 12 months if providing services | 12 months minimum if offered | Covered entity |
| Colorado             | Mandatory if SSN breached [VERIFY]                       | 12 months                    | Covered entity |
| Connecticut          | Mandatory if SSN breached [VERIFY]                       | 24 months [VERIFY]           | Covered entity |
| Delaware             | Mandatory if SSN breached                                | 12 months minimum            | Covered entity |
| District of Columbia | Mandatory if SSN breached [VERIFY]                       | 18 months [VERIFY]           | Covered entity |
| Massachusetts        | Mandatory if SSN breached [VERIFY]                       | 18 months [VERIFY]           | Covered entity |
| Nevada               | Required if 500+ SSNs breached [VERIFY]                  | 12 months [VERIFY]           | Covered entity |
| Pennsylvania         | Mandatory if SSN breached [VERIFY]                       | 12 months [VERIFY]           | Covered entity |
| Rhode Island         | Mandatory if SSN breached                                | 18 months minimum            | Covered entity |
| Other states         | Generally not mandated; recommended best practice        | N/A                          | Voluntary      |

**Practice note**: Even where not mandated, offering credit monitoring is standard practice
and may reduce litigation risk. The notice letter should describe any monitoring offered.
In states where it is mandated (Delaware, Rhode Island, possibly others [VERIFY]), failure
to offer is a statutory violation.

#### 8d. Third-Party / Service Provider Notification

When the breached entity is a **service provider** (processor) not a data owner:

| State             | Service Provider Obligation                                                      | Timeline               |
| ----------------- | -------------------------------------------------------------------------------- | ---------------------- |
| Colorado          | Must notify covered entity within 30 days of breach discovery                    | 30 days from discovery |
| California        | Must notify covered entity "most expedient time possible" [VERIFY SB 446 status] | Expedient time         |
| Most other states | Contract governs; statute may be silent                                          | Per contract           |

**Best practice**: Data processing agreements (DPAs) should specify the service provider's
notification obligation to the data owner (typically 72 hours under GDPR-influenced
agreements). When triage involves a service provider, determine: Did the service provider
notify us on time? Does the service provider's late notice affect our clock? (In some
states, the covered entity's clock begins at the service provider's discovery.)

#### 8e. Law Enforcement Delay

All US states (and federal rules) permit delayed notification when a **law enforcement
agency** determines that notification would impede a criminal investigation or national
security matter. Requirements:

- Law enforcement must actively request the delay (entity cannot self-defer)
- Delay is for a reasonable period, typically 30–90 days (varies by state; may be extended)
- After law enforcement delay lifts, notification must proceed promptly
- Document the law enforcement request and the delay period in the incident record

### Step 9: Notification Classification

For each state where affected residents live, classify the notification obligation:

| Classification               | Definition                                                                               | Action                                                                            |
| ---------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **NOTIFIABLE — URGENT**      | Clear obligation, short deadline (≤30 days); no valid exemption                          | Dispatch notice without delay; AG filing within deadline                          |
| **NOTIFIABLE — STANDARD**    | Clear obligation, longer deadline (31–60 days); no valid exemption                       | Schedule notice per deadline; build notice package                                |
| **NOTIFIABLE — EXPEDIENT**   | Obligation exists but no specific deadline ("most expedient time")                       | Target dispatch within 30–45 days; document rationale for timing                  |
| **CONDITIONAL**              | Obligation depends on risk of harm assessment or unclear PI match; investigation ongoing | Complete risk assessment; document; re-classify after assessment                  |
| **SAFE HARBOR — ENCRYPTION** | Data was encrypted per applicable standard and decryption key not compromised            | Document encryption evidence; record in incident file; [VERIFY state recognition] |
| **SAFE HARBOR — NO HARM**    | After documented investigation, no reasonable likelihood of harm                         | Written no-harm determination; retain 5+ years; AG notice in some states          |
| **SAFE HARBOR — HIPAA**      | HIPAA-covered entity; HIPAA compliance satisfies state law [state-specific]              | Confirm state recognizes HIPAA safe harbor [VERIFY]; comply with HIPAA BNR        |
| **NOT APPLICABLE**           | No affected residents in jurisdiction; PI definition not met; breach definition not met  | Document basis; retain with incident record                                       |

**Conservative default**: Classify as NOTIFIABLE when facts are uncertain. Down-classify
only with documented, attorney-reviewed basis.

### Step 10: Prioritized Notification Timeline

Build the notification calendar using these ordering rules:

1. **Puerto Rico**: 10-day clock to Department of Consumer Affairs — this is the shortest
   clock of any US jurisdiction; check immediately
2. **Federal agencies (FCC, HIPAA-HHS, GLBA-FTC, SEC)**: Run in parallel with state clocks
3. **30-day states** (priority group): California (SB 446 eff. 2026), Colorado, Florida,
   New York, Texas, Utah, Washington — begin notice preparation immediately
4. **ASAP states** (Massachusetts, Maine, New Hampshire, others): No fixed deadline but
   "without unreasonable delay" — target 30 days absent law enforcement delay
5. **45-day states**: Arkansas, Mississippi, New Mexico, Oregon, Rhode Island
6. **60-day states**: Delaware, Louisiana, South Carolina, South Dakota
7. **Remaining ASAP states**: Handle in parallel with groups 4–6

**Strictest-safe sequencing**: When requirements conflict across states, apply:

- **Earliest defensible deadline** across all implicated states
- **Highest protective standard** for notice content (include requirements from ALL states)
- **Most complete notice content** for the combined template

### Step 11: Generate Notification Packages

For each applicable state, generate:

1. **Jurisdiction-specific notice content checklist** (see below)
2. **Draft individual notice letter** (from template in Step 13)
3. **Draft AG filing letter or web portal submission** (from template in Step 13)
4. **Credit monitoring provider referral** (where mandated)

**CLARIFY** — At this stage, ask:

- "Should I generate a single unified notice covering all states' requirements, or
  separate state-by-state notices?"
- Options: Single notice (most states; simplest), State-by-state variants (where specific
  format requirements differ significantly), Both (unified + state supplements)
- _Why this matters_: A single notice covering all states' requirements reduces operational
  complexity but may include details not required in simpler states.

### Step 12: Quality Verification

Before delivering any triage output, run the quality frameworks below.

---

## Notice Content Checklists

### Universal Minimum Notice Content

Every individual notice must include (compiled from strictest across all states):

- [ ] **What happened**: Brief description of the incident (nature and general circumstances)
- [ ] **When it happened**: Date of incident and date of discovery (if known)
- [ ] **What information was involved**: Specific types of PI affected (not individual
      records, but categories: SSN, financial, medical, etc.)
- [ ] **What we are doing**: Steps taken to investigate, mitigate, and prevent recurrence
- [ ] **What you can do**: Recommended steps affected individuals should take to protect
      themselves (credit monitoring, fraud alerts, account monitoring)
- [ ] **Contact information**: Toll-free number, email, or postal address for inquiries;
      hours of operation
- [ ] **Identity theft resources**: Reference to FTC identity theft resources (identitytheft.gov)
      and/or state AG consumer protection resources
- [ ] **Title/header** (California): "Notice of Data Breach" or substantially similar;
      written in plain language [VERIFY other states' format requirements]

**State-specific additions:**

| Additional Element                               | States Requiring It                   |
| ------------------------------------------------ | ------------------------------------- |
| Credit monitoring offer description (if offered) | Florida (if offering), California     |
| Credit monitoring enrollment instructions        | Florida (if offering)                 |
| AGᵢ or regulator contact information             | Massachusetts, some others            |
| Type of entity reporting                         | Massachusetts (to AG)                 |
| Known responsible party                          | Massachusetts (to AG, if known)       |
| Sample copy of notice (to AG)                    | California, Massachusetts, Washington |
| Number of residents affected (to AG)             | Multiple states                       |

### AG Notification Content

AG notifications typically require:

- [ ] Name and contact information of reporting entity
- [ ] Date and nature of breach
- [ ] Types of PI involved
- [ ] Number of affected state residents
- [ ] Steps taken to investigate and mitigate
- [ ] A sample copy of the individual notice (most states)
- [ ] Whether notification has been delayed at law enforcement request
- [ ] Contact person for AG follow-up

**Delivery method**: Most states accept electronic submission. Many have online portals:

- California: oag.ca.gov/privacy/databreach/reporting
- Florida: Provided via Florida Department of Legal Affairs portal [VERIFY current URL]
- New York: AG online portal [VERIFY current URL]
- Massachusetts: AG + OCABR online or certified mail [VERIFY]
- Other states: Certified mail to AG office; check each state's AG website for current
  instructions [VERIFY each before filing]

---

## Federal Overlay Notification Content

### HIPAA — Individual Notice (45 CFR § 164.404(c))

Must include:

- [ ] Brief description of what happened, including date (if known) and date of discovery
- [ ] Description of types of PHI involved (type of information, not individual records)
- [ ] Steps individuals should take to protect themselves from potential harm
- [ ] Brief description of what covered entity is doing to investigate, mitigate, and protect
- [ ] Contact information: toll-free phone, email, website, or address

### HIPAA — HHS Notice

File via HHS Breach Notification web portal:

- If 500+ residents of a state: file simultaneously with individual notice
- If <500 residents per state: maintain log; submit annual report by 60 days after year-end

### GLBA — FTC Notice (16 CFR § 314.9)

File via FTC online portal:

- [ ] Name and contact information of the reporting financial institution
- [ ] Types of information involved
- [ ] Date or date range of the notification event
- [ ] Number of consumers affected or potentially affected
- [ ] General description of the notification event
- [ ] Whether law enforcement has indicated public notification would impede investigation

---

## Severity Classification and Prioritization Framework

### Notification Priority Tiers

**Tier 1 — Act Immediately (<48 hours):**

- Puerto Rico (10-day clock starts at discovery)
- FCC telecom reporting if applicable (7 business days to agencies)
- GLBA FTC reporting if applicable (30 days from discovery — begin immediately)
- SEC Form 8-K if materiality determined (4 business days)
- Any state with a 30-day deadline where >10 days have already elapsed since discovery
- Active law enforcement requests for information

**Tier 2 — Act Within 7 Days:**

- All 30-day deadline states where incident is newly discovered: California, Colorado,
  Florida, Maine [VERIFY], New York, Utah, Washington
- Texas: 30-day AG notice if 250+ residents [VERIFY]; 60-day individual notice
- HIPAA notification to HHS if 500+ PHI records affected
- Begin notice preparation for all "ASAP" states

**Tier 3 — Act Within 14–30 Days:**

- HIPAA individual notification (letter drafting and dispatch)
- ASAP states: Massachusetts, New Hampshire, New Jersey, Maine, Pennsylvania, and others
  — target dispatch no later than 30 days from discovery absent law enforcement delay
- Prepare AG filings for all applicable states

**Tier 4 — Plan and Execute (30–60 Days):**

- 45-day deadline states: Arkansas, Mississippi, New Mexico, Oregon, Rhode Island
- 60-day deadline states: Delaware, Louisiana, South Carolina, South Dakota
- Remaining ASAP states: Illinois, Indiana, Iowa, Minnesota, Missouri, Montana, Nebraska,
  North Carolina, North Dakota, Vermont, Wyoming, DC, and others — dispatch in parallel
  with Tiers 2–3

**Tier 5 — Document and Monitor:**

- States where safe harbor applies (document encryption or no-harm determination)
- States where PI definition is not met (document basis for non-notification)
- States where affected resident count is zero or below AG threshold (document basis)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any triage output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                                    | Fail Action                                              |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every timeline, threshold, and PI definition cites a specific statute section                                                           | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations use consistent format: "State Code § X.XX"                                                                                | Fix format                                               |
| **Currency**   | Every state law provision checked for amendments; [CHECK CURRENCY] flag applied to any provision that may have changed since early 2026 | Flag "[CHECK CURRENCY — law may have been amended]"      |
| **Domain**     | No federal rule applied as universal state rule; no single state's analysis imported into another state's analysis                      | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly surfaced; no false precision on ambiguous timelines                                                              | Add confidence qualifier and [VERIFY] tag                |

### Self-Interrogation for CONDITIONAL Classifications

For any state classified as CONDITIONAL (risk of harm assessment required), apply this
3-pass self-interrogation before finalizing:

**Pass 1 — Legal Chain Integrity**:

- Does the no-harm conclusion follow from the factual evidence available?
- Would a reasonable AG in this state accept this harm assessment?
- What is the strongest counter-argument (that harm IS likely)?

**Pass 2 — Completeness**:

- Have all relevant PI categories been considered (not just obvious ones)?
- Have secondary harms been assessed (reputational, insurance, health, not just financial)?
- Are there state-specific harm factors that apply (e.g., California's broad PI definition)?

**Pass 3 — Challenge**:

- What would a class action plaintiff's attorney argue to establish harm?
- Is there any downstream use of the breached data that could create harm even if no
  immediate harm is visible?
- Is the CONDITIONAL classification conservative enough to protect the organization?

Mark outcome: `self_interrogation: PASS` (no revisions needed) or `self_interrogation:
REVISED` (revised upward to NOTIFIABLE based on self-interrogation).

### Confidence Scoring

For each state-level finding:

| Level        | Range     | Meaning                                                       | Action                                                |
| ------------ | --------- | ------------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled statute; confirmed facts; no ambiguity                | State with confidence; no [VERIFY] needed             |
| **High**     | 0.80–0.94 | Strong statutory authority; minor factual uncertainty         | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Statute exists but ambiguous in application; facts incomplete | State with reasoning; mark [VERIFY] for confirmation  |
| **Possible** | 0.40–0.59 | Genuinely uncertain; recent amendment; ambiguous definition   | Flag for counsel review; present both interpretations |
| **Unlikely** | 0.0–0.39  | Insufficient basis; no statute confirmed                      | Do not assert; mark "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every triage output MUST include a Glass Box audit block:

```yaml
glass_box:
  skill_name: "legalcode-us-breach-notification-triage"
  incident_id: "[BREACH-YYYY-MM-NNN]"
  analysis_date: "[Date]"
  jurisdiction: "50 US states + DC + Puerto Rico + Guam + USVI + American Samoa"
  affected_states_identified: "[count]"
  federal_overlay_applicable: "[HIPAA / GLBA / SEC / FCC / CIRCIA / None]"
  entity_role: "[Controller / Processor / Both]"
  incident_state: "[Suspected / Confirmed PI exposure / Resolved]"
  pi_categories_involved: "[List]"
  assumed_population: "[Known count / Estimated total / Unknown — conservative applied]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[path or 'Not created']"
  playbook_used: "[Playbook name or 'Statutory defaults']"
  notifications_classified:
    - NOTIFIABLE_URGENT: "[count states]"
    - NOTIFIABLE_STANDARD: "[count states]"
    - NOTIFIABLE_EXPEDIENT: "[count states]"
    - CONDITIONAL: "[count states]"
    - SAFE_HARBOR: "[count states — specify basis]"
    - NOT_APPLICABLE: "[count states]"
  earliest_deadline: "[Date + Timezone + State]"
  ag_filings_required: "[count states with AG filing obligation]"
  credit_monitoring_required: "[Yes — states requiring / No]"
  substitute_notice_applicable: "[Yes — basis / No]"
  citations_verified: "[Number VERIFIED vs. [VERIFY] marked]"
  self_interrogation: "[PASS / REVISED / NOT APPLICABLE — no CONDITIONAL items]"
  confidence_distribution:
    definite: "[count states]"
    high: "[count states]"
    probable: "[count states]"
    possible: "[count states]"
    unlikely: "[count states]"
  assumptions: "[List explicit assumptions made for missing facts]"
  limitations:
    - "State law verified as of early 2026; [CHECK CURRENCY] for amendments"
    - "AG guidance verified against stated sources; may have changed"
    - "Safe harbor analysis depends on factual predicate confirmed by forensics"
    - "Credit monitoring requirements marked [VERIFY] for states not confirmed"
  reviewer: "AI-assisted — requires qualified legal counsel review before notice dispatch"
```

---

## Anti-Patterns

What NOT to do in US breach notification triage:

1. **Using one state's PI definition as a proxy for all states** — California's definition
   is among the broadest; using it uniformly over-notifies. Georgia's is narrower.
   Always apply each state's definition to the breached data elements.

2. **Treating "most expedient time" as meaning weeks or months** — Courts and AGs
   interpret this strictly. In the absence of a specific deadline, target dispatch within
   30 days. Delay must be documented and justified.

3. **Forgetting Puerto Rico's 10-day clock** — Puerto Rico's Department of Consumer
   Affairs must be notified within 10 non-extendable days of discovery. This is the
   strictest clock in the US system and is frequently overlooked.

4. **Missing the AG notification threshold analysis** — Some states require AG notice
   only above a resident count threshold (e.g., California >500, Arizona >1,000, Virginia

   > 1,000). Missing this means either over-filing (minor) or under-filing (violation).

5. **Assuming safe harbor without confirmed facts** — The encryption safe harbor only
   applies if the decryption key was not also compromised. Forensic confirmation is
   required before relying on the safe harbor. Document the confirmation.

6. **Applying HIPAA compliance as a state safe harbor without state-by-state verification**
   — Not all states recognize HIPAA compliance as a substitute for state notification.
   Each state where the HIPAA safe harbor is invoked must be independently confirmed.

7. **Treating federal and state obligations as alternatives** — In most cases they run in
   parallel. HIPAA-covered entities must notify under HIPAA AND under applicable state
   laws. The federal and state clocks are independent.

8. **Counting from the wrong clock-start date** — HIPAA starts from "discovery"; GLBA
   Safeguards Rule starts from first day any employee "knows"; some states start from
   "determination." Apply each regime's clock-start rule independently.

9. **Confusing business days and calendar days** — FCC telecom rules use business days;
   most state statutes use calendar days; some use business days. Apply the correct unit
   per statute. When in doubt, use calendar days (stricter).

10. **Omitting the law enforcement delay procedure** — If law enforcement requests delay,
    document it formally. The delay is for the specific period requested, not indefinitely.
    After the delay period, notification must proceed immediately.

11. **Using a single national notice template without state customization** — California
    requires specific title text ("Notice of Data Breach") and specific sections. Florida
    requires description of any credit monitoring services offered. Massachusetts requires
    submission to both AG and OCABR. Customize per jurisdiction.

12. **Not building a credit monitoring obligation into the notice for Delaware and Rhode Island**
    — These states mandate credit monitoring when SSNs are involved. Failing to include it
    is a statutory violation.

13. **Sending individual notices before AG notices where simultaneous filing is required**
    — Some states require simultaneous or prior AG notice before individual notice. Filing
    individual notice first in those states may violate the statute.

14. **Treating the third-party notification obligation as satisfied by internal disclosure**
    — When the entity is a service provider/processor, notifying the data owner is not the
    same as notifying affected individuals. The data owner's obligation to individuals may
    also create a contractual obligation on the service provider to support the owner's notice.

15. **Failing to re-triage when new forensic facts emerge** — New information about the
    scope, PI categories involved, or affected state counts can change the notification
    obligations. Re-run the triage when material forensic findings are updated.

16. **Presenting [VERIFY] items as settled conclusions** — Any statutory citation,
    AG threshold, or safe harbor marked [VERIFY] must be independently verified by counsel
    before relying on it to decide whether to notify or not notify.

---

## Writing Standards

Apply plain-language discipline to all notice outputs:

**For individual notices** (consumer-facing):

- Plain English; sixth-grade reading level target
- Active voice: "We discovered that your information was accessed" not "It has been
  determined that there was unauthorized access to information"
- Short sentences. One point per sentence.
- Avoid legal jargon: "personal data" is clearer than "personally identifiable information"
  or "non-public personal information"
- Begin with the key fact: "We are writing to inform you that..." on the first line

**For AG filings** (regulatory-facing):

- Professional, direct tone
- Specific facts (dates, counts, types of PI)
- Organized by the AG's form or portal structure
- Legal citations where required

**Quality gates before dispatching any notice:**

1. Has a licensed attorney reviewed and approved the notice?
2. Does the notice comply with the specific format requirements of each state it is sent to?
3. Does it address all required content elements for the strictest implicated state?
4. Is the clock deadline met (or will be met before dispatch)?
5. Has the AG filing been prepared and dispatched simultaneously (where required)?
6. Is the incident record updated to log the dispatch date, method, and recipient count?

---

## External Tool Integration

This skill integrates with **legalcode-mcp** for legal research and **legalcode-breach-
severity-assessment** for upstream harm triage.

**With legalcode-mcp connected (preferred):**

- In Step 6, search for current statutory text for each implicated state
- Search for recent AG guidance, enforcement actions, and press releases
- Verify safe harbor provisions and any HIPAA/GLBA preemption language
- Check for statutory amendments enacted after this skill's training cutoff
- Save verified citations to `/tmp/legalcode-breach-notification-research.md`
- Mark all verified citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory citations with [VERIFY]
- Recommend that counsel independently verify each state statute before notice dispatch
- Note: "Statute citations in this triage are based on AI training data as of early 2026;
  verify current text at [state legislature's official website] before relying on them"
- Focus the analysis on operational timeline planning and qualitative risk assessment
- Explicitly state in the Glass Box: `legalcode_mcp: "Not connected — all citations require
independent verification"`

**Upstream skill integration (legalcode-breach-severity-assessment):**

- Use that skill first to determine: harm likelihood, risk vectors, severity classification
- This skill accepts the output of `legalcode-breach-severity-assessment` as input for the
  incident description (Step 1) — import the incident facts section directly

---

## Template Notice Letters

### Template A: Individual Notice Letter

```
[ENTITY NAME]
[Address]
[Date]

NOTICE OF DATA BREACH

Dear [NAME / "Valued Customer" if individualized version not feasible]:

We are writing to inform you that [ENTITY NAME] recently experienced a data security
incident that may have affected your personal information.

WHAT HAPPENED
[Brief description of the incident — when it was discovered; how it occurred (if
known); what systems or records were involved. Avoid speculation.]

WHAT INFORMATION WAS INVOLVED
The following types of your personal information may have been affected:
• [Category 1, e.g., Social Security Number]
• [Category 2, e.g., Financial account number]
• [Add only the categories applicable to this individual or cohort]

WHAT WE ARE DOING
[Describe concrete steps taken: system containment, forensic investigation, law
enforcement notification, security improvements. Be specific.]

WHAT YOU CAN DO
We recommend you take the following steps to protect yourself:
• Place a fraud alert or credit freeze on your credit file by contacting one of the
  three major credit bureaus (Equifax, Experian, TransUnion)
• Review your account statements and credit reports for suspicious activity
• [Credit monitoring offer: "As a precaution, we are offering you [X months] of
  complimentary credit monitoring through [VENDOR]. To enroll, visit [URL] or call
  [NUMBER] by [DEADLINE]."]
• Visit the FTC's identity theft website at identitytheft.gov for additional resources

FOR MORE INFORMATION
If you have questions about this incident, please contact us at:
• Toll-free: [NUMBER], available [HOURS]
• Email: [DEDICATED BREACH INQUIRY EMAIL]
• Mail: [ADDRESS]

We sincerely regret any concern or inconvenience this incident may cause you.

Sincerely,
[NAME]
[TITLE]
[ENTITY NAME]
```

### Template B: Attorney General Notification Letter

```
[Date]

Office of the Attorney General
[State Attorney General's Name]
[Address]
[Filing method: certified mail / portal at URL]

Re: Data Security Breach Notification — [ENTITY NAME]
    Date of Breach: [Date] | Date of Discovery: [Date]

Dear Attorney General [Name]:

Pursuant to [State Statute Citation], [ENTITY NAME] hereby provides notice of a data
security breach affecting residents of [State].

REPORTING ENTITY
Name: [ENTITY NAME]
Contact: [NAME, TITLE, PHONE, EMAIL]
Address: [ADDRESS]
Type of entity: [e.g., retail business, healthcare provider, financial institution]

NATURE OF THE BREACH
[Brief factual description: date, systems affected, how the unauthorized access or
acquisition occurred if known]

INFORMATION INVOLVED
The following categories of personal information were involved:
• [Category 1]
• [Category 2]

NUMBER OF AFFECTED [STATE] RESIDENTS
Affected residents: approximately [NUMBER]
[If count is unavailable: "The exact count of affected [State] residents is under
investigation; currently estimated at [RANGE]"]

DATE OF DISCOVERY
[ENTITY NAME] became aware of the incident on [Date].

STEPS TAKEN
[ENTITY NAME] has taken the following steps:
• [Containment steps]
• [Forensic investigation steps]
• [Law enforcement notification, if any]
• [Security improvement steps]

NOTIFICATION TO INDIVIDUALS
Individual notice letters will be dispatched to affected [State] residents on or before
[Date] via [method: first-class mail / email].

CREDIT MONITORING / REMEDIATION SERVICES
[If offered: describe the service, provider, duration, enrollment instructions]
[If not offered or not required: "We are not offering credit monitoring at this time
because [reason]" or omit this section if not relevant]

LAW ENFORCEMENT INVOLVEMENT
[If law enforcement requested delay: "Notification was delayed at the request of [law
enforcement agency], which has determined that earlier notification would impede an
ongoing criminal investigation. The delay period expired on [Date]."]
[If no law enforcement delay: "There is no current law enforcement delay in effect."]

ENCLOSURE
Enclosed: Sample copy of individual notice letter

[ENTITY NAME] takes data security seriously and regrets the impact of this incident on
[State] residents. We are committed to cooperating fully with your office. Please do not
hesitate to contact [NAME] at [PHONE/EMAIL] with any questions.

Sincerely,
[NAME]
[TITLE]
[ENTITY NAME]

Enclosure: Sample individual notice letter
```

---

## Output Format Template

Structure the final triage output as follows:

```markdown
# US Breach Notification Triage Report

**Incident ID**: [BREACH-YYYY-MM-NNN]
**Analysis Date**: [Date]
**Analyst**: AI-assisted (legalcode-us-breach-notification-triage)
**Review Required**: YES — qualified legal counsel must review before notice dispatch

---

## 1. Executive Outcome

| Item                    | Details                              |
| ----------------------- | ------------------------------------ |
| Go/No-go posture        | [NOTIFIABLE / CONDITIONAL / Exempt]  |
| Earliest deadline       | [Date + Timezone + State]            |
| States requiring notice | [Count] of [Total analyzed]          |
| AG filings required     | [Count states]                       |
| Federal overlays        | [HIPAA / GLBA / SEC / FCC / None]    |
| Priority 1 actions      | [Ordered list — due within 48 hours] |

---

## 2. Incident Summary

- **Discovery date**: [Date + source of awareness]
- **Incident type**: [Ransomware / Unauthorized access / Theft / Misconfiguration / etc.]
- **Affected systems**: [Brief description]
- **PI categories confirmed involved**: [List]
- **Affected individuals (estimated)**: [Total count or range]
- **Affected states (confirmed)**: [List with estimated resident counts]
- **Assumptions**: [List all assumptions made]

---

## 3. Federal Overlay Assessment

| Regime          | Applicable | Entities Affected   | Deadline                                  | Filing Recipient           | Status                     |
| --------------- | ---------- | ------------------- | ----------------------------------------- | -------------------------- | -------------------------- |
| HIPAA BNR       | [Yes/No]   | [Covered entity/BA] | [Date]                                    | HHS, Individuals, Media    | [REQUIRED / N/A]           |
| GLBA Safeguards | [Yes/No]   | [FI type]           | [Date — 30 days]                          | FTC portal                 | [REQUIRED / N/A]           |
| SEC Form 8-K    | [Yes/No]   | [Public company]    | [Date — 4 business days from materiality] | SEC EDGAR                  | [REQUIRED / N/A]           |
| FCC Rules       | [Yes/No]   | [Telecom carrier]   | [7 biz days / 30 days]                    | FCC + FBI + SS + Customers | [REQUIRED / N/A]           |
| CIRCIA          | [Yes/No]   | [Critical infra]    | [72 hrs proposed]                         | CISA                       | [MONITOR — proposed rules] |

---

## 4. Multi-State Applicability Matrix

| State                                | PI Def Met | Breach Def Met | Risk of Harm Threshold | Applicable | Classification | Deadline | AG Filing                 |
| ------------------------------------ | ---------- | -------------- | ---------------------- | ---------- | -------------- | -------- | ------------------------- |
| [State]                              | YES/NO     | YES/NO         | N/A / MET / NOT MET    | YES/NO     | [Tier]         | [Date]   | [YES/NO — threshold/date] |
| [All states with affected residents] | ...        | ...            | ...                    | ...        | ...            | ...      | ...                       |

---

## 5. Prioritized Notification Calendar

### Priority 1 — Act Within 48 Hours

| Action | State/Regime | Deadline | Owner | Evidence |
| ------ | ------------ | -------- | ----- | -------- |

### Priority 2 — Act Within 7 Days

| Action | State/Regime | Deadline | Owner | Evidence |

### Priority 3 — Act Within 14–30 Days

| Action | State/Regime | Deadline | Owner | Evidence |

### Priority 4 — Act Within 30–60 Days

| Action | State/Regime | Deadline | Owner | Evidence |

### Priority 5 — Document and Monitor

| Action | State/Regime | Trigger for Re-assessment | Owner |

---

## 6. Per-State Notification Checklists

### [State 1] — [Classification] — Deadline: [Date]

**Notifiability**: [NOTIFIABLE / CONDITIONAL / SAFE HARBOR / NOT APPLICABLE]
**Confidence**: [Definite / High / Probable / Possible]
**Legal basis**: [Statute citation]
**Clock start**: [Date + source]
**Deadline**: [Date + calendar/business days]
**AG threshold**: [Met / Not met / N/A — specify count]
**AG filing deadline**: [Date] via [method/portal]

**Individual notice content checklist**:

- [ ] What happened (date, nature)
- [ ] Types of PI involved
- [ ] Steps entity is taking
- [ ] Steps individuals should take
- [ ] Contact information
- [ ] [State-specific additions]

**AG notice content checklist**:

- [ ] Entity name and contact
- [ ] Breach nature and date
- [ ] PI types
- [ ] Affected resident count
- [ ] Steps taken
- [ ] Individual notice sample

**Safe harbor analysis**: [Encryption: N/A / Applied / Not confirmed] [Good faith: N/A] [No harm: N/A / Applied / Not documented]

**Credit monitoring obligation**: [Required — [duration] / Recommended / Not required]

**Substitute notice**: [Permitted if cost >[threshold] or >[count] individuals / Not applicable]

[Repeat for each state]

---

## 7. Safe Harbor Registry

| State | Safe Harbor Type | Factual Predicate | Status | Evidence Required |
| ----- | ---------------- | ----------------- | ------ | ----------------- |

---

## 8. Credit Monitoring Summary

| State | Required | Trigger | Duration | Cost Bearer | Implementation |
| ----- | -------- | ------- | -------- | ----------- | -------------- |

---

## 9. Quality Assurance

- **Citation Quality Gates**: [PASS / REVISED — describe revisions]
- **Self-Interrogation** (CONDITIONAL states): [PASS / REVISED — list revised states]
- **Confidence distribution**: [Definite: N] [High: N] [Probable: N] [Possible: N]
- **[VERIFY] items**: [List items requiring independent counsel confirmation]
- **[CHECK CURRENCY] items**: [List recently amended statutes to recheck]

---

## 10. Glass Box Audit Trail

\`\`\`yaml
glass_box:
[Full YAML block as specified above]
\`\`\`

---

## 11. Open Items and Reassessment Triggers

**[VERIFY] items requiring counsel confirmation**:

- [ ] [State + provision + reason verification needed]

**[CHECK CURRENCY] items**:

- [ ] [State + provision + last known amendment date]

**Reassessment triggers**:

- Forensic update changes PI categories involved
- Forensic update changes affected resident count by state
- Law enforcement delay lifted
- New AG guidance or enforcement action in an applicable state
- Federal regulatory update to HIPAA, GLBA, or other overlay
- Affected individual count exceeds or falls below AG threshold in a state
```

---

## Localization Notes

This skill covers all US jurisdictions. For guidance on international breach notification
requirements (GDPR, UK GDPR, LGPD, PIPL, Australian Privacy Act, PIPEDA, etc.), use
`legalcode-breach-severity-assessment` as the primary skill.

For incidents affecting both US and non-US residents, run both skills in parallel:

- This skill → US state-by-state notification obligations
- `legalcode-breach-severity-assessment` → Global jurisdiction analysis (EU, UK, etc.)

Key US territorial notes:

- **Puerto Rico**: 10-day clock is the strictest in the US system; treat as top priority
- **Guam**: Has enacted breach notification law; Guam's own procedures may satisfy notice
  requirements for entities with their own notification procedures consistent with Guam's
  statute [VERIFY]
- **US Virgin Islands**: Has enacted breach notification law [VERIFY full requirements]
- **American Samoa**: Limited specific legislation; federal standards apply as floor [VERIFY]
- **CNMI (Commonwealth of the Northern Mariana Islands)**: Verify applicable law [VERIFY]

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis from deep research on all 50 US
state breach notification statutes, federal overlay requirements (HIPAA, GLBA Safeguards
Rule, SEC Form 8-K Item 1.05, FCC 2024 telecom rules, CIRCIA proposed rules), and
multi-state notification planning methodology. Legal research via WebSearch against
primary sources including NCSL, Perkins Coie Security Breach Notification Chart, IAPP
State Data Breach Notification Chart, Davis Wright Tremaine State Data Breach Summary,
Foley & Lardner State Data Breach Notification Laws, HHS HIPAA Guidance, FTC GLBA
Safeguards Rule publications, and SEC cybersecurity disclosure rules. Structural patterns
adopted from `legalcode-contract-review` (quality frameworks, Glass Box, anti-patterns)
and `legalcode-breach-severity-assessment` (workflow structure, prioritization framework,
finding format). All state statute citations carry [VERIFY] markers — verify current
statutory text against official sources before relying on any provision.

**Key sources consulted** [VERIFY all for currency]:

- NCSL Security Breach Notification Laws: ncsl.org
- Perkins Coie Security Breach Notification Chart: perkinscoie.com
- IAPP State Data Breach Notification Chart: iapp.org
- Davis Wright Tremaine State Data Breach Statutes: dwt.com/gcp/state-data-breach-statutes
- Foley & Lardner State Data Breach Notification Laws: foley.com
- HHS HIPAA Breach Notification Rule: hhs.gov/hipaa/for-professionals/breach-notification
- FTC GLBA Safeguards Rule (16 CFR Part 314): ftc.gov
- SEC Cybersecurity Disclosure Rules (Form 8-K Item 1.05): sec.gov
- FCC Data Breach Notification Rules (47 CFR Part 64): fcc.gov
- California SB 446 (signed October 2025, effective January 1, 2026)
- New York SHIELD Act amendment (signed December 24, 2024)
