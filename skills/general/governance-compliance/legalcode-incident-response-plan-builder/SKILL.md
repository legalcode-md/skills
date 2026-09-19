---
name: legalcode-incident-response-plan-builder
description: 'Build comprehensive Incident Response Plans (IRP) covering the full incident lifecycle:
  preparation, detection and analysis, containment, eradication, recovery, and post-incident activities.
  Use when building an IRP from scratch, reviewing or updating an existing plan, responding to a live
  security incident, or preparing tabletop exercises.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Build comprehensive Incident Response Plans (IRP) covering the full incident lifecycle: preparation, detection and analysis, containment, eradication, recovery, and post-incident activities. Use when building an IRP from scratch, reviewing or updating an existing plan, responding to a live security incident, or preparing tabletop exercises. Produces a complete IRP document package including RACI matrix for cross-functional incident response team roles (legal, IT security, privacy/DPO, communications, executive, HR, external counsel, forensics), severity classification framework (P1-P4 with escalation triggers and response SLAs), regulatory notification decision trees (GDPR Art. 33-34, NIS2 Art. 23, US state breach laws, UK ICO, Australian OAIC, Canadian OPC, SEC Form 8-K), legal privilege protection architecture (dual-track investigation model, attorney-client privilege safeguards, Kovel doctrine application), evidence preservation protocols (chain of custody, legal hold, forensic integrity), six communication templates (internal, executive, board, regulatory, individual, media, customer), tabletop exercise scenarios with inject cards, and post-incident review framework. Aligned with NIST SP 800-61r3 (CSF 2.0, April 2025), NIST SP 800-86, GDPR Art. 33-34, NIS2 Directive Art. 23, ISO/IEC 27035-1/2/3 (2023), ISO/IEC 27037, SANS 6-phase IH&R framework, and CISA incident response guidance. Operates in two modes: pre-incident plan-building and live incident response. Integrates with legalcode-breach-severity-assessment, legalcode-breach-regulatory-notification-drafter, legalcode-us-breach-notification-triage, and legalcode-dsar-workflow-builder.


# Legalcode Incident Response Plan Builder

> **Disclaimer**: This skill provides a framework for AI-assisted incident response
> planning. It does not constitute legal advice. All outputs — particularly regulatory
> notification decisions, privilege strategy, and legal hold instructions — must be
> reviewed by qualified legal counsel licensed in the relevant jurisdiction(s) before
> implementation. Cybersecurity law, regulatory requirements, and breach notification
> timelines change frequently; verify current requirements before relying on any
> deadline, threshold, or procedure described here. Statutory and case law references
> cited in this skill carry hallucination risk — verify against authoritative sources
> before relying on them. Mark any unverified claim `[VERIFY]` and cross-check against
> current official guidance. Inadequate incident response — including missed notification
> windows, destroyed evidence, or compromised privilege — can result in regulatory
> enforcement, civil liability, criminal exposure, and irreversible reputational harm.

---

## Purpose and Scope

This skill builds and executes a complete Incident Response Plan package, from
governance structure and pre-incident preparation through post-incident review and
continuous improvement. It is designed for legal, privacy, and security teams that need
a legally defensible, operationally actionable plan aligned with current international
frameworks.

**Covers:**

- Full IRP lifecycle (Preparation → Detection & Analysis → Containment → Eradication
  → Recovery → Post-Incident Activity)
- Alignment with NIST SP 800-61r3 (CSF 2.0, April 2025), SANS 6-phase IH&R,
  ISO/IEC 27035-1/2/3 (2023), and ISO/IEC 27037
- Severity classification framework (P1 Critical / P2 High / P3 Medium / P4 Low)
- RACI matrix for 9+ roles across 24 IR activities
- Regulatory notification decision tree (GDPR, NIS2, US states, UK, AU, CA, SG, NZ)
- Legal privilege architecture (dual-track investigation model, Kovel doctrine)
- Evidence preservation protocols (legal hold, chain of custody, forensic imaging)
- Six communication template types with fill-in structures
- Tabletop exercise scenarios with inject cards (three complexity levels)
- Post-incident blameless review template
- IRP maintenance schedule and versioning governance
- Integration with legalcode breach skill family

**Does not:**

- Determine whether a specific breach is notifiable (use `legalcode-breach-severity-assessment`)
- Draft the regulatory notification documents (use `legalcode-breach-regulatory-notification-drafter`)
- Map all US state notification obligations and deadlines (use `legalcode-us-breach-notification-triage`)
- Perform forensic root-cause analysis — coordinates forensic engagement, does not execute it
- Provide legal advice or replace qualified incident response counsel
- Cover all sector-specific regulatory overlays in full (HIPAA, GLBA, SEC, CIRCIA, FCA, DORA)
  without explicit localization — flags these and recommends specialist counsel
- Guarantee regulatory outcome or admissibility of any evidence preserved

**Related skills (integration map):**

- `legalcode-breach-severity-assessment` — upstream harm triage; invoke at the personal
  data scope assessment decision gate (Step 5c)
- `legalcode-breach-regulatory-notification-drafter` — downstream; hand off for drafting
  regulatory notification documents once notification decision is made (Step 7)
- `legalcode-us-breach-notification-triage` — US-specific obligation mapping; invoke
  in parallel when US residents are affected
- `legalcode-dsar-workflow-builder` — post-breach data subject rights management;
  invoke at the post-incident phase for managing individual access, correction, and
  deletion requests arising from the breach

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. It covers six primary regulatory regimes and
provides [JURISDICTION-SPECIFIC] markers where local law diverges. All timelines
and thresholds must be verified against current official guidance.

| Regime            | Primary Instrument                                                                           | Regulator                            | Key Obligation                                                        | Status                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------- | ------------------------------------ | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **EU (GDPR)**     | Regulation 2016/679, Art. 33-34; EDPB Guidelines 9/2022                                      | Lead DPA (one-stop-shop)             | 72h controller notification; individual notification for high-risk    | VERIFIED                                                                                |
| **EU (NIS2)**     | Directive 2022/2555, Art. 23                                                                 | National CSIRT / Competent Authority | 24h early warning; 72h notification; 1-month final report             | VERIFIED [JURISDICTION-SPECIFIC: transposition uneven, check national implementing law] |
| **UK**            | UK GDPR (retained); DUA Act 2025                                                             | ICO                                  | 72h notification                                                      | VERIFIED [CHECK CURRENCY: DUA Act 2025 amendments]                                      |
| **United States** | 50 state laws + DC; HIPAA 45 CFR §§164.400-414; SEC Form 8-K Item 1.05; GLBA Safeguards Rule | State AGs; HHS; SEC; FTC             | Varies: 30-90 days state; 60 days HIPAA; 4 business days SEC          | [VERIFY per state; use legalcode-us-breach-notification-triage]                         |
| **Australia**     | Privacy Act 1988 Part IIIC; NDB Scheme                                                       | OAIC                                 | 30-day assessment; notify ASAP after eligible breach confirmed        | VERIFIED [VERIFY current OAIC guidance]                                                 |
| **Canada**        | PIPEDA + SOR/2018-64; Quebec Law 25 Arts. 3.5-3.6; BC/AB PIPA                                | OPC; CAI; provincial commissioners   | As soon as feasible (no hard PIPEDA deadline); Quebec: 72h equivalent | VERIFIED [VERIFY]                                                                       |
| **Singapore**     | PDPA; NDB Regulations                                                                        | PDPC                                 | 3 days (regulator); 30 days (individuals)                             | [VERIFY current PDPC guidance]                                                          |
| **New Zealand**   | Privacy Act 2020 Part 6                                                                      | Privacy Commissioner                 | 72h if serious harm likely                                            | [VERIFY]                                                                                |

[JURISDICTION-SPECIFIC] For organizations subject to sector-specific overlays:

- **HIPAA/HITECH** (US healthcare): 60-day notification; HIPAA Security Rule IR requirements [VERIFY]
- **GLBA** (US financial): FTC Safeguards Rule; 30-day notification for unauthorized access to 500+ customers (amended 2024) [VERIFY]
- **SEC** (US public companies): Form 8-K Item 1.05; 4 business days from materiality determination [VERIFY]
- **DORA** (EU financial entities): Major ICT incident reporting, separate from NIS2 [VERIFY]
- **NIS2 sector-specific** (essential vs. important entities): Check national implementing legislation [JURISDICTION-SPECIFIC]

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** points at key decision forks. Rather than assuming context,
the workflow pauses and asks when the answer would change the direction or output. Use
structured options where provided. If the user has already provided the information, skip
the question and proceed.

**Critical first clarification**: The skill operates in two fundamentally different modes.
Determine mode before any further steps.

---

## Workflow

### Step 1: Determine Operating Mode

**⟁ CLARIFY** — Before anything else, determine how this skill is being invoked:

1. **Operating mode**: How is this skill being invoked?
   - **Plan-Building Mode**: Building or updating an IRP before any incident occurs. Full
     output: complete plan document, all templates, RACI matrix, tabletop scenarios,
     maintenance schedule. Standard timeline (hours to days).
   - **Live Incident Response Mode**: Active incident underway. Output is sequenced by
     urgency: severity classification and containment decision first, regulatory clock
     status second, notification decisions third, documentation last. Time-critical.
   - _Why this matters_: Live mode prioritizes speed; plan-building mode prioritizes
     comprehensiveness. Wrong mode = wrong output priority sequence.

2. **Organizational context** (collect before proceeding):
   - **Organization type**: What sector does the organization operate in?
     - Options: Healthcare (HIPAA), Financial services (GLBA/DORA), Critical infrastructure
       (NIS2 essential entity), Technology/SaaS, Retail/e-commerce, Public sector,
       Multi-sector, Other
   - **Regulatory footprint**: Which jurisdictions process personal data or operate services?
     - Allow multiple selections: EU/EEA, UK, United States, Australia, Canada, Singapore,
       New Zealand, Global/Unknown
   - **Entity type** (GDPR/NIS2 context): Controller, Processor, Joint Controller, NIS2
     essential entity, NIS2 important entity, Not applicable, Unknown
   - **IRP maturity**: Starting from scratch, Updating an existing plan, Responding to
     an audit gap, Testing with tabletop exercises, Other

3. **Incident facts** (if Live Incident Response mode):
   - Discovery timestamp (exact: date, time, timezone)
   - Nature of incident (ransomware, data exfiltration, unauthorized access, insider
     threat, DDoS, supply chain, cloud misconfiguration, other)
   - Systems/data affected (confirmed vs. suspected)
   - Containment status (contained, active, unknown)
   - Is personal data involved? (confirmed yes, suspected, no, unknown)
   - Has external counsel been engaged? (yes, no, being arranged)

### Step 2: Assess Regulatory Landscape

Based on the organizational context gathered in Step 1, determine which regulatory
regimes apply. This shapes every subsequent decision.

**Run the regulatory applicability checklist:**

