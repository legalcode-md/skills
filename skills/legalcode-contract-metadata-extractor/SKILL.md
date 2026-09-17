---
name: legalcode-contract-metadata-extractor
description: Extract structured metadata from contracts and legal documents into a normalized, machine-readable
  format suitable for CLM systems, databases, and analytics. Use when ingesting contracts into a contract
  lifecycle management system, building a contract repository, performing portfolio analysis, enabling
  contract search and discovery, or automating contract data capture. Extracts parties, dates, financial
  terms, governing law, key clauses, obligations, and risk indicators with confidence scoring and provenance
  tracking. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Contract Metadata Extractor

> **Disclaimer**: This skill provides a framework for AI-assisted contract metadata
> extraction. It does not constitute legal advice. All outputs should be reviewed by
> qualified legal or business professionals before operational use. Extraction accuracy
> depends on document quality and structure; verify critical fields against source
> documents before relying on them for business decisions.

## Purpose and Scope

This skill transforms unstructured contract documents into structured, machine-readable
metadata records. It enables systematic contract management, search, analysis, and
integration with enterprise systems.

**Covers:**

- Party identification (names, roles, addresses, identifiers)
- Date extraction (effective, execution, expiration, renewal, notice periods)
- Financial term capture (value, payment terms, price adjustments, currencies)
- Governing law and dispute resolution identification
- Key clause presence and summary (liability, indemnity, IP, data protection, termination)
- Obligation flagging with deadlines and owners
- Risk indicator identification and scoring
- Structured output in JSON, CSV, or CLM-compatible formats
- Batch processing for contract portfolio ingestion
- Confidence scoring and provenance tracking for every extracted field

**Does not:**

- Provide legal interpretation or advice on contract terms
- Replace human review for high-stakes contract decisions
- Guarantee 100% extraction accuracy (all outputs require verification)
- Draft or modify contracts
- Perform contract negotiation or redlining

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. It identifies and extracts the governing law from
each contract without applying jurisdiction-specific interpretation unless explicitly
requested.

[JURISDICTION-SPECIFIC] When extracting metadata, flag these jurisdiction-dependent
considerations:

- Local language requirements (contracts must be in local language to be enforceable)
- Registration or notarization requirements that affect validity dates
- Mandatory contract terms that must be present
- Local entity identifier formats (EIN, Companies House number, SIREN, etc.)
- Currency and payment term conventions
- Data protection regime applicability (GDPR, CCPA, LGPD, etc.)

---

## Interactive Clarification

This skill uses **CLARIFY** prompts at key decision points. Ask before proceeding when:

- The extraction schema needs customization beyond defaults
- Multiple date interpretations exist (execution vs. effective date ambiguity)
- Party roles are unclear from the document structure
- Financial terms are complex or conditional
- Output format requirements are not specified
- Batch processing prioritization is needed

If the user has provided partial context, proceed with explicit assumptions and list each
assumption in the extraction notes.

---

## Workflow

### Step 1: Accept Input Documents

Accept contracts in any of these formats:

- **PDF**: Native, scanned, or image-based (OCR may be required)
- **DOCX/DOC**: Microsoft Word documents
- **Text**: Plain text or pasted contract content
- **URL**: Link to a document in a CLM, cloud storage, or document system
- **Batch**: Multiple documents for portfolio extraction

If the document is scanned or image-based, note that OCR quality affects extraction
accuracy. Flag low-confidence extractions for manual review.

### Step 2: Gather Extraction Context

**CLARIFY** -- Before extraction, confirm these parameters:

1. **Extraction schema**: Which metadata fields are required?
   - Options: **Full extraction** (all 50+ fields), **Core fields only** (parties, dates,
     value, governing law), **Custom schema** (user specifies fields)
   - _Why this matters_: Full extraction takes longer but provides comprehensive data;
     core fields enable faster processing for high-volume ingestion.

2. **Output format**: How should the extracted data be delivered?
   - Options: **JSON** (structured, API-ready), **CSV/TSV** (spreadsheet-compatible),
     **CLM-specific format** (specify system), **Markdown table** (human-readable)
   - _Why this matters_: Different systems require different formats for import.

3. **Confidence threshold**: What is the minimum confidence for auto-acceptance?
   - Options: **High only** (0.80+, conservative), **Moderate** (0.60+, balanced),
     **Low** (0.40+, liberal with more manual review)
   - _Why this matters_: Lower thresholds extract more data but require more verification.

