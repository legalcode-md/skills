---
name: legalcode-citation-checker
description: Verify, correct, and audit legal citations across Bluebook (22nd ed.), California Style Manual
  (4th ed.), OSCOLA (5th ed.), and AGLC (4th ed.) — format compliance, current treatment checks, Shepardizing
  flags, pin cite accuracy, and local court rule compliance. Use when proofreading briefs, motions, memoranda,
  law review articles, or any legal document containing case citations, statute citations, regulatory
  citations, or secondary source citations. Covers US federal and state courts, English and Welsh courts,
  and Australian courts. Flags overruled, reversed, distinguished, and criticized cases with VERIFY markers,
  and checks pin cites against cited propositions. Supports both full-document audit mode and targeted
  single-citation lookup mode.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Citation Checker

> **Disclaimer**: This skill provides a framework for AI-assisted citation verification. It
> does not constitute legal advice. All outputs must be reviewed by a qualified legal
> professional before filing or publication. Citation rules change with new style guide
> editions; verify all rules against the current edition of the applicable style guide. AI
> systems carry hallucination risk — any case cited from memory or flagged as overruled must
> be independently verified in Shepard's, KeyCite, or an equivalent live citator before
> relying on the result. This skill does not substitute for a live citator service.

---

## Purpose and Scope

This skill performs systematic citation auditing of legal documents. It identifies format
errors, flags cases with negative treatment, verifies pin cite accuracy, and checks
compliance with local court citation rules.

**Covers:**

- Format compliance: Bluebook (22nd ed.), California Style Manual (4th ed.),
  OSCOLA (5th ed.), AGLC (4th ed.)
- Case citation validation: structure, reporter hierarchy, court parentheticals, year
  placement, and pincite format
- Statute and regulatory citation: federal and state codes, CFR, UK Acts, Australian
  legislation
- Secondary source citation: law review articles, treatises, books, restatements
- Current treatment: Shepard's and KeyCite signal equivalents, overruling risk
- Local court rules: filing prohibitions (unpublished opinions, citation caps, bundle
  requirements)
- Pin cite accuracy: whether the pincite points to the correct page/paragraph for the
  asserted proposition
- Signal usage: whether introductory signals (see, cf., but see, etc.) are used correctly
- Short-form citation: proper use of id., supra, hereinafter, and style-specific short forms

**Does not:**

- Provide substantive legal analysis of the cited cases
- Substitute for running live Shepard's or KeyCite checks in a citator database
- Verify that a cited case actually supports the legal proposition (semantic accuracy) —
  it verifies that the citation is well-formed and that the case has not been overruled
- Draft citations from scratch (use a drafting skill for that)

---

## Jurisdiction and Governing Law

This skill covers citation practice in three primary jurisdictions:

| Jurisdiction                        | Style Guide                                                                      | Primary Use                                            |
| ----------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **United States (federal + state)** | Bluebook 22nd ed. (Bluepages for practitioners)                                  | Federal courts, most state courts, law review articles |
| **California (state courts)**       | California Style Manual 4th ed. (OR Bluebook — Cal. R. Ct. 1.200 permits either) | California state court filings; CSM strongly preferred |
| **England and Wales**               | OSCOLA 5th ed.                                                                   | UK courts, English law review articles                 |
| **Australia**                       | AGLC 4th ed.                                                                     | Australian courts and academic writing                 |

[JURISDICTION-SPECIFIC] When localizing for other jurisdictions, research and apply:

- The local style guide or court-mandated citation format
- Court-specific practice directions on citation format and bundles
- Rules on citing unpublished or unreported decisions
- Mandatory reporter hierarchy for the jurisdiction
- Paragraph- vs. page-based pinpoint citation conventions
- Rules on citing foreign authority (some courts restrict or require notice)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points rather than assuming
intent. Clarification pauses (marked **⟁ CLARIFY**) occur when:

- The applicable style guide is ambiguous or undetermined
- The document will be filed in a court with specific local rules
- The user's goal (full audit vs. quick check vs. format conversion) is unclear
- A citation is ambiguous and could be interpreted as compliant under one reading

If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept the Document

Accept the document in any of these formats:

- **File**: PDF, DOCX, or text — extract all citations for review
- **Pasted text**: Citation list or document section pasted directly into the conversation
- **Single citation**: One citation string for quick format check
- **URL**: Link to a brief, memo, or document in a cloud system

If no document is provided, prompt the user to supply one.

Read the entire document before beginning the citation audit. Citations interact
(e.g., a properly introduced supra form depends on a correct prior full citation), and
context determines whether a short form is appropriate.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask these questions. Present structured options where
possible. Skip any question already answered by the user's prompt:

1. **Document type and purpose?**
   - Options: Court brief/motion (practitioner), Law review article (academic), Legal
     memorandum, Pleading (complaint/answer), Transactional document (opinion letter,
     closing memo), Other
   - _Why this matters_: Bluebook Bluepages (practitioner) differ materially from
     Whitepages (academic). California courts prohibit citing unpublished opinions.
     English courts require compliance with the 2012 Practice Direction.

2. **Which citation style?**
   - Options: Bluebook (22nd ed.) — Bluepages, Bluebook (22nd ed.) — Whitepages,
     California Style Manual (4th ed.), OSCOLA (5th ed.), AGLC (4th ed.),
     Auto-detect from document content, More than one style in the same document
   - _Why this matters_: Format rules differ significantly between styles. A citation
     that is correct Bluebook may be wrong CSM (e.g., year position, spacing rules).

3. **Filing court or publication venue?**
   - Free text. Prompt with examples: SDNY, 9th Circuit, California Court of Appeal
     (2nd District), UK Supreme Court, Federal Court of Australia
   - _Why this matters_: Determines which local court rules apply (unpublished opinion
     bans, authority bundle limits, neutral citation requirements, mandatory reporter
     hierarchy).

