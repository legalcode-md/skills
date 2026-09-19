---
name: legalcode-estate-plan-generator
description: 'Generates a complete US estate planning document suite: revocable living trust, pour-over
  will, durable financial power of attorney, advance healthcare directive, HIPAA authorization, and asset
  transfer documents (beneficiary designations, TOD deeds, account retitling checklists). Use when clients
  need a full estate plan built from scratch, want to review or update an existing plan, need a trust
  funding checklist, are planning for incapacity or healthcare directives, have estate tax exposure above
  the BEA threshold, have a beneficiary with special needs, or are planning for 2026 exemption cliff.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Generates a complete US estate planning document suite: revocable living trust, pour-over will, durable financial power of attorney, advance healthcare directive, HIPAA authorization, and asset transfer documents (beneficiary designations, TOD deeds, account retitling checklists). Covers federal estate tax planning (IRC §2001, §2010, §2056, §2601), portability elections (IRC §2010(c)(5), Rev. Proc. 2022-32), special needs trusts (42 U.S.C. §1396p), SECURE Act 2.0 inherited IRA rules, and 2026 TCJA sunset planning. Use when clients need a full estate plan built from scratch, want to review or update an existing plan, need a trust funding checklist, are planning for incapacity or healthcare directives, have estate tax exposure above the BEA threshold, have a beneficiary with special needs, or are planning for 2026 exemption cliff. Also triggers for: living trust drafting, pour-over will, healthcare proxy, durable POA, advance directive, HIPAA release, beneficiary designations, trust funding, estate tax analysis, portability, DSUE, dynasty trust, SNT, ABLE account planning.


# Legalcode Estate Plan Generator

> **Disclaimer**: This skill provides a framework for AI-assisted estate planning document
> generation and analysis. It does not constitute legal advice. All outputs must be reviewed
> and executed under the supervision of a qualified estate planning attorney licensed in the
> relevant state(s) before use. Estate planning documents have jurisdiction-specific execution
> formalities — a will executed without proper witnesses or notarization may be void.
> Tax analysis is based on law current as of 2025 and the anticipated 2026 TCJA sunset;
> verify current exemption amounts and rates before relying on any tax provision. Statutory
> and case law references cited from research carry hallucination risk — verify against
> authoritative sources before relying on them.

---

## Purpose and Scope

This skill generates, reviews, and analyzes the complete estate planning document suite for
US clients. It covers both document drafting and strategic planning across the full estate
planning lifecycle.

**Generates and analyzes:**

- Revocable Living Trust (RLT) — primary probate-avoidance and incapacity-management vehicle
- Pour-Over Will — safety net to capture unfunded assets and direct minor guardianship
- Durable Financial Power of Attorney (DPOA) — lifetime financial management during incapacity
- Advance Healthcare Directive (AHCD) — medical decisions, life-sustaining treatment, agent
- HIPAA Authorization — healthcare information disclosure for agent and family
- Asset Transfer Documents — beneficiary designation review, TOD deeds, account retitling,
  trust funding checklist
- Federal estate tax analysis — BEA utilization, portability, marital deduction, GST
- Special needs trust (SNT) analysis — first-party, third-party, pooled variants
- 2026 TCJA sunset planning — strategies to lock in current elevated exemptions

**Does not:**

- Replace an estate planning attorney or provide legal advice
- Generate final execution-ready documents without attorney review
- Cover non-US estate planning (see jurisdiction-specific skills for UK, EU, AU)
- Handle complex business succession (use a business-specific skill for FLP/LLC/buy-sell)
- Provide Medicaid spend-down advice (refer to certified elder law attorney for Medicaid planning)

---

## Jurisdiction and Governing Law

This skill is **US-specific** (federal law) with state-level adaptation markers.

Federal law governs the tax framework (IRC Title 26, 26 U.S.C.). State law governs:

- Will execution formalities (witness and notarization requirements)
- Trust validity and administration (UTC adopted in ~36 states [VERIFY current count])
- Power of attorney formalities (UPOAA adopted in ~30 states [VERIFY current count])
- Healthcare directive requirements (UHCDA adopted in ~13 states [VERIFY current count])
- Community property rules (AZ, CA, ID, LA, NM, NV, TX, WA, WI)
- Transfer-on-death deed availability (~30 states [VERIFY])
- State estate and inheritance taxes (17 states plus DC as of 2025 [VERIFY])

[JURISDICTION-SPECIFIC] For every state, verify and apply:

- Will execution: number of witnesses required, notarization, holographic will recognition
- Trust registration requirements (some states require recording or registration)
- DPOA "hot powers" list requiring express authorization under state UPOAA enactment
- AHCD execution: witnesses vs. notary, prohibited witnesses (healthcare providers, beneficiaries)
- State estate tax exemption and rate (many states have cliffs far below the federal BEA)
- Community property treatment and impact on step-up in basis (IRC §1014)
- Medicaid estate recovery rules (affects trust design for older clients)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
client facts, the workflow pauses and asks when:

- The answer would change which documents are needed or how they are structured
- Tax exposure changes the strategic approach (e.g., above vs. below the BEA cliff)
- Family circumstances create structural forks (minor children, special needs beneficiary,
  blended family, non-citizen spouse, business interests)
- State-specific rules require local verification before proceeding

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

### Step 1: Accept Client Information

Accept client information in any of these formats:

- **Intake questionnaire**: Completed estate planning intake form (PDF, DOCX, or text)
- **Prior estate plan**: Existing documents for review and update
- **Pasted facts**: Client facts pasted directly into the conversation
- **Dictated summary**: Attorney or paralegal narrative of client situation

If no client information is provided, begin the Intake Interview (Step 2).

### Step 2: Conduct the Intake Interview

**⟁ CLARIFY** — Gather the following information before generating any documents.
Present as a structured intake form. Ask all questions before proceeding.

#### Section A — Personal Information

1. **Client name(s) and date(s) of birth**
2. **Marital status**: Single, married, domestic partnership, divorced, widowed
   - If married: Is spouse a US citizen? (Non-citizen spouse → QDOT analysis required)
   - If divorced: Any existing QDRO, divorce decree asset division to consider?
3. **Children**: Names, dates of birth, any with special needs or disabilities?
   - If minor children: Guardian nomination needed
   - If adult children with special needs: SNT analysis required
4. **Other beneficiaries**: Parents, siblings, charitable organizations, friends
5. **State of domicile** (primary residence state — governs document execution)
6. **Other states where real property is owned** (may require ancillary probate avoidance)

#### Section B — Asset Inventory

| Asset Category               | Items to Capture                                                                                            |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Real property                | Address, estimated FMV, current title (joint tenancy, community property, sole ownership), mortgage balance |
| Financial accounts           | Bank, brokerage (non-retirement), current beneficiary designations                                          |
| Retirement accounts          | IRA, 401(k), 403(b), Roth IRA — current beneficiary designations, balance                                   |
| Life insurance               | Carrier, face value, cash value, owner, insured, current beneficiary designation                            |
| Business interests           | Entity type, ownership %, buy-sell agreement, estimated value                                               |
| Tangible personal property   | Vehicles (titled), collectibles, jewelry, art — estimated value                                             |
| Digital assets               | Crypto wallets, domain names, digital accounts with monetary value                                          |
| Total estimated gross estate | (Sum of above — critical for tax threshold analysis)                                                        |

