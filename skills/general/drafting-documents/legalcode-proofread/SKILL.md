---
name: legalcode-proofread
description: Proofreads legal documents for defined term consistency, cross-reference accuracy, party
  name consistency, date logic, pronoun and referent consistency, section numbering, signature block completeness,
  exhibit and schedule references, and legalese errors (shall/will misuse, and/or, archaic boilerplate).
  Generates a structured redlined correction report classifying every finding as ERROR, WARNING, or SUGGESTION
  with specific correction language. Use for contracts, NDAs, employment agreements, leases, corporate
  documents, court filings, policies, and any legal document requiring pre-execution quality review. Triggers
  on phrases like "proofread this contract", "check for consistency errors", "review for defined terms",
  "find errors in this agreement", "check my cross-references", "proofread before signing", "check the
  signature blocks", "review for shall vs will", or "check for and/or usage".
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Proofread

> **Disclaimer**: This skill provides a framework for AI-assisted legal document
> proofreading. It does not constitute legal advice. Proofreading findings are
> mechanical and structural in nature — they do not address substantive legal
> adequacy, enforceability, or strategic risk. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before execution.
> Laws change; verify current applicability before relying on any provision described
> here. Statutory and case law references cited from memory carry hallucination risk —
> verify against authoritative sources before relying on them.

## Purpose and Scope

This skill performs comprehensive proofreading of legal documents — catching the
mechanical errors, inconsistencies, and drafting defects that legal review workflows
typically address last but that AI can systematically surface first.

**Covers:**

- Defined term consistency (definition tracking, orphan definitions, undefined term usage)
- Cross-reference accuracy (section, subsection, exhibit, schedule, and schedule item references)
- Party name consistency (legal names, defined shorthand, pronoun references)
- Date logic (effective dates, expiration, notice periods, retroactive dates, deadline arithmetic)
- Pronoun and referent consistency (it/its vs. they/their, masculine/feminine, entity vs. individual)
- Section numbering and document structure (gaps, duplicates, misnumbering, TOC accuracy)
- Signature block completeness (party identity, authority recitals, witness and notary requirements)
- Exhibit and schedule references (all referenced exhibits exist; all attached exhibits are referenced)
- Legalese and language errors (shall/will, and/or, archaic boilerplate, Latin phrases without translation)

**Does not:**

- Assess substantive legal risk or clause adequacy (see legalcode-contract-review)
- Generate negotiation redlines or advise on legal strategy
- Apply jurisdiction-specific mandatory provisions — this is a structural review
- Replace attorney review of legal content

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. Proofreading checks are structural and applicable
to legal documents across all jurisdictions. Jurisdiction-specific guidance appears where
relevant:

[JURISDICTION-SPECIFIC] When proofreading for a specific jurisdiction, additionally verify:

- Language requirements (some jurisdictions require contracts in the local language)
- Mandatory signature formalities (notarization, witnesses, apostille)
- Required recitals (consideration, capacity, authority statements)
- Specific prohibited terms (e.g., some jurisdictions restrict use of "shall")
- Dating conventions (DD/MM/YYYY vs. MM/DD/YYYY ambiguity in cross-border documents)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming intent, the workflow pauses and asks when:

- The answer would change the scope or focus of the proofreading
- Document structure ambiguity requires human judgment
- Multiple valid correction approaches exist

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

- **File**: PDF, DOCX, or other document format
- **URL**: Link to a document in a document management system or cloud storage
- **Pasted text**: Document text pasted directly into the conversation

If no document is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user:

1. **Document type**: What type of legal document is this?
   - Options: Commercial contract / NDA / Employment agreement / Lease / Corporate document (board resolution, articles, bylaws) / Court filing / Policy or procedure / Other
   - _Why this matters_: Document type determines which checks are most critical (e.g., court filings have strict formatting rules; corporate documents have authority-recital requirements).

2. **Scope of review**: What level of proofreading is needed?
   - Options: **Full proofreading** (all 9 categories, comprehensive), **Focused check** (specific categories only — user specifies), **Pre-execution fast-pass** (errors and warnings only, no suggestions)
   - _Why this matters_: Full proofreading is thorough but lengthy; a fast-pass surfaces only material issues.

3. **Output format**: How should findings be delivered?
   - Options: **By section** (findings organized as they appear in the document), **By category** (all defined-term errors together, all cross-reference errors together, etc.), **Summary only** (totals and top issues), **Full report with corrections**
   - _Why this matters_: Different audiences prefer different formats — editors prefer by-section; quality reviewers prefer by-category.

4. **Known issues**: Are there any specific areas of concern?
   - Free text. Examples: "the exhibit references were updated last minute", "the defined terms section was edited by multiple people", "signature blocks need to be finalized."
   - _Why this matters_: Lets the review lead with the user's highest-concern areas first.

If the user provides partial context, proceed with reasonable defaults and state assumptions explicitly.

### Step 3: First Pass — Document Structure

Before checking individual items, perform a structural read of the entire document:

1. **Identify document parts**: Main body, recitals/preamble, defined terms section (if separate), schedules, exhibits, attachments, and annexes.
2. **Build the party register**: List every party, their full legal name, defined shorthand (e.g., "Company"), and any pronouns used to refer to them.
3. **Build the defined term register**: List every capitalized defined term in the document (both where defined and every use location). Flag terms that appear in ALL CAPS or quotation marks as alternative definition conventions.
4. **Build the section map**: List all section and subsection numbers to enable cross-reference verification.
5. **Build the exhibit/schedule list**: List every exhibit and schedule referenced in the body, and every exhibit and schedule actually attached or labeled.
6. **Identify all dates**: List every date, date range, and deadline referenced in the document.

Save this structural data as a working reference for the subsequent checks. If the
document is long (50+ pages), note that some structural data may require selective
sampling rather than exhaustive enumeration.

**⟁ CLARIFY** — For very long documents or documents with complex schedules:

- Ask whether to perform a **full structural parse** of all sections and schedules, or a
  **focused parse** of the main body plus identified problem areas.
- Ask whether incorporated-by-reference documents (e.g., "Company's Privacy Policy at
  [URL]") should be included in cross-reference verification.

### Step 4: Run the Nine Proofreading Checks

Run all nine checks systematically. For each finding, assign a severity (ERROR / WARNING / SUGGESTION) using the classification in the **Finding Severity Classification** section.

#### Check 1 — Defined Term Consistency

The most common and consequential proofreading error in legal documents.

**1a. Undefined terms used as defined terms**

- Scan every capitalized word or phrase that is used as if it were a defined term.
- Verify each appears in the definitions section (or is defined inline at first use).
- Flag every capitalized term used without a definition as **ERROR**.

**1b. Defined terms not used (orphan definitions)**

- For each term in the definitions section, verify it appears at least once in the document body (other than the definition itself).
- Flag terms defined but never used as **WARNING** (wastes the reader's time; may indicate a deleted provision left a dangling definition).

**1c. Inconsistent defined term labels**

- Verify each concept has exactly one defined term. Flag synonyms used interchangeably for the same concept (e.g., "Services", "the services", "work product") as **WARNING**.
- Check whether defined terms with similar names refer to different concepts in ways that could cause confusion (e.g., "Agreement" and "this Agreement").

**1d. Incorrect capitalization**

- Flag defined terms used in lowercase (e.g., "the parties agree" when "Party" is a defined term) as **WARNING**.
- Flag common words incorrectly capitalized as if they were defined terms (e.g., "the Services and Deliverables" where only "Services" is defined, not "Deliverables") as **WARNING**.

**1e. Definition drift**

- Check whether a defined term is given a narrower or broader meaning in one section than its formal definition suggests. Flag material inconsistencies as **ERROR**.

**Common errors by document type:**

- Contracts: "Agreement" vs. "this Agreement" vs. "the Agreement" (inconsistency)
- Employment agreements: "Employee" vs. "Executive" used interchangeably
- Leases: "Premises" vs. "the Premises" vs. "Leased Premises"
- Corporate documents: "Corporation" vs. "Company" vs. the entity's formal name

#### Check 2 — Cross-Reference Accuracy

**2a. Section references**

- For every internal cross-reference (e.g., "as set forth in Section 5.2(b)"), verify:
  - The referenced section exists.
  - The referenced section covers the subject matter the reference implies.
  - The reference format matches the document's numbering convention (e.g., "Section 5.2(b)" vs. "§ 5.2(b)" vs. "Clause 5.2(b)").
- Flag broken references (section doesn't exist) as **ERROR**.
- Flag plausible misreferences (section exists but covers different subject matter) as **ERROR**.
- Flag formatting inconsistencies in reference style as **WARNING**.

**2b. Defined term references in cross-references**

- Where a cross-reference incorporates a defined term (e.g., "the Permitted Uses described in Section 3"), verify the named concept actually appears in the referenced section.
- Flag mismatches as **ERROR**.

**2c. "Above" / "below" / "herein" references**

- Flag the use of "above", "below", "herein", "hereinafter", "hereinbefore", and "as provided herein" without a specific section reference as **WARNING** (these break when the document is reorganized).

**2d. Incorporated document references**

- Where the document incorporates an external document by reference (e.g., "subject to the Master Services Agreement dated [date]"), verify the reference is complete: document title, parties (if applicable), and date.
- Flag incomplete external references as **WARNING**.

#### Check 3 — Party Name Consistency

**3a. Full legal name accuracy**

- Verify each party's full legal name is stated correctly in the preamble/recitals.
  Common errors: incorrect entity type suffix (Ltd. vs. Limited vs. LLC), incorrect state/jurisdiction of organization, misspelled names, wrong registered name vs. trading name.
- Flag factual name errors as **ERROR** (requires external verification — mark [VERIFY]).

**3b. Defined shorthand consistency**

- Verify each party's defined shorthand (e.g., "Company", "Supplier", "Employee") is used consistently throughout the document.
- Flag instances where the party is referred to by their full legal name after the shorthand is established as **WARNING**.
- Flag instances where the shorthand is used before it is defined as **ERROR**.

**3c. Pronoun consistency for entities**

- Verify that corporate entities are referred to as "it" and "its" (not "they", "their", "he", "she", "his", "her") unless the document deliberately uses plural or gendered language.
- [JURISDICTION-SPECIFIC] Some jurisdictions or drafting traditions use "they/their" for entities — note this as a style choice, not an error.
- Flag inconsistent pronoun use (mixing "it" and "they" for the same entity in the same document) as **WARNING**.

**3d. Signatory and party alignment**

- Verify the parties listed in the signature blocks match exactly the parties identified in the preamble.
- Flag mismatches (a party appearing in the signature block but not the preamble, or vice versa) as **ERROR**.

#### Check 4 — Date Logic

**4a. Effective date**

- Identify the stated effective date and verify it is internally consistent.
- Flag any provision that becomes effective before the document's effective date without explicit retroactivity language as **WARNING**.
- Flag retroactive effective dates without consideration language as **WARNING** (may raise enforceability issues — mark [VERIFY]).

**4b. Deadline arithmetic**

- For every notice period, cure period, or response deadline (e.g., "30 days after the Effective Date", "within 5 Business Days of receipt"), verify:
  - The arithmetic is internally consistent (start date + period = stated end date, where applicable).
  - Whether "days" means calendar days or business days is specified — flag ambiguity as **WARNING**.
  - "Business Days" is defined if used — flag undefined use as **ERROR**.

**4c. Expiration and renewal dates**

- For fixed-term agreements, verify the term length and end date arithmetic is consistent (e.g., if effective date is January 1, 2026, and term is "two years," the expiration should be January 1, 2028 or December 31, 2027 — check which convention is used and flag inconsistency as **ERROR**).
- Verify auto-renewal notice deadlines precede the renewal date by a sufficient margin.

**4d. Date format consistency**

- Verify all dates use a consistent format throughout the document.
- [JURISDICTION-SPECIFIC] Flag DD/MM/YYYY vs. MM/DD/YYYY ambiguity (dates like "03/04/2026" are ambiguous in cross-border documents) as **WARNING**. Recommend spelling out the month.

**4e. Future/past date errors**

- Flag dates that are clearly incorrect for the document's context (e.g., an execution date listed as a past year in a document intended to be signed today, unless intentionally retroactive) as **ERROR** (mark [VERIFY] — requires user confirmation).

#### Check 5 — Pronoun and Referent Consistency

**5a. Referent clarity**

- For each pronoun ("it", "they", "he", "she", "which", "that", "who"), verify the referent is unambiguous. When a sentence contains multiple nouns that could be the referent, flag as **WARNING**.
- Example of ambiguous referent: "The Company shall notify the Supplier that it has received the Deliverables" — "it" could refer to Company or Supplier.

**5b. Collective noun consistency**

- Where a party is a collective noun ("the Committee", "the Board"), verify the pronouns used (it/its vs. they/their) are consistent throughout.

**5c. Defined term gender**

- Where the document uses gendered language for individuals (e.g., "he or she", "his or her"), verify it is consistent throughout. Flag inconsistent use (sometimes "he", sometimes "they") as **WARNING**.
- Flag singular "they/their" for a specifically identified individual as a style note (SUGGESTION) unless the user has specified a preference.

**5d. "Such" and "said" archaisms**

- Flag use of "such [noun]" as a demonstrative (e.g., "such Services" meaning "the Services") as **SUGGESTION** (replace with "the" or "those" for plain language). Document the count but do not flag each instance individually unless the user requests full granularity.

#### Check 6 — Section Numbering and Document Structure

**6a. Numbering sequence integrity**

- Verify section numbers follow a consistent sequence with no gaps, duplicates, or out-of-order numbering.
- Flag gaps (e.g., jumping from Section 4 to Section 6) as **ERROR** unless the gap is explained by intentional deletion with a note.
- Flag duplicate section numbers as **ERROR**.
- Flag out-of-order sections (where the text of a section clearly belongs to a different numbered position) as **WARNING**.

**6b. Subsection numbering consistency**

- Verify subsection numbering format is consistent throughout (e.g., 1.1, 1.2, 1.3 — not mixed with (a), (b), (c) at the same level without a clear convention).
- Flag inconsistent numbering format at the same hierarchical level as **WARNING**.

**6c. Table of contents accuracy**

- If a table of contents is present, verify section titles and page numbers match the document body.
- Flag mismatched section titles as **ERROR** (title in TOC vs. body disagree).
- Flag incorrect page numbers as **WARNING** (common in documents assembled from multiple drafts).

**6d. Heading and section title consistency**

- Verify section heading capitalization convention is consistent (all caps, title case, or sentence case — pick one).
- Flag inconsistent heading formatting as **SUGGESTION**.

#### Check 7 — Signature Block Completeness

**7a. Party identification in signature blocks**

- Verify each signature block identifies the signing party's:
  - Full legal name (matching the preamble exactly)
  - Entity type (e.g., "a Delaware limited liability company") [JURISDICTION-SPECIFIC]
  - Signatory name field (blank line or "[Name]" placeholder)
  - Signatory title field
  - Date field
- Flag missing elements as **ERROR** for legal name and **WARNING** for other fields.

**7b. Authority recitals**

- For corporate entities, verify the signature block includes language confirming the signatory is authorized (e.g., "By: **\_\_\_** [Authorized Signatory]" or "Executed by authority of the board").
- [JURISDICTION-SPECIFIC] Some jurisdictions require specific authority statements — flag absence as **WARNING** with a [VERIFY] tag.

**7c. Witness and notarization requirements**

- [JURISDICTION-SPECIFIC] For document types requiring witnesses or notarization (e.g., deeds in England & Wales, some US real property instruments, apostilled documents), verify witness/notary fields are present.
- Flag absent witness or notary blocks as **ERROR** where required. Mark with [VERIFY] since this depends on jurisdiction and document type.

**7d. Counterparts clause alignment**

- If the document includes a counterparts clause (allowing separate signature pages to constitute a single agreement), verify the signature blocks are consistent with this — each party has its own full signature block.
- Flag a single combined signature block in a document with a counterparts clause as **WARNING**.

**7e. Electronic signature readiness**

- [JURISDICTION-SPECIFIC] If the document will be signed electronically, verify there is no language requiring "wet ink" signature or physical delivery.
- Flag conflicting provisions as **WARNING**.

#### Check 8 — Exhibit and Schedule References

**8a. References in body → exhibits exist**

- For every reference in the document body to an exhibit, schedule, appendix, or attachment (e.g., "as set forth in Exhibit A", "the form of SOW attached hereto as Schedule 1"), verify the referenced document is actually attached.
- Flag references to exhibits or schedules that are not attached as **ERROR**.
- Flag references to exhibits or schedules listed as "to be attached" or "intentionally omitted" as **WARNING** (requires user to confirm whether this is intentional).

**8b. Attached exhibits → referenced in body**

- For every exhibit, schedule, or attachment actually included in the document, verify it is referenced somewhere in the document body.
- Flag attached documents with no reference in the body as **WARNING** (orphan exhibit — may indicate a deleted provision that referenced it).

**8c. Exhibit list accuracy**

- If the document has a "List of Exhibits" or "Table of Schedules," verify the list matches the actual attached documents exactly (in title, letter/number designation, and order).
- Flag discrepancies between the exhibit list and actual exhibits as **ERROR**.

**8d. Exhibit internal cross-references**

- For exhibits that reference the main agreement (e.g., "as defined in the Agreement"), verify the referenced defined terms exist in the main agreement.
- Flag undefined term references in exhibits as **WARNING**.

#### Check 9 — Legalese and Language Errors

**9a. Shall vs. will**

- Apply the Garner/Kimble standard: "shall" should be reserved for imposing a mandatory obligation on the subject of the sentence (the subject must do something). "Will" should be used for future statements of fact, conditions, or predicates.
- Flag common misuses of "shall":
  - "The Agreement shall be governed by the laws of..." — this is a future fact, not a mandatory obligation; use "is governed by" or "will be governed by" — flag as **WARNING**.
  - "Supplier shall have the right to..." — "shall" conferring a right is a classic error; use "may" — flag as **WARNING**.
  - "In the event that [condition] shall occur..." — conditional "shall" is archaic; use "if [condition] occurs" — flag as **SUGGESTION**.
- Flag inconsistent use of "shall" and "will" in comparable obligation provisions as **WARNING** (e.g., "Company shall deliver" but "Supplier will deliver").

**9b. And/or**

- Flag every instance of "and/or" as **WARNING**. This construction is widely condemned in legal drafting because it is ambiguous (does it mean "and" or "or" or "both"?).
- For each instance, suggest the appropriate clarification:
  - If both is intended: "A and B, or either of them"
  - If either/both is intended: "A or B, or both"
  - If one exclusive: "A or B (but not both)"

**9c. Archaic boilerplate**

- Flag the following archaic terms as **SUGGESTION** with plain-language alternatives:
  - "Witnesseth" → Delete (or replace with "Background" or "Recitals")
  - "In witness whereof" → "Signed" or "Executed"
  - "NOW, THEREFORE, in consideration of the mutual covenants..." → Delete or simplify
  - "Hereinafter" → Use the defined shorthand directly
  - "Hereinbefore" / "Hereinafter referred to as" → Use the defined term
  - "Hereto" / "hereof" / "hereunder" → Specify the document and section explicitly
  - "The parties hereby agree as follows" → "The parties agree:"
  - "It is agreed and understood that" → Delete and state the substantive point
  - "For and in consideration of" → "In consideration of"
  - "Any and all" → "all" (or "any", depending on meaning)
  - "Terms and conditions" when used as a single defined concept → Pick one

**9d. Tautological doublets and triplets**

- Flag common legal doublets and triplets as **SUGGESTION**:
  - "null and void" → "void"
  - "cease and desist" → "stop"
  - "each and every" → "each" or "every"
  - "by and between" → "between"
  - "over and above" → "beyond" or "in addition to"
  - "true and correct" → "accurate" or "correct"
  - "acknowledge and agree" → "acknowledge" or "agree" (depending on meaning)
  - "unless and until" → "until" (usually)
  - "final, non-appealable" → verify whether both qualifiers are needed

**9e. Latin and archaic phrases**

- Flag Latin phrases without translations as **SUGGESTION** (include the translation as an alternative):
  - "inter alia" → "including" or "among other things"
  - "pari passu" → "equally and ratably" (flag in non-financial documents)
  - "mutatis mutandis" → "with the necessary changes" or restate the provision explicitly
  - "prima facie" → "on its face" or "presumptively"
  - "pro rata" → acceptable in most jurisdictions; flag only if context is unclear

**9f. Defined term in all-caps**

- Some documents define terms in ALL CAPS rather than Title Case. Flag inconsistencies where some defined terms are ALL CAPS and others are Title Case as **WARNING**.

### Step 5: Consolidate and Classify Findings

After completing all nine checks:

1. Count findings by severity and category.
2. If total findings exceed 50, present a summary first and ask the user whether to receive the full report or a prioritized subset.
3. Apply the **Finding Severity Classification** (below) to confirm each severity assignment.
4. For each ERROR, apply the 2-pass self-interrogation (below).

**⟁ CLARIFY** — For documents with a large number of SUGGESTION-level findings (especially archaic boilerplate):

- Ask: "I found [N] suggestions for modernizing archaic language (e.g., 'Witnesseth', 'and/or', 'null and void'). Should I include all of them, provide a summary count by type, or skip suggestions entirely and focus on errors and warnings?"

### Step 6: Generate the Correction Report

Using the **Output Format Template** (below), generate the correction report organized by the user's preferred format (by section or by category).

For each finding, provide:

- Section reference and finding number
- Severity (ERROR / WARNING / SUGGESTION)
- Category (which of the 9 checks)
- Current text (exact quote or description)
- Correction (specific replacement text or instruction)
- Brief rationale (one sentence)

### Step 7: Quality Verification

Before delivering the report:

1. Run the 5 Citation Quality Gates silently.
2. For every ERROR, run the 2-pass Self-Interrogation.
3. Verify the finding count matches the checklist: all 9 categories have been addressed (or explicitly noted as clean).
4. Generate the Glass Box Audit Trail.
5. Apply the Writing Standards quality gates.

---

## Finding Severity Classification

### ERROR — Must Fix Before Execution

A finding that, if uncorrected, will cause one or more of:

- Ambiguity about a material legal obligation or right
- A broken reference that renders a provision unenforceable or unworkable
- A factual error (wrong party name, wrong date) that could undermine the agreement
- An internal contradiction between provisions

**Examples:**

- Defined term used but never defined
- Cross-reference pointing to a nonexistent section
- Exhibit referenced but not attached
- Party in signature block does not match party in preamble
- Two provisions directly contradict each other on a material point
- Date arithmetic error (stated term length doesn't match dates)

**Action**: Correction is mandatory before execution. Provide specific replacement text.

### WARNING — Should Fix Before Execution

A finding that introduces unnecessary risk, ambiguity, or inconsistency that a careful
drafter would address:

**Examples:**

- Defined term used in lowercase (breaks the definitional convention)
- "And/or" usage (ambiguous)
- Party referred to by shorthand before the shorthand is introduced
- Inconsistent date format (DD/MM vs. MM/DD ambiguity)
- Orphan definition (defined but never used — may indicate a deleted provision)
- "Shall" conferring a right rather than imposing an obligation
- Missing Business Days definition when the term is used
- Inconsistent pronoun for the same entity

**Action**: Correction is strongly recommended. Provide correction language. User may consciously accept the risk.

### SUGGESTION — Consider Fixing

A finding that reflects a best-practice improvement but does not create legal risk or
material ambiguity:

**Examples:**

- Archaic boilerplate ("Witnesseth", "hereinafter", "NOW, THEREFORE")
- Tautological doublets ("null and void", "any and all")
- Latin phrases without translations (in non-technical contexts)
- Inconsistent heading capitalization style
- "Such [noun]" as a demonstrative (replace with "the")
- Conditional "shall" (replace with "if...then" construction)

**Action**: Correction is optional. Provide alternatives. User decides based on house style.

---

## Actionable Output Per Finding

For every finding, use this format:

```
**Finding [number]** | [SEVERITY] | Category: [check name] | Section [X.X]

**Current**: "[exact text or description of the issue]"

**Correction**: "[specific corrected text or instruction]"

**Why**: [One sentence rationale]
```

**For ERROR findings**, additionally include:

- **Impact**: Brief statement of what goes wrong if uncorrected.

**For SUGGESTION findings** that occur many times in the document:

- Group them: "Found 7 instances of 'and/or' in Sections 2.1, 3.4, 5.2, 6.1, 7.3, 8.5, 9.2. Correction for each: replace 'A and/or B' with 'A or B, or both' (or 'A, B, or both' for lists). See Section-by-Section detail for specific language."

---

## Prioritization Framework

When the document has many findings, organize the correction effort:

### Priority 1 — Execute Immediately (All ERRORs)

All findings classified as ERROR must be resolved before the document is executed.
Prioritize findings that:

- Affect party identity (party name errors, signature block mismatches)
- Break cross-references to material provisions (indemnification, liability, payment)
- Create undefined obligations (undefined defined terms used in operative provisions)
- Create internal contradictions on material terms

### Priority 2 — Fix Before Circulation (Critical WARNINGs)

Address WARNINGs that could create ambiguity or embarrassment in negotiation:

- "And/or" in operative provisions
- Shall/will misuse in obligation and rights provisions
- Date format ambiguity in cross-border documents
- Orphan definitions that may confuse the other side

### Priority 3 — Polish Before Execution (Remaining WARNINGs + Selected SUGGESTIONs)

Address remaining WARNINGs and any SUGGESTIONs the drafter wishes to incorporate:

- Archaic boilerplate cleanup
- Inconsistent heading style
- Tautological doublets
- Referent ambiguity in non-material provisions

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                         | Fail Action                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| **Source**     | Every ERROR finding identifies the specific text location and explains the specific error                                                                    | Add location and error description                            |
| **Format**     | All section references in findings match the document's own numbering convention                                                                             | Fix reference format                                          |
| **Currency**   | Where a finding involves a legal standard (e.g., "shall" usage rules), the standard is current and accurate for the governing law                            | Mark "[VERIFY] — applies to [jurisdiction] drafting practice" |
| **Domain**     | Findings stay within the document's own scope — no external legal requirements assumed without [JURISDICTION-SPECIFIC] or [VERIFY] tags                      | Remove or flag out-of-scope findings                          |
| **Confidence** | Uncertainty about whether something is an error is explicitly stated — do not flag a drafting choice as an error without acknowledging it may be intentional | Add confidence qualifier                                      |

### Self-Interrogation for ERROR Findings

For any finding classified as ERROR, apply this 2-pass review:

**Pass 1 — False Positive Check**:

- Is this actually an error, or could it be an intentional drafting choice?
- Is the cross-reference broken, or is the referenced section present under a slightly different numbering format?
- Is the defined term really undefined, or is it defined elsewhere in the document (e.g., in an incorporated exhibit)?
- If the user might contest this classification, acknowledge the ambiguity in the finding.

**Pass 2 — Completeness**:

- Does the correction fix the entire problem, or could the corrected version introduce a new issue?
- Are there other places in the document affected by the same error that the correction should also address?

If either pass reveals a weakness, revise the finding before delivery. Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each proofreading check category, assign a confidence level:

| Level        | Range     | Meaning                                                                                                                     | Action                                                        |
| ------------ | --------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Mechanically verifiable: broken section reference, duplicate section number, attached exhibit with no body reference        | State with confidence                                         |
| **High**     | 0.80-0.94 | Strong convention: "shall" conferring a right, "and/or" ambiguity, orphan definition                                        | State with brief caveat                                       |
| **Probable** | 0.60-0.79 | Interpretation-dependent: pronoun referent ambiguity, date arithmetic in complex provisions                                 | State with reasoning                                          |
| **Possible** | 0.40-0.59 | Genuinely uncertain: whether a capitalized term is a defined term or a title, intentional vs. unintentional drafting choice | Flag for user confirmation                                    |
| **Unlikely** | 0.0-0.39  | Speculative                                                                                                                 | Do not flag as an error; note as a potential observation only |

---

## Glass Box Audit Trail

Every proofreading output MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-proofread"
  document: "[Document title and date]"
  document_type: "[Contract / NDA / Employment / Lease / Corporate / Court Filing / Other]"
  pages_reviewed: "[number or 'unknown']"
  parties_identified: "[number] — [party list]"
  defined_terms_catalogued: "[number]"
  sections_in_map: "[number]"
  exhibits_referenced: "[number]"
  exhibits_attached: "[number]"
  checks_run: "9/9 — [or list omitted checks with reason]"
  total_findings:
    errors: "[number]"
    warnings: "[number]"
    suggestions: "[number]"
  findings_by_category:
    defined_term_consistency: "[ERROR: N | WARNING: N | SUGGESTION: N]"
    cross_reference_accuracy: "[ERROR: N | WARNING: N | SUGGESTION: N]"
    party_name_consistency: "[ERROR: N | WARNING: N | SUGGESTION: N]"
    date_logic: "[ERROR: N | WARNING: N | SUGGESTION: N]"
    pronoun_referent_consistency: "[ERROR: N | WARNING: N | SUGGESTION: N]"
    section_numbering: "[ERROR: N | WARNING: N | SUGGESTION: N]"
    signature_blocks: "[ERROR: N | WARNING: N | SUGGESTION: N]"
    exhibit_schedule_references: "[ERROR: N | WARNING: N | SUGGESTION: N]"
    legalese_language: "[ERROR: N | WARNING: N | SUGGESTION: N]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no ERRORs)"
  legalcode_mcp: "Connected / Not connected"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations — e.g., 'Document was pasted without formatting; section numbers inferred']"
    - "[Any findings requiring user confirmation — e.g., '[VERIFY]: party name accuracy']"
  reviewer: "AI-assisted — requires qualified legal review before execution"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do when proofreading legal documents:

1. **Flagging style choices as errors** — "Witnesseth" and archaic boilerplate are not errors — they are SUGGESTIONs. The user's house style may deliberately use traditional language. Distinguish mandatory corrections from preferences.

2. **Ignoring exhibit consistency** — Many proofreaders check the body but not the exhibits. Exhibits often contain defined terms from the main agreement that have been deleted or renamed. Check exhibits against the current defined terms register.

3. **Treating capitalization as always intentional** — Legal drafters frequently forget to capitalize defined terms after edits. A lowercase word that matches a defined term should be flagged, not ignored.

4. **Missing the orphan definition problem** — Definitions sections grow through successive drafts. When provisions are deleted, their defined terms often remain. A document with unused definitions suggests incomplete editing and confuses readers.

5. **Partial cross-reference verification** — Checking whether a referenced section number exists without checking whether it covers the subject matter the reference implies. Section 5.2 may exist but may cover something completely different if sections were renumbered.

6. **Ignoring date ambiguity in cross-border documents** — "03/04/2026" is March 4 in the US and April 3 in the UK. In any cross-border document, date format ambiguity is a latent error waiting to cause real-world confusion.

7. **Not verifying exhibit attachment** — Marking exhibit references as clean without confirming the exhibits are actually attached (or noting they are "to be attached"). Many executed contracts are missing their exhibits.

8. **Over-flagging "shall"** — "Shall" has a legitimate role in legal drafting: imposing mandatory obligations. The problem is its misuse to confer rights ("shall have the right to") and state future facts. Do not flag every "shall" — only the specific misuse patterns.

9. **Under-counting "and/or"** — "And/or" almost always occurs multiple times in a document once it appears once. Searching for the first instance and stopping is incomplete. Flag every instance.

10. **Accepting incomplete signature blocks** — A signature block missing the title line, the date line, or the notice address (if required by the notice clause) is incomplete. Incomplete signature blocks are discovered at the worst possible time — at execution.

11. **Not checking TOC against body** — Documents with a table of contents are often assembled from multiple drafts that caused the TOC to drift from the body. This is a high-frequency error that is easy to miss if the TOC is not explicitly verified.

12. **Treating party shorthand as interchangeable with full name** — After defining "Acme Corp." as "Company," the document should use "Company" consistently. Reverting to "Acme" or "Acme Corp." in later sections is a WARNING, not a formatting preference.

13. **Ignoring exhibit internal cross-references** — An exhibit referencing "the Agreement" or "as defined above" inherits all the definitional issues of the main document. Exhibits must be checked against the main document's defined terms.

14. **Classifying every archaic phrase as an error** — Some archaic phrases ("pari passu," "pro rata") remain standard in specific contexts (finance, corporate law). Context matters. Flag them as SUGGESTION with context-appropriate alternatives, not as mandatory corrections.

15. **Single-pass review** — A legal document read once top-to-bottom will miss issues that span sections (e.g., a definition introduced in Section 14 used in Section 3 before it is defined). Build the structural register first, then apply the checks — not the other way around.

16. **Ignoring the relationship between checks** — A broken section reference and a missing exhibit are separate findings, but they may have the same root cause (a provision was deleted in a late draft). When multiple findings cluster around the same section, note the pattern — the issue may be more systemic than it appears.

17. **Not flagging "[INTENTIONALLY LEFT BLANK]" without content** — Sections marked "Intentionally Left Blank" that contain text, or sections with content where "Intentionally Left Blank" was expected, are ERROR-level issues that are easy to miss.

18. **Accepting a generic "[Date]" placeholder as a completed date** — Unfilled date placeholders in an executed document are errors. Scan for "[Date]", "[●]", "\_\_\_", and similar placeholder formats and flag each as ERROR.

---

## Writing Standards

Apply plain-language discipline to all correction report output:

**For correction language** (will become the corrected document):

- Use exact replacement language — not paraphrases or descriptions of what to change.
- Match the document's defined term conventions.
- Match the document's obligation language style (if the document uses "shall", use "shall" in corrections, unless the finding is about "shall" misuse).
- Keep corrections minimal — change only what is needed to fix the specific error.

**For rationale lines**:

- One sentence maximum.
- Active voice: "This reference points to Section 4.3, which addresses payment terms, not the defined term described in the text."
- Name the specific problem: not "this is incorrect" but "the section number does not exist in this document."

**For the report summary**:

- Start with the finding counts (ERRORs first).
- Flag the highest-severity items in the first paragraph.
- Organize by priority, not discovery order.

**Quality gates before delivery**:

1. Does every ERROR finding include specific correction language (not just an identification of the problem)?
2. Is every section reference in the findings accurate against the actual document?
3. Are all [VERIFY] tags explained with what needs to be verified and by whom?
4. Is any finding vague? ("This section may have issues" is not a finding — identify the specific issue.)
5. Could any rationale be shorter without losing meaning?

---

## External Tool Integration

**With legalcode-mcp connected:**

- Search for jurisdiction-specific proofreading requirements where [JURISDICTION-SPECIFIC] flags are raised.
- Verify current authority on "shall" vs. "will" drafting conventions for the governing law's jurisdiction.
- For signature block completeness, search for execution formality requirements in the governing jurisdiction.
- Mark all legalcode-mcp-sourced guidance as VERIFIED in the Glass Box audit trail.

**Without legalcode-mcp:**

- Mark all jurisdiction-specific findings with [VERIFY].
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`.
- Focus on mechanical consistency checks (defined terms, cross-references, section numbering) rather than jurisdiction-specific formality requirements.
- All findings remain valid — legalcode-mcp supplements the analysis with legal authority but is not required for the structural checks.

---

## Localization Notes

This skill is jurisdiction-agnostic. The nine proofreading checks apply universally.
Jurisdiction-specific considerations:

| Jurisdiction                | Notable Proofreading Considerations                                                                                                                                                                                  |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **England & Wales**         | "Shall" vs. "will" debate active — Law Commission recommends eliminating "shall" entirely; flag all "shall" as at least SUGGESTION. Deed execution requirements (witness signatures, delivery). [VERIFY]             |
| **United States**           | "Shall" remains standard in many contexts. Business Days definition should reference specific US federal holidays. State-specific execution requirements vary (notarization for real property instruments). [VERIFY] |
| **European Union**          | Documents in languages other than English may require official translation — flag if English document will govern a party whose jurisdiction requires a local-language original. [VERIFY]                            |
| **Australia**               | Deeds require witness signatures; contracts do not. ACL-prohibited terms are a substantive issue (not proofreading), but flag blanket "AS IS" disclaimers for [VERIFY]. [VERIFY]                                     |
| **Nordic jurisdictions**    | Tend to have shorter, plainer contract language — archaic boilerplate is a stronger SUGGESTION here.                                                                                                                 |
| **Civil law jurisdictions** | Watch for common-law concepts imported without translation (e.g., "indemnify and hold harmless" has no direct civil-law equivalent — flag for [JURISDICTION-SPECIFIC] review).                                       |

---

## Output Format Template

Structure the correction report as follows:

```markdown
## Legalcode Proofread — Correction Report

**Document**: [document title or description]
**Document Type**: [contract type]
**Date of Review**: [date]
**Reviewer**: AI-assisted (legalcode-proofread) — requires qualified legal review

---

### Executive Summary

**Total Findings**: [N] ERRORs | [N] WARNINGs | [N] SUGGESTIONs

**Priority action required before execution**:

- [List the top 3-5 most critical errors]

**Overall document quality**: [CLEAN / MINOR ISSUES / SIGNIFICANT ISSUES / REQUIRES SUBSTANTIAL CORRECTION]

- CLEAN: 0 ERRORs, ≤5 WARNINGs
- MINOR ISSUES: 1-5 ERRORs, ≤15 WARNINGs
- SIGNIFICANT ISSUES: 6-15 ERRORs, any number of WARNINGs
- REQUIRES SUBSTANTIAL CORRECTION: 15+ ERRORs or systemic issues across 3+ categories

---

### Findings by Category [or by Section — per user preference]

#### [Category 1: Defined Term Consistency]

| #     | Severity | Section | Issue                            | Correction       |
| ----- | -------- | ------- | -------------------------------- | ---------------- |
| F-001 | ERROR    | §[X]    | "[current text]" — [description] | [corrected text] |
| F-002 | WARNING  | §[Y]    | "[current text]" — [description] | [corrected text] |

[Additional categories follow same format]

---

### Priority 1 — Fix Before Execution (All ERRORs)

[List all ERROR findings with full detail format]

### Priority 2 — Fix Before Circulation (Critical WARNINGs)

[List all WARNING findings]

### Priority 3 — Polish (SUGGESTIONs)

[List all SUGGESTION findings, grouped by type if numerous]

---

### Defined Term Register

| Term   | Defined In            | Definition Location | Use Count | Status                           |
| ------ | --------------------- | ------------------- | --------- | -------------------------------- |
| [Term] | [Section or Preamble] | [§X.X or inline]    | [N]       | ✅ OK / ⚠️ Orphan / ❌ Undefined |

---

### Exhibit/Schedule Checklist

| Exhibit/Schedule   | Referenced In Body | Attached       | Status             |
| ------------------ | ------------------ | -------------- | ------------------ |
| Exhibit A — [Name] | §[X.X]             | ✅ Yes / ❌ No | ✅ OK / ❌ Missing |

---

### Signature Block Review

| Party     | Legal Name in Preamble | Legal Name in Sig Block | Match?  | Missing Fields |
| --------- | ---------------------- | ----------------------- | ------- | -------------- |
| [Party 1] | [Full name]            | [Sig block name]        | ✅ / ❌ | [List]         |

---

[Glass Box Audit Trail — YAML block]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis for the legalcode skill collection.
Research basis: web-backed research via Explore agent covering legal document proofreading
best practices (Bryan Garner's Legal Writing in Plain English, Adams' Manual of Style for
Contract Drafting, Kimble's Lifting the Fog of Legalese, ABA legal drafting guidance,
law firm proofreading checklists, legal technology platform documentation). Structural
quality frameworks adapted from the legalcode-contract-review gold standard skill.

**Attribution**: Legalcode original — created from scratch (Mode A).