4. **Entity resolution**: Should parties be matched against a master entity list?
   - Options: **Yes** (provide list or CLM connection), **No** (extract as-is),
     **Flag duplicates** (identify potential matches without resolving)
   - _Why this matters_: Entity resolution prevents duplicate counterparty records.

5. **Processing mode**: Single document or batch portfolio?
   - Options: **Single** (detailed extraction with full analysis), **Batch** (optimized
     for volume, summary output per document), **Portfolio** (batch + aggregated analytics)

If context is not provided, default to: Full extraction, JSON output, Moderate threshold
(0.60+), No entity resolution, Single document mode.

### Step 3: Document Structure Analysis

Before extracting metadata, analyze the document structure:

1. **Identify document type**: Determine the contract category
   - NDA/Confidentiality Agreement
   - Master Services Agreement (MSA)
   - Statement of Work (SOW)
   - Software License Agreement
   - SaaS/Subscription Agreement
   - Employment Agreement
   - Lease Agreement
   - Purchase/Sale Agreement
   - Partnership/Joint Venture Agreement
   - Amendment/Addendum
   - Other (specify)

2. **Map document sections**: Locate key structural elements
   - Title/header
   - Recitals/background/whereas clauses
   - Definitions section
   - Main body/operative provisions
   - Signature blocks
   - Schedules/exhibits/annexes
   - Incorporated documents by reference

3. **Detect amendments and relationships**: Identify
   - Is this an amendment to a prior agreement?
   - Does this incorporate other documents by reference?
   - Is this part of a master/sub-agreement structure?

**CLARIFY** -- If incorporated documents are referenced but not provided, ask:

- "This contract references [Document X]. Should I extract from available text only, or
  do you have the referenced document to include?"

### Step 4: Extract Core Metadata Fields

Extract the following mandatory fields for every contract:

#### 4.1 Party Information

| Field              | Description                                                         | Extraction Source                |
| ------------------ | ------------------------------------------------------------------- | -------------------------------- |
| Party Name         | Legal name of each party                                            | Title, recitals, signature block |
| Party Role         | Role in the agreement (e.g., "Supplier", "Customer", "Licensor")    | Recitals, definitions            |
| Party Type         | Entity type (corporation, LLC, individual, partnership, government) | Recitals, entity suffix          |
| Registered Address | Legal/registered address                                            | Recitals, notice provisions      |
| Entity Identifier  | Tax ID, registration number, LEI, D-U-N-S                           | Recitals, signature block        |
| Signatory Name     | Name of signing individual                                          | Signature block                  |
| Signatory Title    | Title/position of signatory                                         | Signature block                  |
| Parent/Affiliate   | Parent company or affiliate relationships                           | Recitals, definitions            |

**Extraction rules:**

- Prefer the party name from the signature block over the title (signature block is often
  more precise)
- Extract ALL parties, including guarantors, third-party beneficiaries, and affiliates
- Flag any discrepancy between party names in different document sections
- For individuals, capture "doing business as" names if present

#### 4.2 Key Dates

| Field           | Description                                | Format     | Extraction Source                        |
| --------------- | ------------------------------------------ | ---------- | ---------------------------------------- |
| Execution Date  | Date of signature                          | YYYY-MM-DD | Signature block, opening paragraph       |
| Effective Date  | Date agreement becomes operative           | YYYY-MM-DD | Effective date clause, opening paragraph |
| Expiration Date | Date agreement terminates                  | YYYY-MM-DD | Term clause                              |
| Renewal Date    | Date of next renewal                       | YYYY-MM-DD | Computed from term clause                |
| Notice Deadline | Latest date for termination/renewal notice | YYYY-MM-DD | Computed from notice period              |
| Amendment Date  | Date of amendment (if applicable)          | YYYY-MM-DD | Amendment header                         |

**Date computation rules:**

- If effective date is "upon execution," set equal to execution date
- Compute expiration from initial term starting from effective date
- Compute renewal date from expiration minus auto-renewal notice period
- If dates are relative ("30 days after..."), note the anchor event and compute if anchor
  is known
- Flag any unresolvable dates as `UNRESOLVED_DATE` with the source text

**Date formats encountered:**

- Normalize all dates to ISO 8601 (YYYY-MM-DD)
- Preserve original date text in `source_text` field for audit
- Handle variations: "March 15, 2024", "15/03/2024", "15th day of March 2024"

#### 4.3 Financial Terms