#### Section C — Goals and Concerns

1. **Primary goals**: Avoid probate? Minimize estate taxes? Provide for incapacity?
   Plan for minor children? Protect assets from creditors? Charitable giving?
2. **Trust funding willingness**: Is client willing to retitle assets into trust?
3. **Trustee preference**: Serve as own trustee? Family member? Corporate trustee?
4. **Healthcare agent**: Who should make medical decisions if incapacitated?
5. **Financial agent (POA)**: Who should manage finances if incapacitated?
6. **Asset distribution**: Outright to beneficiaries? In trust? Equal vs. unequal shares?
7. **Conditional distributions**: Age restrictions, incentive provisions, substance abuse protections?
8. **Special circumstances**: Blended family dynamics, estranged family members, anticipated
   large inheritance, pre-nuptial agreement, prior estate plan to update?

**⟁ CLARIFY** — If the gross estate exceeds $7 million (individual) or $14 million (married
couple), flag for enhanced estate tax analysis. If 2026 sunset planning is relevant, ask:
"Do you want me to analyze strategies to lock in the current elevated exemption before the
anticipated 2026 TCJA sunset?"

### Step 3: Classify the Estate Plan Type

Based on intake data, classify the plan into one of five client scenarios. Each drives
document selection, structure, and tax strategy.

| Scenario                            | Triggers                                                     | Core Documents                                                                                    | Tax Strategy                                                              |
| ----------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Basic**                           | Single adult, no minor children, gross estate < $3M          | RLT, Pour-Over Will, DPOA, AHCD, HIPAA                                                            | No estate tax planning needed                                             |
| **Married Couple — Standard**       | Married, no special needs beneficiary, gross estate $3M–$12M | RLT (joint or separate), Pour-Over Wills, DPOAs, AHCDs, HIPAA, transfer docs                      | Portability election, consider credit shelter sub-trust                   |
| **Married Couple — Taxable Estate** | Married, gross estate > $13.99M (2025) per person            | Separate RLTs with AB trust structure or disclaimer trust, Pour-Over Wills, DPOAs, AHCDs, HIPAA   | Credit shelter trust / bypass trust, QTIP trust, ILIT, portability backup |
| **Special Needs**                   | Beneficiary with disability receiving SSI/Medicaid           | RLT with SNT sub-trust (third-party), Pour-Over Will, DPOAs, AHCDs, HIPAA, ABLE account planning  | SNT structured to avoid countable resource classification                 |
| **High Net Worth**                  | Gross estate > $13.99M or above 2026 sunset threshold        | Comprehensive plan with irrevocable trusts (SLAT, GRAT, ILIT, dynasty trust), DPOAs, AHCDs, HIPAA | Active estate freeze and transfer strategies                              |

**⟁ CLARIFY** — For blended families (prior marriages, step-children), ask: "How should
assets be divided between your current spouse and children from prior relationships? This
affects trust structure significantly — options include a QTIP trust, separate trusts per
family branch, or outright equal division."

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** (if connected) to verify jurisdiction-specific requirements for the
client's state of domicile.

**Research for each state:**

1. Will execution: witnesses required, notarization, self-proving affidavit form
2. Trust statute: state UTC enactment, any registration requirements
3. DPOA statute: UPOAA enactment version, "hot powers" list, third-party acceptance
4. AHCD statute: execution requirements, POLST form, pregnancy exception
5. TOD deed availability and recording requirements
6. State estate/inheritance tax: exemption amount, rate schedule, return due dates
7. Community property rules (if applicable)

**Save verified findings** to `/tmp/estate-plan-jurisdiction-[state].md` for use throughout
the drafting workflow.

**If legalcode-mcp is not connected:**

- Mark all state-specific formality requirements with [VERIFY in state statutes]
- Proceed with majority-rule approaches as described below
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`

### Step 5: Generate the Document Suite

Generate each document in the order below. Sequence matters — the trust must be created
before the pour-over will can reference it.

**5a — Revocable Living Trust**
**5b — Pour-Over Will**
**5c — Durable Financial Power of Attorney**
**5d — Advance Healthcare Directive**
**5e — HIPAA Authorization**
**5f — Transfer and Funding Documents**

Each document is detailed in the **Document Analysis** section below.

### Step 6: Estate Tax and Portability Analysis

Perform estate tax analysis for all clients. Flag if action is needed.

**Tax threshold screening:**

- If gross estate < $3M → no federal estate tax issue; flag state estate tax if applicable
- If gross estate $3M–$13.99M → portability election recommended; credit shelter analysis
- If gross estate > $13.99M → comprehensive planning required (see High Net Worth scenario)
- If 2026 sunset planning relevant → exemption utilization strategies

See **Federal Estate Tax Analysis** section below.

### Step 7: Trust Funding Checklist

Generate a trust funding checklist tailored to the client's asset inventory. An unfunded
trust is one of the most common estate planning failures.

See **Trust Funding Checklist** section below.

### Step 8: Self-Interrogation and Quality Review

Before delivering the output, apply the three-pass self-interrogation to all HIGH or
CRITICAL items. Verify completeness against the 18 document elements checklist.

See **Quality Assurance Frameworks** section below.

### Step 9: Deliver the Estate Plan Package

Compile the final output using the **Output Format Template** at the end of this skill.

---

## Document Analysis

### Document 1: Revocable Living Trust

#### Purpose

Holds assets during life, avoids probate on death, provides for management of assets during
incapacity without court-supervised conservatorship.

#### Governing Authority

- Uniform Trust Code (UTC, 2000, as amended 2010) — adopted in approximately 36 states [VERIFY]
- Common law of trusts in non-UTC states (FL, TX, CA, NY have their own trust codes)
- IRC §671–679 (grantor trust rules) — grantor taxed on income during lifetime
- State Uniform Prudent Investor Act (adopted all 50 states) — governs trustee investment duties

#### Required Provisions

| Provision                       | Description                                                                                    | Severity if Absent |
| ------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------ |
| Trust name and date             | Identifies the trust for asset titling                                                         | CRITICAL           |
| Grantor identity                | Full legal name, state of domicile                                                             | CRITICAL           |
| Initial trustee designation     | Grantor typically serves as own trustee                                                        | CRITICAL           |
| Successor trustee chain         | At least 2 levels deep; corporate trustee as backstop                                          | CRITICAL           |
| Incapacity standard             | Defines when successor trustee takes over (e.g., two physicians' certifications)               | HIGH               |
| Revocation/amendment power      | Express reservation of right to revoke or amend                                                | CRITICAL           |
| Distribution during incapacity  | HEMS standard (Health, Education, Maintenance, Support) or broader discretion                  | HIGH               |
| Post-death disposition          | Who gets what, in what share, under what conditions                                            | CRITICAL           |
| Trustee powers                  | Comprehensive enumeration: invest, sell, lease, borrow, make distributions, make tax elections | HIGH               |
| Spendthrift clause              | Protects beneficiaries' interests from creditors and assignees                                 | RECOMMENDED        |
| No-contest (in terrorem) clause | Disinheritance penalty for challenging the trust                                               | RECOMMENDED        |
| Trust protector provision       | Third-party power to modify trust in response to law changes                                   | RECOMMENDED        |
| Governing law                   | State law governing trust administration                                                       | HIGH               |
| Perpetuities savings clause     | Limits trust duration to avoid RAP violation (if state has RAP)                                | HIGH               |
| Schedule A                      | Initial list of assets contributed to trust                                                    | RECOMMENDED        |

#### Trustee Succession Design

```
Primary Trustee: [Grantor(s)]
  ↓ (on incapacity or death)
