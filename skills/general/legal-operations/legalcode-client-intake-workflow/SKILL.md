---
name: legalcode-client-intake-workflow
description: Guide law firms through a structured client intake process from initial contact through engagement.
  Use when onboarding a new client, conducting conflict of interest checks, performing KYC/AML due diligence,
  preparing engagement letters, or setting up a new matter. Covers conflict screening, client qualification,
  risk assessment, fee structures, engagement letter drafting, and matter file setup. Jurisdiction-agnostic
  with localization markers for ABA Model Rules (US), SRA requirements (UK), and other bar regulations.
  Integrates with legalcode-conflict-check and legalcode-matter-triage-workflow for comprehensive intake
  workflows.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Client Intake Workflow

> **Disclaimer**: This skill provides a framework for AI-assisted legal client intake
> workflows. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use. Professional
> responsibility rules, AML regulations, and bar requirements change; verify current
> applicability before relying on any provision described here. Statutory and regulatory
> references cited from memory carry hallucination risk — verify against authoritative
> sources before relying on them.

## Purpose and Scope

This skill guides law firms through a systematic client intake process from initial contact
to matter setup. It ensures ethical compliance, proper documentation, and consistent
client onboarding while identifying risks early in the relationship.

**Covers:**

- Initial client contact and information gathering
- Conflict of interest screening (pre-consultation and comprehensive)
- Client qualification and matter assessment
- KYC/AML due diligence (identity verification, source of funds)
- Risk profiling and tiering (standard, enhanced, high-risk)
- Fee structure selection and communication
- Engagement letter drafting with required disclosures
- Matter file setup and team assignment
- Welcome packet and communication protocol establishment

**Does not:**

- Replace licensed professional judgment on conflict waivers
- Provide legal advice to prospective clients
- Make final accept/decline decisions on matter representation
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

**Related skills:**

- `legalcode-conflict-check` — deep-dive conflict screening
- `legalcode-matter-triage-workflow` — matter prioritization and routing
- `legalcode-engagement-letter` — detailed engagement letter drafting (if available)

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. The firm's home jurisdiction and applicable bar rules
determine which specific requirements apply. The workflow identifies the relevant
regulatory framework early and adapts accordingly.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- **Professional responsibility rules**: ABA Model Rules (US), SRA Code of Conduct (UK),
  local bar rules, notarial requirements
- **Conflict of interest rules**: Rule 1.7 (concurrent), Rule 1.9 (former clients),
  Rule 1.18 (prospective clients), imputation rules
- **Fee disclosure requirements**: Written fee agreements, contingency fee rules,
  retainer accounting, trust account requirements
- **AML/KYC obligations**: BSA/PATRIOT Act (US), MLR 2017 (UK), FATF recommendations,
  beneficial ownership requirements
- **Engagement letter mandates**: State-specific requirements (e.g., NY Part 1215),
  hourly minimums for written agreements, scope of representation requirements
- **Data protection**: GDPR, CCPA, state privacy laws for client information handling
- **Insurance requirements**: Professional liability minimums, disclosure obligations

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the firm's policies or the prospective client's situation, the workflow pauses and asks
when:

- The answer would change the intake path (accept, decline, enhanced due diligence)
- Multiple valid approaches exist and firm policy matters
- Risk assessment requires additional context
- Conflict screening reveals potential issues requiring human judgment

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

### Step 1: Accept Initial Contact

Accept prospective client information in any of these formats:

- **Contact form submission**: Name, contact info, matter summary, referral source
- **Phone/email inquiry**: Transcribed or summarized initial contact
- **Referral package**: Information from referring attorney or client
- **Walk-in intake**: Information gathered at reception
- **Online scheduling**: Automated intake form data

**Minimum information required before proceeding:**

- Full legal name (individual or entity name)
- Contact information (phone, email, address)
- Brief description of legal matter or service needed
- Names of all known adverse parties
- Referral source (if applicable)

If information is incomplete, prompt for the missing elements before advancing to
conflict screening.

### Step 2: Preliminary Conflict Screen

Before any substantive conversation with the prospective client, conduct an initial
conflict check to avoid receiving disqualifying confidential information.

**CLARIFY** — Before running the conflict screen, confirm:

1. **Firm conflict database access**: Do you have access to the firm's conflict
   checking system?
   - Options: Yes (provide system name or describe), No (manual check), Not applicable
     (solo practitioner with personal knowledge)
   - _Why this matters_: Determines whether to run automated or manual conflict checks.