4. **Audit scope?**
   - Options: Full citation audit (all citations in document), Format-only check (no
     current-treatment research), Current treatment only (Shepardize equivalents only),
     Single citation lookup, Convert citation style (specify from → to)
   - _Why this matters_: Full audit takes substantially longer. A format-only check is
     faster but will not catch overruled cases. Communicating scope sets expectations.

5. **Filing deadline or urgency?**
   - Options: Imminent (same day / next day), Standard (within the week), Flexible
   - _Why this matters_: Affects depth of research for borderline or unknown cases.

If context is partially provided, state assumptions explicitly and proceed:
"I'm assuming Bluebook Bluepages (practitioner format) since this appears to be a brief —
let me know if that's wrong and I'll re-run the format checks."

### Step 3: Detect Citation Style and Extract Citation Inventory

Scan the entire document and:

1. **Detect the predominant citation style** if not specified by the user. Look for:
   - Year position (after case name → CSM; after reporter + page → Bluebook; after
     neutral citation → OSCOLA; with bracket type → AGLC)
   - Reporter spacing (F. Supp. 2d → Bluebook; F.Supp.2d → CSM)
   - Footnote vs. in-text citations (footnotes → OSCOLA or AGLC; in-text → Bluebook/CSM)
   - Presence of neutral citations ([Year] Court Number → OSCOLA; [Year] Court Number → AGLC)
   - Statute format (Code § → Bluebook; Code, § → CSM; Act Year s → AGLC)

2. **Build a citation inventory** — list every citation in the document with:
   - Citation type (case / statute / regulation / secondary source / constitution)
   - Location in document (section, paragraph, footnote number)
   - Full text of the citation as it appears
   - Detected style

3. **Flag style mixing** — if multiple styles are used in the same document, flag as
   MATERIAL unless the user confirmed multi-style intent (e.g., a document filed under
   Cal. R. Ct. 1.200 using CSM throughout).

**⟁ CLARIFY** — If the auto-detected style is ambiguous or the document mixes styles,
confirm with the user before running the full audit:

- "I detected a mix of Bluebook and CSM formatting. California Rule of Court 1.200
  permits either but requires consistency throughout. Should I (a) check against CSM
  throughout, (b) check against Bluebook throughout, or (c) flag all inconsistencies
  for you to resolve?"

### Step 4: Format Compliance Check

Apply the **Citation Format Rules** reference tables below for the detected style. For
each citation in the inventory, check:

#### Case Citation Checks

| Check                      | Description                                                                                                                     | Applies to    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Case name format**       | Italicization/underlining, correct abbreviation per style guide tables, omission of procedural phrases                          | All           |
| **Reporter citation**      | Correct reporter abbreviation, proper spacing, correct series designation                                                       | All           |
| **Year parenthetical**     | Position (end for Bluebook; after case name for CSM), brackets vs. parens (OSCOLA/AGLC bracket rules)                           | All           |
| **Court parenthetical**    | Present when required; omitted when redundant from reporter                                                                     | Bluebook, CSM |
| **Neutral citation**       | Present and correct for post-2001 UK cases; present and correct for post-~1998 AU cases                                         | OSCOLA, AGLC  |
| **Pin cite present**       | Required for substantive propositions and direct quotations                                                                     | All           |
| **Pin cite format**        | Page number format (Bluebook/CSM: `, 430`; OSCOLA: page or `[para]`; AGLC: comma + page or `[para]`)                            | All           |
| **Reporter hierarchy**     | Most authoritative available report used                                                                                        | OSCOLA, AGLC  |
| **Short form correctness** | Id. only when immediately preceding citation is same; supra only in OSCOLA/AGLC (not Bluebook); hereinafter properly introduced | All           |
| **Signal usage**           | Introductory signals used where required; correct signal selected                                                               | All           |

#### Statute and Regulatory Citation Checks

| Check                           | Description                                                                                                | Applies to    |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------- |
| **Code title and abbreviation** | Correct abbreviation per style guide tables                                                                | All           |
| **Section symbol**              | `§` (Bluebook/AGLC); `, §` with comma (CSM); `s` (OSCOLA/AGLC)                                             | All           |
| **Year of code**                | Required for Bluebook statute citations; year of code not printing date                                    | Bluebook      |
| **Subdivision format**          | `(a)(1)` (Bluebook); `subd. (a)` (CSM)                                                                     | Bluebook, CSM |
| **Act name + year**             | Act name followed by year (OSCOLA: `Human Rights Act 1998 s 4`; AGLC: `Act Year (jurisdiction) s Section`) | OSCOLA, AGLC  |
| **Jurisdiction marker**         | Required for Australian state/territory legislation                                                        | AGLC          |

#### Secondary Source Citation Checks

| Check                             | Description                                                                                                    | Applies to |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------- |
| **Author name format**            | Full name (Bluebook); last name only (CSM for some sources)                                                    | All        |
| **Title formatting**              | Italics for books/cases; roman for article titles (Bluebook); quotation marks for article titles (OSCOLA/AGLC) | All        |
| **Volume/issue/page structure**   | Correct order and punctuation per style guide                                                                  | All        |
| **Date parenthetical**            | Position and format per style guide                                                                            | All        |
| **Pincite for secondary sources** | Required for specific propositions                                                                             | All        |

### Step 5: Current Treatment Check

For every case citation, check for signals of negative treatment. This step is distinct
from format checking — it assesses whether the cited case remains good law.

**Research process:**

