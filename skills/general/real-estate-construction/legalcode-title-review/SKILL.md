---
name: legalcode-title-review
description: Reviews title commitments and title registers for real estate transactions — purchase, refinance,
  and development. Use when analyzing an ALTA 2021 title commitment (Schedule B-I requirements, Schedule
  B-II exceptions), a UK HM Land Registry official copy of register entries, a California Preliminary
  Report, or any title abstract or opinion letter.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Reviews title commitments and title registers for real estate transactions — purchase, refinance, and development. Use when analyzing an ALTA 2021 title commitment (Schedule B-I requirements, Schedule B-II exceptions), a UK HM Land Registry official copy of register entries, a California Preliminary Report, or any title abstract or opinion letter. Analyzes easements, judgment and tax liens, mechanic's and materialmen's liens, restrictive covenants and CC&Rs, survey exceptions, mineral reservations, gap coverage risks, and endorsement requirements. Generates a closing checklist with prioritized curative action items, responsible parties, and deadlines. Supports the US ALTA/CLTA title insurance framework (owner's and lender's policies) and the UK Land Registration Act 2002 framework (absolute, good leasehold, possessory, and qualified title grades). Also triggers on: ALTA commitment review, title search analysis, Schedule B analysis, Schedule B-II exception analysis, title objection letter, curative title work, clearing title exceptions, closing checklist generation, title insurance endorsements, title defect cure, UK title register review, HM Land Registry search, land charges search, conveyancing title investigation, chain of title review, lien clearance.


# Legalcode Title Review

> **Disclaimer**: This skill provides a framework for AI-assisted title commitment and
> title register review. It does not constitute legal advice. All outputs must be reviewed
> by a qualified real estate attorney, title counsel, or licensed conveyancer before any
> reliance or closing decision is made. Title law is highly jurisdiction-specific, varies
> by county and state in the US, and changes frequently. Statutory and case law references
> cited from memory carry hallucination risk — verify against authoritative sources before
> relying on them. Title insurance commitment exceptions and requirements should always be
> reviewed in conjunction with the title insurer's underwriter and local counsel.

## Purpose and Scope

This skill reviews title commitments (US) and title register entries (UK) for real estate
transactions, producing a classified closing checklist with curative action items,
responsible parties, priorities, and timing.

**Covers:**

- Schedule A review: proposed insured, policy amounts, legal description accuracy
- Schedule B-I Requirements analysis: conditions to satisfy before title policy issuance
- Schedule B-II Exceptions analysis: exceptions to coverage, with curative paths
- Gap coverage risk assessment and protection strategies
- Endorsement requirement analysis by property type and transaction structure
- UK title register analysis: Property Register (A), Proprietorship Register (B), Charges Register (C)
- UK pre-registration title investigation (unregistered land)
- Closing checklist generation with tiered priorities, curative instructions, and party assignments
- Multi-party responsibility mapping (seller, buyer, lender, title company)

**Does not:**

- Draft purchase and sale agreements, deeds, or deeds of trust
- Conduct physical surveys or boundary line determinations
- Provide title insurance underwriting decisions or risk acceptance
- Cover Torrens title systems outside the US and UK frameworks described
- Replace the judgment of a licensed title insurance underwriter or real estate attorney

## Jurisdiction and Governing Law

This skill provides deep coverage for two primary title frameworks:

| Framework                 | Key Authority                                            | Title System                        | Primary Standards                                                                                                            |
| ------------------------- | -------------------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **US (ALTA/CLTA)**        | ALTA 2021 Commitment for Title Insurance                 | Deed recording with title insurance | ALTA 2021 Policy Forms; ALTA/NSPS 2021 Survey Minimum Standards; RESPA 12 U.S.C. §§ 2601-2617 [VERIFY]; state recording acts |
| **UK (HM Land Registry)** | Land Registration Act 2002; Land Registration Rules 2003 | Registered title system             | HMLR Practice Guides; Law Society Conveyancing Protocol; UK Finance Lenders' Handbook                                        |

[JURISDICTION-SPECIFIC] US title law varies substantially by state:

- **California**: CLTA standard policy is the norm; ALTA extended coverage requires a current survey; the industry uses "Preliminary Report" (not "Commitment"); CLTA endorsement forms differ from ALTA national forms.
- **New York**: Abstract of title system remains common; attorney review of abstract is standard; fee title insurance is customary for commercial; TIRSA rate and form filing.
- **Texas**: TLTA/TDI-approved forms (Form T-7 Commitment); escrow closing common; state-specific endorsement forms.
- **Florida**: Different endorsement practice; the F9 Closing Protection Letter (CPL) is standard.

[JURISDICTION-SPECIFIC] For jurisdictions outside US/UK, replace the applicable framework
with local equivalents (e.g., Torrens title for Australia/New Zealand/Canada, deeds
registry for South Africa, Grundbuch for Germany). Engage local counsel for any
jurisdiction not covered here.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis (e.g., lender's vs. owner's review)
- A title exception's materiality depends on business context the user must supply
- Curative path selection requires information only the user has
- Gap period or timing constraints affect how to handle specific requirements

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

### Step 1: Accept the Document

Accept the title document in any of these formats:

- **File**: PDF, DOCX, or image of the title commitment / official copy of register entries
- **Pasted text**: Document text pasted directly into the conversation
- **URL**: Link to a document in a document management system or cloud storage

Identify the document type:

- **US ALTA Commitment**: Has Schedule A, Schedule B-I Requirements, and Schedule B-II Exceptions
- **US California Preliminary Report**: Has Schedule A and combined Schedule B (requirements + exceptions)
- **UK Official Copy of Register Entries (OC1/OC2)**: Has Property Register (A), Proprietorship Register (B), and Charges Register (C)
- **UK Official Search Certificate (OS1/OS2)**: Reveals pending applications and confers a search priority period
- **US Title Opinion Letter**: Attorney-issued narrative; no ALTA form; analyze as a narrative commitment
- **US Abstract of Title**: Historical chain-of-title summary; analyze for chain completeness and encumbrances

### Step 2: Gather Transaction Context

**⟁ CLARIFY** — Before beginning the review, ask the user these questions. Present as structured options:

1. **Transaction type?**
   - Options: Purchase (residential), Purchase (commercial), Refinance/Re-mortgage, Construction Loan, Sale (reviewing as seller), Exchange/1031, Leasehold financing, Other
   - _Why this matters_: Endorsement requirements, curative priorities, and closing checklist items differ substantially by transaction type.

2. **Which side are you representing?**
   - Options: Buyer/Borrower, Seller, Lender only, Both buyer and lender (simultaneous issue), Neutral/escrow or transaction counsel
   - _Why this matters_: Risk tolerance for exceptions and responsibility for curative actions differ by side.

3. **Owner's policy, Lender's policy, or both?**
   - Options: Owner's policy only, Lender's (loan) policy only, Both simultaneous issue, Not yet decided
   - _Why this matters_: Certain standard exceptions can be deleted for extended ALTA owner's coverage but not lender's; policy amounts and insureds differ.