First Successor Trustee: [Named individual — spouse, adult child, or trusted advisor]
  ↓ (if unwilling or unable)
Second Successor Trustee: [Named individual — alternate]
  ↓ (if unwilling or unable)
Corporate Trustee: [Bank trust department or trust company — backstop]
```

**⟁ CLARIFY** — Ask: "Who do you want to manage the trust if you are incapacitated or
after your death? This person has significant responsibility — they will manage assets,
pay bills, and distribute funds to beneficiaries. Options: (A) Spouse or partner,
(B) Adult child, (C) Sibling or friend, (D) Professional/corporate trustee, (E) Co-trustees
(two people acting together for checks and balances)."

#### Sub-Trust Structures for Taxable Estates

For married couples with taxable estates, consider:

**Credit Shelter Trust (Bypass Trust / "B" Trust)**

- Funded with the deceased spouse's remaining BEA (up to $13.99M in 2025)
- Assets grow outside surviving spouse's estate
- Surviving spouse may be discretionary beneficiary (HEMS standard)
- Not included in surviving spouse's estate at death
- Avoids double taxation on appreciation
- [JURISDICTION-SPECIFIC] No longer needed in most states for federal tax purposes due to
  portability, but still valuable in states without portability and for GST planning

**QTIP Trust (Qualified Terminable Interest Property)**

- Marital deduction trust — qualifies for 100% marital deduction (IRC §2056(b)(7))
- Surviving spouse receives all income at least annually
- Trustee (or executor) makes QTIP election on estate tax return (Form 706)
- Allows first spouse to control ultimate remainder distribution (protects children from
  prior relationship against disinheritance)
- DSUE not available on QTIP assets — portability election still required

**Disclaimer Trust**

- Post-mortem flexibility: surviving spouse can disclaim assets into credit shelter trust
  within 9 months of death (IRC §2518)
- Simpler during life (no two-trust administration), flexible at death
- Requires surviving spouse to make informed, timely disclaimer decision

#### Special Needs Sub-Trust (Third-Party SNT)

See Document 6 — Special Needs Trust Analysis below.

---

### Document 2: Pour-Over Will

#### Purpose

Captures any assets not titled in the trust at death and "pours" them into the trust via
probate. Also the vehicle for minor guardian nomination — this cannot be done in a trust.

#### Governing Authority

- Uniform Probate Code (UPC) §2-511 (pour-over wills) — adopted in approximately 18 states [VERIFY]
- State-specific wills acts in non-UPC states
- UTATA (Uniform Testamentary Additions to Trusts Act) — incorporated in most states

#### Required Provisions

| Provision                              | Description                                                          | Severity if Absent           |
| -------------------------------------- | -------------------------------------------------------------------- | ---------------------------- |
| Testamentary intent                    | Express statement this is the testator's will                        | CRITICAL                     |
| Revocation of prior wills              | Express revocation of all prior wills and codicils                   | CRITICAL                     |
| Pour-over clause                       | Residuary estate to trustee of named revocable trust                 | CRITICAL                     |
| Guardian nomination                    | Nomination of guardian(s) for minor children, with alternates        | CRITICAL (if minor children) |
| Personal property memorandum reference | Reference to tangible personal property list (allowed in UPC states) | RECOMMENDED                  |
| Executor nomination                    | With at least one alternate; bond waiver                             | HIGH                         |
| Self-proving affidavit                 | Notarized attestation to avoid in-court witness testimony            | RECOMMENDED                  |

#### Execution Formalities — By State Category

[JURISDICTION-SPECIFIC] Verify state-specific requirements before execution.

| Formality                    | Majority Rule                                                                             | Key Exceptions                                |
| ---------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------- |
| Witnesses required           | 2 adult witnesses                                                                         | VT requires 3 witnesses [VERIFY]              |
| Notarization                 | Not required for validity; required for self-proving affidavit                            | LA requires notarization                      |
| Holographic will recognition | ~30 states recognize holographic (handwritten, unwitnessed) wills [VERIFY]                | CA, TX, NY recognize holographic; NJ does not |
| Electronic wills             | ~15 states permit [VERIFY]                                                                | FL, NV, IN among early adopters               |
| Prohibited witnesses         | Interested witnesses (beneficiaries) create presumption of undue influence in most states |                                               |

**⟁ CLARIFY** — If the client has minor children: "You need to nominate a guardian for your
minor children in your will. This is critically important. Who do you want to raise your
children if both parents die? And who would be the alternate if your first choice is unable
or unwilling to serve?"

---

### Document 3: Durable Financial Power of Attorney

#### Purpose

Authorizes a named agent (attorney-in-fact) to manage financial affairs if the principal
becomes incapacitated. "Durable" means the power survives incapacity (unlike a general POA
which terminates on incapacity). Avoids the need for court-supervised conservatorship.

#### Governing Authority

- Uniform Power of Attorney Act (UPOAA, 2006) — adopted in approximately 27 states [VERIFY]
- State-specific POA statutes in non-UPOAA states
- Restatement (Third) of Agency for general agency principles

#### Immediately Effective vs. Springing

| Type                      | Description                                           | Pros                                              | Cons                                                               |
| ------------------------- | ----------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------ |
| **Immediately effective** | Agent has authority from signing                      | Simpler to use; no incapacity certification delay | Risk of unauthorized use while principal is competent              |
| **Springing**             | Agent's authority "springs" into effect on incapacity | No risk of misuse while competent                 | Requires incapacity determination; third parties may require proof |

**Practice note**: Most estate planners recommend immediately effective DPOAs with a
trusted agent, as the springing mechanism creates practical barriers to use when needed.

#### "Hot Powers" Requiring Express Authorization

Under UPOAA and most state statutes, the following require express grant:

| Hot Power                               | Significance                                                                         | Express Language Required                        |
| --------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------ |
| Make gifts                              | Allows agent to make annual exclusion gifts ($19,000/person in 2025) or larger gifts | "Agent may make gifts" with any limits specified |
| Create or amend trusts                  | Allows trust funding and modification                                                | Express authorization                            |
| Change beneficiary designations         | Critical for retirement accounts                                                     | Express authorization                            |
| Create or amend a survivorship interest | Joint tenancy with right of survivorship                                             | Express authorization                            |
| Exercise fiduciary authority            | If principal is trustee of another trust                                             | Express authorization                            |
| Delegate agent authority                | Sub-agents                                                                           | Express authorization                            |
| Waive principal's rights to benefits    | Government benefits, insurance                                                       | Express authorization                            |

[JURISDICTION-SPECIFIC] Verify state-specific "hot powers" list — varies from UPOAA default.

#### Third-Party Acceptance

Under UPOAA §120, third parties (banks, financial institutions) who refuse to honor a valid
DPOA may be liable for damages. However, third parties may still:

- Request a certification of validity
- Request an opinion of counsel
- Require the institution's own form (contact all financial institutions to confirm acceptance)

---

### Document 4: Advance Healthcare Directive

#### Purpose

Designates a healthcare agent to make medical decisions and expresses the principal's wishes
regarding life-sustaining treatment, organ donation, and other healthcare matters if the
principal is incapacitated.

#### Governing Authority

- Patient Self-Determination Act (42 U.S.C. §1395cc(f)) — requires hospitals to inform
  patients of right to execute advance directives
- Uniform Health-Care Decisions Act (UHCDA, 1993/2019 revision) — adopted in ~13 states [VERIFY]
- State-specific healthcare directive statutes (every state has one)
- Cruzan v. Director, Mo. Dep't of Health, 497 U.S. 261 (1990) — constitutional right to refuse treatment

#### Two-Component Structure

**Component 1 — Healthcare Proxy (Agent Designation)**

- Names agent with authority to make healthcare decisions
- Names successor agent(s)
- Specifies scope of authority (all healthcare decisions, or limited)
- States when authority becomes effective (typically upon incapacity)

**Component 2 — Living Will (Substantive Instructions)**

- Terminal illness / permanent unconsciousness instructions
- Life-sustaining treatment (ventilators, feeding tubes, CPR)
- Comfort care and palliative care instructions
- Organ and tissue donation preferences
- Mental healthcare instructions (if separate is not used)

#### POLST vs. AHCD Distinction

| Document                                                   | Who Executes                | Portability                                                 | Purpose                                                         |
| ---------------------------------------------------------- | --------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------- |
| **AHCD** (Advance Healthcare Directive)                    | Competent adult in advance  | Planning document; not immediately actionable medical order | Designates agent; states future wishes                          |
| **POLST** (Physician Orders for Life-Sustaining Treatment) | Current patient + physician | Portable medical order; immediately actionable              | Current medical instructions for fragile/seriously ill patients |

**Practice note**: AHCD is appropriate for most estate planning clients. POLST is for clients
with serious, current medical conditions. Both can and should coexist.

#### Key Instructions to Elicit

**⟁ CLARIFY** — Ask the client:

1. "If you are in a permanent vegetative state with no reasonable chance of recovery,
   do you want life-sustaining treatment continued, withdrawn, or is it your agent's
   decision?"
2. "Do you want artificial nutrition and hydration (feeding tubes) in that circumstance?"
3. "Do you wish to donate organs and/or tissue at death?"
4. "Are there any specific religious, cultural, or personal values your agent should
   know about in making healthcare decisions?"

[JURISDICTION-SPECIFIC] Several states have pregnancy exceptions — a directive may be
suspended if the principal is pregnant. Verify state law and address in the document.

---

### Document 5: HIPAA Authorization

#### Purpose

Authorizes healthcare providers to disclose protected health information (PHI) to named
individuals — typically the healthcare agent, financial agent, and close family members.
Without this, healthcare providers cannot discuss the patient's medical status with family.

#### Governing Authority

- Health Insurance Portability and Accountability Act, Pub. L. 104-191
- 45 C.F.R. §164.508 — authorization requirements
- 45 C.F.R. §164.510(b) — allows disclosure to family without authorization for direct care
  (but does NOT allow general medical status disclosure without authorization)

#### Required Elements under 45 C.F.R. §164.508(c)

| Element                                                 | Requirement                                                          |
| ------------------------------------------------------- | -------------------------------------------------------------------- |
| Description of PHI to be disclosed                      | "All medical records, health information, and treatment information" |
| Name or class of persons authorized to make disclosure  | Healthcare provider(s) or "any healthcare provider"                  |
| Name or class of persons to whom disclosure may be made | Named individuals (agent, spouse, children)                          |
| Purpose of the disclosure                               | "Personal use and benefit" or "estate planning" or specific purpose  |
| Expiration date or expiration event                     | "Death," "revocation by me," or specific date (not "none")           |
| Signature of individual and date                        | Wet signature required                                               |

#### Scope Recommendations

- Authorize disclosure to healthcare agent (AHCD agent), successor, and key family members
- Include mental health records authorization (many states have separate, more restrictive rules — [JURISDICTION-SPECIFIC])
- Authorize disclosure to DPOA agent for billing and payment purposes
- Include after-death authorization for executor/trustee access to medical records
  (relevant for benefit claims, contested estate proceedings)

---

### Document 6: Asset Transfer Documents and Trust Funding

#### Purpose

An unfunded trust is a wasted trust. Assets must be titled in the name of the trust (or
have the trust named as beneficiary) to pass outside probate.

#### Trust Funding Checklist

| Asset Category                          | Action Required                                                                                                                                                          | Priority |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| **Primary residence**                   | Deed new deed to trustee: "[Client Name], Trustee of the [Trust Name], dated [Date]" — record with county recorder                                                       | HIGH     |
| **Vacation/investment real property**   | Same as primary residence; ancillary trust sub-trust may be needed for out-of-state property                                                                             | HIGH     |
| **Bank accounts (non-retirement)**      | Retitle account to trust; or add trust as POD beneficiary                                                                                                                | HIGH     |
| **Brokerage accounts (non-retirement)** | Retitle to trust; or add trust as TOD beneficiary                                                                                                                        | HIGH     |
| **IRAs (traditional and Roth)**         | DO NOT retitle in trust — update beneficiary designation to named individuals (primary/contingent). Trust-as-beneficiary only if conduit trust requirements met [VERIFY] | CRITICAL |
| **401(k), 403(b), pension**             | Update beneficiary designation. Spouse is default primary beneficiary under ERISA — spousal consent required to change                                                   | CRITICAL |
| **Life insurance**                      | Update beneficiary designation; consider ILIT ownership for large policies                                                                                               | HIGH     |
| **Vehicles**                            | Transfer on death (TOD) title in states that permit it; otherwise leave outside trust (small value probate)                                                              | MEDIUM   |
| **Business interests (LLC/LP)**         | Assign membership/limited partnership interest to trust per operating agreement provisions                                                                               | HIGH     |
| **S-Corp stock**                        | Assign to trust — WARNING: S-Corp may only have eligible trusts as shareholders (QSST or ESBT election required)                                                         | CRITICAL |
| **Digital assets**                      | Note in schedule with access credentials in secure location; see Revised UFADAA state enactments                                                                         | MEDIUM   |
| **Tangible personal property**          | Assignment of tangible personal property memorandum to trust                                                                                                             | MEDIUM   |
| **Safe deposit box**                    | Add trust as co-owner                                                                                                                                                    | LOW      |

#### Beneficiary Designation Review

Beneficiary designations **supersede** the will and trust for accounts they cover.
Conflicting or outdated designations are one of the most common estate planning failures.

| Designation Issue                        | Severity | Corrective Action                                                                                    |
| ---------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------- |
| Ex-spouse still named                    | CRITICAL | Update immediately                                                                                   |
| Estate named as beneficiary              | HIGH     | IRAs payable to estate lose stretch and trigger immediate income tax; replace with named individuals |
| No contingent beneficiary                | HIGH     | Add contingent designation                                                                           |
| Minor child named directly               | HIGH     | Minor cannot receive funds directly; needs custodian or trust — update to trust or UTMA custodian    |
| Special needs beneficiary named directly | CRITICAL | Direct inheritance disqualifies from SSI/Medicaid; update to SNT                                     |
| Per stirpes vs. per capita designation   | MEDIUM   | Confirm intent; default per capita may not be what client intends                                    |

#### Retirement Accounts — SECURE Act 2.0 Rules

Under the SECURE Act 2.0 (Pub. L. 117-328, enacted December 2022):

- **Eligible Designated Beneficiaries (EDBs)** — not subject to 10-year rule:
  - Surviving spouse
  - Minor children (until age of majority, then 10-year rule triggers)
  - Disabled or chronically ill individuals (see IRC §7702B)
  - Individuals not more than 10 years younger than the decedent
- **Designated Beneficiaries (DBs)** — 10-year rule applies (full distribution by end of Year 10)
  - Annual RMDs required during 10-year period if decedent was taking RMDs [VERIFY IRS 2024 final regs]
- **Non-Designated Beneficiaries** (including estates and most trusts) — 5-year rule or
  no-life-expectancy stretch
- **IRS Final Regulations (2024)**: Confirm RMD requirements for inherited IRAs under
  the 10-year rule [VERIFY against IRS final regs effective date]

**Trust-as-Beneficiary Considerations**:

- **Conduit trust**: All RMDs distributed to beneficiaries — look-through available,
  treats beneficiaries as designated beneficiaries
- **Accumulation trust**: Retains RMDs in trust — all beneficiaries (including remote
  contingents) must qualify as designated beneficiaries
- For special needs beneficiaries: accumulation trust with EDB designation for disabled
  beneficiary is preferred but must meet complex requirements [VERIFY]

---

## Federal Estate Tax Analysis

### Applicable Exclusion Amount (BEA) — 2025

| Metric                                  | 2025 Amount                                                   | Notes                                        |
| --------------------------------------- | ------------------------------------------------------------- | -------------------------------------------- |
| Basic Exclusion Amount (BEA) per person | $13,990,000 [VERIFY — indexed annually for inflation]         | Set by TCJA 2017; sunsets 2026               |
| Annual Gift Tax Exclusion               | $19,000 per donor per recipient                               | 2025; indexed for inflation                  |
| Top estate/gift tax rate                | 40%                                                           | On amounts above BEA                         |
| Marital deduction                       | Unlimited (US citizen spouse)                                 | IRC §2056                                    |
| Marital deduction (non-citizen spouse)  | $0 unlimited / $185,000 annual exclusion [VERIFY 2025 amount] | QDOT required for full deferral — IRC §2056A |

### 2026 TCJA Sunset — Planning Window

**CRITICAL**: The elevated BEA under TCJA is scheduled to sunset on January 1, 2026
(absent Congressional action). The BEA is expected to revert to approximately $7 million
per person (inflation-adjusted from the pre-TCJA $5 million base) [VERIFY — depends on
legislative outcome].

**Key anti-clawback rule**: Final Treasury Regulations (T.D. 9884, 2019) confirm that gifts
made during the elevated exemption period that use the higher BEA will NOT be clawed back
even if the exemption drops at death.

**2025–2026 Planning Strategies**:

1. **Lifetime gifts to use elevated BEA** — Make gifts up to $13.99M before sunset
   (direct gifts, or into SLATs, dynasty trusts, or other irrevocable structures)
2. **SLAT (Spousal Lifetime Access Trust)** — Irrevocable trust for spouse;
   uses donor-spouse's BEA; spouse retains access to distributions [IRC §2036 monitoring]
3. **GRAT (Grantor Retained Annuity Trust)** — IRC §2702; effective when appreciation
   exceeds §7520 rate; works in any rate environment for appreciating assets
4. **ILIT (Irrevocable Life Insurance Trust)** — Removes life insurance from estate;
   use "Crummey" demand right powers for annual exclusion funding
5. **Annual exclusion gifting** — $19,000 per donor per recipient; $38,000 per couple;
   use 529 superfunding (5-year election = $95,000 per beneficiary per donor in 2025)

### Portability — Deceased Spousal Unused Exclusion (DSUE)

#### Governing Authority

- IRC §2010(c)(5) — portability election
- Rev. Proc. 2022-32 — 5-year window for late portability election (superseded Revenue
  Procedure 2017-34)

#### Key Rules

| Rule                       | Detail                                                                                                                                                                                               |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Election mechanism         | Form 706 must be filed within 9 months of death (or 15 months with extension)                                                                                                                        |
| Late portability           | Rev. Proc. 2022-32: estates not required to file Form 706 may make portability election within 5 years of death of first spouse — file Form 706 with "FILED PURSUANT TO REV. PROC. 2022-32" notation |
| DSUE amount                | Unused BEA of last deceased spouse is portable to surviving spouse                                                                                                                                   |
| DSUE + BEA stacking        | Surviving spouse uses their own BEA first, then DSUE                                                                                                                                                 |
| GST exemption NOT portable | DSUE cannot be allocated to GST exemption; each spouse must allocate their own GST exemption                                                                                                         |
| DSUE lost on remarriage    | DSUE is the last deceased spouse's; if surviving spouse remarries and new spouse predeceases, earlier DSUE is lost                                                                                   |
| IRS audit risk             | DSUE claims subject to examination during surviving spouse's estate proceeding                                                                                                                       |

**⟁ CLARIFY** — For married clients: "Portability allows the surviving spouse to inherit
the first spouse's unused estate tax exemption. To preserve this, Form 706 must generally
be filed within 9–15 months of the first spouse's death, even if no estate tax is owed.
Do you want me to flag this obligation and include a note to the executor?"

### State Estate and Inheritance Taxes

[JURISDICTION-SPECIFIC] Approximately 17 states plus DC impose estate or inheritance taxes,
often with much lower exemptions than the federal BEA. Research and apply state-specific rules.

States with estate taxes (exemption much lower than federal): MA ($2M), OR ($1M), WA ($2.193M),
MN (~$3M), IL (~$4M), VT (~$5M), NY ($6.94M), ME, CT, HI, MD [VERIFY all amounts — subject
to annual change].

States with inheritance taxes: IA (being phased out), KY, MD (both!), NE, NJ, PA [VERIFY].

**Estate tax cliff effect**: Some states impose tax on the ENTIRE estate when it exceeds
the exemption, not just the excess — NJ formerly, Washington state [VERIFY current structure].

---

## Special Needs Trust Analysis

### When SNT Is Required

An SNT is required whenever a beneficiary receives or may receive means-tested government
benefits including SSI (Supplemental Security Income) and Medicaid. Leaving assets directly
to a special needs beneficiary — through a will, trust, or beneficiary designation — can
disqualify them from these benefits.

### SNT Types

| Type                               | Authority                                   | Funded By                                                                                 | Payback Requirement                                           | Best For                                                                |
| ---------------------------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **First-party (self-settled) SNT** | 42 U.S.C. §1396p(d)(4)(A)                   | Beneficiary's own assets (e.g., personal injury settlement, inheritance already received) | YES — state Medicaid payback on death                         | Beneficiary who received assets directly and needs to preserve benefits |
| **Pooled SNT**                     | 42 U.S.C. §1396p(d)(4)(C)                   | Beneficiary's own assets, managed by nonprofit                                            | YES — proportionate share to Medicaid; remainder to nonprofit | Smaller estates; no family trustee available                            |
| **Third-party SNT**                | General trust law; NOT the Medicaid statute | Third party (parent, grandparent) assets                                                  | NO payback requirement                                        | Estate planning by parents/family for special needs beneficiary         |

### Third-Party SNT Provisions (for estate planning)

Key provisions in a third-party SNT sub-trust within the revocable trust or pour-over will:

1. **Supplemental needs language**: Trust is to "supplement, not supplant" government benefits
   — trustee may not make distributions for items covered by SSI/Medicaid
2. **Trustee selection**: Individual trustee (family member) or co-trustee with professional/
   SNT-specialized trustee; avoid naming the beneficiary as sole trustee
3. **No self-settled language**: Must clearly be funded only from third-party sources
4. **Prohibited distributions**: Direct cash to beneficiary; anything that would count as
   "in-kind support and maintenance" (ISM) reducing SSI (food, shelter)
5. **Permissible distributions**: Education, therapy, recreation, personal care items,
   technology, travel, pet care, entertainment — items that enhance quality of life
6. **Termination**: On death of beneficiary; distribution of remaining assets per trust terms
   (no Medicaid payback required for third-party SNT)

### ABLE Account Interaction

- ABLE accounts (26 U.S.C. §529A) are savings accounts for disabled individuals that do not
  count as SSI/Medicaid resources up to the ABLE exemption ($100,000 for SSI purposes [VERIFY])
- Annual contribution limit: $18,000 in 2024 (indexed) plus beneficiary's employment income
  up to the federal poverty line amount [VERIFY 2025 limit]
- SNT and ABLE can coexist; ABLE is simpler for smaller amounts; SNT for larger amounts
- Coordination: trustee of SNT may fund ABLE account; SNT retains control of larger funds

---

## Quality Assurance Frameworks

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before delivering.

| Gate           | Rule                                                                                              | Fail Action                                |
| -------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **Source**     | Every tax and statutory claim cites a specific IRC section, regulation, or statute                | Add citation or mark "[UNVERIFIED]"        |
| **Format**     | All citations follow consistent format (IRC §XXXX, 42 U.S.C. §XXXX, Pub. L. XXX-XXX)              | Fix format                                 |
| **Currency**   | Exemption amounts, exclusion figures, and regulatory references checked against 2025 IRS guidance | Flag "[CHECK CURRENCY — may have changed]" |
| **Domain**     | Analysis stays within US federal and state estate planning law — no tax advice beyond scope       | Remove or flag out-of-scope guidance       |
| **Confidence** | Uncertainty explicitly stated, not hidden; all [VERIFY] tags present                              | Add confidence qualifier                   |

### Self-Interrogation for High-Severity Items

For any item classified CRITICAL (document execution failure, disqualifying SNT provision,
estate tax cliff), apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
cited authority? For example, does naming an estate as IRA beneficiary actually create the
income tax acceleration risk under the SECURE Act as analyzed?

**Pass 2 — Completeness**: Have all relevant statutes, regulations, and IRS guidance been
considered? Is there a state dimension not yet addressed? Has the SECURE Act 2.0 complexity
been fully accounted for?

**Pass 3 — Challenge**: What is the strongest argument that this risk is overstated? Under
what circumstances might the classification be wrong? (E.g., naming estate as beneficiary
could be intentional for creditor protection in a high-risk profession — did we account for that?)

### Confidence Scoring

| Level        | Range     | Meaning                                                               | Action                                         |
| ------------ | --------- | --------------------------------------------------------------------- | ---------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statutory text                                     | State with confidence                          |
| **High**     | 0.80–0.94 | Strong authority, minor interpretive questions                        | State with brief caveat                        |
| **Probable** | 0.60–0.79 | Good arguments, some uncertainty (e.g., 2026 sunset outcome)          | State with reasoning and contra-indicators     |
| **Possible** | 0.40–0.59 | Genuinely uncertain (state-specific formality, evolving IRS guidance) | Flag for attorney verification with both sides |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                                               | Do not assert; flag "[UNCERTAIN]"              |

### Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-estate-plan-generator"
  mode: "Document Suite Generation"
  client_scenario: "[Basic / Married-Standard / Married-Taxable / Special-Needs / High-Net-Worth]"
  state_of_domicile: "[State]"
  other_states_property: "[List or 'None']"
  gross_estate_estimated: "$[amount]"
  federal_estate_tax_exposure: "[None / Possible / Yes]"
  portability_recommended: "[Yes / No / Not applicable]"
  snт_required: "[Yes / No]"
  tcja_sunset_planning: "[Yes / No]"
  legalcode_mcp: "[Connected / Not connected]"
  jurisdiction_research_file: "[path or 'Not created']"
  documents_generated: "[List of documents]"
  critical_flags: "[List of CRITICAL items or 'None']"
  beneficiary_designation_issues: "[List or 'None']"
  trust_funding_checklist_items: "[count]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED — marked [VERIFY]]"
  confidence_overall: "[HIGH / MEDIUM / LOW — rationale]"
  limitations:
    - "All documents require review and execution under supervision of licensed estate planning attorney"
    - "Tax figures based on 2025 law; 2026 sunset outcome depends on Congressional action"
    - "State-specific execution formalities must be verified for state of domicile"
    - "[Any other specific limitations for this client]"
  reviewer: "AI-assisted — requires qualified estate planning attorney review before execution"
```