| Question                                                         | If Yes → Regime Applicable                                                                               |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Does the organization process personal data of EU/EEA residents? | GDPR Art. 33-34                                                                                          |
| Is the organization an essential or important entity under NIS2? | NIS2 Art. 23 [JURISDICTION-SPECIFIC: check national implementation]                                      |
| Does the organization process personal data of UK residents?     | UK GDPR / ICO                                                                                            |
| Are US residents or their data involved?                         | State breach notification laws (all applicable states); invoke `legalcode-us-breach-notification-triage` |
| Is the organization a US public company?                         | SEC Form 8-K Item 1.05; materiality assessment required                                                  |
| Does the organization handle US health information?              | HIPAA BNR [VERIFY: refer to HIPAA specialist counsel]                                                    |
| Are Australian residents or their data involved?                 | Australian Privacy Act / NDB Scheme / OAIC                                                               |
| Are Canadian residents involved?                                 | PIPEDA + SOR/2018-64; Quebec Law 25 (Quebec residents)                                                   |
| Are Singapore residents involved?                                | PDPA / PDPC [VERIFY]                                                                                     |

[JURISDICTION-SPECIFIC] For NIS2 specifically: the directive required transposition into
national law by October 17, 2024. Implementation varies significantly across EU member
states. Always identify the specific member state law, not just the Directive text. As of
March 2026, infringement procedures are open against multiple states for incomplete
transposition. [VERIFY current transposition status for each relevant member state]

**⟁ CLARIFY** — If the regulatory footprint is uncertain:

- "The regulatory regimes applicable to this incident depend on where the affected data
  subjects reside, not where your organization is headquartered. If the data subjects'
  residences are unknown, which conservative approach should we take?"
  - Options: Assume multi-jurisdiction (most protective); Assume home jurisdiction only
    (fastest); Map known data locations to jurisdictions; Let me provide details

### Step 3: Gather Legal Research

Use **legalcode-mcp** (if connected) to gather jurisdiction-specific legal authority:

1. Search for current notification timelines and thresholds for each applicable regime
2. Search for recent regulator guidance and enforcement decisions relevant to the incident type
3. Search for case law on attorney-client privilege for cybersecurity investigations in
   applicable jurisdiction(s)
4. Search for sector-specific regulatory requirements if sector overlays apply

Save results to a local temporary reference file at `/tmp/legalcode-irp-research.md`:

```markdown
# Legal Research — Incident Response Plan

## Organization: [name]

## Date: [date]

## Applicable Regimes: [list]

### Notification Timelines and Thresholds (VERIFIED)

- [Regime, article, current timeline, threshold, source]

### Regulatory Guidance

- [Regulator, guidance document, key holdings]

### Privilege Case Law

- [Case, citation, key holding — VERIFIED or [VERIFY]]

### Sector-Specific Overlays

- [Regime, requirements, specialist counsel recommended: Y/N]
```

**If legalcode-mcp is not connected:**