4. **Property type?**
   - Options: Single-family residential, Multi-family residential (2-4 units), Multi-family (5+), Commercial office/retail/industrial, Mixed-use, Raw land/vacant, Condominium/co-op, Planned Unit Development (PUD), Agricultural, Special-purpose
   - _Why this matters_: Specific endorsements are triggered by property type (ALTA 4.1 condo, ALTA 5.1 PUD, ALTA 3.1 zoning for commercial).

5. **Is there a current survey?**
   - Options: Yes — ALTA/NSPS survey ordered or available, Yes — older boundary survey only, No survey, Survey in progress
   - _Why this matters_: Determines whether the survey exception can be deleted and whether the ALTA 25 (Same as Survey) endorsement applies.

6. **When is closing scheduled?**
   - Options: Imminent (< 7 days), Near-term (7–30 days), Standard (30–60 days), Flexible / no hard deadline
   - _Why this matters_: Gap period risks, IRS discharge timelines, and curative lead times affect urgency classification and whether closing can proceed on schedule.

### Step 3: Load Legal Authority

Use **legalcode-mcp** to gather jurisdiction-relevant legal authority before analyzing the commitment:

**For US transactions:**

- Recording act priority rules for the applicable state (race, notice, or race-notice)
- State-specific mechanic's lien statutes: perfection period, notice requirements, bond-over procedures
- Federal tax lien statutes: 26 U.S.C. § 6321; IRS Certificate of Discharge procedures [VERIFY]
- State homestead exemption statutes (relevant to judgment lien priority)
- Lis pendens filing requirements and effect under the recording act
- RESPA § 2607 affiliated business disclosures [VERIFY]

**For UK transactions:**

- Land Registration Act 2002 ss.11, 12, 29–31 (priority and effect of registration) [VERIFY]
- LRA 2002 Schedule 3 (overriding interests binding on registered dispositions) [VERIFY]
- Law of Property Act 1925 s.44 (root of title for unregistered land) [VERIFY]
- Land Charges Act 1972 (classes of registrable land charges) [VERIFY]
- Family Law Act 1996 s.31 (home rights notices) [VERIFY]

Save results to `/tmp/legalcode-title-authority.md`.

**If legalcode-mcp is not connected:**

- Mark all statutory references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with analysis using general title law knowledge; flag all jurisdiction-specific rules for independent verification

### Step 4: Schedule A Review (US) / Title Register Header Review (UK)

#### US Schedule A

Verify each Schedule A item and flag discrepancies:

| Item                            | What to Check                                     | Flag If                                                                                                                |
| ------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Commitment / Effective Date** | Recency of the title search                       | > 30 days old before closing; commitment typically expires 180 days from effective date [VERIFY]                       |
| **Policy Amount(s)**            | Owner's = purchase price; Lender's = loan amount  | Either is blank, zero, or inconsistent with the PSA or loan commitment                                                 |
| **Proposed Insured(s)**         | Name(s) exactly match the purchase/loan documents | Name discrepancy (LLC name misspelled, individual missing middle name or suffix)                                       |
| **Legal Description**           | Matches the deed, purchase agreement, and survey  | Any discrepancy between documents; description references a plat not attached                                          |
| **Title Vested In**             | Current owner of record                           | Discrepancy with tax records, deeds on file, or the seller's name in the PSA                                           |
| **Estate Insured**              | Fee simple vs. leasehold                          | Leasehold triggers additional review of ground lease terms, term remaining, and lender's leasehold policy requirements |

**⟁ CLARIFY** — If the legal description differs between the commitment and the purchase agreement: classify as OBJECT and ask the user whether a survey or prior deed is available to reconcile the discrepancy, or whether this should be treated as a blocking defect requiring a corrective deed.

#### UK Title Register Header Review

| Register                  | What to Check                                               | Flag If                                                                       |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Title Number**          | Unique HMLR reference; matches the application              | Mismatch with conveyancing title                                              |
| **Title Grade**           | Absolute (best) vs. Good Leasehold / Possessory / Qualified | Any grade below Absolute requires investigation (see table below)             |
| **Registered Proprietor** | Name, address, and any co-ownership notes                   | Mismatch with seller; offshore entity or trust ownership; trustee discrepancy |
| **Property Description**  | Matches contractual description and filed title plan        | Discrepancy; area shown is inconsistent with the agreed transaction           |
| **Registered Extent**     | Matches the filed plan within acceptable tolerance          | Boundary discrepancy                                                          |

**UK Title Grade Implications:**

| Grade              | Meaning                                                       | Required Action                                                                      |
| ------------------ | ------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Absolute**       | HMLR has examined and guarantees the title                    | Standard review                                                                      |
| **Good Leasehold** | Leasehold registered; freehold landlord's title not verified  | Investigate and verify freehold title; obtain evidence; consider indemnity insurance |
| **Possessory**     | Based on actual possession; prior adverse claims not excluded | Commission possessory title indemnity insurance; investigate history and occupation  |
| **Qualified**      | Subject to a specific exception stated on the register        | Read the stated qualification carefully; indemnity insurance likely required         |

### Step 5: Schedule B-I Requirements Analysis (US)

Schedule B-I lists conditions that must be satisfied before the title insurer will issue the policy. Every B-I item must have a curative action, a responsible party, and a deadline.

Analyze each requirement using the Curative Status system defined in the **Title Defect Severity Classification** section:

| Requirement Category             | Typical Items                                                                                     | Standard Curative Action                                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Payment**                      | Payment of purchase price; payoff of existing loans                                               | Funds confirmed at closing; payoff letters from all existing lenders                                                   |
| **Instrument execution**         | Deed from seller; mortgage/deed of trust from borrower                                            | Executed instruments delivered at closing                                                                              |
| **Existing lien payoffs**        | Existing mortgages, HELOCs, home equity loans                                                     | Payoff letters; fund payoffs from closing proceeds; record releases (Deed of Reconveyance or Satisfaction of Mortgage) |
| **Tax clearance**                | Delinquent taxes; special assessments                                                             | Obtain current tax certificates; pay arrears from sale proceeds                                                        |
| **Corporate / entity authority** | Articles of organization; certificates of good standing; board resolutions; evidence of authority | Order from Secretary of State; draft and adopt required resolutions; confirm signatory authority                       |
| **Survey**                       | Current ALTA/NSPS survey meeting 2021 Minimum Standards                                           | Commission survey; surveyor provides certification meeting the 2021 Standards                                          |
| **Affidavit of title**           | Seller's affidavit covering mechanic's liens, tenancies, possession                               | Seller executes at closing using title company form                                                                    |
| **FIRPTA compliance**            | Certification of non-foreign status (26 U.S.C. § 1445) [VERIFY]                                   | Seller executes FIRPTA affidavit; or withholding agent obtains withholding certificate from IRS                        |
| **Gap coverage**                 | Instructions to record promptly; gap affidavit                                                    | Record deed and mortgage simultaneously at closing; obtain gap affidavit from seller                                   |
| **Probate / estate matters**     | Letters testamentary; court order authorizing sale                                                | Obtain letters; court confirmation order if required by state law [JURISDICTION-SPECIFIC]                              |
| **Mechanic's liens**             | Release of filed mechanic's / materialmen's lien                                                  | Lienor executes release of lien; record; OR post a surety bond to release the property                                 |
| **UCC fixture filings**          | Termination of UCC-1 fixture filing by existing lender                                            | Existing secured party files UCC-3 termination statement                                                               |