1. **Flag for citator verification** — for each case, assess based on:
   - Age of the decision (older cases more likely to have subsequent history)
   - Whether the case addresses a frequently litigated or evolving area of law
   - Whether it is a lower-court decision in a hierarchically settled area
   - Whether the user has mentioned any known negative treatment

2. **Apply Shepard's / KeyCite signal equivalents** — classify each case:

| Signal                              | Meaning                                                              | Action Required                                                                       |
| ----------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 🔴 **RED — Overruled/Reversed**     | Case overruled or reversed on at least one point                     | FATAL — Remove or replace unless relying on an unaffected holding                     |
| 🟠 **ORANGE — Validity Questioned** | Judicial or legislative questioning of the case's validity           | FATAL — Verify specific holding is unaffected before filing                           |
| 🟡 **YELLOW — Negative Treatment**  | Distinguished, criticized, limited, or undermined (not overruled)    | MATERIAL — Read the negative-treatment cases to confirm the cited point is unaffected |
| 🔵 **BLUE — History Available**     | Prior or subsequent history exists; no negative treatment identified | Check — review history for completeness                                               |
| 🟢 **GREEN — Positive Treatment**   | Affirmed, followed, approved                                         | Clean — note for strength of authority                                                |
| ⚪ **UNVERIFIED**                   | No citator data available in this analysis                           | [VERIFY] marker required — must be checked in Shepard's or KeyCite before filing      |

3. **For AI-assisted analysis** — always mark with [VERIFY] and instruct the user to
   run the case through a live citator. AI cannot replace Shepard's or KeyCite, which
   have real-time editorial updates.

4. **Flag Westlaw KeyCite Overruling Risk indicator** — if the user has mentioned or
   provided KeyCite data, note the AI-powered Overruling Risk flag (orange !) which
   indicates a case relies on precedent that has itself been undermined. This requires
   independent lawyer assessment.

**⟁ CLARIFY** — If the document contains a case with an apparent red or orange signal,
ask the user before finalizing the report:

- "I've flagged [case] as potentially overruled/limited. Before I classify this as FATAL,
  can you confirm: (a) whether you have access to Shepard's or KeyCite to verify the
  specific holding, and (b) whether you are relying on this case for the same point that
  received negative treatment?"

### Step 6: Pin Cite Accuracy Check

Pin cites require independent verification — a correct format is worthless if the pin
leads to the wrong page.

For each case cited for a specific proposition:

1. **Verify internal consistency** — the pin cite page or paragraph should be at or after
   the starting page/paragraph. Flag if pin precedes the starting page/paragraph.

2. **Check direct quotations** — if the document quotes a case, the pincite must match
   the quoted language. Flag any quotation without a pincite as MATERIAL.

3. **Check asterisk pagination** — if the citation uses Westlaw `*page` pagination,
   confirm this is appropriate for the filing (some courts require print reporter
   pagination).

4. **Flag missing pincites on substantive propositions** — a case cited for a specific
   legal rule without a pincite should be flagged MATERIAL. A case cited with a "see
   generally" signal does not require a pincite.

5. **Flag footnote pincites** — ensure `n.` prefix (e.g., `430 n.42`) is used where the
   cited proposition appears in a footnote, not on the main page.

**⟁ CLARIFY** — For citations where the pincite cannot be verified from the document
alone, flag for user verification:

- "The pincite `, 431` on [case] cannot be verified from the document. Please confirm
  the proposition you are citing appears on page 431 of the opinion."

### Step 7: Local Court Rules Compliance

Apply jurisdiction-specific rules based on the filing court identified in Step 2.

#### United States

**Unpublished opinion rules (key):**

- **Federal courts**: FRAP Rule 32.1 — all federal circuits must permit citation to
  unpublished federal opinions issued **on or after January 1, 2007**. Pre-2007
  unpublished opinions: check the specific circuit's local rule.
- **Before Rule 32.1 (pre-2007)**: Many circuits prohibit citation of their own
  unpublished opinions. Check specific circuit local rule.
- **California state courts**: Cal. Rule of Court 8.1115 — **unpublished California
  opinions may not be cited or relied upon**. Narrow exceptions apply (same parties;
  final decision in a federal court in a case involving the same parties).

**Other local rules to check:**

- Page/word limits that affect citation density
- Judge-specific AI certification requirements (e.g., N.D. Tex. Judge Starr)
- Requirements to cite the most recent edition of secondary sources
- Requirements to include courtesy copies of cited authorities

#### England and Wales

**Practice Direction: Citation of Authorities (2012)** [2012] 1 WLR 780:

- Neutral citation is **mandatory** for all post-2001 cases
- Must use the **most authoritative available law report** (hierarchy: Law Reports >
  WLR > All ER > specialist series > neutral citation only)
- Cited passages must be marked with a vertical line in the bundle margin
- Bundles must not exceed **10 authorities** without prior permission
- Do not include a case unless you intend to address the court on it
- County court decisions and first-instance decisions generally may not be cited without
  permission in appellate proceedings

**Court of Appeal (CPR Practice Direction 52C):**

- Authorities bundle preparation and marking requirements
- Parties must agree on the authorities bundle where possible
- Each cited passage must be bookmarked and accessible

#### Australia

**High Court of Australia:**

- Cite neutral citation (HCA number) for all post-~1998 decisions
- Must cite the authorised report where available; not just online/unreported version

**Federal Court (FCA/FCAFC):**

- Neutral citations required since ~1999
- Federal Court Rules 2011, Sch 1 — practice notes on authorities

**State courts:**

- Follow AGLC conventions; specific court practice notes may apply
- NSW Supreme Court Equity Division Practice Note SC Eq 1: discourages excessive citation

[JURISDICTION-SPECIFIC] For other Australian states or territories, check the specific
court's practice note or direction on citation format.

