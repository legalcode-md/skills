---
name: legalcode-document-qa
description: >
  Run a comprehensive quality assurance audit on any legal document — contract, agreement,
  deed, policy, or court filing — to detect drafting errors before execution or filing.
  Covers nine QA dimensions: defined term audits (undefined, orphaned, duplicate, and
  miscapitalized terms); cross-reference integrity (stale section numbers, broken
  references); party name consistency (synonym drift, signature block mismatches); date
  and deadline logic (effective date ambiguity, impossible dates, notice period arithmetic);
  numbering and hierarchy (skipped items, inconsistent hierarchy, non-parallel structure);
  gender and pronoun consistency (mixed gendered pronouns, orphaned antecedents); formatting
  and layout (tracked changes, residual comments, font inconsistency, page numbering);
  signature block validation (missing titles, undated lines, entity name mismatches);
  and substance completeness gaps (missing essential provisions, undefined relative
  standards). Generates a prioritized correction report with exact proposed corrections.
  Use when proofreading a contract before execution, auditing a template for quality,
  reviewing a redlined draft, or preparing a document for filing. Works on any document
  type and any jurisdiction.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode Document QA

> **Disclaimer**: This skill provides a framework for AI-assisted document quality
> assurance. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional before use. This skill checks for drafting and formatting
> errors — it does not review substantive legal risk, negotiation positions, or the
> commercial adequacy of terms. Statutory and case law references cited from memory carry
> hallucination risk — verify against authoritative sources before relying on them.

## Purpose and Scope

This skill runs a systematic quality assurance audit on a legal document across nine
dimensions of drafting and formatting quality. It identifies errors, classifies them by
severity, generates exact proposed corrections, and produces a prioritized correction
report ready to implement.

**Covers:**
- Defined term audit (undefined, orphaned, duplicate, and miscapitalized terms)
- Cross-reference integrity (stale references, nonexistent sections)
- Party name consistency (synonym drift, signature block mismatches)
- Date and deadline logic (effective date ambiguity, impossible dates, notice period errors)
- Numbering and hierarchy (skipped items, inconsistent levels, non-parallel structure)
- Gender and pronoun consistency (mixed pronouns, orphaned pronoun antecedents)
- Formatting and layout (tracked changes, residual comments, font/spacing inconsistency)
- Signature block validation (missing dates, title omissions, entity name mismatches)
- Substance completeness gaps (missing essential provisions, undefined relative standards)

**Does not:**
- Assess substantive legal risk, commercial adequacy, or negotiation positions
  (see `legalcode-contract-review` for that analysis)
- Provide legal advice or replace qualified counsel
- Verify that the parties have authority to execute the document
- Assess whether a document's terms are enforceable under any particular governing law

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. Document QA checks — defined term consistency,
cross-reference accuracy, formatting standards — apply regardless of governing law.

[JURISDICTION-SPECIFIC] When the document is governed by a specific jurisdiction, note:
- Signature block formality requirements (witnesses, notarization, seals) vary widely
- Some jurisdictions require documents in the local language or bilingual format
- Execution requirements for deeds, security instruments, and statutory filings differ
- Court filing formatting rules are jurisdiction-specific (margins, font size, line spacing)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. The workflow pauses
and asks when:

- The scope of the QA check needs to be confirmed (full audit vs. focused check)
- The document type affects which QA dimensions are most critical
- Ambiguous issues require user judgment to classify correctly

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

Accept the document in any of these formats:
- **File**: DOCX, PDF, or plain text
- **Pasted text**: Document content pasted directly into the conversation
- **URL**: Link to a document in a document management system or cloud storage

If no document is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the audit, ask the user these questions. Skip any
already answered in the initial prompt:

1. **Document type**: What kind of legal document is this?
   - Options: Commercial contract / agreement, Employment document, Real estate instrument,
     Corporate governance document (board resolution, articles, minutes), Court filing,
     Regulatory submission, Policy or procedure, Other
   - *Why this matters*: Different document types have different essential provisions and
     signature block requirements. A deed requires witnesses; a board resolution requires
     specific recitals; a court filing has strict formatting rules.

2. **Stage in the drafting process**: Where is this document in the workflow?
   - Options: Initial draft (pre-negotiation), Redlined draft (mid-negotiation), Near-final
     (pre-execution), Final (ready to execute/file), Template audit (quality check a
     reusable template)
   - *Why this matters*: Near-final documents warrant the strictest QA pass. Templates need
     checks for leftover placeholders. Mid-negotiation redlines need a check that tracked
     changes are clean.

3. **Scope**: Should this be a full nine-dimension audit or a targeted check?
   - Options: Full audit (all nine dimensions), Defined terms only, Cross-references only,
     Custom focus (specify which dimensions)
   - *Why this matters*: A full audit is appropriate for near-final documents. Targeted
     checks are faster when the user knows the problem area.