| Field                 | Description                             | Extraction Source                |
| --------------------- | --------------------------------------- | -------------------------------- |
| Total Contract Value  | Aggregate value over full term          | Payment clause, pricing schedule |
| Annual Value          | Yearly value (for multi-year contracts) | Computed or stated               |
| Currency              | Currency of payment                     | Payment clause                   |
| Payment Terms         | Net terms (Net 30, Net 60, etc.)        | Payment clause                   |
| Payment Frequency     | How often payment is due                | Payment clause                   |
| Price Escalation      | Annual increase mechanism               | Payment clause, pricing schedule |
| Early Termination Fee | Penalty for early termination           | Termination clause               |
| Late Payment Interest | Interest rate on overdue payments       | Payment clause                   |

**Financial extraction rules:**

- Extract both stated values and formulas (e.g., "10% of revenue")
- Flag variable or contingent pricing as `VARIABLE_VALUE` with formula
- Convert all currencies to a consistent format (ISO 4217 codes)
- If value is per-unit, extract unit type and compute total if quantity is known

#### 4.4 Governing Law and Disputes

| Field               | Description                                         | Extraction Source         |
| ------------------- | --------------------------------------------------- | ------------------------- |
| Governing Law       | Jurisdiction whose law governs                      | Governing law clause      |
| Dispute Forum       | Court or arbitration venue                          | Dispute resolution clause |
| Dispute Mechanism   | Litigation, arbitration, mediation                  | Dispute resolution clause |
| Arbitration Rules   | Applicable arbitration rules (ICC, AAA, LCIA, etc.) | Arbitration clause        |
| Jury Waiver         | Whether jury trial is waived                        | Dispute resolution clause |
| Class Action Waiver | Whether class actions are waived                    | Dispute resolution clause |

### Step 5: Extract Extended Metadata Fields

For full extraction mode, capture these additional fields:

#### 5.1 Term and Renewal

| Field                       | Description                                      |
| --------------------------- | ------------------------------------------------ |
| Initial Term                | Length of initial contract period                |
| Renewal Type                | Auto-renewal, manual renewal, or fixed term      |
| Renewal Term                | Length of each renewal period                    |
| Renewal Notice Period       | Days' notice required to prevent renewal         |
| Maximum Term                | Cap on total contract duration (if any)          |
| Termination for Convenience | Whether either party can terminate without cause |
| Termination Notice Period   | Days' notice required for termination            |
| Cure Period                 | Days to cure breach before termination           |

#### 5.2 Key Clauses Presence and Summary

For each of these clause categories, extract: (1) whether present, (2) summary of key
terms, (3) location in document.

| Clause Category                  | Key Elements to Extract                                         |
| -------------------------------- | --------------------------------------------------------------- |
| **Limitation of Liability**      | Cap amount/formula, mutual or unilateral, carveouts             |
| **Indemnification**              | Scope, mutual or unilateral, capped or uncapped, procedure      |
| **Intellectual Property**        | Ownership of developed IP, license grants, work-for-hire        |
| **Data Protection**              | DPA required, data controller/processor, transfer mechanisms    |
| **Confidentiality**              | Scope, term, carveouts, return/destruction obligations          |
| **Insurance**                    | Required coverage types, minimum amounts, evidence requirements |
| **Assignment**                   | Consent requirements, change-of-control provisions              |
| **Force Majeure**                | Covered events, termination rights                              |
| **Representations & Warranties** | Key warranties, disclaimers, survival period                    |
| **Non-Compete/Exclusivity**      | Scope, territory, duration                                      |
| **Audit Rights**                 | Scope, frequency, notice, cost allocation                       |
| **Compliance**                   | Anti-bribery, sanctions, export control, modern slavery         |

#### 5.3 Obligations and Deadlines

Extract time-bound obligations with:

- Obligation description
- Obligated party
- Benefiting party
- Trigger event
- Due date or deadline rule
- Recurrence (one-time, recurring)
- Consequence of breach

Prioritize obligations related to:

- Payment deadlines
- Notice requirements
- Reporting obligations
- Audit cooperation
- Insurance certificate delivery
- Renewal/termination decisions

#### 5.4 Risk Indicators

Flag potential risk indicators:

| Risk Category          | Indicators to Flag                                               |
| ---------------------- | ---------------------------------------------------------------- |
| **Liability Risk**     | Uncapped liability, broad indemnification, missing liability cap |
| **IP Risk**            | Broad IP assignment, unclear ownership, missing license scope    |
| **Data Risk**          | No DPA, personal data processing without safeguards              |
| **Financial Risk**     | Uncapped price escalation, onerous payment terms, penalties      |
| **Termination Risk**   | No termination for convenience, long lock-in, short cure period  |
| **Compliance Risk**    | Missing anti-bribery, no sanctions clause, regulatory gaps       |
| **Concentration Risk** | Exclusivity provisions, non-compete restrictions                 |

### Step 6: Confidence Scoring and Provenance

For every extracted field, assign:

#### 6.1 Confidence Level

| Level         | Range     | Criteria                                                          |
| ------------- | --------- | ----------------------------------------------------------------- |
| **Definite**  | 0.95-1.0  | Explicit statement, unambiguous text, standard format             |
| **High**      | 0.80-0.94 | Clear statement with minor interpretation, standard location      |
| **Probable**  | 0.60-0.79 | Inferred from context, non-standard location, some ambiguity      |
| **Possible**  | 0.40-0.59 | Derived from related clauses, significant interpretation required |
| **Uncertain** | 0.0-0.39  | Speculative, conflicting information, poor document quality       |

#### 6.2 Provenance Tracking

For every extracted field, record:

- **Source location**: Section/clause number, page number, paragraph
- **Source text**: Verbatim excerpt from which the field was extracted
- **Extraction method**: Direct extraction, computation, inference
- **Confidence score**: Numeric score (0.0-1.0)
- **Notes**: Any caveats, assumptions, or conflicts

### Step 7: Entity Resolution (If Enabled)

If entity resolution is enabled:

1. **Match extracted parties against master list**
   - Use fuzzy matching for name variations
   - Match on entity identifiers where available
   - Flag potential duplicates with similarity scores

2. **Normalize entity names**
   - Remove common suffixes for matching (Inc., LLC, Ltd., GmbH)
   - Handle "doing business as" variations
   - Resolve parent/subsidiary relationships

3. **Output resolution decisions**
   - Matched entities with confidence scores
   - Unmatched entities (new counterparties)
   - Ambiguous matches requiring human review

### Step 8: Validate Extraction Quality

Before delivering results, run quality checks:

#### 8.1 Completeness Check

- All mandatory fields extracted or flagged as missing
- Party count matches document structure (2+ parties expected)
- At least one date field populated
- Governing law identified

#### 8.2 Consistency Check

- Party names consistent across document sections
- Dates are logically consistent (effective <= expiration)
- Financial terms are internally consistent
- No contradictory extractions

#### 8.3 Confidence Distribution

- Flag documents with high proportion of low-confidence extractions
- Recommend manual review for documents below threshold
- Highlight fields requiring verification

### Step 9: Generate Output

Structure the output based on the requested format:

#### 9.1 JSON Output Format