2. **Related parties identified**: Have all known parties been identified?
   - Prospective client name and aliases
   - Spouse/partner (for family law matters)
   - Corporate affiliates (for entity clients)
   - All known adverse parties
   - _Why this matters_: Incomplete party lists create conflict risks.

**Preliminary conflict check process:**

1. Search the firm's conflict database for:
   - Exact name matches (prospective client and adverse parties)
   - Phonetic variants and common misspellings
   - Corporate family relationships
   - Previous matter connections

2. **Classification:**
   - **CLEAR**: No matches found — proceed to Step 3
   - **POTENTIAL CONFLICT**: Matches found — flag for attorney review before proceeding
   - **DEFINITE CONFLICT**: Current adverse representation — do not proceed; decline
     without disclosure of conflict details

3. Document the conflict check:
   - Date and time of check
   - Names and parties searched
   - Database(s) searched
   - Results and classification
   - Reviewer (if escalated)

[JURISDICTION-SPECIFIC] **ABA Model Rule 1.18** (Prospective Clients):

- Even without engagement, duties to prospective clients include confidentiality
- If significantly harmful information is received, the lawyer may be disqualified
- Limit information gathered before conflict check clears to minimize disqualification risk
- Non-engagement does not eliminate duties already owed [VERIFY]

**CLARIFY** — If potential conflict is identified:

"The conflict check returned the following potential matches: [list matches]. Before
proceeding, an attorney must review and determine whether:

- This is a false positive (different person/entity)
- A conflict exists but may be waivable with informed consent
- A conflict exists that cannot be waived
- Screening procedures can avoid imputation to the firm

Would you like to proceed with attorney review, or decline the matter at this stage?"

### Step 3: Initial Consultation and Qualification

Conduct or document the initial consultation to qualify the prospective client and
assess the matter.

**CLARIFY** — Before the consultation, confirm the consultation model:

1. **Consultation format**:
   - Options: In-person meeting, Video conference, Phone call, Email exchange,
     Intake questionnaire only
   - _Why this matters_: Affects identity verification and information depth.

2. **Fee for consultation**:
   - Options: Free initial consultation, Paid consultation (rate: \_\_\_), Contingent on
     engagement, Varies by matter type
   - _Why this matters_: Must be disclosed before the consultation.

**Qualification criteria to assess:**

| Category               | Assessment Questions                                                                                                | Red Flags                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Matter Fit**         | Does this matter align with the firm's practice areas? Is the matter within the firm's geographic scope?            | Outside expertise, unfamiliar jurisdiction                             |
| **Case Merit**         | Does the prospective client have a viable legal position? Are there obvious defenses or limitations?                | Statute of limitations expired, frivolous claims                       |
| **Client Reliability** | Does the client seem cooperative and truthful? Can they meet their obligations (document production, availability)? | Inconsistent story, unrealistic expectations, prior attorney conflicts |
| **Economic Viability** | Can the client afford the representation? Is the matter worth the resources required?                               | Cannot afford fees, de minimis recovery potential                      |
| **Risk Assessment**    | Are there reputational or ethical risks?                                                                            | Adverse publicity, potential conflicts, difficult opposing party       |

**CLARIFY** — After qualification assessment:

"Based on the initial consultation, the matter assessment is:

- **Matter Type**: [type]
- **Estimated Complexity**: [Low / Medium / High / Complex]
- **Economic Viability**: [Viable / Marginal / Non-viable]
- **Risk Level**: [Standard / Elevated / High]
- **Red Flags Identified**: [list or 'None']

**Recommendation**: [Accept / Accept with conditions / Decline / Refer out]

Do you want to proceed with this recommendation, or adjust based on additional factors?"

### Step 4: KYC/AML Due Diligence

Conduct Know Your Customer (KYC) and Anti-Money Laundering (AML) due diligence
appropriate to the matter type and client risk profile.

**CLARIFY** — Determine the applicable AML regime:

1. **Firm jurisdiction and regulatory oversight**:
   - Options: US (state bar + voluntary BSA compliance), UK (SRA + MLR 2017),
     EU (local AML directive implementation), Other (specify)
   - _Why this matters_: Determines mandatory vs. recommended due diligence steps.

