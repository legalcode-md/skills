---
name: legalcode-iceland-real-estate-contracts
description: Generate and review Icelandic real estate contract documents including kauptilbod (bid agreements),
  kaupsamningur (purchase agreements), and kostnadaruppgjor (expense settlements). Use when drafting or
  reviewing real estate transaction documents for residential or commercial property purchases in Iceland.
  Covers all required elements under log nr. 40/2002 um fasteignakaup (Real Estate Purchase Act), integrates
  with HMS (Housing Financing Fund) loan requirements, and produces professionally formatted Word documents.
  Includes comprehensive terminology glossary and contract review checklist for identifying missing or
  unusual provisions. Jurisdiction-specific for Iceland with all Icelandic legal terminology preserved
  alongside English translations.
metadata:
  jurisdiction: Iceland
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Iceland Real Estate Contracts

> **Disclaimer**: This skill provides a framework for AI-assisted generation of Icelandic real
> estate contract documents. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional (logfraedingur) or licensed real estate agent (loggildur
> fasteignasali) in Iceland before use. Laws change; verify current applicability under Icelandic
> law before relying on any provision described here. Statutory and case law references cited
> from memory carry hallucination risk - verify against authoritative sources (Althingi,
> Syslumadur, HMS) before relying on them.

---

## Purpose and Scope

This skill generates three types of Icelandic real estate contract documents:

1. **Kauptilbod** (Bid Agreement / Offer) - The initial binding offer to purchase real estate
2. **Kaupsamningur** (Purchase Agreement) - The full purchase contract after offer acceptance
3. **Kostnadaruppgjor** (Expense Settlement) - The cost allocation document for transaction fees

**Covers:**

- Complete document generation with all legally required sections
- Party information (seljandi/seller, kaupandi/buyer) with kennitala (Icelandic ID)
- Property details (fastanumer, merking, landnumer, fasteignamat, brunabotamat)
- Payment schedules (greidslutilhogun) including cash and loan components
- HMS hlutdeildarlán (equity loan) integration for first-time buyers
- Standard legal terms (skilmalar) compliant with log nr. 40/2002
- Stamp duty (stimpilgjald) and registration fee (thinglysingargjald) calculations
- Signature blocks with witness requirements
- **Contract review**: Checking existing contracts for missing sections, unusual clauses, or deviations from standard terms
- **Terminology reference**: Comprehensive glossary of Icelandic real estate contract phrases with exact legal formulations

**Does not:**

- Replace the need for professional legal review
- Provide legal advice on specific transactions
- Handle commercial real estate leases (husaleiga)
- Generate mortgage/loan documents (those come from lenders)
- Advise on tax implications beyond stamp duty

---

## Jurisdiction and Governing Law

This skill is **specific to Iceland** and generates documents governed by:

| Statute              | Full Name                          | Coverage                                            |
| -------------------- | ---------------------------------- | --------------------------------------------------- |
| **Log nr. 40/2002**  | Um fasteignakaup                   | Real Estate Purchase Act - primary governing law    |
| **Log nr. 48/2003**  | Um neytendakaup                    | Consumer Purchase Act - applies to new construction |
| **Log nr. 99/2004**  | Um solu fasteigna og skipulagsloda | Real Estate Agent Act                               |
| **Log nr. 31/1993**  | Hjuskaparlog                       | Marriage Act - spousal consent requirements         |
| **Log nr. 140/2018** | Um adgerdir gegn peningathvaetti   | Anti-money laundering requirements                  |

**Key regulatory bodies:**

- **Syslumadur** (District Commissioner) - handles thinglysinguna (registration)
- **HMS / Ibudalanasjodur** (Housing Financing Fund) - government mortgage lender
- **Thjodskra** (Registers Iceland) - property registry
- **FMR** (Fasteignamat rikisins) - official property valuation

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses with structured questions when:

- The transaction type affects document selection
- Party details are incomplete
- Payment structure needs clarification
- Special conditions or reservations apply
- HMS loan involvement changes requirements

Questions are marked with **CLARIFY** below. Present options with explanations of why each
matters for the transaction.

---

## Workflow

### Step 1: Determine Mode and Document Type

**CLARIFY** - Ask the user what they need:

**Mode A — Generate Documents**

1. **Kauptilbod only** - Initial bid/offer phase
   - _When to use_: Making an initial offer on a property
   - _What it produces_: Binding offer document with payment schedule and conditions

2. **Kaupsamningur only** - Full purchase agreement
   - _When to use_: Offer already accepted, need the formal purchase contract
   - _What it produces_: Complete purchase agreement with all legal terms

3. **Kostnadaruppgjor only** - Expense settlement
   - _When to use_: Closing/settlement phase, allocating transaction costs
   - _What it produces_: Cost breakdown for stamp duty, fees, and agency charges

4. **Full transaction set** - All three documents
   - _When to use_: Starting a new transaction from scratch
   - _What it produces_: Complete document package for the entire transaction

**Mode B — Review Existing Contract**

5. **Review a contract** - Analyze an existing document for completeness and issues
   - _When to use_: User has received a contract and wants to check it before signing
   - _What it produces_: Structured review report with RED/YELLOW flags
   - _Inputs accepted_: PDF file, Word document, pasted text, or image of contract
   - _Proceeds to_: **Contract Review Mode** section (skip Steps 2-6)

### Step 2: Gather Transaction Details

**CLARIFY** - Collect the following information. Ask for any missing items:

#### 2a. Property Information (Upplysingar um fasteign)

| Field                 | Icelandic Term   | Description                         | Example                          |
| --------------------- | ---------------- | ----------------------------------- | -------------------------------- |
| Property address      | Heiti fasteignar | Full address with postal code       | Bjarkarholt 17, 270 Mosfellsbaer |
| Property ID           | Fastanumer       | 7-8 digit property number           | 20017206                         |
| Marking               | Merking          | Unit designation                    | 030206                           |
| Land number           | Landnumer        | Land parcel number                  | 228369                           |
| Property valuation    | Fasteignamat     | Official assessed value             | 55.000.000 kr.                   |
| Fire insurance value  | Brunabotamat     | Fire insurance assessment           | 48.000.000 kr.                   |
| Property type         | Tegund eignar    | Apartment/house/land                | Ibudareign                       |
| Size                  | Flatarmal        | Square meters                       | 51,8 fm                          |
| Rooms                 | Herbergi         | Number of rooms                     | 2                                |
| Construction year     | Byggingarar      | Year built                          | 2023                             |
| Construction material | Byggingarefni    | Concrete/wood/etc.                  | Steypt                           |
| Building stage        | Byggingastig     | Construction completion stage (1-7) | 7                                |

#### 2b. Seller Information (Seljandi/Eigandi)

| Field             | Icelandic Term        | Description                         |
| ----------------- | --------------------- | ----------------------------------- |
| Name              | Nafn                  | Full legal name or company name     |
| ID number         | Kennitala             | 10-digit Icelandic ID (DDMMYY-XXXX) |
| Email             | Tolvupostfang         | Contact email                       |
| Phone             | Simi                  | Contact phone                       |
| Ownership share   | Hlutfall              | Percentage (100% if sole owner)     |
| Insurance company | Tryggingarf. seljanda | Current property insurance          |

#### 2c. Buyer Information (Kaupandi)

| Field             | Icelandic Term        | Description                      |
| ----------------- | --------------------- | -------------------------------- |
| Name              | Nafn                  | Full legal name                  |
| ID number         | Kennitala             | 10-digit Icelandic ID            |
| Email             | Tolvupostfang         | Contact email                    |
| Phone             | Simi                  | Contact phone                    |
| Ownership share   | Hlutfall              | Percentage share being purchased |
| Insurance company | Tryggingarf. kaupanda | Buyer's intended insurer         |

#### 2d. Transaction Details