---

## Anti-Patterns

These are the most common estate planning failures — errors made both by clients who DIY
and by practitioners who cut corners. Do not replicate them.

1. **The Unfunded Trust** — Creating a revocable trust but failing to retitle assets into
   it. The trust exists on paper but all probate-avoidable assets still go through probate.
   _Prevention_: Generate and deliver the trust funding checklist at the same time as the
   trust; schedule a funding follow-up.

2. **Contradicting Beneficiary Designations** — Beneficiary designations on retirement
   accounts and life insurance supersede the will and trust. An ex-spouse named on a 401(k)
   will inherit those funds regardless of what the trust says.
   _Prevention_: Review all beneficiary designations as part of every estate plan.

3. **Naming a Minor as Direct Beneficiary** — A minor cannot receive funds directly.
   The court will appoint a guardian of the property (expensive, court-supervised) until
   the child reaches majority. Funds distributed at majority — typically age 18 — which may
   not be the client's intent.
   _Prevention_: Use a trust for minor beneficiaries or name a UTMA custodian.

4. **Naming a Special Needs Beneficiary Directly** — Leaving assets directly to a
   beneficiary receiving SSI or Medicaid will disqualify them from benefits.
   _Prevention_: Always use a third-party SNT for special needs beneficiaries.

5. **No Pour-Over Will** — A trust without a pour-over will leaves assets acquired after
   funding without a residuary plan. These assets go through probate by intestacy.
   _Prevention_: Always pair a revocable trust with a pour-over will.