```json
{
  "extraction_metadata": {
    "extraction_id": "EXT-20260302-001",
    "extraction_timestamp": "2026-03-02T12:00:00Z",
    "document_id": "DOC-001",
    "document_name": "Master Services Agreement - Acme Corp.pdf",
    "document_type": "Master Services Agreement",
    "schema_version": "1.0",
    "extraction_mode": "full",
    "overall_confidence": 0.85
  },
  "parties": [
    {
      "party_name": "Acme Corporation",
      "party_role": "Customer",
      "party_type": "Corporation",
      "registered_address": "123 Main Street, Wilmington, DE 19801",
      "entity_identifier": {
        "type": "EIN",
        "value": "12-3456789"
      },
      "signatory": {
        "name": "Jane Smith",
        "title": "Chief Executive Officer"
      },
      "confidence": 0.95,
      "source": {
        "location": "Signature Block, Page 15",
        "text": "ACME CORPORATION, a Delaware corporation..."
      }
    }
  ],
  "dates": {
    "execution_date": {
      "value": "2026-02-28",
      "confidence": 0.98,
      "source": {
        "location": "Signature Block",
        "text": "Dated as of February 28, 2026"
      }
    },
    "effective_date": {
      "value": "2026-03-01",
      "confidence": 0.9,
      "source": {
        "location": "Section 1.1",
        "text": "This Agreement shall be effective as of March 1, 2026"
      }
    },
    "expiration_date": {
      "value": "2029-02-28",
      "confidence": 0.85,
      "computed": true,
      "computation": "effective_date + 36 months",
      "source": {
        "location": "Section 10.1",
        "text": "initial term of three (3) years"
      }
    }
  },
  "financial_terms": {
    "total_contract_value": {
      "value": 500000,
      "currency": "USD",
      "confidence": 0.75,
      "notes": "Based on stated annual value x 3 year term",
      "source": {
        "location": "Exhibit A, Section 2",
        "text": "Annual Fee: $166,666.67"
      }
    }
  },
  "governing_law": {
    "jurisdiction": "State of Delaware",
    "law": "laws of the State of Delaware",
    "dispute_mechanism": "Litigation",
    "dispute_forum": "Courts of the State of Delaware",
    "confidence": 0.98,
    "source": {
      "location": "Section 12.5",
      "text": "This Agreement shall be governed by and construed in accordance with the laws of the State of Delaware..."
    }
  },
  "key_clauses": {
    "limitation_of_liability": {
      "present": true,
      "summary": "Capped at fees paid in prior 12 months; mutual; carveouts for indemnification and confidentiality breach",
      "cap_amount": "fees paid in prior 12 months",
      "mutual": true,
      "carveouts": [
        "indemnification",
        "confidentiality breach",
        "IP infringement"
      ],
      "confidence": 0.9,
      "source": {
        "location": "Section 8.2",
        "text": "..."
      }
    }
  },
  "obligations": [
    {
      "obligation_id": "OBL-001",
      "description": "Provide renewal notice",
      "obligated_party": "Customer",
      "trigger": "90 days before expiration",
      "due_date": "2028-12-01",
      "consequence": "Auto-renewal for 12 months",
      "confidence": 0.85
    }
  ],
  "risk_indicators": [
    {
      "category": "Termination Risk",
      "indicator": "No termination for convenience",
      "severity": "YELLOW",
      "source": {
        "location": "Section 10",
        "notes": "Termination only for cause with 60-day cure period"
      }
    }
  ],
  "extraction_notes": {
    "assumptions": [
      "Effective date interpreted as first day of month following execution"
    ],
    "unresolved_fields": [
      "Insurance requirements - referenced in Exhibit C which was not provided"
    ],
    "conflicts": [],
    "manual_review_required": [
      "Total contract value - derived from annual fee, confirm calculation"
    ]
  },
  "glass_box": {
    "extraction_id": "EXT-20260302-001",
    "document": "Master Services Agreement - Acme Corp.pdf",
    "document_type": "Master Services Agreement",
    "pages_analyzed": 15,
    "sections_identified": 14,
    "fields_extracted": 42,
    "fields_high_confidence": 35,
    "fields_low_confidence": 7,
    "fields_unresolved": 3,
    "entity_resolution": "Not enabled",
    "extraction_mode": "Full",
    "overall_confidence": "HIGH - 0.85",
    "limitations": [
      "Exhibit C not provided - insurance terms not extracted",
      "Scanned signature page - signatory names extracted with moderate confidence"
    ],
    "reviewer": "AI-assisted - requires human verification"
  }
}
```

#### 9.2 CSV Output Format

For batch processing, output a flattened CSV with one row per contract:

| Column              | Description                        |
| ------------------- | ---------------------------------- |
| document_id         | Unique identifier for the document |
| document_name       | File name                          |
| document_type       | Contract category                  |
| party_1_name        | First party name                   |
| party_1_role        | First party role                   |
| party_2_name        | Second party name                  |
| party_2_role        | Second party role                  |
| effective_date      | Effective date (YYYY-MM-DD)        |
| expiration_date     | Expiration date (YYYY-MM-DD)       |
| total_value         | Total contract value               |
| currency            | Currency code                      |
| governing_law       | Governing jurisdiction             |
| liability_capped    | Yes/No                             |
| liability_cap       | Cap amount if capped               |
| has_dpa             | Yes/No                             |
| has_auto_renewal    | Yes/No                             |
| renewal_notice_days | Days notice for renewal            |
| overall_confidence  | Confidence score (0-1)             |
| requires_review     | Yes/No                             |

#### 9.3 Portfolio Analytics (Batch Mode)

For portfolio extraction, include aggregated analytics:

```json
{
  "portfolio_summary": {
    "total_contracts": 150,
    "total_value": 25000000,
    "currencies": { "USD": 120, "EUR": 25, "GBP": 5 },
    "contract_types": {
      "MSA": 45,
      "NDA": 30,
      "SOW": 50,
      "Other": 25
    },
    "counterparty_concentration": {
      "top_5_counterparties": ["...", "..."],
      "concentration_percentage": 35
    },
    "expiration_timeline": {
      "next_30_days": 5,
      "next_90_days": 12,
      "next_12_months": 45
    },
    "risk_summary": {
      "high_risk": 8,
      "medium_risk": 42,
      "low_risk": 100
    },
    "extraction_quality": {
      "high_confidence": 120,
      "moderate_confidence": 25,
      "requires_review": 5
    }
  }
}
```

### Step 10: Quality Verification

Before delivering the extraction, run these quality checks:

#### 10.1 Citation Quality Gates

| Gate             | Rule                                        | Fail Action                |
| ---------------- | ------------------------------------------- | -------------------------- |
| **Source**       | Every extracted field has a source location | Flag as missing provenance |
| **Verbatim**     | Source text matches document content        | Flag extraction error      |
| **Completeness** | All mandatory fields present or flagged     | List missing fields        |
| **Consistency**  | No contradictory extractions                | Flag conflicts for review  |
| **Confidence**   | Overall confidence above threshold          | Recommend manual review    |

#### 10.2 Self-Interrogation for Low-Confidence Extractions

For any field with confidence below 0.60, apply:

**Pass 1 -- Source Verification**:

- Is the source text correctly identified?
- Does the extraction match the source semantically?
- Are there alternative interpretations?

**Pass 2 -- Context Check**:

- Does this extraction make sense given other extracted fields?
- Are there related fields that provide confirmation?
- Does this align with typical contract structure?

**Pass 3 -- Ambiguity Resolution**:

- What is the most reasonable interpretation?
- What would human review likely conclude?
- Should this be flagged for manual review?

### Step 11: CLM System Integration

If integrating with a Contract Lifecycle Management system:

**CLARIFY** -- Which CLM system is the target?

- Icertis, Ironclad, Agiloft, ContractPodAi, DocuSign CLM, Conga, SirionLabs, Other

Map extracted fields to CLM-specific field names and formats. Common mappings:

| Standard Field  | CLM Field Name (varies by system)             |
| --------------- | --------------------------------------------- |
| party_name      | Counterparty Name, Vendor Name, Customer Name |
| effective_date  | Contract Start Date, Effective Date           |
| expiration_date | Contract End Date, Expiration Date            |
| total_value     | Contract Value, Total Amount                  |
| governing_law   | Jurisdiction, Governing Law                   |

Generate import-ready format per CLM system requirements.

---

## Metadata Schema Reference

### Full Field Taxonomy

The complete extraction schema includes 50+ fields organized into categories:

#### Category 1: Document Identification (8 fields)

- document_id, document_name, document_type, document_date, page_count, language,
  amendment_to, master_agreement_ref

#### Category 2: Party Information (12 fields per party)

- party_name, party_role, party_type, registered_address, mailing_address, entity_id,
  entity_id_type, signatory_name, signatory_title, parent_company, affiliates,
  party_aliases

#### Category 3: Dates and Term (10 fields)

- execution_date, effective_date, expiration_date, renewal_date, notice_deadline,
  initial_term, renewal_term, renewal_type, term_cap, amendment_date

#### Category 4: Financial Terms (12 fields)

- total_value, annual_value, currency, payment_terms, payment_frequency, price_formula,
  price_escalation, late_interest_rate, early_termination_fee, discount_terms,
  payment_method, billing_address

#### Category 5: Governing Law and Disputes (8 fields)

- governing_law, dispute_mechanism, dispute_forum, arbitration_rules, arbitration_seat,
  jury_waiver, class_waiver, attorneys_fees

#### Category 6: Key Clauses (14 clause categories)

- Each with: present, summary, key_terms, confidence, source

#### Category 7: Obligations (variable)

- Each with: obligation_id, description, obligated_party, benefiting_party, trigger,
  due_date, recurrence, consequence, confidence

#### Category 8: Risk Indicators (variable)

- Each with: category, indicator, severity, source, recommendation

### SALI-Compatible Tagging

For organizations using SALI (Standards Advancement for the Legal Industry) standards,
map extractions to SALI Legal Matter Specification Standard (LMSS) tags:

| Extraction Field  | SALI Tag Category  |
| ----------------- | ------------------ |
| document_type     | SALI Document Type |
| governing_law     | SALI Jurisdiction  |
| clause_categories | SALI Clause Type   |
| industry_vertical | SALI Industry      |

---

## Severity Classification for Risk Indicators

### RED -- High Risk