4. **Known issues**: Are there any known problem areas to prioritize?
   - Free text. E.g., "The numbering went wrong after we moved sections around" or
     "Not sure if all the cross-references updated correctly."
   - *Why this matters*: Known issues get checked first and flagged prominently.

Proceed with reasonable defaults if the user provides partial context.

### Step 3: Parse the Document Structure

Before running QA checks, map the document:

1. **Identify the structure**: Count sections/clauses, identify schedule/exhibit attachments,
   note if multiple documents are incorporated by reference.
2. **Extract the party definitions**: Find the Introduction or Recitals clause where parties
   are defined with their role-based defined terms (e.g., "ABC Corp. ('Supplier')").
3. **Build the defined terms register**: Extract all capitalized terms that appear to be
   defined (either in a Definitions section, on first use with quotes, or via definitional
   provisions). Note every location where each is defined.
4. **Map the cross-reference targets**: List every section/clause/schedule number that exists
   so cross-references can be validated against this map.

**⟁ CLARIFY** — If the document references external documents by incorporation ("as
defined in the Master Agreement," "subject to the Schedules listed at Annex A"), ask
whether those incorporated documents are available for cross-check, or whether the audit
should proceed on the main document only.

### Step 4: Run the Nine-Dimension QA Audit

Execute all applicable dimensions in order. For each dimension, produce a findings list
using the format specified in the **Correction Entry Format** section.

#### Dimension 1: Defined Term Audit

**What to check:**

| Check | Description | Default Severity |
|-------|-------------|-----------------|
| **UNDEF** | Capitalized term used in the operative provisions but not defined anywhere | CRITICAL |
| **ORPHAN** | Term defined but never used in the operative provisions | MEDIUM |
| **DUPLICATE** | Same term defined in more than one location with potentially different scope | HIGH |
| **MISCAP** | A defined term appears in lower case (or inconsistent case) in at least one location | HIGH |
| **SYNONYM** | Two or more different terms appear to mean the same thing (e.g., "Purchaser" and "Buyer" for the same party) | HIGH |
| **CIRCULAR** | A defined term's definition relies on another term that directly or indirectly relies on it | HIGH |
| **NEVER-NEEDED** | A term is defined with extensive qualification but could have been left as plain English | LOW |

**How to check:**
1. Build a complete list of all capitalized terms in the document.
2. Cross-reference each against the definitions register built in Step 3.
3. For every instance in the operative provisions, verify the capitalization matches the
   defined form exactly.
4. Scan for synonym pairs by looking for terms that reference the same party, concept, or
   amount under different names.

**⟁ CLARIFY** — When a capitalized term appears without a definition but could plausibly
be a deliberate use of a common-English capitalized word (e.g., "Party," "Law," "Person"),
ask the user whether this is intentional before classifying as UNDEF.

#### Dimension 2: Cross-Reference Integrity

**What to check:**

| Check | Description | Default Severity |
|-------|-------------|-----------------|
| **MISSING-TARGET** | Cross-reference points to a section, clause, exhibit, or schedule that does not exist in the document | CRITICAL |
| **WRONG-NUMBER** | Cross-reference appears to point to a real section but the number is wrong (e.g., "Section 4.2" exists but the reference should be "Section 4.3" based on context) | HIGH |
| **SUBJECT-MISMATCH** | The referenced section does not cover the subject matter stated in the cross-reference ("as defined in Section 2.1" but Section 2.1 doesn't define that term) | HIGH |
| **MISSING-HEADING** | Cross-reference uses a section number only, without the heading name — making errors invisible | LOW |
| **STALE-AFTER-DELETION** | The referenced section was deleted in a prior draft and no longer exists | CRITICAL |

**How to check:**
1. Extract every cross-reference in the document (search for "Section," "Clause," "Schedule,"
   "Exhibit," "Annex," "Appendix" followed by a number or letter).
2. Validate each reference against the section map built in Step 3.
3. For references that include both a number and a description, verify the description matches
   the referenced section's actual content or heading.

#### Dimension 3: Party Name Consistency

**What to check:**

| Check | Description | Default Severity |
|-------|-------------|-----------------|
| **INTRO-BODY-MISMATCH** | A party's defined term in the Introduction differs from the term used in the body | CRITICAL |
| **SYNONYM-DRIFT** | A party is referred to by different terms in different parts of the document (e.g., "Buyer" in clauses 1–5, "Purchaser" in clauses 6–12) | HIGH |
| **SIG-BLOCK-MISMATCH** | The entity name in the signature block differs from the entity name in the Introduction or Parties clause | CRITICAL |
| **FULL-NAME-USAGE** | Party's full legal name is used in body clauses instead of the defined short-form term | MEDIUM |
| **PRECEDENT-BLEED** | A party name from a prior contract has been left in the document (copy-paste error) | CRITICAL |
| **WRONG-PARTY** | An obligation or right is attributed to the wrong party | HIGH |

**How to check:**
1. Extract every occurrence of party names and defined party terms.
2. Build a party name map: legal name → defined term → signature block name.
3. Flag any inconsistency in any of the three layers.
4. Search the entire document for party names from other documents that may have been carried
   over by copy-paste (if you can identify them from context).

#### Dimension 4: Date and Deadline Logic

**What to check:**

| Check | Description | Default Severity |
|-------|-------------|-----------------|
| **NO-EFFECTIVE-DATE** | Document does not explicitly state an effective date (relying only on execution date) | HIGH |
| **DATE-ARITHMETIC** | A deadline calculated from the effective date or execution date does not match the stated date (e.g., "30 days from the Effective Date" but the stated deadline is wrong) | HIGH |
| **IMPOSSIBLE-DATE** | A date that cannot exist (February 29 in a non-leap year, day-of-week mismatch, dates before 1900) | CRITICAL |
| **DATE-INCONSISTENCY** | The same event has different dates in different parts of the document | CRITICAL |
| **RETROACTIVE-AMBIGUITY** | Effective date is earlier than the execution date with no provision addressing the retroactive period's obligations | MEDIUM |
| **NOTICE-ARITHMETIC** | Notice period stated in one clause is inconsistent with the termination/renewal logic in another clause | HIGH |
| **FORMAT-INCONSISTENCY** | Dates use different formats in different places (e.g., "March 15, 2025" in one clause and "15/03/2025" in another) | LOW |

**How to check:**
1. Extract every date mentioned in the document with its location and purpose.
2. Check each against the leap-year calendar and day-of-week calendar.
3. Trace the notice period arithmetic: identify the governing term length, renewal cycle, and
   notice windows, and verify they are internally consistent.
4. Check format consistency across all date references.

#### Dimension 5: Numbering and Hierarchy

**What to check:**

| Check | Description | Default Severity |
|-------|-------------|-----------------|
| **SKIPPED-NUMBER** | A list or section sequence skips a number (e.g., items 1, 2, 4, 5 — 3 is missing) | MEDIUM |
| **DUPLICATE-NUMBER** | Two different items share the same number | HIGH |
| **HIERARCHY-INCONSISTENCY** | Heading levels are applied inconsistently (e.g., some third-level headings use bold, others use indented plain text) | MEDIUM |
| **NON-PARALLEL-STRUCTURE** | Items in the same list use inconsistent grammatical structure | MEDIUM |
| **NUMERAL-WORD-INCONSISTENCY** | Numbers are sometimes spelled out ("fifteen") and sometimes in numerals ("15") for the same category | LOW |
| **ORDINAL-INCONSISTENCY** | Ordinals switch between "1st" and "first" form | LOW |
| **POST-EDIT-DRIFT** | Numbering was not updated after a section was moved, added, or deleted | HIGH |

**How to check:**
1. Walk through every numbered list and heading to verify the sequence is complete and correct.
2. Check that headings at the same level follow a consistent visual and structural pattern.
3. Check grammatical parallelism within each list (all items should complete the same stem).
4. Identify any numbering that appears to have not been updated after structural changes.

#### Dimension 6: Gender and Pronoun Consistency

**What to check:**

| Check | Description | Default Severity |
|-------|-------------|-----------------|
| **MIXED-GENDERED** | Document uses "he" in some clauses and "she" or "they" in others for the same role | HIGH |
| **GENDERED-FOR-ENTITY** | A corporate entity is referred to as "he" or "she" instead of "it" | MEDIUM |
| **ORPHANED-PRONOUN** | A pronoun ("it," "they," "he," "she") appears without a clear antecedent — ambiguous referent | HIGH |
| **RESIDUAL-GENDERED** | Gendered pronouns remain from a precedent document that were intended to be replaced | MEDIUM |
| **INCONSISTENT-APPROACH** | Document adopts different gender-neutrality techniques in different clauses (e.g., role-based terms in Section 1, singular "they" in Section 2, noun repetition in Section 3) | LOW |

**How to check:**
1. Search for "he," "she," "his," "her," "him," "himself," "herself" throughout the document.
2. For each occurrence, identify whether it is intentional (referencing a specific named
   individual) or a drafting residue.
3. Verify that each pronoun has a clear and unambiguous antecedent in its sentence or the
   preceding sentence.
4. Check that the approach to gender neutrality is consistent throughout.

#### Dimension 7: Formatting and Layout

**What to check:**

| Check | Description | Default Severity |
|-------|-------------|-----------------|
| **TRACKED-CHANGES** | Document contains accepted or unaccepted tracked changes in the final version | HIGH |
| **RESIDUAL-COMMENTS** | Document contains comment bubbles or review annotations | HIGH |
| **PLACEHOLDER-TEXT** | Document contains "[INSERT]", "TBD," "DRAFT," or similar placeholder text | CRITICAL |
| **FONT-INCONSISTENCY** | Body text uses inconsistent fonts, sizes, or weights | MEDIUM |
| **SPACING-INCONSISTENCY** | Line spacing or paragraph spacing is inconsistent within sections | LOW |
| **PAGE-NUMBERING** | Page numbers are missing, restarted mid-document, or formatted inconsistently | MEDIUM |
| **HIDDEN-METADATA** | Prior party names, author information, or document history carried in metadata | MEDIUM |
| **BLANK-FIELDS** | Date lines, party address blocks, or other fill-in fields are left blank | HIGH |
| **WRONG-DOCUMENT-TITLE** | Document title or header carries the name of a prior document | HIGH |

**How to check:**
1. Scan for tracked change markup and comment annotations.
2. Search for placeholder strings: "[INSERT," "[ADD," "[TBD," "[DATE," "[NAME," "DRAFT," "XX."
3. Review page numbering sequence across the full document.
4. Check that document title, header, and footer are consistent and correct.
5. Check font and spacing consistency by sampling multiple sections.

#### Dimension 8: Signature Block Validation

**What to check:**

| Check | Description | Default Severity |
|-------|-------------|-----------------|
| **MISSING-DATE-LINE** | A party's signature block does not include a date line | HIGH |
| **MISSING-TITLE** | A corporate signatory's signature block does not include a title line | HIGH |
| **ENTITY-MISMATCH** | The entity name in the signature block differs from the entity name in the Introduction | CRITICAL |
| **MISSING-WITNESS** | A signature block that requires a witness (deed, statutory form) has no witness block | CRITICAL |
| **MISSING-NOTARY** | A signature block that requires notarization has no notarial certificate block | CRITICAL |
| **COUNTERPARTS-MISSING** | A multi-party document has no counterparts clause permitting separate execution | MEDIUM |
| **WRONG-PARTY-COUNT** | Fewer signature blocks than contracting parties, or additional signature blocks for non-parties | HIGH |
| **AUTHORITY-RECITAL** | No "duly authorized" or equivalent authority recital for corporate signatories | MEDIUM |

**How to check:**
1. Count the signature blocks and compare to the number of named contracting parties.
2. For each signature block, verify: entity name matches Introduction clause, date line present,
   title line present for corporate signatories.
3. Identify the document type and check whether witnesses or notarization are required.
4. Verify a counterparts clause is present if parties will sign separately.

**⟁ CLARIFY** — Whether witnesses or notarization are required depends on the jurisdiction
and document type. If unclear, ask the user before classifying these as CRITICAL, since
the requirement varies: deeds in England & Wales require witnesses; mortgages in many US
states require notarization; corporate resolutions require board authorization recitals.
Flag the check as [JURISDICTION-SPECIFIC] if the user cannot confirm.

#### Dimension 9: Substance Completeness Gaps

This dimension checks only for the presence or absence of fundamental provisions — not
their substantive quality (which is the domain of contract review skills).

**What to check:**

| Check | Description | Default Severity |
|-------|-------------|-----------------|
| **NO-PARTIES** | Document does not identify the contracting parties | CRITICAL |
| **NO-GOVERNING-LAW** | Document has no governing law or jurisdiction clause | HIGH |
| **NO-TERM** | Document has no stated term, commencement date, or duration | HIGH |
| **NO-DISPUTE-RESOLUTION** | Document has no dispute resolution mechanism | HIGH |
| **UNDEFINED-STANDARD** | Document uses undefined relative standards ("promptly," "reasonable efforts," "materially") without qualification or context | MEDIUM |
| **AMBIGUOUS-OBLIGATION** | An operative clause cannot be determined to impose an obligation ("shall") or grant discretion ("may") from its language | HIGH |
| **INCOMPLETE-PROVISION** | A provision appears incomplete — stops mid-sentence, references a section not yet drafted | CRITICAL |

**How to check:**
1. Verify the document identifies all contracting parties with their legal names and roles.
2. Check for governing law and dispute resolution clauses.
3. Check for any defined commencement date or term duration.
4. Search for "promptly," "reasonable," "material," "timely," "appropriate," and similar
   relative standards — note occurrences and assess whether context makes them sufficiently
   specific.
5. Check every operative clause for clear shall/may distinction.

**⟁ CLARIFY** — For documents where some of these elements are intentionally absent
(e.g., side letters, amendments that incorporate the main agreement by reference), confirm
with the user before flagging as gaps.

### Step 5: Classify and Score Each Finding

For every finding, assign a severity level from the **Issue Severity Classification**
section below. Then apply the **Prioritization Framework** to rank all findings.

**⟁ CLARIFY** — For any borderline CRITICAL/HIGH classification where the severity
depends on business context not visible in the document, present both classifications
and ask:

- "This placeholder text '[INSERT GOVERNING LAW]' could be a CRITICAL issue (key term
  missing from near-final document) or a HIGH issue (intentional placeholder in a working
  draft). Which stage is this document at?"

### Step 6: Generate Correction Report

For each finding, generate a complete correction entry using the **Correction Entry
Format** below. Organize findings by:

1. First: CRITICAL issues (in order of appearance in document)
2. Then: HIGH issues
3. Then: MEDIUM issues
4. Then: LOW issues

### Step 7: Quality Verification

Before delivering the correction report, run these checks:

1. Run the 5 **Citation Quality Gates** silently.
2. For every CRITICAL finding, run the **Self-Interrogation** 2-pass review.
3. Assign a **Confidence Score** to each finding.
4. Verify the correction entry is complete: location identified, proposed correction
   provided, not just a description of the problem.
5. Generate the **Glass Box Audit Trail** and append to the output.

### Step 8: Deliver the Correction Report

Deliver the output using the **Output Format Template** below.

**⟁ CLARIFY** — For large documents with many findings, ask the user whether to:
- Deliver the **full correction report** (all findings with corrections)
- Deliver an **executive summary first** (counts by severity, top issues) followed by the
  full report on request
- Focus on **CRITICAL and HIGH only** (fastest path to a signable document)

---

## Issue Severity Classification

### CRITICAL — Fix Before Any Further Use

Errors that create legal ambiguity, could void or misapply provisions, or will cause
material problems at execution or in dispute resolution.

**Examples:**
- Capitalized term used in operative provision with no definition
- Cross-reference to a section that does not exist
- Party name in signature block differs from Introduction clause
- Placeholder text ("TBD," "[INSERT]") in near-final or final document
- Date that is mathematically impossible
- Incomplete provision (truncated sentence or missing operative clause)
- Witness or notarization block absent where legally required

**Action**: Provide an exact proposed correction. Do not deliver the document without
resolving CRITICAL items.

### HIGH — Fix Before Execution

Errors that materially affect the document's quality, create interpretive risk, or are
likely to be challenged by a counterparty or court.

**Examples:**
- Duplicate definitions for the same term
- Wrong section number in a cross-reference (right concept, wrong number)
- Party name synonym drift ("Buyer" / "Purchaser")
- Date logic errors (notice period arithmetic inconsistency)
- Tracked changes remaining in the document
- Missing date line or title line in signature block
- Residual comment bubbles in final version
- Blank fill-in fields (address, date)

**Action**: Provide an exact proposed correction and flag for review before execution.

### MEDIUM — Fix in Revision

Errors that reduce document quality and may create minor interpretive issues, but do not
create immediate legal risk.

**Examples:**
- Orphaned (unused) definitions
- Inconsistent pronoun use within the same document
- Non-parallel list structure
- Heading hierarchy inconsistency
- Retroactive effective date without clarifying language
- Undefined relative standards ("promptly") in non-critical provisions

**Action**: Provide a proposed correction and a brief note on why the fix improves the
document.

### LOW — Optional Cleanup

Minor editorial or stylistic inconsistencies that do not affect legal meaning.

**Examples:**
- Date format inconsistency across clauses
- Ordinal inconsistency ("1st" / "first")
- Numeral/word inconsistency for the same category of numbers
- Spacing or font inconsistency between sections
- Missing section heading names in cross-references

**Action**: Note the issue and the preferred consistent approach. Implement during the
next revision cycle.

---

## Correction Entry Format

For every finding, provide a complete correction entry:

```
**Finding**: [CRITICAL / HIGH / MEDIUM / LOW] — [Dimension] — [Check Code]
**Location**: [Section/Clause reference, page number if available, or quoted text]
**Description**: [One sentence explaining the error and its potential legal impact]
**Current text**: "[Exact quoted text from the document showing the error]"
**Proposed correction**: "[Exact replacement text, ready to insert]"
**Confidence**: [Definite / High / Probable / Possible — see Confidence Scoring]
```

---

## Prioritization Framework

When presenting findings, organize by these tiers:

### Tier 1 — Pre-Execution Blockers (All CRITICAL Items)

Issues that must be resolved before the document is used for any purpose. A document
with unresolved CRITICAL items should not be executed, filed, or delivered.

- Any undefined capitalized term used in operative provisions
- Any cross-reference to a nonexistent section
- Any party name mismatch between Introduction and signature block
- Any placeholder text in a near-final document
- Any legally impossible date
- Any incomplete provision
- Any missing witness/notary block where required

**Instruction**: Resolve all Tier 1 items before circulating the document further.

### Tier 2 — Pre-Execution Preferred (All HIGH Items)

Issues that materially affect quality and should be resolved before the document is
executed or formally delivered, but do not necessarily require halting progress.

- Duplicate definitions, synonym drift, tracked changes, date arithmetic errors
- Missing signature block elements, blank fill-in fields

**Instruction**: Assign to the responsible drafter with a target resolution date that
falls before the execution deadline.

### Tier 3 — Revision Cycle Items (MEDIUM and LOW Items)

Issues that improve document quality but can be addressed in the next revision cycle,
at a dedicated template cleanup session, or over time.

**Instruction**: Log these findings in the document management system. Resolve during
the next scheduled revision rather than holding up execution.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise before delivering if any
gate fails.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every classification as CRITICAL is based on an identifiable error in the document, not speculation | Add specific location reference or downgrade to HIGH |
| **Format** | Every proposed correction is in exact, ready-to-insert form | Provide specific language rather than vague guidance |
| **Currency** | Every check for jurisdiction-specific requirements is marked [JURISDICTION-SPECIFIC] when not universally applicable | Add marker and clarifying note |
| **Domain** | Analysis stays within the document QA scope — do not venture into substantive legal risk analysis | Remove or mark [OUT OF SCOPE FOR QA] |
| **Confidence** | Uncertainty explicitly stated — do not classify an error as CRITICAL if the intent is ambiguous | Add confidence qualifier or downgrade severity |

### Self-Interrogation for CRITICAL Items

For any item classified as CRITICAL, apply this 2-pass review before delivering:

**Pass 1 — Error Verification**: Is the error actually present in the document? Could the
apparent error be intentional (e.g., a term left undefined because it has a plain English
meaning, a deliberate retroactive effective date)?

**Pass 2 — Correction Completeness**: Is the proposed correction specific and ready to
implement? Does it resolve the full scope of the error, or only the most obvious
manifestation?

If either pass reveals a weakness, revise the finding before delivery.

### Confidence Scoring

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95-1.0 | Error is unambiguous and verifiable from the text alone | State with confidence |
| **High** | 0.80-0.94 | Strong evidence of an error, minor ambiguity possible | State with brief caveat |
| **Probable** | 0.60-0.79 | Likely an error, but could be intentional | Flag with note: "[Verify intent with drafter]" |
| **Possible** | 0.40-0.59 | Possible error, genuinely uncertain | Flag for human review rather than correcting |
| **Unlikely** | 0.0-0.39 | Weak basis — may not be an error | Do not flag as an error; note as an observation |

---

## Glass Box Audit Trail

Every QA audit MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-document-qa"
  document: "[Document title and date]"
  document_type: "[Contract / Deed / Policy / Court Filing / etc.]"
  document_stage: "[Draft / Near-final / Final / Template]"
  dimensions_audited:
    - "Defined Term Audit"
    - "Cross-Reference Integrity"
    - "Party Name Consistency"
    - "Date and Deadline Logic"
    - "Numbering and Hierarchy"
    - "Gender and Pronoun Consistency"
    - "Formatting and Layout"
    - "Signature Block Validation"
    - "Substance Completeness Gaps"
  findings_summary:
    critical: "[N]"
    high: "[N]"
    medium: "[N]"
    low: "[N]"
    total: "[N]"
  legalcode_mcp: "Connected / Not connected"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations — e.g., 'Incorporated documents not reviewed', 'Metadata not accessible']"
    - "[Any jurisdiction-specific checks deferred — e.g., 'Witness requirement not confirmed for jurisdiction']"
  reviewer: "AI-assisted — requires qualified legal review before execution"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do when running a document QA audit:

1. **Flagging intentional capitalization as undefined terms** — Not every capitalized word
   is a defined term. "Government," "Law," "Person," and "Agreement" are commonly
   capitalized without a definition because they have accepted plain-English meanings.
   Check whether a capitalized word is being used as a technical defined term before
   classifying it as UNDEF.

2. **Correcting substance under the guise of QA** — The scope of this skill is drafting
   and formatting errors. Identifying a liability cap as "too low" or an indemnification
   clause as "too broad" is substantive legal analysis, not document QA. Stay in scope.

3. **Generating vague proposed corrections** — "Update the cross-reference" is not a
   correction. A correction must state the exact replacement text: "Replace 'Section 4.2'
   with 'Section 4.3 (Payment Terms)'." The correction must be ready to insert.

4. **Missing the holistic defined-term picture** — Auditing defined terms one by one
   without building a complete register first. The most important checks — synonym drift,
   duplicate definitions, and orphaned definitions — are only visible when you hold the
   full picture of every defined term in the document simultaneously.

5. **Classifying all missing elements as CRITICAL** — The absence of a governing law
   clause in a near-final commercial agreement is HIGH. The same absence in a side letter
   to an agreement that already specifies governing law may be intentional and fine.
   Context matters; apply the severity classification thoughtfully.

6. **Skipping Dimension 7 (Formatting) because it seems trivial** — Tracked changes and
   residual comment bubbles in an "executed" version of a contract have caused significant
   litigation. The document parties execute must be clean. Tracked changes are HIGH, not
   LOW.