| Field          | Icelandic Term     | Description                 |
| -------------- | ------------------ | --------------------------- |
| Purchase price | Kaupverd           | Total purchase price in ISK |
| Delivery date  | Afhendingardagur   | When possession transfers   |
| Contract date  | Dags. kaupsamnings | Date of purchase agreement  |
| Deed date      | Utgafa afsals      | When deed will be issued    |

### Step 3: Determine Payment Structure

**CLARIFY** - Ask about payment arrangements:

1. **Cash payments only** (Greidsla med millifaerslu fjar)
   - Payment at contract signing
   - Payment at delivery
   - Final payment (typically 60 days after delivery)

2. **Bank mortgage** (Lan fra vidurkenndri lanastofnun)
   - Loan amount
   - Lending institution

3. **HMS hlutdeildarlán** (Equity loan from Housing Financing Fund)
   - _Only available for_: First-time buyers or those who haven't owned property in 5 years
   - Loan amount (maximum varies by year and property)
   - Requires pre-approval from HMS

4. **Assumed mortgages** (Yfirtaka ahvilandi vedskulda)
   - Existing mortgages the buyer will assume

**For each loan component, determine:**

- Amount
- Lender
- Due date (typically at delivery unless specified)

### Step 4: Identify Special Conditions

**CLARIFY** - Ask about any special conditions (fyrirvari/serakvadi):

1. **HMS approval reservation** - Transaction contingent on HMS approving the property for
   hlutdeildarlán (required for new construction)

2. **Loan approval reservation** - Transaction contingent on buyer securing financing

3. **Sale of existing property** - Transaction contingent on buyer selling their current home

4. **Inspection reservation** - Contingent on satisfactory property inspection

5. **New construction notes** - For properties under construction:
   - Construction stage at delivery
   - Final inspection requirements
   - Common area completion status

6. **Encumbrances to be released** (Aflysing) - Existing mortgages seller must clear

### Step 5: Calculate Costs

Calculate transaction costs for the kostnadaruppgjor:

#### Stamp Duty (Stimpilgjald)

| Buyer Type                   | Rate                 | Notes                        |
| ---------------------------- | -------------------- | ---------------------------- |
| Individual - first purchase  | 0.4% of fasteignamat | 50% discount for fyrstu kaup |
| Individual - repeat purchase | 0.8% of fasteignamat | Standard rate                |
| Legal entity (ehf., hf.)     | 1.6% of fasteignamat | Higher rate for companies    |

**Calculation**: `[Fasteignamat] x [Rate] = Stimpilgjald`

#### Registration Fees (Thinglysingargjold)

| Item              | Fee                                                  |
| ----------------- | ---------------------------------------------------- |
| Per document      | 2.500 kr.                                            |
| Typical documents | 8-12 (purchase agreement, deed, mortgages, releases) |

**Calculation**: `[Number of documents] x 2.500 kr. = Thinglysingargjald`

#### Real Estate Agency Fee (Umsyslugjald fasteignasolu)

| Service           | Typical Range          |
| ----------------- | ---------------------- |
| Buyer service fee | 50.000 - 100.000 kr.   |
| Full commission   | 1-2% of purchase price |

### Step 6: Generate Documents

Based on the collected information, generate the requested documents using the Word templates.

#### Template Paths

```
templates/iceland-real-estate/
├── kauptilbod-template.docx       # Bid agreement
├── kaupsamningur-template.docx    # Purchase agreement
└── kostnadaruppgjor-template.docx # Expense settlement
```

#### Placeholder Replacement

Replace all `[PLACEHOLDER]` values in the templates with actual transaction data:

| Placeholder          | Data Source       |
| -------------------- | ----------------- |
| `[HEITI FASTEIGNAR]` | Property address  |
| `[POSTNUMER]`        | Postal code       |
| `[SVEITARFELAG]`     | Municipality      |
| `[FASTANUMER]`       | Property ID       |
| `[KENNITALA]`        | Party's kennitala |
| `[NAFN SELJANDA]`    | Seller name       |
| `[NAFN KAUPANDA]`    | Buyer name        |
| `[KAUPVERD]`         | Purchase price    |
| `[UPPHAED]`          | Amount values     |
| `[DAGSETNING]`       | Dates             |

---

## Document Structure Reference

### Kauptilbod (Bid Agreement) Structure

1. **Header** - Property name and postal number
2. **Upplysingar um fasteign** - Property details table
3. **Eigendur (Seljendur)** - Seller information
4. **Kaupendur** - Buyer information
5. **Kaupverd og afhending** - Price and delivery date
6. **A. Greidslutilhogun** - Cash payment schedule
7. **B. Lan** - Loan breakdown
8. **Lysing** - Property description narrative
9. **Skilmalar** - Standard legal terms (20 clauses)
10. **Aetladur kostnadur kaupenda** - Estimated buyer costs
11. **Tilbod rennur ut** - Offer expiration date/time
12. **Undirskriftir** - Signature blocks
13. **Vottar** - Witness attestation
14. **Fasteignasali** - Agent information

### Kaupsamningur (Purchase Agreement) Structure

1. **Header** - Price and property identification
2. **Party tables** - Seller and buyer with full details
3. **Key dates table** - Contract, delivery, release, deed dates
4. **Fasteignalysing** - Detailed property information
5. **Thinglyst skjol** - Registered documents on the property
6. **Lysing a kaupsamningi** - Contract description
7. **Kaupverd og greidslutilhogun** - Price breakdown
8. **A. Greidslutilhogun** - Payment instructions with bank details
9. **Skilmalar** - Full legal terms (24 clauses)
10. **Eftirtaldar ahvilandi vedskuldir** - Encumbrances to be released
11. **Signature section** with witness table

### Kostnadaruppgjor (Expense Settlement) Structure

1. **Header** - Property identification
2. **Fasteign table** - Property details with fasteignamat
3. **Party tables** - Seller and buyer
4. **Kostnadur vid kaupsamning** - Cost breakdown table
5. **Stimpil- og thinglysingargjold** - Government fee payment details
6. **Umsyslugjald fasteignasolu** - Agency fee payment details
7. **Signatures** - Seller, buyer, and agent

---

## Standard Legal Terms (Skilmalar) Reference

The kauptilbod and kaupsamningur include these standard clauses based on log nr. 40/2002:

### Binding Effect (Clauses 1-3)

- Offer binding until expiration
- Counter-offer terminates original offer
- Written acceptance creates binding contract

### Governing Law (Clause 4)

- Log nr. 40/2002 um fasteignakaup applies
- Deviations only as explicitly stated

### Property Condition (Clauses 5-8)

- Seller discloses encumbrances and restrictions
- Property meets requirements of fasteignakaupalog
- Used property not defective unless material impairment or culpable conduct
- Equipment and fixtures as inspected or per law/contract

### Disclosure (Clauses 9-10)

- Seller must disclose known material information
- Buyer cannot claim defects they knew or should have known

### Delivery (Clauses 11, 14-15)

- Clean delivery on agreed date
- Risk transfers at delivery
- Buyer takes possession and responsibility from delivery

### Payment and Interest (Clause 12)

- No interest on payments made on time
- Default interest (dráttarvextir) on late payments

### Mortgage Assumption (Clause 13)

- Buyer must notify creditors of assumption
- Obtain lender consent if required

### Documentation Review (Clause 16)

- Parties reviewed: thinglysingarvottord, FMR certificate, söluyfirlit
- These form part of the contract

### Registration (Clauses 17-18)

- Contract to be registered promptly
- Buyer pays stamp duty and registration fees
- Deviations from law must be explicit

### Encumbrance-Free Sale (Clause 19)

- Property sold free of undisclosed encumbrances

### Deed Entitlement (Clause 20)

- Buyer entitled to deed upon full performance

### Special Provisions (Clause 18 serakvadi)

- Any contract-specific deviations or conditions

### Marriage Act Compliance (Clause 23)

