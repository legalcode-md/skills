---
name: legalcode-defined-term-audit
description: Extracts and audits all defined terms in one or more legal documents — flags unused (orphaned)
  definitions, terms used but never defined, circular definitions, inconsistent usage, overly broad definitions,
  precision gaps, shadowed definitions, and conflicting definitions across related documents. Use when
  conducting pre-execution quality review of any contract, agreement, policy, regulation, or legislation;
  during due diligence on acquired contract portfolios; after substantial redlining or document merging;
  before filing regulatory submissions; or when preparing complex multi-document transaction sets (loan
  facilities with schedules, M&A agreements, franchise disclosure documents, software license suites).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Extracts and audits all defined terms in one or more legal documents — flags unused (orphaned) definitions, terms used but never defined, circular definitions, inconsistent usage, overly broad definitions, precision gaps, shadowed definitions, and conflicting definitions across related documents. Use when conducting pre-execution quality review of any contract, agreement, policy, regulation, or legislation; during due diligence on acquired contract portfolios; after substantial redlining or document merging; before filing regulatory submissions; or when preparing complex multi-document transaction sets (loan facilities with schedules, M&A agreements, franchise disclosure documents, software license suites). Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers. Triggers on: defined term audit, definition check, orphaned definitions, unused definitions, undefined terms, circular definitions, inconsistent definitions, definition section review, definition quality, overly broad definition, multi-document definition conflict, definition register, terms and definitions analysis, glossary audit.


# Legalcode Defined Term Audit

> **Disclaimer**: This skill provides a framework for AI-assisted defined term analysis. It
> does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. The audit may not detect
> every issue in complex, layered documents — human review is required to confirm all
> findings. Statutory and case law references cited from memory carry hallucination risk —
> verify against authoritative sources before relying on them.

---

## Purpose and Scope

This skill performs a **comprehensive defined term audit** on single documents or
multi-document sets. It extracts every defined term, builds a Definition Register, and
systematically audits for eight categories of definition problems — from structural errors
(circular, undefined, orphaned) to quality problems (overly broad, precision gaps) to
multi-document conflicts.

**Covers:**

- Complete extraction of all defined terms (explicit definitions, section-level definitions,
  incorporated definitions, and deemed definitions)
- Eight-category issue classification: ORPHANED / UNDEFINED_USAGE / CIRCULAR /
  INCONSISTENT_USAGE / OVERLY_BROAD / MULTI_DOCUMENT_CONFLICT / PRECISION_GAP / SHADOWED
- CRITICAL / HIGH / MEDIUM / LOW severity classification per finding
- Insertion-ready remediation language for each issue found
- Multi-document conflict analysis with precedence analysis
- Definition architecture recommendations for the definitions section
- Prioritized action plan (Tier 1 blockers / Tier 2 preferred / Tier 3 housekeeping)
- Glass Box audit trail with Definition Register table

**Does not:**

- Provide substantive legal advice on whether underlying commercial terms are fair
- Replace a full contract review — this is a targeted definition-layer analysis
- Guarantee exhaustive detection in heavily formatted, OCR-converted, or fragmented documents
- Evaluate the legal validity of definitions under any specific jurisdiction's law (flags
  jurisdiction-specific risks with [JURISDICTION-SPECIFIC] markers only)

**Relationship to adjacent skills:**

- **legalcode-cross-reference-analyzer**: Covers all cross-reference integrity (section
  references, inter-document chains, date alignment, conflicting provisions). This skill
  is more focused on the quality of the definitions themselves, not just their usage.
- **legalcode-document-qa**: Broad pre-execution QA across 9 dimensions; defined terms
  is one dimension. This skill goes significantly deeper on definition quality.
- **legalcode-proofread**: Proofreading including defined term consistency. This skill
  focuses on definition substance and quality, not just capitalization or formatting.

Use this skill when the **quality and precision of the definitions** is the primary concern.
Use legalcode-cross-reference-analyzer when section references and inter-document chains
are the primary concern.

---

## Jurisdiction and Governing Law

This is a **jurisdiction-agnostic** skill. Definition quality is a structural property of
legal documents independent of governing law. However, certain issue types carry
jurisdiction-specific legal consequences that this skill flags.

[JURISDICTION-SPECIFIC] Where definition issues carry jurisdiction-specific legal risk:

- **Ambiguity resolution**: How the governing jurisdiction's courts resolve ambiguous
  definitions (e.g., contra proferentem, ejusdem generis, contextual interpretation under
  good faith obligations in civil law) [VERIFY]
- **Incorporation by reference**: Whether the jurisdiction requires specific language to
  give legal effect to imported definitions [VERIFY]
- **Consumer contract definitions**: Consumer protection regimes in many jurisdictions
  impose transparency requirements on how key terms are defined in consumer contracts
  (e.g., EU Unfair Contract Terms Directive 93/13/EEC, UK CRA 2015) [VERIFY]
- **Language versions**: In bilingual jurisdictions, definition inconsistencies between
  language versions carry heightened legal risk [VERIFY]