- Proceed with framework knowledge documented in this skill
- Mark all specific timelines, thresholds, and citations with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`

### Step 4: Severity Classification

Classify the incident severity using the framework in the **Severity Classification
Reference** section. For Plan-Building mode, use this section to populate the IRP's
severity classification policy. For Live Incident Response mode, classify the active
incident now before proceeding.

**⟁ CLARIFY** — For Live Incident Response mode, if severity is ambiguous:

- "Based on what is currently known, I would classify this as [P1/P2] because [rationale].
  Key unknown that could change this: [unknown]. Should I proceed with this classification
  while investigation continues, or gather more facts first?"

**Severity affects everything that follows** — escalation path, response SLAs, privilege
activation, notification timing, communication sequence, and regulatory clock assessment.

### Step 5: Activate Legal Privilege Track (if P1 or P2)

For P1 and P2 incidents — and for any incident where litigation or regulatory enforcement
is reasonably anticipated — activate the Legal Privilege Track immediately.

**⟁ CLARIFY** — Privilege track decision:

- Has outside breach counsel been engaged? (yes/no/arranging)
- Has outside counsel retained the forensics firm directly? (yes/no/not yet)
- _Why this matters_: If forensics were engaged before outside counsel, privilege may
  already be compromised for materials produced to date. Outside counsel must review
  the situation and advise on damage limitation.

**Privilege track activation checklist** (all items required before Investigation Track B begins):

- [ ] Outside counsel engaged and confirmed as directing the investigation
- [ ] Forensics firm engagement letter from outside counsel references "anticipation of litigation"
- [ ] Dual-track investigation structure documented (see **Legal Privilege Framework**)
- [ ] Investigation Track B materials labeled "Attorney-Client Privileged / Attorney Work Product"
- [ ] Distribution list for forensic reports approved by outside counsel only
- [ ] Legal hold notice issued for all relevant custodians
- [ ] Legal hold covers: all incident-related logs, emails, Slack/Teams messages, forensic outputs

**If outside counsel is not yet engaged:** Stop. Engage outside breach counsel before
any forensic investigation proceeds. This is the most common — and most costly — privilege
mistake in incident response.

See **Legal Privilege Framework** section for the full dual-track investigation model.

### Step 6: Personal Data Scope Assessment and Notification Decision

Determine whether the incident involves personal data and whether regulatory notification
is required.

**Invoke `legalcode-breach-severity-assessment`** for harm triage if personal data
involvement is confirmed or suspected. This produces the risk assessment needed for the
notification decision.

Use the **Regulatory Notification Decision Tree** to determine:

1. Which regimes are triggered
2. Which thresholds are met
3. Which notification clocks are running and when they expire
4. Whether individual notification is required in addition to supervisory authority notification

**⟁ CLARIFY** — Notification decision (if borderline):

- "The harm assessment is borderline under [regime]. Notification is triggered if
  [threshold condition]. Based on current facts, I assess this as [likely / unlikely /
  uncertain] to meet the threshold because [rationale]. Should I: (a) proceed to draft
  notification (safe-harbor approach), (b) document the not-notifiable decision with
  rationale, or (c) await further investigation before deciding?"
- _Why this matters_: Erring toward notification is generally safer regulatorily;
  erring toward non-notification preserves confidentiality and avoids potentially
  premature or inaccurate public record.

**When notification decision is made:** Hand off to `legalcode-breach-regulatory-notification-drafter`
for the actual drafting of notification documents. Do not duplicate that skill's
capability here.

### Step 7: Execute IRP Phases (Operational Response)

Based on the severity classification and current incident phase, execute the applicable
IRP phase guidance:

**For Plan-Building mode:** Build out the IRP document using the phase frameworks below
as the structural backbone.

**For Live Incident Response mode:** Navigate directly to the current phase and execute.

See **Incident Lifecycle Reference** for the deep-dive guidance on each phase.

**Parallel workstreams** (do not sequence these — run simultaneously):

- Containment and eradication (IT Security / CISO)
- Legal and regulatory analysis (Legal / DPO / External Counsel)
- Communications management (Communications / CEO)
- Evidence preservation (Legal / Forensics)
- Notification decision and filing (DPO / External Counsel)

### Step 8: Generate IRP Document Package

Assemble the complete IRP document package. The package components are:

| Component                                  | Mode       | Priority      |
| ------------------------------------------ | ---------- | ------------- |
| IRP Policy Statement (executive mandate)   | Plan-Build | Required      |
| Severity Classification Framework          | Both       | Required      |
| Incident Response Team Roster + RACI       | Plan-Build | Required      |
| Incident Response Workflow Diagrams        | Plan-Build | Required      |
| Regulatory Notification Decision Tree      | Both       | Required      |
| Legal Privilege Architecture               | Both       | Required      |
| Evidence Preservation Protocol             | Both       | Required      |
| Communication Templates (6 types)          | Both       | Required      |
| Tabletop Exercise Scenarios (3 scenarios)  | Plan-Build | Required      |
| Post-Incident Review Template              | Both       | Required      |
| IRP Maintenance Schedule                   | Plan-Build | Required      |
| Playbook Appendix (tool roster, retainers) | Plan-Build | Recommended   |
| Sector-Specific Overlay Annexes            | Plan-Build | If applicable |

**⟁ CLARIFY** — For Plan-Building mode with time constraints:

- "The full IRP package has [N] components. Should I produce all components now, or
  prioritize? Recommended priority order: (1) severity framework + RACI — these guide
  all live response decisions; (2) regulatory decision tree — governs notification
  obligations; (3) communication templates — needed immediately in any incident; (4)
  tabletop scenarios — used for testing the plan."

### Step 9: Tabletop Exercise Design

Design tabletop exercises calibrated to the organization's sector, threat model, and
IRP maturity level. See **Tabletop Exercise Framework** for three scenarios with inject
cards, discussion questions, evaluation rubrics, and gap identification templates.

**⟁ CLARIFY** — Tabletop scope:

- "Should the tabletop exercises focus on: (a) all three scenarios (comprehensive
  3-session program), (b) the most relevant scenario for your threat model (single
  focused session), or (c) scenario customization (I'll adapt a scenario to a specific
  threat you want to test)?"

### Step 10: Quality Verification

Before delivering any IRP output, run the full quality verification:

1. Run the **5 Citation Quality Gates** silently. Revise failures before delivery.
2. For any P1 severity determination in the live incident track, run the **3-pass
   Self-Interrogation**.
3. Assign **Confidence Scores** to all regulatory notification conclusions.
4. Verify all [JURISDICTION-SPECIFIC] markers are placed correctly.
5. Verify dual-track privilege architecture is correctly structured.
6. Generate the **Glass Box Audit Trail** and append to output.

---

## Incident Lifecycle Reference

### Phase 1: Preparation

**Purpose:** Build the organizational capability to respond effectively before any incident occurs.

**Key activities and owners:**

| Activity                                         | Owner (RACI)                  | Output                     |
| ------------------------------------------------ | ----------------------------- | -------------------------- |
| Draft IRP policy and obtain executive mandate    | Legal/CISO (A: Executive)     | Signed IRP Policy          |
| Identify and train Incident Response Team        | CISO                          | IRT Roster + Skills Matrix |
| Establish RACI matrix                            | CISO + Legal                  | RACI Document              |
| Pre-retain external breach counsel               | Legal (A: GC)                 | Retainer Agreement         |
| Pre-retain forensics firm (through counsel)      | Legal + External Counsel      | Engagement Letter          |
| Pre-retain PR/crisis communications firm         | Communications                | Retainer Agreement         |
| Establish out-of-band communication channel      | CISO + IT                     | Verified Channel           |
| Build asset inventory and data map               | CISO + Privacy                | Asset Register / Data Map  |
| Integrate with `legalcode-data-mapping-workflow` | Privacy/DPO                   | RoPA / Data Flow Diagram   |
| Establish cyber insurance policy                 | Legal + Finance               | Policy Documentation       |
| Define regulatory contact directory              | Legal/DPO                     | Regulator Contact List     |
| Set up evidence preservation infrastructure      | CISO + Legal                  | WORM storage configured    |
| Conduct tabletop exercises (minimum annual)      | CISO + Legal + Communications | Exercise Report            |
| Review and update IRP (minimum annual)           | CISO + Legal                  | IRP Version Log            |

**NIST SP 800-61r3 CSF 2.0 alignment:** Preparation maps to the Govern and Identify
functions. Rev. 3 (April 2025) emphasizes that IR policy must derive from organizational
governance, with senior leadership commitment as a first-order requirement. [VERIFY
current NIST SP 800-61r3 recommendations against published final]

**ISO/IEC 27035-1:2023 alignment:** Preparation covers the "Plan and Prepare" phase,
including mandatory incident management policy, IRT establishment, and documentation
of classification schemes. [VERIFY ISO/IEC 27035-1:2023 and 27035-2:2023]

### Phase 2: Detection and Analysis

**Purpose:** Identify security events, determine whether an incident has occurred, and classify severity.

**Key activities:**

1. **Event detection** — SIEM alerts, EDR telemetry, threat intelligence feeds, user reports,
   third-party notification (vendor/partner breach notification), regulator inquiry
2. **Initial triage** — Is this a security event or confirmed incident? Apply the P1-P4
   classification criteria from the Severity Classification Reference
3. **Incident declaration** — Formal declaration triggers IRP activation, legal privilege
   assessment, and clock tracking
4. **Evidence collection begins** — Do not remediate before forensic preservation is
   initiated. See Evidence Preservation Protocol.
5. **RACI activation** — Notify all roles with Responsible/Accountable assignments for
   the detected severity tier

**Clock management** (critical for compliance):

| Clock                      | Starts                    | Deadline           | Notes                                                   |
| -------------------------- | ------------------------- | ------------------ | ------------------------------------------------------- |
| GDPR Art. 33               | Controller awareness      | 72 hours           | "Awareness" ≠ certainty; reasonable certainty of breach |
| NIS2 Art. 23 early warning | Entity awareness          | 24 hours           | Separate clock from GDPR                                |
| NIS2 Art. 23 notification  | Entity awareness          | 72 hours           | Separate from early warning                             |
| HIPAA BNR (US)             | Discovery                 | 60 days            | [VERIFY]                                                |
| SEC Form 8-K               | Materiality determination | 4 business days    | [VERIFY; requires securities counsel]                   |
| State breach laws (US)     | Discovery (most states)   | Varies (5-90 days) | Use legalcode-us-breach-notification-triage             |
| Australian NDB             | Awareness                 | 30 days to assess  | Then prompt notification                                |

**Awareness vs. discovery distinction:** Most US state laws use "discovery" as the clock trigger.
GDPR and NIS2 use "awareness" — the moment the controller/entity has a reasonable degree
of certainty that a breach has occurred. These are not the same date. Document both with
timestamps. [JURISDICTION-SPECIFIC]

### Phase 3: Containment

**Purpose:** Stop the bleeding. Prevent further damage while preserving evidence.

**Short-term containment (hours):**

- Network isolation of affected systems
- Account lockout / credential resets for compromised accounts
- Block known attacker infrastructure at perimeter
- **Do not wipe or rebuild yet** — forensic imaging must precede any system modification

**Long-term containment (days):**

- Temporary operational configurations allowing business continuity
- Enhanced monitoring of adjacent systems
- Parallel clean-system rebuild (for P1)

**Legal hold trigger:** Issue legal hold notice for all relevant document custodians
simultaneously with containment actions. Do not allow normal document retention/deletion
policies to continue. See Evidence Preservation Protocol.

**Privilege gate:** Route all forensic investigation scoping, findings, and communications
through outside counsel. See Legal Privilege Framework.

**⟁ CLARIFY** — Containment authorization level:

- For P1: Pre-authorize CISO to take containment actions without real-time executive
  approval? (yes, with post-action notification / no, real-time sign-off required)
- _Why this matters_: Bureaucratic approval chains during P1 incidents cost hours that
  directly harm regulatory compliance deadlines and damage scope.

### Phase 4: Eradication

**Purpose:** Remove the threat actor and their artifacts from the environment.

**Key activities:**

- Root cause analysis (conducted through legal track if privilege maintained)
- Threat actor removal: malware eradication, backdoor closure, persistence mechanism removal
- IOC-based sweeping: search all systems for indicators of compromise
- Patch all exploited vulnerabilities
- Rebuild compromised systems from verified clean backups or golden images
- Verify backup integrity (confirm backups are not also compromised)
- Reset all credentials that may have been exposed

**Eradication authorization:** CISO is accountable for technical eradication authorization.
Legal and DPO must confirm that notification obligations do not require preservation of
evidence that eradication would destroy.

### Phase 5: Recovery

**Purpose:** Restore systems and services to production; monitor for recurrence.

**Key activities:**

- Gradual production cutover with enhanced monitoring
- Validate system integrity before each cutover step
- Monitor for attacker re-entry for at least 30 days post-recovery
- Business impact assessment: what data was unavailable, what operations were disrupted
- Recovery authorization: CISO accountable; business units confirm acceptable state
- Communicate recovery status to affected internal and external stakeholders
- File any required supplementary regulatory notifications (NIS2 1-month final report; GDPR supplements)

### Phase 6: Post-Incident Activity

**Purpose:** Learn from the incident; improve the plan; close regulatory loops.

**Blameless post-incident review (PIR):**

- Conduct within 2 weeks of recovery (for P1) or 4 weeks (for P2/P3)
- Explicitly blameless culture: the goal is systemic improvement, not individual fault
- Attendees: full IRT including legal, communications, business units
- Review: timeline, decision quality, communication effectiveness, tool gaps, process failures
- Outputs: IRP update action items with owners and deadlines; regulatory follow-up items

**Regulatory follow-up:**

- File NIS2 Art. 23 final report (1 month after initial notification) [VERIFY]
- File GDPR supplementary notification if phased filing was used
- Respond to any regulator requests for additional information
- Update GDPR breach register (Art. 33(5): all incidents must be documented even if not notified)

**Litigation readiness assessment:**

- Work with outside counsel to assess civil litigation risk (class action, customer claims)
- Preserve all evidence per the legal hold — do not release hold until litigation risk assessed
- Document all decisions, rationales, and timelines for defensive use

---

## Severity Classification Reference

### P1 — CRITICAL

**Definition (any single criterion triggers P1):**

- Confirmed exfiltration, encryption, or destruction of personal data affecting ≥10,000 individuals
- Any exfiltration involving special-category data (health, biometric, financial account, government
  ID, children's data, criminal record) regardless of volume
- Active ransomware with production systems offline or at imminent risk
- Nation-state or APT attribution confirmed or credibly suspected
- Critical infrastructure disruption (energy, healthcare, financial services, water, transport)
- Board-reportable under SEC Form 8-K or equivalent (public company disclosure obligation)
- Regulatory notification clock already running under any jurisdiction
- Threat actor with confirmed persistent access (active intrusion)
- Supply chain compromise affecting all downstream customers
- Public exposure confirmed (dark web posting, journalist inquiry received)

**Response SLAs:**

- IR team assembled: within 30 minutes
- Containment strategy decision: within 2 hours
- Executive notification: within 2 hours
- External counsel + forensics engaged: same day (within 4 hours)
- GDPR/NIS2 early warning filed (if triggered): within 24 hours
- GDPR/NIS2 formal notification (if triggered): within 72 hours

**Escalation chain:** CISO → GC/Legal → CEO → Board Chair → External Counsel → Forensics

---

### P2 — HIGH

**Definition (any single criterion triggers P2):**

- Confirmed personal data breach involving 500–9,999 individuals, standard categories
- Suspected breach with high probability of personal data compromise, active investigation
- Significant system compromise; containment achieved; exfiltration unconfirmed
- Third-party/vendor breach with confirmed access to the organization's data
- Regulatory inquiry received referencing a potential security incident
- Business email compromise resulting in data exposure or financial fraud

**Response SLAs:**

- IR team assembled: within 2 hours
- CISO and Legal notified: within 4 hours
- Privacy/DPO harm assessment begun: within 8 hours
- Executive update: within 12 hours
- Notification decision finalized: within 24-48 hours

**Escalation chain:** CISO → GC/Legal + DPO → CEO (if material) → External Counsel (standby)

---

### P3 — MEDIUM

**Definition (triggers P3 absent P1/P2 criteria):**

- Potential breach under investigation; personal data compromise not yet confirmed
- Confirmed incident affecting only internal or non-personal data
- Security event with limited blast radius (single system, no confirmed external exfiltration path)
- Lost or stolen encrypted device (device locked; remote wipe available)
- DDoS causing service degradation without data access

**Response SLAs:**

- Investigation commenced: within 4 hours
- Privacy/DPO and IT Security notified: within 8 hours
- First status report to management: within 24 hours
- Resolution or escalation decision: within 72 hours

---

### P4 — LOW

**Definition (all criteria must be met):**

- No personal data involved, or personal data access is confirmed impossible
- Contained within internal systems; no external access path
- No regulatory notification obligation under any applicable jurisdiction
- Minor policy violation with no confirmed data risk

**Response SLAs:**

- Incident logged: same business day
- IT Security team review: within 5 business days
- Monthly aggregate trend report to CISO

**Escalation trigger from P4 → P3:** Any finding of potential personal data access or
external access path during investigation.

---

## RACI Matrix

Adapt this RACI to the organization's actual structure. Every **A** cell must map to a
named individual, not just a role, in the organization-specific playbook.

**Role abbreviations:** CIS = CISO/IT Security | LEG = Legal/GC | DPO = Privacy/DPO |
COM = Communications | EXE = Executive/CEO | HR = HR | EXT = External Counsel |
FOR = Forensics Firm | BUL = Business Units

| Activity                                 |  CIS  |  LEG  |  DPO  | COM |  EXE  | HR  |  EXT  | FOR | BUL |
| ---------------------------------------- | :---: | :---: | :---: | :-: | :---: | :-: | :---: | :-: | :-: |
| Event detection and logging              |   R   |   I   |   I   |  —  |   I   |  —  |   —   |  —  |  C  |
| Initial severity classification          |   R   |   C   |   C   |  —  |   I   |  —  |   —   |  —  |  C  |
| Incident declaration (formal)            |   R   |   C   |   C   |  —  |   A   |  —  |   —   |  —  |  I  |
| Containment decision and execution       |   R   |   C   |   C   |  —  |   A   |  —  |   C   |  C  |  C  |
| Legal privilege track activation         |   C   | **A** |   C   |  —  |   I   |  —  |   R   |  —  |  —  |
| Legal hold issuance                      |   C   | **A** |   C   |  —  |   I   |  I  |   R   |  —  |  —  |
| Forensic firm engagement (via counsel)   |   C   | **A** |   I   |  —  |   I   |  —  |   R   |  R  |  —  |
| Evidence preservation / chain of custody |   C   |   C   |   I   |  —  |   I   |  —  | **A** |  R  |  —  |
| Personal data scope assessment           |   C   |   C   | **A** |  —  |   I   |  —  |   C   |  C  |  C  |
| Harm assessment (GDPR/privacy)           |   I   |   C   | **A** |  —  |   I   |  —  |   C   |  —  |  C  |
| Regulatory notification decision         |   C   |   C   | **A** |  —  |   A   |  —  |   C   |  —  |  —  |
| GDPR/UK Art. 33 notification filing      |   I   |   C   | **A** |  —  |   I   |  —  |   C   |  —  |  —  |
| NIS2 early warning filing                |   I   |   C   |   R   |  —  |   I   |  —  | **A** |  —  |  —  |
| NIS2 formal notification filing          |   I   |   C   |   R   |  —  |   I   |  —  | **A** |  —  |  —  |
| US state notification filing             |   I   |   C   |   R   |  —  |   I   |  —  | **A** |  —  |  —  |
| Individual data subject notification     |   I   |   C   | **A** |  R  |   I   |  —  |   C   |  —  |  —  |
| Law enforcement referral decision        |   C   | **A** |   I   |  —  |   I   |  I  |   C   |  —  |  —  |
| Internal employee communication          |   I   |   C   |   I   |  R  | **A** |  C  |   —   |  —  |  I  |
| Executive / board update                 |   C   |   C   |   C   |  —  |   R   |  —  |   C   |  —  |  —  |
| Media / public statement                 |   C   |   C   |   R   |  R  | **A** |  —  |   C   |  —  |  —  |
| Customer / partner notification          |   C   |   C   |   C   |  R  | **A** |  —  |   C   |  —  |  R  |
| Cyber insurance claim notification       |   I   |   R   |   I   |  —  | **A** |  —  |   C   |  —  |  —  |
| Eradication authorization                | **A** |   I   |   I   |  —  |   I   |  —  |   —   |  C  |  C  |
| Recovery authorization                   | **A** |   I   |   I   |  —  |   I   |  —  |   —   |  C  |  C  |
| Post-incident review facilitation        |   R   |   C   |   C   |  C  |   I   |  C  |   —   |  C  |  C  |
| Lessons learned dissemination            |   R   |   C   |   C   |  C  | **A** |  I  |   —   |  —  |  I  |
| IRP update and version control           | **A** |   C   |   C   |  —  |   I   |  —  |   —   |  —  |  —  |
| Tabletop exercise design and delivery    |   R   |   C   |   C   |  —  |   I   |  —  |   —   |  —  |  C  |

[JURISDICTION-SPECIFIC] The DPO/Legal accountability split for regulatory notification
decisions:

- **EU/UK incidents (GDPR):** DPO owns the technical filing obligation; Legal/GC owns
  the strategic advice on what and when to file. In practice, co-accountability.
- **US incidents:** General Counsel typically owns the notification decision; state law
  counsel reviews per-state obligations.
- **NIS2 incidents:** Legal typically owns the CSIRT notification (operational security
  dimension); DPO co-owns where the incident also constitutes a personal data breach.

---

## Regulatory Notification Decision Tree

Traverse each gate sequentially. A "Yes" at any gate does not prevent further traversal —
continue through all gates to identify all notification obligations.

```
[INCIDENT CONFIRMED]
        |
        v