- Parties declare compliance with hjuskaparlog (spousal consent for family home)

---

## HMS Hlutdeildarlán Integration

When the transaction involves HMS equity loans, include these provisions:

### Eligibility Requirements

- First-time buyer OR no property ownership in past 5 years
- Property must be approved for hlutdeildarlán
- Buyer must have 5% personal funds
- Base loan from approved credit institution required

### Required Reservations (Fyrirvari)

```
Kauptilbod thetta er gert med theim fyrirvara ad seljandi fai eignina samthykkt sem
hlutdeildarlanseign hja HMS og skal thad liggja fyrir eigi sidar en 4 vikum fra
samthykki kauptilbods thessa, ella hafa badir adilar heimild til ad falla fra
tilbodi thessu an skadabota.

Kauptilbod thetta er gert med theim fyrirvara ad kaupandi fai umsokn sina fyrir
hlutdeildarláni samthykkta hja HMS og skal thad liggja fyrir eigi sidar en 4 vikum
fra samthykki kauptilbods thessa, ella hafa badir adilar heimild til ad falla fra
tilbodi thessu an skadabota.
```

### Interest Provisions for New Construction

For loans released after safety inspection but before full registration:

```
Greidist ny lan kaupanda ekki ut a gjalddaga skv. kauptilbodi thessu er samid um ad
greidslurnar beri almenna vexti overdtryggdra utlana skv. 4. gr. laga nr. 38/2001.
```

---

## Quality Frameworks

### Citation Quality Gates

Run these checks before delivering any document:

| Gate                     | Rule                                     | Fail Action                  |
| ------------------------ | ---------------------------------------- | ---------------------------- |
| **Kennitala Format**     | Must be DDMMYY-XXXX (10 digits)          | Reject invalid format        |
| **Fastanumer Format**    | Must be valid property ID from Thjodskra | Flag for verification        |
| **Fasteignamat Source**  | Must match official FMR valuation        | Mark [VERIFY] if unconfirmed |
| **Legal References**     | Must cite correct statute numbers        | Verify against Althingi      |
| **Calculation Accuracy** | All amounts must sum correctly           | Recalculate before delivery  |

### Self-Interrogation for High-Value Transactions

For transactions over 100.000.000 kr., apply additional review:

**Pass 1 - Legal Completeness**: Are all mandatory disclosures present? Is the spousal consent
clause appropriate given the property type?

**Pass 2 - Financial Accuracy**: Do all payment amounts sum to the purchase price? Are the
stamp duty calculations correct for the buyer type?

**Pass 3 - Risk Assessment**: Are there unusual conditions that should be flagged? Is the
delivery timeline realistic for the construction stage?

### Confidence Scoring

| Level        | Range     | Meaning                                 | Action                    |
| ------------ | --------- | --------------------------------------- | ------------------------- |
| **Definite** | 0.95-1.0  | All data verified, standard transaction | Proceed with delivery     |
| **High**     | 0.80-0.94 | Most data verified, minor gaps          | Deliver with notes        |
| **Probable** | 0.60-0.79 | Key data unverified                     | Flag [VERIFY] items       |
| **Possible** | 0.40-0.59 | Significant uncertainty                 | Require user confirmation |
| **Unlikely** | 0.0-0.39  | Major data gaps                         | Do not generate document  |

---

## Glass Box Audit Trail

Every generated document set should be accompanied by this metadata:

```yaml
glass_box:
  skill_name: "legalcode-iceland-real-estate-contracts"
  document_type: "[Kauptilbod / Kaupsamningur / Kostnadaruppgjor / Full Set]"
  jurisdiction: "Iceland"
  governing_law:
    - "Log nr. 40/2002 um fasteignakaup"
    - "Log nr. 48/2003 um neytendakaup" # if new construction
    - "Log nr. 31/1993 hjuskaparlog"
  property_id: "[Fastanumer]"
  transaction_value: "[Kaupverd] kr."
  buyer_type: "[Individual-First / Individual-Repeat / Legal Entity]"
  hms_involvement: "[Yes/No]"
  special_conditions: "[List any fyrirvari]"
  data_verification:
    fasteignamat_source: "[FMR / User-provided / Unverified]"
    kennitala_format: "[Valid / Invalid]"
    payment_totals: "[Verified sum matches kaupverd]"
  confidence: "[HIGH / MEDIUM / LOW] - [rationale]"
  generated_documents:
    - path: "[output path]"
      type: "[document type]"
  reviewer: "AI-assisted - requires qualified legal review"
```

---

## Anti-Patterns Catalogue

What NOT to do when generating Icelandic real estate documents:

1. **Invalid Kennitala Format** - Never accept IDs that don't match DDMMYY-XXXX pattern.
   The kennitala is essential for registration and tax purposes.

2. **Omitting Spousal Consent Reference** - Article 64 of hjuskaparlog requires disclosure
   of marital status and consent for family home sales. Never omit this clause.

3. **Wrong Stamp Duty Rate** - First-time buyers get 0.4%, repeat buyers pay 0.8%, companies
   pay 1.6%. Applying the wrong rate causes registration delays.

4. **Missing HMS Reservations** - If the buyer is using hlutdeildarlán, the standard HMS
   reservations are mandatory. Omitting them creates unenforceable contracts.

5. **Assuming Default Interest** - Never include interest on payments made on time. The
   standard is no interest on timely payments; only dráttarvextir on late payments.

6. **Ignoring Building Stage** - For new construction, the byggingastig affects when loans
   can be disbursed and when registration is possible. Always capture this.

7. **Generic Legal Terms** - Icelandic real estate has specific legal terminology. Never
   substitute generic translations - use the proper Icelandic terms.

8. **Missing Witness Requirements** - Valid signatures require witness attestation (vottar).
   Documents without proper witness sections are invalid for thinglysinguna.

9. **Incorrect Payment Account Details** - Government fees must go to the correct syslumaður
   account. Misrouted payments cause delays.

10. **Omitting Anti-Money Laundering Declaration** - Log nr. 140/2018 requires buyers to
    declare the legal source of funds. This clause is mandatory.

11. **Hardcoding Interest Rates** - Central bank rates change. Reference "almenna vexti
    overdtryggdra utlana skv. 4. gr. laga nr. 38/2001" rather than specific percentages.

12. **Missing Encumbrance Release Section** - If there are existing mortgages to be released,
    they must be listed with vedhafi, skjalsnumer, and amounts. Omission blocks registration.

13. **Wrong Thinglysingargjald Calculation** - Currently 2.500 kr. per document. Count all
    documents to be registered (typically 8-12).

14. **Forgetting the Skilalysung Reference** - For new construction, the skilalysung
    (specification document) is incorporated by reference. Always mention it.

15. **Not Specifying Municipality** - The sveitarfelag affects which syslumaður handles
    registration. Always include the correct municipality.

---

## Writing Standards

When generating Icelandic real estate documents:

### Terminology Discipline

- Use proper Icelandic legal terms with consistent spelling
- Include special characters: þ, ð, á, é, í, ó, ú, ý, æ, ö
- If system limitations prevent special characters, use standard transliteration:
  - þ → th, ð → d, æ → ae, ö → o

### Number Formatting

- Currency: Use period as thousands separator, no decimal places for ISK
  - Correct: 55.400.000 kr.
  - Incorrect: 55,400,000 kr. or 55400000 kr.
- Percentages: Use comma as decimal separator
  - Correct: 0,8%
  - Incorrect: 0.8%
- Dates: DD-MM-YYYY or written out
  - Correct: 15-04-2024 or 15. april 2024

### Document Structure

- Use clear section headings in Icelandic
- Maintain consistent table formatting
- Include all required signature blocks
- Add page numbers (Sida X af Y)

---

## Output Format Template

When delivering generated documents, use this format:

```markdown
## Generated Iceland Real Estate Documents

### Transaction Summary

- **Property**: [Address], [Municipality]
- **Fastanumer**: [ID]
- **Purchase Price**: [Amount] kr.
- **Parties**: [Seller] → [Buyer]
- **Document Date**: [Date]

### Generated Documents

1. **Kauptilbod** (Bid Agreement)
   - File: `[filename].docx`
   - Status: [Generated / Requires review]

2. **Kaupsamningur** (Purchase Agreement)
   - File: `[filename].docx`
   - Status: [Generated / Requires review]

3. **Kostnadaruppgjor** (Expense Settlement)
   - File: `[filename].docx`
   - Stamp duty: [Amount] kr. ([Rate])
   - Registration fees: [Amount] kr.
   - Agency fee: [Amount] kr.
   - Total buyer costs: [Amount] kr.

### Items Requiring Verification

- [ ] [Item 1]
- [ ] [Item 2]

### Next Steps

1. Review all documents with fasteignasali
2. Verify fasteignamat from FMR
3. Confirm HMS approval (if applicable)
4. Submit to syslumaður for thinglysinguna
```

---

## External Tool Integration

### Template Generation

Use the JavaScript templates to generate Word documents:

```bash
cd templates/iceland-real-estate/
node kauptilbod-template.js    # Generates kauptilbod-template.docx
node kaupsamningur-template.js # Generates kaupsamningur-template.docx
node kostnadaruppgjor-template.js # Generates kostnadaruppgjor-template.docx
```

### Template Customization

The templates are written in JavaScript using the `docx` library. To customize:

1. Edit the `.js` file with updated text or structure
2. Run `node [template].js` to regenerate the `.docx`
3. Validate the output opens correctly in Word/LibreOffice

### Integration with legalcode-mcp

If connected to legalcode-mcp, use it to verify:

- Current fasteignamat values from FMR
- Property registration status from Thjodskra
- Current central bank reference rates
- Recent amendments to fasteignakaupalog

If not connected, mark unverified items with [VERIFY] and note in the Glass Box audit trail.

---

## Localization Notes

This skill is **already localized for Iceland**. No adaptation needed for Icelandic law.

For potential future expansion to other Nordic jurisdictions:

| Jurisdiction | Key Differences                                                   |
| ------------ | ----------------------------------------------------------------- |
| **Norway**   | Different property registration system (Kartverket), no kennitala |
| **Sweden**   | Lantmäteriet handles registration, different stamp duty structure |
| **Denmark**  | Tinglysning system, different documentation requirements          |
| **Finland**  | Dual language requirements (Finnish/Swedish)                      |

---

## Icelandic Real Estate Contract Terminology Glossary

This glossary contains the **exact legal phrases** used in Icelandic real estate contracts. These are
formulaic expressions — the precise wording carries legal weight and should be reproduced exactly
when drafting documents. Organized by context of use.

### Payment and Transfer Phrases (Greiðsluhugtök)

| Icelandic Phrase                                                                      | English Translation                                                            | Context / Usage                                                                                 |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| **Greitt með millifærslu fjár**                                                       | Paid by wire transfer                                                          | Standard cash payment method. Used in greiðslutilhögun tables.                                  |
| **Greitt með millifærslu við kaupsamning**                                            | Paid by wire transfer at purchase agreement                                    | First payment tranche — due at contract signing.                                                |
| **Greitt með millifærslu fjár við undirritun kaupsamnings**                           | Paid by wire transfer at signing of purchase agreement                         | Formal version of above, used in kaupsamningur.                                                 |
| **Greitt með millifærslu fjár við afhendingu eignar**                                 | Paid by wire transfer at property delivery                                     | Second payment tranche — due at handover.                                                       |
| **Greitt með millifærslu fjár við lokauppgjör 60 dögum eftir afhendingu**             | Paid by wire transfer at final settlement 60 days after delivery               | Standard final payment tranche.                                                                 |
| **Greitt eins og greiðslur berast**                                                   | Paid as payments are received                                                  | Used when seller receives payment in instalments or when loan disbursement timing is uncertain. |
| **Greiðsla við kaupsamning greitt inn á [nafn] kt. [kennitala] nr. [reikningsnúmer]** | Payment at purchase agreement paid into [name] ID [kennitala] account [number] | Full payment instruction format with escrow/recipient details.                                  |
| **Aðrar greiðslur greitt inn á [nafn] kt. [kennitala], rkn. [reikningsnúmer]**        | Other payments paid into [name] ID [kennitala], account [number]               | Secondary payment account instruction.                                                          |
| **Samtals greiðslur**                                                                 | Total payments                                                                 | Sum line in payment schedule.                                                                   |
| **Kaupverð**                                                                          | Purchase price                                                                 | The total agreed price for the property.                                                        |
| **A. Greiðslur** / **A. Greiðslutilhögun**                                            | A. Payments / A. Payment arrangement                                           | Section header for cash payment schedule.                                                       |
| **A. Greiðslutilhögun með millifærslu fjár**                                          | A. Payment arrangement by wire transfer                                        | Full section header in kaupsamningur.                                                           |
| **B. Lán**                                                                            | B. Loans                                                                       | Section header for loan components.                                                             |
| **B. Fasteignaveðbréf**                                                               | B. Mortgage bonds                                                              | Alternative loan section header in kaupsamningur.                                               |

### Loan and Financing Phrases (Lánahugtök)

| Icelandic Phrase                                                            | English Translation                                                 | Context / Usage                                                        |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Lán frá viðurkenndri lánastofnun**                                        | Loan from a recognized lending institution                          | Standard bank mortgage component.                                      |
| **HMS hlutdeildarlán**                                                      | HMS equity loan (Housing Financing Fund shared equity loan)         | Government-backed loan for first-time buyers.                          |
| **Lán eru gefin út strax eftir öryggisúttekt**                              | Loans are disbursed immediately after safety inspection             | Used for new construction — loans release upon safety clearance.       |
| **Yfirtaka áhvílandi veðskulda**                                            | Assumption of existing mortgages                                    | When buyer takes over seller's existing loans.                         |
| **Almenna vexti óverðtryggðra útlána skv. 4. gr. laga nr. 38/2001**         | General interest on non-indexed loans per Art. 4 of Act No. 38/2001 | Reference rate for late payment interest. Never hardcode a percentage. |
| **Dráttarvextir**                                                           | Default interest / penalty interest                                 | Interest charged on overdue payments.                                  |
| **Vextir reiknast ekki á útborgunargreiðslur sem greiðast á umsömdum degi** | No interest accrues on payments made on the agreed date             | Standard clause — timely payments carry no interest.                   |
| **Dráttarvextir reiknast við greiðsludrátt**                                | Default interest accrues on late payment                            | Paired with above — only late payments bear interest.                  |

### Property Description Phrases (Fasteignalýsing)

| Icelandic Phrase                                                            | English Translation                                                                           | Context / Usage                                         |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Ásamt öllu er eigninni fylgir og fylgja ber að engu undanskildu**         | Together with everything that accompanies and should accompany the property, nothing excluded | Standard completeness clause in property description.   |
| **Þar með talið tilheyrandi hlutdeild í sameign hússins og lóðarréttindum** | Including the corresponding share in common areas of the building and land rights             | Always follows the completeness clause for apartments.  |
| **Íbúðareign merkt [merking], fastanúmer [fastanúmer]**                     | Residential property marked [marking], property ID [ID]                                       | Standard property identification format.                |
| **Ásamt geymslu í kjallara**                                                | Including storage in basement                                                                 | Common addition for apartment properties.               |
| **Upplýsingar um fasteign**                                                 | Information about property                                                                    | Section header in kauptilboð.                           |
| **Fasteignalýsing**                                                         | Property description                                                                          | Detailed property description section in kaupsamningur. |
| **Eignarhluti í fasteign**                                                  | Ownership share in property                                                                   | Percentage share being transacted.                      |
| **Eignarhluti í lóð**                                                       | Ownership share in land/lot                                                                   | Land rights percentage.                                 |
| **Byggingastig**                                                            | Construction stage (1-7)                                                                      | Completion level: 1=foundation, 7=fully complete.       |
| **Matstig**                                                                 | Valuation stage                                                                               | FMR assessment completion level.                        |

