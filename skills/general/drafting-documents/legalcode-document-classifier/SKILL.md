---
name: legalcode-document-classifier
description: Classify documents for e-discovery by relevance, privilege, and issue coding. Generates confidence-scored
  classification decisions, hot document flags, privilege log entries, and production-ready summaries
  for civil and commercial litigation. Use when conducting first-pass or second-pass document review,
  organizing a privilege log, identifying key custodian documents, applying issue codes to a review set,
  running quality control on a classified batch, or preparing a production transmittal. Supports Technology-Assisted
  Review (TAR) validation workflows, inadvertent-disclosure analysis, clawback procedures under FRE 502,
  and cross-border privilege assessment. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers; deepest
  coverage for US federal (FRCP), US state, UK, EU, and cross-border matters.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Document Classifier

> **Disclaimer**: This skill provides a framework for AI-assisted e-discovery document
> classification. It does not constitute legal advice. All outputs — including privilege
> determinations, responsiveness calls, and privilege log entries — must be reviewed and
> approved by a qualified attorney licensed in the relevant jurisdiction before use or
> reliance. Privilege law is jurisdiction-specific and fact-intensive; a classification
> that is correct in one jurisdiction or context may be incorrect in another. Statutory
> and case law references cited from memory carry hallucination risk — verify against
> authoritative sources before relying on them. Nothing in this skill creates an
> attorney-client relationship.

---

## Purpose and Scope

This skill classifies documents for e-discovery review and generates the structured outputs
litigation teams need: privilege log entries, responsiveness determinations, issue codes,
hot document flags, and production summaries.

**Covers:**

- Relevance classification: RESPONSIVE / NON-RESPONSIVE / NEEDS-REVIEW
- Privilege classification: AC (attorney-client) / WP (work product — ordinary and opinion) / JD (joint defense/common interest) / NOT-PRIVILEGED / PRIVILEGE-REVIEW
- Issue coding: hierarchical issue → sub-issue → fact coding with hot document flags
- Privilege log entry generation: functional descriptions compliant with FRCP 26(b)(5)(A)
- Redaction coding: PRIV / PII / CONFIDENTIAL / SCA (sensitive company affairs)
- Quality control: sampling frameworks, conflict detection, elusion rate analysis
- TAR/predictive coding validation: recall, precision, F-score workflows
- Clawback and inadvertent disclosure: FRE 502(d) order drafting and claw-back letters
- Production transmittal summaries: Bates ranges, metadata fields, load file specs

**Does not:**

- Provide legal advice or replace attorney judgment on privilege determinations
- Guarantee compliance with any specific court order or case-specific protocol
- Substitute for a litigation hold or ESI preservation analysis (see
  `legalcode-litigation-hold` if available)
- Classify government or classified national security documents

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The applicable procedural rules, privilege law,
and discovery obligations depend on the forum (court) and substantive law of the matter.

[JURISDICTION-SPECIFIC] When localizing, identify and apply:

| Jurisdiction               | Key Rules / Statutes                                                                                                                                           |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **US Federal (FRCP)**      | FRCP Rules 26, 34, 45; Federal Rules of Evidence 501, 502; 28 U.S.C. § 1782                                                                                    |
| **US State courts**        | Vary; most follow FRCP model with state-specific modifications                                                                                                 |
| **UK**                     | Civil Procedure Rules (CPR) Parts 31, 31.6 standard disclosure; Legal Advice Privilege; Litigation Privilege; Three Rivers (No 6) [2004] UKHL 48               |
| **EU / Continental**       | National civil procedure codes; generally more limited discovery obligations; GDPR Art. 5(1)(b) purpose limitation on cross-border data transfer for discovery |
| **Cross-border (US → UK)** | US privilege may not be recognized by UK courts; UK in-house counsel privilege narrower than US; conflict of laws analysis required                            |

[JURISDICTION-SPECIFIC] Privilege scope differences to flag:

- **US**: Attorney-client privilege extends to in-house counsel communications broadly; work product protects materials prepared in anticipation of litigation
- **UK**: Legal advice privilege is narrower; Three Rivers (No 6) restricts who is the "client" in large organizations; litigation privilege requires dominant purpose test
- **EU**: In-house counsel generally cannot assert legal professional privilege before EU competition authorities (AM&S/Akzo Nobel line)
- **Australia**: Common law privilege (Evidence Act 1995 s.118-126); dominant purpose test for litigation privilege

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses when:

- The answer would change classification outcomes
- Privilege analysis requires factual context only the user can supply
- The applicable procedural rules are ambiguous
- The coding protocol or issue code structure is undefined

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

### Step 1: Accept the Document Set

Accept documents in any of these formats:

- **Single document**: Paste text, provide file path, or share a document directly
- **Batch list**: A list of document references (Bates numbers, file names, or excerpts)
  with associated metadata (date, author, recipient, subject, file type)
- **Metadata-only set**: A spreadsheet or structured list without full document text —
  for first-pass metadata triage
- **Review platform export**: A CSV or JSON export from a review platform (Relativity,
  Everlaw, Logikcull, etc.)

If no document is provided, ask the user to supply one or describe the classification task.

### Step 2: Gather Matter Context

**⟁ CLARIFY** — Before beginning, ask:

1. **Matter type**: What type of litigation or proceeding?
   - Options: US federal civil litigation, US state court litigation, UK civil litigation,
     Regulatory investigation (specify regulator), Internal investigation, International
     arbitration, Other
   - _Why this matters_: Determines which procedural rules govern privilege and
     responsiveness, and which issue code structure to use.

2. **Party role**: Which side is conducting the review?
   - Options: Plaintiff, Defendant, Third-party subpoena respondent, Regulator/government,
     Neutral (court-appointed special master)
   - _Why this matters_: Determines the perspective for responsiveness and issue coding;
     privilege analysis is the same but log format may vary by party.

3. **Document request scope**: What is the user required to produce?
   - Free text or list: Paste the relevant document requests (RFPs) or describe the
     subject matter. Prompt: "Paste the relevant RFPs, or describe the topics at issue."
   - _Why this matters_: Defines responsiveness. Without this, responsiveness calls are
     guesses.