[GATE 1] Was personal data accessed, exfiltrated, altered, or destroyed
         without authorization?
  NO → Log as pure security incident. No data breach notification.
       Proceed to eradication. P3/P4 handling.
  YES / UNKNOWN →
        |
        v
[GATE 2] What is the entity's role in relation to this data?
  PROCESSOR only → Notify the relevant Controller(s) without undue delay
                   (GDPR: EDPB recommends within 24h). Clock runs for Controller.
                   Also assess NIS2 notification if entity is essential/important.
  CONTROLLER (partly or wholly) →
        |
        v
[GATE 3] Could the breach result in ANY risk to the rights and freedoms
         of natural persons?
  UNLIKELY (document risk assessment) → No Art. 33 notification required.
                                         Document decision in breach register.
  POSSIBLE or UNCERTAIN →
        |
        v
[GATE 4] Which jurisdiction's law governs? [Check ALL that apply]

  ┌──────────────────────────────────────────────────────────────────┐
  │ EU/GDPR (EEA residents affected)                                 │
  │ → NOTIFY: Lead DPA (one-stop-shop mechanism if multi-EU)         │
  │   Timeline: Art. 33 → 72 hours from awareness                   │
  │   Content: 4 mandatory elements (Art. 33(3)(a)-(d))             │
  │   Phased filing: permitted if info not all available at 72h      │
  │   → Invoke legalcode-breach-regulatory-notification-drafter      │
  ├──────────────────────────────────────────────────────────────────┤
  │ UK GDPR (UK residents affected)                                  │
  │ → NOTIFY: ICO                                                    │
  │   Timeline: 72 hours from awareness                             │
  │   [CHECK CURRENCY: DUA Act 2025 amendments]                     │
  │   → Invoke legalcode-breach-regulatory-notification-drafter      │
  ├──────────────────────────────────────────────────────────────────┤
  │ NIS2 (organization is essential/important entity in EU)          │
  │ → NOTIFY: National CSIRT / Competent Authority                   │
  │   Stage 1 — Early warning: 24 hours from awareness              │
  │   Stage 2 — Incident notification: 72 hours from awareness      │
  │   Stage 3 — Final report: 1 month after Stage 2                 │
  │   [JURISDICTION-SPECIFIC: check national implementing law]       │
  │   [Note: NIS2 + GDPR may require SIMULTANEOUS notifications      │
  │    to different authorities]                                      │
  ├──────────────────────────────────────────────────────────────────┤
  │ United States (US residents affected)                            │
  │ → NOTIFY: Multiple state AGs; federal sector regulators          │
  │   → Invoke legalcode-us-breach-notification-triage for all      │
  │   applicable state deadlines and AG thresholds                  │
  │   Public company? → SEC Form 8-K Item 1.05: 4 business days     │
  │   from materiality determination [VERIFY; securities counsel]   │
  │   HIPAA covered entity/BA? → HHS: 60 days [VERIFY; specialist]  │
  ├──────────────────────────────────────────────────────────────────┤
  │ Australia (AU residents affected)                                │
  │ → NOTIFY: OAIC (Notifiable Data Breach Statement)               │
  │   Timeline: Expeditiously; 30-day assessment window             │
  │   Eligible breach threshold: serious harm likely [VERIFY]       │
  ├──────────────────────────────────────────────────────────────────┤
  │ Canada (CA residents affected)                                   │
  │ → NOTIFY: OPC (PIPEDA + SOR/2018-64) + provincial               │
  │   commissioners (Quebec Law 25: 72h equivalent)                  │
  │   → Invoke legalcode-breach-regulatory-notification-drafter     │
  ├──────────────────────────────────────────────────────────────────┤
  │ Other jurisdictions                                              │
  │ → [VERIFY applicable regime and timeline]                        │
  │   Singapore PDPA: 3 days (PDPC) [VERIFY]                        │
  │   New Zealand Privacy Act 2020: 72h if serious harm [VERIFY]    │
  └──────────────────────────────────────────────────────────────────┘

        |
        v
[GATE 5] Does the incident involve special-category or sensitive data?
  YES (health, biometric, financial, children, government ID, racial/ethnic,
       religious, sexual orientation, criminal record) →
       Presumption of HIGH RISK. Proceed directly to Gate 6 as "high risk."
       Escalate to P1 if not already classified.
  NO →
        |
        v
[GATE 6] Does the breach pose HIGH RISK to affected individuals?
         (GDPR Art. 34 threshold; higher than Art. 33)
  HIGH RISK (confirmed or likely) →
       → Individual notification REQUIRED (GDPR Art. 34; UK equivalent;
         similar triggers apply in US, AU, CA)
       → Time: without undue delay (EU/UK — no explicit hour clock;
         US states: same individual deadline as regulator or separate)
       → Channel: email, letter, or where disproportionate effort → public notice
       → Use communication Template 4 (Affected Individual Notification)
  NO HIGH RISK →
       → Supervisory authority notification only; document rationale
        |
        v
[GATE 7] Dual-notification scenario? (NIS2 + GDPR simultaneously)
  YES → Identify whether both the CSIRT (NIS2) and the DPA (GDPR) have
        been notified. These are separate filings to separate authorities.
        Timeline: NIS2 24h early warning may fire before GDPR 72h clock.
        [Note: EU Digital Omnibus single-entry-point proposal not yet
        enacted as of March 2026 — file both separately until law changes]
  NO →
        |
        v
[GATE 8] Are you within all applicable notification windows?
  IN WINDOW → Draft and file. Invoke legalcode-breach-regulatory-notification-drafter.
  WINDOW EXPIRED → File late notification with explicit acknowledgment and
                   mitigation measures. Document all steps taken to expedite.
                   Consult legal counsel before filing to manage enforcement risk.
  BORDERLINE / CLOCK START DISPUTED → ⟁ CLARIFY: Seek legal sign-off on
                   clock start date interpretation before filing.