7. **Running QA without a section map** — Validating cross-references by searching for the
   referenced section number without first building a complete list of all sections in the
   document will miss cases where both the reference and the target are wrong. Build the
   section map first.

8. **Ignoring incorporated documents** — Many contracts incorporate schedules, exhibits,
   annexes, or external agreements by reference. A cross-reference may be technically
   correct in the main agreement but point to a section in an attached schedule that has
   been deleted. Ask whether incorporated documents are available.

9. **Correcting pronoun consistency by always choosing one approach** — There are multiple
   valid approaches to gender-neutral drafting (role-based terms, singular "they," noun
   repetition). The goal is consistency within the document, not imposing a particular
   style. Flag inconsistency; do not override a deliberate drafting choice.

10. **Flagging "DRAFT" as CRITICAL when the document is, in fact, a draft** — Placeholder
    text and "DRAFT" watermarks are appropriate in working documents. The stage-context
    from Step 2 determines whether a placeholder is CRITICAL (near-final document), HIGH
    (clean draft being shared externally), or acceptable (internal working version).

11. **Validating dates without checking the calendar** — Stating "February 30 is an invalid
    date" is obvious. The subtler checks — February 29 in non-leap years (e.g., 2025),
    day-of-week mismatches (e.g., "Wednesday, March 15, 2025" when March 15, 2025 was a
    Saturday), and notice period arithmetic — require actually calculating against a
    calendar. Do the math.