### Step 8: Compile Audit Report

Apply the **Citation Issue Classification** framework below. For each issue identified:

1. Classify severity (FATAL / MATERIAL / MINOR)
2. State the specific rule violated
3. Provide the corrected citation
4. Note whether manual verification is still required

Run the **Citation Quality Gates** (see below) before delivering the report.

---

## Citation Format Reference

### Bluebook (22nd Edition, 2025) — Bluepages (Practitioner)

#### Cases

**Full citation structure:**
`*Case Name*, Volume Reporter FirstPage, PinPage (Court Year).`

- Case name: italicize or underline; first listed party each side only; abbreviate per
  Table 6; omit "State of", "City of" (unless alone); do not abbreviate "United States"
  when party; omit "et al."
- Reporter: abbreviate per Table 1; adjacent single capitals close up (F.2d); single
  capital + longer abbreviation has space (F. Supp. 2d)
- Court parenthetical: omit if apparent from reporter (U.S. → SCOTUS; F.4th → circuit
  apparent from reporter); include circuit for F.4th reporters (e.g., `(9th Cir. 2023)`)
- Pin cite: `, 430`; range: `, 442-45` (drop repetitious digits); footnote: `, 430 n.42`
- Unreported: `2010 WL 2947233, at *3 (9th Cir. July 29, 2010)`

**Key 22nd edition changes (2025):**

- New "Contrast" signal (previously "Compare" did double duty)
- AI/LLM citations (Rule 18.3, Whitepages only): requires prompt, service, exact prompt,
  saved PDF on file
- "(citation modified)" replaces "(cleaned up)" per Rule B5.3
- US Supreme Court: single reporter `443 U.S. 307 (1979)` — no triple-reporter required
- Tribal law: new Rule 22

**Short forms:**

- `Id. at 431.` — only when immediately preceding citation is same case
- `431 F.2d at 893.` — volume + reporter + "at" + page

#### Statutes

`Title U.S.C. § Section (Year).`

- Year: year of code edition, not current year
- State statutes: use current official code; consult Table 1 for state abbreviations
- Session laws (uncodified): `Pub. L. No. 116-136, § 2, 134 Stat. 281, 284 (2020)`

#### Regulations

`Title C.F.R. § Section (Year).`
`Named Rule, Title C.F.R. § Section (Year).`

Federal Register (pre-codification):
`Title, Volume Fed. Reg. First page, Pincite (Date) (to be codified at ...)`

#### Signals

| Signal                    | Use                                                               |
| ------------------------- | ----------------------------------------------------------------- |
| [no signal]               | Cited authority directly states the proposition                   |
| _See_                     | Cited authority clearly supports but does not directly state      |
| _See also_                | Additional supporting authority (already cited support exists)    |
| _Cf._                     | Cited authority supports by analogy                               |
| _See, e.g.,_              | One of many supporting authorities                                |
| _E.g.,_                   | Many authorities state the proposition; only citing one           |
| _Accord_                  | Same rule in different jurisdiction or court level                |
| _But see_                 | Contrary authority                                                |
| _But cf._                 | Contrary by analogy                                               |
| _Compare ... with ..._    | Comparison illustrating a rule or point                           |
| _Contrast_ (NEW 22nd ed.) | Comparison illustrating difference (previously part of "Compare") |

---

### California Style Manual (4th Edition)

#### Cases

**Full citation structure:**
`*Case Name* (Year) Volume Reporter FirstPage, PinPage`

- **Year parenthetical immediately follows case name** (not at end)
- No spaces in reporter abbreviations: `Cal.App.4th`, `F.Supp.2d`
- Use official California reporters: Cal., Cal.2d, Cal.3d, Cal.4th;
  Cal.App., Cal.App.2d, Cal.App.3d, Cal.App.4th
- Court of Appeal designation included in parenthetical for Ct. App. cases:
  `(2011) 195 Cal.App.4th 1112, 1119`
- Do NOT cite unpublished California opinions (Cal. R. Ct. 8.1115)

**Short forms:**
`*Case Name*, supra, Volume Reporter at Page`

#### Statutes

`Code, § Section, subd. (subdivision)`

Comma before `§` is required. Subdivision format: `subd. (a)` not `(a)`.

Examples:

- `Gov. Code, § 1, subd. (b)`
- `Cal. Const., art. I, § 1`

---

### OSCOLA (5th Edition)

#### Cases with Neutral Citation (Post-2001 UK Cases)

**Structure:** `*Case name* [Year] Court Number, [Year] Volume Report FirstPage [PinPara].`

Rules:

- Neutral citation always precedes law report citation
- Use most authoritative available law report:
  1. Law Reports (AC, QB, Ch, Fam) — always prefer
  2. Weekly Law Reports (WLR)
  3. All England Law Reports (All ER)
  4. Specialist reports
  5. Neutral citation only if unreported
- **Square brackets [ ]**: year is essential to identify the volume (AC, QB, WLR, All ER)
- **Round brackets ( )**: year is contextual, volume number sufficient
- Pincites: paragraph numbers in square brackets `[42]`, `[45]–[47]`; page numbers unbracketed

**Court abbreviation reference:**

| Abbreviation               | Court                                |
| -------------------------- | ------------------------------------ |
| UKSC                       | UK Supreme Court                     |
| UKHL                       | House of Lords (pre-2009)            |
| EWCA Civ                   | Court of Appeal (Civil Division)     |
| EWCA Crim                  | Court of Appeal (Criminal Division)  |
| EWHC [QB/Ch/Fam/Admin/TCC] | High Court (division in parentheses) |

**Statutes:**
`Human Rights Act 1998 s 4(2)`
Multiple sections: `ss 3–5`

**Secondary sources:**

