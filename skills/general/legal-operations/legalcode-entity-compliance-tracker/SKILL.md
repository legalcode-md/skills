---
name: legalcode-entity-compliance-tracker
description: Track corporate entity compliance obligations across jurisdictions and generate compliance
  calendars. Use when managing annual reports, franchise tax filings, registered agent maintenance, officer
  and director changes, good standing certificates, business license renewals, or beneficial ownership
  filings for one or more legal entities. Covers domestic and foreign-qualified entities across all US
  states, UK Companies House, Australian ASIC, Canadian federal and provincial, and other major jurisdictions.
  Flags overdue and upcoming filings, classifies compliance status (COMPLIANT / SCHEDULED / APPROACHING
  / URGENT / CRITICAL / UNKNOWN), and produces executive dashboards, operational calendars, entity-level
  reports, and prioritized action lists. Also use when onboarding acquired entities, building compliance
  programs from scratch, or auditing a multi-subsidiary corporate structure for compliance gaps. Jurisdiction-agnostic
  with [JURISDICTION-SPECIFIC] markers.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Entity Compliance Tracker

> **Disclaimer**: This skill provides a framework for AI-assisted corporate entity
> compliance tracking. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional licensed in the relevant jurisdiction before use. Filing
> deadlines, fee amounts, and statutory requirements change frequently — verify current
> applicability against authoritative Secretary of State and regulatory authority publications
> before relying on any provision described here. Statutory and regulatory references carry
> hallucination risk — verify against primary sources before acting. This skill does not
> replace a qualified registered agent service or corporate counsel.

## Purpose and Scope

This skill tracks ongoing entity compliance obligations for one or more legal entities
across any combination of jurisdictions. It builds or audits compliance calendars, flags
delinquent and at-risk filings, classifies each obligation's status, and produces
actionable reports for legal operations teams, corporate counsel, and business stakeholders.

**Covers:**

- Annual reports, biennial statements, and periodic filings with Secretaries of State
- Franchise tax, alternative entity tax, and related state tax obligations
- Registered agent maintenance, changes, and resignation response
- Officer and director change notification requirements
- Good standing certificates — when required, how to obtain, and validity periods
- Business licenses — state, local, and professional license renewals
- Foreign qualification — triggering events, certificates of authority, and withdrawal
- Beneficial ownership information (BOI) reporting under the Corporate Transparency Act [VERIFY current enforcement status]
- Multi-entity portfolio management and subsidiary compliance audits
- Post-acquisition compliance integration workflows

**Does not:**

- File documents directly with government agencies (produces instructions for filing)
- Provide legal advice or replace qualified corporate counsel or registered agent services
- Calculate income taxes, payroll taxes, or federal corporate tax obligations
- Monitor litigation or regulatory enforcement actions
- Replace a purpose-built entity management system (CT Corporation, CSC, Harbor Compliance, etc.)

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. Compliance obligations are determined by each entity's
state/country of formation and every jurisdiction where it holds a certificate of authority
(foreign qualification). The skill adapts its analysis to whichever jurisdictions are relevant
to the portfolio being tracked.

[JURISDICTION-SPECIFIC] Core jurisdiction-specific variations the skill must recognize:

**United States (federal + state):**

- Each state has its own annual report form, deadline pattern (fixed date, anniversary-based,
  or fiscal-year-based), fee schedule, and enforcement timeline before administrative dissolution
- Delaware: most commonly used incorporation state; annual report + franchise tax due March 1
  (corporations) and June 1 (LLCs — flat $300 tax); Authorized Shares vs. Assumed Par Value
  Capital Method election is critical for corporations with large authorized share counts
- California: dual-track compliance (Secretary of State Statement of Information + Franchise
  Tax Board $800 minimum annual tax); suspension by FTB and SOS are independent and both
  can apply simultaneously [VERIFY current FTB thresholds]
- Florida: May 1 annual report deadline; $400 late fee after May 1; administrative dissolution
  triggered after the third Friday of September [VERIFY current dissolution timeline]
- Texas: franchise tax report due May 15; separate from income tax; calculated on gross receipts
  [VERIFY current rate schedule]

**United Kingdom:**

- Companies House: confirmation statement due within 14 days of the 12-month review period end;
  annual accounts due 9 months after accounting reference date (private companies); separate
  obligations with separate penalties [VERIFY current Companies House fee schedule]
- Director appointment, resignation, and address changes: Form AP01, TM01, CH01 — each due
  within 14 days [VERIFY current filing period]
- Strike-off proceedings for non-compliance; criminal liability for directors who fail to file

**Australia:**

- ASIC annual review: entities receive an annual review notice on their anniversary date;
  review fee due within 2 months; late fees apply [VERIFY current ASIC fee schedule]
- Director and officer changes: due within 28 days of change [VERIFY]
- ASIC-initiated deregistration for non-payment

**Canada:**

- Federal corporations (Canada Business Corporations Act): annual return due 60 days after
  anniversary of incorporation [VERIFY current deadline and fee]
- Director changes: due within 15 days to Corporations Canada [VERIFY]
- Provincial variations: each province has its own requirements for provincial corporations
  and foreign-registered companies [JURISDICTION-SPECIFIC — verify per province]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than proceeding
on assumptions that would undermine the reliability of the compliance calendar, the workflow
pauses and asks when:

- The scope of the portfolio is unclear (how many entities, which jurisdictions)
- Critical data fields are missing (formation date, registered agent, EIN)
- The engagement mode would change the output format materially
- Good standing status cannot be confirmed from available data

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

### Step 1: Accept Input and Determine Engagement Mode

Accept input in any of these formats:

- **Entity roster**: Spreadsheet, CSV, or list of entity names with states of incorporation
  and foreign qualification states
- **Existing compliance records**: Prior compliance calendar, entity management system export,
  or registered agent status report
- **Portfolio description**: Verbal description of the corporate structure
  (e.g., "12 US entities all Delaware-incorporated, 2 UK Ltds, 1 Canadian federal corp")
- **Single entity assessment**: One entity's name, formation details, and jurisdiction list
- **Trigger event**: "We just acquired [Company X] — what are their compliance obligations?"
  or "We hired our first Texas employee — what does that trigger?"

**⟁ CLARIFY** — Before beginning, ask the user to confirm:

1. **Operating mode**: Which best describes the goal?
   - Options: **Full Portfolio Audit** (comprehensive status of all entities), **Calendar
     Generation** (build or refresh a 12-month compliance calendar), **Overdue Triage**
     (identify and remediate delinquent filings only), **Acquisition Integration** (onboard
     a newly acquired entity's obligations), **Single Jurisdiction Deep-Dive** (all
     obligations in one state or country), **Nexus Analysis** (assess whether new activity
     in a state triggers foreign qualification)
   - _Why this matters_: Each mode produces different primary outputs and has different
     data requirements.

2. **Output format desired**:
   - Options: Executive status dashboard only, Full operational compliance calendar,
     Entity-level compliance reports, Overdue action list, All of the above
   - _Why this matters_: Determines the structure and scope of the deliverable.

3. **Tracking window**:
   - Options: Rolling 12 months from today (default), Calendar year, Fiscal year, Custom range
   - _Why this matters_: Determines which upcoming obligations are in scope.

If the user provides partial context, proceed with defaults (Full Portfolio Audit, all
outputs, rolling 12 months) and state assumptions explicitly.

---

### Step 2: Build or Validate the Entity Roster

For each entity in the portfolio, collect or confirm the following core identity data.
Flag missing fields immediately — they block accurate compliance tracking.

**Minimum required fields per entity:**

| Field                                              | Required?            | Notes                                               |
| -------------------------------------------------- | -------------------- | --------------------------------------------------- |
| Legal name (exact, as registered)                  | **Required**         | Must match state records exactly                    |
| Entity type                                        | **Required**         | C-Corp, S-Corp, LLC, LP, LLP, Ltd, GmbH, etc.       |
| State/country of formation                         | **Required**         | Domestic jurisdiction                               |
| Formation date                                     | **Required**         | Drives anniversary-based deadlines                  |
| Fiscal year end                                    | **Required**         | Drives franchise tax deadlines in some states       |
| EIN / Company Registration Number                  | **Required**         | Tax ID and state identification                     |
| All foreign qualification jurisdictions            | **Required**         | Every state/country with a certificate of authority |
| Registered agent name and address per jurisdiction | **Required**         | Must be current on file with the state              |
| Internal owner (attorney/paralegal/team)           | **Required**         | For alert routing and escalation                    |
| Nature of business                                 | **Required**         | Required on most annual reports                     |
| Current officer/director roster                    | Strongly recommended | Required on most annual report forms                |
| Authorized shares / issued shares                  | Conditional          | Required for Delaware franchise tax (corporations)  |
| Gross assets                                       | Conditional          | Required for Delaware APVC franchise tax method     |
| Parent entity / subsidiaries                       | Recommended          | Enables corporate group compliance mapping          |