```

---

## Legal Privilege Framework

The legal privilege architecture is a structural constraint on incident response, not
an optional consideration. Privilege decisions made in the first hours determine whether
the organization can protect its investigation from civil discovery and regulatory scrutiny.

### The Dual-Track Investigation Model

Establish two structurally separate tracks on Day 1 of any P1 or P2 incident:

**Track A — Business Continuity / Regulatory Track**

- Operated by: IT Security, Privacy/DPO, Compliance, IT Operations
- Purpose: Containment, system restoration, regulatory notification preparation, business continuity
- Communications: **Not privileged.** Subject to discovery, regulatory review, and Freedom of Information requests.
- Deliverables: Incident tickets, remediation plans, regulatory notification drafts, business status reports
- Label: [BUSINESS TRACK — Not Privileged]

**Track B — Legal Investigation Track**

- Operated by: Outside Breach Counsel (not solely in-house counsel) directing the forensics firm
- Purpose: Legal advice, litigation strategy, privileged investigation for anticipation of litigation
- Communications: Attorney-Client Privileged / Attorney Work Product
- Deliverables: Privileged investigation memorandum (not a standalone forensic report designed for broad use)
- Distribution: Outside counsel approves every recipient before sharing
- Label: **ATTORNEY-CLIENT PRIVILEGED — DO NOT DISTRIBUTE WITHOUT COUNSEL APPROVAL**

### Privilege Protection Checklist

Run this checklist at the first privilege gate (Step 5 of the workflow):

- [ ] Outside breach counsel engaged, confirmed in writing, and directing Track B
- [ ] Forensics firm retained by outside counsel under separate engagement letter
- [ ] Forensics engagement letter states: "work performed to assist in rendering legal
      advice and in anticipation of potential litigation or regulatory enforcement action"
- [ ] All forensic deliverables addressed to outside counsel, not to the organization directly
- [ ] Forensic report distribution list approved by outside counsel before any sharing
- [ ] Business continuity team receives only technical remediation findings (not the
      full privileged investigation report)
- [ ] All Track B email and document communications labeled "Attorney-Client Privileged"
- [ ] Separate document custodian for privileged materials; access log maintained
- [ ] Litigation hold issued for all relevant custodians (contemporaneous with or before investigation)
- [ ] Forensic payments classified as legal expenses (not regular IT operational costs)

### Privilege Risk Factors (and Mitigations)

| Risk Factor                                                           | Mitigation                                                                                                                                 |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Forensics firm retained before counsel engaged                        | Engage counsel immediately; counsel reviews and re-retains if possible; assess extent of privilege contamination                           |
| Forensic report shared broadly within organization                    | Limit distribution retroactively; consult outside counsel on privilege waiver risk                                                         |
| Forensic report designed for regulatory submission (not legal advice) | Restructure deliverables: counsel drafts privileged memo incorporating findings; regulatory notification drafted separately from this memo |
| In-house counsel only (no outside counsel)                            | Obtain outside breach counsel for the investigation; in-house counsel's work product may have narrower privilege protection                |
| Communications about legal strategy sent on business email            | Use dedicated secure channel; limit to Track B participants; label appropriately                                                           |

[VERIFY] Current privilege case law in applicable jurisdiction. As of early 2026, courts
in the US have increasingly scrutinized forensic privilege claims where the primary purpose
of the investigation was regulatory compliance rather than litigation preparation. The
dual-track model is the current best practice to address this scrutiny. [VERIFY against
current case law with outside counsel]

### Kovel Doctrine Application

Under the Kovel doctrine, communications between lawyers and forensic third parties who
are "instrumental to providing legal advice" may be protected under attorney-client
privilege (analogous to a translator or forensic accountant working under counsel's
direction). This protection depends on: (a) the third party being retained by and
reporting to counsel; (b) the work being necessary to enable counsel to give legal advice;
and (c) the communications being treated as confidential. [VERIFY with outside counsel
for applicable jurisdiction]

---

## Evidence Preservation Protocol

### Legal Hold

**Trigger:** Issue legal hold notice immediately upon:

- Any P1 or P2 incident classification (default trigger)
- Any confirmed personal data breach (regardless of classification)
- Receipt of regulatory inquiry, subpoena, or law enforcement contact related to a security incident
- Any indication that litigation (civil, criminal, or regulatory) is reasonably anticipated
- Explicit instruction from outside breach counsel

**Legal hold notice must cover all custodians** with potentially relevant:

- Security event logs (SIEM, EDR, firewall, proxy, VPN)
- Active Directory / Entra ID authentication logs
- Cloud audit logs (AWS CloudTrail, Azure Monitor, GCP Cloud Audit Logs)
- Email and messaging systems (Outlook, Gmail, Slack, Teams, Zoom)
- Incident response tickets and documentation
- All forensic outputs (images, reports, evidence packages)
- Communication records related to the incident (internal and external)
- Contracts and agreements with affected vendors / customers

**Monitoring requirement:** Issuing the hold notice is insufficient. Counsel must follow up
to confirm the hold is implemented and maintained. Establish a legal hold monitoring schedule.

### Chain of Custody Documentation

For each item of evidence, maintain a custody record containing:

1. **Evidence identification:**
   - Description (system, file, log set, disk image, email archive)
   - Unique identifier (hash value: SHA-256)
   - Date/time of collection
   - Collection method and tool (with version)

2. **Provenance:**
   - System from which collected (hostname, IP, OS, cloud resource ID)
   - Who collected (name, role, organization)
   - Authorization basis (legal hold, forensic scope letter)

3. **Integrity verification:**
   - SHA-256 hash at collection
   - SHA-256 hash verification after transfer (must match)
   - Any chain-of-custody breaks noted with explanation

4. **Custody log:**
   - Every person who accessed the evidence (name, role, date/time, purpose)
   - Every transfer (from whom, to whom, date/time, method, signed receipt)

5. **Storage:**
   - Current location (immutable/WORM storage; write-once media; access-controlled vault)
   - Access controls in place

### Forensic Image Integrity

**Required practices:**

- Take bit-for-bit forensic images using validated tools (FTK Imager, dd with verification,
  Magnet AXIOM, or equivalent)
- Generate SHA-256 hash of every image immediately upon capture
- Verify hash before and after every transfer
- Store images on write-once or immutable media (WORM, AWS S3 Object Lock, Azure Blob
  immutable storage, or equivalent)
- Do not modify, defragment, or run antivirus on original evidence drives
- Maintain a separate working copy for analysis; preserve original untouched
- Document all forensic tool versions and settings used

### Log Preservation Requirements

**Log sources to preserve immediately:**

- SIEM (all events for the relevant period)
- EDR/antivirus alerts and telemetry
- Firewall and proxy logs
- VPN authentication logs
- Active Directory / Entra ID sign-in logs and audit logs
- Cloud provider audit logs (auto-purge risk: most providers delete on 30/90/180-day cycles;
  manual preservation must be triggered within hours of incident discovery)
- Email gateway logs (SPF/DKIM failures, attachment analysis)
- Web server access logs
- Application logs for affected systems

**Retention minimum:** Duration of investigation + 2 years, OR applicable statute of
limitations for anticipated litigation (whichever is longer). For GDPR incidents: minimum
5 years per EDPB guidance on breach documentation under Art. 33(5). [VERIFY]

**Export and preservation:** Export logs to tamper-evident, immutable storage. Do not
rely on in-place log systems for long-term preservation — they may be overwritten,
modified, or compromised.

---

## Communication Template Framework

All communications during an active incident must be routed through the privilege determination:

- Track A materials (operational, not privileged): can be shared with appropriate internal audience
- Track B materials (privileged): distribute only with outside counsel approval

**Privilege labeling convention:**

- Track A communications: [BUSINESS TRACK — Not Privileged]
- Track B communications: [ATTORNEY-CLIENT PRIVILEGED — DO NOT DISTRIBUTE]

---

### Template 1: Internal Incident Brief (First Hour)

**Audience:** IR team, CISO, Legal — not yet distributed broadly
**Privilege status:** Prepare under legal track if outside counsel engaged; otherwise Track A
**Format:** Structured fill-in, max 1 page, minutes to complete

```
INTERNAL INCIDENT BRIEF — [BUSINESS TRACK / PRIVILEGED — select]
Incident ID: INC-[YYYYMMDD]-[###]
Discovery timestamp: [Date, time, timezone]
Current timestamp: [Date, time]
Prepared by: [Name, role]

PRELIMINARY SEVERITY: [ ] P1 Critical  [ ] P2 High  [ ] P3 Medium  [ ] P4 Low
Rationale for classification: [2 sentences]

INCIDENT SUMMARY
Nature: [Ransomware / data exfiltration / unauthorized access / other]
Affected systems: [List or "Under investigation"]
Affected data: [Personal data: YES / NO / UNKNOWN | Categories: ]
Containment status: [ ] Contained  [ ] Active  [ ] Unknown

IMMEDIATE ACTIONS REQUIRED
1. [Action] — Owner: [Name] — Deadline: [Time]
2. [Action] — Owner: [Name] — Deadline: [Time]
3. [Action] — Owner: [Name] — Deadline: [Time]

CLOCK STATUS
[ ] GDPR 72h clock: RUNNING (started: [time]) | Expires: [time] | NOT TRIGGERED
[ ] NIS2 24h early warning: RUNNING (started: [time]) | Expires: [time] | NOT TRIGGERED
[ ] Other: [regime, clock status]

LEGAL TRACK STATUS
[ ] Outside counsel engaged (firm: [name]) — privilege track ACTIVE
[ ] Outside counsel not yet engaged — ACTIVATE IMMEDIATELY
[ ] Forensics retained through counsel: YES / NO / IN PROGRESS

KNOWN UNKNOWNS
- [What we don't yet know #1]
- [What we don't yet know #2]

NEXT UPDATE: [Time] — Owner: [Name]
```

---

### Template 2: Executive / Board Notification

**Audience:** CEO, CFO, Board (when required), Audit Committee
**Privilege status:** If legal track active, route through counsel before distribution
**Timing:** P1 within 4 hours; P2 within 12 hours; P3 at 24 hours if escalation warranted
**Format:** 1-2 pages maximum; readable without technical background

```
EXECUTIVE INCIDENT BRIEFING — [CONFIDENTIAL]
Date: [Date, time]
To: [Recipients]
From: [CISO / GC]
Re: Security Incident — [Brief descriptor] — [Severity]

1. WHAT HAPPENED
[2-3 sentences: nature of incident, date/time of discovery, current status.
Confirmed facts only. State explicitly what is still under investigation.]

2. WHAT WE KNOW vs. WHAT WE DON'T KNOW
Known: [confirmed facts]
Unknown: [list key unknowns explicitly]

3. BUSINESS IMPACT
Operational: [Systems affected, services disrupted, duration]
Customer impact: [Scope, if known]
Financial exposure: [Insurance coverage, regulatory fines, litigation risk — preliminary]

4. REGULATORY EXPOSURE
[ ] GDPR notification required — deadline: [time] — status: [filed/draft/pending]
[ ] NIS2 notification required — early warning: [time]; formal: [time]
[ ] Other jurisdictions: [list]
[ ] No regulatory notification required — rationale on file

5. CURRENT RESPONSE STATUS
Containment: [status]
Investigation: [phase, by: inside counsel only / outside counsel directed]
Legal privilege: [protected / not yet protected / under assessment]

6. DECISIONS REQUIRED FROM EXECUTIVE
[ ] Authorize additional budget for [forensics / PR / legal]: $[amount]
[ ] Authorize law enforcement referral
[ ] Authorize public statement (see comms template)
[ ] Authorize ransom payment — NOTE: consult legal + law enforcement first
[ ] [Other decision requiring authorization]

7. NEXT UPDATE: [Date, time] — Owner: [Name]
```

---

### Template 3: Regulatory Notification (Universal Core)

_Use `legalcode-breach-regulatory-notification-drafter` to produce jurisdiction-specific
formatted versions of this content. The elements below are the universal core that every
regulatory notification must address._

**Universal mandatory elements:**

1. Nature of the personal data breach (attack vector, system affected, mechanism of unauthorized access)
2. Categories of personal data affected (contact, financial, health, government ID, etc.)
3. Approximate number of data subjects affected (by category if applicable)
4. Approximate number of data records affected
5. Name and contact details of DPO or responsible contact point
6. Likely consequences of the breach (harm assessment)
7. Measures taken or proposed to address the breach (containment, eradication, remediation)
8. Measures taken or proposed to mitigate adverse effects on data subjects
9. Timeline of events (date of breach, date of discovery/awareness, date of notification)
10. [If phased filing]: statement that initial notification is incomplete; supplementary information to follow

**NIS2-specific additions:**

- Entity classification (essential / important)
- Cross-border impact assessment (other member states, other entities)
- Sector criticality assessment
- Indicators of compromise (if available and lawful to share)

**Timeline tracking (attach to all regulatory notifications):**

```
Clock tracking record (for regulator reference and internal records):
- Incident timestamp (when breach occurred): [date/time/timezone]
- Awareness timestamp (when organization became aware): [date/time/timezone]
- Discovery timestamp (when breach confirmed): [date/time/timezone]
- Time between awareness and this notification: [hours and minutes]
- [If > 72h for GDPR/NIS2]: Reasons for delay: [explanation]
```

---

### Template 4: Affected Individual Notification

**Audience:** Data subjects whose personal data was compromised with high-risk consequence
**Legal review:** Required before sending any individual notification
**Language:** Plain language; avoid legal jargon; empathetic tone
**Channel:** Email (preferred); post/letter; website notice (if disproportionate effort)

```
Subject: Important notice about your personal information

Dear [Name / "Valued Customer"],

We are writing to inform you of a security incident that has affected your personal information.

WHAT HAPPENED
On approximately [date], we discovered [plain-language description of what occurred].
Our investigation determined that [categories of personal data] associated with your account
may have been accessed [or: was accessed] by an unauthorized party.

WHAT INFORMATION WAS INVOLVED
The following categories of your personal information were affected:
[List specific data categories: e.g., name, email address, account number. Be specific.]

WHAT WE ARE DOING
We have [containment actions taken: e.g., secured the affected system, reset passwords,
engaged external security specialists]. We are also [ongoing actions].

WHAT YOU CAN DO TO PROTECT YOURSELF
1. [Specific protective action, e.g., change your password immediately]
2. [Specific protective action, e.g., monitor your bank statements for unusual activity]
3. [Specific protective action, e.g., be alert to phishing emails referencing this incident]
[If applicable]: We are offering [credit monitoring / identity protection service] at no cost.
To enroll: [enrollment link or phone number] | Offer expires: [date]

YOUR RIGHTS
[JURISDICTION-SPECIFIC: include applicable rights — e.g., EU/UK GDPR rights to access,
erasure, complaint to supervisory authority; US state rights where applicable]
To exercise your rights or ask questions: [dedicated breach response contact]
[DPA contact if EU/UK]: You may also contact [supervisory authority name and contact]

CONTACT US
Dedicated breach response line: [phone/email] — available [hours/timezone]

We sincerely regret that this occurred and are committed to protecting your information.

[Organization name]
[Date]
```

---

### Template 5: Media / Public Statement

**Audience:** Press, public, social media
**Legal review:** Mandatory before release; treat as non-privileged public record
**Privilege note:** Coordinate with outside counsel; this statement is NOT privileged
**Timing:** Only after regulatory notification filed (where applicable)

```
[HOLDING STATEMENT — FOR IMMEDIATE RELEASE / EMBARGO: [DATE]]

[Organization] Responds to Security Incident

[CITY, DATE] — [Organization] is aware of a security incident that [brief factual description
of confirmed scope]. We take the protection of [customer/patient/employee] data extremely
seriously, and we are actively investigating this matter with the support of leading external
cybersecurity experts.

[If personal data involved]: We have notified [relevant regulatory authorities] in accordance
with our legal obligations and are contacting [affected individuals / customers] directly.

We have taken immediate steps to [containment actions already completed] and continue to
[ongoing actions]. We are cooperating fully with [law enforcement / regulatory authorities,
if applicable].

We are committed to keeping [affected individuals / customers] informed as our investigation
progresses. Further updates will be provided at [website URL / contact channel].

For media inquiries: [spokesperson name, title, contact]
For customer/individual inquiries: [dedicated breach response contact]

---
[Organization] is [one sentence about organization]. [Website]
```

**Pre-cleared Q&A document** must be prepared by communications + legal before any media
briefings. Do not ad-lib responses during a P1 incident.

---

### Template 6: Customer / Partner Notification

**Audience:** B2B customers, partners, vendors who may be affected or need to take action
**Timing:** After regulatory notification (to avoid prejudicing regulatory process)
**Legal review:** Required; check contractual breach notification SLAs
**Note:** Review customer DPAs and MSAs — contractual breach notification obligations
may set shorter timelines than regulatory law

```
[CONFIDENTIAL BUSINESS COMMUNICATION]

To: [Customer/Partner Name]
From: [Contact Name, Title, Organization]
Date: [Date]
Re: Security Incident Notification

Dear [Contact],

We are writing to notify you of a security incident affecting [Organization] that may
be relevant to our relationship.

SUMMARY OF INCIDENT
On [date], we discovered [plain-language description of the incident]. Our investigation
is [ongoing / substantially complete].

IMPACT ON YOUR ORGANIZATION / DATA
[ ] Your data WAS affected: [specific data types, approximate records, scope]
[ ] Your data MAY HAVE BEEN affected: [investigation is ongoing; we will update you]
[ ] Your data WAS NOT affected: [rationale/scope explanation]

ACTIONS WE HAVE TAKEN
[List completed containment/remediation steps with dates]

ACTIONS YOU SHOULD CONSIDER
[List any specific steps the customer should take, if applicable]

REGULATORY NOTIFICATIONS
We have filed notifications with [regulatory authorities] on [date(s)]. This notification
[DOES / DOES NOT] satisfy the notification requirement under [relevant contract section].
A separate formal notice under [contract clause] will / will not follow.

POINT OF CONTACT
For questions or additional information: [dedicated contact name, email, phone]
We commit to providing updates at the following intervals: [schedule]

[Signature block]
```

---

## Tabletop Exercise Framework

Tabletop exercises should be conducted at minimum annually (more frequently for P1 risk
organizations). Three scenarios are provided at increasing complexity levels.

### Exercise Design Principles

1. **Realism**: Use real employee names, actual software systems, real customer names (anonymized)
2. **Plot twists**: Add unexpected complications after initial scenario presentation
3. **Privilege decisions**: Include decisions that force the team to think about legal protection
4. **Time pressure**: Use actual clocks to simulate 72-hour regulatory windows
5. **Role-play**: Simulate media inquiries, regulator calls, law enforcement contact
6. **Blameless debrief**: Conclude with immediate gap identification, not finger-pointing

### Scenario A: Ransomware with Data Exfiltration (P1)

**Complexity:** High | **Duration:** 3-4 hours | **Participants:** Full IRT

**Scenario narrative:**
It is 11:47 PM on a Friday. Your Security Operations Center receives automated alerts
showing mass encryption activity across your core database servers. Initial investigation
reveals ransomware has encrypted your primary customer database, backup systems, and
active directory. The attacker has left a ransom note demanding $2.5 million in Bitcoin.
Your threat intelligence team quickly identifies this as [known ransomware group] — a group
known to exfiltrate data before encrypting it and to operate a leak site. Your organization
processes personal data of approximately 150,000 EU customers and 80,000 US customers across
12 states.

**Injects (release sequentially):**

1. **T+30 min:** The forensics team confirms attacker had access to your network for 21 days.
   Log analysis shows evidence of staged data exfiltration.
2. **T+1 hr:** Your CEO calls asking "should we just pay the ransom?" Legal must advise.
3. **T+2 hrs:** A journalist from [major outlet] emails your press team: "I've seen your
   customer data on a dark web leak site. Can you comment?"
4. **T+3 hrs:** The attacker emails your CFO directly: "You have 48 hours to pay or we
   publish all data."
5. **T+4 hrs:** An EU customer tweets that their data is on a paste site — it's going viral.
6. **T+5 hrs:** Law enforcement calls asking you to delay public disclosure for 72 hours
   to avoid compromising their investigation.

**Discussion questions:**

1. Who makes the ransom payment decision? What process does your IRP specify?
2. When does your GDPR 72-hour clock start? When did "awareness" occur?
3. How do you handle the journalist inquiry while the regulatory clock is running?
4. Does law enforcement's request to delay disclosure conflict with GDPR Art. 33?
5. Has privilege been preserved? Who retained the forensics firm and when?
6. Do you have a holding statement ready? Can it go out before you notify the ICO?

**Evaluation rubric:**

- Was severity correctly classified as P1 within 30 minutes? (Y/N + rationale)
- Was outside counsel engaged before forensics firm briefed? (Y/N + timing)
- Was legal hold issued before any eradication actions? (Y/N + timing)
- Was GDPR 72h clock identified and tracked correctly? (Y/N + error if any)
- Was the media inquiry handled correctly (no unauthorized disclosure)? (Y/N)

**Gaps to identify:**

- IRP did not address ransom payment decision authority
- No pre-vetted forensics firm (no retainer)
- GDPR clock start date was disputed internally (who has the authority to declare "awareness"?)
- No out-of-band communication channel — incident response was coordinated via the compromised email system

---

### Scenario B: Third-Party Vendor Breach (P2)

**Complexity:** Medium | **Duration:** 2 hours | **Participants:** Legal, DPO, CISO, Communications

**Scenario narrative:**
You receive an email at 9:15 AM on a Tuesday from a key SaaS vendor informing you that
they have experienced a security incident. The vendor states that an unauthorized party
accessed systems containing "customer data" but provides no further details. Your
organization uses this vendor to process customer profile data for approximately 35,000
EU customers and 25,000 US customers. You have a data processing agreement (DPA) with
the vendor. The vendor says they will "provide more information within 5 business days."

**Injects:**

1. **T+1 hr:** The vendor's DPA you hold requires them to notify you "without undue delay"
   but you cannot reach anyone above the account manager.
2. **T+2 hrs:** You discover your own DPA requires you to notify [your clients] within
   24 hours of a breach involving their data. You have 12 hours remaining.
3. **T+3 hrs:** The vendor updates you: they confirm customer PII was accessed, but
   cannot quantify the scope yet.
4. **T+4 hrs:** A DPA inquiry arrives from the French CNIL asking for information about
   the vendor's incident.

**Discussion questions:**

1. Are you the controller or the processor here? How does that change your obligations?
2. Can you file a GDPR Art. 33 notification with incomplete information? Should you?
3. How do you enforce the vendor's DPA notification obligations?
4. Do you need to notify your own clients? By when?

---

### Scenario C: Insider Threat with Regulatory Disclosure (P1)

**Complexity:** High | **Duration:** 3-4 hours | **Participants:** Full IRT plus HR

**Scenario narrative:**
Your HR system access logs show that a senior data analyst submitted their resignation
last Monday. IT access review reveals the employee downloaded 800,000 customer records
to a personal cloud storage account and transferred 35 GB of proprietary algorithm files
to an unknown location in the 72 hours before submitting their resignation. The employee
has now departed the organization. The customer records contain names, contact information,
purchase history, and — for approximately 12,000 customers — payment card information.

**Injects:**

1. **T+30 min:** Legal confirms the employee signed an NDA and data handling policy.
   They want to initiate civil proceedings immediately. Should this be coordinated with the IR?
2. **T+1 hr:** Law enforcement calls proactively — they have intelligence this employee
   was recruited by a competitor. They want your forensic evidence.
3. **T+2 hrs:** HR wants to announce the employee's departure internally. Legal must advise.
4. **T+3 hrs:** The employee's personal lawyer calls threatening defamation claims if
   the organization discloses the incident publicly.
5. **T+4 hrs:** Your PCI DSS QSA calls — they saw an alert and want to know if this is
   a reportable event under PCI DSS.

**Discussion questions:**

1. Does litigation against the employee affect privilege for the IR investigation?
2. How does law enforcement coordination affect your regulatory notification timing?
3. Can HR announce the employee's departure? Is there messaging coordination risk?
4. Does PCI DSS create a separate notification obligation? Who handles it?
5. How do you contain reputational risk from the employee's legal threat while being
   transparent with regulators?

---

### Post-Exercise Gap Documentation Template

```
TABLETOP EXERCISE GAP LOG
Exercise: [Scenario name] | Date: | Participants:

IRP GAPS IDENTIFIED
# | Gap Description | Phase Affected | Severity (Critical/Major/Minor) | Owner | Remediation Action | Deadline
--|-----------------|----------------|--------------------------------|-------|-------------------|----------
1 | | | | | |
2 | | | | | |

DECISIONS NOT COVERED BY CURRENT IRP
- [Decision area the team could not resolve because the IRP was silent]

COMMUNICATION FAILURES OBSERVED
- [Gap in communication protocol, channel, or template]

RACI AMBIGUITIES
- [Activity where it was unclear who was responsible or accountable]

REGULATORY CLOCK ERRORS
- [Misidentification of clock start, timeline, or notification scope]

PRIVILEGE RISKS IDENTIFIED
- [Decisions made that could have compromised privilege]

IRP UPDATE ACTIONS
# | Section to Update | Proposed Change | Owner | Deadline
--|------------------|----------------|-------|----------
1 | | | |

NEXT EXERCISE DATE: [date] | NEXT SCENARIO: [A/B/C / custom]
```

---

## Post-Incident Review Framework

**Purpose:** Systematic learning and IRP improvement without blame assignment.

**Timing:** P1 within 2 weeks of recovery; P2 within 4 weeks; P3 within 8 weeks.

**Blameless PIR structure:**

```
POST-INCIDENT REVIEW REPORT
Incident ID: | Severity: | Date of discovery: | Date of recovery:
Prepared by: | Review date: | Participants:

CULTURE STATEMENT
This review is conducted in a blameless format. The goal is systemic improvement,
not individual accountability. All participants are encouraged to share complete
and honest information. Findings will not be used in performance evaluations.

1. INCIDENT TIMELINE
[Detailed chronological timeline with key decision points and communication events]

2. WHAT WENT WELL
[Specific practices that functioned as intended — name them for reinforcement]

3. WHAT DIDN'T WORK
[Specific failures: tools, processes, communications, decision authority gaps]

4. ROOT CAUSE ANALYSIS
[Contributing factors — technical, process, governance, resource]

5. REGULATORY COMPLIANCE ASSESSMENT
- Were all notification deadlines met? (Y/N) If no, explain.
- Were notifications accurate and complete? (Y/N) If no, explain.
- Were evidence preservation obligations met? (Y/N) If no, explain.
- Are any regulatory follow-up obligations outstanding? (Y/N) If yes, list.

6. LITIGATION / INSURANCE ASSESSMENT
- Is civil litigation risk elevated post-incident? (Y/N) Outside counsel assessment:
- Was cyber insurance claim filed? (Y/N) Status:
- Are evidence preservation obligations for anticipated litigation current? (Y/N)

7. IRP UPDATE REQUIREMENTS
# | IRP Section | Required Change | Priority | Owner | Deadline
--|-------------|----------------|---------|-------|----------
1 | | | HIGH/MED/LOW | |

8. SYSTEMIC IMPROVEMENTS
[Broader organizational, technology, or governance changes recommended]

9. NEXT TABLETOP EXERCISE
Target date: | Scenario: | Participants:
```

---

## Prioritization Framework

When building an IRP or responding to an incident, prioritize activities in this order:

### Tier 1 — Life Safety and Critical Infrastructure (Immediate)

- Any incident affecting systems with life-safety implications (medical devices, critical
  infrastructure, OT/ICS environments) takes absolute priority over all other considerations
- Containment of systems posing direct physical risk precedes all documentation and legal processes
- Alert relevant emergency services or government authorities if life risk is present [JURISDICTION-SPECIFIC]

### Tier 2 — Regulatory Compliance (Within Statutory Deadlines)

- Regulatory notification timelines are non-negotiable once triggered
- Privilege architecture must be activated before investigation proceeds (cannot be remediated retroactively)
- Legal hold must be issued before any remediation that could destroy evidence

### Tier 3 — Business Continuity (Within SLAs)

- Containment and eradication to minimize business disruption
- Customer/partner communication to maintain trust and meet contractual obligations
- Insurance claim notification (check policy notification deadlines)

### Tier 4 — Systemic Improvement (Post-Incident)

- Post-incident review and IRP updates
- Training and awareness program enhancements
- Technology and process improvements identified in the PIR

**IRP Build Priority (Plan-Building mode):**

1. Severity classification framework + RACI (without these, all live response is improvised)
2. Regulatory notification decision tree (governs the highest-stakes time-bound decisions)
3. Communication templates (needed immediately in any incident; cannot draft under pressure)
4. Legal privilege architecture (must be in place before first incident to be effective)
5. Evidence preservation protocol (must be trained before first incident)
6. Tabletop exercises (testing the plan; cannot be effective without the plan first)
7. Maintenance schedule and versioning governance

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any IRP output. Revise any failures before delivery.

| Gate           | Rule                                                                                                     | Fail Action                                                                 |
| -------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Source**     | Every regulatory timeline and threshold cites a specific article, statute, or regulation                 | Add citation or mark "[UNVERIFIED — verify with current official guidance]" |
| **Format**     | Citations follow a consistent format for the jurisdiction (e.g., "Art. 33 GDPR" not "GDPR article")      | Fix format                                                                  |
| **Currency**   | All cited provisions and timelines are marked [VERIFY] pending confirmation they reflect current law     | Flag "[CHECK CURRENCY — regulatory guidance evolves]"                       |
| **Domain**     | No jurisdiction-specific rules stated as universal; all [JURISDICTION-SPECIFIC] markers correctly placed | Remove or mark jurisdictional bleed                                         |
| **Confidence** | Uncertainty is stated explicitly, not hidden; privilege case law is marked [VERIFY]                      | Add confidence qualifier                                                    |

### Self-Interrogation for P1 Severity Determinations

For any P1 classification in a live incident, apply this 3-pass review before delivering:

**Pass 1 — Classification Integrity:**

- Does the P1 determination follow logically from the criteria in the Severity Classification Reference?
- Is there a credible argument that this is P2 rather than P1? If so, state it.
- Would a reasonable CISO with the same facts reach the same conclusion?

**Pass 2 — Completeness:**

- Have all applicable regulatory regimes been identified?
- Have all notification clocks been assessed?
- Have all affected data types and subject categories been considered?
- Has the privilege assessment been run?

**Pass 3 — Challenge:**

- What would change the classification to P2?
- Are there facts not yet known that could materially change the severity assessment?
- Is the organization being appropriately conservative (over-responding is safer than under-responding for regulatory purposes)?

### Confidence Scoring

Assign confidence scores to all regulatory notification conclusions and legal assessments:

| Level        | Range     | Meaning                                                          | Action                                                     |
| ------------ | --------- | ---------------------------------------------------------------- | ---------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law; explicit statutory provision; no reasonable doubt   | State with confidence                                      |
| **High**     | 0.80-0.94 | Strong authority; minor interpretation questions; consensus view | State with brief caveat                                    |
| **Probable** | 0.60-0.79 | Good arguments; jurisdiction-specific uncertainty                | State with reasoning and markers                           |
| **Possible** | 0.40-0.59 | Genuine uncertainty; competing views                             | Flag for legal counsel review                              |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                                          | Mark "[UNCERTAIN — legal counsel required]"; do not assert |

---

## Glass Box Audit Trail

Every IRP engagement output must include this audit trail, adapted for the mode (live
incident vs. plan-building):

```yaml
glass_box:
  skill_name: "legalcode-incident-response-plan-builder"
  mode: "Live Incident Response / Plan-Building — [select]"
  incident_id: "[INC-YYYYMMDD-### or 'N/A (plan-building)']"
  severity_classification: "[P1/P2/P3/P4 — confirmed/preliminary]"
  classification_rationale: "[Key criteria that determined the classification]"
  organization_type: "[sector]"
  regulatory_regimes_assessed:
    - "[Regime 1 — applicable / not applicable / VERIFY]"
    - "[Regime 2 — applicable / not applicable / VERIFY]"
  notification_clocks:
    gdpr_art33: "[Running since: XX:XX UTC / Not triggered / VERIFY]"
    nis2_early_warning: "[Running since: XX:XX UTC / Not triggered / VERIFY]"
    nis2_formal: "[Running since: XX:XX UTC / Not triggered / VERIFY]"
    other: "[Regime, clock status]"
  privilege_track_status: "[Active — outside counsel directing / Not activated / Compromised — assess]"
  legal_hold_status: "[Issued — [date/time] / Not yet issued / N/A]"
  forensics_firm: "[Retained through counsel / Retained directly — PRIVILEGE RISK / Not engaged]"
  legalcode_mcp: "[Connected — authority verified / Not connected — manual verification required]"
  research_reference_file: "[/tmp/legalcode-irp-research.md / Not created]"
  related_skills_invoked:
    breach_severity_assessment: "[Invoked / Not yet / N/A]"
    breach_regulatory_notification_drafter: "[Invoked / Not yet / N/A]"
    us_breach_notification_triage: "[Invoked / Not yet / N/A]"
    dsar_workflow_builder: "[Invoked / Not yet / N/A]"
  citations_verified: "[N VERIFIED] / [N marked VERIFY]"
  self_interrogation: "[PASS / REVISED / N/A — no P1 classification]"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  limitations:
    - "[Scope limitation, assumption, or caveat]"
    - "[Sector-specific overlay not covered: refer to specialist counsel]"
  reviewer: "AI-assisted — requires qualified legal and cybersecurity review before any regulatory filing or production use"
```

---

## Anti-Patterns

What NOT to do in incident response planning and execution. Every item below represents
a documented failure mode with real regulatory, litigation, and operational consequences.

### Legal and Privilege Anti-Patterns

1. **Retaining the forensics firm directly, before engaging outside counsel** — The forensic
   report becomes a business document, not attorney work product. Privilege is compromised
   before the investigation begins. This is the single most common — and most costly —
   privilege error in cybersecurity incident response.

2. **Distributing the forensic report broadly within the organization** — Wide distribution
   defeats work-product protection even if the engagement was initially privileged. Every
   recipient beyond the minimum necessary increases the risk that a court will find privilege
   was waived.

3. **Using in-house counsel alone to direct the forensic investigation** — In-house counsel
   communications may receive narrower privilege protection than outside counsel. Engage
   outside breach counsel for any investigation where litigation or enforcement is anticipated.

4. **Filing regulatory notifications before legal review** — Regulatory notifications
   are non-privileged public records. Errors in initial filings (scope, timeline, content)
   cannot be retracted and become the evidentiary baseline for enforcement actions.

5. **Conflating the NIS2 and GDPR notification clocks** — NIS2 Art. 23 requires a 24-hour
   early warning to the CSIRT — a separate obligation that fires before the GDPR 72-hour
   clock to the DPA. Missing the 24-hour NIS2 obligation while focused on GDPR is a
   common dual-regime failure.

6. **Failing to identify the one-stop-shop lead DPA** for multi-EU incidents — Notifying
   all EU DPAs simultaneously when a lead DPA one-stop-shop mechanism applies wastes time,
   creates inconsistent regulatory submissions, and signals poor legal sophistication.

7. **Missing the NIS2 1-month final report obligation** — Many organizations file the
   initial NIS2 notification and then consider the obligation discharged. The 1-month
   final report is a separate mandatory deliverable that closes the regulatory loop.

### Operational Anti-Patterns

8. **No pre-designated incident commander** — When an incident occurs, role ambiguity
   causes the first critical hours to be consumed by organizational politics rather than
   containment decisions. Every IRP must name a specific Incident Commander and succession.

9. **Containment before forensic imaging** — Rebuilding, wiping, or patching systems
   before forensic images are taken destroys evidence needed for criminal prosecution,
   civil litigation, insurance claims, and regulatory defense. Always image before remediation.

10. **Using production communication channels during active compromise** — Coordinating
    incident response via potentially compromised email or Slack alerts the attacker and
    allows adversarial monitoring. Out-of-band communication channels (Signal, dedicated
    bridge line, out-of-band video call) must be pre-established and pre-tested.

11. **Treating the IRP as a document rather than a muscle** — A plan written once and
    never tested through tabletop exercises fails at the worst possible moment. An untested
    IRP is effectively no IRP. Test annually at minimum; test after every significant change.

12. **Sequential workflow during parallel regulatory clocks** — Organizations work through
    incident phases one at a time (contain → investigate → decide → notify) when regulatory
    deadlines demand these run in parallel. Notification clocks do not pause while
    forensic investigation continues.

13. **No pre-vetted vendor roster** — Discovering you need a forensics firm, crisis PR
    agency, or breach response call center during an active P1 incident means wasting
    critical hours on procurement, NDA execution, and onboarding. Pre-signed retainer
    agreements for all three are essential preparation.

14. **Assuming backups are clean** — Ransomware operators routinely target backup
    systems before deploying encryption. Test backup integrity as a standard P1 response
    action. Restoration from a compromised backup extends the attacker's access.

### Communication Anti-Patterns

15. **Issuing any public statement before regulatory notification** — In GDPR/NIS2
    jurisdictions, regulators who learn of incidents from press coverage reliably apply
    more aggressive enforcement scrutiny than regulators who receive timely, substantive
    notifications from the organization.

16. **Minimizing language in external communications** — "Potential unauthorized access,"
    "may have been affected," "limited personal information" — language that understates
    the confirmed scope creates credibility and enforcement exposure when the true scope
    becomes public.

17. **No dedicated breach response communication channel** — Routing affected individuals
    to a general customer service email creates inconsistent messaging, fails to capture
    the complaint record required for regulator reporting, and overwhelms support teams.

18. **Missing contractual notification deadlines to customers** — Many DPAs and MSAs
    require breach notification within 24-48 hours. Missing these contractual deadlines
    creates breach-of-contract exposure independent of and in addition to regulatory penalties.

### Structural and Governance Anti-Patterns

19. **No formal severity classification system** — Without a defined classification scheme,
    every incident is either downplayed (to avoid escalation) or escalated maximally (out
    of risk aversion). Both failure modes waste resources and undermine organizational trust
    in the IR process.

20. **Post-incident reviews that assign blame** — When PIRs become blame sessions,
    participants provide incomplete or self-protective information, honest root causes
    are never identified, and the organization fails to learn. Structure PIRs explicitly
    as blameless. Separate any individual accountability processes from the PIR entirely.

21. **Failing to notify cyber insurers promptly** — Many cyber insurance policies have
    notice provisions triggered by the incident itself, not only at claim time. Late
    notification can void coverage at the worst possible moment. Check and calendar the
    insurance notification deadline as standard Step 1 for any P1/P2 incident.

22. **IRP that omits the processor/controller distinction** — When a breach occurs at a
    third-party processor, it is a common failure to treat the response as solely the
    processor's responsibility. The controller retains primary regulatory notification
    obligations under GDPR Art. 33. The IRP must explicitly address how the organization
    responds when it is the controller and the breach is at a processor.

---

## Writing Standards

Apply these standards to all IRP outputs and communications:

1. **Factual discipline**: State only what is confirmed. Separate confirmed facts from
   suspected facts from unknown facts in every communication.

2. **Precision over hedging**: "72 hours from awareness" is correct. "We have a day or
   two to notify" is dangerous. Use the precise statutory language.

3. **Plain language for individual notifications**: Individual data subject notifications
   must be readable by a non-specialist. Test with a plain-language readability tool.
   Maximum 8th-grade reading level for consumer audiences.

4. **No speculation in regulatory filings**: State what is known, note what is under
   investigation, and indicate when supplementary information will follow. Do not speculate
   about cause, attribution, or scope beyond confirmed facts.

5. **Consistent terminology**: Use the same term throughout all communications (e.g.,
   "unauthorized access" vs. "breach" — legal has specific meanings; align with legal's
   preferred formulation before going external).

6. **Timestamp and version all documents**: Every IRP document, communication draft,
   and evidence log must carry a timestamp and version number. Incident response
   documentation is subject to regulatory and litigation scrutiny.

7. **Legal review gate before external release**: No communication leaves the organization
   during an active incident without legal review. This includes social media responses,
   customer support scripts, and executive quotes.

8. **[VERIFY] before relying**: Every specific statutory timeline, penalty figure, and
   threshold in this skill should be verified against current official sources before
   use in any actual incident response or regulatory filing.

---

## External Tool Integration

### legalcode-mcp

Use legalcode-mcp (when connected) to verify:

- Current notification timelines for applicable regimes
- Recent enforcement decisions and supervisory authority guidance
- Sector-specific regulatory requirements for applicable jurisdiction
- Current transposition status of NIS2 in relevant EU member states

Save research results to `/tmp/legalcode-irp-research.md` and cite in the Glass Box.

**If legalcode-mcp is not connected:**

- Proceed with the guidance in this skill
- Mark all specific timelines and thresholds with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Strongly recommend external verification with current regulatory guidance before
  any regulatory filing

### Integration with Legalcode Breach Skill Stack

| Skill                                              | When to Invoke                                                  | Output Consumed                                |
| -------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------- |
| `legalcode-breach-severity-assessment`             | At personal data scope assessment gate (Step 6)                 | Harm assessment, notifiability determination   |
| `legalcode-breach-regulatory-notification-drafter` | When notification decision is made                              | Submission-ready notification documents        |
| `legalcode-us-breach-notification-triage`          | When US residents are confirmed affected                        | Per-state obligation matrix, deadline calendar |
| `legalcode-dsar-workflow-builder`                  | Post-breach, when data subjects submit access/deletion requests | DSAR response workflow                         |

---

## Output Format Template

Each IRP engagement produces a package with the following named outputs:

```markdown
# Incident Response Plan — [Organization Name]

## Version [X.X] | [Date] | [Mode: Plan-Build / Live Incident]

### Classification: [CONFIDENTIAL / ATTORNEY-CLIENT PRIVILEGED]

---

## Executive Summary

[1 page: scope, regulatory exposure, key decisions, status]

## Section 1: IRP Policy and Governance

[Mandate statement; IRT composition; RACI; review schedule]

## Section 2: Severity Classification Framework

[P1-P4 criteria, SLAs, escalation chains]

## Section 3: Incident Response Lifecycle

[Phase 1-6 operational guidance with owners and decision gates]

## Section 4: Regulatory Notification Decision Tree

[Traversable flowchart with jurisdiction-specific timelines]

## Section 5: Legal Privilege Architecture

[Dual-track model; privilege checklist; Kovel doctrine application]

## Section 6: Evidence Preservation Protocol

[Legal hold trigger; chain of custody; forensic integrity; log preservation]

## Section 7: Communication Templates

[Templates 1-6 with fill-in structures]

## Section 8: Tabletop Exercise Program

[Scenario A, B, C with inject cards and evaluation rubrics]

## Section 9: Post-Incident Review Template

[Blameless PIR structure with gap documentation]

## Appendix A: Regulatory Contact Directory

[Per-jurisdiction regulator contact information — [VERIFY current details]]

## Appendix B: Pre-Vetted Vendor Roster

[External counsel, forensics firm, PR firm — with retainer confirmation]

## Appendix C: Cyber Insurance Policy Reference

[Policy number, coverage, notification deadlines, claim contact]

## Glass Box Audit Trail

[YAML audit trail per schema above]
```

---

## Localization Notes

When localizing this skill for a specific jurisdiction:

1. **Replace [JURISDICTION-SPECIFIC] markers** with the specific statutory citation and
   requirement for the target jurisdiction
2. **Verify NIS2 implementing legislation** — the national law (not the Directive text)
   governs for EU member states; transposition varies significantly
3. **Add sector-specific overlays** — HIPAA for US healthcare, DORA for EU financial
   entities, FCA incident reporting for UK regulated financial services — as dedicated
   annexes reviewed by specialist counsel
4. **Adjust privilege analysis** — Attorney-client privilege and work product doctrine
   vary significantly between common law and civil law jurisdictions; the dual-track
   model is grounded in US/UK case law and may need adaptation elsewhere
5. **Localize communication templates** — Language requirements, individual notification
   rights disclosures, and regulator-specific mandatory content elements vary by jurisdiction
6. **Check national NIS2 transposition** for accurate Art. 23 implementing requirements
   and competent authority designation in each relevant EU member state [VERIFY]

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis produced by a 2-agent research
pipeline: Agent 1 (Structural Analyst — NIST SP 800-61r3 April 2025 CSF 2.0 restructure,
SANS 6-phase IH&R, ISO/IEC 27035-1/2/3 2023, ISO/IEC 27037, NIS2 Art. 23 24-72-1month
three-tier reporting, GDPR Art. 33-34 awareness clock and phased notification, HIPAA BNR,
SEC Form 8-K materiality, Australian NDB, PIPEDA SOR/2018-64, attorney-client privilege
dual-track model with Kovel doctrine, evidence preservation chain of custody, CISA tabletop
exercise framework, P1-P4 severity classification with SLAs, 18-item anti-pattern list)

- Agent 2 (Prompt Engineering & Quality Analyst — severity classification design with
  numeric thresholds, full 27-activity RACI matrix, 8-gate regulatory notification decision
  tree, 6 communication templates with fill-in structures, 20-item anti-pattern list,
  dual-mode operation design, privilege architecture as structural constraint, integration
  map with legalcode breach skill stack, quality dimension scoring 40/40 target, Glass Box
  schema design). Aligned with legalcode-contract-review gold-standard quality frameworks
  (Citation Quality Gates, 3-pass Self-Interrogation, 5-level Confidence Scoring, Glass Box
  audit trail). Integrates into legalcode breach skill family alongside
  legalcode-breach-severity-assessment, legalcode-breach-regulatory-notification-drafter,
  legalcode-us-breach-notification-triage, and legalcode-dsar-workflow-builder.