12. **Delivering corrections without locations** — A correction without a location reference
    ("Clause 4.2, second sentence") cannot be implemented. Every correction entry must
    include the exact location so the drafter can find it in seconds.

13. **Treating party name consistency as a low-priority check** — Party name inconsistency
    ("Buyer" / "Purchaser") is a documented source of contract disputes. Courts have held
    that inconsistent use of party name terms can create ambiguity about which party an
    obligation was intended to bind. Classify synonym drift as HIGH, not MEDIUM.

14. **Single-dimension analysis** — Running only the defined terms check because that is
    what the user asked about, then overlooking a signature block mismatch or a CRITICAL
    broken cross-reference. Unless the user explicitly requests a targeted check, run all
    nine dimensions. The most dangerous errors are often not in the dimension the user
    suspected.

15. **Confusing substantive gaps with QA gaps** — A missing limitation of liability clause
    is a substantive risk issue (→ `legalcode-contract-review`). A missing governing law
    clause in a document type that always requires one is a completeness gap (→ this
    skill). The distinction is: QA gaps are about whether the document is correctly
    assembled; substantive gaps are about whether the terms protect the client.

---

## Writing Standards

Apply plain-language discipline to all output:

**For correction descriptions** (may be shared with the drafting team):
- State the error and its potential impact in one sentence
- Active voice: "Section 4.2 references 'Section 7.5' which does not exist" not "Section
  7.5 is referenced by Section 4.2 but cannot be found"