4. **Issue code structure**: Is there an existing coding guide?
   - Options: I have a coding guide (share it), Use the default structure in this skill,
     I need help building a coding guide from the RFPs
   - _Why this matters_: Issue coding without a defined structure produces inconsistent
     results across reviewers and review passes.

5. **Privilege agreement**: Is there a protective order or FRE 502(d) order in place?
   - Options: Yes (share or describe key terms), No, Unknown
   - _Why this matters_: A 502(d) order changes the inadvertent disclosure/clawback
     analysis. The absence of one increases risk from inadvertent production.

6. **Privilege log format**: What format is required?
   - Options: FRCP default (document-by-document Vaughn Index), Categorical log,
     Metadata-only log, Court-ordered format (describe), Let the skill decide
   - _Why this matters_: Log format affects the level of detail required per entry.

### Step 3: Load the Coding Protocol

Look for an existing coding protocol or review manual in the matter files or provided
context. The protocol should define:

- **Responsiveness criteria**: Which topics, date ranges, custodians, and document types
  are within scope
- **Privilege criteria**: Which privilege types apply and the factual elements for each
- **Issue code hierarchy**: The tree of issues → sub-issues → facts
- **Hot document criteria**: What makes a document "hot" for this matter
- **Redaction triggers**: PII, trade secrets, confidentiality designations

**If no coding protocol is configured:**

**⟁ CLARIFY** — Inform the user that no protocol was found. Ask:

- **Option A: Build a coding guide now** — Extract RFPs and case facts to generate a
  preliminary coding guide with responsiveness criteria, privilege criteria, and a proposed
  issue code hierarchy. Faster to classify consistently once built.
- **Option B: Classify using default framework** — Apply the default classification
  framework in this skill using general litigation principles. Mark classifications as
  "PROTOCOL-PENDING" and flag for confirmation.
- **Option C: Metadata triage only** — Classify based on metadata fields (date, author,
  recipient, subject) without reading document content, to prioritize which documents to
  review fully.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Read the forum court, applicable procedural rules, and privilege law. Use **legalcode-mcp**
to retrieve the governing privilege rules.

**Research process:**

1. **Identify the governing forum** from the matter context.

   **⟁ CLARIFY** — If any of the following are true, ask before proceeding:
   - Forum is unclear or a cross-border matter (multiple jurisdictions may apply)
   - Privilege law of state is different from forum state (diversity jurisdiction)
   - Regulatory investigation with its own privilege standards (SEC, DOJ, FCA, etc.)

2. **Search legalcode-mcp** for the applicable privilege law:
   - Attorney-client privilege elements in the governing jurisdiction
   - Work product doctrine scope and ordinary vs. opinion work product distinction
   - Joint defense / common interest privilege requirements
   - In-house counsel privilege scope
   - Crime-fraud exception standards
   - Subject matter waiver doctrine
   - FRE 502 / equivalent inadvertent disclosure rules

3. **Save relevant results** to a local temporary file (e.g.,
   `/tmp/legalcode-discovery-authority.md`). Structure as:

   ```markdown
   # Discovery Authority Reference — [Matter Name]

   ## Forum: [Court / Jurisdiction]

   ## Date: [date]

   ### Attorney-Client Privilege

   - [Elements, key cases, statutory authority]

   ### Work Product Doctrine

   - [Scope, ordinary vs. opinion, key cases]

   ### Joint Defense Privilege

   - [Requirements, key cases]

   ### FRE 502 / Inadvertent Disclosure

   - [Applicable rule or equivalent]
   ```

4. **Use this reference** throughout the classification analysis. Mark any citation
   sourced from legalcode-mcp as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Proceed with general privilege knowledge
- Mark all legal authority with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — manual verification required"`

### Step 5: Classify Each Document

Apply the three-dimension classification to each document. Run all three dimensions in
parallel; they are independent determinations.

**⟁ CLARIFY** — For large batches (100+ documents):

- Ask whether to perform full content analysis or metadata-priority triage
- Ask whether to produce a per-document log or a batch summary
- Ask whether to flag "borderline" documents separately for human review

#### Dimension 1: Relevance / Responsiveness

Determine whether the document is responsive to the outstanding discovery requests.

| Code                   | Meaning                                                      | Action                                                                      |
| ---------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------- |
| **RESPONSIVE**         | Document falls within scope of one or more RFPs              | Include in production (unless privileged); apply issue codes                |
| **NON-RESPONSIVE**     | Document falls outside all RFPs                              | Withhold from production; no privilege log entry needed                     |
| **RESPONSIVE-PARTIAL** | Document contains both responsive and non-responsive content | Produce responsive portions; redact non-responsive portions with basis code |
| **NEEDS-REVIEW**       | Borderline or ambiguous responsiveness                       | Escalate to senior attorney for determination                               |

**Responsiveness analysis factors:**

- Temporal scope: Is the document within the specified date range?
- Custodian scope: Is the author or recipient a custodian within the collection scope?
- Subject matter scope: Does the document relate to a topic covered by any RFP?
- FRCP 26(b)(1) proportionality: Even if technically responsive, flag if the marginal
  relevance is low relative to the burden of reviewing/producing it.

[JURISDICTION-SPECIFIC] Under FRCP 26(b)(1) (post-2015 amendment), responsiveness is not
sufficient alone — production must also be proportional to the needs of the case. Under
pre-2015 standards ("reasonably calculated to lead to discovery of admissible evidence"),
the standard was broader. Confirm which version applies.

#### Dimension 2: Privilege

Determine whether the document is protected from disclosure by privilege.

##### Attorney-Client Privilege (AC)

**Elements** [VERIFY for jurisdiction]:

1. Communication between an attorney and client (or prospective client)
2. Made in confidence (no third-party present without necessity)
3. For the purpose of seeking or giving legal advice
4. Not waived (no disclosure to non-privileged parties)

**Indicators of AC privilege:**

- Document is a communication between in-house/outside counsel and client personnel
- Subject line or content references legal advice, legal matter, or litigation
- Communication is marked "Attorney-Client Privileged," "Legal Advice," or similar
- Attorney is a sender, recipient, or cc'd party in a legal advisory capacity