- Articles: `JAG Griffith, 'The Common Law and the Political Constitution' (2001) 117 LQR 42, 64.`
- Books: `Roger O'Keefe, *International Criminal Law* (3rd edn, OUP 2015) 17.`
- Subsequent references: `*Niemitz* (n 1)` for first footnote cross-reference
- `ibid` for consecutive references to same source

**EU materials:**

- Regulation/Directive: `Council Directive 2008/99/EC ... [2008] OJ L328/28`
- CJEU cases: `Case C-176/03 *Commission v Council* EU:C:2005:542`
- ECtHR: `*Omojudi v UK* (2009) 51 EHRR 10, para 3`

---

### AGLC (4th Edition, 2018)

#### Reported Cases

**Round brackets `( )` = volume-organized reports** (year is context):
`*Harriton v Stephens* (2006) 226 CLR 52, 78.`

**Square brackets `[ ]` = year-organized reports** (year is locator):
`*Bakker v Stewart* [1980] VR 17, 21 (Lush J).`

Key AGLC report abbreviations:

| Abbreviation | Report                                |
| ------------ | ------------------------------------- |
| CLR          | Commonwealth Law Reports (High Court) |
| HCA          | High Court of Australia (neutral)     |
| NSWLR        | NSW Law Reports                       |
| VR           | Victorian Reports                     |
| FCA          | Federal Court of Australia (neutral)  |
| FCAFC        | Full Court of Federal Court (neutral) |

**Page spans**: minimal digits with en-dash: `, 335–8`
**Paragraph pincite**: `[46]`, `[20]–[23]`
**Judicial officer**: `(Lush J)` in round brackets after pincite if clarity requires

#### Unreported Cases (Medium Neutral Citation)

`*Case name* [Year] Court Judgment number [Para].`

Example: `*Kadir v The Queen* [2020] HCA 1, [14].`

#### Legislation

`Act Title Year (Jurisdiction) s Section.`
Example: `Criminal Code Act 1995 (Cth) s 11.1.`

#### Secondary Sources

`Author, 'Title' (Year) Volume *Journal Abbreviation* First page, Pincite.`

Subsequent references: `*Brown* (n 1)`; `ibid [14]`

---

## Citation Issue Classification

Classify every citation issue using this three-tier system:

### FATAL — Must Fix Before Filing

A FATAL issue means the document **cannot be filed as-is** without serious risk of:

- Court rejection or striking of the brief
- Sanctions under FRCP 11, RPC 3.3, or equivalent
- Submission of a fabricated, overruled, or misleading citation
- Violation of a mandatory local rule that may result in adverse consequences

**FATAL issues include:**

- Case does not exist (hallucinated citation)
- Case exists but is overruled or reversed **on the cited holding** (red flag)
- Direct quotation does not appear in the cited source
- Unpublished California opinion cited in California state court (Cal. R. Ct. 8.1115)
- Unpublished federal opinion from a circuit that prohibits citation (pre-FRAP 32.1)
- Statute cited in a version that has since been repealed or materially amended
- Missing citation where an asserted legal proposition has no supporting authority

**Action**: State specific defect, explain the risk (with legal basis where applicable),
and provide the corrected or replacement citation. Do not allow filing without remediation.

---

### MATERIAL — Fix Before Filing (High Priority)

A MATERIAL issue creates significant credibility risk, may cause confusion for the court,
or departs from mandatory style rules in ways that affect meaning or usability.

**MATERIAL issues include:**

- Case received yellow flag (negative treatment) and the negative-treatment case may
  affect the cited holding — must be verified
- Pin cite is absent on a substantive proposition (court cannot locate the cited point)
- Pin cite appears incorrect based on internal consistency check
- Wrong reporter cited when an authoritative reporter (Law Reports, CLR) is available
  and required
- Year in wrong position (CSM vs. Bluebook mismatch causes reader confusion)
- Court parenthetical missing when required for jurisdiction identification
- Style inconsistency throughout document (mixing Bluebook and CSM)
- Signal usage wrong in a way that misrepresents the authority (e.g., no signal when
  the case only tangentially supports the proposition)
- Statute cited in incorrect version (wrong code edition year, wrong section number)

**Action**: State specific rule violated, provide corrected citation, flag for verification.

---

### MINOR — Fix for Best Practice

A MINOR issue is a technical formatting error that does not affect meaning or create
substantive risk, but departs from the applicable style guide.

**MINOR issues include:**

- Reporter abbreviation spacing error (F. Supp. 2d vs. F.Supp.2d — cosmetic difference
  between Bluebook and CSM)
- Pin cite format inconsistency (e.g., using "430–431" instead of "430–31" for page ranges)
- Case name abbreviation inconsistency (abbreviating a word that style guide does not
  require abbreviating, or vice versa)
- Incorrect short-form structure (supra used where style guide uses different short form)
- Missing "n." prefix on footnote pincites
- Inconsistent italicization of case names
- Journal abbreviation not matching style guide tables

**Action**: Provide corrected citation and cite the specific rule.

---

## Prioritization Framework

### Tier 1 — Must Fix Before Filing (FATAL issues)

All FATAL classification issues must be resolved before the document is filed or published.
There is no acceptable fallback for:

- Nonexistent cases
- Overruled cases cited for overruled holdings
- Cal. R. Ct. 8.1115 violations
- Fabricated quotations

**Sequencing**: Resolve FATAL issues first. If a FATAL issue is an overruled case, the
attorney must decide whether to (a) cite the same case for an unaffected holding,
(b) find a replacement case, or (c) abandon the proposition. Do not make this decision
without the attorney.

### Tier 2 — Fix Before Filing (MATERIAL issues)