6. **Naming "Estate" as IRA Beneficiary** — Naming the estate as beneficiary of an IRA
   eliminates the 10-year stretch and triggers immediate income tax acceleration. No named
   beneficiary = same problem.
   _Prevention_: Always name individuals or a qualifying trust as IRA beneficiary.

7. **Joint Tenancy Overriding the Trust** — Assets held in joint tenancy with right of
   survivorship pass to the surviving joint tenant regardless of trust terms. Parents adding
   an adult child to title "for convenience" may inadvertently gift half the property and
   divert it from the intended beneficiaries.
   _Prevention_: Review all title arrangements; use trust ownership rather than joint tenancy.

8. **S-Corporation Stock in Trust Without S-Corp Election** — Not all trusts are eligible
   S-corporation shareholders. A revocable trust is eligible during the grantor's lifetime,
   but a successor trust must make a Qualified Subchapter S Trust (QSST) or Electing Small
   Business Trust (ESBT) election within 2 years.
   _Prevention_: Flag S-corp interests in intake; include S-Corp election reminder in
   trust administration instructions.

9. **The Stale Estate Plan** — An estate plan drafted before major life changes (marriage,
   divorce, birth of children, death of named trustees or agents, significant asset changes)
   may be worse than no plan. A trust naming a deceased trustee or a will leaving everything
   to a prior spouse can cause significant harm.
   _Prevention_: Recommend review every 3–5 years or after any major life event.