**Red flags that may defeat AC privilege:**

- Attorney was acting as a business advisor, not legal advisor
- Communication was shared with third parties outside the privilege circle
- In-house attorney was on distribution as a "business as usual" cc
- Document is a client-to-client communication where attorney is merely cc'd
- "Dual purpose" communication (part business, part legal) — may not be privileged
  if dominant purpose was business [JURISDICTION-SPECIFIC]

[JURISDICTION-SPECIFIC] **US in-house counsel**: Privilege applies to legal advice
communications; business advice does not qualify. Courts look at whether attorney wore
"legal hat" vs. "business hat." **UK in-house counsel (Three Rivers No 6)**: Much
narrower — only communications from the specific employees authorized to seek/receive
legal advice are protected, not communications from lower-level employees.

##### Work Product Doctrine (WP)

**Elements** [VERIFY for jurisdiction; US: FRCP 26(b)(3)]:

1. Document or tangible thing
2. Prepared by or for a party or its representative (including attorney)
3. In anticipation of litigation or for trial

**Two tiers:**
| Tier | Label | Protection Level | Overcome by? |
|------|-------|-----------------|-------------|
| Ordinary work product | WP-ORD | Strong but qualified | Showing of substantial need + inability to obtain equivalent without undue hardship |
| Opinion work product | WP-OPN | Near-absolute | Only in extraordinary circumstances; direct at-issue waiver |

**Indicators of work product:**

- Document prepared after a specific claim arose or was reasonably anticipated
- Document contains legal analysis, strategy, or impressions
- Document created by attorney, paralegal, or at attorney's direction
- Document is a draft pleading, legal memorandum, or deposition outline
- Investigative notes or interview summaries prepared by counsel

**Distinctions:**

- Business records created in the ordinary course of business are NOT work product
  even if later relevant to litigation
- Documents created before litigation was reasonably anticipated are NOT work product
- Ordinary factual investigation materials may be ordinary work product only

##### Joint Defense / Common Interest Privilege (JD)

**Elements** [VERIFY for jurisdiction]:

1. Communication between co-parties (defendants or potential co-defendants) or their counsel
2. Made pursuant to a joint defense agreement (JDA) or common interest arrangement
3. In furtherance of a common legal interest (not merely common business interest)
4. Made in confidence

**Indicators:**

- Reference to a joint defense agreement or common interest agreement
- Communication between counsel for two or more co-defendants or related parties
- Content addresses shared litigation strategy, common legal exposure, or coordinated defense

**Risk areas:**

- JDA parties who later become adverse — privilege may dissolve
- Common interest must be legal, not merely commercial
- JDA should be in writing to be defensible

##### Classification Codes

| Code                  | Privilege Basis                              | Log Required?                           |
| --------------------- | -------------------------------------------- | --------------------------------------- |
| **PRIVILEGED-AC**     | Attorney-client privilege                    | Yes                                     |
| **PRIVILEGED-WP-ORD** | Ordinary work product                        | Yes                                     |
| **PRIVILEGED-WP-OPN** | Opinion work product                         | Yes — note opinion WP in description    |
| **PRIVILEGED-JD**     | Joint defense / common interest              | Yes                                     |
| **PRIVILEGED-MULTI**  | Multiple privilege bases                     | Yes — list all bases                    |
| **NOT-PRIVILEGED**    | No privilege applies                         | No log entry                            |
| **PRIVILEGE-REVIEW**  | Borderline — requires attorney determination | Escalate; do not produce until resolved |
| **PARTIAL-PRIV**      | Document is partially privileged             | Produce with redactions; note in log    |

#### Dimension 3: Issue Coding

Apply issue codes to all RESPONSIVE, NOT-PRIVILEGED documents (and RESPONSIVE-PARTIAL
portions after redaction). Issue codes capture the substantive relevance of each document
to the claims and defenses in the case.

**Default issue code hierarchy** (customize per matter):

```
RESPONSIVE
├── LIABILITY
│   ├── LIB-KNOWLEDGE — Documents showing party's awareness of key facts
│   ├── LIB-CAUSATION — Documents bearing on causation analysis
│   ├── LIB-INTENT — Documents showing intent, motive, or state of mind
│   └── LIB-NOTICE — Documents establishing notice
├── DAMAGES
│   ├── DAM-QUANTUM — Documents bearing on amount of damages
│   ├── DAM-MITIGATION — Documents bearing on plaintiff's duty to mitigate
│   └── DAM-AVOIDED — Documents showing damages avoided
├── AFFIRMATIVE-DEFENSE
│   ├── DEF-STATUTE-OF-LIMITATIONS — Documents relevant to SOL analysis
│   ├── DEF-COMPARATIVE-FAULT — Documents supporting comparative fault
│   └── DEF-WAIVER — Documents supporting waiver/estoppel defense
├── WITNESS
│   ├── WIT-CREDIBILITY — Documents bearing on witness credibility
│   └── WIT-PRIOR-STATEMENTS — Prior statements by key witnesses
└── HOT
    ├── HOT-ADMISSION — Direct admissions against interest
    ├── HOT-SMOKING-GUN — Documents proving or disproving key allegations directly
    ├── HOT-KEY-CUSTODIAN — From key decision-makers at critical times
    └── HOT-IMPEACHMENT — Documents that contradict known testimony
```

**⟁ CLARIFY** — If the matter involves specialized claims (antitrust, securities fraud,
IP, employment), ask the user whether to apply a specialized issue code template:

- Employment: harassment/discrimination, retaliation, wage-and-hour, leave
- Antitrust: agreement evidence, market definition, competitive effects, damages
- Securities: materiality, scienter, loss causation, reliance
- IP: infringement, validity/invalidity, claim construction, damages (reasonable royalty, lost profits)

### Step 6: Hot Document Flagging

Apply the HOT flag independently of issue codes. A document is HOT when it:

**Substantive criteria (apply any one):**

- Contains a direct admission against interest (e.g., "We knew the product was defective")
- Contradicts a key witness's sworn testimony or public statements
- Shows knowledge, notice, or intent at a critical moment
- Directly proves or disproves a central allegation
- Reveals concealment, destruction, or manipulation of evidence