2. **Matter type — high-risk activities**:
   - Does this matter involve: Real property transactions, Trust or company formation,
     Financial transactions, Client fund handling, Asset structuring?
   - _Why this matters_: Certain activities trigger enhanced due diligence requirements.

3. **Client risk profile**:
   - Options: Standard (individual, domestic, routine matter), Elevated (entity client,
     complex structure, or moderate risk factors), High (PEP, high-risk jurisdiction,
     unusual circumstances, large transaction value)
   - _Why this matters_: Determines due diligence depth.

**KYC/AML checklist:**

#### Individual Clients

| Item                      | Standard Due Diligence                        | Enhanced Due Diligence                                    |
| ------------------------- | --------------------------------------------- | --------------------------------------------------------- |
| **Identity Verification** | Government-issued photo ID                    | Multiple forms of ID, in-person or certified verification |
| **Address Verification**  | Utility bill, bank statement (within 90 days) | Multiple address verifications, residency confirmation    |
| **Source of Funds**       | General inquiry for fees                      | Documented source with supporting evidence                |
| **Source of Wealth**      | Not required unless elevated                  | Full wealth source documentation                          |
| **PEP Screening**         | Database check                                | Enhanced screening, ongoing monitoring                    |
| **Sanctions Check**       | OFAC/consolidated list                        | Multiple sanctions lists, adverse media                   |
| **Ongoing Monitoring**    | Not required                                  | Periodic re-verification, transaction monitoring          |

#### Entity Clients

| Item                           | Standard Due Diligence                     | Enhanced Due Diligence                                      |
| ------------------------------ | ------------------------------------------ | ----------------------------------------------------------- |
| **Entity Verification**        | Certificate of incorporation, registration | Full corporate documents, good standing                     |
| **Ownership Structure**        | Identify 25%+ beneficial owners            | Full ownership chain to natural persons                     |
| **Authorized Representatives** | Board resolution or authorization          | Certified authorization, ID verification of all signatories |
| **Source of Funds**            | General inquiry                            | Audited financials, bank references                         |
| **PEP/Sanctions Screening**    | Entity + beneficial owners                 | Extended related parties                                    |
| **Jurisdiction Risk**          | Home jurisdiction check                    | All operating jurisdictions                                 |

[JURISDICTION-SPECIFIC] **UK MLR 2017 Requirements** [VERIFY]:

- Mandatory CDD for all regulated legal services
- Risk-based approach with documented risk assessments
- EDD for PEPs, high-risk third countries, complex/unusual transactions
- SARs to National Crime Agency (NCA) for suspicious activity
- No tipping off — do not disclose SAR filing to client
- Training requirements for all staff
- Annual compliance reviews for larger firms

[JURISDICTION-SPECIFIC] **US BSA/PATRIOT Act** [VERIFY]:

- Applies primarily to transactions involving financial institutions
- Voluntary compliance recommended for law firms
- SAR filing to FinCEN if suspicious activity detected
- OFAC screening for sanctions compliance
- Currency transaction reporting thresholds
- Client identity verification (CIP-style procedures)

**Document the KYC/AML review:**

- Risk classification (Standard / Elevated / High)
- Due diligence steps completed
- Documents collected and verified
- Screening results (PEP, sanctions, adverse media)
- Any unusual circumstances noted
- Reviewer sign-off

### Step 5: Fee Structure and Economics

Determine and communicate the fee structure for the engagement.

**CLARIFY** — Confirm fee arrangement:

1. **Fee structure type**:
   - Options: Hourly (standard rates), Hourly (blended rate), Flat fee (matter-based),
     Contingency, Hybrid (hourly + success fee), Retainer (ongoing relationship),
     Subscription (fixed periodic fee)
   - _Why this matters_: Drives engagement letter terms and client expectations.

2. **Retainer requirement**:
   - Options: No retainer required, Evergreen retainer (replenished), Fixed retainer
     (applied to fees), Trust account deposit (for expenses)
   - _Why this matters_: Must be clearly documented and trust-accounted.

3. **Expense handling**:
   - Options: Included in fees, Billed at cost, Billed with markup (specify %),
     Capped at amount
   - _Why this matters_: Expense disputes are a common client complaint.

**Fee structure checklist:**

- [ ] Fee type clearly defined
- [ ] Rates specified (hourly: by timekeeper; flat: total and payment schedule)
- [ ] Retainer amount and replenishment terms
- [ ] Expense categories and billing method
- [ ] Billing frequency (monthly, quarterly, upon completion)
- [ ] Payment terms (due upon receipt, Net 30, etc.)
- [ ] Late payment consequences (interest, suspension of work)
- [ ] Fee disputes process