Material risk requiring immediate attention or escalation:

- Uncapped liability or missing liability cap
- Unilateral broad indemnification
- No data processing agreement when personal data is processed
- IP assignment of customer's pre-existing IP
- Missing governing law clause
- Exclusivity that materially restricts business

### YELLOW -- Medium Risk

Significant deviation requiring review:

- Liability cap below market standard
- Asymmetric indemnification
- Missing key clauses (insurance, audit rights)
- Unusual governing law or dispute forum
- Aggressive auto-renewal terms
- Broad non-compete provisions

### GREEN -- Low Risk / Acceptable

Standard terms or favorable provisions:

- Balanced liability cap at or above market standard
- Mutual indemnification with reasonable scope
- All expected clauses present
- Reasonable termination flexibility
- Standard payment terms

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates before delivering any extraction:

| Gate             | Rule                                          | Fail Action              |
| ---------------- | --------------------------------------------- | ------------------------ |
| **Source**       | Every field has source location and text      | Flag missing provenance  |
| **Format**       | All dates in ISO 8601, currencies in ISO 4217 | Normalize format         |
| **Consistency**  | No internal contradictions                    | Flag conflict for review |
| **Completeness** | All mandatory fields present or flagged       | List gaps                |
| **Confidence**   | Low-confidence fields identified              | Recommend verification   |

### Self-Interrogation for Uncertain Extractions

For any field with confidence below 0.60:

**Pass 1 -- Source Verification**:

- Is the source text correctly identified?
- Could the text support a different extraction?
- Is there additional context that changes the interpretation?

**Pass 2 -- Cross-Reference**:

- Do other fields in the document support this extraction?
- Is this consistent with the document type and structure?
- Would this be expected in a contract of this type?

**Pass 3 -- Resolution**:

- What is the most likely correct extraction?
- Should this be flagged for manual review?
- What additional information would resolve the uncertainty?

### Confidence Scoring Framework

| Level         | Range     | Criteria                               | Recommended Action     |
| ------------- | --------- | -------------------------------------- | ---------------------- |
| **Definite**  | 0.95-1.0  | Explicit, unambiguous, standard format | Auto-accept            |
| **High**      | 0.80-0.94 | Clear with minor interpretation        | Accept with spot-check |
| **Probable**  | 0.60-0.79 | Inferred or non-standard location      | Review if material     |
| **Possible**  | 0.40-0.59 | Significant interpretation required    | Manual review required |
| **Uncertain** | 0.0-0.39  | Speculative or conflicting             | Flag as unextracted    |

---

## Glass Box Audit Trail

Every extraction output includes a Glass Box section for traceability:

```yaml
glass_box:
  extraction_id: "[unique extraction ID]"
  document: "[document name/identifier]"
  document_type: "[contract category]"
  extraction_timestamp: "[ISO 8601 timestamp]"
  extraction_mode: "[full / core / custom]"
  schema_version: "[schema version]"
  pages_analyzed: "[number]"
  sections_identified: "[number]"
  total_fields_extracted: "[number]"
  fields_definite_confidence: "[number] (0.95+)"
  fields_high_confidence: "[number] (0.80-0.94)"
  fields_moderate_confidence: "[number] (0.60-0.79)"
  fields_low_confidence: "[number] (<0.60)"
  fields_unresolved: "[number]"
  entity_resolution: "[enabled/disabled] - [matches found]"
  overall_confidence: "[HIGH/MEDIUM/LOW] - [numeric score]"
  assumptions:
    - "[List of assumptions made during extraction]"
  limitations:
    - "[Any scope limitations or caveats]"
  manual_review_recommended:
    - "[Fields or sections requiring human verification]"
  reviewer: "AI-assisted extraction - requires verification for operational use"
```

---

## Anti-Patterns

What NOT to do in contract metadata extraction:

1. **Extracting without provenance** -- Every extracted field must have a source location
   and verbatim source text. Extractions without provenance cannot be verified and should
   not be trusted for operational use.

2. **Over-trusting OCR output** -- Scanned documents often have OCR errors. Do not
   auto-accept extractions from scanned documents without flagging OCR quality concerns.

3. **Ignoring document structure** -- Contracts have predictable structures. Party names
   in signature blocks are more reliable than names in recitals. Effective dates in dated
   clauses are more reliable than dates in headers.

4. **Conflating execution and effective dates** -- These are distinct concepts. Execution
   date is when parties signed; effective date is when the contract becomes operative.
   They may be the same but are often different.