**⟁ CLARIFY** — For any entity where foreign qualification states are unknown: ask whether
the entity has employees, physical offices, bank accounts, real property, or substantial
ongoing sales activity in states beyond its formation state. Each such nexus likely requires
foreign qualification. If the answer is uncertain, recommend a nexus analysis before
finalizing the entity roster.

**Blocking gaps** — Do not proceed without these. Treat any entity missing its formation
date, registered agent, or EIN as UNKNOWN status until the data is confirmed.

---

### Step 3: Map All Filing Obligations Per Entity

For each entity in each jurisdiction where it is formed or foreign-qualified, enumerate
every recurring and event-driven compliance obligation. Build a **Filing Obligation Matrix**:
entity × jurisdiction × filing type × frequency × deadline.

#### Category A — Annual/Periodic State Filings

The foundational compliance obligation. Almost every formal business entity must file annual
or periodic information reports with the Secretary of State (or equivalent authority) in
every jurisdiction where it is formed or qualified to do business.

| Filing Type              | Key Jurisdictions                               | Pattern                                            | Notes                                                                                           |
| ------------------------ | ----------------------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Annual report            | Most US states                                  | Fixed date or anniversary                          | Content varies by state; typically includes officer list, principal address, nature of business |
| Biennial statement       | NY, FL (biennial), NV (biennial for some types) | Every 2 years                                      | Do not confuse biennial with annual                                                             |
| Statement of Information | California                                      | Corps: biennial in anniversary month; LLCs: annual | Separate from FTB obligations                                                                   |
| Confirmation statement   | UK Companies House                              | Within 14 days of 12-month review period end       | Confirms or updates basic company information                                                   |
| Annual accounts          | UK, Ireland, Germany                            | Private UK: 9 months after ARD                     | Separate from confirmation statement; requires financial statements                             |
| Annual return            | Canada federal, most provinces                  | 60 days after anniversary (federal CBCA)           | [VERIFY per province]                                                                           |
| Annual review            | Australia ASIC                                  | Anniversary date                                   | Entity receives notice; fee due within 2 months                                                 |

**[JURISDICTION-SPECIFIC] Key US state deadline patterns:**

| State                    | Filing                               | Deadline Pattern                              | Base Fee                      |
| ------------------------ | ------------------------------------ | --------------------------------------------- | ----------------------------- |
| Delaware (Corps)         | Annual Report + Franchise Tax        | March 1                                       | $50 + tax (min $175)          |
| Delaware (LLC/LP/GP)     | Annual Tax                           | June 1                                        | $300 flat                     |
| Delaware (Foreign Corps) | Annual Report                        | June 30                                       | $125                          |
| California (Corps)       | Statement of Information             | Biennial, anniversary month                   | $25                           |
| California (LLCs)        | Statement of Information             | Annual, anniversary month                     | $20                           |
| Florida (Corps)          | Annual Report                        | May 1 (late fee); Sept. 3rd Fri (dissolution) | $138.75                       |
| New York (Corps)         | Biennial Statement                   | Biennial, anniversary month                   | $9/2yr                        |
| Texas                    | Franchise Tax Report                 | May 15                                        | No fee (tax payment separate) |
| Wyoming                  | Annual Report                        | Anniversary month                             | Min. $60                      |
| Nevada                   | Annual List + State Business License | Anniversary month                             | Variable                      |
| Pennsylvania             | Annual Report                        | December 31                                   | [VERIFY — implemented 2024]   |
| Georgia                  | Annual Registration                  | April 1                                       | $50+                          |
| North Carolina           | Annual Report                        | April 15                                      | $25 (corps); $200 (LLCs)      |
| Colorado                 | Periodic Report                      | Anniversary month (2-month window)            | $10                           |
| Illinois                 | Annual Report                        | Varies by entity type                         | [VERIFY]                      |

All fees should be verified against the current Secretary of State website before filing —
fee schedules change without notice.

#### Category B — Franchise Tax and Entity Tax

Franchise tax is distinct from income tax. It is a privilege tax for the right to exist as
or transact business as a legal entity in a state. Not all states impose franchise tax;
some impose it under different names (Commercial Activity Tax, Business Privilege Tax, etc.).

**Delaware franchise tax — critical notes for corporations:**

The default Authorized Shares Method systematically overcharges entities with many authorized
but few issued shares (common startup cap table). Always calculate both methods:

- **Authorized Shares Method**: Number of authorized shares × per-share rate (ranging from
  $0.0001 to higher tiers based on authorization brackets; minimum $175). A corporation
  with 10 million authorized shares may generate a bill of $85,000+ under this method.

- **Assumed Par Value Capital Method (APVC)**: Uses gross assets divided by total issued
  shares to derive an assumed par value, then taxes only issued shares at that rate.
  For a startup with $5M in assets and 2M issued shares out of 10M authorized, this method
  typically yields $400–$5,000 in tax.

The entity may explicitly elect the APVC method when filing — always calculate both and
select the lower. Failure to calculate both methods is one of the most costly and common
entity compliance errors. [VERIFY current rate schedule with Delaware Division of Corporations]

**Other franchise tax obligations:**

| State      | Tax Type                     | Basis                    | Deadline                             | Notes                                    |
| ---------- | ---------------------------- | ------------------------ | ------------------------------------ | ---------------------------------------- |
| California | Minimum franchise tax        | Net income; $800 minimum | 15th day of 4th month of tax year    | FTB obligation separate from SOS SOI     |
| Texas      | Franchise tax                | Gross receipts           | May 15                               | 0.75% general rate (verify current rate) |
| Nevada     | Modified Business Tax        | Wages                    | Quarterly                            | Employer obligation                      |
| Illinois   | Franchise tax                | Paid-in capital          | 15th day of 3rd month after tax year | [VERIFY — subject to possible phase-out] |
| New York   | Capital base / fixed minimum | Business capital         | March 15 (calendar year corps)       | [VERIFY]                                 |

[JURISDICTION-SPECIFIC] Verify current rates, thresholds, and filing mechanics for each
jurisdiction directly from the relevant taxing authority — franchise tax rates and structures
change regularly.

#### Category C — Registered Agent Obligations

Every US state and most non-US jurisdictions require every registered formal business entity
to maintain a designated registered agent with a physical street address (not a P.O. box)
in that jurisdiction.

**Tracking requirements:**

- Registered agent name on file in each jurisdiction (confirm matches state records)
- Registered agent street address in each jurisdiction (confirm is current physical address)
- Registered agent fee payment status (commercial agents resign upon non-payment)
- Date of last registered agent confirmation or communication
- Change of registered agent filing requirements: typically a Statement of Change filed with
  the Secretary of State (fee $25–$50 per state); effective immediately or upon filing

**Flag immediately if:**

- Any jurisdiction lacks a registered agent on file
- The agent on file has the wrong address
- The entity has not confirmed registered agent status within the past 12 months
- A commercial registered agent has issued a resignation notice

**Consequences of losing the registered agent:**
Service of process may be delivered to the Secretary of State as substitute (entity never
receives actual notice of a lawsuit), good standing is lost immediately in most states, and
administrative dissolution proceedings may commence within 30–60 days.

#### Category D — Officer and Director Records

Most states require officer and director information to be current on file with the Secretary
of State. The timing of required updates varies significantly:

| Jurisdiction                | Officer/Director Change Filing                                     | Deadline                                 |
| --------------------------- | ------------------------------------------------------------------ | ---------------------------------------- |
| Most US states (MBCA-based) | Update via next annual report                                      | Next annual report due date              |
| Florida                     | Online update available immediately                                | Best practice: update promptly           |
| UK Companies House          | Form AP01 (appointment), TM01 (resignation), CH01 (address change) | 14 days from change                      |
| Australia ASIC              | RA71/RA61 equivalent                                               | 28 days from change                      |
| Canada (federal CBCA)       | Director change notification                                       | 15 days from change                      |
| Germany                     | Geschäftsführer-Änderung                                           | Within 3 weeks for notarization [VERIFY] |

Even where no interim filing is strictly required (most MBCA states), best practice is to
update state records promptly upon any officer or director change. Stale records create
problems for banking, lending, M&A due diligence, and notarization requirements.

#### Category E — Good Standing Certificates

A Certificate of Good Standing (also called Certificate of Existence or Certificate of
Status) is an official state-issued document confirming the entity is registered, current
on all filings, current on all taxes and fees, and has not been dissolved or suspended.

**When required:**

- Opening or modifying business bank accounts
- Applying for business loans, credit lines, or SBA financing
- Foreign qualification in a new state (requires a certificate from the home state)
- M&A transactions — buy-side and sell-side due diligence
- Government contract applications
- Major commercial agreements (particularly with institutional counterparties)
- Real estate closings
- Professional license renewals

**Validity:** Certificates reflect status as of the date issued. Requesters typically
require issuance within 30–90 days; financial institutions often require within 60 days.

**Tracking requirement:** Maintain a record of the most recently obtained certificate per
jurisdiction per entity, with the date obtained. Flag any entity for which a certificate
has not been confirmed within 12 months or where a certificate is known to be needed within
60 days.

#### Category F — Business Licenses

**State business licenses**: Certain states require a general business license to operate
(Nevada: mandatory State Business License, $200 annually; Washington state: Unified Business
Identifier + Business License). Most states do not have a general business license but
require industry-specific licenses.

**Local business licenses**: City and county business licenses are required in most US
municipalities and many international jurisdictions. These are typically annual, tied to
the physical address of operations, and managed separately from state obligations.

**Professional and industry licenses**: Any entity operating in a regulated profession
(healthcare, legal, financial services, insurance, construction, childcare, food service)
must track professional and occupational licenses separately. These have their own renewal
cycles (typically annual or biennial) and are issued by state licensing boards.

**Key tracking fields per license:**

- License type and issuing authority
- License number
- Effective and expiration dates
- Renewal deadline (often 30–90 days before expiration)
- Required renewal documentation
- Fee amount

#### Category G — Event-Driven Obligations

These obligations are triggered by specific corporate events rather than the calendar:

| Trigger Event                        | Required Filing                                                  | Typical Deadline                                             |
| ------------------------------------ | ---------------------------------------------------------------- | ------------------------------------------------------------ |
| Change of registered agent           | Statement/Certificate of Change of Agent                         | Immediate (file as soon as new agent confirmed)              |
| Change of principal office address   | Statement of Change of Address                                   | Per state; many require prompt filing                        |
| Change of registered office address  | Statement of Change of Registered Office                         | Per state; many require prompt filing                        |
| Change of officers/directors         | Annual report update or interim form                             | Per jurisdiction (see Category D)                            |
| Beneficial ownership change (US CTA) | FinCEN BOI update report                                         | 30 days from change [VERIFY current CTA enforcement status]  |
| New state operations (nexus trigger) | Certificate of authority / foreign qualification                 | Before or promptly upon commencement of business             |
| Entity name change                   | Certificate of Amendment                                         | Per state; effective upon filing                             |
| Merger or conversion                 | Certificate of Merger / Conversion + foreign state notifications | Per state timeline; withdrawal filings in all foreign states |
| Dissolution / winding up             | Certificate of Dissolution + withdrawal from all foreign states  | Per state                                                    |

---

### Step 4: Calculate All Deadlines for the Tracking Window

For each obligation identified in Step 3, calculate:

1. **Statutory deadline**: The actual regulatory due date
2. **Internal action deadline**: Statutory deadline minus the filing-type-specific lead time
3. **Data collection deadline**: Internal action deadline minus preparation time
4. **Alert trigger dates**: 90 / 60 / 30 / 14 / 7 days before internal action deadline

**Standard lead times by filing complexity:**

| Filing Type                                 | Preparation Window                                | Internal Buffer Before Statutory |
| ------------------------------------------- | ------------------------------------------------- | -------------------------------- |
| Annual report (simple, online)              | 10 business days                                  | 5 business days                  |
| Annual report (complex, with financials)    | 30 calendar days                                  | 7 business days                  |
| UK annual accounts (requiring audit)        | 90 calendar days                                  | 10 business days                 |
| Delaware franchise tax (APVC calculation)   | 14 calendar days                                  | 5 business days                  |
| BOI report / 30-day update                  | 5 business days                                   | 2 business days                  |
| Certificate of authority (new state)        | 20 business days                                  | N/A (trigger-based)              |
| Good standing certificate (ordered for use) | 5 business days lead; order 30 days before needed | Order 30 days before needed      |
| Business license renewal                    | 15 business days                                  | 7 business days                  |
| Registered agent change filing              | 5 business days                                   | N/A (trigger-based)              |

**Date calculation rules:**

- If a statutory deadline falls on a weekend or federal/national holiday, assume the next
  business day applies unless the jurisdiction specifies otherwise (verify per jurisdiction)
- Anniversary-based deadlines: use the entity's exact formation date to calculate the
  correct month and/or date
- California Statement of Information for corporations: due in the anniversary month of the
  filing anniversary, not the formation date
- Delaware annual report: always March 1 for domestic corporations regardless of fiscal
  year end (June 30 for foreign corporations; June 1 for LLCs/LPs/GPs)
- UK confirmation statement: 12-month review period runs from incorporation date (for new
  companies) or from the end of the previous confirmation statement period

---

### Step 5: Classify Compliance Status

Apply the six-tier status classification to each filing obligation based on the current date
relative to deadlines and on the completeness and verifiability of data.

See **Compliance Status Classification** section below for the full six-tier system
(COMPLIANT / SCHEDULED / APPROACHING / URGENT / CRITICAL / UNKNOWN) and the decision rules
for each tier.

**⟁ CLARIFY** — Before classifying as COMPLIANT, confirm: "Do you have a confirmation
number, receipt, or state acknowledgment for this filing? Or are you relying on internal
records that the filing was submitted?" Unconfirmed filings should be classified as
APPROACHING or UNKNOWN, not COMPLIANT.

---

### Step 6: Validate Against Registered Agent Records

Cross-reference the entity roster against registered agent confirmation data:

- Is a registered agent on file in every jurisdiction where the entity is formed or qualified?
- Is the registered agent's address current with the state? (Common failure: the RA changed
  addresses and did not update the state record)
- Are registered agent fees current? (Commercial agents resign upon non-payment)
- Has the registered agent provided any notices — delinquency notices, resignation notices,
  service of process receipt?

**⟁ CLARIFY** — Ask: "Do you have direct access to your registered agent's portal or
confirmation of current status for each entity? If yes, please provide the most recent
good standing confirmation or portal export. If no, these entities should be classified as
UNKNOWN until verified."

**Warning**: State delinquency notices, annual report reminders, and service of process are
sent to the registered agent's address on file with the state — not to the company's principal
office. If the registered agent information is stale, the company may have received no notice
of delinquency and no notice of lawsuits or regulatory actions.

---

### Step 7: Triage CRITICAL and URGENT Items

Before generating calendar outputs, run a triage pass to surface and prioritize delinquent
and at-risk obligations.

**Triage protocol:**

1. **CRITICAL items** (past statutory deadline, not confirmed filed):
   - Determine whether the entity can be reinstated or the filing made late
   - Calculate penalty and interest accrued (see jurisdiction-specific penalty structures)
   - Determine whether good standing has been lost and whether administrative dissolution
     proceedings have commenced
   - Identify reinstatement requirements: back fees + penalties + reinstatement form + current
     annual report (all jurisdictions with reinstatement procedures vary — [VERIFY per state])
   - Flag any entity in administrative dissolution for immediate escalation

2. **URGENT items** (internal deadline passed, statutory deadline not yet reached):
   - Confirm whether a rush or expedited filing is available (most Secretary of State offices
     offer expedited processing for an additional fee)
   - Identify the responsible owner and confirm they are engaged
   - Assess whether the filing can be submitted on time without escalation