[JURISDICTION-SPECIFIC] **Contingency fee restrictions** [VERIFY]:

- Criminal cases: Generally prohibited
- Domestic relations: Prohibited for divorce property/alimony in most jurisdictions
- Written agreement required: Specific disclosure requirements vary by state
- Maximum percentages: Some jurisdictions cap contingency fees
- Settlement vs. trial: Sliding scale disclosures required

[JURISDICTION-SPECIFIC] **Fee disclosure requirements** [VERIFY]:

- **New York Part 1215**: Written letter required for domestic relations matters
  with specific disclosures
- **California**: Written fee agreements required for contingent and certain other
  matters; specific arbitration disclosure
- **UK SRA**: Price transparency for certain services; complaints procedure disclosure

### Step 6: Engagement Letter Drafting

Draft or generate an engagement letter that documents the attorney-client relationship,
scope of representation, and terms.

**CLARIFY** — Engagement letter scope:

"What scope of representation should the engagement letter cover?

- **Limited scope**: Specific tasks only (e.g., 'review of contract,' 'opinion letter on X')
- **Matter-specific**: Full representation on this matter only
- **Ongoing relationship**: General representation with matter-by-matter assignments
- **Unbundled services**: Specified tasks; client responsible for remainder

_Why this matters_: Scope creep and implied ongoing representation are major malpractice
risk areas."

**Required engagement letter elements:**

| Section                     | Required Content                                                        | Compliance Notes                                                          |
| --------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Parties**                 | Client name (legal entity), firm name, responsible attorney(s)          | Identify who is NOT the client (e.g., corporate officer individually)     |
| **Scope of Services**       | Specific services included, explicit exclusions                         | Critical for avoiding scope creep and claims of inadequate representation |
| **Fees and Billing**        | Fee structure, rates, retainer, expenses, billing frequency             | State-specific requirements; trust account disclosures                    |
| **Communication**           | Update frequency, preferred channels, who may communicate               | Managing expectations; authorized contacts                                |
| **Client Responsibilities** | Document provision, availability, truthfulness, payment                 | Basis for withdrawal if not met                                           |
| **Confidentiality**         | Confirmation of attorney-client privilege; exceptions                   | Required disclosures (fraud, imminent harm)                               |
| **Conflicts**               | Current conflict status; waiver if applicable; future conflict handling | Informed consent requirements                                             |
| **Termination**             | How either party may end the relationship; consequences                 | Withdrawal procedures; file retention                                     |
| **File Retention**          | How long files retained; format; destruction policy                     | Comply with bar requirements                                              |
| **Dispute Resolution**      | Arbitration/mediation for fee disputes; malpractice claims              | Cannot limit malpractice liability in some jurisdictions                  |
| **Signatures**              | Client signature acknowledging terms; firm signature                    | E-signature acceptable in most jurisdictions                              |

**CLARIFY** — Special provisions:

"Do any of the following special provisions apply?

- [ ] **Joint representation**: Multiple clients with aligned interests (joint defense,
      co-defendants) — requires conflict waiver and common interest disclosure
- [ ] **Third-party payer**: Someone other than the client is paying fees — requires
      independence and confidentiality disclosures
- [ ] **Limited scope representation**: Unbundled services — requires clear boundaries
- [ ] **Advance conflict waiver**: For future conflicts — must be specific and informed
- [ ] **Alternative fee arrangement**: Non-standard fee structure — requires detailed terms
- [ ] **Insurance defense**: Tripartite relationship disclosures"

**Generate the engagement letter** using the collected information and firm templates.
Ensure all jurisdiction-specific requirements are included.

### Step 7: Comprehensive Conflict Check

After the prospective client has agreed to engage (or contemporaneously with engagement
letter signing), run the comprehensive conflict check.

This step expands on the preliminary check in Step 2 by including:

- All parties now known from the full matter intake
- Related parties, subsidiaries, and affiliates
- Key witnesses and their counsel
- Insurance carriers and their counsel
- Expert witnesses and consultants
- Any additional parties identified during consultation

**Conflict check categories:**