MATERIAL issues should be resolved before filing unless the deadline makes full correction
impossible. In that case:

- Prioritize pincite-absent substantive propositions and signal misuse
- Flag all uncorrected MATERIAL issues explicitly in the report
- Note that any [VERIFY] markers require a live Shepard's or KeyCite check

### Tier 3 — Best Practice (MINOR issues)

MINOR issues should be corrected to maintain professional quality and credibility. Courts
and senior practitioners notice consistent adherence to citation rules as a proxy for
overall brief quality. However, if time is short, Tier 1 and Tier 2 issues take precedence.

---

## Citation Quality Gates

Run these five gates silently before delivering the audit report. If any gate fails,
revise before delivering.

| Gate            | Rule                                                                                                                    | Fail Action                                                                     |
| --------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Existence**   | Every cited case exists as a real, retrievable decision                                                                 | Mark FATAL if any case cannot be verified; add "[VERIFY — may be AI-generated]" |
| **Treatment**   | Every cited case has been checked for overruling, reversal, and negative treatment                                      | Mark [VERIFY] for any case not independently checked via live citator           |
| **Format**      | All citations follow the applicable style guide rules consistently throughout the document                              | Identify specific rule violated for each deviation                              |
| **Pincite**     | Every substantive proposition and direct quotation has a corresponding pincite                                          | Mark MATERIAL for any missing pincite on a substantive claim                    |
| **Local Rules** | No citation violates a mandatory local court rule (unpublished opinion ban, bundle limit, neutral citation requirement) | Mark FATAL for any local rule violation                                         |

---

## Self-Interrogation for FATAL Citations

For every FATAL classification, apply this 3-pass review before finalizing:

**Pass 1 — Existence Chain**: Does the case actually exist as described? Is the volume,
reporter, and first page plausible? Would a lawyer searching the named reporter volume
find the case at the stated page? If unable to verify existence, note explicitly:
"[CANNOT VERIFY EXISTENCE — run in Westlaw/Lexis before filing]"

**Pass 2 — Treatment Precision**: If the case has received negative treatment (red or
orange flag), is the negative treatment on the _same holding_ the document cites it for?
A case can be reversed on one point while remaining good law on others. Do not classify
as FATAL if the negative treatment clearly does not affect the cited proposition.

**Pass 3 — Local Rule Applicability**: Does the specific local rule actually apply in
this court, at this procedural posture, for this type of authority? Some unpublished
opinion restrictions apply only to state court opinions, not federal opinions.
Some bundle limits apply only at appellate level.

Result marking: if a FATAL classification is revised after self-interrogation, note:
`[Reclassified: FATAL → MATERIAL after Pass 2 — negative treatment does not affect cited holding. Still requires live citator verification.]`

---

## Confidence Scoring

Apply to every current-treatment assessment and format rule determination:

| Level        | Range     | Meaning                                                    | Action                                                       |
| ------------ | --------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled style rule; current edition confirmed              | State with confidence                                        |
| **High**     | 0.80–0.94 | Strong rule basis; minor interpretation questions          | State with brief caveat                                      |
| **Probable** | 0.60–0.79 | Good basis; rule may have changed in current edition       | State with reasoning; flag edition to verify                 |
| **Possible** | 0.40–0.59 | Genuine uncertainty; rule may apply differently in context | Flag for professional verification with both interpretations |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                    | Do not assert; flag "[UNCERTAIN — verify in style guide]"    |

**Never assert that a case is overruled without a [VERIFY] qualifier** — live citator
services have editorial currency that AI analysis cannot match.

---

## Glass Box Audit Trail

Include this block at the end of every citation audit report:

```yaml
glass_box:
  skill_name: "legalcode-citation-checker"
  document: "[Document title and date]"
  document_type: "[Brief / Memo / Article / Pleading / Other]"
  filing_court: "[Court name or 'Not for filing — internal']"
  citation_style: "[Bluebook Bluepages / CSM / OSCOLA / AGLC / Mixed]"
  edition_used: "[Bluebook 22nd ed. / CSM 4th ed. / OSCOLA 5th ed. / AGLC 4th ed.]"
  total_citations_found: "[number]"
  citations_audited: "[number]"
  fatal_issues: "[number] — [brief list]"
  material_issues: "[number] — [brief list]"
  minor_issues: "[number]"
  current_treatment_checked: "[number] / [total] — remainder require live citator"
  legalcode_mcp: "Connected / Not connected"
  live_citator_available: "Yes / No — [all [VERIFY] markers require independent check]"
  pincites_flagged: "[number]"
  local_rules_applied: "[Rule names applied or 'None identified']"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "AI cannot replace live Shepard's or KeyCite — all [VERIFY] markers require independent citator check"
    - "Pin cite accuracy cannot be confirmed without access to the source documents"
    - "[Any other scope limitations or assumptions]"
  reviewer: "AI-assisted — requires attorney verification before filing"
```

---

## Anti-Patterns

What NOT to do when checking citations:

1. **Treating AI-generated "no negative treatment" as citator-equivalent** — AI analysis
   cannot replicate the real-time editorial currency of Shepard's or KeyCite. Always
   require [VERIFY] for current treatment, regardless of AI confidence.

2. **Flagging a case as FATAL solely based on any yellow/orange signal** — A yellow flag
   means "read the negative-treatment cases." It does not mean the case is bad law on the
   cited point. Self-interrogation Pass 2 exists precisely to avoid this over-flagging.

3. **Format-only checking without treatment verification** — A perfectly formatted citation
   to an overruled case is more dangerous than a format error. Treatment check is always
   required unless the user has explicitly scoped it out.

4. **Applying Whitepages rules to practitioner documents** — Bluebook Whitepages (footnote
   format, academic journals) rules differ significantly from Bluepages (in-text, court
   documents). Always confirm practitioner vs. academic context before applying format rules.