**Procedural criteria (apply any one):**

- Referenced or cited in a key court filing or deposition
- Marked as an exhibit in any deposition
- Appears in communications on the critical path of the disputed events

**Custodian criteria (apply any one):**

- Authored or received by the most senior decision-makers involved in the disputed matter
- Created or received during the key time window (defined per matter)
- From custodians with the highest document relevance density

**Heat levels:**

| Level    | Criteria                                                         | Action                                     |
| -------- | ---------------------------------------------------------------- | ------------------------------------------ |
| **HOT**  | Meets 2+ criteria above OR contains a direct admission           | Flag immediately; escalate to lead counsel |
| **WARM** | Meets 1 criterion above OR is highly relevant to a central issue | Flag for prioritized review                |
| **COLD** | Responsive but no elevated significance                          | Standard production path                   |

### Step 7: Generate Privilege Log Entries

For each PRIVILEGED document, generate a privilege log entry compliant with FRCP
Rule 26(b)(5)(A) [JURISDICTION-SPECIFIC].

**Required fields (FRCP default; negotiate variations at Rule 26(f) conference):**

| Field                        | Required      | Notes                                        |
| ---------------------------- | ------------- | -------------------------------------------- |
| Sequence number              | Yes           | Unique identifier (e.g., PRIV-001)           |
| Bates / Doc ID               | If available  |                                              |
| Date                         | Yes           | Date of document creation                    |
| Document type                | Yes           | Email, memo, letter, draft, attachment, etc. |
| Author(s)                    | Yes           | Including role (attorney/client)             |
| Recipients (To / CC / BCC)   | Yes           | Including role                               |
| Privilege basis              | Yes           | AC / WP-ORD / WP-OPN / JD / MULTI            |
| Functional description       | Yes           | See standards below                          |
| Redaction basis (if partial) | If applicable | PRIV / PII / CONFIDENTIAL                    |

**Functional Description Standard:**

The description must reveal enough to allow assessment of the privilege claim without
disclosing the privileged content itself.

DO include:

- The general subject matter of the legal advice sought or given
- The type of legal matter (litigation, regulatory, transactional)
- The relationship between author and recipient establishing privilege
- For work product: the litigation or anticipated litigation to which it relates

DO NOT include:

- The actual legal advice, analysis, conclusions, or strategy
- Specific facts from the document
- Quotes or paraphrases of privileged content
- Detail so specific that the description itself discloses the privileged matter

**Functional description templates:**

_Attorney-client email:_

> "Email dated [DATE] from [NAME], [outside/in-house] counsel, to [NAME], [Title], containing
> legal advice regarding [general subject] in connection with [matter/transaction/regulatory proceeding].
> Communication reflects [counsel's legal analysis / client's request for legal guidance] on
> [general legal issue]."

_Work product memo:_

> "Memorandum dated [DATE] prepared by [NAME], counsel, for [NAME/firm internal use], containing
> counsel's mental impressions, legal conclusions, and analysis prepared in anticipation of
> litigation arising from [general subject matter]. Reflects attorney's legal strategy and
> assessment of [general legal issue]."

_Joint defense communication:_

> "Email dated [DATE] from [NAME], counsel for [Party A], to [NAME], counsel for [Party B],
> exchanging legal analysis and defense strategy in connection with [general subject] pursuant to
> Joint Defense Agreement dated [DATE]. Communication made in furtherance of common defense interest."

**⟁ CLARIFY** — For categorical privilege logs (grouping similar documents under one entry):

- Confirm the court allows categorical logs for this matter
- Define the grouping criteria (same privilege type, same date range, same author-recipient pair)
- Apply the NYC Bar categorical log model or court-ordered format

### Step 8: Identify Redaction Needs

For RESPONSIVE documents that contain isolated privileged portions, identify specific
redactions rather than withholding the entire document.

**Redaction coding:**