### Party and Identification Phrases (Aðilar og auðkenning)

| Icelandic Phrase                                      | English Translation                | Context / Usage                                        |
| ----------------------------------------------------- | ---------------------------------- | ------------------------------------------------------ |
| **Seljandi** / **Eigandi** / **Eigendur**             | Seller / Owner / Owners            | Used interchangeably in headers.                       |
| **Kaupandi** / **Kaupendur**                          | Buyer / Buyers                     | Singular/plural buyer designation.                     |
| **Kennitala**                                         | National ID number (DDMMYY-XXXX)   | Required for all parties; format validated.            |
| **Tölvupóstfang** / **Tölvupóstur**                   | Email address                      | Contact information field.                             |
| **Hlutfall**                                          | Share / Percentage                 | Ownership percentage (e.g., 50.00 %).                  |
| **Tryggingarf. seljanda** / **Tryggingarf. kaupanda** | Seller's/Buyer's insurance company | Property insurance provider.                           |
| **F.h. [nafn ehf.]**                                  | On behalf of [company name]        | Used in signature blocks when a legal entity is party. |

### Legal Terms and Clauses (Lagahugtök og skilmálar)

| Icelandic Phrase                                                                                                                         | English Translation                                                                                                                  | Context / Usage                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **Skilmálar**                                                                                                                            | Terms and conditions                                                                                                                 | Standard legal terms section header.                             |
| **Sérákvæði**                                                                                                                            | Special provisions                                                                                                                   | Contract-specific deviations from standard terms.                |
| **Fyrirvari** / **Fyrirvara**                                                                                                            | Reservation / Condition precedent                                                                                                    | Contingency clauses (e.g., HMS approval, loan approval).         |
| **Kauptilboð þetta er gert með þeim fyrirvara að...**                                                                                    | This offer is made with the reservation that...                                                                                      | Standard reservation opening phrase.                             |
| **...ella hafa báðir aðilar heimild til að falla frá tilboði þessu án skaðabóta**                                                        | ...otherwise both parties are entitled to withdraw from this offer without damages                                                   | Standard reservation closing — mutual walk-away right.           |
| **Bindandi kaupsamningur er kominn á þegar skriflegt tilboð hefur verið samþykkt**                                                       | A binding purchase agreement is formed when a written offer has been accepted                                                        | Formation of contract clause.                                    |
| **Gagnkvæm skuldbinding, annars vegar um greiðslu kaupverðs og hins vegar um afhendingu eignar**                                         | Mutual obligation, on one hand regarding payment of purchase price and on the other regarding delivery of property                   | Core of binding agreement definition.                            |
| **Notuð fasteign telst ekki gölluð, nema ágallinn rýri verðmæti hennar svo nokkru varði eða seljandi hafi sýnt af sér saknæma háttsemi** | Used property is not considered defective unless the defect materially diminishes its value or the seller has shown culpable conduct | Key defect threshold — "materiality" standard for used property. |
| **Lög nr. 40/2002 um fasteignakaup**                                                                                                     | Real Estate Purchase Act No. 40/2002                                                                                                 | Primary governing law citation.                                  |
| **Lög nr. 48/2003 um neytendakaup**                                                                                                      | Consumer Purchase Act No. 48/2003                                                                                                    | Applies to new construction (neytendakaup).                      |
| **1. mgr. 64.gr. hjúskaparlaga nr. 31/1993**                                                                                             | Art. 64(1) of the Marriage Act No. 31/1993                                                                                           | Spousal consent requirement for family home.                     |

### Delivery and Transfer Phrases (Afhending og yfirfærsla)

| Icelandic Phrase                                                                     | English Translation                                                              | Context / Usage                                                   |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Afhendingardagur**                                                                 | Delivery date                                                                    | Date of physical possession transfer.                             |
| **Eign skal afhenda vel hreingerða á umsömdum afhendingardegi**                      | Property shall be delivered well cleaned on the agreed delivery date             | Standard delivery condition.                                      |
| **Áhættan af eign flyst frá seljanda til kaupanda við afhendingu**                   | Risk of property transfers from seller to buyer at delivery                      | Risk transfer clause.                                             |
| **Kaupandi hirðir frá þeim tíma arð af henni og greiðir af henni skatta og skyldur** | Buyer receives income from the property and pays taxes and duties from that time | Post-delivery obligations shift.                                  |
| **Seljandi til sama tíma**                                                           | Seller until the same time                                                       | Seller's obligation limit — pairs with buyer's assumption clause. |
| **Eign getur verið afhent að lokinni öryggisúttekt**                                 | Property can be delivered after safety inspection                                | New construction delivery condition.                              |
| **Þrátt fyrir að sameign og umhverfi sé ekki fullbúið**                              | Despite common areas and surroundings not being fully completed                  | New construction caveat — partial completion delivery.            |
| **Seljandi ábyrgist að eign fái lokaúttekt**                                         | Seller guarantees the property will receive final inspection                     | Seller's obligation for new construction completion.              |
| **Dags. kaupsamnings**                                                               | Date of purchase agreement                                                       | Key date field.                                                   |
| **Aflýsing**                                                                         | Release / cancellation (of encumbrances)                                         | Date when existing mortgages are removed.                         |
| **Útgáfa afsals**                                                                    | Issuance of deed                                                                 | When the final deed of sale is issued.                            |

### Disclosure and Inspection Phrases (Upplýsingaskylda og skoðun)

| Icelandic Phrase                                                                                                        | English Translation                                                                                        | Context / Usage                                       |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **Seljandi skal gefa kaupanda þær upplýsingar um eign, sem hann vissi eða mátti vita um**                               | Seller shall provide buyer with information about the property that he knew or should have known           | Seller's disclosure obligation.                       |
| **Kaupandi hafði réttmæta ástæðu til að ætla að hann fengi**                                                            | Buyer had reasonable cause to expect to receive [said information]                                         | Standard for information the buyer can rely on.       |
| **Kaupandi getur ekki borið fyrir sig neitt varðandi ástand og gæði eignar sem hann þekkti til eða átti að þekkja til** | Buyer cannot invoke anything regarding condition and quality of property that he knew or should have known | Buyer's inspection duty — no claims for known issues. |
| **Hafi hann skoðað eign fyrir kaupin eða látið það undir höfuð leggjast þrátt fyrir áskoranir**                         | If he inspected the property before purchase or neglected to do so despite invitations                     | Buyer's obligation to inspect.                        |
| **Skoða eignina á þann hátt sem góð venja er**                                                                          | Inspect the property in a manner consistent with good practice                                             | Post-delivery inspection standard.                    |

### Registration and Fees (Þinglýsing og gjöld)