**⟁ CLARIFY** — For any B-I item involving a third-party action (IRS discharge, court order, government clearance, existing lender payoff): ask the user whether the action has been initiated and what the current status is. Third-party timelines can derail closings that do not account for them early.

### Step 6: Schedule B-II Exceptions Analysis (US)

Schedule B-II lists what the title policy will not cover. Analyze each exception and classify it using the four-tier system in the **Title Defect Severity Classification** section.

#### Standard Exceptions — Often Deletable with Extended Coverage

These five standard exceptions appear in virtually every commitment. They can often be deleted with a current ALTA/NSPS survey and extended coverage endorsements:

| Standard Exception                   | Description                                 | How to Delete                                                                              |
| ------------------------------------ | ------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Rights of parties in possession**  | Unrecorded tenants or adverse possessors    | Survey + physical inspection + tenant estoppel certificates                                |
| **Survey / encroachments exception** | Matters a current survey would disclose     | Current ALTA/NSPS survey showing no adverse matters; certify survey to the title company   |
| **Unrecorded easements**             | Easements not appearing in public records   | Survey confirming none; or ALTA 28 easement endorsement for specific relied-upon easements |
| **Unrecorded mechanic's liens**      | Liens for labor/materials not yet perfected | No-lien/gap affidavit from seller; confirm no recent construction work                     |
| **Taxes not yet due and payable**    | Current and future year taxes               | Buyer assumes; CLEAR — prorate at closing                                                  |

**⟁ CLARIFY** — Before classifying the survey exception: "Is an ALTA/NSPS survey being obtained for this transaction? If yes, the survey exception can likely be deleted and I'll identify what the survey needs to confirm. If no survey is planned, the exception will remain — should I evaluate whether that leaves unacceptable risk given the property type and transaction?"

#### Special Exceptions — Property-Specific Analysis

**A. Easements and Rights-of-Way**

| Type                                           | Analysis                                                                                                          | Curative or Endorsement                                                                             |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Utility easements (underground, perimeter)** | Acceptable if not under existing improvements; cross-check against survey and building footprint                  | ALTA 9 endorsement; confirm on survey                                                               |
| **Access / ingress-egress easement**           | Beneficial to property: CLEAR. Burden on property: analyze scope, exclusivity, and interference with proposed use | ALTA 17 access endorsement if insuring property relies on easement for access                       |
| **Drainage easements**                         | Check whether easement restricts the buildable area                                                               | Engineering review if easement covers proposed development footprint                                |
| **Prescriptive easements claimed**             | Assert claim was never established or has been abandoned; require evidence                                        | Quitclaim deed from adverse party; affidavit of non-use; indemnity title policy as fallback         |
| **Railroad / utility corridor rights-of-way**  | Fee or easement? Ownership of abandoned corridor?                                                                 | Survey; confirm whether easement has terminated by abandonment; state law on rail corridor reverter |
| **Conservation easements**                     | Permanent use restrictions on development; held by government or land trust                                       | Review scope carefully; FATAL for development if it covers the proposed development area            |

**B. Liens and Financial Encumbrances**

| Lien Type                                   | Priority                                                         | Curative Action                                                                    | Timing Notes                                                                          |
| ------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Current year property taxes**             | Super-priority in most states                                    | Prorate and pay at closing; CLEAR                                                  | Confirm amount from tax collector; verify no special assessments                      |
| **Prior year delinquent taxes**             | Super-priority                                                   | Pay in full from closing proceeds; require current tax certificate                 | CURATIVE; straightforward if funds available                                          |
| **Federal tax lien (IRS)**                  | Attaches to all property of taxpayer — 26 U.S.C. § 6321 [VERIFY] | IRS Certificate of Discharge (Form 14135 process) or Subordination; or full payoff | Allow 30–90 days for IRS processing; initiate early                                   |
| **State tax lien**                          | Varies by state                                                  | State agency release; payoff from proceeds                                         | State-specific procedures [JURISDICTION-SPECIFIC]                                     |
| **Judgment lien**                           | Files from docket date; priority from recording date             | Release/satisfaction from judgment creditor                                        | Identify creditor; confirm homestead exemption if applicable [JURISDICTION-SPECIFIC]  |
| **HOA / CID assessment lien**               | Often super-priority for recent assessments [VERIFY state law]   | Obtain HOA payoff statement; pay from closing proceeds                             | ALTA 5.1 PUD or ALTA 4.1 condo endorsement                                            |
| **Mechanic's / materialmen's lien**         | Super-priority in most states for improvement work               | Pay lien amount; lienor executes release; record; OR post surety bond              | Super-priority can beat a recorded mortgage; address immediately                      |
| **Deed of trust / mortgage to be released** | Senior lien; must be released at closing                         | Payoff letter + Deed of Reconveyance or Satisfaction of Mortgage                   | Record release before or simultaneously with new instruments                          |
| **UCC fixture filing**                      | Covers personal property components                              | UCC-3 termination by existing secured party                                        | Review scope of fixtures; confirm no gap in coverage                                  |
| **Lis pendens**                             | Notice of pending litigation on title                            | Obtain court order dismissing or vacating lis pendens                              | OBJECT or FATAL depending on the underlying litigation; title company will not insure |

**C. Covenants, Conditions, and Restrictions (CC&Rs / Restrictive Covenants)**

| Issue                               | Analysis                                                                                     | Action                                                                                                                |
| ----------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **HOA CC&Rs**                       | Review use restrictions, architectural controls, right of first refusal, transfer fees       | Obtain HOA docs; confirm compliance with intended use; flag any ROFR holder                                           |
| **Subdivision restrictions**        | Minimum setbacks, building materials, use limitations                                        | Confirm intended use complies; check enforcement by neighbors vs. HOA                                                 |
| **Historic district covenants**     | Preservation restrictions, FAR limits, façade controls                                       | Confirm compliance; government enforcement cannot be insured over                                                     |
| **Racially restrictive covenants**  | Void under Shelley v. Kraemer (1948) [VERIFY] and Fair Housing Act 42 U.S.C. § 3604 [VERIFY] | Note the void covenant; document-level correction where state law provides a process (e.g., Cal. Gov. Code § 12956.2) |
| **Environmental deed restrictions** | Prohibit residential use; restrict soil disturbance; groundwater use prohibitions            | FATAL for residential use if property is contaminated; Phase II ESA required before reclassification                  |
| **Right of first refusal**          | Third party has purchase priority right                                                      | OBJECT — obtain written ROFR waiver from holder before proceeding to closing                                          |