3. **Escalation rule**: Any entity that has lost good standing in its state of formation or
   that has been administratively dissolved must be flagged for immediate review regardless
   of where it falls in the tracking window. Administrative dissolution can create personal
   liability for officers and directors who continue to act on the entity's behalf.

---

### Step 8: Calculate Compliance Cost Estimates

For each obligation in the tracking window, produce a cost estimate:

| Cost Component                    | Source                                          | Notes                                                  |
| --------------------------------- | ----------------------------------------------- | ------------------------------------------------------ |
| State filing fee                  | Current Secretary of State fee schedule         | [VERIFY CURRENT FEE SCHEDULE] — fees change frequently |
| Registered agent service fee      | RA provider invoice or contract                 | May be bundled annually or per-filing                  |
| Professional service fee          | Attorney/paralegal hourly rate × estimated time | Use organization's standard rates                      |
| Franchise tax / entity tax amount | Calculated per jurisdiction rules               | Delaware: calculate both methods; use lower            |
| Penalty and interest accrued      | Per jurisdiction penalty formula                | Apply only to CRITICAL/overdue items                   |

**Aggregate to:** Total by entity; total by jurisdiction; total delinquency costs (CRITICAL
items only, with penalty calculation date noted).

**Important**: Flag all cost estimates with [VERIFY CURRENT FEE SCHEDULE]. State filing fees
change without advance notice, and fee schedules must be verified against the current
Secretary of State website immediately before filing.

---

### Step 9: Generate the Compliance Calendar

Produce the compliance calendar for the tracking window. Structure as:

**Month-by-month view:** All obligations ordered by internal action deadline (not statutory
deadline). For each month, list obligations due that month, grouped by status classification.

**Filtered views on request:** Entity-filtered (all obligations for one entity),
jurisdiction-filtered (all obligations in one state), filing-type-filtered (all annual
reports across all entities), status-filtered (all APPROACHING/URGENT/CRITICAL items).

**Each calendar entry must include:**

- Entity name and legal form
- Filing type (from Category A–G taxonomy)
- Jurisdiction
- Statutory deadline date
- Internal action deadline date
- Current status classification (COMPLIANT / SCHEDULED / APPROACHING / URGENT / CRITICAL / UNKNOWN)
- Responsible owner
- Filing agent (if using registered agent or third-party service)
- Estimated cost [VERIFY CURRENT FEE SCHEDULE]
- Confirmation number and date (if already filed)
- Notes (special requirements, prior-period issues, data needed)

---

### Step 10: Quality Verification

Before delivering any output, run the quality checks:

1. Run the 5 Citation Quality Gates silently. Revise any failures.
2. For every CRITICAL item, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each jurisdiction's deadline and fee information.
4. Verify completeness: confirm every entity in the roster has been assessed in every
   jurisdiction where it is formed or qualified.
5. Check for anti-patterns (see Anti-Patterns section): flag any detected in the portfolio.
6. Generate the Glass Box Audit Trail.

---

### Step 11: Set Review Schedule and Handoff Protocol

Establish a maintenance cadence and document the handoff for ongoing management:

**Review cadence:**

- **Weekly**: Review CRITICAL and URGENT items; confirm completions; add new event-triggered
  obligations
- **Monthly**: Full calendar review; check for state fee or deadline changes; confirm
  registered agent status; update for personnel changes
- **Quarterly**: Review entire entity roster for structural changes (new subsidiaries,
  dissolved entities, M&A activity, new state nexus); reconcile actual filing costs against
  estimates
- **Annually**: Full refresh of all filing obligations and deadlines; audit all confirmation
  numbers against the prior-year obligation list; update for regulatory changes; verify all
  registered agent information against state records

**Handoff checklist for each completed filing:**

- [ ] Filing submitted by internal action deadline
- [ ] Confirmation number or receipt number recorded in compliance record
- [ ] Receipt/acknowledgment PDF saved to entity document repository
- [ ] Good standing certificate obtained if needed for upcoming transactions
- [ ] Compliance calendar updated with next-period obligation (same filing type, next year)
- [ ] Compliance cost recorded in budget tracking

**Event-driven triggers requiring immediate calendar update:**

- New subsidiary formed or acquired → add to entity roster immediately
- Entity dissolved or withdrawn from a state → file dissolution/withdrawal; remove from calendar
- Merger or conversion completed → file merger documents; handle predecessor entity withdrawal
  filings in all foreign states
- Change of registered agent → file change-of-agent form in every affected state
- Address change (principal or registered office) → file address change forms per state
- Any officer/director change → update records per jurisdiction requirements
- FinCEN BOI beneficial ownership change → 30-day update obligation [VERIFY CTA status]
- Business license expiration notice received → initiate renewal immediately

---

## Filing Obligation Reference

### Delaware Franchise Tax Calculation Guide

The Delaware franchise tax is the most commonly miscalculated corporate compliance obligation.
For corporations, two methods exist and the entity may choose the lower:

**Method 1 — Authorized Shares Method:**

- 1–10,000 authorized shares: $175 flat
- 10,001–100,000 authorized shares: $250 flat
- 100,001+ authorized shares: $85 per 10,000 additional shares (or fraction thereof)
- For a corporation with 10,000,000 authorized shares: approximately $85,000+ in tax
- Maximum for non-exempt corporations: $200,000 (large corporate filers: $250,000)

**Method 2 — Assumed Par Value Capital Method (APVC) [almost always lower for startups]:**

1. Compute: Assumed Par Value = (Gross Assets ÷ Issued Shares) × $0.0001 (or actual par if higher)
2. Compute: Assumed Par Value Capital = Issued Shares × Assumed Par Value
3. Compute: Tax = Assumed Par Value Capital × $0.0001 × $400 (rate per $1M or fraction thereof)
4. Minimum tax under APVC: $400

[VERIFY current rate schedule with Delaware Division of Corporations — rates change]

For corporations owing $5,000+ in franchise tax, estimated quarterly payments are required
(40% due June 1, 20% September 1, 20% December 1, balance March 1).

Penalty for failure to file or pay: $200 + 1.5% monthly interest on unpaid tax and penalty.

### Registered Agent Resignation Response Protocol

When a registered agent resigns or gives notice of resignation:

1. **Receive notice** (may be letter to principal office from RA provider or Secretary of State)
2. **Identify replacement agent** immediately — individual resident of the state or licensed
   commercial RA service
3. **File Statement of Change of Registered Agent** with the Secretary of State in the affected
   state — fee typically $25–$50; effective immediately or upon processing
4. **Confirm acceptance** from the new registered agent (most states require written consent)
5. **Update internal records** — entity roster, compliance calendar, registered agent contacts
6. **Verify state records** show the new agent after filing — check Secretary of State portal
   within 5 business days
7. **Timeline**: Complete within 30 days of resignation notice where possible — states vary
   in how long they allow before loss of good standing [VERIFY per state]

### Administrative Dissolution / Reinstatement

**Reinstatement requirements (general pattern — [VERIFY per state]):**

1. Application for reinstatement (state-specific form)
2. All past-due annual report fees and taxes paid in full
3. All penalties and interest paid in full
4. Reinstatement fee paid ($100–$500 depending on state)
5. All delinquent reports filed

**Key reinstatement risks:**

- **Name conflict**: Another entity may have registered the same name during the dissolution
  period; a name change may be required before reinstatement
- **Time limit**: Some states limit reinstatement to 2–5 years after dissolution; entities
  dissolved for longer may need a new formation
- **Retroactive liability**: The entity may still owe obligations incurred during the
  dissolution period; reinstatement does not erase liability
- **Contract voidability**: In some jurisdictions, contracts entered into by a dissolved
  entity may be voidable by the counterparty [VERIFY per jurisdiction]

---

## Compliance Status Classification

The six-tier status system replaces the simple RED/YELLOW/GREEN model. Entity compliance
has distinct failure modes (substantive delinquency vs. procedural urgency) and a meaningful
distinction between confirmed compliance and assumed compliance.

### COMPLIANT (Blue)

**Definition**: Filing confirmed complete with confirmation number for the current period;
good standing verified; no outstanding obligations within the tracking window.

**Criteria:**