| Icelandic Phrase                                                          | English Translation                                                                | Context / Usage                                       |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **Þinglýsing** / **Þinglýsinguna**                                        | Registration (at district commissioner)                                            | Act of registering documents at sýslumaður.           |
| **Þinglýst skjöl**                                                        | Registered documents                                                               | Section listing all registered documents on property. |
| **Þinglýsingarvottorð**                                                   | Registration certificate                                                           | Certificate of registration status.                   |
| **Stimpilgjald**                                                          | Stamp duty                                                                         | Government tax on property transfer.                  |
| **Stimpilgjald kaupsamnings**                                             | Stamp duty on purchase agreement                                                   | The specific stamp duty amount.                       |
| **Þinglýsingargjald af skjölum - [N] skjöl - 2.500 kr. skjalið**          | Registration fee for documents - [N] documents - 2,500 kr. per document            | Per-document registration fee format.                 |
| **Þar af stimpil- og þinglýsingargjöld**                                  | Of which stamp and registration fees                                               | Subtotal line in kostnaðaruppgjör.                    |
| **Sýslumaðurinn á höfuðborgarsvæðinu rknr. [reikningur] kt. [kennitala]** | The district commissioner of the capital area account no. [account] ID [kennitala] | Payment instruction for government fees.              |
| **Kvittun sendist á [email]**                                             | Receipt sent to [email]                                                            | Receipt delivery instruction.                         |
| **Umsýslugjald fasteignasölu** / **Umsýsluþóknun fasteignasölu**          | Real estate agency management fee                                                  | Agency fee — separate from stamp/registration.        |
| **Þjónustu- og umsýslugjald**                                             | Service and management fee                                                         | Alternative agency fee label.                         |
| **Kostnaður við kaupsamning**                                             | Cost of purchase agreement                                                         | Section header in kostnaðaruppgjör.                   |
| **Áætlaður kostnaður kaupenda**                                           | Estimated buyer costs                                                              | Section header in kauptilboð.                         |
| **Samtals**                                                               | Total                                                                              | Sum line in cost tables.                              |

### Contract Formation and Binding (Samningsgerð)

| Icelandic Phrase                                                                  | English Translation                                                                                        | Context / Usage                        |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **Tilboð rennur út [dagsetning] [tími]**                                          | Offer expires [date] [time]                                                                                | Offer expiration deadline.             |
| **Tilboðsmóttakandi samþykkir tilboð þetta og lýsir yfir að hann sé fjárráða**    | Offer recipient accepts this offer and declares that he/she is financially competent                       | Standard acceptance clause.            |
| **Kaupandi, sem lýsir sig fjárráða, býðst til að kaupa**                          | Buyer, who declares himself/herself financially competent, offers to purchase                              | Opening of binding offer.              |
| **Sé um að ræða gagntilboð býðst seljandi, sem lýsir sig fjárráða, til að selja** | If this is a counter-offer, the seller, who declares himself/herself financially competent, offers to sell | Counter-offer formulation.             |
| **Með höfnun tilboðs fellur það niður**                                           | Upon rejection, the offer lapses                                                                           | Effect of rejection.                   |
| **Það er sömuleiðis höfnun á tilboði ef gagntilboð kemur fram**                   | It is also a rejection of an offer if a counter-offer is made                                              | Counter-offer = rejection of original. |

### Anti-Money Laundering Declaration (Peningaþvætti)

| Icelandic Phrase                                                                                                                                                                                   | English Translation                                                                                                                                                    | Context / Usage                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **Kaupandi eignar lýsir því yfir, með áritun sinni á skjal þetta, að fé það sem notað er í viðskiptum þessum, er fengið með lögmætum hætti og brýtur ekki gegn lögum eða reglum um peningaþvætti** | The buyer declares, by signing this document, that the funds used in this transaction are lawfully obtained and do not violate laws or regulations on money laundering | Mandatory AML declaration under log nr. 140/2018. |
| **s.s. lögum um aðgerðir gegn peningaþvætti og fjármögnun hryðjuverka nr. 140/2018**                                                                                                               | i.e., Act on Measures Against Money Laundering and Terrorist Financing No. 140/2018                                                                                    | Statutory citation for AML.                       |

### Spousal Consent (Hjúskaparstaða)

| Icelandic Phrase                                                                                                         | English Translation                                                                                               | Context / Usage              |
| ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **Aðilar lýsa því yfir að undirritanir af hans/hennar hálfu séu í samræmi við 1. mgr. 64.gr. hjúskaparlaga nr. 31/1993** | Parties declare that signatures on their behalf are in accordance with Art. 64(1) of the Marriage Act No. 31/1993 | Spousal consent declaration. |
| **Hvað snertir hjúskaparstöðu, búsetu og húsnæði til atvinnurekstrar**                                                   | Regarding marital status, residence, and business premises                                                        | What Art. 64 covers.         |

### Fixtures and Fittings (Fylgihlutir)

| Icelandic Phrase                                                                          | English Translation                                                                                       | Context / Usage                                                         |
| ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Í eldhúsi skal vera eldavél, ofn og vifta**                                             | In the kitchen there shall be a stove, oven and extractor fan                                             | Standard kitchen fixtures.                                              |
| **Í baðherbergi fylgja föst hengi, innréttingar og tæki svo og skápur yfir eða við vask** | In the bathroom, fixed fittings, fixtures and equipment follow, as well as a cabinet above or by the sink | Standard bathroom fixtures.                                             |
| **Múr- og naglfastar innréttingar**                                                       | Wall-mounted and nail-fixed fixtures                                                                      | General rule — fixed items convey with sale.                            |
| **Gluggatjaldastangir og festingar, en ekki gluggatjöld**                                 | Curtain rods and fixtures, but not curtains                                                               | Exception — curtains do NOT convey.                                     |
| **Þó fylgja rimla-, strimla- og rúllugluggatjöld**                                        | However, venetian blinds, strip blinds and roller blinds do follow                                        | Exception to exception — these DO convey.                               |
| **Í bílskúr fylgir fastur ljósabúnaður, rafknúnir hurðaopnarar**                          | In garage, fixed lighting and electric door openers follow                                                | Garage fixtures.                                                        |
| **Skilalýsing**                                                                           | Specification/handover description                                                                        | Detailed spec document for new construction, incorporated by reference. |

### Encumbrances and Release (Veðbönd og aflýsing)

| Icelandic Phrase                                                                                                   | English Translation                                                                                                   | Context / Usage                          |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **Eftirtaldar áhvílandi veðskuldir eru kaupanda óviðkomandi og skal seljandi aflýsa þeim svo fljótt sem verða má** | The following encumbrances are of no concern to the buyer and the seller shall have them released as soon as possible | Standard encumbrance release clause.     |
| **Eignin seld án frekari kvaða og veðbanda en í því segir**                                                        | Property sold free of further encumbrances and liens than stated herein                                               | Clean-title guarantee.                   |
| **Veðhafi**                                                                                                        | Lien holder / Mortgagee                                                                                               | Column header in encumbrance table.      |
| **Þinglýst skjal nr.**                                                                                             | Registered document number                                                                                            | Registration reference for encumbrances. |
| **Upphafleg fjárhæð**                                                                                              | Original amount                                                                                                       | Face value of the mortgage at issuance.  |

### Witness and Signature (Vottar og undirskrift)

| Icelandic Phrase                                                                               | English Translation                                                                   | Context / Usage                           |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------- |
| **Vottar að réttri dags. undirskrift og fjárræði**                                             | Witnesses correct date, signature and financial competence                            | Witness attestation line.                 |
| **Vottur að réttri undirritun, dagsetningu og fjárræði aðila**                                 | Witness to correct signing, date and financial competence of parties                  | Alternative witness formulation.          |
| **Til staðfestu undirrita kaupandi og seljandi skjal þetta í viðurvist tveggja vitundarvotta** | In confirmation, buyer and seller sign this document in the presence of two witnesses | Standard signing clause in kaupsamningur. |
| **Undirskrift kaupanda**                                                                       | Buyer's signature                                                                     | Signature block label.                    |
| **Undirskrift seljanda**                                                                       | Seller's signature                                                                    | Signature block label.                    |
| **Staður - dags.**                                                                             | Place - date                                                                          | Location and date field at signing.       |

### New Construction Specific (Nýbyggingar)

