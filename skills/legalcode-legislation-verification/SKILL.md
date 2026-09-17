---
name: legalcode-legislation-verification
description: Verify cited statutes, regulations, directives, rules, and public guidance for currency,
  accuracy, and proposition support. Use when a legal document, brief, opinion, contract, or AI-generated
  output contains citations to legislation and you need to confirm that each provision exists, is currently
  in force (or was in force at the relevant date), has been correctly cited, has not been repealed or
  materially amended since citation, applies to the claimed territory, and actually supports the legal
  proposition advanced.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Verify cited statutes, regulations, directives, rules, and public guidance for currency, accuracy, and proposition support. Use when a legal document, brief, opinion, contract, or AI-generated output contains citations to legislation and you need to confirm that each provision exists, is currently in force (or was in force at the relevant date), has been correctly cited, has not been repealed or materially amended since citation, applies to the claimed territory, and actually supports the legal proposition advanced. Covers primary legislation (Acts, codes, statutes), secondary and delegated legislation (Statutory Instruments, regulations, orders, decrees), EU legislation (regulations directly applicable, directives requiring transposition), court procedural rules, and regulatory guidance. Flags hallucinated citations, wrong section numbers, uncommenced provisions, territorial scope mismatches, and guidance-cited-as-legislation errors. Jurisdiction-agnostic: covers UK, EU, US federal, Australia, Canada, Ireland, and Nordic jurisdictions with explicit [JURISDICTION-SPECIFIC] markers. Integrates with legalcode-mcp when connected.


# Legalcode Legislation Verification

> **Disclaimer**: This skill provides a framework for AI-assisted legislation verification.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before relying on them in legal
> proceedings, filings, or opinions. AI systems carry significant hallucination risk when
> generating or verifying legal citations — the 16–17% hallucination rate documented in
> benchmark studies means that every citation must be independently verified against an
> authoritative official source before use. Statutory text changes; regulatory guidance is
> updated without notice; commencement orders may be delayed indefinitely. Verify currency
> before relying on any provision described here.

---

## Purpose and Scope

This skill verifies that cited legislation is accurate, current, in force, correctly
scoped, and supportive of the proposition advanced.

**Covers:**

- Citation format correctness (Acts, SIs, EU instruments, CFR, regulations, orders)
- In-force and commencement verification (Royal Assent vs. commencement date, staged orders)
- Amendment and repeal status (has the provision been amended since cited?)
- Territorial scope (does this provision apply where claimed?)
- Pinpoint accuracy (does the cited section/article/subsection actually say what is claimed?)
- Proposition support (does the cited provision actually support the legal argument?)
- Guidance vs. legislation distinction (is non-binding guidance cited as if binding?)
- Uncommenced provisions (enacted but not yet in force)
- Sunset clauses and temporary legislation (COVID-era measures, emergency powers)
- EU directive transposition status (directive obligations vs. national implementing measures)
- Post-Brexit REUL/assimilated law status (UK)
- International treaty applicability and ratification status

**Does not:**