- Confirmation number or official receipt on file
- Receipt/acknowledgment document saved to entity records
- Good standing confirmed (certificate obtained or verified via state portal within 90 days)
- Next-period obligation entered in compliance calendar

**Required action**: None for this obligation. Maintain monitoring cadence.

### SCHEDULED (Green)

**Definition**: Filing obligation exists and is calendared; statutory deadline is 90+ days
away; no action required yet; entity is believed to be in good standing.

**Criteria:**

- Filing obligation identified and calendar entry created
- Internal action deadline is 30+ days in the future
- Prior-period filing confirmed complete (confirmation number on file)
- No known compliance issues or outstanding deficiencies

**Required action**: None. Monitor on standard weekly cadence.

### APPROACHING (Yellow)

**Definition**: Filing obligation is within the preparation window (60–90 days to statutory
deadline, or internal action deadline within 30 days). Preparation should be initiated.

**Criteria:**

- Statutory deadline within 90 calendar days, OR internal action deadline within 30 days
- Required data not yet collected (shares, officers, gross assets, officer roster update, etc.)
- Responsible owner not yet engaged on this specific filing

**Required action**: Engage responsible owner; begin data collection; initiate filing
preparation. For complex filings (UK accounts, franchise tax calculation), begin immediately.

### URGENT (Orange)

**Definition**: Internal action deadline has passed but statutory deadline has not. Filing
must be initiated immediately to avoid delinquency. Risk of missing statutory deadline is
real and requires escalation.

**Criteria:**

- Internal action deadline has passed (no confirmation number on file)
- Statutory deadline within 30 days or less
- Filing not yet in progress

**Required action**: Initiate filing immediately. Assess whether expedited processing is
available (many states offer same-day to 2-day expedited processing for an additional fee).
Escalate to supervisor if responsible owner has not acted within 24 hours.

### CRITICAL (Red)

**Definition**: Statutory deadline has passed and filing has not been confirmed. Entity is
delinquent. Penalties are accruing or have accrued. Good standing may be lost.

**Criteria:**

- Statutory deadline is past (today's date exceeds statutory deadline)
- No confirmation number or receipt on file for the current period
- Penalty and interest calculation required

**Required action**:

1. Calculate accrued penalty and interest
2. Determine whether late filing is accepted (most states accept late filings with penalty;
   some require reinstatement applications if dissolution has been initiated)
3. File immediately, even late, to stop penalty accrual
4. Verify good standing status — if lost, obtain reinstatement concurrently
5. Escalate to senior counsel if administrative dissolution has been initiated
6. Document all actions taken and remediation steps in compliance record

### UNKNOWN (Gray)

**Definition**: Compliance status cannot be determined due to missing data or inability to
verify prior-period filings. Treated with urgency equivalent to URGENT until resolved.

**Criteria:**
Any of the following are true:

- Formation date is missing (prevents anniversary-based deadline calculation)
- Registered agent status unconfirmed (cannot verify good standing)
- EIN or registration number is missing (cannot verify state records)
- Prior-period filing status unconfirmed (no confirmation number and no state records check)
- Entity recently acquired and compliance records not yet reviewed or transferred

**Required action**: Gather missing data as highest priority. In parallel, search state
records for the entity's current good standing status (most Secretaries of State provide
online good standing verification). If state records show delinquency or dissolution, treat
as CRITICAL immediately.

**Status Transition Logic:**

```
COMPLIANT  →  SCHEDULED   [when a new period's obligation enters the calendar]
SCHEDULED  →  APPROACHING [when the 90-day threshold is crossed]
APPROACHING →  URGENT     [when the internal action deadline passes without filing]
URGENT     →  CRITICAL    [when the statutory deadline passes without filing]
CRITICAL   →  COMPLIANT   [when reinstatement or late filing is confirmed with confirmation number]
UNKNOWN    →  any status  [when sufficient data is gathered to assign a definitive status]
```

---

## Prioritization Framework

When multiple obligations require attention simultaneously, prioritize using this framework:

### Priority 1 — Formation State / Existential Risk

Address first: any CRITICAL or URGENT obligation in the entity's state of formation. Loss
of good standing in the formation state is the most severe outcome — it affects the entity's
legal existence and cascades to all foreign jurisdictions.

Equally high priority: any entity in administrative dissolution proceedings, or any entity
that has lost a registered agent in its formation state.

### Priority 2 — Revenue-Critical State Operations

Address second: any CRITICAL or URGENT obligation in a state where the entity has substantial
revenue, employees, or operations. Losing the right to transact business in an operating
state can directly impair business operations.

Also in this tier: California suspension by the FTB (contracts unenforceable in CA courts)
and any state where a government contract or professional license requires current good
standing.

### Priority 3 — Foreign Qualification States

Address third: CRITICAL and URGENT obligations in all other foreign-qualified states.

### Priority 4 — APPROACHING Items by Deadline Proximity

Within APPROACHING items, prioritize by days remaining to internal action deadline. Lead
with items requiring the most preparation time (UK annual accounts, complex franchise tax
calculations) over simple online filings.

### Priority 5 — SCHEDULED Items

Monitor on standard cadence. No immediate action required, but verify data collection
deadlines have been calendared.

### Cost-Impact Tiers for Delinquency

| Tier   | Characterization                                                                               | Typical Consequence                                                                             | Urgency                     |
| ------ | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------- |
| Tier A | Formation state delinquency; administrative dissolution; registered agent resignation          | Loss of legal existence; personal liability exposure; contracts voidable                        | Immediate — within 24 hours |
| Tier B | Major operating state delinquency; California FTB suspension; UK Companies House late accounts | Loss of right to transact business; contract unenforceability; director personal liability (UK) | Same week                   |
| Tier C | Foreign qualification state delinquency; business license expiration                           | Cannot sue in that state; accumulated penalties; operational disruption                         | Within 2 weeks              |
| Tier D | Officer/director record staleness; DBA expiration; good standing certificate expired           | Third-party reliance issues; banking complications; due diligence complications                 | This quarter                |

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                | Fail Action                                             |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Source**     | Every deadline, fee amount, and penalty calculation cites the specific jurisdiction's current official source                       | Mark "[VERIFY CURRENT — [STATE] SOS website]"           |
| **Format**     | All deadlines expressed as specific calendar dates (not "30 days after fiscal year end") and verified for the current filing period | Recalculate as specific dates                           |
| **Currency**   | Every fee amount and deadline noted as potentially stale; instructions to verify against current SOS website                        | Flag "[VERIFY CURRENT FEE SCHEDULE — may have changed]" |
| **Domain**     | Analysis for each jurisdiction draws only on that jurisdiction's rules; no assumption that another state's pattern applies          | Remove or flag cross-jurisdiction assumptions           |
| **Confidence** | Uncertainty explicitly stated for any jurisdiction-specific detail derived from memory rather than live research                    | Add confidence qualifier and [VERIFY] tag               |

---

## Self-Interrogation for CRITICAL Items

For any filing obligation classified as CRITICAL, apply this 3-pass review before delivering:

**Pass 1 — Deadline Integrity**:

- Is the statutory deadline calculation correct for this entity type, this state, and
  the current filing year?
- Does the deadline pattern (fixed date / anniversary / fiscal year) apply correctly?
- Has a holiday or weekend adjustment been considered?

**Pass 2 — Consequence Completeness**:

- Have all consequences of this specific delinquency been assessed (penalty amount, good
  standing impact, dissolution timeline, officer liability risk)?
- Is this jurisdiction one where dissolution has already been initiated, or only where
  penalty fees are accumulating?

**Pass 3 — Challenge**:

- Is there any basis on which the statutory deadline may have been extended (natural disaster
  relief, regulatory guidance, judicial order)?
- Is there a cure period during which a late filing avoids the worst consequences?
- Does the CRITICAL classification overstate urgency for this specific jurisdiction's
  enforcement pattern?

If any pass reveals an error or overstatement, revise before delivery.

---

## Confidence Scoring

Apply a confidence level to each jurisdiction's deadline and fee information included in the
output. The primary source of error in entity compliance tracking is stale or misremembered
deadline and fee information.