| Type                       | Rule           | Assessment                                                                    | Resolution                                    |
| -------------------------- | -------------- | ----------------------------------------------------------------------------- | --------------------------------------------- |
| **Current client adverse** | Rule 1.7(a)(1) | Direct adversity in any matter?                                               | Decline or informed consent (if consentable)  |
| **Material limitation**    | Rule 1.7(a)(2) | Does another client, personal interest, or relationship limit representation? | Decline or informed consent                   |
| **Former client**          | Rule 1.9       | Same or substantially related matter? Confidential information risk?          | Decline or informed consent of former client  |
| **Prospective client**     | Rule 1.18      | Significantly harmful information from declined prospective client?           | Decline or screening + consent                |
| **Imputed conflicts**      | Rule 1.10      | Does any lawyer's conflict impute to the firm?                                | Screening (if permitted), consent, or decline |

**Document the comprehensive check:**

- Complete party list searched
- All databases and systems checked
- Results and analysis for each potential conflict
- Conflict classification (none, waivable, non-waivable)
- Resolution for each (cleared, consented, screened, matter declined)
- Attorney sign-off with date

### Step 8: Engagement Confirmation

Finalize the engagement by obtaining signed agreements and confirming the relationship.

**Engagement confirmation checklist:**

- [ ] Engagement letter signed by client
- [ ] Engagement letter signed by authorized firm representative
- [ ] Retainer payment received (if required)
- [ ] Retainer deposited to trust account
- [ ] KYC/AML documentation complete
- [ ] Conflict check documentation filed
- [ ] Client contact information verified
- [ ] Billing information collected
- [ ] Client preferences documented (communication, format, etc.)

**CLARIFY** — If any items are incomplete:

"The following items are still outstanding before engagement is complete:
[list outstanding items]

Options:

- Wait for completion before opening matter
- Open matter with conditions (specify what is pending)
- Escalate to responsible attorney for decision"

### Step 9: Matter File Setup

Create the matter file and set up the engagement in firm systems.

**Matter setup checklist:**

| Task                 | Description                                        | System/Location            |
| -------------------- | -------------------------------------------------- | -------------------------- |
| **Matter number**    | Generate unique matter identifier                  | Practice management system |
| **Client record**    | Create or link to existing client                  | CRM / Client database      |
| **Matter type**      | Classify by practice area, matter type             | Coding system              |
| **Team assignment**  | Assign responsible attorney, team members, support | Staffing system            |
| **Billing setup**    | Enter fee arrangement, rates, retainer             | Billing system             |
| **Document folder**  | Create folder structure per firm protocol          | DMS                        |
| **Calendar entries** | Add key dates, deadlines, statute of limitations   | Calendar system            |
| **Conflict parties** | Enter all parties for ongoing conflict checking    | Conflict system            |
| **Budget**           | Create matter budget if required                   | Budget tracker             |

**Statutory deadline tracking:**

**CLARIFY** — "Does this matter have any statutory deadlines that must be calendared
immediately?

- Statute of limitations date
- Filing deadlines
- Response deadlines
- Regulatory deadlines
- Contractual deadlines

_Why this matters_: Missing a statutory deadline is a leading cause of malpractice claims."

### Step 10: Client Welcome and Onboarding

Complete the onboarding by providing the client with welcome materials and establishing
communication protocols.

**Welcome packet contents:**

- [ ] Welcome letter from responsible attorney
- [ ] Copy of signed engagement letter
- [ ] Firm contact information (who to contact for what)
- [ ] Client portal access instructions (if applicable)
- [ ] Document upload instructions
- [ ] Communication preferences confirmation
- [ ] Key dates and next steps
- [ ] Billing FAQ / payment methods
- [ ] Privacy policy / data handling notice

**Communication protocol establishment:**

- [ ] Primary contact identified
- [ ] Preferred communication method (email, phone, portal)
- [ ] Authorized contacts list (who else can communicate)
- [ ] Update frequency expectation (weekly, milestone-based, etc.)
- [ ] Emergency contact procedure
- [ ] Document sharing method established

**Initial matter steps:**

- [ ] Schedule first substantive meeting/call
- [ ] Request initial document package from client
- [ ] Identify immediate deadlines and actions
- [ ] Brief team on engagement
- [ ] Send docketing/calendar invites

### Step 11: Quality Verification

Before marking intake complete, verify all required steps were completed.

**PDCA Quality Cycle:**

**PLAN**: Identified intake as [standard / elevated / high-risk]. Selected [fee structure].
Determined [scope of representation].