| Icelandic Phrase                                                               | English Translation                                                    | Context / Usage                                         |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------- |
| **Eign í smíðum**                                                              | Property under construction                                            | Flags new-build status.                                 |
| **Ófyrirsjáanlegir atburðir**                                                  | Unforeseeable events                                                   | Force majeure concept for construction delays.          |
| **Kaupandi mun ekki gera kröfu á seljanda nema tafir verði umfram 60 daga**    | Buyer will not make claims against seller unless delays exceed 60 days | Standard delay tolerance.                               |
| **Eignaskiptayfirlýsing er í vinnslu**                                         | Condominium declaration is in progress                                 | New build — condo docs not yet finalized.               |
| **Kaupandi greiðir skipulagsgjald sem verður 0,3% af endanlegu brunabótamati** | Buyer pays planning fee of 0.3% of final fire insurance value          | Standard planning fee for new construction.             |
| **Öryggisúttekt**                                                              | Safety inspection                                                      | Construction milestone that triggers loan disbursement. |
| **Lokaúttekt**                                                                 | Final inspection                                                       | Full completion inspection.                             |
| **Auglýsingaefni t.a.m. tölvumyndir eru eingöngu til hliðsjónar**              | Advertising material such as computer images are for reference only    | Marketing materials disclaimer for off-plan purchases.  |

---

## Contract Review Mode

When the user provides an existing contract (kauptilboð, kaupsamningur, or kostnaðaruppgjör) for review,
follow this structured review process. The goal is to identify **missing elements**, **unusual provisions**,
**deviations from standard terms**, and **potential risks**.

### Step 1: Identify Document Type

Determine which type of document is being reviewed:

- **Kauptilboð** — Apply the Bid Agreement Review Checklist
- **Kaupsamningur** — Apply the Purchase Agreement Review Checklist
- **Kostnaðaruppgjör** — Apply the Expense Settlement Review Checklist
- **Unknown** — **CLARIFY** — Ask the user what document type this is

### Step 2: Structural Completeness Check

#### Kauptilboð Review Checklist

Check that each of the following sections is present and complete:

**Section A — Header and Identification**

- [ ] Property address with postal number (póstnúmer)
- [ ] Fastanúmer (property ID)
- [ ] Merking (unit marking)
- [ ] Landnúmer (land number) — _if applicable; may be pending for new construction_

**Section B — Property Details (Upplýsingar um fasteign)**

- [ ] Fasteignamat (property valuation) — _flag if 0 kr. without explanation_
- [ ] Brunabótamat (fire insurance value) — _flag if 0 kr. without explanation_
- [ ] Eignarhluti í fasteign and lóð (ownership shares)
- [ ] Insurance companies for both seller and buyer

**Section C — Parties**

- [ ] Seller: Nafn, Kennitala, Tölvupóstur, Sími, Hlutfall — all present
- [ ] Buyer: Nafn, Kennitala, Tölvupóstur, Sími, Hlutfall — all present
- [ ] Kennitala format validated (DDMMYY-XXXX for individuals, YYMMDD-XXXX for companies)
- [ ] Hlutfall percentages sum to 100% for each side

**Section D — Payment Structure**

- [ ] A. Greiðslur section present with numbered line items
- [ ] Each payment line has: Nr., Lýsing (description), Upphæð (amount)
- [ ] Payment descriptions use correct terminology:
  - "Greitt með millifærslu við kaupsamning" (at contract)
  - "Greitt með millifærslu fjár við afhendingu" (at delivery)
  - "X dögum eftir afhendingu með millifærslu fjár" (post-delivery)
- [ ] B. Lán section present if loans involved
- [ ] Loan descriptions specify lender type ("Lán frá viðurkenndri lánastofnun", "HMS hlutdeildarlán")
- [ ] **A. Greiðslur + B. Lán = Kaupverð** — amounts sum correctly

**Section E — Delivery and Price**

- [ ] Afhendingardagur (delivery date) specified
- [ ] Kaupverð (purchase price) clearly stated

**Section F — Property Description (Lýsing)**

- [ ] Contains "ásamt öllu er eigninni fylgir og fylgja ber að engu undanskildu"
- [ ] References "tilheyrandi hlutdeild í sameign hússins og lóðarréttindum"
- [ ] For new construction: references eignaskiptayfirlýsing and skilalýsing
- [ ] For new construction: öryggisúttekt/lokaúttekt delivery conditions

**Section G — Standard Terms (Skilmálar)**

- [ ] Contains at least 20 numbered clauses
- [ ] Key clauses present:
  - Binding effect and counter-offer rules (clauses 1-3)
  - Governing law reference to log nr. 40/2002 (clause 4)
  - Property condition and defect threshold (clauses 5-7)
  - Fixtures and fittings clause (clause 8)
  - Disclosure obligations (clauses 9-10)
  - Delivery and risk transfer (clauses 11, 14-15)
  - Interest/default interest (clause 12)
  - Registration and stamp duty (clauses 17-18)
  - Encumbrance-free sale (clause 19)
  - Deed entitlement (clause 20)
  - Spousal consent / hjúskaparlög reference (clause 23)

**Section H — Costs and Expiration**

- [ ] Áætlaður kostnaður kaupenda — estimated buyer costs
- [ ] Stimpilgjald amount with correct rate cited
- [ ] Þinglýsingargjald estimate
- [ ] Agency fee (umsýslugjald/þjónustugjald)
- [ ] Tilboð rennur út — expiration date and time

**Section I — Signatures and Witnesses**

- [ ] Undirskrift kaupanda block
- [ ] Undirskrift seljanda/eiganda block
- [ ] Vottar section with at least one witness
- [ ] Anti-money laundering declaration (log nr. 140/2018)
- [ ] Fasteignasali information with kennitala

**Section J — HMS Reservations (if applicable)**

- [ ] Fyrirvari that seller gets property approved for hlutdeildarlán
- [ ] Fyrirvari that buyer gets HMS application approved
- [ ] Walk-away clause ("ella hafa báðir aðilar heimild til að falla frá...án skaðabóta")
- [ ] Time limit specified (typically 3-4 weeks)

#### Kaupsamningur Review Checklist

All items from Kauptilboð checklist PLUS:

**Additional Section K — Detailed Property Description (Fasteignalýsing)**

- [ ] Fasteignanúmer, Landeign nr., Sveitarfélag
- [ ] Byggingargerð, Herbergi, Flatarmál
- [ ] Fasteignamat, Brunabótamat, Húsmat, Lóðarmat
- [ ] Byggingarefni, Byggingarár
- [ ] Byggingastig and Matstig
- [ ] Insurance companies (Vátr.fél)
- [ ] Inngangur type (sameiginlegur/sér)

**Additional Section L — Registered Documents (Þinglýst skjöl)**

- [ ] All registered documents listed with type and registration number
- [ ] Tryggingarbréf, eignaskiptayfirlýsing, lóðarleigusamningur present
- [ ] Cross-reference with encumbrances section

**Additional Section M — Key Dates Table**

- [ ] Dags. kaupsamnings (purchase agreement date)
- [ ] Afhending (delivery date)
- [ ] Aflýsing (encumbrance release)
- [ ] Útgáfa afsals (deed issuance date)
- [ ] Dates are logically ordered and realistic

**Additional Section N — Bank Payment Instructions**

- [ ] Account numbers for escrow/payment recipient
- [ ] Skýring (reference code) for payment identification
- [ ] Tilkynning (notification) email address

**Additional Section O — Full Skilmálar (24 clauses)**

- [ ] All 24 standard clauses present
- [ ] Additional clauses for new construction (log nr. 48/2003 reference)
- [ ] Clause 10 — delivery condition: "vel hreingerða" (well cleaned)
- [ ] Clause 14 — cost allocation for maintenance contributions
- [ ] Clause 15 — buyer's right to withhold payment for defects
- [ ] Clause 16 — documents reviewed listed (veðbandayfirlit, fasteignayfirlit, söluyfirlit, skilalýsing, eignaskiptayfirlýsing, lóðarleigusamningur)
- [ ] Clause 17 — stöðvunarréttur (right to halt payments if seller fails to release liens)
- [ ] Clause 20 — sérákvæði section for deviations