5. **Assuming Bluebook applies everywhere in the US** — California Rule of Court 1.200
   permits CSM or Bluebook. California practitioners strongly prefer CSM. A Bluebook-perfect
   citation may still be wrong in a California state court document if it follows
   Bluebook year-parenthetical position (end) rather than CSM (after case name).

6. **Ignoring the reporter hierarchy in OSCOLA and AGLC** — Citing a WLR report when the
   Law Reports version exists (OSCOLA) or citing an online report when an authorised
   report exists (AGLC) is a MATERIAL error in those jurisdictions, not a MINOR one.

7. **Flagging "id." in footnotes as wrong when it is correct** — "Id." is correct in
   OSCOLA and AGLC footnotes for consecutive references to the same source. Do not apply
   Bluebook's "id." rules to OSCOLA or AGLC documents.

8. **Accepting auto-generated Westlaw/LexisNexis citations as correctly formatted** —
   Westlaw and LexisNexis "copy citation" features do not produce Bluebook-compliant
   citations (they often omit court parentheticals, use wrong reporter spacing, or omit
   the code year). Every auto-generated citation must be verified against the style guide.

9. **Applying 21st-edition Bluebook rules to 22nd-edition documents** — The 22nd edition
   (2025) introduced the "Contrast" signal, changed "(cleaned up)" to "(citation modified)",
   and added AI citation rules. Post-2025 documents should follow the 22nd edition.
   Confirm which edition applies before flagging "Contrast" signal usage as wrong.

10. **Missing the unpublished opinion ban in California** — Cal. Rule of Court 8.1115 is
    strict: no unpublished California opinions in California court filings. A single
    unpublished opinion citation is a FATAL error in a California state court document.
    Do not treat this as a MINOR formatting issue.

11. **Reporting pincite errors without providing the correct pincite** — A citation audit
    that flags "pincite appears wrong" without providing the correct alternative leaves
    the attorney with no actionable path forward. Always try to provide the corrected
    form, or clearly mark as "[VERIFY — correct pincite unknown to this analysis]".

12. **Conflating AGLC bracket rules (round vs. square)** — AGLC bracket usage is the
    opposite of what many practitioners expect: round brackets when the volume number
    identifies the case; square brackets when the year identifies the case. Applying this
    backwards is a persistent error. CLR, NSWLR, and most current Australian reporters
    use round brackets. Some older and year-organized state reporters use square.

13. **Skipping the signal check** — Signals are part of the citation, not decoration.
    Using no signal when "see" is required (the case supports but does not directly state),
    or using "see" when a no-signal citation is appropriate (the case directly states the
    proposition), misrepresents the authority to the court. This is a MATERIAL error.

14. **Missing the OSCOLA mandatory neutral citation rule** — For post-2001 UK cases,
    OSCOLA requires the neutral citation to appear first, before any law report citation.
    Omitting the neutral citation is a MATERIAL error in an OSCOLA document, not a MINOR
    formatting issue.

15. **Producing the audit report without running the Citation Quality Gates** — The five
    gates (Existence, Treatment, Format, Pincite, Local Rules) exist to catch systematic
    errors before the user sees them. Skipping the gates and delivering a raw list of
    issues without the systematic check misses the patterns (e.g., all id. citations may
    be broken because the anchor citation was wrong).

16. **Treating a corrected citation format as substantively accurate** — Correcting
    `, at 430` to `, 430` (a MINOR fix) does not mean page 430 is actually the right
    pincite. Format correction and substance verification are separate obligations.

17. **Failing to distinguish between CSM and Bluebook statute formats** — Bluebook uses
    `42 U.S.C. § 1983 (2018)` (no comma before §, year of code at end). CSM uses
    `Gov. Code, § 1, subd. (b)` (comma before §, subdivision in long form). Applying
    one standard to a document drafted under the other produces incorrect corrections.

---

## Writing Standards

When drafting the citation audit report:

**Plain language.** Assume the reader is a lawyer, not a citation specialist. Write issue
descriptions that are immediately actionable, not abstract descriptions of rule violations.

**Active voice.** "The pin cite `, 430` does not match the asserted proposition, which
appears at page 436" not "The page 430 pincite has been observed to be inconsistent with
the proposition's location at page 436."

**Specific.** Always cite the specific style guide rule. "Bluebook B10.1.1 requires the
court parenthetical to be omitted when apparent from the reporter" is more useful than
"the court parenthetical is not required here."

**Corrected form always included.** For every FATAL and MATERIAL issue, provide the
corrected citation immediately following the issue description. For MINOR issues,
provide corrected form unless correction is trivial and self-evident.

**Sequencing.** Lead the report with FATAL issues, then MATERIAL, then MINOR. Within
each tier, order by document sequence (location in the brief).

**Quality gates before delivery:**

1. Is every flagged issue accompanied by a corrected or alternative citation?
2. Is every FATAL classification either verified or marked [VERIFY] with clear instruction?
3. Are [VERIFY] markers explained — what the attorney needs to check and where?
4. Could a junior associate use this report to make all corrections without asking follow-up
   questions? If not, add specificity.
5. Does the Glass Box audit trail reflect the actual scope of work performed?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as a supplemental research tool for
current legal authority and secondary source verification.

**With legalcode-mcp connected:**

- Search for cases flagged for current treatment to confirm existence and basic history
- Retrieve current statute text to verify the cited version is not outdated
- Cross-reference secondary sources (treatises, restatements) to verify edition
  and page numbers
- Mark legalcode-mcp-sourced verifications as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp (standard mode):**