5. **Assuming standard meanings** -- "Net 30" may mean 30 days from invoice date, statement
   date, or receipt date depending on context. Extract the full payment term language, not
   just the shorthand.

6. **Ignoring amendments** -- A contract may have been amended multiple times. Without the
   full amendment chain, extractions from the base agreement may be outdated.

7. **Single-pass extraction** -- Read the entire document before extracting. Later sections
   may clarify or override earlier sections. Definitions may change the meaning of terms
   used earlier.

8. **Ignoring incorporated documents** -- If a contract incorporates terms by reference
   (e.g., "subject to Vendor's Standard Terms at [URL]"), those terms are part of the
   contract. Flag incorporated documents not provided.

9. **Normalizing away precision** -- Do not simplify "within thirty (30) calendar days
   following the last day of each calendar quarter" to "quarterly." Preserve the precise
   language and provide a normalized version separately.

10. **Assuming two parties** -- Many contracts have more than two parties (guarantors,
    third-party beneficiaries, multiple affiliates). Extract ALL parties.

11. **Extracting defined terms as general terms** -- If "Confidential Information" is a
    defined term with specific scope, do not treat it as synonymous with general
    confidential information.

12. **Ignoring conditional clauses** -- Many obligations are conditional ("if Customer
    requests an audit..."). Extract the condition as part of the obligation, not just the
    obligation itself.

13. **Extracting from headers/footers** -- Document headers, footers, watermarks, and page
    numbers may contain outdated or template information. Prefer body text.

14. **Failing to flag conflicts** -- If Section 5 says "30 days" and Section 12 says "60
    days" for the same obligation, flag the conflict rather than picking one.

15. **Assuming currency** -- Do not assume USD. Extract the stated currency. If not stated,
    flag as ambiguous.

---

## Writing Standards

Apply these standards to extraction output:

**For field values:**

- Use consistent formats (ISO 8601 dates, ISO 4217 currencies)
- Preserve precision (do not round financial amounts)
- Maintain case as in source document for names
- Normalize whitespace and remove formatting artifacts

**For summaries and notes:**

- Active voice, short sentences
- Specific references ("Section 5.2") not vague ("somewhere in the document")
- Plain language, no jargon
- Confident statements with caveats where appropriate

**Quality gates before delivery:**

1. Can the extraction be verified against the source document?
2. Are all low-confidence extractions flagged?
3. Are there any internal contradictions?
4. Would a human reviewer reach the same extraction?
5. Is the output in the requested format?

---

## External Tool Integration

This skill is designed to work with:

**legalcode-mcp** (if connected):

- Verify entity identifiers against business registries
- Validate governing law jurisdictions
- Cross-reference regulatory requirements
- Check for known problematic clauses

**CLM Systems** (via API):

- Push extracted metadata directly to CLM
- Match counterparties against CLM master data
- Trigger CLM workflows based on extraction results

**Document Processing Tools**:

- Invoke OCR for scanned documents
- Parse complex document structures
- Handle multiple file formats

**Without external tools:**

- Extraction proceeds with available document content
- Entity resolution is disabled or manual
- Flag verification requirements in output

---

## Localization Notes

This skill is jurisdiction-agnostic but extraction accuracy varies by:

**Language:**

- Primary support for English-language contracts
- Bilingual contracts: extract from both language versions if material differences
- Non-English contracts: flag language for specialized processing

**Jurisdiction-specific formats:**

- US: EIN, state of incorporation, Delaware/Nevada conventions
- UK: Companies House number, registered office
- EU: VAT numbers, GDPR references, local entity types (GmbH, SAS, B.V.)
- Other: Flag jurisdiction for specialized processing

**Local conventions:**

- Date formats (MM/DD/YYYY vs. DD/MM/YYYY)
- Currency notation
- Entity type suffixes

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis combining contract metadata
extraction best practices, CLM integration patterns, SALI standards alignment, and
Legalcode quality frameworks into a comprehensive metadata extraction skill. Incorporates
research on AI-powered contract analytics, structured data extraction schemas, and
enterprise CLM requirements.

---

## Related Skills

- **legalcode-obligation-tracker**: For deep obligation extraction and tracking
- **legalcode-contract-review**: For clause-by-clause legal analysis
- **legalcode-contract-comparison**: For comparing contracts against templates or prior versions
- **legalcode-contract-risk-scorer**: For detailed risk assessment