**Additional Section P — Encumbrance Release Table**

- [ ] Table with columns: Veðréttur, Veðhafi, Þinglýst skjal nr., Upphafleg fjárhæð, Útgáfudagur
- [ ] All listed encumbrances flagged as "kaupanda óviðkomandi" (not buyer's concern)
- [ ] Obligation on seller to release ("seljandi aflýsa þeim svo fljótt sem verða má")

#### Kostnaðaruppgjör Review Checklist

**Section Q — Property and Party Identification**

- [ ] Fasteign, Fastanúmer, Landnúmer, Merking, Áætlað fasteignamat
- [ ] Seljandi with Kennitala and Hlutfall
- [ ] Kaupandi with Kennitala and Hlutfall

**Section R — Cost Breakdown**

- [ ] Stimpilgjald — correct rate applied:
  - First-time buyer (fyrstu kaup): 0.4% of fasteignamat
  - Repeat buyer: 0.8% of fasteignamat
  - Legal entity: 1.6% of fasteignamat
- [ ] Stimpilgjald calculation is mathematically correct
- [ ] Þinglýsingargjald — number of documents x 2.500 kr. is accurate
- [ ] Umsýsluþóknun/umsýslugjald fasteignasölu — agency fee present
- [ ] Samtals (total) is correct sum
- [ ] "Þar af stimpil- og þinglýsingargjöld" subtotal is correct

**Section S — Payment Instructions**

- [ ] Sýslumaður account number and kennitala for government fees
- [ ] Kvittun sendist email for sýslumaður receipt
- [ ] Real estate agency account number and kennitala
- [ ] Kvittun sendist email for agency receipt

**Section T — Signatures**

- [ ] Undirskrift seljanda
- [ ] Undirskrift kaupanda
- [ ] Fasteignasali signature/information

### Step 3: Unusual Clause Detection

Flag any of the following as **YELLOW** (unusual, may need attention) or **RED** (highly unusual, strong review recommended):

#### RED Flags — Immediate Attention

| Finding                                                      | Why It Matters                                                              |
| ------------------------------------------------------------ | --------------------------------------------------------------------------- |
| Missing anti-money laundering declaration                    | Mandatory under log nr. 140/2018. Document may be rejected at registration. |
| Missing spousal consent clause (hjúskaparlög)                | Sale of family home without spousal consent is voidable under Art. 64.      |
| Payment amounts do not sum to kaupverð                       | Mathematical error or missing payment component — blocks registration.      |
| No witness section or incomplete witness block               | Invalid for þinglýsing — documents require witnessed signatures.            |
| Stamp duty calculated on wrong base or rate                  | Will be rejected by sýslumaður — must match fasteignamat and buyer type.    |
| Interest rate hardcoded instead of referencing law           | Should cite "skv. 4. gr. laga nr. 38/2001" — hardcoded rates become stale.  |
| Missing HMS fyrirvari when HMS loan is in payment structure  | Buyer has no walk-away right if HMS denies the property or application.     |
| Delivery date is before construction completion date         | Logically impossible — may indicate a drafting error.                       |
| Seller is legal entity but stimpilgjald uses individual rate | 1.6% applies to legal entities; 0.8%/0.4% only for individuals.             |

#### YELLOW Flags — Worth Reviewing

| Finding                                                 | Why It Matters                                                                     |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Fasteignamat or brunabótamat is 0 kr.                   | Normal for new construction not yet registered, but should be explained in Lýsing. |
| "SÉRÁKVÆÐI: ENGIN" present                              | Standard, but confirm no special conditions were overlooked.                       |
| Delivery date uses "eða fyrr" or approximation          | Acceptable for construction, but buyer should understand uncertainty.              |
| More than 60-day gap between delivery and final payment | Unusual — standard is 60 days. Longer period should be justified.                  |
| Seller's insurance listed as unknown                    | May indicate property isn't currently insured — risk during transition.            |
| Missing skipulagsgjald reference for new construction   | 0.3% of brunabótamat is standard for new builds.                                   |
| Eignaskiptayfirlýsing listed as "í vinnslu"             | Normal for new builds but means condo docs aren't finalized.                       |
| No reference to söluyfirlit                             | The sales overview should be listed as reviewed by parties.                        |
| Agency fee significantly above or below market range    | Standard range is 50.000-100.000 kr. for buyer service fee.                        |

### Step 4: Terminology Verification

Cross-reference all legal phrases against the Terminology Glossary above. Flag:

- **Incorrect formulations** — phrases that deviate from standard wording
- **Mixed terminology** — using "greiðslur" in one place and "greiðslutilhögun" inconsistently
- **Missing standard phrases** — e.g., the "ásamt öllu er eigninni fylgir" completeness clause
- **Unofficial translations** — Icelandic legal terms replaced with informal language

### Step 5: Generate Review Report

Output a structured review in this format:

```markdown
## Contract Review Report — [Document Type]

### Property: [Address], [Municipality]

### Parties: [Seller] → [Buyer]

### Date Reviewed: [Date]

---

### Structural Completeness: [X/Y sections present]

| Section   | Status       | Notes     |
| --------- | ------------ | --------- |
| Header/ID | ✅ / ⚠️ / ❌ | [details] |
| Parties   | ✅ / ⚠️ / ❌ | [details] |
| Payment   | ✅ / ⚠️ / ❌ | [details] |
| ...       | ...          | ...       |

### RED Flags (Immediate Attention Required)

1. **[Finding]** — [Explanation and recommendation]
2. ...

### YELLOW Flags (Worth Reviewing)

1. **[Finding]** — [Explanation and recommendation]
2. ...

### Terminology Check

| Phrase Found | Expected Standard | Status  |
| ------------ | ----------------- | ------- |
| ...          | ...               | ✅ / ⚠️ |

### Payment Verification

| Component          | Amount  | Running Total |
| ------------------ | ------- | ------------- |
| A. Greiðslur       | [X] kr. | [X] kr.       |
| B. Lán             | [X] kr. | [X] kr.       |
| **Kaupverð**       |         | **[X] kr.**   |
| **Match**: ✅ / ❌ |

### Stamp Duty Verification

- Buyer type: [First-time / Repeat / Legal entity]
- Rate applied: [X]%
- Fasteignamat: [X] kr.
- Expected stimpilgjald: [X] kr.
- Actual stimpilgjald: [X] kr.
- **Match**: ✅ / ❌

### Missing Elements

- [ ] [Element 1 — what should be added]
- [ ] [Element 2 — what should be added]

### Summary

**Overall Assessment**: [GREEN — Standard contract, no significant issues] /
[YELLOW — Minor issues or missing non-critical elements] /
[RED — Significant issues requiring attention before signing]

**Confidence**: [HIGH / MEDIUM / LOW] — [rationale]

> ⚠️ This review is AI-assisted and does not constitute legal advice. Have a qualified
> lögfræðingur or löggildur fasteignasali review any issues flagged above.
```

---

## Provenance

**Created**: 2026-02-27
**Source**: Legalcode original synthesis

**Research basis**:

- Log nr. 40/2002 um fasteignakaup (Althingi)
- Log nr. 99/2004 um solu fasteigna og skipulagsloda
- HMS hlutdeildarlán requirements (island.is)
- Standard form contracts from Icelandic real estate agencies
- Example documents: Miklaborg, LIND Fasteignasala, RE/MAX

**Template sources**:

- Analyzed actual kauptilbod, kaupsamningur, and kostnadaruppgjor documents
- Extracted standard skilmalar clauses compliant with log nr. 40/2002
- Structured output following Icelandic legal document conventions

**Legal framework verified against**:

- [Althingi Law Database](https://www.althingi.is/lagas/nuna/2002040.html)
- [HMS/Ibudalanasjodur](https://www.hms.is/)
- [Island.is property services](https://island.is/en/land-and-real-estate)