**D. Mineral Rights and Subsurface Interests**

| Issue                               | Analysis                                                                     | Action                                                                            |
| ----------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Prior mineral reservation**       | Surface vs. subsurface severed; does grantor or third party hold minerals?   | Confirm surface use rights not restricted; ALTA 35 mineral endorsement for lender |
| **Oil and gas lease**               | Active or terminated? Third-party extraction rights and surface entry rights | Review lease terms; confirm whether lease has expired or been released            |
| **Mining claims (federal / state)** | Federal patent or unpatented mining claim affecting the property             | Title company to review; may require BLM or state agency clearance                |

**E. Other Common Special Exceptions**

| Exception                                           | Analysis                                                 | Action                                                                          |
| --------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Pending assessment districts**                    | New public improvements resulting in special assessments | Review with municipality; factor into closing cost estimates                    |
| **Rights of way for public utilities (recorded)**   | Typically acceptable                                     | Confirm location on survey; verify not under building footprint                 |
| **Unrecorded leases / occupancy rights**            | Tenants in possession not yet documented                 | Obtain estoppel certificates; review lease terms; ALTA 9 endorsement for lender |
| **Reverter clauses**                                | Property reverts to grantor if stated condition violated | OBJECT — review condition carefully; may be FATAL for financing                 |
| **Rights of way reserved by grantor in prior deed** | Historical path, road, or access reserved                | Confirm scope on survey; verify whether active or abandoned                     |

### Step 7: UK Title Register / Pre-Registration Title Analysis

#### A Register — Property Register

| Entry Type                               | Analysis Points                                                                                                              |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Description of land**                  | Matches Land Registry title plan and contractual description?                                                                |
| **Easements benefiting the property**    | Identify appurtenant rights (access, drainage, services); confirm each still exists and has not been extinguished            |
| **Positive covenants**                   | Note: positive covenants do not bind successors at common law; check for indemnity chain or restriction requiring compliance |
| **Rights reserved in prior conveyances** | Rights of former owners to use the land; check impact on proposed use                                                        |

#### B Register — Proprietorship Register

