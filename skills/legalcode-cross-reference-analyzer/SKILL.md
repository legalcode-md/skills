---
name: legalcode-cross-reference-analyzer
description: 'Analyzes document sets for cross-reference integrity: builds a defined terms register, audits
  internal section references, maps inter-document reference chains, detects conflicting provisions, flags
  mismatched dates, and surfaces undefined or orphaned terms. Use when reviewing a contract suite, M&A
  document package, loan facility agreement with schedules, franchise disclosure document, or any multi-document
  transaction set where internal consistency is critical. Also use for single-document integrity checks
  before execution, during due diligence, or after substantial redlining. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC]
  markers. Triggers on: cross-reference check, defined terms audit, internal consistency review, document
  suite integrity, conflicting provisions analysis, undefined terms check, orphaned references, mismatched
  definitions.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Cross-Reference Analyzer

> **Disclaimer**: This skill provides a framework for AI-assisted cross-reference integrity
> analysis. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use. Cross-
> reference errors identified by this skill may not be exhaustive; manual verification is
> required before relying on any finding. Statutory and case law references cited from
> memory carry hallucination risk — verify against authoritative sources before relying on
> them.

---

## Purpose and Scope

This skill performs **cross-reference integrity analysis** on single documents or document
suites. It systematically audits the internal logical consistency of legal documents:
whether terms are defined and used consistently, whether section references point to real
and correct provisions, whether related documents agree on shared definitions, and whether
operative dates and conditions align.

**Covers:**

- Defined terms register: build, audit, and report on every capitalized/defined term
- Internal cross-references: section, clause, exhibit, schedule, and appendix references
- Inter-document cross-references: definitions imported across a document suite
- Conflicting provisions: same subject matter governed by inconsistent terms
- Date and deadline alignment: effective dates, expiry dates, notice periods, and
  condition precedent deadlines
- Undefined terms: operative terms used without definition
- Orphaned definitions: defined terms never used in operative provisions
- Circular definitions: terms defined by reference to themselves (directly or indirectly)
- Version drift: references to a prior version of an attached document

**Does not:**

- Provide substantive legal advice on whether the underlying terms are commercially fair
- Draft new contract language (see drafting-specific skills)
- Replace a full contract review — this is a targeted integrity check, not a commercial
  risk analysis
- Guarantee exhaustive detection — complex, layered document suites require human review
  to confirm all findings

---

## Jurisdiction and Governing Law

This is a **jurisdiction-agnostic** skill. Cross-reference integrity is a structural
property of legal documents independent of the governing law. The analysis does not
depend on the legal system but may produce findings that have jurisdiction-specific
legal consequences.

[JURISDICTION-SPECIFIC] Where cross-reference errors carry jurisdiction-specific legal
consequences, note:

- **Ambiguity resolution**: How courts in the governing jurisdiction resolve ambiguous or
  conflicting provisions (e.g., contra proferentem, ejusdem generis, specific prevails
  over general, later provision prevails) [VERIFY]
- **Incorporation by reference**: Whether a jurisdiction requires specific language to
  incorporate external documents by reference [VERIFY]
- **Priority / order of precedence**: Whether the jurisdiction's courts give effect to
  express priority provisions in commercial contracts [VERIFY]