| Level        | Range     | Meaning                                                                         | Action                                                                   |
| ------------ | --------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Definite** | 0.95–1.0  | Verified against primary source within this session                             | State with confidence; note verification source                          |
| **High**     | 0.80–0.94 | Well-established rule with low rate of change (e.g., Delaware March 1 deadline) | State with brief note to verify fee amount                               |
| **Probable** | 0.60–0.79 | General rule that varies by entity type or has been subject to recent change    | State with explicit caveat and [VERIFY] tag                              |
| **Possible** | 0.40–0.59 | Jurisdiction details from general knowledge; meaningful uncertainty             | Flag for verification before relying; provide both possible alternatives |
| **Unlikely** | 0.0–0.39  | Jurisdiction not well-known or detail not reliably remembered                   | Do not assert; flag "[UNKNOWN — research required]"                      |

**Default rule**: Treat all fee amounts as Probable confidence (0.60–0.79) unless verified
against a live source in this session. Fee schedules change annually in many states.

---

## Glass Box Audit Trail

Every entity compliance tracker output MUST include this Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-entity-compliance-tracker"
  run_date: "[DATE]"
  tracking_window: "[START DATE] to [END DATE]"
  engagement_mode: "[Full Portfolio Audit / Calendar Generation / Overdue Triage / etc.]"
  portfolio_summary:
    entities_assessed: "[number]"
    jurisdictions_covered: "[number]"
    total_obligations_mapped: "[number]"
  status_breakdown:
    compliant: "[number]"
    scheduled: "[number]"
    approaching: "[number]"
    urgent: "[number]"
    critical: "[number]"
    unknown: "[number]"
  data_quality:
    entities_with_confirmed_formation_date: "[number / total]"
    entities_with_confirmed_registered_agent: "[number / total]"
    entities_with_confirmed_prior_filing: "[number / total]"
    entities_with_unknown_foreign_qualification_states: "[number]"
  legalcode_mcp: "Connected / Not connected"
  external_verification_performed: "[Yes — [method] / No — all deadlines and fees require verification]"
  fee_schedule_verification: "[Verified against [source] on [date] / Not verified — [VERIFY CURRENT FEE SCHEDULE] applies to all fee amounts]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  anti_patterns_detected: "[List any detected from the portfolio, or 'None identified']"
  limitations:
    - "[Any scope limitations: e.g., 'Foreign qualification states not confirmed for 3 entities']"
    - "[Any data gaps: e.g., 'Delaware franchise tax calculation awaiting gross assets figure']"
    - "[Any jurisdictions not covered: e.g., 'International entities outside US, UK, AU, CA not assessed']"
  disclaimer: "This output requires verification of all deadlines and fees against current official sources before acting. Not legal advice."
  reviewer: "AI-assisted — requires review by qualified legal counsel or registered agent service"
```

---

## Anti-Patterns

The following 18 anti-patterns represent the most common causes of entity compliance failure.
Actively check for each during every engagement and flag when detected.

**AP-01: Tracking Only the Formation State**
Tracking Delaware compliance while ignoring California, Texas, New York, and all other foreign
qualification states where the entity actually operates. Annual reports and taxes are typically
owed in every state where the entity holds a certificate of authority — often 10–30 states
for a mid-size company. Detection: ask how many states the entity is registered to do business
in; if less than the number of states where it has employees or offices, flag the gap.

**AP-02: Confusing Annual Report and Franchise Tax as One Obligation**
In many states (including Delaware), the annual report and franchise tax are separate obligations
with separate filing mechanics, deadlines, and payments — even when they appear on the same
website. Delaware corporations: annual report (Division of Corporations) and franchise tax
are submitted together but the LLC annual tax is an entirely separate portal with a different
June 1 deadline. Always treat these as distinct line items in the compliance calendar.

**AP-03: Relying on State Reminder Notices**
States send reminders to the registered agent's address on file — not to the company's
principal office. If the registered agent has changed without a filed change-of-agent form,
or if the RA's address is outdated, the company may receive no reminders at all. Compliance
tracking must be calendar-based, not notice-based. Never assume a missing reminder means
there is no obligation.

**AP-04: Treating Good Standing as a Single Global Status**
Good standing is jurisdiction-specific and is evaluated independently in every state.
An entity can be in good standing in Delaware but simultaneously suspended by the California
FTB for unpaid minimum franchise tax. Good standing must be tracked per entity per
jurisdiction. Never represent an entity as "in good standing" globally without jurisdiction-
by-jurisdiction confirmation.

**AP-05: Confusing Annual and Biennial Filing Obligations**
Many states require biennial (every two years) rather than annual reports. Treating all
reports as annual generates unnecessary filings in biennial states and, more dangerously,
can cause a biennial obligation to be missed in the off year if the system erroneously shows
it as having been "filed" in year one. Always confirm whether an obligation is annual or
biennial before scheduling.

**AP-06: Using Fiscal Year End as a Proxy for Annual Report Deadlines**
Most state annual reports are due on a fixed calendar date or an anniversary date — not on
the entity's fiscal year end. Using fiscal year end as a proxy will systematically create
wrong deadlines for most states. Always use the state-specific deadline pattern.

**AP-07: Missing the Delaware Authorized Shares Method Trap**
Filing Delaware franchise tax using the Authorized Shares Method for a startup with 10M+
authorized shares and generating a $50,000–$100,000+ tax bill instead of calculating the
Assumed Par Value Capital Method (which typically yields $400–$5,000 for the same company).
The Delaware Division of Corporations sends initial bills using the Authorized Shares Method;
the company must request and calculate the APVC method to obtain the correct (usually far
lower) amount. Failure to catch this costs thousands of dollars per year.

**AP-08: Not Tracking California as a Dual-Track Obligation**
California requires both a Secretary of State Statement of Information (SOS track) and a
Franchise Tax Board minimum annual tax of $800 (FTB track). Suspension can occur from either
agency independently. A company that files the SOI but fails to pay FTB can be suspended by
FTB. A company that pays FTB but fails to file the SOI can be suspended by SOS. Both tracks
must be tracked separately with separate responsible owners and confirmation processes.

**AP-09: Missing the FinCEN BOI 30-Day Update Obligation**
Beneficial ownership changes must be reported to FinCEN within 30 days of the change. This
is an event-driven obligation (not calendar-based) and many compliance systems predating the
Corporate Transparency Act (effective January 1, 2024 for most entities) lack an alert
mechanism for it. Ensure every officer/director/owner change triggers a BOI update review.
[VERIFY: CTA enforcement status requires current verification — has been subject to
regulatory and judicial developments since 2024]

**AP-10: Annual Report Filed Without Officer/Director Verification**
Many states require the annual report to reflect current officer and director information. A
report filed without updating for officer/director changes creates false official records and
may constitute an independent violation in some states. Before every annual report, explicitly
confirm the officer/director roster is current.

**AP-11: Treating Dissolved or Merged Entities as Still Requiring Compliance**
When an entity merges into another entity or is dissolved, compliance obligations transfer
to the surviving entity or terminate. Predecessor entities do not require annual reports
after the effective date of dissolution or merger — but they do require dissolution/withdrawal
filings in all foreign qualification states. Continuing to track and file for a non-existent
entity wastes resources; failing to file withdrawals in foreign states can create ongoing
penalty accrual.

**AP-12: Registered Agent Fee Delinquency as a Compliance Oversight**
Registered agent fees are vendor payments, not state filing obligations. However, failure
to pay RA fees results in the agent resigning, which triggers a state filing obligation
(change of agent) within 30–60 days and, if unfulfilled, loss of good standing. Track RA
fee payment separately from state filing obligations but treat RA fee delinquency as an
elevated risk requiring prompt resolution.

**AP-13: Not Maintaining Formation Documents**
The original certificate of incorporation/formation, all amendments, certificates of
authority, and registered agent designations are the evidentiary foundation of the entity's
legal existence. Many M&A delays, bank account difficulties, and government contract problems
trace to an entity's inability to produce its formation documents. Formation document
maintenance is a compliance function. The compliance tracker must include a formation
document checklist and flag any entity missing core documents.

**AP-14: Skipping Compliance Diligence During M&A**
When a company is acquired, the acquirer inherits all compliance obligations, including
historical delinquencies, unknown administrative dissolutions, and lapsed foreign
qualifications. Failure to conduct entity compliance diligence pre-closing creates
unquantified risk: unknown penalties, unknown loss of good standing, unknown dissolved
subsidiaries. Entity compliance audit is a required element of any acquisition due diligence
program. Always onboard acquired entities into the compliance calendar as a post-closing
priority.

**AP-15: Conflating Registered Office Address and Principal Office Address**
The registered office (the address on file with the Secretary of State, typically the
registered agent's physical address) and the company's principal place of business are
separate legal concepts, often separately maintained in state records. A change of principal
business address does not automatically update the registered office on file with the state,
and vice versa. Both addresses must be tracked and updated independently through separate
filings when they change.

**AP-16: Assuming Universal Annual Report Requirements**
Not all states require annual reports or franchise taxes from all entity types. Ohio
historically required no annual report from LLCs (note: Ohio filing requirements have
evolved — [VERIFY]). New Mexico traditionally has not required annual reports for LLCs
[VERIFY]. Washington frames its annual business report as a business license renewal within
a different regulatory framework. Applying a universal assumption that every state requires
an annual report from every entity type will generate phantom obligations in some states
and miss real obligations framed differently in others.

**AP-17: Ordering Good Standing Certificates Too Late**
Good standing certificates are needed at closing of M&A transactions, bank account openings,
and government contract awards. Standard processing in most states is 3–7 business days;
expedited options may be same-day but at significant cost. Ordering a certificate with less
than 5 business days before it is needed is insufficient in most states. Order good standing
certificates at least 30 days before they are needed for any significant transaction.

**AP-18: Single-Owner Compliance Tracking Without Backup**
If the only person who knows the compliance calendar is a single paralegal, associate, or
compliance officer, personnel changes (turnover, illness, leave of absence) create a
complete gap in compliance tracking. Every entity compliance program must have at minimum
a primary owner, a named secondary owner, and a defined escalation path to senior counsel.
The skill must prompt for secondary owner assignment and flag any obligation with no named
backup as an organizational risk.

---

## Writing Standards

Apply plain-language discipline to all output:

**For compliance reports and dashboards:**

- Plain language. No unnecessary legal jargon.
- Active voice: "File the annual report by March 1" not "The annual report is required to be
  filed by March 1 pursuant to..."
- Short sentences. One instruction per sentence.
- Specific dates, not general time windows: "March 1, 2027" not "early next year"
- Name the actor: "Legal team must..." not "It is required that..."
- Concrete cost figures with verification flags: "$50 filing fee [VERIFY CURRENT FEE SCHEDULE]"

**For action lists:**

- Verb-first imperatives: "File," "Obtain," "Update," "Confirm," "Escalate"
- Owner named explicitly for every action item
- Deadline stated as a specific date for every action item
- Next step stated for every CRITICAL and URGENT item, not just the item itself

**Quality gates before delivery:**

1. Can a non-lawyer business stakeholder understand the status dashboard?
2. Can the paralegal responsible for a specific filing understand exactly what to do
   and by when from the action list?
3. Is every deadline stated as a specific calendar date (not a relative reference)?
4. Is every fee amount flagged with [VERIFY CURRENT FEE SCHEDULE]?
5. Are all CRITICAL items listed first in the output?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 3 (mapping filing obligations), search for current statutory requirements for
  each jurisdiction in the portfolio
- Verify current fee schedules and penalty structures against the legalcode-mcp database
- Search for recent legislative or regulatory changes affecting filing requirements
- For CRITICAL items, search for jurisdiction-specific reinstatement procedures and timelines
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Remove the [VERIFY] and [VERIFY CURRENT FEE SCHEDULE] tags where verification has been
  completed via legalcode-mcp

**Without legalcode-mcp:**

- Proceed using the jurisdiction-specific information in this skill's Filing Obligation
  Reference section and the research frameworks above
- Mark every deadline and fee amount with [VERIFY CURRENT FEE SCHEDULE]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — all deadlines and fees
require independent verification against current state SOS and taxing authority websites"`
- Recommend that the user verify critical deadlines directly with their registered agent or
  at the relevant Secretary of State website before filing