- Short sentences. One issue per entry.
- Name the location precisely: clause number, sentence position, or quoted text

**For proposed corrections**:
- Provide exact replacement text in quotation marks
- If deletion is required, state: "Delete '[quoted text]' in its entirety"
- If addition is required, state: "Insert '[text]' after '[anchor text]'"
- Never say "update the reference" without specifying the exact update

**Quality gates before delivery**:
1. Does every CRITICAL finding include an exact proposed correction?
2. Is every location reference specific enough for a drafter to find without searching?
3. Is the executive summary accurate (does the finding count match the corrections listed)?
4. Are all jurisdiction-specific checks correctly marked [JURISDICTION-SPECIFIC]?
5. Could any correction be misread as a substantive legal position? If yes, add a note
   clarifying that it is a drafting quality observation only.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**
- Verify jurisdiction-specific signature block requirements (witness, notarization,
  seal requirements) for the document's governing law
- Check whether specific document types require mandatory provisions under the applicable
  jurisdiction's law
- Verify current date-related legal requirements (notice periods under specific statutes,
  statutory form requirements)
- Mark all legalcode-mcp-sourced legal requirements as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**
- Mark all jurisdiction-specific checks with [JURISDICTION-SPECIFIC] and [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Flag signature block completeness checks as "requires jurisdiction-specific
  verification — [VERIFY witness/notarization requirements]"
- Focus the QA on the seven non-jurisdiction-dependent dimensions: defined terms,
  cross-references, party names, dates, numbering, pronouns, and formatting

---

## Localization Notes

The nine QA dimensions are largely universal, but several jurisdiction-specific overlays
apply:

**Signature block requirements:**
- **England & Wales**: Deeds require two witnesses OR a company execution under s.44 CA 2006
  ("executed as a deed" wording + two authorized signatories or one authorized signatory
  and a witness) [VERIFY current requirements]
- **US**: Notarization requirements vary by state and document type; powers of attorney and
  real estate instruments typically require notarization [VERIFY state-specific rules]
- **Civil law jurisdictions**: Many require notarization or apostille for certain
  instruments; authentic act form may be required for real property transactions [VERIFY]
- **Australia**: Requirements differ by state; deeds executed by companies require
  execution under s.127 Corporations Act 2001 or by an attorney [VERIFY]

**Language requirements:**
- Several jurisdictions require contracts to be in the local language or in bilingual form
  (France — Law No. 94-665, Belgium, Quebec) [VERIFY current requirements]. A QA audit of
  a document intended for use in such jurisdictions should flag if only an English version
  is present.

**Date format conventions:**
- Day-month-year format is standard in most of the world; month-day-year is standard in
  the US. A date written "3/4/2025" is ambiguous cross-jurisdictionally. Flag any
  date not written in unambiguous long-form (e.g., "March 4, 2025" or "4 March 2025").

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Document QA Report

**Document**: [Document title / identifier]
**Document Type**: [Contract / Deed / Policy / Filing / etc.]
**Document Stage**: [Draft / Near-final / Final / Template]
**Audit Date**: [date]
**Dimensions Audited**: [List of dimensions audited]

---

## Executive Summary

| Severity | Count |
|----------|-------|
| CRITICAL | [N]   |
| HIGH     | [N]   |
| MEDIUM   | [N]   |
| LOW      | [N]   |
| **Total** | **[N]** |

**Assessment**: [1-2 sentence assessment of the document's overall QA status, e.g.,
"This document has 2 CRITICAL issues that must be resolved before execution: an undefined
capitalized term in the payment clause and a broken cross-reference in the termination
clause. Once resolved, the document is otherwise in good shape with 4 HIGH items and 6
MEDIUM items that should be addressed before signing."]

**Recommendation**: [HOLD — resolve CRITICAL issues first / PROCEED WITH CAUTION — HIGH
items should be resolved / CLEAR FOR EXECUTION — only MEDIUM/LOW items remain]

---

## Tier 1 — Pre-Execution Blockers (CRITICAL)

[List each CRITICAL finding using the Correction Entry Format]

---

## Tier 2 — Pre-Execution Preferred (HIGH)

[List each HIGH finding using the Correction Entry Format]

---

## Tier 3 — Revision Cycle Items (MEDIUM and LOW)

[List each MEDIUM/LOW finding using the Correction Entry Format]

---

## Dimensions Audited — Summary by Category

| Dimension | Status | Findings |
|-----------|--------|----------|
| 1. Defined Term Audit | PASS / ISSUES | [N] findings |
| 2. Cross-Reference Integrity | PASS / ISSUES | [N] findings |
| 3. Party Name Consistency | PASS / ISSUES | [N] findings |
| 4. Date and Deadline Logic | PASS / ISSUES | [N] findings |
| 5. Numbering and Hierarchy | PASS / ISSUES | [N] findings |
| 6. Gender and Pronoun Consistency | PASS / ISSUES | [N] findings |
| 7. Formatting and Layout | PASS / ISSUES | [N] findings |
| 8. Signature Block Validation | PASS / ISSUES | [N] findings |
| 9. Substance Completeness Gaps | PASS / ISSUES | [N] findings |

---

[Glass Box Audit Trail — YAML as specified above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:
- Ken Adams, *A Manual of Style for Contract Drafting* (5th ed., ABA Publishing) — the
  leading reference on defined term precision, obligation/discretion distinction, and
  language consistency in commercial contracts [VERIFY current edition]
- ABA Business Law Today (November 2024) — analysis of busted cross-references and their
  legal consequences
- PerfectIt, LexCheck, Litera Contract Companion, and CrossCheck feature documentation —
  representing industry consensus on the most important automated QA checks
- BC Law Institute, *Gender Diversity in Legal Writing* (2021)
- Thomson Reuters research on the frequency and cost of legal document drafting errors
- Definely analysis: "Document and contract errors could lead to claims against your firm"
- Weagree contract drafting principles (date and consistency guidance)
- Lawyers Mutual NC: "Drafting Errors: Small Mistakes Can Lead to Big Claims"
- Legalcode cross-reference-analyzer skill structural patterns (Legalcode original,
  2026-03-21) — adapted defined-terms and cross-reference analysis dimensions
- Legalcode contract-review skill quality frameworks (Legalcode original, 2026-02-27) —
  Citation Quality Gates, Self-Interrogation, Confidence Scoring, and Glass Box audit trail
  patterns adapted to the document QA context