| Code             | Basis                                                               | Action                                         |
| ---------------- | ------------------------------------------------------------------- | ---------------------------------------------- |
| **PRIV**         | Attorney-client or work product                                     | Redact and include in privilege log            |
| **PII**          | Personally identifiable information (SSN, medical, financial, etc.) | Redact per protective order terms              |
| **AEO**          | Attorneys' Eyes Only designation                                    | Produce with AEO designation                   |
| **CONFIDENTIAL** | Trade secret / proprietary business information                     | Produce under protective order                 |
| **SCA**          | Sensitive company affairs (unrelated to case)                       | [JURISDICTION-SPECIFIC] — confirm court allows |
| **3P-PRIV**      | Third-party privilege claim (not party's privilege)                 | Flag for notification to third party           |

**Redaction log fields:** Doc ID / Bates range, redaction code, page/location, brief basis.

**⟁ CLARIFY** — Before applying redactions:

- Confirm whether the protective order governs PII redaction format
- Confirm whether the court requires OCR text for redacted documents
- Confirm whether metadata must be included or stripped for sensitive fields

### Step 9: Quality Control

Run QC procedures on the classified set before producing or delivering the privilege log.

#### 9a. Consistency Sampling

Sample at minimum 5% of documents in each classification category (or 50 documents,
whichever is greater) and verify coding consistency:

| QC Check                   | Method                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| Responsiveness consistency | Sample NON-RESPONSIVE docs; verify none are clearly responsive                             |
| Privilege consistency      | Sample PRIVILEGED docs; verify elements of the claimed privilege are present               |
| Over-designation check     | Sample PRIVILEGED-AC docs; verify attorney is giving/receiving legal (not business) advice |
| Hot document check         | Sample COLD docs from key custodians and key date range; verify none are actually HOT      |
| Elusion rate               | Sample documents in the "NOT-PRIVILEGED" bin; verify no privileged documents were missed   |

#### 9b. TAR Validation (if applicable)

For Technology-Assisted Review workflows:

| Metric       | Target                    | Flag if                                    |
| ------------ | ------------------------- | ------------------------------------------ |
| Recall       | ≥ 75% (Sedona standard)   | < 75% — expand training set                |
| Precision    | ≥ 75%                     | < 75% — over-inclusive; increase threshold |
| F-score      | ≥ 0.75                    | < 0.75 — rebalance recall vs. precision    |
| Elusion rate | ≤ 1% (high-stakes matter) | > 1% — continue active learning passes     |

Elusion rate = percentage of documents scored as non-responsive that are actually responsive
upon review. Courts may require disclosure of elusion rate in TAR disputes.

[JURISDICTION-SPECIFIC] Da Silva Moore v. Publicis Groupe, 287 F.R.D. 182 (S.D.N.Y. 2012)
approved TAR with transparency about the process. Courts generally require parties to
disclose the TAR methodology, training set parameters, and validation metrics if challenged.

#### 9c. Conflict Detection

Flag and resolve conflicts before production:

- Same document coded RESPONSIVE by one reviewer and NON-RESPONSIVE by another
- Same attorney coded as PRIVILEGED by one reviewer and NOT-PRIVILEGED by another
- Document produced in a prior matter now coded PRIVILEGED (may be inconsistent position)

### Step 10: Inadvertent Disclosure and Clawback

If a privileged document has been inadvertently produced, apply the clawback procedure.

**FRE 502 analysis** [JURISDICTION-SPECIFIC]:

| Issue                      | FRE 502(b) Default                                                                               | FRE 502(d) Order Effect                                                  |
| -------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| Waiver standard            | Inadvertent production does NOT waive privilege if reasonable steps taken to prevent and correct | Court order can provide absolute protection regardless of reasonableness |
| Claw-back right            | Yes, if timely and steps were reasonable                                                         | Yes, regardless of care taken                                            |
| Receiving party obligation | Must return/destroy/sequester promptly upon notice                                               | Must comply with court order                                             |

**Clawback letter elements:**

1. Identification of the inadvertently produced document(s) (Bates numbers)
2. The privilege basis claimed
3. Demand for return/destruction and confirmation
4. Citation to FRE 502(b) or the applicable 502(d) order
5. Reservation of rights

**⟁ CLARIFY** — If a privileged document has been produced:

- Was there a 502(d) order? (If yes, protection is strong regardless of care taken)
- Has the receiving party used the document in any filing or deposition? (If yes, may need
  court intervention to claw back)
- How many documents were involved? (Systematic production may indicate inadequate review
  procedures that could affect the reasonableness finding)

### Step 11: Compile Outputs

Assemble the classification deliverables:

1. **Classification summary**: Counts by category (RESPONSIVE / NON-RESPONSIVE / PRIVILEGED
   by type / HOT / WARM / COLD / NEEDS-REVIEW)
2. **Privilege log**: All PRIVILEGED documents in the required format
3. **Redaction log**: All RESPONSIVE-PARTIAL documents with redaction basis
4. **Hot document report**: All HOT and WARM documents with brief explanations
5. **Issue code distribution**: Count of documents by issue code
6. **QC report**: Sampling results, TAR metrics (if applicable), conflicts resolved
7. **Production transmittal summary**: Documents to be produced, Bates ranges, metadata fields

### Step 12: Quality Verification

Before delivering any output, run the quality checks in the **Quality Assurance Framework**
section below.

---

## Classification Framework Summary

### Responsiveness Classification

| Code         | Label              | Criteria                                                           |
| ------------ | ------------------ | ------------------------------------------------------------------ |
| R            | RESPONSIVE         | Within temporal scope + custodian scope + subject matter of ≥1 RFP |
| NR           | NON-RESPONSIVE     | Fails all three criteria                                           |
| RP           | RESPONSIVE-PARTIAL | Responsive portions co-exist with non-responsive portions          |
| NR-B         | BORDERLINE         | Marginally responsive; apply proportionality filter                |
| NEEDS-REVIEW | ESCALATE           | Ambiguous; requires senior attorney determination                  |

### Privilege Classification

| Code        | Label                 | Elements                                                          |
| ----------- | --------------------- | ----------------------------------------------------------------- |
| PRIV-AC     | Attorney-Client       | Attorney ↔ client; confidential; legal advice purpose; no waiver  |
| PRIV-WP-ORD | Ordinary Work Product | Prepared by/for party; in anticipation of litigation; not opinion |
| PRIV-WP-OPN | Opinion Work Product  | Same as WP-ORD + contains mental impressions/legal conclusions    |
| PRIV-JD     | Joint Defense         | Co-parties; JDA; common legal interest; confidential              |
| PRIV-MULTI  | Multiple Bases        | Two or more bases apply; list all in log                          |
| NP          | Not Privileged        | No privilege basis applies                                        |
| PR          | Privilege Review      | Borderline; escalate before any production                        |
| PP          | Partial Privilege     | Privilege applies to portions only; redact and produce balance    |

### Document Heat Classification

| Code | Label         | Criteria                                                              |
| ---- | ------------- | --------------------------------------------------------------------- |
| HOT  | Hot Document  | 2+ indicators OR direct admission / smoking gun; escalate immediately |
| WARM | Warm Document | 1 indicator; prioritize for attorney review                           |
| COLD | Cold          | Responsive but no elevated significance                               |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                       | Fail Action                         |
| -------------- | ------------------------------------------------------------------------------------------ | ----------------------------------- |
| **Source**     | Every privilege determination cites a specific rule, statute, or established legal element | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All privilege log entries follow a consistent, jurisdiction-appropriate format             | Standardize format                  |
| **Currency**   | Every cited rule or statute is checked for amendments (e.g., FRCP Dec 2025 amendments)     | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within the matter's governing procedural law                                | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                  | Add confidence qualifier            |

### Self-Interrogation for High-Consequence Classifications

For any document coded PRIVILEGED (especially AC or WP) or HOT, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Do the claimed privilege elements actually appear in
or about this document? Would a court upholding a challenge to this privilege log entry
find the claim facially valid?

**Pass 2 — Completeness**: Have all relevant privilege bases been considered? Is there
an argument the document is NOT privileged that has not been addressed?

**Pass 3 — Challenge**: What is the strongest argument that this document is NOT
privileged? Under what circumstances (crime-fraud exception, subject matter waiver,
at-issue waiver) might the privilege be defeated?

### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                                                  |
| ------------ | --------- | ------------------------------------------------ | ------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear privilege elements present; no waiver risk | Classify with confidence                                |
| **High**     | 0.80–0.94 | Strong privilege indicators; minor questions     | Classify with brief caveat                              |
| **Probable** | 0.60–0.79 | Most elements present; some ambiguity            | Classify and flag for senior review                     |
| **Possible** | 0.40–0.59 | Genuinely uncertain; elements disputed           | PRIVILEGE-REVIEW; senior determination required         |
| **Unlikely** | 0.0–0.39  | Weak or absent privilege basis                   | NOT-PRIVILEGED unless human review determines otherwise |

Apply confidence scoring per document to:

- Responsiveness call
- Privilege claim
- Hot document determination

Documents with Probable or lower confidence must be reviewed by a supervising attorney
before inclusion in the privilege log or production.

---

## Anti-Patterns

The following are the most common and consequential errors in e-discovery document
classification. Do NOT do these:

1. **Over-designating routine business communications as privileged** — Marking all
   emails that cc an attorney as "PRIVILEGED-AC" without verifying the attorney was
   acting in a legal (not business) advisory capacity. This produces an inflated, legally
   vulnerable privilege log that invites sanctions and adverse inferences.

2. **Under-designating true opinion work product** — Coding an attorney's litigation
   strategy memorandum as merely ordinary work product (WP-ORD) when it contains mental
   impressions and legal conclusions. Opinion work product enjoys near-absolute protection;
   failing to distinguish it weakens the protection asserted.

3. **Privilege log descriptions that are too vague** — Generic descriptions such as
   "Attorney-client communication re: legal matter" do not satisfy FRCP 26(b)(5)(A)
   and will be found deficient by courts. Every entry needs a functional description
   with enough specificity to allow privilege assessment.

4. **Privilege log descriptions that reveal privileged content** — Over-describing to
   appear thorough and inadvertently disclosing the legal advice, strategy, or analysis
   itself. The description should describe the nature of the communication without
   disclosing what was actually said.

5. **Treating in-house counsel as automatically creating privilege** — Copying in-house
   counsel on a distribution list does not make a document privileged. The attorney must
   be present in a legal advisory capacity. Particularly problematic in UK and EU matters
   where in-house counsel privilege is narrower [JURISDICTION-SPECIFIC].

6. **Ignoring the crime-fraud exception** — Classifying a document as privileged without
   considering whether it was created in furtherance of a crime or fraud. If facts suggest
   a crime-fraud exception applies, flag for immediate senior attorney attention rather than
   logging without note.

7. **Failing to identify partial privilege** — Withholding an entire multi-page document
   because one paragraph is privileged, instead of producing the non-privileged portions
   with targeted redactions. Courts disfavor over-withholding and may order production of
   entire documents as a sanction.

8. **No 502(d) order in high-volume review** — Proceeding through a large-scale document
   review without a court-ordered FRE 502(d) clawback agreement. A 502(d) order provides
   absolute protection against waiver from inadvertent production; its absence creates
   ongoing waiver risk.

9. **Classifying work product based on subject matter, not timing** — Classifying
   documents as work product solely because they relate to a topic that became litigated,
   without verifying they were prepared "in anticipation of litigation." Documents created
   in the ordinary course of business before litigation was reasonably anticipated are not
   protected.

10. **Inconsistent custodian-by-custodian review** — Applying different privilege criteria
    or responsiveness standards to documents from different custodians. Privilege law does
    not vary by custodian. Inconsistency creates conflicts in the log and may expose the
    review to court-ordered re-review.

11. **Missing embedded attachments** — Classifying an email as non-privileged without
    reviewing its attachments for privilege. Privileged attachments make the parent
    communication effectively privileged; non-privileged emails with privileged attachments
    require careful handling.

12. **Failing to log forwarded privilege chains** — When a privileged email is forwarded
    or included in a chain with a third party, the forwarded version may no longer be
    privileged (waiver by disclosure). Each version of a forwarded chain must be analyzed
    separately.

13. **Not checking for subject matter waiver** — When a party produces privileged
    communications on a topic in litigation, it may inadvertently waive privilege for all
    communications on the same topic. Always flag selective disclosure of privileged
    materials for lead counsel review.

14. **Hot document suppression bias** — Unconsciously coding damaging documents as
    non-responsive or under-classifying them to avoid production. This creates both
    professional responsibility and obstruction risks. Apply responsiveness criteria
    neutrally regardless of whether the document is favorable or unfavorable.

15. **Using metadata-only triage as a substitute for content review** — Classifying
    documents based solely on subject line, author, or recipient without reading the
    content. A neutral-looking subject line may contain damaging admissions; an attorney's
    name in a cc field does not alone create privilege.

16. **No quality control on non-responsive documents** — QC sampling only the responsive
    set and not sampling the non-responsive set for missed responsiveness. Elusion rate
    testing on non-responsive documents is required to validate the completeness of the
    review.

17. **Ignoring cross-border privilege asymmetry** — Classifying a US-privileged document
    as protected without flagging that the same document may not be privileged in a
    parallel UK or EU proceeding. [JURISDICTION-SPECIFIC]

18. **Applying US work product standards to foreign-produced documents** — Work product
    doctrine is a US procedural protection. Documents produced by non-US counsel in
    non-US proceedings may not qualify, particularly if the litigation was not reasonably
    anticipated at the time.

---

## Writing Standards

Before delivering any classification output:

1. **Use precise privilege terminology** — "Attorney-client privilege" not "lawyer
   privilege"; "ordinary work product" not "attorney work product" (which conflates
   both tiers); "joint defense privilege" not "common interest agreement."