- **Language requirements**: Whether the jurisdiction requires bilingual documents where
  cross-reference inconsistencies between language versions carry special legal
  significance [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the scope or depth of the analysis
- Multiple valid approaches exist (e.g., full audit vs. focused check)
- Document structure is ambiguous and requires human clarification
- A finding could be an intentional drafting choice rather than an error
- The document set is large enough that prioritization is required

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

- **Files**: PDF, DOCX, TXT, or other text-extractable formats
- **Pasted text**: Contract text pasted directly into the conversation
- **URLs**: Links to documents in a CLM, cloud storage, or document system
- **Multi-document**: Multiple files forming a suite (e.g., Agreement + Schedules +
  Exhibits + Side Letters)

**⟁ CLARIFY** — If the input contains multiple documents, confirm the document set:

1. "Please confirm which documents are in scope:
   - Only the main agreement and its attached schedules/exhibits?
   - The main agreement plus separately executed ancillary documents?
   - A full transaction suite (e.g., SPA + disclosure letter + facility agreement)?
   - A regulatory filing package?"

2. "Which document is the **master** or **primary** document for hierarchy purposes?
   (This determines which document's definitions govern in conflicts.)"

3. "Is there an **order of precedence** clause in any of these documents? If so, which
   document takes priority?"

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the analysis, gather context:

1. **Analysis scope**: What is the primary objective?
   - Options:
     - **Full integrity audit** — All 7 analysis modules (most thorough)
     - **Defined terms only** — Build a complete defined terms register and audit usage
     - **Cross-reference check only** — Focus on section/clause references and inter-document links
     - **Conflicting provisions only** — Find contradictions and inconsistencies
     - **Pre-execution final check** — Quick pass on CRITICAL and HIGH severity items only
     - **Post-redline consistency check** — Focus on areas that changed after the last redline
   - _Why this matters_: A full audit may be impractical for a 300-page facility package;
     scoping to the most valuable modules is often more useful.

2. **Document context**: What type of transaction is this?
   - Options: Commercial contract, M&A transaction suite, Loan/finance documents,
     Real estate transaction, Regulatory filing package, Employment document package,
     Franchise disclosure document, Other
   - _Why this matters_: Different document types have different cross-reference
     architectures; transaction suites require deeper inter-document analysis.

3. **Trigger**: Why is this analysis being run?
   - Options: Pre-execution final review, Post-redline consistency check, Due diligence,
     Dispute — clause interpretation, Remediation of known inconsistency, Routine QA
   - _Why this matters_: Determines whether to flag all findings or focus on findings
     relevant to a specific dispute or gate.

4. **Version information**: Are there multiple versions of any document in the set?
   - If yes: confirm which version is the operative version and whether prior versions
     are in scope for comparison.

If the user provides partial context, proceed with what is available and **state
assumptions explicitly**.

### Step 3: Map the Document Architecture

Before beginning clause-level analysis, build a structural map of the document set.

**3a. Document inventory**

For each document, record:

| #   | Document Name    | Date   | Parties   | Status           | Role in Suite |
| --- | ---------------- | ------ | --------- | ---------------- | ------------- |
| 1   | [Main Agreement] | [date] | [parties] | [Executed/Draft] | Primary       |
| 2   | [Schedule 1]     | [date] | [parties] | [Executed/Draft] | Incorporated  |
| 3   | [Exhibit A]      | [date] | [parties] | [Executed/Draft] | Incorporated  |
| …   | …                | …      | …         | …                | …             |

**3b. Incorporation chain**

Trace every incorporation-by-reference statement:

```
[Document A] § 1.1 — incorporates [Schedule 1]
[Document A] § 12.3 — incorporates [Document B] definitions "as amended from time to time"
[Schedule 1] — references [Exhibit C] for pricing
```

Flag any circular incorporations (A incorporates B which incorporates A) as CRITICAL.

**3c. Order of precedence**

Identify and record any order of precedence clause. If none exists:

**⟁ CLARIFY** — "No order of precedence clause was found. In the event of a conflict
between documents, which should take priority? Options:

- The main agreement governs over all schedules/exhibits
- Schedules govern over the main agreement body (common in financial documents)
- More specific provision governs over general (common law default)
- Later executed document governs over earlier (common law default)
- I'll indicate priorities as we go through the analysis"

### Step 4: Build the Defined Terms Register

Construct a comprehensive register of every defined term in the document set. This is
the foundation for all subsequent analysis.

**4a. Extraction procedure**

Scan every document for:

1. **Explicit definitions**: Terms defined using quotation marks, capitalization with
   surrounding definition language (e.g., "means," "shall mean," "refers to," "has the
   meaning"), or a dedicated Definitions section
2. **Section-level definitions**: Terms defined within the body of operative clauses
   (not just in a central Definitions section)
3. **Incorporated definitions**: Definitions imported by reference from another document
   ("as defined in the Master Agreement," "as such term is defined in the Facility
   Agreement")
4. **Deemed definitions**: Terms defined implicitly by context or by reference to an
   external standard (e.g., "Business Day" with reference to a specified financial
   center)

**4b. Defined terms register format**

Build a register in this format:

```
| Term | Defined In | Section | Definition Summary | Used In | Count | Issues |
|------|-----------|---------|-------------------|---------|-------|--------|
| [Term] | [Doc/Sec] | [§X.X] | [1-line summary] | [Docs/Sections] | [N] | [flags] |
```

Issue flags to assign during register build:

- `UNDEFINED_USAGE` — term appears capitalized/used as defined but has no definition
- `ORPHANED` — term is defined but never appears in operative provisions
- `MULTI-DEFINED` — term is defined differently in two or more documents
- `CIRCULAR` — definition refers back to itself directly or indirectly
- `IMPORTED_UNDEFINED` — definition imported by reference but the source document is
  not in scope or the definition cannot be located
- `VERSION_MISMATCH` — definition imported "as defined in [Document]" but the Document
  in scope differs from the version referenced

**⟁ CLARIFY** — For large document suites with hundreds of defined terms:

- "I've identified [N] defined terms. Would you like the full register, or should I focus
  on terms that have issues (flagged terms only)?"

### Step 5: Audit Defined Terms Usage

For each term in the Defined Terms Register, verify:

**5a. Usage consistency check**

| Test                               | Pass                                                                                        | Fail                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Definition-to-usage alignment**  | Operative use is consistent with the definition                                             | Term is used in a sense the definition does not support                 |
| **Capitalization consistency**     | Term is always capitalized when used as defined and never capitalized when used generically | Mixed capitalization — sometimes defined, sometimes general             |
| **Cross-document consistency**     | Same term has same meaning across all documents in the suite                                | Same word is defined differently in two documents (even if intentional) |
| **Scope consistency**              | Term used only in contexts that fall within the defined scope                               | Term used in contexts that arguably fall outside the defined scope      |
| **Pronoun/substitute consistency** | When a defined term is referred to by shorthand or pronoun, the reference is unambiguous    | "the Agreement" is ambiguous when multiple agreements are in scope      |

**5b. Circular definition detection**

For every definition that refers to another defined term, trace the chain. If the chain
returns to the original term, flag CIRCULAR:

```
"Affiliate" means any entity that Controls, is Controlled by, or is under common
Control with a Party. → "Control" means the ability to direct the management of an
Affiliate. [CIRCULAR: Affiliate → Control → Affiliate]
```

**5c. Near-miss and synonym detection**

Flag terms that appear to describe the same concept but are defined separately:

- "Intellectual Property" vs. "Intellectual Property Rights" vs. "IP"
- "Confidential Information" vs. "Confidential Material" vs. "Confidential Data"
- "Business Day" vs. "Working Day"

**⟁ CLARIFY** — For apparent synonyms: "The document uses both '[Term A]' and '[Term B]'.
Are these intentionally distinct, or should one of them be harmonized? In their current
form, they are treated as separate concepts."

### Step 6: Audit Internal Cross-References

Scan every section, clause, exhibit, and schedule reference within each document.

**6a. Reference types to audit**

| Reference Type                    | Example                                             | Check                                                                |
| --------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------- |
| **Section reference**             | "subject to Section 5.3"                            | Does §5.3 exist? Does its subject matter match the reference?        |
| **Clause reference**              | "pursuant to Clause 12(b)"                          | Does Clause 12(b) exist? Is the reference correct?                   |
| **Exhibit/Schedule reference**    | "as set forth in Exhibit A"                         | Is Exhibit A attached? Does it address the referenced subject?       |
| **Definition section reference**  | "as defined in Section 1"                           | Does Section 1 contain the definition? Is it the correct definition? |
| **Condition precedent reference** | "upon satisfaction of the conditions in Schedule 2" | Does Schedule 2 address conditions precedent? Are they complete?     |
| **Cross-exhibit reference**       | "Schedule 3, Part B, paragraph 4"                   | Does the granular reference exist?                                   |

**6b. Reference integrity tests**

For every internal reference identified:

1. **Existence test**: Does the referenced provision exist in the document?
2. **Subject matter test**: Does the subject matter of the referenced provision match
   what the referring provision says it says?
3. **Completeness test**: Does the referenced provision address everything the referring
   provision expects of it? (e.g., a reference to "the payment schedule in Exhibit C"
   when Exhibit C only partially addresses payment terms)
4. **Version test**: Where exhibits are updated versions of previously executed documents,
   does the reference include a version identifier, and does it match the attached version?

**6c. Broken reference detection**

Flag every reference where:

- The referenced provision does not exist (CRITICAL)
- The referenced provision exists but its subject matter does not match (HIGH)
- The referenced provision is partially responsive but incomplete (MEDIUM)
- The reference is ambiguous (e.g., "as provided above" without a clear antecedent)
  (MEDIUM)

### Step 7: Audit Inter-Document Cross-References

For document suites, trace every cross-document reference.

**7a. Reference chain mapping**

Build a reference chain:

```
Main Agreement §1.1 → "Permitted Transferee" as defined in the SHA
SHA §1 → "Permitted Transferee" means …
```

For each link in the chain, verify:

1. The source document is in scope and the referenced version is current
2. The definition or provision in the referenced document has not been amended since
   the reference was drafted
3. No intermediate document in the chain has been superseded

**7b. Definition import conflicts**

The most common inter-document cross-reference failure: Term X is imported from
Document A into Document B, but Document A has been amended and the definition has
changed, or Document B's context gives the term a meaning inconsistent with the import.

Test for:

- Definition in source document vs. expected meaning in importing document
- Whether amendments to the source document since execution affect imported definitions
- Whether "as amended from time to time" language creates unintended scope creep

**7c. Incorporated document completeness**

For every document incorporated by reference:

1. Is the incorporated document in scope (attached or accessible)?
2. Does it exist in its entirety, or is there a stub?
3. Is the version referenced consistent with the version available?

**⟁ CLARIFY** — When a referenced document is not in scope:

- "The document references [External Document] in [section]. This document is not part
  of the set provided. Should I flag this as an IMPORTED_UNDEFINED reference, or will
  you supply the document for analysis?"

### Step 8: Detect Conflicting Provisions

Scan for provisions addressing the same subject matter with inconsistent terms.

**8a. Conflict categories**

| Conflict Type              | Description                                                                      | Severity Default |
| -------------------------- | -------------------------------------------------------------------------------- | ---------------- |
| **Operative conflict**     | Two provisions directly contradict — both cannot be complied with simultaneously | CRITICAL         |
| **Definitional conflict**  | Same term defined differently in two places                                      | HIGH             |
| **Scope conflict**         | One provision grants rights that another restricts                               | HIGH             |
| **Procedural conflict**    | Two provisions establish different procedures for the same event                 | HIGH             |
| **Numeric conflict**       | Same figure (cap, deadline, threshold) stated differently in two places          | HIGH             |
| **Drafting inconsistency** | Two provisions address same topic differently but both can be complied with      | MEDIUM           |
| **Temporal conflict**      | Two provisions apply to the same period but are inconsistent                     | HIGH             |
| **Hierarchy resolution**   | Conflict addressable by order of precedence                                      | MEDIUM           |

**8b. High-risk conflict zones**

Pay particular attention to conflicts in these areas, which are most frequently
problematic in practice:

- **Liability caps**: Cap stated in the main body vs. cap restated in a schedule or
  exhibit (even minor discrepancies matter)
- **Payment terms**: Different payment periods, rates, or triggers in the main body
  and in a pricing schedule
- **IP ownership**: Ownership allocated differently in the main body vs. a statement
  of work or exhibit
- **Termination triggers**: Termination events listed in the main body vs. termination
  events in an incorporated document
- **Data processing requirements**: Data protection obligations in the main body vs.
  a DPA attachment (different retention periods, breach notification timelines)
- **Non-compete scope**: Non-compete in main body vs. non-compete in a side letter
  (different duration, geography, or activity scope)
- **Governing law**: Different governing law stated in the main body vs. in a
  schedule or exhibit
- **Dispute resolution**: Different dispute mechanisms in the main body vs. in an
  embedded schedule

**8c. Resolution pathway**

For each conflict identified, determine:

1. Does an order of precedence clause resolve it?
2. Does the rule of "specific provision over general provision" resolve it?
3. Does the rule of "later provision over earlier provision" resolve it?
4. Is the conflict irresolvable on the face of the document? (CRITICAL)

**⟁ CLARIFY** — For conflicts where the resolution is ambiguous: "I found a conflict in
[subject matter] between [provision A] and [provision B]. The document has [no order of
precedence / an order of precedence that may apply]. In your view, which provision should
govern? This will affect how I classify the severity."

### Step 9: Check Date and Deadline Alignment

Verify temporal coherence across the document set.

**9a. Date types to audit**

| Date Type                         | What to Check                                                                            |
| --------------------------------- | ---------------------------------------------------------------------------------------- |
| **Effective date**                | Consistent across all documents in the suite; not in the future unless intended          |
| **Execution date**                | Date actually signed vs. date stated "as of"                                             |
| **Term / expiry date**            | Consistent with effective date + stated term length                                      |
| **Notice periods**                | Notice periods in termination, renewal, and cure provisions are realistic and consistent |
| **Condition precedent deadlines** | CP longstop dates are sufficient given the CP obligations                                |
| **Payment dates**                 | Payment dates flow logically from delivery/milestone triggers                            |
| **Regulatory deadlines**          | Compliance and filing deadlines are achievable                                           |
| **Amendment dates**               | Any amendments are dated after the original and reference the correct original           |

**9b. Temporal conflict detection**

Flag where:

- Effective dates are inconsistent across documents in a suite (e.g., main agreement
  effective January 1 but a key schedule effective February 1 with no gap explanation)
- A notice period is mathematically insufficient (e.g., 90-day notice in a 60-day
  contract term)
- A retroactive effective date creates obligations before the signing date without an
  explicit "as of" statement
- A condition precedent longstop date has already passed (making CP satisfaction
  impossible)
- Payment terms create a date sequence that is logically impossible
- An amendment post-dates its own recitals

**9c. Date format inconsistency**

Flag where dates are expressed inconsistently (e.g., "January 1, 2025" in one place and
"01/01/25" in another, or a document uses European day-month-year format in some places
and US month-day-year in others). [JURISDICTION-SPECIFIC: Date format requirements may
vary by jurisdiction for regulated documents or court filings.]

### Step 10: Severity Classification and Triage

Classify every finding using the four-tier severity system.

---

## Severity Classification System

### CRITICAL — Resolve Before Execution

A cross-reference failure that creates an operational, legal, or enforcement risk if
left unresolved. The document cannot function as intended with this issue outstanding.

**Characteristics:**

- The error makes compliance impossible (operative conflict)
- The error makes a key right or obligation unenforceable or illusory
- A fundamental term is used but not defined anywhere in the suite
- A cross-reference points to a non-existent provision on which an operative obligation
  depends
- A definition imported from another document creates a meaning directly contrary to
  the operative context

**Examples:**

- "Permitted Purpose" appears throughout the confidentiality regime but is not defined
  anywhere in the document suite
- Section 12.5(a) is referenced in the limitation of liability clause but Section 12.5
  only has subsections (b) through (d)
- Two documents define "Change of Control" inconsistently: one requires 50% shareholder
  threshold, the other 30% — and both documents trigger different consequences on
  "Change of Control"
- A condition precedent longstop date of March 1 in a document executed on March 5

**Action**: Must resolve. Generate specific remediation language. Escalate to counsel
if the error reflects an underlying commercial ambiguity rather than a drafting mistake.

---

### HIGH — Resolve Before Signing or Filing

A cross-reference failure that creates material ambiguity or risk but does not make
the document completely inoperable. A court may be able to interpret its way out of
the issue, but relying on a court is undesirable.

**Characteristics:**

- A defined term is used in a way arguably inconsistent with its definition
- The same concept is addressed by two provisions that are not directly contradictory
  but can be read in conflicting ways
- An internal reference is to the right section but that section's subject matter does
  not precisely match the reference
- A term is defined in one document and used in another without an explicit import
  provision
- Two documents state the same date-triggered obligation with different notice periods

**Examples:**

- "Affiliate" is defined to include controlled subsidiaries, but the non-compete clause
  restricts "the Company and all Affiliates" in a way that may capture entities the
  parties did not intend
- The main agreement says payment is due "within 30 days" and the payment schedule says
  "net 45" with no order of precedence
- "Intellectual Property" is defined in the main body to exclude software, but Exhibit A
  refers to "all Intellectual Property, including software"
- A renewal notice period in the agreement body (60 days) differs from the renewal
  notice period in the auto-renewal schedule (90 days)

**Action**: Resolve. Generate specific remediation options (prefer: align provisions;
alternative: add an explicit priority note if the discrepancy is intentional).

---

### MEDIUM — Resolve Before Signature if Practical; Flag for Awareness

A cross-reference failure that creates inefficiency, potential ambiguity, or drafting
inconsistency but has a clear interpretation and unlikely to cause enforcement problems.

**Characteristics:**

- A defined term is defined but never used (orphaned definition)
- A term is used in both its defined and generic sense, causing minor ambiguity
- A cross-reference points to the right section but the section title in the reference
  does not match the actual section title (typographical, not substantive)
- Two synonym terms are used for the same concept without a clear reason for distinction
- A date is expressed inconsistently across documents

**Examples:**

- "Force Majeure Event" is defined but the clause uses "force majeure event" (lower case)
  throughout
- "Affiliate" appears both capitalized (as a defined term) and uncapitalized (generic use)
  in the same document
- Exhibit B is titled "Pricing Schedule" in the main agreement but "Fee Schedule" in its
  own header
- "Business Day" defined differently in the main agreement vs. the accompanying DPA
  (both plausible; creates minor uncertainty for deadline calculations)

**Action**: Fix if easy; flag for awareness if complex. Note that while unlikely to
cause enforcement problems, inconsistencies can be cited in disputes.

---

### LOW — Style and Consistency Improvements

Minor drafting inconsistencies that do not create ambiguity or risk. Appropriate for
clean-up passes or long-term document quality management.

**Characteristics:**

- Redundant definitions (defined term matches its plain-language meaning exactly)
- Stylistic variation in how section references are expressed ("Section 5" vs. "§5")
- Inconsistent use of defined term abbreviations that are still unambiguous
- Minor formatting differences between documents that do not affect substance

**Action**: Note. Fix in routine document maintenance. Do not prioritize.

---

## Remediation Guidance

For every CRITICAL and HIGH finding, provide specific remediation guidance:

### Remediation Format

```
**Finding ID**: [XR-001]
**Type**: [Undefined Term / Orphaned Term / Broken Reference / Conflict / Date Mismatch / etc.]
**Severity**: [CRITICAL / HIGH / MEDIUM / LOW]
**Location**: [Document name, Section/Clause]
**Issue**: [Precise description of the cross-reference failure]
**Affected provisions**: [List of all sections affected by or depending on the broken reference]
**Remediation Option A** (preferred): [Specific fix — e.g., insert definition, correct reference, add priority note]
**Remediation Option B** (alternative): [Alternative fix if Option A is not commercially acceptable]
**Rationale**: [Why this matters — what breaks if left unresolved]
**Confidence**: [Level + range, e.g., "High (0.85) — the reference clearly points to a non-existent provision"]
```

### Remediation Principles

1. **Prefer alignment over priority notes**: When two provisions conflict, the preferred
   fix is to harmonize them into one consistent provision. Using an order of precedence
   note to resolve the conflict is a fallback — it resolves the legal question but leaves
   the reader to navigate an inconsistency.

2. **Preserve commercial intent**: Before proposing a fix, confirm the commercial intent.
   An inconsistency between two liability caps may reflect an intentional negotiation
   compromise — do not harmonize without asking.

3. **Draft-quality remediation language**: For CRITICAL items, provide insertion-ready
   language. For HIGH items, provide a precise description of the change required.

4. **Flag root cause**: If a cluster of findings stems from a common root cause (e.g.,
   a definitions article was not updated when the main body was redlined), identify the
   root cause so the party can address it systematically rather than fix each symptom
   individually.

---

## Issue Prioritization Framework

### Tier 1 — Pre-Execution Blockers

Issues that must be resolved before any document is executed, filed, or delivered:

- CRITICAL findings in any operative provision
- CRITICAL findings in a defined term used in more than one document
- Any date conflict that makes execution impossible or creates retroactive obligations
  without explicit agreement
- Any inter-document conflict that is unresolvable by the order of precedence

### Tier 2 — Pre-Signing Strong Preferences

Issues that should be resolved before signing but have a fallback interpretation:

- HIGH findings in defined terms used in key operative provisions (liability, IP, data
  protection, payment)
- HIGH conflicts in liability-sensitive areas (caps, indemnities, termination triggers)
- Any date misalignment in notice periods or condition precedent deadlines
- Imported definitions that do not function correctly in context

### Tier 3 — Post-Execution Housekeeping

Issues appropriate for amendment at next renewal or maintenance pass:

- MEDIUM findings throughout (orphaned terms, synonym pairs, typographical
  reference mismatches)
- LOW findings throughout (style and consistency)
- Any findings that cannot be resolved without reopening commercial negotiation

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise any failure before
delivering.

| Gate           | Rule                                                                                                                 | Fail Action                                                      |
| -------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Source**     | Every finding cites the specific provision(s) involved — document name, section, and exact text                      | Add citation or mark "[LOCATION UNVERIFIED]"                     |
| **Format**     | All references follow a consistent format (e.g., "Agreement §5.3(a)" not just "§5.3")                                | Fix format                                                       |
| **Currency**   | References to the correct version of each document                                                                   | Flag "[VERSION UNCONFIRMED — verify which version is operative]" |
| **Domain**     | Analysis flags only findings within the document set provided — no assumptions about external documents not in scope | Remove or flag out-of-scope assumptions                          |
| **Confidence** | Uncertainty is explicitly stated, not hidden. If a finding might be an intentional drafting choice, say so           | Add qualifier: "this may be intentional — confirm with counsel"  |

### Self-Interrogation for CRITICAL Findings

For every CRITICAL-severity finding, apply this 3-pass review before delivering:

**Pass 1 — Existence Check**:

- Does the finding cite the correct document and section?
- Have I re-read the exact language of both the referring provision and the referenced
  provision?
- Is there any other definition, priority clause, or contextual language elsewhere in
  the document set that resolves the apparent error?

**Pass 2 — Completeness**:

- Have I identified all provisions that depend on or are affected by this failure?
- Is the impact on the document's operation accurately described?
- Are there any schedules, amendments, or exhibits that resolve the conflict?

**Pass 3 — Challenge**:

- Is this finding actually an intentional drafting choice that I have misread as an error?
- What is the strongest argument that this cross-reference works as drafted?
- Would a careful reader recognize this as an error, or would they simply apply the
  natural interpretation?

Mark the Glass Box audit trail with `self_interrogation: PASS` or
`self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                                                       | Action                                            |
| ------------ | --------- | ----------------------------------------------------------------------------- | ------------------------------------------------- |
| **Definite** | 0.95-1.0  | Clear error — referenced provision does not exist                             | State with confidence                             |
| **High**     | 0.80-0.94 | Strong evidence of error — subject matter mismatch or conflicting definitions | State with brief caveat                           |
| **Probable** | 0.60-0.79 | Likely error but possible intentional drafting choice                         | State with reasoning and note possible intent     |
| **Possible** | 0.40-0.59 | Genuine ambiguity — may or may not be an error                                | Flag for counsel review with both interpretations |
| **Unlikely** | 0.0-0.39  | Weak basis for flagging — likely intentional                                  | Do not flag as error; note as observation only    |

---

## Glass Box Audit Trail

Every cross-reference analysis output MUST include a Glass Box audit trail:

```yaml
glass_box:
  skill_name: "legalcode-cross-reference-analyzer"
  documents_analyzed:
    - name: "[Document 1 name]"
      date: "[document date]"
      status: "[executed/draft]"
      pages: "[N]"
    - name: "[Document 2 name]"
      date: "[document date]"
      status: "[executed/draft]"
      pages: "[N]"
  analysis_scope: "[Full audit / Focused: specified modules]"
  defined_terms_total: "[N]"
  defined_terms_flagged: "[N]"
  orphaned_terms: "[N]"
  undefined_usages: "[N]"
  multi_defined_terms: "[N]"
  circular_definitions: "[N]"
  internal_references_checked: "[N]"
  broken_internal_references: "[N]"
  inter_document_references_checked: "[N]"
  broken_inter_document_references: "[N]"
  conflicts_identified: "[N]"
  date_misalignments: "[N]"
  findings_total: "[N]"
  by_severity:
    critical: "[N]"
    high: "[N]"
    medium: "[N]"
    low: "[N]"
  order_of_precedence_present: "[Yes / No / Partial]"
  self_interrogation_applied: "[N CRITICAL items reviewed]"
  self_interrogation: "[PASS / REVISED on N items]"
  legalcode_mcp: "[Connected / Not connected]"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  limitations:
    - "[Any scope limitations, e.g., embedded PDFs not extractable]"
    - "[Any provisions marked as potentially intentional rather than errors]"
    - "[Any documents not available for inter-document reference checking]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in cross-reference analysis:

1. **Flagging intentional inconsistencies as errors** — Not every inconsistency is a
   drafting mistake. Different payment terms in the main agreement vs. a schedule may
   reflect a negotiated compromise. Before flagging a conflict, ask whether the
   inconsistency could be intentional. Always include a "may be intentional" note for
   ambiguous findings.

2. **Missing the orphan definition problem** — Many analyzers focus on undefined usages
   and miss orphaned definitions. A defined term that appears in the definitions section
   but is never used in operative provisions may indicate a deleted clause whose
   corresponding definition was not cleaned up — a material drafting risk.

3. **Treating synonyms as harmless** — Using "Intellectual Property" in one clause and
   "Intellectual Property Rights" in another without a definitions note may seem like a
   style issue, but it creates a colorable argument that the two terms have different
   scopes. Flag synonym pairs in operative provisions, not just for style.

4. **Ignoring section re-numbering after redlines** — The most common source of broken
   references is clause renumbering after sections are added or removed. An analyzer
   that only checks whether a referenced section exists (existence test) and not whether
   its subject matter matches the reference (subject matter test) will miss these.

5. **Skipping schedule and exhibit references** — Most reference checks focus on the main
   agreement body and miss the complex reference networks within schedules and exhibits,
   or between schedules and the main body. Schedules often contain references back to the
   main body using section numbers that change during redlining.

6. **Reporting all findings at equal severity** — A 200-item report where CRITICAL,
   HIGH, MEDIUM, and LOW findings are not distinguished is nearly useless. The whole
   value of the analysis is in prioritization. Always apply the four-tier severity
   system and present CRITICAL items prominently.

7. **Not checking imported definitions in context** — When a definition is imported from
   another document, simply finding it and confirming it exists is insufficient. The
   imported definition must be read in the context of its use in the importing document.
   A definition that works perfectly in the source document may be incompatible with
   the operative context where it is used.

8. **Circular definition chains beyond two hops** — Circular definition checkers often
   only check direct circularity (A defined as B, B defined as A). Three- and four-hop
   circles (A → B → C → A) are common in large document suites with interconnected
   definitions. Trace the full definition chain for every term that defines by reference
   to another defined term.

9. **Assuming the definitions section is exhaustive** — Many contracts define terms
   within operational clauses rather than in a centralized Definitions section.
   Restricting the defined terms search to the definitions article will miss a significant
   proportion of defined terms, especially in financial and M&A documents.

10. **Ignoring date format ambiguity** — In international transactions, "01/02/2025" is
    read as January 2 (US) or February 1 (UK/EU). In a document suite with parties and
    counsel from different date-convention jurisdictions, ambiguous date formats in
    operative provisions are HIGH severity. Never assume the reader will adopt the
    drafter's date convention.

11. **Missing the "as amended from time to time" problem** — Where a definition is
    imported with "as amended from time to time" language, the current version of the
    imported definition may differ materially from the version in force when the
    importing document was executed. This is not a drafting error but an ongoing
    monitoring risk — flag it as such.

12. **Over-reporting MEDIUM and LOW to pad the finding count** — An analysis that
    identifies 150 LOW-severity style issues and 3 CRITICAL errors, but presents them
    in a flat list, directs attention away from material issues. Always present CRITICAL
    and HIGH findings first, separately, and prominently.

13. **Not tracing the full dependency tree of a broken reference** — A single broken
    reference often propagates: if §5.3 does not exist but is cited in §8.1(b), and
    §8.1(b) is in turn cited in §12.4(a) as a condition to a key right, the failure
    cascades. Always trace downstream dependencies of CRITICAL broken references.

14. **Analyzing documents in isolation without reading the suite as a whole** — Reviewing
    each document independently without tracking how definitions and references flow
    across the suite misses the most material class of errors: inter-document
    inconsistencies and imported-definition failures.

15. **Treating the Defined Terms Register as a one-time artifact** — In large document
    suites undergoing ongoing negotiation, the Defined Terms Register must be treated as
    a living document that needs to be refreshed after every substantial redline. An
    analyzer that generates the register once and does not flag that it needs updating is
    providing false assurance.

16. **Skipping the order of precedence analysis** — Where an order of precedence clause
    exists, some apparent conflicts are actually resolved conflicts. Flagging them as
    CRITICAL when they are resolved by precedence wastes time and credibility. Always
    read the order of precedence clause before classifying conflicts.

17. **Conflating missing definitions with undefined usages** — A capitalized term that
    lacks a definition may be an error (undefined usage) or it may be a proper noun,
    an external standard, or a term defined in a governing law. Distinguish between
    terms that appear to need a definition but lack one, and terms that are capitalized
    for other reasons.

18. **Not flagging documents that were "not reviewed" clearly** — If any document
    referenced in the suite was not available for analysis, the Glass Box audit trail
    must state this explicitly. An analysis that silently skips a referenced document
    creates false confidence in the completeness of the review.

---

## Writing Standards

Apply plain-language discipline to all output.

**For finding descriptions**:

- Active voice: "Section 12.3 references Section 8.5, which does not exist" not
  "Section 8.5, which is referenced in Section 12.3, cannot be located"
- Lead with the problem: "UNDEFINED TERM: 'Permitted Purpose' is used in 14 operative
  clauses but is not defined anywhere in the document suite"
- Name the exact provision: always cite the document name, section, and clause
- Quantity the impact: "affects 8 operative provisions" is more useful than "affects
  several provisions"

**For remediation language**:

- Insertion-ready: remediation language should be copy-paste-ready for a drafter,
  not a vague instruction like "add a definition for this term"
- Brief rationale: one or two sentences explaining why this fix resolves the issue
- Note where the fix may require renegotiation vs. where it is a pure drafting fix

**Quality gates before delivery**:

1. Is every CRITICAL finding supported by exact document location and text quotation?
2. Has the CRITICAL Self-Interrogation been applied to every CRITICAL finding?
3. Is the severity classification applied consistently (same type of error = same tier)?
4. Are all findings clearly classified and not mixed with observations or commentary?
5. Is the Glass Box audit trail complete and accurate?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as a supplemental legal research
tool when cross-reference errors raise jurisdiction-specific legal questions.

**With legalcode-mcp connected:**

- When a conflict appears to involve a legally mandatory provision (e.g., a mandatory
  data breach notification period that conflicts with the contractual period), use
  legalcode-mcp to verify the applicable mandatory requirement
- When a definitional conflict involves a term with a statutory definition (e.g.,
  "Consumer," "Personal Data," "Employment"), use legalcode-mcp to identify the
  statutory definition and assess whether the contractual definition is consistent
- When an inter-document reference conflict creates a potentially unenforceable
  provision, use legalcode-mcp to research the governing law's treatment of
  conflicting provisions
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark any legal consequence assessments with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus on structural integrity analysis rather than legal consequence assessment
- The core value of this skill — cross-reference mapping and integrity checking — does
  not depend on legalcode-mcp and functions fully without it

---

## Localization Notes

This is a jurisdiction-agnostic skill. The cross-reference analysis is structural and
does not require jurisdiction-specific legal knowledge. However, certain findings may
have jurisdiction-specific legal consequences:

- [JURISDICTION-SPECIFIC] **Civil law jurisdictions**: Courts may apply different rules
  for resolving conflicts between general and specific provisions. Where the contract is
  governed by a civil law system, note that the applicable Civil Code's gap-filling rules
  may resolve some apparent conflicts that would remain unresolved under common law.
  [VERIFY]

- [JURISDICTION-SPECIFIC] **Bilingual document requirements**: Some jurisdictions require
  contracts to be executed in the local language or impose that the local language version
  governs in conflicts. Where a document suite includes translations, cross-reference
  consistency between language versions is an additional analysis layer. [VERIFY]

- [JURISDICTION-SPECIFIC] **Incorporation by reference requirements**: Some jurisdictions
  impose specific requirements for effective incorporation by reference (e.g., specific
  language, notice to the other party, or availability of the incorporated document).
  Where incorporation by reference is used, flag whether the applicable requirements
  appear to be met. [VERIFY]

- [JURISDICTION-SPECIFIC] **Consumer contracts**: Many jurisdictions impose mandatory
  terms in consumer contracts that override inconsistent contractual terms. Cross-
  reference errors involving mandatory terms may have greater legal significance in
  consumer contexts. [VERIFY]

---

## Output Format Template

Structure the final deliverable as follows:

```markdown
## Cross-Reference Integrity Analysis

**Analysis Date**: [date]
**Document Set**:

- [Document 1 name] — [date] — [executed/draft]
- [Document 2 name] — [date] — [executed/draft]
  **Analysis Scope**: [Full audit / Focused modules]
  **Total Findings**: [N] ([X] CRITICAL / [X] HIGH / [X] MEDIUM / [X] LOW)

---

## Executive Summary

[3-5 sentence summary of the overall cross-reference health of the document set.
Identify the most significant cluster of issues and the recommended immediate action.]

**Recommendation**: [Overall verdict — e.g., "Ready to execute subject to resolving 2
CRITICAL items" / "Significant rework required before execution" / "Good cross-reference
integrity with minor clean-up items"]

---

## CRITICAL Findings — Resolve Before Execution

### XR-[001] [Brief title]

**Type**: [Undefined Term / Broken Reference / Operative Conflict / etc.]
**Location**: [Document name, §X.X]
**Issue**: [Precise description]
**Text**: "[Exact quote of the problematic language]"
**Affected provisions**: [List]
**Remediation Option A**: [Preferred fix with insertion-ready language]
**Remediation Option B**: [Alternative]
**Rationale**: [Why this matters]
**Confidence**: [Level (range)]

[Repeat for each CRITICAL finding]

---

## HIGH Findings — Resolve Before Signing

[Same format as CRITICAL]

---

## MEDIUM Findings — Resolve if Practical

[Summary table format acceptable for MEDIUM findings:]

| ID     | Type   | Location   | Issue Summary    | Remediation Note |
| ------ | ------ | ---------- | ---------------- | ---------------- |
| XR-[N] | [type] | [location] | [1-line summary] | [brief fix]      |

---

## LOW Findings — Style and Consistency

[Table format:]

| ID     | Location   | Issue    | Note            |
| ------ | ---------- | -------- | --------------- |
| XR-[N] | [location] | [1-line] | [optional note] |

---

## Defined Terms Register

| Term   | Defined In | Section | Used In         | Usage Count | Issues       |
| ------ | ---------- | ------- | --------------- | ----------- | ------------ |
| [Term] | [Doc]      | [§X.X]  | [Docs/Sections] | [N]         | [flags or —] |

---

## Inter-Document Reference Map

| From Document | From Section | References       | To Document | To Section | Status                          |
| ------------- | ------------ | ---------------- | ----------- | ---------- | ------------------------------- |
| [Doc A]       | [§X.X]       | [term/provision] | [Doc B]     | [§Y.Y]     | ✅ Valid / ⚠️ Issue / ❌ Broken |

---

## Date and Deadline Summary

| Date/Deadline  | Document | Section | Date Stated | Alignment    |
| -------------- | -------- | ------- | ----------- | ------------ |
| Effective date | [Doc]    | [§]     | [date]      | ✅ / ⚠️ / ❌ |
| Expiry date    | [Doc]    | [§]     | [date]      | ✅ / ⚠️ / ❌ |
| [Other]        | [Doc]    | [§]     | [date]      | ✅ / ⚠️ / ❌ |

---

## Recommended Action Plan

### Immediate (Before Execution)

1. [CRITICAL finding remediation]
2. [CRITICAL finding remediation]

### Pre-Signing (Before Signature)

1. [HIGH finding remediation]
2. [HIGH finding remediation]

### Post-Execution Maintenance

1. [MEDIUM/LOW clean-up items]

---

[Glass Box Audit Trail — YAML block as specified above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on cross-reference integrity
analysis best practices in legal document quality management. Research conducted via
web-backed agent team analysis covering CLM platform practices, legal drafting guidance,
due diligence methodology, and common malpractice vectors in multi-document transaction
suites. Calibrated against the `legalcode-contract-review` gold standard for workflow
design, quality frameworks, severity classification, and Glass Box audit trail structure.