**Recommended state verification sources (without legalcode-mcp):**

| Jurisdiction     | Primary Source                   | Verification URL Pattern                                |
| ---------------- | -------------------------------- | ------------------------------------------------------- |
| Delaware         | Division of Corporations         | corp.delaware.gov                                       |
| California       | Secretary of State + FTB         | sos.ca.gov / ftb.ca.gov                                 |
| Florida          | Division of Corporations         | dos.fl.gov/sunbiz                                       |
| New York         | Division of Corporations         | dos.ny.gov                                              |
| Texas            | Secretary of State + Comptroller | sos.state.tx.us / comptroller.texas.gov/taxes/franchise |
| Wyoming          | Secretary of State               | sos.wyo.gov                                             |
| Nevada           | Secretary of State               | sos.nv.gov                                              |
| UK               | Companies House                  | companieshouse.gov.uk                                   |
| Australia        | ASIC                             | asic.gov.au                                             |
| Canada (federal) | Corporations Canada              | ised-isde.canada.ca                                     |

[These URLs are directional only — verify currency at time of use]

---

## Output Format Template

### Template A: Compliance Status Dashboard (Executive)

```
ENTITY COMPLIANCE PORTFOLIO STATUS
Generated: [DATE]
Tracking Window: [START DATE] to [END DATE]
Portfolio: [N] entities | [N] jurisdictions | [N] total obligations tracked

═══════════════════════════════════════════════════════
STATUS SUMMARY
═══════════════════════════════════════════════════════

  COMPLIANT   [N]  — No action required
  SCHEDULED   [N]  — No action required yet
  APPROACHING [N]  — Initiate preparation
  URGENT      [N]  — Action required this week
  CRITICAL    [N]  — Delinquent; immediate action
  UNKNOWN     [N]  — Data gaps; verification needed

ESTIMATED COMPLIANCE COSTS — TRACKING WINDOW
  Filing fees:                $[X]    [VERIFY CURRENT FEE SCHEDULE]
  Registered agent fees:      $[X]
  Estimated professional time:$[X]
  Delinquency penalties:      $[X]    [if CRITICAL items present]
  TOTAL ESTIMATED:            $[X]

═══════════════════════════════════════════════════════
IMMEDIATE ATTENTION REQUIRED
═══════════════════════════════════════════════════════

CRITICAL — [N] OVERDUE FILING(S) REQUIRING IMMEDIATE ACTION

  [Entity Name] ([Entity Type]) | [Formation State]
  Filing:            [Filing Type]
  Jurisdiction:      [State/Country]
  Deadline:          [DATE] ([N] days overdue)
  Penalty Accrued:   $[X] + [rate]% interest per month [VERIFY]
  Good Standing:     [Confirmed / At Risk / Lost]
  Action Required:   [Specific step — e.g., "File late annual report via [State] SOS online
                     portal; pay $[X] filing fee + $[X] penalty; obtain confirmation number"]
  Owner:             [Name] | [Email]

URGENT — [N] FILING(S) PAST INTERNAL DEADLINE

  [Entity Name] | [Jurisdiction]
  Filing:            [Filing Type]
  Statutory Deadline:[DATE] ([N] days remaining)
  Internal Deadline: [DATE] ([N] days past internal deadline)
  Action Required:   Initiate filing immediately; consider expedited processing
  Owner:             [Name] | [Email]

UNKNOWN — [N] ENTITIES WITH UNVERIFIED STATUS

  [Entity Name] | [Jurisdiction]
  Missing Data:      [List specific missing fields]
  Action Required:   Obtain [registered agent confirmation / formation documents / EIN /
                     prior filing receipts] by [DATE]
  Owner:             [Name] | [Email]

═══════════════════════════════════════════════════════
UPCOMING OBLIGATIONS
═══════════════════════════════════════════════════════

NEXT 30 DAYS

| Entity | Jurisdiction | Filing Type | Statutory Deadline | Internal Deadline | Status | Owner |
|--------|-------------|-------------|-------------------|-------------------|--------|-------|
| [Name] | [State]     | [Type]      | [DATE]            | [DATE]            | APPROACHING | [Name] |

31–60 DAYS

| Entity | Jurisdiction | Filing Type | Statutory Deadline | Internal Deadline | Status | Owner |
|--------|-------------|-------------|-------------------|-------------------|--------|-------|

61–90 DAYS

| Entity | Jurisdiction | Filing Type | Statutory Deadline | Internal Deadline | Status | Owner |
|--------|-------------|-------------|-------------------|-------------------|--------|-------|
```