10. **DPOA Without Hot Powers** — A DPOA that lacks express authorization for gifts,
    trust modification, or beneficiary changes cannot be used for the most important
    estate planning lifetime actions. The agent cannot make annual exclusion gifts to
    reduce the taxable estate.
    _Prevention_: Include express "hot powers" grants; review agent's scope carefully.

11. **Missing HIPAA Authorization** — Healthcare providers cannot discuss a patient's
    condition with family without HIPAA authorization. A DPOA or AHCD alone does not
    authorize disclosure under HIPAA to all family members.
    _Prevention_: Include a standalone HIPAA authorization in every estate plan.

12. **QTIP Trust Without Portability Election** — The executor of the first spouse's estate
    must elect portability on Form 706 within 9–15 months of death. If the estate doesn't
    file because no tax is due, the portability is lost — possibly permanently (absent the
    Rev. Proc. 2022-32 late election window).
    _Prevention_: Include a mandatory note to executor to file Form 706 for portability;
    recommend attorney consultation at first spouse's death.

13. **Ignoring State Estate Taxes** — States like Massachusetts, Oregon, and Washington
    have estate taxes with exemptions far below the federal BEA. A $6M estate owes nothing
    to the IRS but may owe significant state estate tax.
    _Prevention_: Research state estate tax for every client's state of domicile.