- **Regulatory definitions**: Some jurisdictions mandate specific definitions for regulated
  terms (e.g., "personal data" under GDPR, "consumer" under CCPA, "derivative work" under
  copyright law) — deviating from statutory definitions requires explicit justification [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The scope of the audit would change meaningfully based on user input
- Multiple valid approaches exist and the user's preference affects the output
- Ambiguity in the document structure requires a decision to proceed correctly
- The appropriate depth or strictness of review depends on context

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

### Step 1: Accept Input

Accept the document(s) in any of these formats:

- **File(s)**: PDF, DOCX, TXT, or other document format
- **Pasted text**: Contract or document text pasted directly into the conversation
- **File paths**: Paths to documents in a local repository or file system (use Read and
  Glob tools to retrieve)
- **Multiple documents**: A set of related documents forming a transaction suite

If no document is provided, prompt the user to supply one.

**⟁ CLARIFY** — When multiple documents are provided, confirm the document hierarchy:

- Which document is the master/principal agreement?
- Which are schedules, exhibits, annexes, or side letters?
- Are there any incorporated-by-reference documents (e.g., vendor terms at a URL)?
- Is there an express order of precedence clause? If yes, note it — it governs conflict
  resolution in Step 7.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the audit, ask these context questions. Skip any already
answered:

1. **Purpose**: What is this audit for?
   - Options: Pre-execution review (before signing), Due diligence review (acquiring a
     contract portfolio), Post-redline cleanup (after extensive negotiation), Regulatory
     filing preparation, Quality check before internal approval, Other
   - _Why this matters_: Pre-execution and regulatory filing contexts require Tier 1 issues
     to be resolved before delivery. Due diligence contexts may tolerate more findings.

2. **Scope**: Which issue categories should the audit cover?
   - Options: Full audit (all 8 categories), Definition structure only (ORPHANED /
     UNDEFINED_USAGE / CIRCULAR), Quality issues only (OVERLY_BROAD / PRECISION_GAP),
     Multi-document conflicts only (MULTI_DOCUMENT_CONFLICT), Custom selection
   - Default: Full audit (all 8 categories)
   - _Why this matters_: A focused audit produces faster results; a full audit is more
     comprehensive but takes longer.

3. **Strictness**: How strictly should overly broad and precision gap findings be applied?
   - Options: Conservative (flag only clear problems), Standard (flag probable problems),
     Strict (flag anything potentially imprecise)
   - Default: Standard
   - _Why this matters_: In complex commercial agreements, some definitional breadth is
     intentional. Strict mode produces more findings that may require contextual judgment.

4. **Document type** (if not evident from the document):
   - Options: Commercial agreement, Employment/services contract, Finance/loan document,
     Regulatory submission, Legislation/regulation, Policy document, Other
   - _Why this matters_: Finance documents and legislation have different definition
     conventions than commercial agreements. The audit calibrates accordingly.

If the user provides partial context, proceed with defaults and state assumptions explicitly.

### Step 3: Gather Jurisdiction-Relevant Authority (Optional)

If the governing law clause is present and **legalcode-mcp** is connected:

1. Identify the governing law from the document's governing law clause.
2. Search legalcode-mcp for:
   - Statutory definitions for key regulated terms in the governing jurisdiction (e.g.,
     "personal data," "consumer," "financial instrument," "employee")
   - Judicial interpretation of ambiguous or disputed definitions in this jurisdiction
   - Mandatory definition requirements under applicable sector regulation

3. Save relevant results to `/tmp/legalcode-term-audit-authority.md`.

**If legalcode-mcp is not connected:**

- Proceed without statutory verification
- Mark any jurisdiction-specific regulatory definition notes with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`

### Step 4: Extract All Defined Terms

Systematically extract every defined term from the document(s). Cast a wide net —
definitions appear in multiple forms:

**Explicit definitions (Definition Section)**: Terms collected in a central definitions
section, typically using "means," "shall mean," "has the meaning," or "is defined as."

**Section-level definitions**: Terms defined in the body of the document at the point of
first use: "for purposes of this Section," "as used in this Article," "'Deliverables'
means..."

**Incorporated definitions**: Definitions imported from another document: "as defined in
the Master Agreement," "as defined in Section 2 of Schedule A."

**Deemed definitions**: Definitions by implication or deeming: "the following shall be
deemed Confidential Information," "references to 'Control' shall be construed to mean..."

**Statutory definitions**: Terms whose definition is "as defined under [statute]" — note
these separately, as the statutory definition controls and should be verified.

**Capitalization-implied definitions**: Terms used in capitalized form throughout the
document that lack an explicit definition (these are candidates for UNDEFINED_USAGE).

**For each term, record:**

- Term text (exact wording)
- Definition type (explicit / section-level / incorporated / deemed / statutory)
- Location (section/clause reference)
- Full definition text (or "NONE" if no definition found)
- Every location where the term appears in operative provisions

### Step 5: Build the Definition Register

Compile a Definition Register table. This is the foundational output of the audit and
serves as the working reference for all subsequent analysis.

**Definition Register format:**

```
| # | Term | Defined At | Definition Type | Definition Text (Summary) | Used At | Issue Flags |
|---|------|-----------|-----------------|--------------------------|---------|-------------|
| 1 | [Term] | [§ ref] | Explicit | [summary] | [§ refs or NONE] | [flags or CLEAN] |
```

For large documents (50+ defined terms), group alphabetically and provide a count.

**Preliminary issue flags** (apply during extraction, confirm in Step 6):

- `ORPHANED?` — defined but no uses found
- `UNDEFINED?` — used but no definition found
- `MULTI-DEFINED?` — same term defined in two or more places
- `INCONSISTENT-CAP?` — term appears both capitalized and uncapitalized in operative text

### Step 6: Run the Eight-Category Audit

Apply the full issue catalogue to the Definition Register. For each issue found, record:

- Issue category and code
- Severity (CRITICAL / HIGH / MEDIUM / LOW)
- Exact location(s)
- Explanation of the problem
- Proposed remediation (from the Remediation Templates section)

---

#### Category 1: ORPHANED — Defined But Never Used

**What it is**: A term is defined in the definitions section or elsewhere but appears
nowhere in the operative provisions of the document.

**Detection method**: For each defined term, verify that it appears at least once in a
provision outside the definition itself. Flag any term with zero operative uses.

**Sub-types:**

- `ORPHAN-COPY`: Term was copied from a source contract and is genuinely irrelevant to
  this agreement. Highest risk — may imply unintended scope.
- `ORPHAN-DELETED`: Term was once used but the operative provision was deleted; the
  definition was not cleaned up. Lower risk but creates reader confusion.
- `ORPHAN-RECITAL-ONLY`: Term appears only in recitals/whereas clauses, not in operative
  provisions. Recital-only usage typically has no legal force — assess whether the term
  was intended to be operative.

**Legal risk**: Orphaned definitions can invite arguments that the defined scope was
intended to extend beyond the operative provisions; they clutter the document and increase
reader confusion; in regulated documents, extraneous definitions may trigger regulator
questions.

**Severity default**: HIGH (ORPHAN-COPY), MEDIUM (ORPHAN-DELETED, ORPHAN-RECITAL-ONLY).
Escalate to CRITICAL if an orphaned definition involves a commercially significant term
(e.g., a defined "Excluded Liability" that is never referenced in the liability clause).

---

#### Category 2: UNDEFINED_USAGE — Used But Never Defined

**What it is**: A term appears in operative provisions in a clearly defined-term style
(capitalized, or structurally parallel to other defined terms) but no corresponding
definition exists.

**Detection method**: For each capitalized term in operative provisions, verify a
corresponding definition exists. Flag capitalized terms with no definition.

**Sub-types:**

- `UNDEFINED-EXPLICIT`: The term is clearly intended as a defined term (capitalized,
  parallel structure to other defined terms) but the definition is missing.
- `UNDEFINED-IMPLIED`: The term is not consistently capitalized but is used in a way
  that implies a technical meaning — the document relies on understood meaning that may
  be disputed.
- `UNDEFINED-STATUTORY-ASSUMED`: The term is likely intended to carry its statutory
  meaning but that is not stated, creating risk if the statute is amended.

**Legal risk**: Undefined usage in material operative provisions (payment obligations,
IP ownership, liability clauses, termination triggers) is a Tier 1 pre-execution blocker.
Courts may apply plain meaning, trade usage, or course of dealing to fill the gap —
outcomes vary by jurisdiction and context.

**Severity default**: CRITICAL if the undefined term appears in a payment, liability,
IP ownership, or termination provision. HIGH for other operative provisions. MEDIUM for
recitals, background, or purpose clauses.

---

#### Category 3: CIRCULAR — Term Defined by Reference to Itself

**What it is**: A term is defined in a way that either directly references itself, or
creates a definitional loop through a chain of cross-references (A → B → A, or
A → B → C → A).

**Detection method**:

1. For each definition, check whether the defined term itself appears within the definition
   text (direct circularity).
2. For each definition that references another defined term, follow the chain until either
   an independent definition is reached (no circularity) or the original term is
   encountered again (circular chain).

**Sub-types:**

- `CIRCULAR-DIRECT`: The definition of X uses the word X. Example: defining "Confidential
  Information" as "any information that the parties agree is confidential."
- `CIRCULAR-CHAIN`: A → B → A or A → B → C → A. Example: "Business Day" → "banking day"
  → defined as "a day on which businesses conduct normal Business Day operations."
- `CIRCULAR-TAUTOLOGICAL`: The definition merely restates the term in different words
  without adding content. Example: "Services" means "the services to be provided under
  this Agreement."

**Legal risk**: Circular definitions are unenforceable as definitional guidance — the
term becomes meaningless or subject entirely to court interpretation. In disputes, a
circular definition typically results in the term receiving its plain-language or
contextual meaning, which may not match the drafters' intent.

**Severity default**: CRITICAL for circular definitions on material terms. HIGH for
tautological definitions that will require judicial interpretation.

---

#### Category 4: INCONSISTENT_USAGE — Same Term, Different Meanings

**What it is**: A defined term is used in different sections with materially different
meaning, or the same concept is referred to by different terms in different sections
(synonym drift).

**Detection method**: For each defined term, compare its usage across all operative
provisions against its stated definition. Flag uses that appear to deviate in scope,
meaning, or application. Also flag cases where the same concept is expressed by different
terms in different sections.

**Sub-types:**

- `INCONSISTENT-SCOPE`: Term X is defined broadly but used narrowly in some sections
  (implicitly excluding part of the defined scope) or vice versa.
- `CAPITALIZATION-DRIFT`: The same term is sometimes capitalized (invoking the definition)
  and sometimes not (appearing to invoke plain-language meaning), creating ambiguity about
  which meaning applies.
- `SYNONYM-DRIFT`: The same concept is called "Confidential Information" in Section 3,
  "confidential data" in Section 7, and "proprietary information" in Section 12, suggesting
  either three separate defined terms or inadvertent synonym creation.
- `SCHEDULE-BODY-MISMATCH`: A term is used with one meaning in the body of the agreement
  and a different meaning in a schedule or exhibit.

**Legal risk**: Inconsistent usage creates ambiguity that courts resolve against the
drafter under contra proferentem. In multi-party agreements, inconsistent usage can
create obligations or liabilities the drafter did not intend.

**Severity default**: HIGH for INCONSISTENT-SCOPE and SYNONYM-DRIFT on material terms.
MEDIUM for CAPITALIZATION-DRIFT and SCHEDULE-BODY-MISMATCH on non-material terms.
Escalate to CRITICAL when the inconsistency affects a core obligation (payment, liability,
IP, termination).

---

#### Category 5: OVERLY_BROAD — Definition Exceeds Operational Scope

**What it is**: A definition that captures significantly more subject matter than the
operative provisions actually require, creating unintended obligations, liabilities, or
restrictions.

**Detection method**: Compare the scope of each definition against each operative
provision that uses it. Ask: does the full breadth of the definition apply in every
operative context, or does the definition capture more than needed?

**Sub-types:**

- `OVERINCLUSIVE-SCOPE`: The definition includes categories of subject matter not covered
  by the operative provisions. Example: defining "Intellectual Property" to include trade
  secrets when the agreement only addresses copyright assignments.
- `OPEN-ENDED`: The definition uses "including without limitation" or "any other" language
  that effectively makes it unlimited in scope. While common, these clauses can be
  problematic when the operative provision they feed is not itself limited.
- `AFFILIATE-CREEP`: Definitions of "Affiliate" or similar terms that import obligations
  to, or rights of, entities the parties did not contemplate. Example: an affiliate
  definition that includes entities under common indirect control, making a large
  conglomerate affiliate network party to obligations.
- `RETROACTIVE-SCOPE`: A definition that covers past activities or existing items when
  the parties likely intended only prospective application.

**Legal risk**: Overly broad definitions can significantly expand a party's obligations
or liabilities beyond commercial intent. In liability clauses, an overly broad definition
of "Losses" or "Damages" can defeat the purpose of limitation provisions. In IP provisions,
an overly broad definition of "Work Product" or "Deliverables" can transfer more IP than
intended.

**Severity default**: HIGH for definitions that feed material liability, IP, or payment
provisions. MEDIUM for definitions used in lower-risk contexts.

**⟁ CLARIFY** — When applying the OVERLY_BROAD category, the assessment depends heavily
on the parties' intent and the deal context. Before flagging overly broad definitions in
CRITICAL or HIGH severity, ask:

- "I've found that [Term X] is defined more broadly than it appears to be used in the
  operative provisions. Is the broad definition intentional (providing flexibility for
  future activities) or does it need to be narrowed to match actual scope?"

---

#### Category 6: MULTI_DOCUMENT_CONFLICT — Same Term, Different Definitions Across Documents

**What it is**: The same term is defined differently in two or more related documents
in the transaction suite, and no express order-of-precedence clause or conflict resolution
provision resolves the discrepancy.

**Detection method**: For each term defined in Document A, check whether the same term
is defined in Documents B, C, etc. If yes, compare the definitions. Flag any material
difference.

**Sub-types:**

- `CONFLICT-NO-PRECEDENCE`: Term defined differently, no order of precedence clause.
  The highest severity — no clear resolution mechanism.
- `CONFLICT-AMBIGUOUS-PRECEDENCE`: An order of precedence clause exists but it is
  unclear which document's definition controls for this term (e.g., precedence clause
  covers "operative provisions" but not "definitions").
- `CONFLICT-SCHEDULE-NARROWER`: A schedule or exhibit narrows or qualifies a definition
  from the main agreement. This is sometimes intentional but can create gaps.
- `CONFLICT-VERSION-DRIFT`: Definitions were consistent in earlier drafts but diverged
  during negotiation of one document, with the other document not updated.

**Legal risk**: Multi-document conflicts on material terms require litigation or
renegotiation to resolve. The risk is highest in leveraged finance documents (where
defined terms flow across facility agreements, security documents, and intercreditor
agreements), M&A agreements (where the same term in the SPA, disclosure letter, and
transitional services agreement may carry different meaning), and franchise packages
(where FDD definitions may differ from the franchise agreement).

**Severity default**: CRITICAL for conflicts on material terms (payment, liability, IP,
representations, conditions precedent) without a clear precedence rule. HIGH for
conflicts on secondary terms. MEDIUM for conflicts where an order of precedence clause
likely resolves the issue but ambiguity remains.

---

#### Category 7: PRECISION_GAP — Definition Inadequate for Its Operative Context

**What it is**: A definition exists but is too vague, ambiguous, or incomplete to
meaningfully constrain or guide the operative provision that uses it.

**Detection method**: For each definition, assess whether a reasonable reader — applying
the definition strictly — could determine with confidence whether a specific fact pattern
falls within or outside the defined term. If the answer is "it depends on context" or
"reasonable people could disagree," flag as PRECISION_GAP.

**Sub-types:**

- `VAGUE`: Definition uses subjective or undefined qualifiers ("material," "reasonable,"
  "commercially reasonable," "significant," "substantial") without grounding them in
  objective criteria.
- `INCOMPLETE`: Definition omits categories of subject matter that are clearly relevant
  to the operative provision. Example: "Change of Control" that does not define control
  by percentage threshold or voting rights.
- `AMBIGUOUS-CONNECTOR`: Definition uses "and/or" or lists items without specifying
  whether all must be present or any one suffices — the definition's logical structure
  is unclear.
- `CIRCULAR-QUALIFIER`: Definition uses a qualifier that is itself undefined ("Material
  Adverse Change" defined as "a change that is materially adverse" — the qualifier
  "materially adverse" is not defined).

**Legal risk**: Precision gaps create litigation risk on the terms most likely to be
disputed. A vague "Material Adverse Change" definition has generated substantial
litigation. A vague "Confidential Information" definition may leave trade secrets
unprotected. Precision gaps in "Deliverables" or "Services" create scope disputes.

**Severity default**: HIGH for precision gaps in commercially material terms (MAC, IP
ownership, payment obligations, liability). MEDIUM for precision gaps in lower-risk
contexts.

---

#### Category 8: SHADOWED — Local Definition Overrides Global Without Notice

**What it is**: A section-level or schedule-level definition uses the same term as a
general definitions section but provides a different meaning for that section, without
clearly signaling that the general definition is being overridden.

**Detection method**: For each section-level definition, check whether the same term
is defined in the general definitions section. If yes, verify that the section-level
definition clearly signals the override ("for purposes of this Section only," "as used
in this Article," "notwithstanding the definition in Section 1.1").

**Sub-types:**

- `SHADOW-SILENT`: Section-level definition conflicts with general definition without any
  signaling language. A reader applying the general definition in this section would reach
  the wrong result.
- `SHADOW-PARTIAL`: Section-level definition narrows (but does not fully replace) the
  general definition. Operative in this section, but not clearly flagged — creates
  consistency questions when the provision is read in isolation.
- `SHADOW-AMBIGUOUS`: The relationship between the section-level and general definition
  is genuinely unclear — it is uncertain which controls.

**Legal risk**: Shadowed definitions create a trap for readers and reviewers who assume
the general definition controls everywhere. In disputes, parties may argue for the
definition most favorable to their position, leaving the question for judicial resolution.

**Severity default**: HIGH for SHADOW-SILENT on material terms. MEDIUM for
SHADOW-PARTIAL or SHADOW-AMBIGUOUS.

---

### Step 7: Multi-Document Conflict Analysis

When multiple documents are in scope, perform a cross-document definition comparison
after completing the per-document audit in Step 6.

**⟁ CLARIFY** — Confirm the document precedence structure before analyzing conflicts:

- Is there an express order of precedence clause? If yes, identify its exact scope.
- Does the precedence clause cover definitions specifically, or only operative provisions?
- Are there any definitions that the parties intended to vary by document?

**Conflict analysis process:**

1. **Build the Cross-Document Definition Matrix**: For each term defined in more than one
   document, create a row comparing the full definition text across documents.

2. **Classify each conflict**: Apply the MULTI_DOCUMENT_CONFLICT sub-types from
   Category 6.

3. **Apply the order of precedence** (if one exists): Determine which definition controls
   under the stated priority. Flag if the precedence clause's scope is ambiguous with
   respect to definitions vs. operative provisions.

4. **Flag high-risk conflict zones**: Priority investigation for definitions in these
   areas, which are most frequently disputed in multi-document transactions:
   - Liability caps and definitions of "Losses," "Damages," "Claims"
   - IP ownership and definitions of "Work Product," "Intellectual Property,"
     "Deliverables," "Background IP," "Foreground IP"
   - Termination triggers and definitions of "Material Breach," "Insolvency Event,"
     "Change of Control," "MAC"
   - Payment and definitions of "Fees," "Expenses," "Net Revenue," "Gross Revenue"
   - Data and definitions of "Personal Data," "Confidential Information"
   - Non-compete scope and definitions of "Competing Business," "Territory,"
     "Restricted Period"

5. **Generate conflict resolution analysis**: For each CRITICAL or HIGH conflict, identify
   the preferred approach:
   - **Harmonize**: Adopt one definition across all documents (recommended for most cases)
   - **Differentiate explicitly**: Keep different definitions but add signaling language
     making the variation clear and intentional
   - **Add precedence rule**: If harmonization is not feasible, add an express order of
     precedence clause covering definitions specifically

### Step 8: Classify and Prioritize All Findings

After completing the eight-category audit and multi-document conflict analysis, classify
every finding using the Severity Classification below, then apply the Prioritization
Framework to produce the action plan.

**⟁ CLARIFY** — For borderline severity classifications on commercially significant terms,
ask rather than assume:

- "I've classified [Term X — OVERLY_BROAD] as HIGH severity. Given the deal context, should
  I treat this as CRITICAL (must fix before signing) or is the broad definition intentional?"
- "There are [N] MEDIUM severity findings. Should I include all of them in the report, or
  focus only on Tier 1 and Tier 2 items?"

### Step 9: Generate Remediation Language

For each CRITICAL and HIGH finding, generate insertion-ready remediation language.

**Remediation Format:**

```
**Finding**: [Issue code] — [Term]
**Location**: [Section reference]
**Issue**: [One-sentence description of the problem]
**Severity**: [CRITICAL / HIGH / MEDIUM / LOW]
**Current text**: "[exact definition text or 'NO DEFINITION FOUND']"
**Proposed remediation**: "[insertion-ready replacement language]"
**Rationale**: [Why this change resolves the issue, in 1-2 sentences]
**Alternative approach**: [If the primary remediation requires negotiation, a fallback]
```

For MULTI_DOCUMENT_CONFLICT findings, include:

- Which document's definition to adopt as the harmonized version (with rationale)
- The harmonized definition text
- Any signaling language to add to the other documents

### Step 10: Quality Verification

Before delivering the output, run the Quality Assurance Framework:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every CRITICAL-classified finding, run the 3-pass Self-Interrogation. Revise if
   any pass reveals the classification is incorrect.
3. Assign a Confidence Score to each CRITICAL and HIGH finding.
4. Verify completeness: confirm all 8 issue categories have been checked (each either
   produces findings or is confirmed clean).
5. Cross-check: verify that the Definition Register accounts for every defined term found
   in the document. If the document has obvious definitions not appearing in the register,
   investigate and add them.
6. Verify the multi-document conflict analysis covers all terms shared across documents.
7. Generate the Glass Box Audit Trail and append it to the output.

### Step 11: Deliver Output

Structure the final deliverable per the Output Format Template. Deliver in this order:

1. Executive Summary (issues by severity, document-level health assessment)
2. Definition Register (complete table)
3. Findings by Category (all 8 categories, findings or "CLEAN")
4. Multi-Document Conflict Analysis (if applicable)
5. Prioritized Action Plan (Tier 1 / Tier 2 / Tier 3)
6. Definition Architecture Recommendations (structural improvements)
7. Glass Box Audit Trail

---

## Severity Classification

### CRITICAL — Pre-Execution Blocker

Issues that create genuine legal ambiguity, undermine material rights or obligations,
or could be litigated with unpredictable outcomes. Must be resolved before execution.

**Examples:**

- Undefined term used in a payment obligation, liability clause, or IP ownership provision
- Circular definition on a core commercial term (MAC, Change of Control, Material Breach)
- Multi-document conflict on liability, IP, or termination without a precedence rule
- Orphaned definition that appears to negate an operative provision's intended scope

**Action**: Flag prominently in Executive Summary. Generate remediation language. Do not
recommend execution until resolved.

### HIGH — Pre-Execution Preferred

Issues that materially affect interpretation or rights but are unlikely to create immediate
legal risk. Strongly recommended for resolution before execution.

**Examples:**

- Overly broad definition feeding a liability or IP provision
- Inconsistent capitalization on a commercially significant term
- Precision gap in a "Material Adverse Change" or "Deliverables" definition
- Multi-document conflict on secondary terms without a precedence rule
- Shadowed definition on a material term without signaling language

**Action**: Include in main findings with remediation language. Recommend resolution
before signing.

### MEDIUM — Revision Cycle Housekeeping

Issues that create inconvenience or minor interpretation questions but are unlikely to
be material in practice.

**Examples:**

- Orphaned definition of a term that was once but is no longer used
- Precision gap in a low-risk definitional context (background recitals, boilerplate)
- Synonym drift in non-material sections
- Tautological definition that courts would readily interpret by context

**Action**: Include in findings with brief remediation note. Recommend resolution in
the next revision cycle.

### LOW — Style and Preference

Stylistic issues, cosmetic inconsistencies, or opportunities for definitional improvement
that do not affect legal rights.

**Examples:**

- Excessive definitions for plain-language terms unlikely to be disputed
- Minor formatting inconsistencies in the definitions section
- Definitions that could be more elegantly drafted but are legally adequate

**Action**: Note in an appendix or style comments. Optional to address.

---

## Prioritization Framework

Organize findings and remediation actions by tier:

### Tier 1 — Pre-Execution Blockers (Must Fix Before Signing)

Findings at CRITICAL severity, plus any HIGH findings where the user confirms the
issue must be resolved before execution:

- Undefined terms in payment, liability, IP ownership, or termination provisions
- Circular definitions on core commercial terms
- Multi-document conflicts on material terms with no precedence rule
- Orphaned definitions that directly contradict operative provisions

**Approach**: Generate remediation language. Do not recommend execution until resolved.
Escalate to senior counsel if remediation is contested.

### Tier 2 — Pre-Execution Preferred (Strongly Recommended Before Signing)

Findings at HIGH severity:

- Overly broad definitions affecting significant obligations
- Precision gaps on commercially sensitive terms
- Shadowed definitions on material terms
- Multi-document conflicts on secondary terms
- Inconsistent usage on commercially significant terms

**Approach**: Generate remediation language. Recommend resolution. If counterparty
resists, document the business justification for accepting the risk.

### Tier 3 — Revision Cycle Housekeeping (Address in Next Revision)

Findings at MEDIUM and LOW severity:

- Orphaned definitions (cleanup)
- Minor precision improvements
- Style and formatting issues
- Synonyms in low-risk sections

**Approach**: Note for future revision. No action required before execution.

---

## Definition Architecture Recommendations

After completing the audit, provide structural recommendations for the definitions
section as a whole. Assess:

1. **Central vs. distributed**: Should all definitions be centralized in a single
   definitions section, or are there valid reasons for section-level definitions?
   Recommend centralization for terms used in multiple sections; allow section-level
   definitions only for terms used exclusively within that section.

2. **Alphabetical order**: Definitions should be in alphabetical order for navigability.
   Flag if they are not.

3. **Derived definitions**: Where a definition is derived from or tied to another
   definition, verify the logical dependency is clear (e.g., "Affiliate" should be
   defined before "Affiliated Entity").

4. **Cross-references in definitions**: Definitions that cross-reference other defined
   terms (rather than standing alone) create dependency chains. Flag excessive
   dependency depth (>3 hops to reach an independent definition).

5. **Operative language in definitions**: Definitions should only define — they should
   not impose obligations, grant rights, or create conditions. Flag any definition that
   contains operative language, which should be moved to the appropriate operative clause.

6. **Definition section placement**: For multi-document transaction sets, consider
   whether a master definitions schedule (incorporated by reference into all documents)
   would reduce conflict risk.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                    | Fail Action                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim about a definition's enforceability or effect cites a specific statute, regulation, principle, or marks the claim as general practice | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                                                                             | Fix format                                               |
| **Currency**   | Any referenced statute or regulation is flagged for currency check                                                                                      | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the document's governing law. No assumptions from other jurisdictions leaking in                                                  | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden. If classification of an issue is uncertain, say so                                                           | Add confidence qualifier                                 |

### Self-Interrogation for CRITICAL Findings

For any finding classified as CRITICAL, apply this 3-pass self-interrogation before
delivering:

**Pass 1 — Validity of Classification**: Is this actually CRITICAL, or am I overstating
the risk? Does the missing or flawed definition actually create a material legal risk in
the context of how the term is used operationally? Could a court or practitioner readily
interpret the term by context even without a clean definition?

**Pass 2 — Completeness**: Have I identified all instances where this definition issue
creates risk? Are there operative provisions I missed that use this term? If multi-document,
have I checked all documents in the set?

**Pass 3 — Remediation Quality**: Is my proposed remediation correct, precise, and free
of new issues? Does the proposed definition introduce new ambiguity? Is it consistent
with the rest of the definitions section?

If any pass reveals a weakness, revise before delivery. Mark the audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each CRITICAL and HIGH finding, assign a confidence level:

| Level        | Range     | Meaning                                          | Action                                             |
| ------------ | --------- | ------------------------------------------------ | -------------------------------------------------- |
| **Definite** | 0.95–1.0  | Issue is clear and unambiguous                   | State with confidence                              |
| **High**     | 0.80–0.94 | Issue is present; minor interpretation questions | State with brief caveat                            |
| **Probable** | 0.60–0.79 | Issue is likely but depends on context or intent | State with reasoning and ask for confirmation      |
| **Possible** | 0.40–0.59 | Genuinely uncertain — may be intentional         | Flag for counsel review with both interpretations  |
| **Unlikely** | 0.0–0.39  | Weak basis for the finding                       | Do not assert; flag "[UNCERTAIN — context needed]" |

---

## Glass Box Audit Trail

Every output MUST include a Glass Box audit section at the end.

```yaml
glass_box:
  skill: "legalcode-defined-term-audit"
  document: "[Document title and date, or 'Document suite: [list]']"
  document_type: "[Agreement type]"
  governing_law: "[Jurisdiction identified from governing law clause, or 'Not identified']"
  audit_scope: "[Full 8-category / Partial: [categories]]"
  strictness: "[Conservative / Standard / Strict]"
  total_defined_terms: "[number]"
  terms_clean: "[number]"
  terms_flagged: "[number]"
  findings_by_category:
    orphaned: "[count] — [CLEAN or brief description]"
    undefined_usage: "[count] — [CLEAN or brief description]"
    circular: "[count] — [CLEAN or brief description]"
    inconsistent_usage: "[count] — [CLEAN or brief description]"
    overly_broad: "[count] — [CLEAN or brief description]"
    multi_document_conflict: "[count or N/A] — [CLEAN or brief description]"
    precision_gap: "[count] — [CLEAN or brief description]"
    shadowed: "[count] — [CLEAN or brief description]"
  findings_by_severity:
    critical: "[count]"
    high: "[count]"
    medium: "[count]"
    low: "[count]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, structural issues with the document, or OCR/formatting caveats]"
    - "[Any assumptions made about capitalization conventions or definition intent]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in a defined term audit:

1. **Flagging every orphaned definition as CRITICAL** — Not all orphaned definitions
   carry meaningful risk. An orphaned definition of "Business Day" in a contract with
   no time-sensitive obligations is LOW severity. Calibrate severity to the term's role
   in the commercial deal, not just its structural status.

2. **Assuming capitalization means definition** — In many documents, terms are
   capitalized for emphasis, stylistic convention, or to reference a party name — not
   because they are intended as defined terms. Investigate capitalization patterns before
   declaring a term undefined.

3. **Single-pass extraction** — Extracting terms only from the definitions section and
   missing section-level, incorporated, deemed, and statutory definitions. Run a
   systematic search across all document sections before concluding the register is
   complete.

4. **Ignoring schedules, exhibits, and annexes** — The most significant multi-document
   conflicts often arise in schedules and exhibits, where different counsel drafted
   under different instructions. Never audit a document without its attachments.

5. **Conflating imprecision with invalidity** — An imprecise definition is not the same
   as an unenforceable one. A precision gap warrants remediation language, not a
   declaration that the provision is void. Reserve CRITICAL classification for issues
   that genuinely undermine the document's function.

6. **Missing circular chains** — Direct circularity (A = A) is easy to spot. Chains
   (A → B → C → A) require active chain-following. Do not flag "no circular definitions"
   without tracing multi-hop dependency chains, especially in complex finance documents
   with interdependent defined terms.

7. **Treating all definitional breadth as a problem** — Some overly broad definitions
   are intentional. Counsel deliberately drafts "Intellectual Property" broadly to
   future-proof the clause. Before flagging OVERLY_BROAD at HIGH or CRITICAL, confirm
   the breadth is not intentional by reviewing the operative context and (if possible)
   the deal negotiation history.

8. **Proposing remediation without reading operative context** — A remediation that
   fixes the definition in isolation may break an operative provision. Always verify
   that proposed replacement language works correctly in every operative clause where
   the term is used.

9. **Cross-document analysis without confirming the document set** — If the user provides
   three documents but there are five in the transaction suite, the multi-document
   conflict analysis will be incomplete. Always confirm the complete document set before
   concluding no conflicts exist.

10. **Ignoring the precedence clause** — When an order-of-precedence clause exists,
    many apparent multi-document conflicts are resolved by it. Analyze conflicts in
    light of the precedence clause before classifying them. Only flag as CRITICAL if the
    conflict persists after applying the precedence rule.

11. **Confusing synonym drift with inconsistent usage** — Synonym drift (calling the same
    thing by different names) and inconsistent usage (applying the same defined term
    with different meaning) are different problems requiring different remediation. Synonym
    drift is typically resolved by choosing one term and eliminating the others.
    Inconsistent usage requires clarifying which meaning applies in each context.

12. **Generating remediation for MEDIUM/LOW findings before CRITICAL/HIGH** — Time spent
    polishing style issues before fixing undefined terms in operative provisions is
    time wasted. Always prioritize Tier 1 findings and generate their remediation first.

13. **Declaring the document "clean" based on the definitions section alone** — The
    definitions section may look correct while the body of the document uses terms not
    in the definitions section (because the body was drafted by different counsel or
    merged from another document). Always extract terms from both the definitions section
    and the operative provisions, and reconcile them.

14. **Missing statutory definitions** — When a definition states "as defined under
    [statute]," the applicable meaning is the current statutory text, which may have been
    amended. Flag all statutory definitions for currency verification — a definition that
    was accurate when drafted may be stale if the statute has been amended.

15. **Over-remediating** — Proposing complex replacement definitions when a simple fix
    suffices. A definition with a precision gap often needs only a specific threshold
    or a clarifying parenthetical added. Write the minimum change that resolves the
    issue — do not re-draft the entire definition section.

16. **Applying inconsistent treatment across parties** — Flagging an overly broad
    definition of "Losses" that benefits one party while ignoring an equally broad
    definition that benefits the other party. The audit must be symmetric — flag issues
    regardless of which party benefits from the imprecision.

---

## Writing Standards

Apply plain-language discipline to all remediation language and findings:

**For remediation language** (inserted into the document):

- Definitions should be declarative: "means [X]" or "has the meaning set out in [§]"
- Avoid operating language in definitions — no "shall," "must," or "will"
- Be specific: define by category, threshold, or exhaustive list rather than open-ended
  "including without limitation" language where precision matters
- Parallel structure: if a definition lists multiple items, use consistent grammatical form
- Where a definition refers to another defined term, use the defined term's exact
  capitalization

**For findings** (read by legal professionals):

- Active voice: "Section 3.1 uses 'Permitted Use' without a definition" not
  "A definition for 'Permitted Use' has not been provided"
- Be specific: cite the exact section reference, not "somewhere in the document"
- State the risk concisely: "Creates ambiguity about whether [specific scenario] is
  within the defined scope"
- Avoid hedging language for Definite and High confidence findings — if the finding is
  clear, state it clearly

**Quality gates before delivery:**

1. Is every CRITICAL finding supported by a specific example from the document?
2. Is every proposed remediation tested against the operative provisions that use the term?
3. Is the Definition Register complete — does every term in operative provisions appear
   in it?
4. Are all multi-document conflicts identified, not just the most obvious ones?
5. Is the Executive Summary readable by a business stakeholder without legal training?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 3, search for statutory definitions of regulated terms in the governing
  jurisdiction
- Verify whether any defined terms deviate from mandatory regulatory definitions
- Search for leading cases on interpretation of disputed defined terms in the governing
  jurisdiction
- Mark all legalcode-mcp-sourced references as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory definition notes with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Focus the audit on structural and quality issues rather than regulatory compliance
- Do not create the local authority reference file

---

## Localization Notes

This skill is jurisdiction-agnostic by design. For jurisdiction-specific variants:

**Common Law jurisdictions** (UK, US, Australia, Canada, etc.):

- Contra proferentem applies to ambiguous definitions — this increases the risk of
  precision gaps in the drafter's definitions
- [JURISDICTION-SPECIFIC] Check whether consumer contract transparency rules impose
  additional definition clarity requirements [VERIFY]

**Civil Law jurisdictions** (France, Germany, most of EU, etc.):

- Good faith obligations (BGB §242, Code Civil Art. 1104) inform how ambiguous
  definitions are interpreted — courts may apply a purposive reading
- [JURISDICTION-SPECIFIC] Some civil law jurisdictions impose mandatory definitions for
  regulated terms in specific contract types [VERIFY]

**EU contracts**:

- GDPR imposes mandatory definitions for "personal data," "processing," "data subject,"
  "controller," "processor" — deviating from or narrowing these statutory definitions
  carries regulatory risk [VERIFY current statutory text]
- EU AI Act 2024/1689 imposes defined meanings for "AI system," "high-risk AI," "deployer,"
  "provider" — contracts involving AI should align with or expressly qualify these [VERIFY]

**Finance documents** (loan facilities, derivatives, structured finance):

- ISDA Master Agreement and related schedules have highly developed defined term
  conventions — apply finance-specific precision standards
- LMA/LSTA facility agreement definitions are market standard — deviations should be
  intentional and clearly marked
- [JURISDICTION-SPECIFIC] Banking regulation may impose specific definitions for
  "financial instrument," "eligible counterparty," "professional client" [VERIFY]

**Multi-lingual documents**:

- In bilingual jurisdictions (Canada, Switzerland, Belgium, EU instruments), definition
  inconsistencies between language versions have heightened legal significance
- [JURISDICTION-SPECIFIC] Some jurisdictions hold that one language version controls in
  the event of conflict — verify which [VERIFY]

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Defined Term Audit — [Document Name]

**Document(s)**: [document titles]
**Document type**: [agreement type]
**Governing law**: [jurisdiction or 'Not identified']
**Audit scope**: [Full 8-category / Partial]
**Date of audit**: [date]

---

## Executive Summary

**Overall definition health**: [GREEN — Clean / YELLOW — Issues Found / RED — Critical Issues]

**Total defined terms identified**: [number]
**Terms with no issues**: [number]
**Terms with issues**: [number]

| Severity | Count | Key Terms Affected |
| -------- | ----- | ------------------ |
| CRITICAL | [N]   | [list of terms]    |
| HIGH     | [N]   | [list of terms]    |
| MEDIUM   | [N]   | [list of terms]    |
| LOW      | [N]   | [list of terms]    |

**Key action**: [One-sentence summary of most important action required]

---

## Definition Register

| #   | Term   | Defined At | Type   | Definition Summary | Used At | Issues           |
| --- | ------ | ---------- | ------ | ------------------ | ------- | ---------------- |
| 1   | [Term] | §[ref]     | [type] | [summary]          | §[refs] | [flags or CLEAN] |

[...]

---

## Findings by Category

### Category 1: ORPHANED — [N findings / CLEAN]

[For each finding:]
**Finding DTA-001**

- **Term**: [Term]
- **Location**: [§ ref]
- **Issue**: [Description]
- **Severity**: [CRITICAL / HIGH / MEDIUM / LOW] | Confidence: [level]
- **Current text**: "[definition text]"
- **Proposed remediation**: [Delete this definition / [replacement language]]
- **Rationale**: [Why]

### Category 2: UNDEFINED_USAGE — [N findings / CLEAN]

[...]

### Category 3: CIRCULAR — [N findings / CLEAN]

[...]

### Category 4: INCONSISTENT_USAGE — [N findings / CLEAN]

[...]

### Category 5: OVERLY_BROAD — [N findings / CLEAN]

[...]

### Category 6: MULTI_DOCUMENT_CONFLICT — [N findings / CLEAN / N/A]

[Cross-document definition comparison matrix if applicable]

### Category 7: PRECISION_GAP — [N findings / CLEAN]

[...]

### Category 8: SHADOWED — [N findings / CLEAN]

[...]

---

## Prioritized Action Plan

### Tier 1 — Pre-Execution Blockers (Resolve Before Signing)

| #   | Finding   | Term   | Issue           | Proposed Fix  |
| --- | --------- | ------ | --------------- | ------------- |
| 1   | DTA-[ref] | [Term] | [issue summary] | [fix summary] |

### Tier 2 — Pre-Execution Preferred (Strongly Recommended)

[Same table format]

### Tier 3 — Revision Cycle Housekeeping

[Same table format — can be condensed]

---

## Definition Architecture Recommendations

[Structural improvement recommendations]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis from scratch (Mode A) via
legalcode-skill-enhancement workflow. Research basis: web-backed research covering
defined term auditing best practices (Kenneth Adams Manual of Style for Contract
Drafting, ABA Business Law Section guidance, Weagree 22-rule best practice framework,
Morgan Lewis "Back to Basics" defined terms analysis, Litera Contract Companion automated
flagging methodology, Kira Systems and Luminance contract analytics patterns, Adams on
Contract Drafting circular definitions and orphaned term analysis, Washington State Bar
drafting guidance, process.st contract audit checklist, SpotDraft and Juro contract
audit frameworks). Structural quality frameworks adapted from legalcode-contract-review
gold standard. Eight-category issue architecture (ORPHANED/UNDEFINED_USAGE/CIRCULAR/
INCONSISTENT_USAGE/OVERLY_BROAD/MULTI_DOCUMENT_CONFLICT/PRECISION_GAP/SHADOWED) is a
Legalcode original synthesis. Complements: legalcode-cross-reference-analyzer (broader
cross-reference integrity including section references and inter-document chains),
legalcode-document-qa (9-dimension pre-execution QA audit), legalcode-proofread
(structural proofreading with defined term consistency as one of 9 categories).