**DO**: Executed conflict checks, KYC/AML, engagement letter, matter setup, and client
onboarding steps.

**CHECK**: Run the verification checks below.

**ACT**: Document any exceptions, escalations, or process improvements identified.

**Intake completion verification:**

| Category         | Verification                                                | Status |
| ---------------- | ----------------------------------------------------------- | ------ |
| **Conflicts**    | Preliminary and comprehensive checks documented and cleared |        |
| **KYC/AML**      | Appropriate due diligence completed for risk level          |        |
| **Engagement**   | Signed engagement letter on file                            |        |
| **Financials**   | Retainer received and deposited (if required)               |        |
| **Matter Setup** | Matter file created with proper coding                      |        |
| **Deadlines**    | All known deadlines calendared                              |        |
| **Team**         | Team assigned and briefed                                   |        |
| **Client**       | Welcome packet sent, portal access provided                 |        |

---

## Intake Status Classification

### GREEN — Complete

All intake steps completed. No conflicts identified or all conflicts properly resolved/
waived. Documentation complete. Matter ready for substantive work.

**Criteria:**

- Preliminary and comprehensive conflict checks clear or properly resolved
- KYC/AML appropriate for risk level complete
- Engagement letter signed by all parties
- Retainer received (if required)
- Matter file set up in all systems
- Team assigned
- Client onboarded

### YELLOW — Conditional

Intake substantially complete but one or more items pending. May begin limited work,
but full engagement requires completion.

**Examples:**

- Awaiting retainer payment (engagement letter signed)
- Awaiting conflict waiver signature
- KYC documentation requested but not yet received
- Team assignment pending

**Action**: Track outstanding items. Set deadline for completion. Limit work to
non-billable or explicitly authorized items until resolved.

### RED — Blocked

Intake cannot be completed. Matter must be declined or escalated.

**Examples:**

- Non-waivable conflict identified
- Client failed KYC/AML (suspicious activity, sanctions match)
- Client refuses to sign engagement letter
- Client cannot pay required retainer
- Matter outside firm competence or jurisdiction

**Action**: Decline representation (in writing). Do not perform substantive work.
Return any materials. Advise on statute of limitations if relevant.

---

## Risk Tiering Framework

### Standard Risk

- Individual client, domestic jurisdiction
- Routine matter type in firm's practice areas
- No elevated risk factors
- Clear conflict check
- Straightforward fee arrangement

**Due diligence**: Standard KYC. Routine engagement letter. Normal onboarding.

### Elevated Risk

- Entity client with multiple owners
- Cross-border elements
- Complex matter or novel legal issues
- Moderate transaction value
- Prior law firm relationships to investigate
- Referral from unknown source

**Due diligence**: Enhanced KYC for beneficial owners. Senior attorney review of
engagement. Elevated conflict check (related parties). Document risk factors in file.

### High Risk

- PEP (Politically Exposed Person) or close associate
- High-risk jurisdiction nexus (FATF list, sanctions risk)
- Unusual source of funds or wealth
- Very large transaction value
- Adverse media or reputational concerns
- Red flags during consultation
- Prior SAR filings or regulatory inquiries (if known)

**Due diligence**: Full EDD. In-person identity verification. Source of wealth
documentation. Senior partner approval required. Enhanced monitoring during engagement.
Consider declining if risk cannot be mitigated.

---

## Citation Quality Gates

Run these 5 gates silently before delivering any intake documentation or recommendations.
If any gate fails, revise before delivering.

| Gate           | Rule                                                                              | Fail Action                         |
| -------------- | --------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every regulatory reference cites a specific rule, statute, or requirement         | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All citations follow proper format (e.g., ABA Model Rule 1.7, SRA Code para. 6.2) | Fix format                          |
| **Currency**   | Cited rules checked for amendments                                                | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within the applicable regulatory framework                         | Remove inapplicable requirements    |
| **Confidence** | Uncertainty explicitly stated                                                     | Add confidence qualifier            |

---

## Self-Interrogation for High-Risk Intakes

For any intake classified as High Risk, apply this 3-pass review before recommending
acceptance:

**Pass 1 — Regulatory Compliance**:

- Have all required due diligence steps been completed?
- Is the documentation sufficient to satisfy a regulatory audit?
- Are there any residual red flags that were not resolved?

**Pass 2 — Reputational Risk**:

- If this matter becomes public, would the firm's involvement be defensible?
- Are there any associations that could harm the firm's reputation?
- Has adverse media been thoroughly checked?