2. **Distinguish privilege from confidentiality** — A confidential document is not
   automatically privileged. Confidentiality is a fact that supports (but does not
   establish) privilege; it is not itself a legal protection against discovery.

3. **State elements explicitly** — When classifying a document as privileged, identify
   the specific elements that are satisfied, not just the conclusion. This makes the
   log defensible and the reasoning auditable.

4. **Flag uncertainty, do not suppress it** — If you are unsure whether privilege
   applies, say so explicitly with a PRIVILEGE-REVIEW code and a brief note. Do not
   default to withholding to "play it safe" — over-withholding has its own legal
   consequences.

5. **Apply consistent terminology throughout** — Do not use "responsive" and "relevant"
   interchangeably. Responsiveness is a discovery determination (within the scope of
   RFPs); relevance is an evidentiary determination (admissible evidence standard).
   These overlap but are not identical.

6. **Date references in privilege log entries** — Use ISO format (YYYY-MM-DD) or the
   format required by the applicable court order. Do not leave date fields blank.

7. **Identify attorney roles clearly** — In the author/recipient fields of privilege
   logs, identify whether each attorney is "outside counsel," "in-house counsel," or
   "co-counsel" to support the privilege claim.

---

## External Tool Integration

### legalcode-mcp

Use legalcode-mcp in Step 4 to research jurisdiction-specific privilege rules:

**With legalcode-mcp connected:**

- Search for the applicable privilege rules in the forum jurisdiction
- Verify current FRCP amendments (most recent: December 1, 2025)
- Research any case-specific court orders or standing discovery rules
- Verify TAR case law in the forum (particularly for contested TAR methodology)
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed using general privilege knowledge
- Mark all statutory and case law references with [VERIFY]
- Note: `legalcode_mcp: "Not connected — manual verification required"`
- Focus QC effort on privilege classifications rather than legal authority verification

### Review Platform Integration

This skill can process exports from common review platforms:

| Platform    | Export Format                                          | Import Notes                                       |
| ----------- | ------------------------------------------------------ | -------------------------------------------------- |
| Relativity  | CSV with metadata fields + text extract                | Map metadata columns to classification fields      |
| Everlaw     | CSV / JSON export                                      | Include document text for content analysis         |
| Logikcull   | CSV export with tag fields                             | Use tag fields to import existing first-pass codes |
| Concordance | DAT load file + text                                   | Parse DAT format; map fields per load file spec    |
| Generic     | Any CSV with: Date, From, To, CC, Subject, Body, Bates | Standard import                                    |

---

## Glass Box Audit Trail

Include this YAML block in every classification run output:

```yaml
glass_box:
  skill_name: "legalcode-document-classifier"
  mode: "Classification run"
  matter: "[Matter name / case caption — or 'Not provided']"
  forum: "[Court and jurisdiction — or 'Not provided']"
  governing_privilege_law: "[Jurisdiction and key rules]"
  documents_classified: "[total number]"
  responsive: "[count]"
  non_responsive: "[count]"
  privileged_ac: "[count]"
  privileged_wp_ord: "[count]"
  privileged_wp_opn: "[count]"
  privileged_jd: "[count]"
  not_privileged: "[count]"
  privilege_review_escalations: "[count]"
  hot_documents: "[count]"
  warm_documents: "[count]"
  legalcode_mcp: "Connected / Not connected"
  authority_citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  qc_sampling_rate: "[percentage sampled]"
  tar_metrics_applied: "Yes — recall [X], precision [X], F-score [X], elusion [X] / No"
  confidence_summary: "HIGH / MEDIUM / LOW — [rationale]"
  privilege_log_format: "[FRCP default / Categorical / Court-ordered]"
  fre_502_order: "Yes / No / Unknown"
  inadvertent_productions_flagged: "[count or 'None']"
  limitations:
    - "[Any scope limitations, assumptions, or jurisdictional caveats]"
    - "[Any documents excluded from review]"
  reviewer: "AI-assisted — requires qualified attorney review and approval"
```

---

## Localization Notes

### United States (Federal)

- **Primary rules**: FRCP 26(b), 26(b)(3), 26(b)(5); FRE 501, 502
- **December 2025 FRCP amendments**: Rule 26(b)(5)(A) now requires parties to negotiate
  privilege log format (fields, metadata, narrative) at the Rule 26(f) conference
- **FRE 502(d)**: Court orders provide absolute protection; negotiate before review begins
- **TAR case law**: Da Silva Moore (2012), In re Biomet (2013), In re Rio Tinto (2016),
  Winfield v. City of New York — transparency about process required
- **State courts**: Most follow FRCP model but may differ on privilege scope and discovery
  deadlines; verify [JURISDICTION-SPECIFIC]

### United States (State)

- **California**: California Evidence Code §§ 950-962 (attorney-client); CCP § 2018
  (work product); broader work product protection than federal; mediation privilege CEC § 1115
- **New York**: CPLR § 3101; in-house counsel privilege recognized; attorney work product
  doctrine is absolute for certain materials
- **Delaware**: As above; frequent corporate litigation; frequent use of ADR orders

### United Kingdom

- **Legal Advice Privilege**: Communications between a lawyer and client for the purpose
  of giving or receiving legal advice. Three Rivers (No 6) [2004]: client entity is narrow
  in large organizations.
- **Litigation Privilege**: Documents created for the dominant purpose of litigation that
  is reasonably in contemplation. Broader than US work product; protects third-party
  documents.
- **No work product doctrine equivalent**: UK uses litigation privilege instead.
- **Inspection**: CPR Part 31 governs standard disclosure; "train of inquiry" test abolished
  by CPR 31.6.
- **Cross-border**: Documents privileged under English law may not be privileged under
  US law and vice versa. Analyze both regimes for cross-border matters.

### European Union / Continental

- **Limited discovery**: Most EU jurisdictions do not have US-style disclosure obligations;
  much narrower document production
- **In-house counsel**: AM&S Europe v Commission [1982] ECR 1575 and Akzo Nobel Chemicals
  [2010] CJEU: in-house counsel communications are NOT protected by legal professional
  privilege in EU competition proceedings. [VERIFY for updates]
- **GDPR impact**: Cross-border transfers of personal data for US litigation purposes must
  comply with GDPR Chapter V transfer mechanisms; "litigation exception" is narrow

---

## Output Format Template

Use this template for every classification run output:

---