---

### Template B: Full Compliance Calendar (Operational)

```
COMPLIANCE CALENDAR — [ENTITY NAME or "ALL ENTITIES"]
Period: [MONTH YEAR] to [MONTH YEAR]
Generated: [DATE]
All internal action deadlines shown; statutory deadlines in parentheses.

═══════════════════════════════════════════════════════
[MONTH YEAR]
═══════════════════════════════════════════════════════

[STATUS] [Filing Type]
Entity:             [Legal Name] ([Entity Type])
Jurisdiction:       [State/Country]
Internal Deadline:  [DATE]  ← ACT BY THIS DATE
Statutory Deadline: [DATE]
Responsible Owner:  [Name] | [Email]
Filing Agent:       [RA Provider / In-house / TBD]
Required Data:      [Officer list / Gross assets / Nature of business / etc.]
Est. Cost:          $[X] filing fee + $[X] RA fee = $[X] total [VERIFY CURRENT FEE SCHEDULE]
Confirmation #:     [PENDING / XXXXXXXXXX]
Notes:              [Any special instructions]

────────────────────────────────────────────────────────

[NEXT MONTH YEAR]

  ...

═══════════════════════════════════════════════════════
ANNUAL SUMMARY — COST BY ENTITY
═══════════════════════════════════════════════════════

| Entity | Formation State | # Obligations | Total Est. Cost | # Critical | # Urgent |
|--------|----------------|---------------|-----------------|-----------|---------|
| [Name] | Delaware       | [N]           | $[X]            | [N]       | [N]     |

═══════════════════════════════════════════════════════
ANNUAL SUMMARY — COST BY JURISDICTION
═══════════════════════════════════════════════════════

| Jurisdiction | # Entities | # Obligations | Total Filing Fees | Total RA Fees | Total Est. |
|-------------|-----------|---------------|------------------|--------------|------------|
| Delaware    | [N]       | [N]           | $[X]             | $[X]         | $[X]       |
```

---

### Template C: Entity-Level Compliance Report

```
ENTITY COMPLIANCE REPORT
Entity:      [Legal Name]
Type:        [Entity Type]
Report Date: [DATE]

═══════════════════════════════════════════════════════
ENTITY IDENTITY
═══════════════════════════════════════════════════════

Legal Name (registered):  [Exact name on file]
Trade Names / DBAs:       [List or "None"]
Entity Type:              [Type]
Formation Jurisdiction:   [State/Country]
Formation Date:           [DATE]
Fiscal Year End:          [MM-DD]
EIN / Tax ID:             [XXX-XXXXXXX or "MISSING — obtain immediately"]
Company Reg. No.:         [If applicable]
Nature of Business:       [Description]
Current Status:           [Active / Dissolved / Suspended / Unknown]
Primary Owner:            [Name] | [Email]
Secondary Owner:          [Name] | [Email] | "NONE — ASSIGN IMMEDIATELY"
Last Record Review:       [DATE]

FORMATION DOCUMENTS CHECKLIST
  [ ] Certificate of Incorporation/Formation (original or certified copy)
  [ ] IRS EIN Confirmation Letter (SS-4 response)
  [ ] All Amendments to Formation Documents
  [ ] Operating Agreement / Bylaws / Partnership Agreement
  [ ] Initial Board/Member Resolutions
  [ ] Certificate(s) of Authority — all foreign qualification states
  [ ] Current Registered Agent Designations on File — all states
  [ ] Prior-Year Annual Report Confirmations (at minimum, last 3 years)

═══════════════════════════════════════════════════════
REGISTERED AGENTS ON FILE
═══════════════════════════════════════════════════════

| Jurisdiction | Agent Name | Agent Address | Fee Status | Last Confirmed |
|-------------|-----------|---------------|-----------|----------------|
| [State]     | [Name]    | [Address]     | Current   | [DATE]         |

═══════════════════════════════════════════════════════
GOOD STANDING STATUS
═══════════════════════════════════════════════════════

| Jurisdiction | Status | Last Verified | Certificate Date | Notes |
|-------------|--------|--------------|-----------------|-------|
| Delaware    | [STATUS] | [DATE]     | [DATE or N/A]   | [Notes] |

═══════════════════════════════════════════════════════
FILING OBLIGATION REGISTER
═══════════════════════════════════════════════════════

| Filing Type | Jurisdiction | Freq. | Statutory Deadline | Internal Deadline | Status | Est. Cost | Confirmation # |
|-------------|-------------|-------|-------------------|-------------------|--------|-----------|----------------|
| Annual Report + Franchise Tax | Delaware | Annual | [DATE] | [DATE] | [STATUS] | $[X] [VERIFY] | [# or PENDING] |
| Statement of Information | California | Biennial | [DATE] | [DATE] | [STATUS] | $25 [VERIFY] | [# or PENDING] |
| Confirmation Statement | UK CH | Annual | [DATE] | [DATE] | [STATUS] | £50 [VERIFY] | [# or PENDING] |
...

═══════════════════════════════════════════════════════
REQUIRED ACTIONS
═══════════════════════════════════════════════════════

IMMEDIATE (CRITICAL / URGENT):
  1. [Specific action] — Owner: [Name] — By: [DATE]

THIS MONTH (APPROACHING — within 30 days of internal deadline):
  1. [Specific action] — Owner: [Name] — By: [DATE]

THIS QUARTER (APPROACHING — 30–90 days):
  1. [Specific action] — Owner: [Name] — By: [DATE]

═══════════════════════════════════════════════════════
ANTI-PATTERNS DETECTED
═══════════════════════════════════════════════════════

[List any anti-patterns identified in this entity's compliance record, or "None identified."]

═══════════════════════════════════════════════════════
NOTES AND SPECIAL CONSIDERATIONS
═══════════════════════════════════════════════════════

[Entity-specific notes: pending mergers, acquisition integration, unusual jurisdictions,
outstanding penalties under negotiation, registered agent transitions in progress, etc.]

═══════════════════════════════════════════════════════
DISCLAIMER
═══════════════════════════════════════════════════════

This report is generated by an AI-assisted skill and does not constitute legal advice. All
filing deadlines, fee amounts [VERIFY CURRENT FEE SCHEDULE], and statutory requirements
must be verified against current Secretary of State and regulatory authority publications
before acting. Statutory requirements change; verify current applicability. This report
does not replace engagement of qualified legal counsel or a licensed registered agent service.
```

---

## Localization Notes

When tracking entities outside the primary US/UK/AU/CA framework covered in this skill:

1. Identify the equivalent of the "Secretary of State" in the target jurisdiction (e.g.,
   Registrar of Companies in India, Chamber of Commerce in Netherlands, Handelsregister
   in Germany, Registre de Commerce in France)

2. Identify the equivalent annual/periodic filing obligation and its deadline pattern

3. Identify the equivalent of the "registered agent" requirement (some jurisdictions use
   a local representative concept, others require a local director or nominee)

4. Identify whether officer/director changes require immediate regulatory notification
   or are captured in the periodic report

5. Identify the equivalent of the "good standing certificate" and what authority issues it

6. Flag all obligations for jurisdictions not covered by this skill with [VERIFY — local
   counsel review required] rather than applying assumptions from better-known jurisdictions

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- Deep web research on US Secretary of State requirements across all 50 states, with detailed
  coverage of Delaware, California, Florida, Texas, New York, Wyoming, and Nevada
- UK Companies House filing requirements and penalty structures
- Australian ASIC annual review framework
- Canadian federal (CBCA) and Ontario entity compliance requirements
- Delaware franchise tax calculation methodology (Authorized Shares Method vs. APVC Method)
- CT Corporation / Wolters Kluwer, CSC, Harbor Compliance, and Cogency Global entity
  management platform research for best-practice workflow patterns
- CLOC and ACC entity management guidance
- Legalcode reference standard methodology (legalcode-contract-review architecture)
- FinCEN Corporate Transparency Act BOI reporting requirements [VERIFY current status]
- Research on administrative dissolution and reinstatement procedures, registered agent
  resignation response protocols, and multi-entity compliance portfolio management patterns

This skill is jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers and should be
validated against current state SOS and taxing authority sources before use in any
specific engagement. Laws and fee schedules change; verify before filing.