- Provide substantive legal analysis or advice on the underlying legal question
- Substitute for running live citator checks (Westlaw KeyCite, LexisNexis Shepard's, vLex)
- Verify the content of case law citations (see `legalcode-citation-checker`)
- Draft legislation or regulatory submissions
- Assess the policy merits of a legislative provision

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. It adapts its verification methodology based on the
jurisdiction(s) identified in the source document. The analysis identifies the governing
jurisdiction and applies the appropriate authoritative sources and citation conventions.

[JURISDICTION-SPECIFIC] When localizing or expanding coverage, apply:

- The correct authoritative official database for that jurisdiction's legislation
- The correct citation format conventions (OSCOLA, Bluebook, Australian Guide to Legal
  Citation, etc.)
- Jurisdiction-specific commencement and amendment mechanics
- Devolved or sub-national scope distinctions (England & Wales vs. Scotland, federal
  vs. state/province, EU regulation vs. directive)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction of the verification
- The jurisdiction or temporal scope of the verification is ambiguous
- The purpose of the document affects how verification should be framed
- The user wants a subset of checks rather than a full verification pass

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

## Authoritative Source Map

Map citations to the official authoritative database for their jurisdiction before verifying.
Do not use secondary or aggregator sources as the primary verification target.

| Jurisdiction         | Primary Legislation                                  | Secondary Legislation                               | Case Law                                              | Notes                                                   |
| -------------------- | ---------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------- |
| **UK**               | legislation.gov.uk                                   | legislation.gov.uk (SIs)                            | BAILII; National Archives Find Case Law               | Point-in-time feature for historical versions           |
| **EU**               | EUR-Lex (OJ L/C series)                              | EUR-Lex (Implementing/Delegated Acts)               | CJEU via EUR-Lex or CVRIA                             | CELEX number is the canonical identifier                |
| **US Federal**       | govinfo.gov; congress.gov                            | eCFR (editorial only — verify against official CFR) | US federal courts via govinfo.gov                     | eCFR is NOT official — cross-check with printed CFR     |
| **Australia**        | Federal Register of Legislation (legislation.gov.au) | legislation.gov.au                                  | AustLII                                               | State/Territory legislation on respective state portals |
| **Canada**           | laws-lois.justice.gc.ca (official since June 2009)   | laws-lois.justice.gc.ca                             | CanLII                                                | Provinces: e-Laws (ON), QC Légis Québec, etc.           |
| **Ireland**          | Irish Statute Book (irishstatutebook.ie)             | irishstatutebook.ie (SIs)                           | BAILII; courts.ie                                     | Pre-1922 Acts on irishstatutebook.ie (selected)         |
| **Nordic — Denmark** | Retsinformation.dk                                   | Retsinformation.dk                                  | N/A (no free national database)                       | Operated by Danish Ministry of Justice                  |
| **Nordic — Finland** | Finlex.fi                                            | Finlex.fi                                           | KKO/KHO decisions via finlex.fi                       | Official since January 2011                             |
| **Nordic — Norway**  | Lovdata.no (free tier)                               | Lovdata.no                                          | Lovdata (Supreme/High Court; district court selected) | Lovdata Pro for full coverage                           |
| **Nordic — Sweden**  | Riksdagen.se                                         | Riksdagen.se; sfs.riksdagen.se                      | JUNO; Infotorg (subscription)                         | Free SFS (Statens Författningssamling) on riksdagen.se  |
| **EEA/EFTA**         | EEA-Lex                                              | EEA-Lex                                             | EFTA Court via efta.int                               | Check Joint Committee Decisions for EEA incorporation   |

### NOT Authoritative for Legal Citations

| Source                                    | Permissible Use                   | Prohibited Use                                   |
| ----------------------------------------- | --------------------------------- | ------------------------------------------------ |
| Wikipedia                                 | Background context, overview      | Any citation or compliance claim                 |
| Law firm blogs / alerts                   | Understanding issues              | Authoritative statements, compliance conclusions |
| GitHub legal-tech repositories            | Code architecture patterns        | Legal data, citation verification                |
| News articles                             | Current events background         | Legal interpretation                             |
| Third-party summaries (LexBlog, etc.)     | Overview                          | Compliance decisions                             |
| AI-generated text (including this output) | Structured verification framework | Substitute for live database check               |

---

## Workflow

### Step 1: Accept Input

Accept the input in any of these formats:

- **Document**: A legal document, contract, brief, memo, or AI-generated output containing
  legislative citations to verify
- **Citation list**: One or more citation strings pasted directly
- **Proposition + citation**: A legal claim with the cited provision supporting it
- **Single provision**: A specific Act, SI, regulation, directive, or code section to verify

If no material is provided, prompt the user to supply citations for verification.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning verification, ask the user:

1. **What is the purpose of this document?**
   - Options: Court filing / regulatory submission, Client advice / legal opinion, Contract
     or transactional document, Internal research note, AI-generated output requiring
     QA verification, Other
   - _Why this matters_: Court filings carry professional responsibility obligations for
     citation accuracy; AI-generated output requires especially rigorous verification given
     the 16–17% benchmark hallucination rate for legal citations.

2. **What jurisdiction(s) does the document cover?**
   - Options: UK (specify: E&W / Scotland / NI / UK-wide), EU (specify member state if
     transposition matters), US federal, specific US state, Australia, Canada, Ireland,
     Nordic (specify country), Multiple jurisdictions (list), Unknown — infer from document
   - _Why this matters_: Determines which authoritative sources to use and which
     citation format conventions apply.

3. **What is the relevant temporal reference date?**
   - Options: Current (today's date), Specific past date (user to specify), Date of
     document signing / execution, Date of relevant transaction or event
   - _Why this matters_: Legislation changes. A provision in force today may not have
     been in force at the date of the transaction, or vice versa.

4. **What checks should be run?**
   - Options: Full verification (all 7 checks), Format and currency only (quick scan),
     In-force and repeal only, Proposition support only (does the cited text actually say
     this?), Custom (user specifies)
   - _Why this matters_: A full verification pass is comprehensive but time-consuming for
     large documents; targeted checks suit specific QA needs.

5. **Are any citations flagged as potentially problematic?**
   - Free text. Allow user to highlight specific provisions of concern.
   - _Why this matters_: High-risk citations (AI-generated, from memory, unusual
     jurisdictions) warrant deeper verification.

If the user provides partial context, proceed with what you have and state assumptions
explicitly. For batch/automated runs, default to: full verification, current date,
jurisdiction inferred from document text.

### Step 3: Parse and Classify Citations

Extract all legislative citations from the input material. For each citation:

1. **Identify the instrument type** from the classification table below
2. **Extract the citation components** (see Verification Anatomy by Instrument Type)
3. **Assign a preliminary jurisdiction** based on the citation form
4. **Flag anomalies** immediately visible without database lookup (e.g., a year that seems
   inconsistent with the instrument, an obviously malformed SI number, a directive
   reference applied to a pre-EU member state date)

**⟁ CLARIFY** — If a citation is ambiguous or multi-jurisdictional, ask before proceeding:

- "Citation 'Data Protection Act 2018' — should I verify this as UK law, Irish law (where a
  different Act of similar name exists), or both?"
- "The document references 'Regulation 2016/679' without specifying EU or UK. Should I
  verify against the EU GDPR, the UK GDPR, or both?"

### Step 4: Map to Authoritative Sources

For each citation, identify the authoritative database for verification using the
Authoritative Source Map above. Note:

- Whether the required database is accessible via legalcode-mcp or requires manual lookup
- Whether a point-in-time version is needed (historical date) vs. current version
- Whether you are checking primary legislation, secondary legislation, or guidance

**With legalcode-mcp connected (preferred):**
Use legalcode-mcp to retrieve the provision text and status directly. Save the most
relevant results to a local temporary reference file at
`/tmp/legalcode-legislation-verification-[document-id].md` structured as:

```markdown
# Legislation Verification Reference — [Document Title or ID]

## Date: [date]

## Temporal Reference: [current / [specific date]]

### Citations Verified via legalcode-mcp

| Citation   | Status                                      | Notes      |
| ---------- | ------------------------------------------- | ---------- |
| [citation] | [CURRENT / AMENDED / REPEALED / UNVERIFIED] | [findings] |
```

**Without legalcode-mcp:**
Proceed with training-data-based verification only. Mark every statutory provision with
[VERIFY AGAINST AUTHORITATIVE SOURCE] and note in the Glass Box audit trail:
`legalcode_mcp: "Not connected — all citations require manual database verification"`

### Step 5: Apply the 7-Check Verification Protocol

For each citation, run the full verification protocol. Each check produces a status:
`PASS` / `FAIL` / `CAUTION` / `UNVERIFIABLE`. Aggregate these into the overall citation
status (see Status Classification below).

---

#### Check 1: Source Authority

**Purpose**: Is the citation to an authoritative official source, or is it based on a
secondary source, aggregator, or AI output?

**Procedure**:

- Identify whether the citation can be traced to one of the authoritative databases in
  the Source Map
- If the citation was sourced from a third-party summary, law firm alert, or AI-generated
  text, flag it for independent primary-source verification
- Note any citations that cannot be traced to a clearly authoritative source

**Pass criterion**: The provision is verifiable against an authoritative official database.
**Fail criterion**: The provision cannot be traced to any authoritative source.
**CAUTION**: The provision may exist but can only be verified via a subscription database
(Westlaw, LexisNexis, vLex) that is not currently accessible.

---

#### Check 2: Citation Format

**Purpose**: Is the citation correctly formatted for the jurisdiction and instrument type?

Verify each citation against the format table in **Verification Anatomy by Instrument Type**
below. Common format errors include:

- Wrong year (Royal Assent year vs. year commonly known by)
- Transposed or incorrect SI/regulation number
- Missing chapter number for UK Acts
- Incorrect section/subsection notation (e.g., "s.15(1)(b)" vs. "Section 15 subsection 1
  paragraph b")
- CELEX number errors (EU legislation)
- Missing "as amended" notation for consolidated texts

**Pass criterion**: Citation follows the correct format for the jurisdiction.
**Fail criterion**: Citation has a format error that would prevent accurate identification.
**CAUTION**: Minor format deviation that does not impede identification (abbreviation style,
spacing), but should be corrected for professional documents.

---

#### Check 3: In-Force and Commencement Status

**Purpose**: Is the cited provision currently in force at the temporal reference date? Was
it in force at the date of the transaction or event?

**This is one of the most common failure modes.** Acts may receive Royal Assent in one year
but not commence until a later date — or may never commence at all. Staged commencement
orders mean that different sections of the same Act may come into force on different dates.

**Procedure**:

1. Identify whether the provision has a commencement section or whether it comes into force
   on Royal Assent
2. Check whether a commencement order has been made for the provision
3. For staged commencement: verify the specific provision (not just the Act as a whole)
4. Check for sunset clauses and expiry dates
5. For temporary legislation (emergency measures, pandemic provisions): verify whether the
   provision is still in force or has expired
6. For the relevant temporal date: verify in-force status at that specific date

[JURISDICTION-SPECIFIC] Commencement mechanics:

- **UK**: Commencement orders are SIs made under the relevant Act. Most Acts nominate a
  commencement date by SI. Without a commencement order, the Act generally comes into force
  on Royal Assent (Interpretation Act 1978). Check legislation.gov.uk commencement notes.
- **EU Regulations**: Enter into force 20 days after publication in the Official Journal
  (unless a different date is specified). No transposition required. Apply in all
  member states directly.
- **EU Directives**: Have a transposition deadline (typically 2 years). Must be implemented
  by member state legislation by that deadline. The directive itself is not directly
  applicable (except for direct effect in vertical relationships after the deadline).
- **US Federal**: Federal statutes typically specify an effective date or come into force on
  enactment. Regulations (CFR) take effect as specified in the Federal Register notice.
- **Australia**: Commonwealth Acts generally come into force on Royal Assent unless
  specified otherwise. Check commencement table at legislation.gov.au.
- **Nordic**: Check country-specific legislation portals for commencement annotations.

**Pass criterion**: Provision is confirmed in force at the temporal reference date.
**Fail criterion**: Provision is not in force at the temporal reference date (not yet
commenced, expired, or otherwise not operative).
**CAUTION**: Provision is in force but has been amended since the cited version; or
commencement status cannot be confirmed without live database access.

---

#### Check 4: Amendment and Repeal Status

**Purpose**: Has the cited provision been repealed, revoked, or materially amended since
it was originally enacted (or since the temporal reference date)?

**This is a critical check.** Provisions that are "in force" may have been substantially
amended. A citation to the original text of an amended provision misrepresents the current
law.

**Procedure**:

1. Check whether the provision has been amended since enactment
2. If amended: identify what changed and whether the amendment is material to the proposition
3. Check whether the provision has been repealed or revoked in its entirety
4. For UK legislation: check legislation.gov.uk "revised" version vs. "as enacted" version
5. For EU legislation: check EUR-Lex consolidated text (note: consolidated texts are not
   official; the OJ is the authoritative source)
6. For repealed provisions: note what superseded them

[JURISDICTION-SPECIFIC] Amendment tracking:

- **UK REUL/Assimilated Law**: Post-Brexit, retained EU law has been reclassified as
  "assimilated law" as of 1 January 2024. Some REUL was revoked by the Retained EU Law
  (Revocation and Reform) Act 2023. Check the Retained EU Law Dashboard. EU interpretation
  principles no longer apply to assimilated law after 1 January 2024.
- **EU**: EUR-Lex provides consolidated texts. The CELEX number for the consolidated version
  differs from the original instrument. Cross-reference the OJ to verify the authentic text.
- **US CFR**: eCFR is updated daily but is an editorial compilation. Cross-check with the
  official Federal Register and List of CFR Sections Affected (LSA) for recent changes.

**Pass criterion**: Provision is current and has not been materially amended or repealed.
**Fail criterion**: Provision has been repealed, or has been materially amended such that
the cited version no longer reflects the current law.
**CAUTION**: Provision has been amended but the amendment is not material to the cited
proposition; or amendment status cannot be confirmed without live database access.

---

#### Check 5: Territorial Scope

**Purpose**: Does the cited provision apply to the jurisdiction being claimed?

Territorial scope errors are common in multi-jurisdictional documents and AI-generated text.

**Procedure**:

1. Identify the territorial extent of the cited provision
2. Confirm that the claimed jurisdiction falls within that territorial extent
3. For devolved matters (UK): distinguish England & Wales, Scotland, Northern Ireland,
   UK-wide
4. For federal systems: distinguish federal vs. state/provincial law
5. For EU: distinguish EU regulations (apply in all member states) from directives (require
   transposition; check whether the specific member state has transposed)
6. For international conventions: check which jurisdictions have ratified and whether any
   reservations apply

[JURISDICTION-SPECIFIC] Territorial scope complexity:

- **UK Devolution**: Asymmetric devolution means that the same policy area may be devolved
  in Scotland, partially devolved in Wales, and reserved in Northern Ireland, or vice versa.
  Legislation.gov.uk records the extent of each provision.
- **EU Directives**: Even after the transposition deadline, check whether the specific
  member state has actually transposed (Commission infringement proceedings are common for
  late/incorrect transposition). EUR-Lex "National Transposition" collection identifies
  implementing measures per member state.
- **EEA**: EU acts incorporated into the EEA Agreement via Joint Committee Decision apply
  in Iceland, Liechtenstein, and Norway, often with adaptations. Check EEA-Lex. Note:
  the Common Agricultural Policy and Common Fisheries Policy do NOT apply to EEA EFTA states.
- **US Federal vs. State**: Federal minimum standards vs. state law (states may set higher
  standards). Verify whether the document intends to cite federal or state law.

**Pass criterion**: Provision applies to the jurisdiction where it is cited.
**Fail criterion**: Provision does not apply to the claimed jurisdiction.
**CAUTION**: Provision's territorial scope is unclear or conditional on additional
implementation steps not yet taken.

---

#### Check 6: Pinpoint Accuracy

**Purpose**: Does the cited section, subsection, article, paragraph, or regulation actually
contain the text or rule claimed?

Pinpoint errors are a classic AI hallucination failure mode and occur frequently in
manually assembled documents. Common errors:

- Off-by-one section numbers (citing s.15 when the relevant text is in s.16)
- Wrong subsection (citing s.15(1) when the specific rule is in s.15(2))
- Citing a general section when a specific carve-out governs
- Citing the definition subsection for a substantive obligation (or vice versa)
- Citing a transitional provision as the substantive rule
- Citing an SI that amends another SI and mistaking the amended section for the original

**Procedure**:

1. Retrieve the text of the cited provision (via legalcode-mcp or authoritative database)
2. Confirm that the cited section/subsection/paragraph actually contains the claimed content
3. If it does not, search for the correct pinpoint
4. Note whether the provision says exactly what the document claims, or whether there are
   material qualifications or carve-outs that the citation omits

**Pass criterion**: The cited pinpoint contains the text or rule claimed, including any
material qualifications.
**Fail criterion**: The cited pinpoint does not contain the claimed text; or the text is
present but material qualifications are omitted that change the meaning.
**UNVERIFIABLE**: Cannot confirm pinpoint accuracy without live database access.

**⟁ CLARIFY** — For propositions that paraphrase rather than quote a provision directly,
ask: "This citation supports the claim '[claim]' — shall I verify whether the cited
provision supports this paraphrase, or only whether the citation format and currency are
correct?"

---

#### Check 7: Proposition Support

**Purpose**: Does the cited provision actually support the legal proposition being advanced,
or is it cited for a broader or different proposition than it establishes?

This is the most legally substantive check and requires understanding the claimed proposition
and the actual text of the provision.

Common proposition support failures:

- Citing a statute that creates a right but omitting the statutory qualifications that limit it
- Citing a regulatory provision that is permissive ("may") and asserting it is mandatory
- Citing case law (via a statutory provision that codifies it) incorrectly
- Citing a provision that has been interpreted narrowly by courts, when the citation implies
  broader application
- Citing a repealed provision that was superseded by a narrower or different rule

**Procedure**:

1. Identify the legal proposition being advanced
2. Retrieve the text of the cited provision
3. Assess whether the provision, on its terms, supports the proposition
4. Note any statutory qualifications, exceptions, or definitional constraints that affect
   scope
5. Assign a confidence score to the proposition support assessment

**Pass criterion**: The cited provision, on its terms, supports the proposition as stated.
**Fail criterion**: The cited provision does not support the proposition as stated, or the
proposition overstates or misstates what the provision establishes.
**CAUTION**: The provision supports the proposition but there are material qualifications
that are omitted from the citation context.

---

### Step 6: Guidance vs. Legislation Distinction

Separately from the 7-check protocol, identify any instances where regulatory guidance is
cited as if it were binding legislation.

**Guidance is not legislation.** Regulatory guidance (codes of practice, circulars,
practice directions from non-statutory bodies, agency FAQ documents) does not have the
force of law unless specifically given binding status by statute.

For each item of guidance cited:

1. Identify whether it is guidance or legislation
2. If guidance: assess whether it has statutory backing that makes it quasi-binding (e.g.,
   a code of practice that a court or tribunal must "have regard to")
3. Flag any guidance cited as if it were binding legislation

[JURISDICTION-SPECIFIC] Guidance status:

- **UK codes of practice**: Many have a statutory "have regard to" duty (e.g., ACAS codes,
  ICO codes). Failure to follow is not automatically unlawful but is relevant evidence.
- **US agency guidance**: Federal agencies cannot impose legally binding requirements
  through guidance documents alone. However, guidance may indicate how an agency will
  exercise enforcement discretion.
- **EU soft law**: European Commission guidelines, notices, and recommendations are not
  legally binding but are widely followed and can be admitted as evidence of Commission
  interpretation.

### Step 7: Flag Hallucination Risk Items

Apply heightened scrutiny to any citation that exhibits one or more hallucination risk
indicators:

| Risk Indicator                            | Description                                                                     | Action                                                                    |
| ----------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| AI-generated source                       | Document or citation was produced by an AI tool                                 | Verify against primary source before any reliance                         |
| Very specific pinpoint                    | Exact subsection/paragraph citations are common hallucination sites             | Verify the specific paragraph exists and says what is claimed             |
| Obscure or short-lived provision          | Lesser-known Acts, temporary measures, transitional rules                       | Verify existence and status                                               |
| Jurisdiction mismatch                     | Statute name sounds like it applies universally but may not                     | Verify territorial extent                                                 |
| Round-number sections                     | Citations to s.1, s.100 etc. are statistically more common in hallucinated text | Verify text of provision                                                  |
| Plausible but unverifiable                | Citation sounds correct but cannot be found in authoritative sources            | Mark UNVERIFIABLE; treat as potentially fabricated                        |
| Inconsistent year                         | Year in the citation is inconsistent with the legal context                     | Verify year and whether this is a Royal Assent vs. commencement confusion |
| "As amended" without specifying amendment | Implies awareness of amendment without citing it                                | Identify the specific amending instrument                                 |

### Step 8: Classify Each Citation

Assign an overall status to each citation based on the 7-check protocol results:

(See **Status Classification** section below for the full classification system.)

For each SUPERSEDED or INCORRECT citation, generate a specific corrective action using
the format in **Actionable Output per Finding** below.

### Step 9: Quality Verification

Before delivering the verification report:

1. Run the 5 Legislation Citation Quality Gates (see Quality Assurance Framework)
2. For any INCORRECT classification, run the 2-pass Self-Interrogation
3. Assign a Confidence Score to each material verification finding
4. Compile the Glass Box Audit Trail

### Step 10: Output

Deliver the verification report using the Output Format Template below.

---

## Verification Anatomy by Instrument Type

### Primary Legislation

#### UK Acts of Parliament

```
[Short Title] [Year], s.[section]([subsection])([paragraph])
Example: Equality Act 2010, s.26(1)(b)

Components to verify:
- Short title (verify against legislation.gov.uk)
- Year (Royal Assent year — note: NOT the year it came into force)
- Chapter number (optional for citation but useful for disambiguation)
- Section number (verify against authoritative text)
- Subsection/paragraph (verify against authoritative text)
- Whether the provision is in the revised (consolidated) or "as enacted" version
```

**Chapter format** (when used): `[Short Title] [Year] (c.[chapter number])`

**⟁ CLARIFY** if the Royal Assent year and the year the Act is commonly known by differ
(e.g., an Act that received Royal Assent in December 2020 may be commonly cited by its
subject-matter year if it did not commence until 2021).

#### US Federal Statutes

```
[Title] U.S.C. § [section]([subsection])
Example: 42 U.S.C. § 1983

OR citation by Public Law:
Pub. L. [Congress]-[number], [year] Stat. [page number]
Example: Pub. L. 111-274, 124 Stat. 2861

Components to verify:
- Title number in the US Code
- Section number
- Current codification (law may be codified differently from citation)
- Whether the provision has been amended since original enactment
```

#### EU Primary Legislation (Treaties)

```
Treaty on the Functioning of the European Union (TFEU), Art. [number]
Treaty on European Union (TEU), Art. [number]

Components to verify:
- Correct treaty name (TFEU vs. TEU; consolidated version year)
- Article number (renumbered by Lisbon Treaty 2007)
```

### Secondary and Delegated Legislation

#### UK Statutory Instruments

```
The [Name] [Type] [Year] (SI [Year]/[Number]), [reg./art./sch.] [number]
Example: The Working Time Regulations 1998 (SI 1998/1833), reg. 4(1)

Components to verify:
- Full name of the SI (not abbreviated)
- SI year and number (format: SI YYYY/NNNN)
- Regulation/article/rule/schedule number and paragraph
- Whether the SI is in force (check for revocation SIs)
- Whether the provision has been amended by a subsequent amending SI
```

**⟁ CLARIFY** if the SI number cannot be confirmed — it may be cited from memory and
the number is a common hallucination point.

#### EU Regulations (Directly Applicable)

```
Regulation (EU) [Year]/[Number] of the European Parliament and of the Council
  of [date] on [subject], Art. [number]
Short form: EU Regulation [Year]/[Number], Art. [number]

CELEX number format: 3[Year]R[4-digit-number]
Example: GDPR = Regulation (EU) 2016/679, CELEX 32016R0679

Components to verify:
- Year and number (format: YYYY/NNN)
- Date of entry into force (20 days after OJ publication unless stated)
- Date of application (regulations can have deferred application dates)
- Whether the regulation has been amended (check EUR-Lex consolidated text)
- Whether the article has been amended or deleted
```

#### EU Directives

```
Directive [Year]/[Number]/EU of the European Parliament and of the Council
  of [date] on [subject], Art. [number]

CELEX number format: 3[Year]L[4-digit-number]
Example: CSRD = Directive (EU) 2022/2464, CELEX 32022L2464

Components to verify:
- Year and number
- Transposition deadline (directives must be implemented by this date)
- Whether the specific member state has transposed (check EUR-Lex National Transposition)
- National implementing measure (the directive article vs. the implementing regulation)
- IMPORTANT: Cite the NATIONAL IMPLEMENTING MEASURE for obligations in member states,
  not the directive itself (except for vertical direct effect claims after the deadline)
```

#### US Code of Federal Regulations

```
[Title] C.F.R. § [part].[section]
Example: 45 C.F.R. § 164.508

OR for proposed rules: [Volume] Fed. Reg. [page number] ([date])

Components to verify:
- Title and part number
- Whether eCFR version has been cross-checked against official printed CFR
- Date of last amendment (List of CFR Sections Affected — LSA)
- Whether the provision is still current or has been amended/revoked
```

#### Australia: Legislative Instruments

```
[Name] [Year] (Cth), s.[section]
Example: Fair Work Act 2009 (Cth), s.394

Statutory instruments: [Name] [Year], cl.[clause] or s.[section]

Components to verify:
- Jurisdiction suffix: (Cth) for Commonwealth; (NSW), (Vic), etc. for states
- Section number (check Federal Register of Legislation for current version)
- Whether the instrument has been repealed or amended
```

#### Canada: Regulations

```
[Name], [SOR/Year-Number] or CRC, c.[chapter], s.[section]
Example: Privacy Regulations, SOR/83-508, s. 3

Components to verify:
- SOR (Statutory Orders and Regulations) number
- Whether the regulation is consolidated or point-in-time
- Provincial regulations: check provincial gazette for citation format
```

### Court Rules and Procedural Instruments

```
UK Civil Procedure Rules (CPR): CPR r.[part].[rule]
  Example: CPR r.31.6

US Federal Rules of Civil Procedure: Fed. R. Civ. P. [rule]
  Example: Fed. R. Civ. P. 26(b)(1)

Australia: [Jurisdiction] Rules [Year], r.[rule]
  Example: Federal Court Rules 2011, r.5.03

Components to verify:
- Whether rules are current (procedural rules are frequently amended by practice directions)
- Practice directions: note these are NOT statutory and may have different status
- Whether the cited version reflects current rules (check official court website)
```

### Regulatory Guidance

```
[Issuing body], [Title of guidance document], [date/version], [paragraph or section]
Example: ICO, Guide to the UK GDPR, January 2021 (updated [date]), para. [X]

Components to verify:
- Date/version of the guidance (guidance is updated without formal legislative process)
- Whether the guidance has been superseded by a later version
- Legal status of the guidance (binding, quasi-binding, advisory, informational)
- IMPORTANT: Distinguish clearly from binding legislation in citations
```

---

## Status Classification

Assign one overall status to each citation based on the 7-check protocol results.

### ✅ VERIFIED

All applicable checks pass. The citation is correctly formatted, the provision is in force
at the temporal reference date, has not been materially amended or repealed, applies to
the claimed territory, the pinpoint is accurate, and the provision supports the claimed
proposition.

**Action**: No action required. Include in Glass Box as VERIFIED.

### ⚠️ CAUTION

One or more checks raise concerns that do not render the citation clearly incorrect but
require attention before reliance. Examples:

- Provision in force but has been amended since the cited version; amendment may or may
  not affect the proposition
- Minor format error that does not affect identification but should be corrected
- Territorial scope conditional on transposition status that has not been confirmed
- Proposition support is probable but there are qualifications that should be noted
- Guidance cited in a way that might be read as implying binding status

**Action**: Correct the identified concern before relying on the citation in a formal
document. Specify the concern and remediation step in the output.

### ❓ UNVERIFIABLE

Cannot confirm the citation's accuracy without access to an authoritative live database
that is not currently accessible. The citation may be correct or incorrect; the skill
cannot determine which.

**Action**: Flag prominently. Do not rely on the citation in court filings, regulatory
submissions, or formal opinions without independent verification via an authoritative
database (legislation.gov.uk, EUR-Lex, govinfo.gov, etc.) or a live citator service
(Westlaw, LexisNexis, vLex).

### 🔄 SUPERSEDED

The cited provision has been amended, revoked, replaced, or otherwise superseded. The
citation may have been correct at a past date but does not represent current law.

**Action**: Identify the superseding provision. Provide the correct current citation.
If the document concerns a past transaction at a date when the original provision was in
force, note that the citation was correct at that date but needs a temporal qualifier.

### ❌ INCORRECT

The citation contains a substantive error: the provision does not exist at the cited
reference, the section number is wrong, the year is wrong in a way that identifies a
different instrument, the provision does not support the claimed proposition, or the
provision has been repealed in its entirety.

**Action**: Identify the specific error. Provide the correct citation where possible.
If the provision appears to be hallucinated (no corresponding provision can be found in
the authoritative database), flag it as a potential AI hallucination and recommend that
no reliance be placed on the proposition until independently verified.

---

## Actionable Output per Finding

For each CAUTION, SUPERSEDED, or INCORRECT citation, produce a finding entry:

```
**Citation**: [original citation string]
**Status**: [CAUTION / SUPERSEDED / INCORRECT]
**Check(s) that failed**: [list of the specific checks that did not pass]
**Finding**: [specific description of the error or concern]
**Corrective action**: [specific steps to resolve]
**Correct citation** (where determinable): [corrected citation string]
**Confidence in correction**: [Definite / High / Probable / Possible / Unlikely]
**Reliance risk**: [CRITICAL — do not rely / HIGH — verify before use / MEDIUM — note and correct]
```

---

## Prioritization Framework

Prioritize verification findings by reliance risk:

### Priority 1 — Do Not Rely (CRITICAL)

Citations that, if relied on without correction, create material professional or legal risk:

- INCORRECT citations (provision does not exist or has been repealed)
- Potential AI hallucinations (no authoritative source found)
- SUPERSEDED citations where the superseding provision materially changes the law
- Citations to uncommenced provisions as if they are in force
- Guidance cited as binding legislation where it is not

### Priority 2 — Verify Before Use (HIGH)

Citations that are probably correct but carry unacceptable uncertainty for formal documents:

- UNVERIFIABLE citations in court filings or formal opinions
- CAUTION citations in high-stakes documents (regulatory submissions, M&A due diligence)
- Citations where the pinpoint cannot be confirmed without live database access

### Priority 3 — Correct and Note (MEDIUM)

Citations with format errors or minor concerns that do not affect the substance:

- Format errors that do not affect identification
- Guidance cited in a way that implies binding status but in a low-stakes context
- CAUTION citations where the amendment does not affect the proposition

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify all citations in the document. Classify by instrument type and
jurisdiction. Map to authoritative sources. Identify high-risk citations for priority
treatment.

**DO**: Apply the 7-check protocol to each citation. Classify each citation. Generate
finding entries for all CAUTION/SUPERSEDED/INCORRECT citations.

**CHECK**: Run the 5 Legislation Citation Quality Gates. For INCORRECT classifications,
run the 2-pass Self-Interrogation. Verify that all citations have been processed.

**ACT**: Record any novel findings (e.g., newly discovered hallucination patterns, unusual
jurisdictional scope issues). Update the Glass Box audit trail. Deliver the output.

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                  | Fail Action                                          |
| -------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **Source**     | Every verification finding cites the authoritative source consulted or explicitly states UNVERIFIABLE | Add source reference or mark UNVERIFIABLE            |
| **Format**     | All corrected citations follow the correct format for the jurisdiction and instrument type            | Fix format                                           |
| **Currency**   | Every provision checked for amendments or repeal at the temporal reference date                       | Flag [CHECK CURRENCY — verify against live database] |
| **Domain**     | Analysis stays within the jurisdiction's legal framework — no cross-jurisdictional assumptions        | Remove or flag jurisdictional bleed                  |
| **Confidence** | Uncertainty is explicitly stated for every UNVERIFIABLE finding                                       | Add confidence qualifier                             |

### Self-Interrogation for INCORRECT Classifications

For any citation classified as INCORRECT, apply this 2-pass review before delivering:

**Pass 1 — Error Identification Integrity**:

- Is the identified error actually an error, or could it reflect a valid alternative
  citation form (abbreviation convention, short title usage, historical citation style)?
- Could the year difference reflect a Royal Assent vs. commencement distinction rather
  than a wrong year?
- Could the section number reflect an amendment that renumbered sections, rather than a
  wrong section?

**Pass 2 — Correction Confidence**:

- Is the proposed correct citation actually correct, or could the correction itself
  introduce an error?
- Has the "correct" citation been verified against an authoritative source, or is it
  itself based on training data?
- If the correction cannot be confirmed against an authoritative source, should the
  classification be UNVERIFIABLE rather than INCORRECT?

If either pass reveals uncertainty, revise the classification before delivery. Never
confidently assert INCORRECT if there is a plausible alternative interpretation.

### Confidence Scoring

For each material verification finding, assign a confidence level:

| Level        | Range     | Meaning                                                           | Action                                                     |
| ------------ | --------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Provision verified against authoritative source; status confirmed | State with confidence                                      |
| **High**     | 0.80–0.94 | Strong basis from training data; minor verification risk remains  | State with brief caveat                                    |
| **Probable** | 0.60–0.79 | Training data supports finding but live verification needed       | State with explicit caveat and verification recommendation |
| **Possible** | 0.40–0.59 | Genuinely uncertain — competing interpretations exist             | Flag for human verification; present both possibilities    |
| **Unlikely** | 0.0–0.39  | Weak basis; finding may itself be incorrect                       | Mark [UNCERTAIN — verify independently]                    |

---

## Glass Box Audit Trail

Every verification output MUST include a Glass Box audit section. This makes the
verification process traceable and auditable.

```yaml
glass_box:
  skill: "legalcode-legislation-verification"
  document: "[document title or identifier]"
  document_type: "[court filing / legal opinion / contract / AI output / research note / other]"
  temporal_reference: "[current / YYYY-MM-DD]"
  jurisdiction(s): "[list of jurisdictions covered]"
  verification_scope: "[full 7-check / format and currency / in-force and repeal / proposition support / custom]"
  citations_identified: "[total number]"
  citations_verified: "[number with VERIFIED status]"
  citations_caution: "[number with CAUTION status]"
  citations_unverifiable: "[number with UNVERIFIABLE status]"
  citations_superseded: "[number with SUPERSEDED status]"
  citations_incorrect: "[number with INCORRECT status]"
  legalcode_mcp: "[Connected — citations verified via legalcode-mcp / Not connected — training data only]"
  reference_file: "[path to temp reference file or 'Not created']"
  hallucination_risk_items: "[number of citations flagged for heightened hallucination risk]"
  guidance_vs_legislation_issues: "[number identified / 0]"
  self_interrogation: "[PASS / REVISED / NOT APPLICABLE (no INCORRECT items)]"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  limitations:
    - "[e.g., 'All verifications based on training data only — live database verification required for court filing use']"
    - "[e.g., 'UK REUL/assimilated law status not independently confirmed — check Retained EU Law Dashboard']"
  reviewer: "AI-assisted — requires qualified legal review before reliance"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in legislation verification:

1. **Accepting AI-generated citations without verification**: AI language models hallucinate
   in approximately 1 in 6 legal citations (Stanford benchmarking). Every citation produced
   by an AI tool — including this skill — must be independently verified against an
   authoritative official database before reliance in any formal legal context.

2. **Treating the Royal Assent date as the commencement date**: Most significant Acts come
   into force later than Royal Assent, via commencement orders. Citing an Act as "in force
   from [Royal Assent date]" when commencement was later misrepresents the law.

3. **Verifying the Act but not the specific section**: An Act being "in force" does not
   mean every section is in force. Staged commencement orders can leave specific provisions
   uncommenced for years. Always verify the specific provision, not just the parent Act.

4. **Citing consolidated text as if it were the authoritative text**: EUR-Lex consolidated
   texts are documentary compilations without legal force; the Official Journal is the
   authentic text. UK legislation.gov.uk "revised" texts are editorially consolidated; the
   "as enacted" version is the authentic text. Always acknowledge which version you are citing.

5. **Citing an EU directive for an obligation owed to individuals in a member state**: EU
   directives bind member states, not directly individuals or businesses (with limited
   exceptions for vertical direct effect after the transposition deadline). Cite the national
   implementing legislation for the actual obligation. "Directive 2016/97/EU, Art. 20" is
   the wrong citation for an IDD obligation in Germany — cite the Versicherungsvertragsgesetz
   or equivalent implementing measure.

6. **Treating eCFR as the authoritative US federal regulatory text**: The Electronic Code
   of Federal Regulations is an editorial compilation. It is updated daily and is a useful
   research tool, but it is not the official, authenticated legal text. Cross-verify against
   the official CFR and the Federal Register.

7. **Ignoring post-Brexit REUL / assimilated law status (UK)**: EU-derived legislation in
   the UK has undergone significant reclassification since December 2020. Some REUL was
   revoked at the end of 2023; remaining REUL is now "assimilated law" and is no longer
   interpreted using EU principles. Citing pre-Brexit EU-derived provisions without checking
   current UK status may be citing law that no longer exists in the same form.

8. **Ignoring territorial scope within the UK**: England & Wales, Scotland, and Northern
   Ireland have different legislative frameworks on devolved matters. An Act with extent
   "England and Wales only" does not apply in Scotland. Always check the extent provision
   of the Act.

9. **Citing guidance as legislation**: Regulatory guidance (agency circulars, practice
   directions from non-statutory bodies, codes of practice without statutory backing) does
   not have the force of law. Citing it as if it imposes binding obligations overstates its
   legal effect. Distinguish between binding legislation, quasi-binding codes (those that
   courts must "have regard to"), and purely advisory guidance.

10. **Using point-in-time verification without flagging it**: If you verify a provision "as
    it stood on [date]" for a historical transaction, make this explicit. Presenting
    historical law as current law — or vice versa — is a material error.

11. **Confusing SI numbers with SI years**: SI 1998/1833 means the 1833rd SI made in 1998,
    not the 1998th SI of 1833. Transposing the number and the year (SI 1833/1998) is a
    common error that makes the citation impossible to locate.

12. **Verifying the primary legislation without checking the operative secondary legislation**:
    Many substantive obligations are imposed by secondary legislation made under a parent Act.
    Citing the parent Act when the specific obligation derives from the SI misidentifies the
    authoritative source and the correct citation.

13. **Assuming that a repeating Act (Finance Act, Appropriation Act) is the correct version**:
    Annual Acts with the same short title exist for multiple years (Finance Act 2020, Finance
    Act 2021, Finance Act 2022 etc.). Citing "Finance Act, s.[X]" without the year is
    unverifiable, and citing the wrong year produces a completely different legislative
    provision.

14. **Treating "in force" as equivalent to "currently unamended"**: A provision may be
    in force but substantially amended since the cited version. An analysis that confirms
    in-force status without checking amendment history misses a critical verification step.

15. **Verifying format without verifying content**: A citation can be perfectly formatted
    (correct Act name, correct year, correct section number format) and still be substantively
    wrong (the section does not say what the document claims). Format verification is
    necessary but not sufficient.

16. **Accepting "as amended" without identifying the amendment**: A citation noting that a
    provision is cited "as amended" without identifying the amending instrument is incomplete.
    The amended version may differ materially from the unamended version; the reader is
    entitled to know what the amendment was.

17. **Citing a provision for a broader proposition than it establishes**: A provision that
    applies to "employers with 250 or more employees" cannot be cited for a general
    obligation on all employers. A permission ("may") cannot be cited for a mandate ("must").
    Always verify that the proposition matches the actual scope and effect of the provision.

18. **Assuming that because you found a provision with a similar citation it is the one intended**:
    Hallucinated citations often resemble real citations closely. A citation to "Environmental
    Protection Act 1990, s.34A" should not be confirmed by finding s.34 of that Act — the
    "A" subsection may not exist. Verify the exact reference, not a close approximation.

---

## Localization Notes

### UK-Specific Depth

The UK system has several features that frequently cause verification errors:

- **Commencement orders**: Almost every significant Act requires a separate SI to commence
  its provisions. legislation.gov.uk commencement notes track these.
- **Revised vs. as enacted**: legislation.gov.uk shows both. The "revised" version
  incorporates textual amendments. Not all provisions are kept up to date — check the
  "Status" tab.
- **Extent vs. application**: "Extent" is the geographic scope of the provision; "application"
  may further limit where the provision operates in practice. Both must be checked.
- **UK REUL/assimilated law**: The Retained EU Law (Revocation and Reform) Act 2023 made
  sweeping changes effective 1 January 2024. Any citation to UK law that derives from
  EU legislation needs verification against current assimilated law status.

### EU-Specific Depth

- **CELEX numbers**: Each EU legal instrument has a unique CELEX number on EUR-Lex. The
  format reveals the instrument type (e.g., 32016R0679 = 2016 Regulation 679 = GDPR).
- **Consolidated vs. authentic**: EUR-Lex consolidated texts show all amendments integrated
  but are not the Official Journal authentic text. Corrigenda (corrections) are common in EU law.
- **Regulations vs. Directives**: Regulations apply directly; directives require
  transposition. Many practitioners confuse these, particularly for GDPR (regulation,
  directly applicable) vs. NIS2 Directive (requires national transposition by October 2024).
- **Transposition deadlines**: A directive's transposition deadline does not guarantee that
  a member state has actually transposed. Check EUR-Lex "National Transposition" for each
  member state's implementing measures.

### US-Specific Depth

- **Codification lag**: Newly enacted statutes may not immediately appear in the US Code on
  govinfo.gov. The Statutes at Large (via govinfo.gov) is the authoritative text for recent
  enactments before codification.
- **eCFR editorial disclaimer**: eCFR explicitly states it is not the official legal edition.
  Always cross-verify important regulations against the official CFR print edition and
  the Federal Register.
- **State law divergence**: Federal minimum standards are often exceeded by state law.
  Verify whether a federal citation alone covers the complete legal obligation, or whether
  state law must also be cited.

### Nordic-Specific Depth

- **Language**: Nordic legislation databases publish primarily in the national language.
  Legal translations (to English) are not authoritative and may lag behind amendments.
- **Norway (Lovdata)**: The full database (Lovdata Pro) is a subscription service; the
  free tier provides Supreme Court and selected decisions but not all legislation.
- **Sweden (SFS)**: The Statutes Compilation (Statens Författningssamling) is the
  authoritative source. Each instrument has an SFS number (e.g., SFS 1982:763).
- **Finland (Finlex)**: Official since January 2011; Swedish-language texts available for
  most laws (Finland is bilingual — Finnish and Swedish texts are equally authentic).

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary verification tool.

**With legalcode-mcp connected (preferred):**

- In Step 4, use legalcode-mcp to retrieve the text of each cited provision
- Verify in-force status, amendment history, and pinpoint accuracy against the database
- Save results to `/tmp/legalcode-legislation-verification-[document-id].md`
- Mark all legalcode-mcp-verified citations as VERIFIED in the Glass Box audit trail
- For SUPERSEDED or INCORRECT findings, search for the correct current provision via
  legalcode-mcp

**Without legalcode-mcp:**

- Mark all citations with [VERIFY AGAINST AUTHORITATIVE SOURCE]
- Note in Glass Box: `legalcode_mcp: "Not connected — training data only"`
- Provide direct URL to the authoritative database for each citation
  (e.g., `https://www.legislation.gov.uk/ukpga/2010/15/section/26` for Equality Act 2010, s.26)
- Apply heightened confidence scoring (no finding should exceed "Probable" confidence
  without legalcode-mcp or live database verification)
- Include a prominent notice: "All verifications in this report are based on AI training
  data and carry hallucination risk. Independently verify every citation against the
  authoritative database before reliance in any formal legal context."

---

## Writing Standards

Apply plain-language discipline to all output.

**For finding entries (shared with lawyers and non-lawyers):**

- Active voice: "Section 15 does not contain the claimed rule" not "The claimed rule is
  not contained in Section 15"
- Short sentences. One finding per sentence.
- Name the specific error: "The year should be 2010, not 2001" not "there may be a
  year-related issue"
- Avoid hedge stacking: not "it appears that this may potentially be an issue" — say
  what the finding is and what the confidence level is

**For the verification report (formal document):**

- Executive summary suitable for a non-lawyer who needs to understand risk exposure
- Technical details in the per-citation table for the lawyer who will act on the findings
- Confidence scores to allow the reader to triage where independent verification is needed

**Quality gates before delivery:**

1. Can a supervising lawyer immediately act on each finding? If not, add specificity.
2. Is every INCORRECT finding supported by a stated basis (not just asserted)?
3. Is every UNVERIFIABLE finding accompanied by the URL for manual verification?
4. Has the Glass Box audit trail been completed?
5. Are all confidence levels accurately set — no overconfidence where training data is the
   only basis?

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Legislation Verification Report

**Document**: [title or identifier]
**Document type**: [court filing / legal opinion / contract / AI output / other]
**Jurisdiction(s)**: [list]
**Temporal reference date**: [date]
**Verification scope**: [full 7-check / targeted]
**Date of verification**: [date]
**legalcode-mcp**: [Connected / Not connected — manual verification required]

---

## Executive Summary

**Overall finding**: [brief description of the overall citation quality]

- Total citations reviewed: [N]
- ✅ VERIFIED: [N] ([%])
- ⚠️ CAUTION: [N] ([%])
- ❓ UNVERIFIABLE: [N] ([%])
- 🔄 SUPERSEDED: [N] ([%])
- ❌ INCORRECT: [N] ([%])

**Priority 1 items (do not rely)**: [N] — [brief description if any]
**Guidance cited as legislation**: [N items / None]
**AI hallucination risk citations**: [N / None]

**Recommended action**: [one-paragraph summary of what needs to be done before the document can be used]

---

## Citation-by-Citation Verification Table

| #   | Citation   | Type                                 | Check 1 Source                   | Check 2 Format      | Check 3 In-Force                 | Check 4 Amendment                | Check 5 Scope                    | Check 6 Pinpoint         | Check 7 Proposition              | Status           |
| --- | ---------- | ------------------------------------ | -------------------------------- | ------------------- | -------------------------------- | -------------------------------- | -------------------------------- | ------------------------ | -------------------------------- | ---------------- |
| 1   | [citation] | [Act/SI/Reg/Directive/Rule/Guidance] | [PASS/FAIL/CAUTION/UNVERIFIABLE] | [PASS/FAIL/CAUTION] | [PASS/FAIL/CAUTION/UNVERIFIABLE] | [PASS/FAIL/CAUTION/UNVERIFIABLE] | [PASS/FAIL/CAUTION/UNVERIFIABLE] | [PASS/FAIL/UNVERIFIABLE] | [PASS/FAIL/CAUTION/UNVERIFIABLE] | [✅/⚠️/❓/🔄/❌] |

---

## Findings

### Priority 1 — Do Not Rely

[For each INCORRECT or high-risk citation:]

**Citation**: [original citation string]
**Status**: ❌ INCORRECT / 🔄 SUPERSEDED
**Finding**: [specific description of the error]
**Corrective action**: [specific steps to resolve]
**Correct citation** (where determinable): [corrected citation string]
**Confidence in correction**: [Definite / High / Probable / Possible]

---

### Priority 2 — Verify Before Use

[For each UNVERIFIABLE citation or CAUTION citation in a high-stakes context:]

**Citation**: [original citation string]
**Status**: ❓ UNVERIFIABLE / ⚠️ CAUTION
**Finding**: [concern]
**Verification URL**: [direct link to authoritative database]
**Corrective action**: [what to check]

---

### Priority 3 — Correct and Note

[For CAUTION items with format errors or minor concerns:]

**Citation**: [original citation string]
**Issue**: [brief description]
**Recommended correction**: [corrected citation or notation]

---

## Guidance vs. Legislation Issues

[If any guidance was cited as if binding, list here with explanation]

---

## Notes on Hallucination Risk

[If any citations were flagged for heightened hallucination risk, explain which and why]

---

## Next Steps

[Ordered list of specific actions, with priority level]

1. [Priority 1 action: citation to correct before filing / sending]
2. [Priority 2 action: verification required before use]
3. [Priority 3 action: format correction recommended]

---

[Glass Box YAML — see Glass Box Audit Trail section]
```

---

## Provenance

Legalcode original synthesis (2026-03-22). Created as a native Legalcode replacement for
the imported `legislation-verification` skill (`skills/general/workflows/imported-uk-legal-plugins--skills-legislation-verification/SKILL.md`), which was UK-only and tied to a specific CLI tool (`legislation-intel`) and Neo4j infrastructure not available in the general Legalcode deployment. This skill extends coverage to all major common law and EU jurisdictions, adds the full 18-element Legalcode quality framework, and adds jurisdiction-agnostic multi-instrument coverage. Legal research basis: official database documentation (legislation.gov.uk, EUR-Lex, govinfo.gov, legislation.gov.au, laws-lois.justice.gc.ca, irishstatutebook.ie, Nordic portals), Stanford AI hallucination benchmarking (16–17% citation hallucination rate), EU directive transposition mechanics (EUR-Lex National Transposition collection), and UK REUL/assimilated law research (Retained EU Law (Revocation and Reform) Act 2023, Retained EU Law Dashboard). All legal references marked [VERIFY] where not independently confirmed.