```markdown
# Document Classification Report

**Matter**: [Case name / matter number]
**Prepared**: [Date]
**Reviewer**: AI-assisted (legalcode-document-classifier) — requires attorney review
**Forum**: [Court and jurisdiction]
**Documents reviewed**: [N]

---

## Classification Summary

| Category                             | Count | % of Total   |
| ------------------------------------ | ----- | ------------ |
| RESPONSIVE                           | [N]   | [%]          |
| NON-RESPONSIVE                       | [N]   | [%]          |
| RESPONSIVE-PARTIAL (needs redaction) | [N]   | [%]          |
| NEEDS-REVIEW (escalate)              | [N]   | [%]          |
| **PRIVILEGED-AC**                    | [N]   | [% of total] |
| **PRIVILEGED-WP-ORD**                | [N]   | [%]          |
| **PRIVILEGED-WP-OPN**                | [N]   | [%]          |
| **PRIVILEGED-JD**                    | [N]   | [%]          |
| **PRIVILEGE-REVIEW** (escalate)      | [N]   | [%]          |
| HOT documents                        | [N]   | [%]          |
| WARM documents                       | [N]   | [%]          |

---

## Privilege Log

| #        | Bates/ID | Date       | Type   | From           | To/CC             | Privilege | Description              | Confidence |
| -------- | -------- | ---------- | ------ | -------------- | ----------------- | --------- | ------------------------ | ---------- |
| PRIV-001 | [Bates]  | YYYY-MM-DD | [type] | [Author, role] | [Recipient, role] | [PRIV-AC] | [Functional description] | [0.0–1.0]  |
| PRIV-002 | ...      | ...        | ...    | ...            | ...               | ...       | ...                      | ...        |

---

## Hot Document Report

| #        | Bates/ID | Date       | From     | To          | Heat | Reason                                                   | Issue Codes     |
| -------- | -------- | ---------- | -------- | ----------- | ---- | -------------------------------------------------------- | --------------- |
| HOT-001  | [Bates]  | YYYY-MM-DD | [Author] | [Recipient] | HOT  | [Brief reason: e.g., "Admission of knowledge of defect"] | [LIB-KNOWLEDGE] |
| WARM-001 | ...      | ...        | ...      | ...         | WARM | ...                                                      | ...             |

---

## Issue Code Distribution

| Issue Code    | Label                 | Count |
| ------------- | --------------------- | ----- |
| LIB-KNOWLEDGE | Liability — Knowledge | [N]   |
| LIB-INTENT    | Liability — Intent    | [N]   |
| DAM-QUANTUM   | Damages — Quantum     | [N]   |
| HOT-ADMISSION | Hot — Admission       | [N]   |
| [other codes] | ...                   | [N]   |

---

## Redaction Log

| #       | Bates/ID | Page(s)   | Redaction Code | Basis                            |
| ------- | -------- | --------- | -------------- | -------------------------------- |
| RED-001 | [Bates]  | [pp. X-Y] | PRIV           | [AC privilege — attorney advice] |
| RED-002 | [Bates]  | [p. Z]    | PII            | [SSN at para. 3]                 |

---

## Escalations Requiring Attorney Review

| #       | Bates/ID | Date       | Issue                                   | Recommended Action                    |
| ------- | -------- | ---------- | --------------------------------------- | ------------------------------------- |
| ESC-001 | [Bates]  | YYYY-MM-DD | [Borderline privilege; confidence 0.55] | Senior attorney review before logging |
| ESC-002 | ...      | ...        | ...                                     | ...                                   |

---

## QC Summary

- Documents sampled: [N] ([%] of classified set)
- NON-RESPONSIVE sampled (elusion check): [N]; problems found: [N]
- PRIVILEGED-AC sampled (over-designation check): [N]; problems found: [N]
- HOT/WARM sampled (under-designation check): [N]; problems found: [N]
- Conflicts resolved: [N]
- TAR metrics (if applicable): Recall [X], Precision [X], F-score [X], Elusion [X%]

---

## Production Transmittal Summary

- Documents to be produced: [N]
- Bates range: [FIRST] – [LAST]
- File format: [TIFF/PDF/Native, per production specs]
- Metadata fields included: [list]
- Load file format: [Concordance DAT / Relativity CSV / other]
- Confidentiality designations applied: [None / CONFIDENTIAL / AEO]
- Documents withheld on privilege: [N] (see privilege log)
- Documents produced with redactions: [N] (see redaction log)

---

## Glass Box Audit Trail

[Insert YAML from Glass Box template above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- US: FRCP Rules 26, 34, 45 (through December 2025 amendments); Federal Rules of Evidence
  501, 502; Hickman v. Taylor, 329 U.S. 495 (1947); Upjohn Co. v. United States, 449 U.S.
  383 (1981); Zubulake v. UBS Warburg, 217 F.R.D. 309 (S.D.N.Y. 2003); Da Silva Moore v.
  Publicis Groupe, 287 F.R.D. 182 (S.D.N.Y. 2012); In re Biomet M2a Magnum Hip Implant
  Products Liab. Litig., No. 3:12-MD-2391 (N.D. Ind. 2013) [VERIFY]
- UK: CPR Part 31; Three Rivers District Council v Governor and Company of the Bank of
  England (No 6) [2004] UKHL 48; Waugh v British Railways Board [1980] AC 521 (dominant
  purpose test) [VERIFY]
- EU: AM&S Europe Ltd v Commission [1982] ECR 1575; Akzo Nobel Chemicals Ltd v Commission
  [2010] CJEU C-550/07 [VERIFY]; GDPR Reg. 2016/679 Art. 5(1)(b)
- EDRM Model and Stages Standards; Sedona Principles (3rd ed. 2018); Sedona Conference
  Commentary on TAR (2023); Sedona Conference Commentary on Privilege Logs (Feb 2024)
- ABA Formal Ethics Opinions on technology and privilege; EDRM Privilege Log Protocol v2.0 (2023)
- USA v. Heppner (SDNY, Feb 2026) — AI-generated documents and privilege [VERIFY]
- Arnold & Porter, "New Privilege Log Rules Are Here" (Dec 2025); ABA Business Law Today,
  "Crafting Effective Privilege Logs" (Nov 2024)

Attribution: Legalcode original synthesis — not derived from or based on any single
external skill. Research-backed creation using the 2-agent research pipeline.