14. **Pour-Over Will Without Guardian Nomination** — Clients with minor children must
    nominate a guardian in the will (not the trust — guardianship is a court proceeding
    and requires testamentary evidence of the parent's wishes).
    _Prevention_: Always ask about minor children in intake; flag guardian nomination as
    CRITICAL when applicable.

15. **Trust Protector Provisions Without Defined Powers** — Including a trust protector
    but failing to specify the protector's powers with precision can create ambiguity or
    enable overreach.
    _Prevention_: Define trust protector powers expressly: modify to comply with changed
    law, change governing jurisdiction, remove and replace trustee, but not alter
    beneficial interests without specific authorization.

16. **SLAT Reciprocal Trust Risk** — Spouses who each create SLATs for the other on
    identical terms risk the IRS collapsing them as "reciprocal trusts" (inclusion in
    both estates under Lehman v. Commissioner principles).
    _Prevention_: Vary the terms, timing, and assets — at least one year apart; different
    beneficial structures.

17. **Digital Assets Without Access Instructions** — Cryptocurrency wallets, domain names,
    and password-protected accounts may become inaccessible without a record of access
    credentials, even if the trust technically owns them.
    _Prevention_: Include digital assets schedule with secure storage instructions; reference
    Revised UFADAA fiduciary access provisions under state law.

18. **No No-Contest Clause in Contested-Estate States** — In states where in terrorem
    clauses are enforced (majority), the absence of a no-contest clause leaves the estate
    vulnerable to speculative challenges. In states where they are not enforced (FL, IN, KY),
    include a warning that the clause has no effect.
    _Prevention_: Include no-contest clause with a carved-out exception for challenges
    with probable cause; note state-specific enforceability.

---

## Writing Standards

Before delivering any estate plan output, verify these standards:

1. **Define terms before use**: "Trustee," "Beneficiary," "Successor Trustee," "Agent,"
   "Principal" — define in a Definitions section at the start of each document.
2. **Avoid gender-specific pronouns**: Use the client's pronouns or rewrite to avoid; use
   "the Trustee" not "he/she."
3. **Use active voice in operative clauses**: "The Trustee shall distribute" not
   "distributions shall be made by the Trustee."
4. **Plain language in instruction sections**: Avoid legalese in checklists, analyses,
   and recommendations; reserve legal terminology for operative provisions.
5. **Consistency across documents**: Terms defined in the trust should match terms used
   in the pour-over will (e.g., trust name, date, trustee).
6. **Hedge appropriately**: Use "typically," "generally," and "in most states" for
   majority-rule statements; never make a universally-stated claim that has state exceptions.
7. **No hallucinated citations**: Mark any citation not verified against an authoritative
   source with [VERIFY]. Do not fabricate case citations.
8. **Execution blocks**: Every document template must include the correct execution block
   for the state of domicile (witness lines, notary block, attestation language).

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 4, search for state-specific execution formalities, trust code provisions,
  POA "hot powers" lists, and state estate tax rules
- Search for current IRS estate and gift tax exclusion amounts and any 2025–2026 developments
- Search for SECURE Act 2.0 final IRS regulations on inherited IRA RMDs
- Save verified results to `/tmp/estate-plan-jurisdiction-[state].md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all state-specific formality requirements with [VERIFY in state statutes]
- Mark all tax figures with [CHECK CURRENCY — verify current IRS inflation adjustments]
- Mark all SECURE Act 2.0 RMD analysis with [VERIFY against IRS 2024 final regs]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using research-backed defaults described in each document section

---

## Localization Notes

This skill covers US federal law with state adaptation markers. For state-specific adaptation:

### High-Priority States for Local Research

| State      | Key Differences                                                                                                                                                                                 |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| California | Community property; Prop 19 (property tax reassessment on death); CA Probate Code trust formalities; CA statutory DPOA form; Prob. Code §21380 (donative transfer restrictions for elder abuse) |
| New York   | NY EPTL trust provisions; NY GOL POA form (very specific form requirements); NY healthcare proxy statute; state estate tax ($6.94M exemption, cliff effect); NY trust decanting statute         |
| Texas      | Community property; TX Property Code TOD deeds; no state estate tax; TX statutory DPOA; TX Estates Code pour-over provisions                                                                    |
| Florida    | No state estate tax; FL trust code ch. 736; FL statutory form POA; FL AHCD statute; FL electronic wills authorized                                                                              |
| Illinois   | IL estate tax (~$4M exemption); IL POA statute; IL no TOD real property deed; ancillary probate required for out-of-state property                                                              |
| Washington | Community property; WA estate tax (above $2.193M [VERIFY]); WA TEDRA for trust modifications; WA digital assets act                                                                             |

---

## Output Format Template

Deliver the estate plan output in the following structured format.

---

```markdown
# Estate Plan Package — [Client Name(s)]

**Date prepared**: [Date]
**Prepared by**: AI-assisted (legalcode-estate-plan-generator) — REQUIRES ATTORNEY REVIEW
**State of domicile**: [State]
**Client scenario**: [Basic / Married-Standard / Married-Taxable / Special-Needs / High-Net-Worth]

---

## Executive Summary

**Gross estate (estimated)**: $[amount]
**Federal estate tax exposure**: [None / Monitoring / Active planning required]
**2026 sunset planning**: [Not applicable / Recommended — see Tax Analysis section]
**Special needs planning**: [Not required / Required — SNT included]
**CRITICAL items**: [List or "None identified"]

---

## Document Suite

### 1. Revocable Living Trust — [Trust Name]

**Structure**: [Single grantor / Joint spousal / Married couple with separate trusts]
**Trustee succession**: [Grantor] → [Successor 1] → [Successor 2] → [Corporate backstop]
**Distribution at death**: [Summary of disposition scheme]
**Sub-trusts**: [Credit shelter / QTIP / SNT / Minors' trust / None]
**Special provisions**: [No-contest, trust protector, spendthrift — list]

[DRAFT OPERATIVE PROVISIONS]

---

### 2. Pour-Over Will — [Client Name]

**Executor**: [Name], alternate: [Name]
**Guardian nomination** (if applicable): [Name], alternate: [Name]
**Residuary disposition**: All to Trustee of [Trust Name]

[DRAFT OPERATIVE PROVISIONS]

---

### 3. Durable Financial Power of Attorney

**Agent**: [Name]
**Successor agent**: [Name]
**Effective**: [Immediately / Springing on incapacity]
**Hot powers expressly granted**: [List: gifts, trust modification, beneficiary changes, etc.]

[DRAFT OPERATIVE PROVISIONS]

---

### 4. Advance Healthcare Directive

**Healthcare agent**: [Name], successor: [Name]
**Life-sustaining treatment**: [Client's stated wishes]
**Artificial nutrition and hydration**: [Client's stated wishes]
**Organ donation**: [Client's stated wishes]

[DRAFT OPERATIVE PROVISIONS]

---

### 5. HIPAA Authorization

**Persons authorized to receive PHI**: [Agent, Successor, Named family members]
**PHI scope**: All medical records and health information
**Purpose**: Personal use, estate administration, healthcare decision-making
**Expiration**: Upon revocation or death of the individual

[DRAFT OPERATIVE PROVISIONS]

---

## Beneficiary Designation Review

| Account        | Institution   | Current Beneficiary | Recommended Change | Priority               |
| -------------- | ------------- | ------------------- | ------------------ | ---------------------- |
| [Account type] | [Institution] | [Current]           | [Recommended]      | [CRITICAL/HIGH/MEDIUM] |

---

## Trust Funding Checklist

| Asset               | Current Title   | Required Action                     | Completed |
| ------------------- | --------------- | ----------------------------------- | --------- |
| [Primary residence] | [Current]       | Deed to trustee of [Trust Name]     | ☐         |
| [Bank accounts]     | [Current]       | Retitle or add POD                  | ☐         |
| [Brokerage]         | [Current]       | Retitle or add TOD                  | ☐         |
| [IRA / 401(k)]      | N/A             | Update beneficiary designation only | ☐         |
| [Life insurance]    | [Current owner] | Update beneficiary designation      | ☐         |
| [Business interest] | [Current]       | Assignment to trust                 | ☐         |

---

## Estate Tax Analysis

**Federal BEA remaining (estimated)**: $[amount] (based on prior taxable gifts of $[amount])
**Portability**: [Recommended / Not applicable]

- Note to executor: File Form 706 within 9 months of death of first spouse to preserve DSUE,
  even if no estate tax is due. Late election available under Rev. Proc. 2022-32 within 5 years.
  **2026 Sunset Strategies**:
- [List recommended strategies with estimated tax savings]
  **State estate tax**: [State] imposes estate tax above $[amount]. Estimated exposure: $[amount].

---

## Special Needs Analysis (if applicable)

**Beneficiary**: [Name]
**Government benefits**: [SSI / Medicaid / SSDI / Other]
**SNT structure**: Third-party SNT sub-trust within Revocable Trust
**Trustee recommendation**: [Individual + professional co-trustee / Corporate SNT trustee]
**ABLE account**: [Recommended / Not applicable]

---

## Execution Requirements — [State]

| Document | Witnesses Required  | Notarization             | Special Requirements          |
| -------- | ------------------- | ------------------------ | ----------------------------- |
| Will     | [N] witnesses       | [Yes/No]                 | [Self-proving affidavit]      |
| Trust    | None in most states | Notarization recommended | [State specifics]             |
| DPOA     | [Witnesses]         | [Yes/No]                 | [Statutory form requirements] |
| AHCD     | [Witnesses]         | [Yes/No]                 | [Prohibited witnesses]        |
| HIPAA    | None required       | [Recommended]            | [None]                        |

> ⚠️ **All documents must be executed under the supervision of a licensed estate planning
> attorney in [State]. Do not execute any document without professional review of these
> AI-generated provisions.**

---

## Recommended Next Steps

1. [ ] Attorney review of all draft provisions
2. [ ] Resolve all [VERIFY] flags with current state statutes and IRS guidance
3. [ ] Execute documents in order: Trust → Will → DPOA → AHCD → HIPAA
4. [ ] Fund the trust: retitle assets per Trust Funding Checklist
5. [ ] Update beneficiary designations per Beneficiary Designation Review
6. [ ] File Form 706 for portability election within 9–15 months of first spouse's death (if married)
7. [ ] Schedule 3-year review or upon major life event

---

## Glass Box Audit Trail

[Populate from template in Quality Assurance Frameworks section]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on US federal estate planning
law (IRC Title 26, SECURE Act 2.0 Pub. L. 117-328, Rev. Proc. 2022-32), uniform acts
(UTC 2000, UPOAA 2006, UHCDA 1993/2019), HIPAA (45 C.F.R. Part 164), and Medicaid SNT
rules (42 U.S.C. §1396p). Research conducted via web-search agent pipeline. Incorporates
Legalcode quality frameworks (Citation Quality Gates, Self-Interrogation, Confidence Scoring,
Glass Box Audit Trail, Anti-Patterns) adapted from the legalcode-contract-review reference
standard. 18/18 required elements present.