| Entry Type                 | Analysis Points                                                                                                                                         |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Registered proprietor**  | Matches seller/borrower; check for corporate, trust, or overseas entity ownership requiring additional steps                                            |
| **Title grade**            | See Step 4 for grade analysis and required actions                                                                                                      |
| **Restrictions**           | Form A restriction (requires second trustee or trust corporation for overreaching); Form L (lender's consent); any special restriction — read carefully |
| **Cautions / inhibitions** | Older protective entries; investigate basis and whether removal is required                                                                             |

#### C Register — Charges Register

| Entry Type                                | Analysis Points                                                                                                                                            |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Registered legal charges (mortgages)**  | Must be discharged at completion; obtain DS1 or e-DS1 from lender; confirm redemption figures                                                              |
| **Equitable charges / notices**           | Are they being removed? May require application and/or court order                                                                                         |
| **Notices protecting third-party rights** | Home rights notices (FLA 1996 s.31); estate contract notices; option notices; unilateral notices — investigate each and confirm removal or compliance      |
| **Restrictive covenants (burden)**        | Assess enforceability under Tulk v Moxhay (1848) [VERIFY]; identify beneficiaries; consider indemnity insurance where benefit uncertain or covenant is old |
| **Easements and rights (burden)**         | Review scope; confirm compatible with proposed use and development plans                                                                                   |

#### Overriding Interests (Schedule 3 LRA 2002) — Bind the Buyer Without Appearing on the Register [VERIFY]

| Overriding Interest                        | Risk                                                                                    | Investigation and Mitigation                                                                      |
| ------------------------------------------ | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Persons in actual occupation** (para. 2) | Unregistered beneficial interest; occupying tenant under short lease; adverse possessor | Physical inspection; direct enquiry of all occupiers; review CPSE responses; occupation estoppels |
| **Legal leases ≤ 7 years** (para. 1)       | Short residential or commercial tenancy; periodic tenancy                               | Full inspection; tenancy agreement and rent roll review; confirm terms                            |
| **Legal easements and profits** (para. 3)  | Prescriptive or implied easements not on register                                       | CPSE enquiries; inspect for physical evidence of use (worn paths, pipes, cables)                  |
| **Franchise and manor rights**             | Rare; archaic                                                                           | Review historical title deeds if any reference to manor                                           |

#### UK Pre-Registration Title (Unregistered Land)

Where land is unregistered, investigate:

1. **Root of title**: Must be at least 15 years old under LPA 1925 s.44 [VERIFY]; ideally a conveyance on sale with full title guarantee.
2. **Chain of title**: Each link must be examined; identify missing links or wild deeds.
3. **Land Charges Search** (at HMLR Land Charges Department): search all estate owners in the chain for:
   - Class C(i): Puisne mortgage (legal mortgage not protected by deposit of title deeds)
   - Class C(iii): Limited owner's charge
   - Class C(iv): General equitable charge
   - Class D(i): Inland Revenue charge
   - Class D(ii): Restrictive covenant created after 1925
   - Class D(iii): Equitable easement created after 1925
   - Class F: Spouse's / civil partner's home rights (FLA 1996) [VERIFY]
4. **Trigger first registration** if the transaction is a registrable disposition under LRA 2002 s.4 [VERIFY].

#### UK Standard Property Searches — Recommend Alongside Title Review

| Search                             | Purpose                                                                                                  | When to Order                                                          |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Local Authority (LLC1 + CON29)** | Planning history, enforcement notices, road adoption, tree preservation orders, radon, contaminated land | All transactions                                                       |
| **CON29O Optional Enquiries**      | Pipelines, minerals, commons, drainage, road proposals                                                   | Advise client on relevant selections                                   |
| **Drainage and Water (CON29DW)**   | Sewer adoption, water main location, drainage connection rights                                          | All transactions                                                       |
| **Environmental Search**           | Contamination, flood risk, mining history, natural subsidence                                            | All transactions; essential for industrial/commercial                  |
| **Chancel Repair Search**          | Potential liability for historic chancel repair                                                          | Unregistered land; registered land purchased pre-October 2013 [VERIFY] |
| **Mining Search**                  | Coal Authority, potash, tin, china clay, brine                                                           | Relevant geographic areas                                              |

### Step 8: Gap Coverage Analysis

The **gap period** is the time between the effective date of the title search and the date the closing documents are recorded. During the gap, new liens can be filed (IRS levy, judgment, mechanic's lien), lis pendens can be docketed, and a prior conveyance can be recorded if the seller made a fraudulent prior conveyance.

#### Gap Risk Assessment

| Risk Level   | Gap Period | Risk Factors                                                                  | Recommended Action                                                                           |
| ------------ | ---------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Low**      | < 7 days   | No known pending actions; no recent construction                              | Standard gap affidavit from seller; record same day as closing                               |
| **Moderate** | 7–30 days  | Recent construction completed; multiple sellers or complex entity structure   | Extended gap affidavit; confirm no new liens; bring-down search at or shortly before closing |
| **High**     | > 30 days  | Ongoing construction; known creditor issues; delayed closing; IRS involvement | Gap Endorsement (ALTA 16 or equivalent) [VERIFY availability]; interim bring-down required   |

#### Gap Curative Measures

1. **Record promptly**: Instruct title company to record deed and mortgage the same day as closing; confirm in closing instructions and escrow agreement.
2. **Affidavit of Title / Gap Affidavit**: Seller / borrower certifies no new conveyances, liens, or encumbrances since the commitment date.
3. **Gap Endorsement (ALTA 16)** [VERIFY form availability by state]: Extends title insurance coverage to the closing / recording date.
4. **Bring-Down Search**: Order a same-day or day-before bring-down of the title search to catch any instruments recorded after the original commitment.
5. **Construction Loan Specific**: Require no-lien affidavits from general contractor and all subcontractors / materialmen; consider ALTA 14 (Future Advance) and ALTA 9 (restrictions, encroachments, mechanic's liens) endorsements.

### Step 9: Endorsements Assessment

Based on property type and transaction structure, recommend the appropriate endorsements. Confirm availability with the title underwriter in the applicable state.

| Endorsement                                            | Description                                                                               | Required For                                                                                      |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **ALTA 3.1 — Zoning**                                  | Insures property zoning classification and permitted use                                  | Commercial, multi-family, mixed-use, any transaction where zoning compliance matters              |
| **ALTA 4.1 — Condominium**                             | Insures condo unit description, by-laws, and CC&Rs                                        | Condominium purchase or refinance                                                                 |
| **ALTA 5.1 — Planned Unit Development**                | Insures PUD status and HOA obligations                                                    | PUD transactions                                                                                  |
| **ALTA 6.2 — Variable Rate Mortgage**                  | Protects lender for future rate adjustments                                               | ARM and variable-rate loans                                                                       |
| **ALTA 8.1 — Environmental Protection Lien**           | Insures lender against environmental super-priority liens                                 | Commercial and industrial transactions                                                            |
| **ALTA 9 — Restrictions, Encroachments, Minerals**     | Insures against CC&R violations, encroachments, and mineral rights claims                 | Commercial; residential when survey obtained                                                      |
| **ALTA 14 — Future Advance**                           | Protects future advances under revolving or construction credit                           | Construction loans; revolving credit facilities                                                   |
| **ALTA 16 — Gap**                                      | Extends coverage from commitment effective date to recording date                         | Transactions with gap risk; delayed recording                                                     |
| **ALTA 17 — Access and Entry**                         | Insures legal, physical, and vehicular access to the property                             | Any property where access depends on easements or where access is not directly from a public road |
| **ALTA 18.1 — Multiple Tax Parcels**                   | Insures where insured land spans multiple tax parcel numbers                              | Large commercial; assembled parcels                                                               |
| **ALTA 19.1 — Contiguity**                             | Insures multiple parcels are contiguous                                                   | Assembled parcels; phased development                                                             |
| **ALTA 22 — Location**                                 | Certifies that the property address corresponds to the legal description                  | Commercial; any transaction where address and description discrepancy is a concern                |
| **ALTA 25 — Same as Survey**                           | Insures consistency of legal description with the ALTA/NSPS survey                        | Any transaction with a current ALTA survey                                                        |
| **ALTA 28 — Easement**                                 | Insures that a specific easement is not extinguished and is enforceable                   | Transactions relying on an appurtenant easement for access or utility service                     |
| **ALTA 35 — Minerals and Other Subsurface Substances** | Insures against loss from subsurface mineral extraction by record owner of mineral estate | Areas with active or reserved mineral rights; energy-producing states                             |
| **ALTA 36 — Energy Project**                           | Covers energy project-related easements and rights                                        | Wind, solar, and energy infrastructure projects                                                   |

[JURISDICTION-SPECIFIC] State endorsement forms may differ from ALTA national forms:

- **California**: Use CLTA endorsement forms; verify ALTA equivalents are filed with CDI.
- **Texas**: Use TDI-approved forms (Form T-series); confirm availability with TLTA underwriter.
- **New York**: TIRSA-approved forms; confirm availability with title company's NY counsel.

**⟁ CLARIFY** — For commercial transactions: "Would you like me to recommend a comprehensive endorsement package based on the property type, transaction structure, and exceptions identified? I can include coverage analysis for each endorsement."

### Step 10: Curative Action Plan

For each CURATIVE or OBJECT item identified in Steps 4–9, generate a curative action entry using the format in the **Curative Action Framework** section below.

For each FATAL item: notify all parties immediately, explain the specific defect, and identify the resolution path (if any) or confirm that closing cannot proceed.

### Step 11: Quality Verification and Closing Checklist

Before delivering output:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every FATAL-classified item, run the 3-pass Self-Interrogation.
3. Assign Confidence Scores to each material finding.
4. Verify all B-I requirements have been addressed with a curative action and responsible party.
5. Verify all B-II exceptions have been classified and actioned (no exception left as "TBD").
6. Confirm that the recommended endorsements are available in the applicable state.
7. Generate the Glass Box Audit Trail and append it to the output.

---

## Title Defect Severity Classification

### CLEAR — No Action Required

The item is standard, acceptable, and does not represent a risk to title or the proposed use of the property.

**Examples:**

- Current year property taxes (buyer assumes on a prorated basis at closing)
- Utility easements along the perimeter of the lot confirmed not under improvements
- Standard CC&Rs with use restrictions compatible with the buyer's intended use
- Prior deeds of trust being paid off at closing (payoff letter obtained)

**Action**: Note in the closing checklist as "CLEAR — no action required."

### CURATIVE — Action Required Before Closing

The item must be resolved before the title policy can be issued. Curative actions are typically ministerial (payoff, document execution, recording of a release) but have a definite deadline.

**Examples:**

- Existing mortgage being paid off at closing (payoff letter required; release to be recorded)
- Delinquent property taxes (must be paid from closing proceeds)
- Missing corporate resolution from LLC seller (must be delivered before closing)
- Mechanic's lien filed for recent construction (must be paid or bonded over)
- Judgment lien against seller (must be paid, or confirm homestead exemption applies)

**Action**: Generate a curative action entry with responsible party, instruments needed, and deadline.

### OBJECT — Material Title Objection

The item creates a meaningful cloud on title, is not acceptable as-is, and cannot be resolved by standard closing procedure. Requires negotiation with the seller, special exception removal, or endorsement.

**Examples:**

- Prescriptive easement claim asserted by adjacent landowner (no release available)
- CC&R provision inconsistent with buyer's intended use (e.g., prohibits commercial use)
- Environmental deed restriction limiting residential use where buyer intends residential
- Right of first refusal not waived by the holder
- Federal tax lien requiring IRS Certificate of Discharge (not yet requested)
- Prior conveyance in chain of title not properly acknowledged or released

**Action**: Issue a formal title objection; specify curative alternatives; assign deadline for seller to cure; classify as Tier 1 or Tier 2.

### FATAL — Non-Insurable Title Defect

The item cannot be insured over and may prevent issuance of a clean title policy. The transaction cannot proceed until the defect is resolved.

**Examples:**

- Lis pendens of a lawsuit directly challenging the seller's ownership or the transaction
- Missing link in the chain of title with no recorded deed and no curative instrument available
- Deed in the chain executed by a grantor under legal incapacity with no ratification
- Environmental restriction absolutely prohibiting the proposed use with no variance or correction path
- Outstanding bankruptcy automatic stay (11 U.S.C. § 362) preventing the conveyance [VERIFY]
- Active federal tax lien that the IRS has declined to discharge or subordinate

**Action**: Notify all parties immediately. Advise that closing cannot proceed. Specify the resolution path if one exists; advise on timeline realistically.

---

## Curative Action Framework

For each CURATIVE, OBJECT, or FATAL item:

```
**Exception / Requirement**: [Reference number or description from the commitment]
**Classification**: CLEAR / CURATIVE / OBJECT / FATAL
**Type**: Lien | Easement | Covenant | Document Gap | Entity / Authority | Survey | Gap Risk | Other
**Description**: [What the commitment or register states]
**Risk if not resolved**: [Consequence — loss of coverage, cloud on title, closing failure, IRS action]
**Curative action**: [Precise steps, in order]
**Instruments needed**: [Specific instruments — Deed of Reconveyance, Release of Lien, IRS Certificate of Discharge, Corporate Resolution, etc.]
**Responsible party**: Seller | Buyer | Lender | Title Company | [Named Third Party: specify]
**Deadline**: Before closing | Before title update / bring-down | Before recording | [Specific date]
**Alternatives**: [If primary cure path fails, what are the fallback options?]
**Tier**: 1 (Blocking) | 2 (Material) | 3 (Administrative)
**Confidence**: Definite (0.95–1.0) | High (0.80–0.94) | Probable (0.60–0.79) | Possible (0.40–0.59) | Unlikely (0.0–0.39)
```

### Curative Instruments Quick Reference

| Instrument                                 | Purpose                                                                                          | Executed / Filed By                                    |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| **Deed of Reconveyance**                   | Releases deed of trust after payoff (trustee reconveys to borrower)                              | Trustee at lender's written request                    |
| **Satisfaction of Mortgage**               | Releases mortgage after payoff (mortgage-state jurisdictions)                                    | Lender; recorded by title company                      |
| **Release of Lien**                        | Releases mechanic's / materialmen's lien                                                         | Lien claimant (contractor, supplier)                   |
| **Lien Bond / Surety Bond**                | Bonds over a mechanic's lien, releasing the property from the lien                               | Bonding company; posted by owner or contractor         |
| **IRS Certificate of Discharge**           | Releases specific property from federal tax lien                                                 | IRS (Form 14135 process); allow 30–90 days [VERIFY]    |
| **IRS Certificate of Subordination**       | Subordinates federal tax lien to lender's mortgage                                               | IRS; allow 30–90 days [VERIFY]                         |
| **Judgment Satisfaction / Release**        | Releases judgment lien                                                                           | Judgment creditor; filed with court clerk and recorded |
| **Corrective Deed**                        | Corrects description, party name, or execution error in a prior deed                             | Original grantor of the deed being corrected           |
| **Quitclaim Deed**                         | Transfers any interest held; used to release easement claims, adverse interests                  | Adverse claimant or easement holder                    |
| **Affidavit of Title (No-Lien Affidavit)** | Seller's sworn statement: no new encumbrances, no unrecorded interests, no parties in possession | Seller; executed at closing                            |
| **FIRPTA Affidavit**                       | Certifies seller is not a foreign person; avoids withholding requirement                         | Seller (or withholding agent for foreign seller)       |
| **Corporate / LLC Resolution**             | Authorizes entity to enter transaction and designates authorized signatories                     | Entity's governing body (board, members, manager)      |
| **DS1 / e-DS1 (UK)**                       | Discharge of registered legal charge (mortgage)                                                  | Lender's solicitor via HMLR e-Discharge portal         |
| **Form RX3 (UK)**                          | Application to cancel a restriction on the register                                              | Registered proprietor with supporting evidence         |
| **Form AP1 (UK)**                          | Application to change the register (transfer, charge, restriction)                               | Buyer's / lender's solicitor                           |

---

## Prioritization Framework

### Tier 1 — Blocking Items (Closing Cannot Proceed Without Resolution)

- FATAL defects of any kind
- B-I requirements that have not been and cannot be satisfied within the closing timeline
- Any unvacated lis pendens or automatic stay [VERIFY]
- Environmental restrictions absolutely prohibiting the proposed use with no cure path
- Missing or unenforceable deed in the chain of title
- Outstanding probate matter with no court authorization to sell
- Right of first refusal not waived and ROFR holder exercising the right

### Tier 2 — Material Items (Must Resolve Before Closing; Resolution Path Exists)

- Existing mortgages and deeds of trust (payoff letters required; releases to be recorded)
- Delinquent property taxes (pay from closing proceeds)
- Filed mechanic's or materialmen's liens (pay or bond over)
- Federal or state tax liens (IRS discharge or subordination in process)
- Judgment liens where creditor is cooperating with a release
- Missing corporate authority documents (in process of being obtained)
- Environmental deed restrictions requiring Phase II clearance
- Easements that require endorsement (ALTA 17, 28) or survey confirmation

### Tier 3 — Administrative / Monitoring Items

- Current year taxes (CLEAR — buyer assumes at closing)
- Standard utility easements not affecting the building footprint (CLEAR)
- CC&Rs confirmed acceptable for the intended use (CLEAR)
- Future assessment possibilities (note and monitor)
- Endorsement package to be obtained at closing (not blocking, but must be confirmed available)

**Priority instruction**: Resolve all Tier 1 items before setting a closing date. Confirm all Tier 2 items are in process before scheduling. Tier 3 items to be noted in the closing letter and monitored through recording confirmation.

---

## Quality Assurance Framework

### Citation Quality Gates

Run silently before delivering output. If any gate fails, revise before delivering.

| Gate           | Rule                                                                                                                                         | Fail Action                                              |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim (lien priority, exception interpretation, curative requirement) cites a specific statute, rule, or established practice    | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                                                                  | Fix format                                               |
| **Currency**   | Every cited statute or regulation checked for amendment or repeal                                                                            | Flag "[CHECK CURRENCY — verify current version]"         |
| **Domain**     | Analysis stays within the applicable jurisdiction; no cross-jurisdictional bleed (e.g., applying ALTA analysis to a UK Land Registry matter) | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated; do not present a speculative curative path as certain                                                         | Add confidence qualifier                                 |

### Self-Interrogation for FATAL Items

For any item classified as FATAL, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the FATAL classification follow logically from the specific defect? Would a reasonable title underwriter in this jurisdiction actually refuse to insure? Is there a curative path I have not considered (curative statute, quiet title action, indemnity insurance, court order)?

**Pass 2 — Completeness**: Have all relevant statutes, curing procedures, and title insurance practice guides been considered? Are there state-specific curative mechanisms (e.g., limitations period that has run on an old adverse claim; curative recording act)?

**Pass 3 — Challenge**: What is the strongest argument that this defect IS insurable or curable? Has a title examiner ever insured over a similar defect with a specific exception, endorsement, or underwriting approval? Under what circumstances might the defect be less material than it appears?

Revise before delivery if any pass reveals the FATAL classification needs adjustment. Mark audit trail as `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                                                 | Action                                                                    |
| ------------ | --------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled title law; lien release is complete; clear recording act result | State with confidence                                                     |
| **High**     | 0.80–0.94 | Strong authority; minor procedural questions remain                     | State with brief caveat                                                   |
| **Probable** | 0.60–0.79 | Good analysis but fact-specific; curative path has open steps           | State with reasoning; flag remaining steps                                |
| **Possible** | 0.40–0.59 | Genuinely uncertain; depends on court / IRS / third-party action        | Flag for title counsel review with both risk factors and curative options |
| **Unlikely** | 0.0–0.39  | Speculative; no established curative path                               | Do not assert; flag as "[UNCERTAIN — title counsel to advise]"            |

---

## Glass Box Audit Trail

Every title review output must include this audit section:

```yaml
glass_box:
  skill_name: "legalcode-title-review"
  document_type: "ALTA 2021 Commitment / UK Official Copy of Register Entries / CA Prelim Report / Title Opinion / Other"
  property_address: "[Property address or parcel identifier]"
  effective_date: "[Title search effective date]"
  transaction_type: "[Purchase / Refinance / Construction / Other]"
  user_side: "[Buyer/Borrower / Seller / Lender / Escrow]"
  policy_type: "[Owner's / Lender's / Simultaneous Issue / Not determined]"
  jurisdiction: "[State + County (US) / UK county / Other]"
  b1_requirements_reviewed: "[number]"
  b1_open_items: "[number]"
  b2_exceptions_reviewed: "[number]"
  exceptions_classified:
    clear: "[number]"
    curative: "[number]"
    object: "[number]"
    fatal: "[number]"
  endorsements_recommended: "[list or 'None recommended']"
  gap_risk: "Low / Moderate / High"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no FATAL items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or matters not reviewed]"
  reviewer: "AI-assisted — requires review by qualified real estate attorney or title counsel"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in title commitment or title register review:

1. **Accepting all standard exceptions without analysis** — Standard exceptions (rights of parties in possession, survey exception, unrecorded easements) are often deletable with a current survey and extended coverage. Failing to flag these for deletion leaves the client with less coverage than available.

2. **Not identifying the search period behind the commitment** — The commitment is only as good as the title search behind it. A 40-year search may miss a 50-year old cloud. Always ask what period the search covers and whether any periods were not fully examined.

3. **Treating all liens as equally urgent** — A current-year tax lien is CLEAR; a federal tax lien requiring IRS discharge may take 45–90 days. Failing to triage by urgency and cure timeline causes missed deadlines and failed closings.

4. **Curative checklist without responsible parties and deadlines** — Every item must have an owner. A checklist that says "obtain lien release" without assigning responsibility to the seller and setting a deadline is not actionable.

5. **Ignoring the gap period** — Closing without addressing the gap exposes the buyer to liens filed between the title search date and recording. This is especially acute in jurisdictions without automatic gap protection under the recording act.

6. **Missing entity authority issues** — When a seller or borrower is an entity, failing to verify existence, good standing, authorized signatories, and required resolutions can void the instruments executed at closing.

7. **Assuming ALTA endorsements are available in all states** — ALTA national endorsements are not approved by all state insurance regulators. In California, Texas, and New York, different form sets apply. Always confirm endorsement availability with the title underwriter.

8. **Classifying racial covenants as blocking defects** — Racially restrictive covenants are void and unenforceable (Shelley v. Kraemer; FHA). They do not affect title as a blocking matter. Note them; pursue statutory correction where available; do not treat as a FATAL defect.

9. **Failing to require a bring-down search** — Ordering a title search only at the start of a transaction and not at or shortly before closing allows late-filed liens, lis pendens, and conveyances to go undetected.

10. **Not distinguishing CLTA from ALTA coverage** — CLTA standard coverage leaves standard exceptions in place; ALTA extended coverage deletes them with a survey. Failing to identify which policy type is issued and whether extended coverage is available leads to underinsurance.

11. **Ignoring easements because they appear on every report** — A utility easement through the center of the proposed building footprint is not just a "standard exception." Cross-reference every easement against the survey to confirm it does not interfere with the proposed use or existing improvements.

12. **Treating federal tax liens as simple payoffs** — Federal tax liens require an IRS Certificate of Discharge or Subordination — not merely payment. The IRS process takes 30–90 days and is not guaranteed. Identify early and initiate promptly.

13. **Overlooking overriding interests (UK)** — UK title register review that ignores Schedule 3 LRA 2002 overriding interests (especially persons in actual occupation) misses the most significant source of unregistered equitable claims. A physical inspection and direct inquiry of occupiers is non-negotiable.

14. **Single-pass reading of the commitment** — B-II exceptions and B-I requirements are linked. A B-II exception (existing mortgage) is the same item as a B-I requirement (payoff of existing mortgage). Read the whole commitment before classifying individual items; cross-check B-I and B-II for consistency.

15. **Missing mineral rights severance** — In states with active energy sectors (Texas, Oklahoma, North Dakota, Colorado, Pennsylvania, West Virginia), mineral rights are routinely severed from surface rights. A deed conveying "surface rights only" without a mineral endorsement or severance analysis leaves the buyer exposed.

16. **Failing to address the right of first refusal** — An outstanding, unwaived ROFR must be obtained before the sale can proceed. The ROFR holder can void the transaction after closing if not properly waived.

17. **Not reviewing environmental deed restrictions against the intended use** — Environmental deed restrictions limiting use to commercial/industrial are FATAL for a residential transaction. Cross-check every deed restriction against the buyer's intended use before classifying.

---

## Writing Standards

Apply plain-language discipline to all output:

**For the closing checklist:**

- Use action verbs: "Obtain payoff letter from [lender name]" not "Payoff letter should be obtained"
- Name the actor: "Seller's counsel to deliver executed resolution by [date]"
- Specify instruments precisely: "Deed of Reconveyance from [Trustee name]" not "Release of lien"
- Include hard dates: "Must be recorded by [closing date]" not "prior to closing"

**For title objection descriptions:**

- State the specific risk in one sentence: "This exception allows [party] to [claim], which would [specific harm to buyer/lender]"
- Reference the specific exception number from the commitment
- Avoid legal jargon without explanation; define technical terms where used

**Quality gates before delivery:**

1. Can a non-attorney client understand what each curative item requires them to do?
2. Does each OBJECT-classified item have a specific proposed resolution path?
3. Is every legal claim backed by a citation or flagged [VERIFY]?
4. Is the closing timeline realistic given the curative actions and lead times required?
5. Are responsible parties identified for every open action item?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for state-specific recording acts, lien statutes, and title insurance regulations
- Verify FIRPTA withholding requirements and current dollar thresholds
- Confirm state-specific mechanic's lien perfection periods and bond-over procedures
- Verify federal tax lien discharge procedures (IRS Form 14135 process)
- Check for recent amendments to recording acts or title insurance statutes
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Flag all state-specific rules (lien periods, recording priorities, endorsement availability) for independent legal research
- Focus analysis on structural issues and obvious defects; note that legal citation accuracy requires independent verification

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Title Review Summary

**Document**: [Commitment number / HMLR title number / reference]
**Property**: [Address or parcel identifier]
**Effective Date**: [Title search / register effective date]
**Transaction**: [Purchase / Refinance / Development / etc.]
**Side Represented**: [Buyer/Borrower / Seller / Lender / Neutral]
**Policy Type**: [Owner's / Lender's / Simultaneous Issue]
**Jurisdiction**: [State + County / UK county]
**Date of Review**: [date]

---

## Critical Findings

[Top 3–5 issues — FATAL and OBJECT classifications — with one-line summaries and tier classification]

---

## Closing Checklist

### Tier 1 — Blocking Items (Closing Cannot Proceed Until Resolved)

| #   | Item          | Classification | Curative Action  | Responsible Party | Deadline |
| --- | ------------- | -------------- | ---------------- | ----------------- | -------- |
| 1   | [Description] | FATAL / OBJECT | [Specific steps] | [Party]           | [Date]   |

### Tier 2 — Material Items (In Process — Must Resolve Before Closing)

| #   | Item          | Classification | Curative Action  | Responsible Party | Deadline |
| --- | ------------- | -------------- | ---------------- | ----------------- | -------- |
| 1   | [Description] | CURATIVE       | [Specific steps] | [Party]           | [Date]   |

### Tier 3 — Administrative / Monitoring

| #   | Item          | Classification | Notes        |
| --- | ------------- | -------------- | ------------ |
| 1   | [Description] | CLEAR          | [Brief note] |

---

## Schedule B-I Requirements Status

| #   | Requirement   | Status                                    | Curative Action | Responsible | Deadline |
| --- | ------------- | ----------------------------------------- | --------------- | ----------- | -------- |
| 1   | [description] | OPEN / IN PROGRESS / SATISFIED / BLOCKING | [action]        | [party]     | [date]   |

---

## Schedule B-II Exceptions Analysis

### FATAL and OBJECT Exceptions

**Exception [#]: [Short description]**

- **Classification**: OBJECT / FATAL
- **Risk**: [Specific harm if not resolved]
- **Curative action**: [Precise steps in order]
- **Instruments needed**: [List]
- **Responsible**: [Party]
- **Deadline**: [Date or milestone]
- **Confidence**: [Level]

### CURATIVE Exceptions

[Same format]

### CLEAR Exceptions

| #   | Exception                   | Classification | Notes                                                  |
| --- | --------------------------- | -------------- | ------------------------------------------------------ |
| 1   | Current year property taxes | CLEAR          | Prorated at closing; confirm amount with tax collector |

---

## Gap Coverage Assessment

**Gap risk level**: [Low / Moderate / High]
**Gap period**: [Effective date] to [Expected recording date] ([X] days)
**Recommended gap measures**: [List]

---

## Recommended Endorsements

| Endorsement | Reason                                                                  | Priority                          |
| ----------- | ----------------------------------------------------------------------- | --------------------------------- |
| [ALTA 9]    | [Restrictions, encroachments — recommended given CC&Rs on the property] | Required / Recommended / Optional |

---

## Next Steps

[Prioritized action list with owners, instruments needed, and deadlines]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill covers US (ALTA/CLTA) and UK (Land Registration Act 2002) frameworks in depth. For other jurisdictions:

| Jurisdiction  | Title System                                                          | Key Differences                                                                                                 | Local Adaptation Required                                            |
| ------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Australia** | Torrens indefeasibility (state-based Land Titles Offices)             | Caveats instead of lis pendens; PEXA electronic lodgement; state transfer duty                                  | Replace with AU Torrens framework; engage state-specific conveyancer |
| **Canada**    | Mix of Torrens (BC, AB, SK, MB) and deed recording (ON, QC, Atlantic) | Province-specific Land Transfer Tax; Title Insurance (FCT/Stewart) becoming standard                            | Province-specific framework [JURISDICTION-SPECIFIC]                  |
| **Ireland**   | Land Registry (Registered) and Registry of Deeds (Unregistered)       | Registration of Title Act 1964; Property Registration Authority; LPTS e-registration                            | Separate Ireland conveyancing skill                                  |
| **Germany**   | Grundbuch (federal land register system)                              | Grundbuchauszug extract; Auflassung formality; notarial requirement for all transfers; Grundschuld vs. mortgage | German Grundbuch analysis framework                                  |
| **France**    | Publicité foncière / Service de la publicité foncière                 | Notarial transfer mandatory; état hypothécaire; droit de préemption; plus-values                                | French notarial due diligence framework                              |

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis combining:

- ALTA 2021 Commitment for Title Insurance forms and standards (effective July 1, 2021)
- ALTA endorsement framework (current 2006–2021 endorsement editions)
- UK Land Registration Act 2002 and Land Registration Rules 2003
- HM Land Registry Practice Guide series (PGs 1, 15, 18, 19, 40)
- US recording act priority analysis (race, notice, and race-notice states)
- Federal tax lien discharge procedures (IRS Code § 6321; Form 14135 process)
- Mechanic's lien statutes general principles across US states
- UK Law Society Conveyancing Protocol and Standard Conditions of Sale
- Reference structural patterns from legalcode-contract-review (reference standard) and
  legalcode-real-estate-due-diligence (sister skill, eight-workstream due diligence framework)

Research basis: web-backed legal research on ALTA commitment structure, Schedule B-I/II
analysis, gap coverage, endorsements, UK title register analysis, and curative title work
conducted during creation. All statutory citations should be independently verified against
current authoritative sources before reliance.