- Proceed with format analysis and structural checks
- Apply [VERIFY] markers to all current-treatment assessments
- Note in Glass Box: `legalcode_mcp: "Not connected — all treatment flags require live citator"`
- Focus the audit on format compliance, signal usage, pincite structure, and local rules

**Recommended citator services for attorney follow-up:**

- **Shepard's Citations** (LexisNexis / Lexis+): Full signal system with editorial review;
  Shepard's Graphical view; jurisdiction-organized results
- **KeyCite** (Westlaw / Westlaw Precision): Red/yellow/striped flags; AI Overruling Risk
  indicator; real-time monitoring alerts
- **Cert Citator** (vLex Fastcase): Expert-edited negative citator; Precedent Map; often
  available through state bar associations
- **Clearbrief** (Word add-in): Hallucination detection; Fact-Cite for claim-to-source
  linking; style conversion (CSM ↔ Bluebook)
- **TypeLaw**: Automated technical citation correction; style conversion; formatting errors

---

## Output Format Template

```markdown
## Citation Audit Report

**Document**: [title and date]
**Filing court**: [court name or "Internal / Not for filing"]
**Citation style**: [Bluebook Bluepages / CSM / OSCOLA / AGLC]
**Edition**: [style guide edition]
**Audit scope**: [Full / Format-only / Treatment-only / Single citation]
**Date of audit**: [date]
**Total citations found**: [number]

---

## Executive Summary

[2-4 sentences: total issues found, breakdown by tier, most critical issues,
and whether any FATAL issues prevent filing as-is.]

---

## FATAL Issues — Must Fix Before Filing

### [Citation number or location] — [Citation as written]

**Issue**: [Specific defect — e.g., "Case does not appear to exist" / "Case overruled on cited holding" / "Unpublished opinion prohibited by Cal. R. Ct. 8.1115"]
**Rule**: [Specific rule — e.g., "Cal. R. Ct. 8.1115" / "FRAP 32.1"]
**Risk**: [Practical consequence of filing with this error]
**Corrected form** (if applicable): `[corrected citation or replacement]`
**Action required**: [Specific instruction to attorney]

[Repeat for each FATAL issue]

---

## MATERIAL Issues — Fix Before Filing

### [Citation number or location] — [Citation as written]

**Issue**: [Specific defect]
**Rule**: [Specific rule]
**Corrected form**: `[corrected citation]`
**Verification needed**: [Yes/No — if yes, what to check and where]

[Repeat for each MATERIAL issue]

---

## MINOR Issues — Best Practice Fixes

| Location   | Citation as Written | Issue   | Corrected Form | Rule       |
| ---------- | ------------------- | ------- | -------------- | ---------- |
| [location] | [citation]          | [issue] | [corrected]    | [rule ref] |

[...]

---

## Current Treatment Summary

| Case                  | Signal                                        | Verified?             | Notes        |
| --------------------- | --------------------------------------------- | --------------------- | ------------ |
| [Case name, citation] | 🟢 GREEN / 🟡 YELLOW / 🔴 RED / ⚪ UNVERIFIED | [Yes / No — [VERIFY]] | [Brief note] |

[...]

**[VERIFY] Instructions**: The following cases require a live Shepard's or KeyCite check
before filing: [list cases]. Log in to [LexisNexis Shepard's / Westlaw KeyCite] and run
each case to confirm current treatment.

---

## Local Court Rules Compliance

[Summary of local rules checked and any violations. "No local rule violations detected"
if clean. FATAL classification for any violations.]

---

## Corrected Citation List

For convenience, below is a corrected version of every citation that had any issue
(FATAL, MATERIAL, or MINOR):

| Original   | Corrected   | Change                        |
| ---------- | ----------- | ----------------------------- |
| [original] | [corrected] | [brief description of change] |

[...]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill covers Bluebook (US), CSM (California), OSCOLA (England and Wales), and AGLC
(Australia). When adapting for other jurisdictions:

**Canada:**

- The Canadian Guide to Uniform Legal Citation (McGill Guide, 9th ed.) is the primary
  academic citation standard
- Court filing format varies by jurisdiction; Ontario and British Columbia have their own
  guidance
- Neutral citations: `2020 SCC 1` (Supreme Court of Canada), `2020 ONCA 1`, etc.
- Statutes: `Copyright Act, RSC 1985, c C-42, s 2` (federal); provincial codes vary

**Ireland:**

- Irish courts follow OSCOLA conventions for UK and EU authorities
- Neutral citations: `[2023] IESC 1` (Supreme Court), `[2023] IECA 1`, `[2023] IEHC 1`

**Scotland:**

- Scottish courts: `2020 SC 1` (Court of Session); `2020 SLT 1` (Scots Law Times)
- OSCOLA applies with Scottish-specific reporter conventions

**New Zealand:**

- New Zealand Law Style Guide (3rd ed., 2018) for academic writing
- Neutral citations: `[2023] NZSC 1`, `[2023] NZCA 1`, `[2023] NZHC 1`

**[JURISDICTION-SPECIFIC]** For any jurisdiction not listed: research the court's current
practice direction on citation format; identify the neutral citation convention (most
common law jurisdictions adopted neutral citations in the late 1990s–2000s); identify the
preferred or mandatory law report series; and identify any rules on citing foreign or
unreported authority.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on deep legal research
across Bluebook 22nd ed. (2025), California Style Manual 4th ed., OSCOLA 5th ed.,
AGLC 4th ed., Shepard's Citations, Westlaw KeyCite, California Rule of Court 1.200 and
8.1115, FRAP Rule 32.1, Practice Direction: Citation of Authorities (2012), and current
AI citation sanction case law (2023–2026). Calibrated against the legalcode-contract-review
gold standard for quality framework coverage. No third-party skills were incorporated.