**Pass 3 — Economic Rationality**:

- Is the expected fee worth the elevated compliance burden?
- Are there termination risks that would make engagement uneconomical?
- Is the client likely to be a long-term relationship or one-off?

If any pass reveals concerns, document them and require partner-level approval.

---

## Confidence Scoring

For intake decisions and risk classifications, assign a confidence level:

| Level        | Range     | Meaning                                        | Action                         |
| ------------ | --------- | ---------------------------------------------- | ------------------------------ |
| **Definite** | 0.95-1.0  | Clear information, verified identity, no flags | Proceed with standard process  |
| **High**     | 0.80-0.94 | Minor ambiguities but resolvable               | Proceed with documentation     |
| **Probable** | 0.60-0.79 | Some uncertainty, reasonable assumptions       | Flag for attorney review       |
| **Possible** | 0.40-0.59 | Significant gaps or conflicting information    | Escalate before proceeding     |
| **Unlikely** | 0.0-0.39  | Major red flags or verification failures       | Decline or require remediation |

---

## Glass Box Audit Trail

Every completed intake MUST include a Glass Box audit section for traceability:

```yaml
glass_box:
  intake_id: "[Matter number or intake reference]"
  client: "[Client name]"
  matter_type: "[Practice area / matter type]"
  intake_date: "[Date completed]"
  responsible_attorney: "[Name]"
  jurisdiction: "[Firm jurisdiction / regulatory framework]"
  risk_tier: "Standard / Elevated / High"
  conflict_checks:
    preliminary:
      date: "[Date]"
      result: "Clear / Potential / Definite"
      resolution: "[If applicable]"
    comprehensive:
      date: "[Date]"
      parties_checked: "[Number]"
      result: "Clear / Waived / Screened"
  kyc_aml:
    level: "Standard CDD / Enhanced DD"
    identity_verified: "Yes / Pending / N/A"
    source_of_funds: "Verified / Documented / Not required"
    pep_screening: "Clear / Flagged / N/A"
    sanctions_screening: "Clear / Flagged"
  engagement:
    letter_signed: "Yes / Pending"
    retainer_received: "Yes / Waived / Pending"
    scope: "Limited / Matter-specific / Ongoing"
  matter_setup:
    file_created: "Yes / Pending"
    team_assigned: "Yes / Pending"
    deadlines_calendared: "Yes / N/A / Pending"
  status: "GREEN (Complete) / YELLOW (Conditional) / RED (Blocked)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any assumptions, pending items, or scope limitations]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in client intake:

1. **Skipping the preliminary conflict check** — Receiving confidential information before
   checking conflicts can disqualify the entire firm under Rule 1.18. Always screen before
   substantive discussions.

2. **Incomplete party identification** — Checking only the named parties misses corporate
   affiliates, related individuals, and adverse parties. Expand the search to related
   parties.

3. **Applying the wrong KYC level** — Using standard due diligence for a high-risk client
   creates regulatory exposure. Match due diligence to risk tier.

4. **Generic engagement letters** — Using a one-size-fits-all template without adapting
   to the specific matter, fee arrangement, and jurisdictional requirements leads to gaps
   and disputes.

5. **Unclear scope of representation** — Failing to define what is and is not included
   creates scope creep and implied obligations. Be explicit about exclusions.

6. **Ignoring red flags** — Dismissing client inconsistencies, unusual circumstances,
   or negative references without investigation. Document and escalate red flags.

7. **Accepting retainers before conflict clear** — Depositing a retainer before conflicts
   are resolved creates complications if the matter must be declined.

8. **Missing statute of limitations** — Failing to immediately calendar known deadlines.
   This is a leading cause of malpractice claims.

9. **No written fee agreement** — Many jurisdictions require written agreements for
   certain fee types. Even where not required, absence creates disputes.

10. **Failing to identify the actual client** — For entity representations, confusing the
    entity with its officers/owners leads to conflict issues and privilege problems.

11. **Inadequate entity verification** — Accepting verbal authority to engage without
    written authorization from the entity creates validity questions.

12. **Tipping off on AML concerns** — If a SAR is filed, disclosure to the client is a
    criminal offense in many jurisdictions.

13. **Proceeding without full intake documentation** — Starting work before intake is
    complete creates risk if the engagement later fails.

14. **Single point of failure in conflict checks** — Relying on one database or one
    person to catch conflicts. Use multiple checks and systems.

15. **Assuming jurisdiction requirements** — Applying home jurisdiction rules to a
    client/matter governed by different rules. Research applicable requirements.

---

## Writing Standards

Apply plain-language discipline to all intake documentation:

**For engagement letters** (client-facing):

- Plain language. Avoid unnecessary legalese.
- Short sentences. One concept per paragraph.
- Active voice: "We will represent you" not "Representation shall be provided"
- Clear headings for each topic
- Contact information prominent
- Key terms defined simply

**For internal intake memos**:

- Same plain-language standards
- Document decision rationale
- Flag any exceptions or unusual circumstances
- Include Glass Box audit trail

**Quality gates before completion**:

1. Can a non-lawyer client understand the engagement letter?
2. Could intake documentation survive a bar audit?
3. Are all required elements present for the jurisdiction?
4. Is the conflict analysis documented sufficiently for future review?
5. Would a successor attorney understand the matter from the file?

---

## External Tool Integration

This skill integrates with **legalcode-mcp** for regulatory research and verification.

**With legalcode-mcp connected:**

- Search for jurisdiction-specific bar rules on conflicts, fees, and engagement
- Verify current AML/KYC requirements for the applicable regime
- Research any novel conflict scenarios against ethics opinions
- Check for recent disciplinary actions or rule changes
- Mark all legalcode-mcp-sourced references as VERIFIED

**Without legalcode-mcp:**

- Mark all regulatory references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Use general knowledge of professional responsibility rules
- Recommend verification against current bar rules before relying on requirements

---

## Output Format Template

Structure the completed intake documentation as:

```markdown
## Client Intake Summary

**Intake ID**: [number]
**Client**: [name]
**Matter**: [brief description]
**Matter Type**: [practice area / type]
**Responsible Attorney**: [name]
**Intake Date**: [date]

---

## Intake Status: [GREEN / YELLOW / RED]

[If YELLOW: List outstanding items]
[If RED: Reason for block and recommended action]

---

## Conflict Check Summary

| Check         | Date   | Result   | Resolution   |
| ------------- | ------ | -------- | ------------ |
| Preliminary   | [date] | [result] | [resolution] |
| Comprehensive | [date] | [result] | [resolution] |

**Parties Checked**: [list]

---

## KYC/AML Summary

**Risk Tier**: [Standard / Elevated / High]
**Due Diligence Level**: [Standard CDD / Enhanced DD]

| Item                  | Status   |
| --------------------- | -------- |
| Identity Verification | [status] |
| Address Verification  | [status] |
| Source of Funds       | [status] |
| PEP Screening         | [status] |
| Sanctions Check       | [status] |

---

## Engagement Terms

**Scope**: [scope of representation]
**Fee Structure**: [type and details]
**Retainer**: [amount and status]
**Billing**: [frequency and terms]

---

## Matter Setup

- [ ] Matter file created: [number]
- [ ] Team assigned: [names]
- [ ] Deadlines calendared: [key dates]
- [ ] Client onboarded: [portal access, welcome sent]

---

## Risk Factors and Notes

[Any elevated risk factors, red flags, or special considerations]

---

## Next Steps

1. [First action item]
2. [Second action item]
3. [...]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill is jurisdiction-agnostic. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with specific bar rules and requirements
2. Replace [VERIFY] tags with verified regulatory citations
3. Add jurisdiction-specific intake requirements (e.g., NY Part 1215, California rules)
4. Add jurisdiction-specific KYC/AML requirements (MLR 2017 for UK, state bar for US)
5. Include local engagement letter templates or requirements
6. Add jurisdiction-specific anti-patterns
7. Update frontmatter to reference the specific jurisdiction

**Key jurisdiction variations to address:**

- **US (by state)**: Varies significantly by state bar; ABA Model Rules as baseline
- **UK (England & Wales)**: SRA Code of Conduct, MLR 2017, LSAG guidance
- **EU**: National bar rules plus EU AML Directives
- **Canada**: Provincial law societies with varying requirements
- **Australia**: State-based legal profession acts

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis combining professional responsibility
requirements, AML/KYC best practices, engagement letter standards, and law firm intake
workflows into a comprehensive jurisdiction-agnostic skill. Research sources include ABA
Model Rules, SRA Code of Conduct, MLR 2017 requirements, FATF recommendations, and law
firm practice management best practices.
