---
name: legalcode-copyright-infringement-assessment
description: Assess copyright infringement risk across US, EU, and UK law. Use when determining whether
  a work infringes an existing copyright, evaluating defenses to an infringement claim, clearing a proposed
  use before publication or distribution, responding to a DMCA takedown or cease-and-desist letter, or
  advising on copyright risk in AI training datasets, sampling, digital media, software development, or
  creative works. Covers substantial similarity analysis, fair use four-factor evaluation (17 USC 107),
  EU InfoSoc Directive exceptions (2001/29/EC), UK fair dealing (CDPA 1988 ss.29–30A), de minimis use,
  independent creation defense, DMCA safe harbor (17 USC 512), statutory damages and willfulness (17 USC
  504), and AI-generated content copyright. Also triggers when asked about parody, satire, remix, sampling,
  text and data mining, educational use, news reporting, or platform liability for user-generated content.
  Jurisdiction-agnostic workflow with deep US/EU/UK coverage.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Copyright Infringement Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted copyright infringement
> assessment. It does not constitute legal advice. All outputs should be reviewed by a
> qualified IP lawyer licensed in the relevant jurisdiction before use. Copyright law
> evolves rapidly — cases cited may have been reversed, distinguished, or superseded; verify
> all citations against authoritative sources before relying on them. Statutory and case law
> references from memory carry hallucination risk — mark all unverified references [VERIFY].

---

## Purpose and Scope

This skill assesses copyright infringement risk by analyzing the original work, the allegedly
infringing work or use, and the applicable legal framework. It produces a classified risk
assessment with actionable recommendations.

**Covers:**

- Substantial similarity analysis (extrinsic/intrinsic test; abstraction-filtration-comparison
  for software; ordinary observer test)
- Fair use four-factor analysis (17 USC 107) including the post-AWF v. Goldsmith (2023)
  transformative use framework
- EU InfoSoc Directive 2001/29/EC exceptions and DSM Directive 2019/790 text and data mining
- UK fair dealing (CDPA 1988 ss.29–30A) and the parody/pastiche exception (s.30A)
- DMCA safe harbor eligibility and takedown procedure compliance (17 USC 512)
- De minimis use doctrine
- Independent creation defense
- Other defenses: public domain, licence, first sale/exhaustion, merger doctrine
- Statutory damages and willfulness assessment (17 USC 504; EU Enforcement Directive 2004/48/EC)
- AI-generated content and training data copyright issues
- Dual perspectives: claimant (rights enforcement) and respondent/clearance (defence)

**Does not:**

- Draft copyright licences (see `legalcode-technology-license-agreement`)
- Handle trademark or patent infringement (see `legalcode-patent-landscape-analysis`)
- Assess moral rights claims independently (addressed where relevant to infringement analysis)
- Provide legal advice or replace qualified IP counsel

---

## Jurisdiction and Governing Law

This skill provides deep coverage across three primary jurisdictions:

| Jurisdiction       | Primary Statute                                                                     | Key Standard                                                                       |
| ------------------ | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **United States**  | Copyright Act 1976, 17 USC §§ 101–1332                                              | Originality (Feist); substantial similarity; four-factor fair use                  |
| **European Union** | InfoSoc Directive 2001/29/EC; DSM Directive 2019/790; Software Directive 2009/24/EC | "Own intellectual creation" (Infopaq); exhaustive exceptions list; three-step test |
| **United Kingdom** | CDPA 1988 (as amended, post-Brexit)                                                 | Substantial part; fair dealing (enumerated purposes only)                          |

**Berne Convention foundation**: All three jurisdictions are Berne Union members. The
Convention sets minimum standards (life + 50 years; no formalities for protection) that
most national laws exceed. [VERIFY for specific jurisdiction]

[JURISDICTION-SPECIFIC] For jurisdictions outside US/EU/UK, research:

- Local adaptation of Berne minimum standards
- Whether a fair use (US-style open-ended) or fair dealing (UK-style enumerated) system applies
- Registration requirements (most Berne members do not require registration for protection,
  but it may affect remedies)
- Moral rights inalienability (especially relevant in EU civil law jurisdictions)
- Specific statutory damages regimes

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- The same facts could support multiple risk classifications depending on context
- Evidence of copying, access, or defence strength depends on facts the user must supply
- Damages assessment requires information only the user can provide

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

### Step 1: Accept the Materials

Accept materials in any of these formats:

- **File**: The original work and/or allegedly infringing work as documents, images, audio,
  or code files
- **URL**: Link to the original or allegedly infringing content online
- **Description**: Written description of both works and the nature of the alleged
  infringement
- **Pasted text**: Excerpts from the works, side-by-side for comparison

If neither the original nor the allegedly infringing work is provided, prompt the user
to supply at least a description of each.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the analysis, ask the user the following questions.
Present as structured options where possible:

1. **Perspective**: Which role are you assessing from?
   - Options: **Claimant** (my copyright may have been infringed), **Respondent/Defendant**
     (I have been accused of infringement), **Clearance** (pre-use assessment before
     publication or distribution), **Neutral** (third-party assessment)
   - _Why this matters_: The classification and recommended actions differ significantly
     depending on perspective. A finding of BORDERLINE risk means "proceed carefully" for
     clearance but "raise the defence" for a defendant.

2. **Work type**: What type of work is involved?
   - Options: Literary work (text, code, screenplay), Musical work (composition, lyrics),
     Sound recording (master recording), Artistic/visual work (photograph, painting,
     illustration, design), Audiovisual work (film, video), Software/code, Database,
     Architectural work, Other
   - _Why this matters_: The substantial similarity test and available exceptions differ
     by work type. Software uses the AFC test; music uses Arnstein v. Porter; visual works
     use total look and feel.

3. **Jurisdiction(s)**: Where is the original work owned/registered and where does the
   allegedly infringing use occur?
   - Options: United States only, European Union (specify member state if relevant),
     United Kingdom only, Cross-border (specify countries), Unknown/multiple
   - _Why this matters_: Fair use is a US doctrine; UK fair dealing is narrower; EU has
     an exhaustive list of exceptions. DMCA safe harbour applies only in the US.

4. **Registration**: Has the original work been registered with the US Copyright Office
   (or equivalent)?
   - Options: Yes — registered before alleged infringement began, Yes — registered more
     than 3 months after first publication, No — not registered, Unknown
   - _Why this matters_: Under 17 USC 412, statutory damages and attorney's fees are only
     available if registration precedes infringement or occurs within 3 months of first
     publication.

5. **DMCA context**: Is this a digital/online infringement scenario involving a platform
   or service provider?
   - Options: Yes — hosted on third-party platform (social media, cloud, UGC platform),
     Yes — I am a platform/OSP receiving a takedown notice, No — direct infringement
     between two parties
   - _Why this matters_: DMCA safe harbour (17 USC 512) applies only to qualifying service
     providers in the US; the EU has a parallel regime under DSM Directive Article 17.

6. **Commercial context**: Is the allegedly infringing use commercial or non-commercial?
   - Options: Commercial (for profit or business use), Non-commercial (personal, educational,
     research), Mixed (non-profit but with commercial elements)
   - _Why this matters_: Affects the fair use analysis (factor 1) and the EU/UK educational
     and private-use exceptions.

If the user provides partial context, proceed with stated assumptions. State assumptions
explicitly: "I'm assuming US law governs — let me know if a different jurisdiction applies."

### Step 3: Gather Jurisdiction-Relevant Legal Authority

Identify the applicable jurisdiction(s) from the context provided. Use **legalcode-mcp**
to gather current legal authority for this assessment.

**Research process:**

1. **Search legalcode-mcp** for:
   - Current text of the applicable copyright statute (17 USC, CDPA 1988, InfoSoc
     Directive as implemented in the relevant member state)
   - Leading case law on substantial similarity for the work type involved
   - Current fair use / fair dealing case law (especially post-AWF v. Goldsmith for US)
   - DMCA safe harbour case law if platform/online infringement is involved
   - Recent legislative developments affecting the work type or use case

2. **Save results** to `/tmp/legalcode-copyright-authority.md`:

   ```markdown
   # Copyright Authority Reference — [Matter Description]

   ## Date: [date]

   ## Jurisdictions: [list]

   ### Statutes & Regulations

   - [Statute, section, current text or summary]

   ### Case Law — Substantial Similarity

   - [Case, citation, key holding]

   ### Case Law — Fair Use / Exceptions

   - [Case, citation, key holding]

   ### Case Law — DMCA / Platform Liability

   - [Case, citation, key holding]

   ### Recent Developments

   - [Development, date, impact]
   ```

3. **Use the reference file throughout** the analysis. Cite legalcode-mcp-sourced
   authority as VERIFIED in the Glass Box Audit Trail.

**If legalcode-mcp is not connected:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box Audit Trail: `legalcode_mcp: "Not connected"`
- Focus the analysis on structural risk assessment and flag that legal citations require
  independent verification

### Step 4: Identify Protectable Expression

Before assessing similarity, determine what is actually protected in the original work.
This step filters unprotectable elements that cannot anchor an infringement claim.

**⟁ CLARIFY** — If the protectable elements are unclear from the materials provided, ask:
"To assess infringement, I need to identify what is legally protected in the original work.
Can you identify which specific elements of the original you believe were copied?"

Apply the following framework:

**Protectable elements:**

- Original expression with "minimal degree of creativity" (Feist Publications v. Rural Tel.
  Serv. Co., 499 U.S. 340 (1991)) [VERIFY]
- EU standard: "own intellectual creation" reflecting personal intellectual creation
  (Infopaq International A/S v. Danske Dagblades Forening, C-5/08 (CJEU 2009)) [VERIFY]
- Selection, coordination, or arrangement of elements (even if individual elements are
  not protectable)
- Specific expression of an idea (not the idea itself)

**Unprotectable elements — filter before similarity analysis:**

| Element                      | Rule                                                                                                                     | Examples                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| **Ideas, concepts, methods** | 17 USC 102(b); not protectable in any jurisdiction                                                                       | Plot ideas, game rules, mathematical methods                          |
| **Facts and data**           | Feist: no "sweat of the brow" copyright in raw data                                                                      | News events, historical dates, scientific data                        |
| **Functional elements**      | Functional aspects of software/designs are not protectable expression                                                    | APIs (but see Oracle v. Google), utilitarian product features         |
| **Merger doctrine**          | When there is only one (or very few) ways to express an idea, the expression merges with the idea and is not protectable | Legal form language, standard warnings, minimal-expression structures |
| **Scènes à faire**           | Stock elements, standard features, elements dictated by genre or conventions                                             | Stock characters, standard plot elements, clichéd phrases             |
| **Titles, names, slogans**   | Generally not copyrightable (trademark law may apply separately)                                                         | Song titles, character names, advertising taglines                    |
| **US government works**      | 17 USC 105: works created by US federal government employees as part of official duties                                  | Federal statutes, court opinions, federal agency reports              |
| **Public domain works**      | Copyright has expired or never subsisted                                                                                 | Pre-1928 US works; life + 70 years EU/UK                              |

**For software**, apply the **Abstraction-Filtration-Comparison (AFC) test**
(Computer Associates Int'l v. Altai, Inc., 982 F.2d 693 (2d Cir. 1992) [VERIFY]):

1. **Abstraction**: Decompose program into structural components (literal code → algorithms
   → program structure → purpose)
2. **Filtration**: Remove unprotectable elements from each level (ideas, elements dictated
   by efficiency, elements from public domain, functional requirements)
3. **Comparison**: Compare remaining protectable expression to defendant's work

### Step 5: Assess Copying and Access

Copyright infringement requires proof of: (1) ownership of a valid copyright AND
(2) copying of protected expression.

Copying is typically proven by circumstantial evidence:

- **Access**: The defendant had a reasonable opportunity to view or encounter the original
  work. Access can be inferred from:
  - Wide public distribution (published, broadcast, online)
  - Actual receipt or access (forwarded, viewed, purchased)
  - Access to a third party who shared with defendant ("chain of access")

- **Probative similarity**: The works are similar enough to support an inference of copying
  (even if the copying is of unprotectable elements — this is distinct from actionable
  substantial similarity)

**⟁ CLARIFY** — If access is disputed or uncertain:

- "Is there evidence the defendant had access to the original work? For example: was the
  original publicly available? Did the defendant receive a copy? Did the defendant work
  with someone who had access?"

**Inverse ratio rule**: Some US circuits (formerly 9th Circuit) held that less evidence
of access was needed if similarity was very high. Note: The 9th Circuit **rejected** the
inverse ratio rule in Skidmore v. Led Zeppelin, 952 F.3d 1051 (9th Cir. 2020) (en banc)
[VERIFY]. Independent creation remains a complete defence even with high similarity.

**Subconscious copying**: A defendant who unconsciously reproduces a protected work can
still infringe (Bright Tunes Music Corp. v. Harrisongs Music, Ltd., 420 F. Supp. 177
(S.D.N.Y. 1976) — George Harrison's "My Sweet Lord") [VERIFY].

### Step 6: Substantial Similarity Analysis

Apply the appropriate substantial similarity test for the jurisdiction and work type:

**⟁ CLARIFY** — For complex works or mixed jurisdictions:
"For this substantial similarity analysis, should I focus on (a) US circuit court standards,
(b) EU 'essential characteristics' standard, (c) UK 'substantial part' standard, or
(d) all three?"

See **§2. Substantial Similarity Analysis** in the Topic Analysis Reference section for
the full analytical framework.

Output a comparative table for each set of potentially copied elements:

| Element     | Original Expression | Allegedly Infringing Expression | Protected? | Substantially Similar? |
| ----------- | ------------------- | ------------------------------- | ---------- | ---------------------- |
| [Element 1] | [Description]       | [Description]                   | Yes/No     | Yes/Probably/No        |
| [Element 2] | ...                 | ...                             | ...        | ...                    |

### Step 7: Defense Analysis

For each viable defence, assess strength and apply the relevant framework. Work through
all defences before reaching the overall classification — a weak infringement case paired
with a strong defence may still reach PROBABLE DEFENSE even if the similarity analysis
leans toward copying.

#### 7a. Fair Use (US) / Fair Dealing (UK) / EU Exceptions

Apply the applicable framework from the **Topic Analysis Reference** sections §3 (US
Fair Use), §4 (EU Exceptions), and §5 (UK Fair Dealing).

**⟁ CLARIFY** — For borderline fair use / fair dealing cases:
"The fair use analysis here is genuinely contested. Before I classify this, can you tell me:
(a) What is the purpose and intended audience for the allegedly infringing work?
(b) Is there an existing licensing market for this type of use of the original?
(c) Did the user seek or consider a licence before using the work?"

#### 7b. DMCA Safe Harbour (US digital/platform context)

If the infringement involves a platform or online service provider, assess safe harbour
eligibility. See **§6. DMCA Safe Harbour** in the Topic Analysis Reference.

#### 7c. De Minimis Use

Assess whether the taking is quantitatively and qualitatively trivial. See **§7. De
Minimis Use** in the Topic Analysis Reference.

#### 7d. Independent Creation

If the defendant claims independent creation, assess the strength of that defence.
See **§8. Independent Creation Defence** in the Topic Analysis Reference.

#### 7e. Other Defences

Check all applicable defences from **§9. Other Defences**:

- Public domain status of the original
- Express or implied licence
- First sale / exhaustion (distribution context)
- Merger doctrine (ideas merged with expression)
- Government works / sovereign immunity

### Step 8: Damages and Willfulness Assessment

Assess the damages exposure if infringement is found. See **§10. Statutory Damages and
Willfulness** in the Topic Analysis Reference.

**⟁ CLARIFY** — To complete the damages assessment, ask if not already established:

1. "Is the original work registered with the US Copyright Office? If so, when was it
   registered relative to the alleged infringement?"
2. "Has the copyright owner previously sent a cease-and-desist letter or DMCA takedown
   notice to this defendant regarding this work?"
3. "Was the defendant aware (or should they have been aware) that the original was
   copyrighted when the use began?"

### Step 9: Risk Classification

Classify the overall infringement risk using the five-tier system defined in the
**Risk Classification** section below. For each tier, apply the appropriate
**⟁ CLARIFY** points if the evidence is borderline.

**⟁ CLARIFY** — For borderline PROBABLE INFRINGEMENT / BORDERLINE cases:
"This assessment is on the border between PROBABLE INFRINGEMENT and BORDERLINE. The key
uncertainty is [defence/element]. Can you tell me [specific question]? This will determine
whether I classify this as requiring immediate legal response or a more measured approach."

### Step 10: Recommended Actions

Generate recommendations calibrated to:

- The risk classification (CLEAR INFRINGEMENT → CLEAR DEFENSE)
- The user's perspective (claimant / respondent / clearance)
- The damages exposure (registration status, willfulness indicators)

See the **Actionable Output Per Finding** and **Prioritization Framework** sections for
the full action matrices.

### Step 11: Quality Verification

Before delivering the assessment, run all quality checks:

1. **Citation Quality Gates** — Run all 5 gates silently. Revise any failures.
2. **Self-Interrogation** — For any CLEAR INFRINGEMENT or CLEAR DEFENSE classification,
   run the 3-pass self-interrogation. Revise if any pass reveals a weakness.
3. **Confidence Scoring** — Assign a confidence score to each material finding.
4. **Completeness check** — Confirm all applicable defences have been addressed; confirm
   jurisdiction coverage matches the context provided.
5. **Generate Glass Box Audit Trail** and append to the output.

### Step 12: Generate Output

Structure the final deliverable using the **Output Format Template** at the end of this
skill. Deliver:

- Executive summary with overall classification
- Copyrightability analysis
- Substantial similarity table
- Defence analysis per applicable defence
- Damages exposure table
- Recommended actions (calibrated to perspective)
- Glass Box Audit Trail

---

## Topic Analysis Reference

### §1. Copyrightability and Protectable Expression

Copyright subsists automatically upon creation of an original work fixed in a tangible
medium of expression (US: 17 USC 102; EU: upon creation; UK: CDPA s.3(2)). No formalities
are required for protection in Berne Union countries, though registration has material
consequences for US remedies.

**Originality standards:**

| Jurisdiction | Standard                                                                                     | Authority                                                                |
| ------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| US           | "Original" = independently created + "minimal degree of creativity"                          | Feist Publications v. Rural Tel. Serv. Co., 499 U.S. 340 (1991) [VERIFY] |
| EU           | "Own intellectual creation" reflecting "free and creative choices"                           | Infopaq C-5/08; Painer C-145/10 [VERIFY]                                 |
| UK           | Same as EU post-Infopaq adoption; pre-Infopaq: "skill and labour" approach still influential | Designers Guild v. Russell Williams [2000] UKHL 58 [VERIFY]              |

**Copyright term (general rule):**

- **US**: Life of author + 70 years (works created after 1978); complex pre-1978 rules
  (consult Hirtle's copyright duration chart [VERIFY])
- **EU**: Life + 70 years (Directive 2006/116/EC) [VERIFY]
- **UK**: Life + 70 years (CDPA s.12) [VERIFY]

**Sound recordings / phonograms:**

- US: Published before 2022 = 95 years from publication under MMA 2018 transition rules [VERIFY]
- EU: 70 years from release (Term Extension Directive 2011/77/EU) [VERIFY]
- UK: 70 years from release (CDPA s.13A) [VERIFY]

---

### §2. Substantial Similarity Analysis

Substantial similarity is the core question in most copyright infringement cases. Apply
the test appropriate to the jurisdiction and work type.

#### 2.1 United States

**9th Circuit — Extrinsic/Intrinsic test:**

- **Extrinsic test** (objective): Compare specific, objectively identifiable elements of
  the works (plot, characters, themes, setting, mood, dialogue, sequence of events, pace).
  Expert testimony is admissible. Filter out unprotectable elements before comparison.
- **Intrinsic test** (subjective): Would the "ordinary reasonable person" find the works
  substantially similar in total concept and feel? No expert testimony; purely subjective.
  _Both_ tests must be satisfied for actionable similarity. (Rentmeester v. Nike, 932
  F.3d 986 (9th Cir. 2019) [VERIFY])

**2d Circuit — Ordinary Observer test:**

- After filtering unprotectable elements, would an "ordinary observer" — unless looking
  for differences — mistake the copy for the original? Total look and feel matters.
  (Arnstein v. Porter, 154 F.2d 464 (2d Cir. 1946) [VERIFY])

**Qualitative substantiality (all circuits):**

- Even if a small _quantity_ is taken, infringement exists if the _quality_ of what was
  taken is substantial — i.e., the "heart" of the original work. (Harper & Row v. Nation
  Enters., 471 U.S. 539 (1985) [VERIFY] — 300 words from 200,000-word memoir were the
  most powerful passages)

#### 2.2 European Union

The CJEU standard requires reproduction of the "essential characteristics" of the original
expression — the elements reflecting the author's personal intellectual creation:

- Even a short extract (11-word newspaper headline) can be a reproduction if it contains
  protected expression (Infopaq C-5/08 [VERIFY])
- What matters is whether the defendant reproduced elements reflecting the author's
  "free and creative choices," not merely the author's labour or investment
- Sampling: Even a 2-second phonogram sample can infringe the sound recording right
  (though not the musical composition if altered beyond recognition) (Pelham v. Hütter,
  C-476/17 [VERIFY])

#### 2.3 United Kingdom

Under CDPA s.16(3), infringement requires copying of "a substantial part" of the work:

- "Substantial" is qualitative, not merely quantitative (Designers Guild v. Russell
  Williams [2000] UKHL 58 [VERIFY])
- Ask: were the elements copied the product of the author's skill and intellectual effort?
- "Astute observation" or significant research that produces factual data — even if
  effort-intensive — does not attract copyright in the data itself (Ravenscroft v. Herbert
  [1980]; see also Football Dataco v. Yahoo! UK Ltd C-604/10 (CJEU) on database rights
  [VERIFY])

#### 2.4 Software-Specific (AFC Test)

Apply the Abstraction-Filtration-Comparison (AFC) test (Computer Associates v. Altai,
982 F.2d 693 (2d Cir. 1992) [VERIFY]) to software:

**Step A — Abstraction**: Break the allegedly infringing program into structural levels:

```
Level 1: Specific literal code (source code, object code)
Level 2: Program architecture and structure
Level 3: Module design and interoperability
Level 4: Data structures and algorithms
Level 5: Purpose and function
```

**Step B — Filtration**: At each level, remove unprotectable elements:

- Ideas, algorithms, and mathematical operations (17 USC 102(b))
- Elements dictated by efficiency (only one efficient way to accomplish the result)
- Elements dictated by external factors (hardware, OS requirements, industry standards)
- Public domain elements (standard code libraries, open-source components)
- **APIs**: The declaring code of an API can be copyrightable expression; reimplementation
  for interoperability may be fair use (Oracle Am., Inc. v. Google LLC, 593 U.S. 1 (2021)
  [VERIFY] — Google's copying of Java API declarations for Android held fair use)

**Step C — Comparison**: Compare remaining protectable expression only.

---

### §3. Fair Use (17 USC 107) — United States

Fair use is an affirmative defence. The defendant bears the burden of establishing fair
use. Courts assess all four factors, and no single factor is determinative — they must be
weighed together.

#### Factor 1: Purpose and Character of the Use

Key questions:

- Is the use commercial or non-commercial? (Commercial weighs against fair use, but is
  not determinative — Campbell v. Acuff-Rose Music, Inc., 510 U.S. 569 (1994) [VERIFY])
- Is the use transformative — does it add new meaning, expression, message, or purpose
  that is different from the original?

**Post-AWF v. Goldsmith (2023) framework:**

The Supreme Court in Andy Warhol Foundation for the Visual Arts, Inc. v. Goldsmith, 598
U.S. 508 (2023) [VERIFY] clarified the transformative use analysis:

- The question is whether the allegedly infringing work has a **sufficiently different
  purpose or character** compared to the original work, **not** simply whether it adds
  new aesthetic expression
- A commercial use that serves the **same basic purpose** as the original (e.g., both
  used as magazine covers to illustrate the same artist) weighs heavily against fair use,
  even if the new work adds artistic transformation
- "Transformative" does not automatically mean artistically distinct — transformation
  must be assessed in relation to the original's market and purpose

**Parody vs. satire:**

- **Parody** (commenting on the original work) can be transformative fair use because it
  must evoke the original to comment on it (Campbell v. Acuff-Rose [VERIFY])
- **Satire** (using the original to comment on something else) receives less protection
  because it could have borrowed from something else
- Key question: does the new work need to evoke the original, or could it have used a
  different work?

#### Factor 2: Nature of the Copyrighted Work

- Works closer to the creative/expressive end of the spectrum receive stronger protection
  than factual/informational works
- Unpublished works receive stronger protection than published works (Harper & Row [VERIFY])
- This factor is generally the least decisive of the four

#### Factor 3: Amount and Substantiality Taken

- Both **quantity** (what percentage of the original was taken) and **quality** (was the
  "heart" of the original taken?) matter
- Taking a small but highly memorable or essential portion can weigh against fair use
  even if the proportion is small (Harper & Row: 300 words from 200,000 [VERIFY])
- Wholesale copying of an entire work weighs against fair use
- No bright-line rules — context governs

#### Factor 4: Effect on the Potential Market

- Assess both the **actual harm** to the current market for the original and harm to
  any **potential licensing market** for this type of use
- If the use replaces the original (i.e., the defendant's work serves as a substitute),
  factor 4 weighs heavily against fair use
- If the use creates a new market that does not substitute for the original, factor 4
  weighs in favour
- **AWF v. Goldsmith** context: the licensing market for using the original image on
  magazine covers was a relevant market, and Warhol's use directly competed in that market

**Overall fair use assessment:**
Apply the four-factor balancing test. Note the factors that favour and oppose fair use.
There is no mathematical formula — courts assess the totality. Identify the two or three
most decisive factors and weight them accordingly.

---

### §4. EU Copyright Exceptions (InfoSoc Directive Art. 5)

EU exceptions are **exhaustive** — member states may only implement exceptions listed in
the directive, subject to the three-step test. Unlike US fair use, there is no open-ended
exception for "transformative" uses.

**Key exceptions under InfoSoc Directive 2001/29/EC Art. 5:**

| Exception                    | Article                                    | Scope                                                                    | Conditions                                                                           |
| ---------------------------- | ------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| Temporary copies             | Art. 5(1)                                  | Transient/incidental technical copies (browsing cache, streaming buffer) | Mandatory exception; no licence required                                             |
| Research/private study       | Art. 5(2)(c) (institutions) / Art. 5(3)(a) | Scientific/educational purposes                                          | Non-commercial; adequate acknowledgment; may require compensation                    |
| Quotation/criticism/review   | Art. 5(3)(d)                               | Quoting for commentary, criticism, review                                | Must be for criticism/review; adequate acknowledgment; extent no more than justified |
| News reporting               | Art. 5(3)(c)                               | Reporting on current events                                              | Press articles re-published only if not expressly reserved; acknowledgment required  |
| Parody, caricature, pastiche | Art. 5(3)(k)                               | Not mandatory — optional for member states                               | Must not unreasonably prejudice legitimate interests of the rightsholder             |
| Teaching/education           | Art. 5(3)(a)                               | Illustration for teaching                                                | Non-commercial purpose; acknowledged; extent justified                               |
| Persons with disabilities    | Art. 5(3)(b)                               | Uses solely for benefit of those with disability                         | No commercial purpose                                                                |

**DSM Directive 2019/790 exceptions:**

| Exception                          | Article   | Scope                                                                           |
| ---------------------------------- | --------- | ------------------------------------------------------------------------------- |
| Text and data mining — research    | Art. 3    | Research organisations and cultural heritage institutions; no opt-out           |
| Text and data mining — general     | Art. 4    | Any person/entity; rightsholders can **opt out** by machine-readable means      |
| Educational — digital/cross-border | Art. 5    | Mandatory exception; extended to online and cross-border educational activities |
| Cultural heritage preservation     | Art. 6    | Cultural heritage institutions; preservation copies                             |
| Out-of-commerce works              | Art. 8–11 | Collective licensing for out-of-commerce works by institutions                  |

**Three-step test (Art. 5(5) InfoSoc; Art. 9 Berne):**
An exception only applies if it:

1. Applies only in **special cases**
2. Does not **conflict with the normal exploitation** of the work
3. Does not **unreasonably prejudice the legitimate interests** of the rightsholder

**CJEU key cases:**

| Case                                  | Citation        | Key Holding                                                                                                                                 |
| ------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Infopaq v. Danske Dagblades           | C-5/08 (2009)   | 11-word extract can be copyright-protected; all copies including RAM copies are "reproductions"                                             |
| Pelham v. Hütter (Metall auf Metall)  | C-476/17 (2019) | Even a 2-second phonogram sample is a reproduction of the sound recording; sampling for artistic purposes may qualify under parody/pastiche |
| Funke Medien v. Bundesrepublik        | C-469/17 (2019) | News reporting exception does not override fundamental rights; exceptions must be interpreted strictly                                      |
| Spiegel Online v. Volker Beck         | C-516/17 (2019) | Hyperlinking to works without authorisation does not infringe if no new public is reached                                                   |
| VG Bild-Kunst v. Stiftung Preußischer | C-392/19 (2021) | Embedding a work in a frame on another website can infringe if technical measures are circumvented                                          |

[VERIFY all citations above against authoritative sources]

---

### §5. UK Fair Dealing (CDPA 1988)

UK fair dealing is **purpose-specific** — only the enumerated purposes qualify. It is
narrower than US fair use. "Fairness" is assessed in the context of the specific purpose.

**Key fair dealing provisions:**

| Section  | Purpose                                | Key Conditions                                                                                                 |
| -------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| s.29(1)  | Research for a non-commercial purpose  | Must be fair; sufficient acknowledgment unless impracticable                                                   |
| s.29(1C) | Private study                          | No acknowledgment required; no commercial purpose                                                              |
| s.30(1)  | Criticism or review                    | Criticism of the work or another work; sufficient acknowledgment; work must be available to the public         |
| s.30(2)  | Reporting current events               | Literary, dramatic, musical, or artistic works only; acknowledgment required (except for news in broadcasts)   |
| s.30A    | Parody, caricature, pastiche           | No acknowledgment required; must not conflict with normal exploitation or unreasonably prejudice rightsholders |
| s.31A    | Accessible copies for disabled persons | Must not commercially exploit the work                                                                         |
| s.32     | Illustration for instruction           | Non-commercial educational purposes; acknowledgment required                                                   |

**Assessing "fairness":**
Courts consider: (Hubbard v. Vosper [1972] 2 QB 84 [VERIFY])

- The proportion of the work taken relative to the purpose
- Whether the work was commercially available and used to avoid paying for a licence
- The purpose of the use and whether it required taking the amount taken
- The impact on the market for the original work

**Important post-Brexit point:** UK courts have not fully adopted CJEU fair dealing
jurisprudence. Existing CJEU cases pre-Brexit remain persuasive but are not binding.
Post-Brexit CJEU developments are not incorporated into UK law.

---

### §6. DMCA Safe Harbour (17 USC 512) — United States

The DMCA safe harbour shields qualifying online service providers (OSPs) from liability
for monetary damages for infringing content created by users.

**Four categories of safe harbour:**

| Category                      | Section | Type of Activity                                                   | Key Requirements                                                             |
| ----------------------------- | ------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| Transitory communications     | 512(a)  | Routing, transmitting, caching (ISPs, backbone)                    | Near-automatic; must be transitory and no modification                       |
| System caching                | 512(b)  | Intermediate caching of transmitted material                       | Standard technical process; no modification; comply with updating conditions |
| Storage at direction of users | 512(c)  | Hosting user-uploaded content (social media, cloud, UGC platforms) | Most litigated; see below                                                    |
| Information location tools    | 512(d)  | Search engines, linking/indexing                                   | No knowledge; no direct financial benefit; expeditious removal               |

**Requirements for 512(c) storage safe harbour:**

1. **No actual knowledge** of specific infringement
2. **No "red flag" knowledge**: not aware of facts/circumstances from which infringement
   is apparent (Viacom Int'l v. YouTube, Inc., 676 F.3d 19 (2d Cir. 2012) [VERIFY] —
   "red flag" requires specific knowledge, not general awareness of widespread infringement)
3. **No direct financial benefit** when the OSP has the right and ability to control the
   infringing activity (the "RICO-style" control requirement)
4. **Expeditious removal** of infringing content upon receipt of a valid DMCA takedown
   notice (512(c)(3))
5. **Designated agent**: The OSP must have a registered DMCA agent with the Copyright
   Office and publish agent contact information
6. **Repeat infringer policy**: The OSP must implement and enforce a policy for terminating
   repeat infringers (512(i)) (BMG Rights Mgmt. v. Cox Commc'ns, 881 F.3d 293 (4th Cir. 2018) [VERIFY] — Cox's non-enforcement of repeat infringer policy forfeited safe harbour)

**Valid DMCA takedown notice (512(c)(3)) must include:**

- Identification of the copyrighted work (or representative list for multiple works)
- Identification of the infringing material with sufficient information to locate it
- Contact information for the complaining party
- Good faith belief statement that the use is not authorised
- Accuracy statement under penalty of perjury
- Physical or electronic signature

**Counter-notification (512(g)) process:**

- User submits counter-notice with: identification of removed material, contact info,
  good faith belief of mistake or misidentification, consent to jurisdiction
- OSP must restore material in 10–14 business days unless copyright owner files suit
- Filing a knowingly false takedown notice creates liability (512(f))

**EU parallel — DSM Directive Article 17 (Upload Filters):**
Platforms that profit from hosting large volumes of user-generated content (OCSSPs) must:

- Obtain authorisation from rightsholders (licences), OR
- Demonstrate best efforts to obtain authorisation, absence of infringement, and expeditious
  removal of notified content
- Does not apply to non-profit encyclopaedias, open-source software platforms, small/micro
  platforms, or B2B cloud services
  [JURISDICTION-SPECIFIC — requires verification of national implementing legislation]

---

### §7. De Minimis Use

The de minimis doctrine holds that trivial copying that is both quantitatively and
qualitatively inconsequential does not constitute actionable infringement. The doctrine
is not expressly in the US Copyright Act but has long been recognised judicially.

**US standard:**

- Courts ask whether a reasonable person would consider the taking insignificant
- Newton v. Diamond, 388 F.3d 1189 (9th Cir. 2004) [VERIFY]: copying 3 notes from a
  flute composition held de minimis after filtering (note: the sound recording right in
  the _performance_ was at issue, not the musical composition)
- But: Ringgold v. Black Entertainment Television, Inc., 126 F.3d 70 (2d Cir. 1997)
  [VERIFY]: brief display of a quilt as set decoration for approximately 27 seconds (in
  non-sequential segments) held NOT de minimis — the quilt was recognisable
- Music sampling: Most circuits have moved away from a blanket "get a licence, pay a fee"
  rule; quantitative and qualitative triviality is assessed. However, a sample of the
  "heart" of a song (the distinctive hook) is rarely de minimis regardless of length.

**EU/UK:**

- There is no formal de minimis doctrine in EU copyright law. The CJEU in Pelham [VERIFY]
  held that even a 2-second sample is a reproduction of the phonogram. Member states
  may implement the parody/pastiche exception to address minor artistic uses.
- UK: CDPA s.16(3) requires a "substantial part" to be copied. Very minor takings may
  fail the substantiality threshold, but this is assessed qualitatively.

---

### §8. Independent Creation Defence

Independent creation is a complete defence to copyright infringement. Unlike patent
infringement, copyright infringement requires proof of actual copying — an author who
independently creates an identical work does not infringe.

**Elements of the defence:**

1. The defendant had no access to the original work, OR
2. The defendant accessed the original work but created the allegedly infringing work
   independently without copying

**Evidence supporting independent creation:**

- Creation timeline documentation (dated drafts, version control history, commit logs)
- Design documents, notes, or sketches predating any claimed access
- Evidence of independent sources or inspiration for the allegedly infringing work
- Testimony of witnesses who can attest to the creation process
- Expert evidence of the frequency of parallel independent creation in the relevant field
- Absence of any plausible access route (e.g., defendant's work pre-dates public release
  of the original)

**Subconscious copying risk:**
Unconscious copying of a work the defendant encountered and later forgot having seen can
constitute infringement (Bright Tunes Music Corp. v. Harrisongs Music, Ltd. [VERIFY]).
The defence requires that the creation was genuinely independent at the time of creation,
not merely that the defendant did not consciously intend to copy.

**Prior creation as affirmative evidence:**
If the defendant can prove the allegedly infringing work was created before the original
was published or disclosed, this is strong evidence of independent creation.

---

### §9. Other Defences

#### 9.1 Public Domain

A work in the public domain cannot be infringed. Verify copyright status using:

- **US**: Hirtle's chart for pre-1978 works (complex rules depending on publication date,
  notice, registration, and renewal); works published 2025 − 95 = 1930 or before are
  generally in the US public domain [VERIFY for edge cases]
- **EU/UK**: Life of author + 70 years from 1 January of the year following death [VERIFY]
- **US government works**: Federal government works (17 USC 105) are in the public domain
  upon creation; state government works are a different analysis [VERIFY]

**Caution:** A work in the public domain may still be covered by a newly created
derivative work copyright. For example, a 1900 novel is public domain, but a 2000 stage
adaptation is protected (only the adaptation's original elements are protected — not the
underlying novel).

#### 9.2 Licence (Express or Implied)

- **Express licence**: A written or oral agreement granting the right to use the work.
  Check scope, territory, duration, and permitted uses against the allegedly infringing use.
- **Implied licence**: Courts may find an implied licence where: (a) the plaintiff created
  the work at the defendant's request, (b) delivered the work to the defendant, and (c) the
  plaintiff's conduct indicated the defendant could copy and distribute the work.
- **Open source/Creative Commons**: Many works are available under open content licences.
  Verify: (a) whether the applicable licence conditions have been met (attribution,
  share-alike, non-commercial restrictions); (b) whether the use is within the licence scope.

#### 9.3 First Sale Doctrine / Distribution Exhaustion

- **US (17 USC 109)**: The owner of a lawfully made copy may resell or lend that specific
  copy without authorisation (first sale doctrine). Does NOT permit reproduction.
  Digital downloads are generally not covered — the doctrine applies to physical copies
  (Kirtsaeng v. John Wiley & Sons, Inc., 568 U.S. 519 (2013) [VERIFY] — extends to
  foreign-manufactured authorised copies)
- **EU**: Copyright exhaustion applies within the EU after a lawful first sale in the EU
  (Coditel v. Ciné Vog Films, C-262/81 [VERIFY]). For digital downloads: UsedSoft GmbH
  v. Oracle Int'l Corp., C-128/11 (CJEU 2012) [VERIFY] held resale of downloaded software
  licences is exhausted (Software Directive Art. 4(2))
- **UK**: Post-Brexit, UK exhaustion rules may diverge from EU; UK government consulted
  on exhaustion regime (UK+ exhaustion) — [JURISDICTION-SPECIFIC, verify current regime]

#### 9.4 Merger Doctrine

Where there is only one (or very few) ways to express an idea, the expression merges
with the idea and is not copyrightable. This is a copyrightability-limiting doctrine, not
technically a fair use defence, but it filters out unprotectable expression at the
copyrightability stage. Commonly applied to: legal forms with mandatory language, game
rules, standardised instructional language, simple geometric designs with no room for
variation.

---

### §10. Statutory Damages and Willfulness

#### 10.1 US Statutory Damages (17 USC 504)

| Category | Range per Work | Conditions                                                                               |
| -------- | -------------- | ---------------------------------------------------------------------------------------- |
| Regular  | $750 – $30,000 | Judge or jury discretion                                                                 |
| Willful  | Up to $150,000 | If plaintiff proves defendant knew or had reason to know of infringement                 |
| Innocent | As low as $200 | If defendant proves it was not aware and had no reason to believe the use was infringing |

**Registration prerequisite (17 USC 412):** Statutory damages and attorney's fees (17 USC 505) are **only available** if the copyright was registered with the US Copyright Office
either:

- Before the infringement commenced, OR
- Within 3 months of the work's first publication (and before the infringement)

Failure to register within these windows limits the plaintiff to actual damages only.

**Actual damages (17 USC 504(b)):** The copyright owner's actual losses PLUS any profits
of the infringer attributable to the infringement not already captured in the actual
losses calculation. The infringer bears the burden of proving deductible expenses.

#### 10.2 Willfulness Indicators

Strong willfulness evidence:

- Defendant received and ignored a DMCA takedown notice for this specific work
- Defendant received a cease-and-desist letter identifying the infringement and continued
- Internal documentation showing knowledge of the copyright claim
- Pattern of repeated infringement of the same work or owner's works
- Deliberate copying or near-wholesale reproduction of identifiable original expression
- Active concealment of the copying (e.g., altered attribution, removal of watermarks)

**Reckless disregard / wilful blindness** can also support a willfulness finding — a
defendant cannot avoid liability by deliberately ignoring obvious signs of infringement.

#### 10.3 EU / UK Damages

**EU (Enforcement Directive 2004/48/EC):**

- Damages based on: economic prejudice (lost profits, unfair profits of infringer), moral
  prejudice (damage to reputation, distress), and reasonable royalty as alternative measure
- Member states may implement additional measures including seizure and destruction
- Provisional measures and injunctions available

**UK (CDPA 1988):**

- s.97(1): Damages for infringement (compensatory, not punitive)
- s.97(2): **Additional damages** for flagrant infringement — courts may award damages
  having regard to the benefit derived by the defendant and the flagrancy of the infringement.
  This can have a punitive character in egregious cases.
- Account of profits (equitable remedy in lieu of damages)
- Delivery up (s.99) and order for destruction (s.114)

---

### §11. AI-Generated Content and Copyright

This is a rapidly evolving area. Apply all citations with particular care and verify
against current guidance.

#### 11.1 Copyrightability of AI-Generated Works

**US:** The Copyright Act protects only works of human authorship. The Copyright Office
has consistently refused registration for works generated autonomously by AI without
meaningful human creative control (see Copyright Office Guidance 2023; Thaler v. Vidal,
43 F.4th 1207 (Fed. Cir. 2022) [VERIFY] — same principle in patent context):

- Works generated solely by AI without human creative input: **not copyrightable**
- Works where human author makes meaningful creative choices (selection of AI-generated
  content, arrangement, editing, adding human expression): **registrable to the extent
  of human-authored elements**
- The "prompt alone" debate: the Copyright Office has generally found that prompting AI
  is more like giving instructions than creating original expression; registration is
  denied for purely AI-generated elements even with elaborate prompts

**EU/UK:** "Own intellectual creation" and similar standards require human authorship.
Purely AI-generated works without human creative choices are likely unprotectable.
UK uniquely has a "computer-generated works" provision (CDPA s.9(3)) protecting works
generated by computer where there is no human author — the "author" is the person who
made arrangements necessary for creation — but this predates modern generative AI and
its scope in this context is unsettled.

#### 11.2 AI Training Data

**US:** Whether training large language models and image generation models on copyrighted
works constitutes copyright infringement is actively litigated:

- Thomson Reuters Enterprise Centre GmbH v. ROSS Intelligence, Inc. (D. Del. 2025)
  [VERIFY]: copying of Westlaw headnotes for AI training held not fair use — commercial
  purpose, entire works copied, direct market substitution
- Ongoing: Getty Images v. Stability AI (D. Del.); Authors Guild v. OpenAI (S.D.N.Y.);
  multiple consolidated cases
- No definitive appellate or Supreme Court ruling as of the knowledge cutoff

**EU:** DSM Directive Article 4 allows text and data mining (TDM) for general purposes
but permits rightsholders to **opt out** via machine-readable means (e.g., `robots.txt`,
metadata reservations). If a rightsholder has opted out, training on their works is not
covered by the Art. 4 exception. Art. 3 TDM for research organisations has no opt-out.

**UK:** Exception for TDM for non-commercial research (s.29A CDPA, added 2014); broader
commercial TDM exceptions were proposed in 2023 consultation but not enacted as of
knowledge cutoff. [VERIFY current UK TDM position]

---

## Risk Classification

Classify the overall infringement risk using the five-tier system:

### CLEAR INFRINGEMENT — Act Immediately

Direct evidence of copying of protected expression; no viable defences identified or
defences are clearly insufficient; registration status supports maximum damages.

**Indicators:**

- Verbatim or near-verbatim reproduction of a substantial portion of protected expression
- No plausible fair use / fair dealing argument (commercial use, no transformation, market
  harm clear)
- Evidence of deliberate copying (access confirmed; no credible independent creation claim)
- DMCA safe harbour clearly unavailable (direct infringer, not platform)
- Willfulness indicators present

**Claimant actions**: Send cease-and-desist; prepare DMCA takedown; preserve evidence;
consult litigation counsel; consider emergency TRO or preliminary injunction if ongoing harm.
**Respondent actions**: Immediate cessation of use; engage IP counsel; assess exposure;
document all potential defences; consider licence negotiation.

### PROBABLE INFRINGEMENT — Strong Case, Seek Counsel

Substantial evidence of copying of protected expression; defences are present but weak;
overall balance of factors favours the copyright owner.

**Indicators:**

- Non-verbatim but clearly recognisable copying of the "heart" of the original
- Fair use factors predominantly weigh against the use
- Independent creation implausible given access and similarity
- DMCA safe harbour requirements not fully met

**Claimant actions**: Send cease-and-desist; assess litigation viability; consult counsel
on damages exposure and settlement range.
**Respondent actions**: Consult IP counsel urgently; assess strongest defences; consider
proactive licence negotiation to avoid litigation; do not continue infringing use.

### BORDERLINE — Genuine Contest; Counsel Required

Competing legal arguments on both sides; reasonable lawyers and judges could reach
different conclusions; outcome may depend on specific circuit/jurisdiction or trial facts.

**Indicators:**

- Similarity exists but defences (especially fair use) are genuinely arguable
- AWF v. Goldsmith-era ambiguity about transformative use
- De minimis argument not clearly foreclosed
- DMCA notice-and-takedown compliance questionable
- Jurisdiction-specific rules create divergent outcomes

**Claimant actions**: Obtain legal opinion before pursuing litigation; assess settlement
options; monitor defendant's conduct for willfulness signals.
**Respondent / Clearance actions**: Do not proceed with the use without qualified legal
advice; consider modifying the use to strengthen defences; document all clearance steps taken.

### PROBABLE DEFENSE — Likely Defensible, Some Risk Remains

Defences appear likely to prevail; some residual risk; responsible parties should document
the defence basis clearly.

**Indicators:**

- Fair use factors predominantly favour the use (transformative, non-commercial, no
  market substitution)
- Or: strong de minimis or independent creation defence
- Or: DMCA safe harbour conditions clearly met
- Or: public domain / licence confirmed

**Claimant actions**: Weak case; do not pursue litigation without reassessment; consider
whether any aspect of the use could be modified to eliminate even this residual risk.
**Respondent / Clearance actions**: Proceed with the use; document the defence basis
in writing; retain evidence of independent creation, transformative purpose, or licence;
monitor for any changed facts.

### CLEAR DEFENSE — No Infringement Risk

Strong, clear defences with minimal residual risk; the use is lawful on current facts.

**Indicators:**

- Work is in the public domain
- Express written licence covers the use
- No substantial similarity (taking is trivial, qualitatively minor)
- Fair use overwhelmingly favours the use (strong transformative, non-commercial,
  no market harm)
- Independent creation documented

**All perspectives**: Proceed; retain documentation. No action needed beyond maintaining
the evidence that supports the defence.

---

## Actionable Output Per Finding

For each infringement finding identified, deliver actionable output structured as:

```
**Finding ID**: [#]
**Element(s) taken**: [specific description of the allegedly copied elements]
**Protectable?**: [Yes / Partial / No]
**Substantial similarity**: [Yes / Arguably / No]
**Applicable defence(s)**: [Fair use / Fair dealing / DMCA / De minimis / Independent creation / Other]
**Defence strength**: [Strong / Moderate / Weak / Not applicable]
**Classification**: [CLEAR INFRINGEMENT → CLEAR DEFENSE]
**Confidence**: [Definite / High / Probable / Possible / Unlikely]
**Recommended action (Claimant)**: [specific action]
**Recommended action (Respondent)**: [specific action]
**Recommended action (Clearance)**: [specific action]
**Damages note**: [Registration status impact; estimated range if infringement found]
```

---

## Prioritization Framework

Organise findings and actions by urgency:

### Tier 1 — Immediate (Within Days)

Issues that require action before the situation worsens:

- CLEAR INFRINGEMENT with ongoing harm (e.g., still live on a platform, actively distributed)
- Imminent statute of limitations issue (US: 3-year limitations period for copyright
  infringement, 17 USC 507(b) [VERIFY])
- Emergency injunctive relief situations (irreparable harm from continued distribution)
- DMCA takedown responses due (platform restoring removed content after counter-notice)
- Active litigation deadline

**Action threshold**: Retain IP counsel; send cease-and-desist or respond to one; halt
infringing use; preserve all evidence; begin documentation of damages.

### Tier 2 — Near-Term (Within Weeks)

Issues requiring attention but not emergencies:

- PROBABLE INFRINGEMENT with quantifiable ongoing damages
- Registration decision: if infringement is recent, is there still time to register
  before the 3-month window closes to preserve statutory damages eligibility?
- Licence negotiation to resolve a PROBABLE INFRINGEMENT or BORDERLINE finding
- DMCA repeat infringer policy review (for platforms)
- Platform takedown notice preparation

**Action threshold**: Obtain legal opinion; quantify exposure; pursue licence or
settlement; evaluate registration status.

### Tier 3 — Monitor (Ongoing)

Background issues that do not require immediate action but should be tracked:

- BORDERLINE findings where the user intends to continue the use
- Evolving AI copyright law that may affect training data or AI-generated content
- Changes in the commercial landscape that could affect market harm analysis (new
  licensing options, new competing platforms)
- UK TDM law reform developments

**Action threshold**: Monitor case law developments; retain documentation; set a review
date to reassess if circumstances change.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                  | Fail Action                                              |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                                                                      | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent format recognisable for the jurisdiction (e.g., US: Reporter citations; EU: C-case numbers; UK: EWCA/UKSC/CDPA s.X) | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or repeal — especially for rapidly evolving areas (AI, DMCA, DSM implementation)                         | Flag "[CHECK CURRENCY]"                                  |
| **Domain**     | Analysis stays within the identified governing jurisdiction(s). No assumptions from other jurisdictions bleeding in                                   | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden. In copyright law, many issues are genuinely uncertain — be explicit about this                             | Add confidence qualifier                                 |

### Self-Interrogation for CLEAR INFRINGEMENT and CLEAR DEFENSE

For any finding classified at either extreme (CLEAR INFRINGEMENT or CLEAR DEFENSE),
apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity:**

- Does the risk classification follow logically from the cited authority?
- Would a court in this jurisdiction actually reach this conclusion on these specific facts?
- Is there a counter-argument that opposing counsel would immediately raise?

**Pass 2 — Completeness:**

- Has the applicable substantial similarity test been correctly identified for the work
  type and jurisdiction?
- Have all applicable defences been considered — not just the obvious ones?
- Has the registration status impact on remedies been correctly assessed?

**Pass 3 — Challenge:**

- What is the strongest argument for the opposite classification?
- Under what changed facts would this classification shift by one or two tiers?
- Is the extreme classification justified, or does the evidence support a more nuanced
  PROBABLE tier classification?

If any pass reveals a weakness, revise the classification before delivery. Record in the
Glass Box Audit Trail: `self_interrogation: "PASS"` or `self_interrogation: "REVISED —
[reason]"`.

### Confidence Scoring

Assign a confidence level to each material finding:

| Level        | Range     | Meaning                                                         | Action                                                  |
| ------------ | --------- | --------------------------------------------------------------- | ------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, directly on point authority                        | State with confidence                                   |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions                | State with brief caveat                                 |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ                | State with explicit reasoning and contra-indicators     |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing authorities (common in fair use) | Flag for counsel review with both sides of the argument |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                                         | Do not assert; flag "[UNCERTAIN — counsel to advise]"   |

---

## Glass Box Audit Trail

Every copyright infringement assessment MUST include a Glass Box Audit Trail at the end:

```yaml
glass_box:
  assessment_date: "[date]"
  original_work: "[title/description, type, author/owner]"
  allegedly_infringing_work: "[description, type, defendant]"
  assessing_party_role: "[Claimant / Respondent / Clearance / Neutral]"
  jurisdiction: "[US / EU / UK / Other]"
  work_type: "[Literary / Musical / Sound recording / Visual / Audiovisual / Software / Database / Other]"
  registration_status: "[Registered pre-infringement / Registered post-3mo window / Not registered / Unknown]"
  substantial_similarity_test_applied: "[9th Circuit Extrinsic/Intrinsic / 2d Circuit Ordinary Observer / AFC (software) / EU Essential Characteristics / UK Substantial Part]"
  defences_assessed:
    - "[Fair use / Fair dealing / EU exception — result]"
    - "[DMCA safe harbour — result]"
    - "[De minimis — result]"
    - "[Independent creation — result]"
    - "[Other — result]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-copyright-authority.md or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED or UNVERIFIED]"
  case_law_consulted:
    - "[Case, citation — VERIFIED or UNVERIFIED]"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED]"
  self_interrogation: "PASS / REVISED — [reason] / NOT APPLICABLE (no extreme classification)"
  overall_classification: "[CLEAR INFRINGEMENT / PROBABLE INFRINGEMENT / BORDERLINE / PROBABLE DEFENSE / CLEAR DEFENSE]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, jurisdiction gaps, missing evidence]"
  reviewer: "AI-assisted — requires qualified IP legal review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in copyright infringement assessment:

1. **Failing to filter unprotectable elements before comparing works** — The most common
   analytical error. A similarity analysis that includes ideas, facts, standard elements,
   or functional requirements will overstate infringement risk. Always apply
   Abstraction-Filtration (for software) or element filtering (for all work types) before
   the similarity comparison.

2. **Treating all copying as infringement** — Not all copying is copyright infringement.
   Copying of unprotectable elements (facts, ideas, scènes à faire, public domain
   material) is not infringement regardless of how much is taken. Identify _what_ was
   copied, not just _that_ it was copied.

3. **Treating "transformative" as a magic word** — Post-AWF v. Goldsmith (2023), calling
   a use "transformative" does not end the fair use analysis. A commercially competitive
   use in the same market as the original is not protected merely because it adds
   artistic or stylistic transformation. Always assess the _purpose and character_ in
   relation to the original's market purpose.

4. **Applying US fair use doctrine in EU or UK contexts** — The EU has no fair use
   doctrine. The UK has narrow fair dealing. A use that qualifies as transformative fair
   use under US law may still infringe under EU or UK law. Always apply jurisdiction-
   specific exceptions.

5. **Ignoring the registration timing requirement for statutory damages** — For US
   infringement, statutory damages and attorney's fees are entirely unavailable if
   registration is late. Failing to check registration timing before estimating damages
   exposure produces materially wrong outputs.

6. **Confusing the DMCA safe harbour with a general fair use defence** — The DMCA safe
   harbour (17 USC 512) is only available to qualifying _service providers_. A direct
   infringer (a person who themselves copies the work) cannot claim safe harbour. The
   safe harbour protects platforms from _their users'_ infringement, not from their own.

7. **Assuming de minimis always saves short uses** — The de minimis analysis is
   qualitative, not merely quantitative. Taking a 2-second sample of the most recognisable
   hook in a famous song is rarely de minimis. Always assess quality (was the "heart"
   taken?) not just quantity.

8. **Ignoring the "heart of the work" doctrine in sampling and quotation** — Both the US
   and UK courts assess whether the _qualitatively_ most significant part of the original
   was taken, not just the percentage. Taking the 300 most important words from a 200,000-
   word work can be more significant than taking 1,000 less distinctive words.

9. **Conflating copyright with trademark or trade dress** — A logo, product shape, or
   character name that is not copyrightable may still attract trademark or trade dress
   protection. Copyright infringement assessment should not attempt to address trademark
   claims — flag separately and note the different legal framework.

10. **Asserting a blanket independent creation defence without evidence** — The independent
    creation defence requires actual evidence of the creation process. Asserting "my
    client created this independently" without drafts, version history, or dated records
    is weak. In litigation, the defence must be substantiated.

11. **Overstating the DMCA counter-notification process as a resolution mechanism** —
    A DMCA counter-notice requires the user to accept jurisdiction of a US federal court.
    Submitting a counter-notice does not resolve the underlying infringement claim; it
    merely restores the content while the copyright owner decides whether to sue.

12. **Ignoring opt-out signals for EU TDM** — Under DSM Directive Art. 4, a rightsholder
    who has expressly reserved rights against TDM (via robots.txt, metadata, or other
    machine-readable means) has effectively opted out. Using such works for general
    commercial TDM is not covered by the Art. 4 exception.

13. **Treating AI-generated outputs as uncopyrightable without analysing human creative
    input** — The US Copyright Office approach is nuanced: elements reflecting human
    creative choices (selection, arrangement, editing) in an AI-assisted work may be
    registrable; purely AI-generated elements are not. Assess each element's origin.

14. **Skipping the market harm analysis in fair use** — Factor 4 (market effect) remains
    critical and is often the most fact-intensive. Failing to assess both the actual
    market harm and the potential licensing market produces incomplete fair use analysis.
    Even a non-commercial use can harm a licensing market if it forecloses the copyright
    owner's ability to licence that type of use.

15. **Assuming pre-1978 US works are in the public domain without verification** — US
    copyright duration for pre-1978 works is complex. Publication date, whether copyright
    notice was affixed, whether the work was registered, and whether the copyright was
    renewed all affect duration. Never assume; use Hirtle's chart or a copyright duration
    calculator for each specific work. [VERIFY]

16. **Presenting BORDERLINE findings with false certainty** — Copyright law, particularly
    fair use, is notoriously unpredictable. If the analysis is genuinely uncertain, say
    so explicitly. A confident CLEAR INFRINGEMENT classification on a borderline case may
    cause harm (unjustified takedowns, chilling of legitimate speech). Calibrate
    confidence scores carefully.

17. **Conflating the musical composition copyright with the sound recording copyright** —
    These are separate rights in the US (and EU). A sample may infringe the sound
    recording master (typically owned by a record label) without infringing the underlying
    musical composition (typically owned by a publisher/songwriter), or vice versa. Always
    identify both rights and both potential claimants in music cases.

---

## Writing Standards

Apply plain-language discipline to all output:

**For risk assessments and recommendations:**

- Active voice: "The fair use defence is weak" not "The fair use defence is considered to
  be weak given the circumstances"
- Specific, not vague: cite the relevant statute, case, or provision rather than saying
  "this may have enforceability issues"
- Name the risk concretely: state the damages range and the specific infringement scenario,
  not just "there is significant legal risk"
- Short sentences. One point per sentence.

**For legal citations:**

- Use standard citation format for the jurisdiction
- Mark all unverified citations [VERIFY]
- Date-stamp any recent case law — copyright law on AI, fair use, and platform liability
  has evolved rapidly and citations should be timestamped

**Quality gates before delivery:**

1. Can a non-lawyer business owner understand the classification and recommended action?
2. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
3. Has every applicable defence been addressed — not just fair use?
4. Is the confidence level honest — does it reflect genuine uncertainty where it exists?
5. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Step 3: Search for current text of applicable copyright statutes (17 USC, CDPA 1988,
  national implementation of InfoSoc Directive)
- Search for leading substantial similarity cases for the specific work type and circuit
- Search for current fair use cases in the relevant area (especially post-AWF v. Goldsmith)
- Search for DMCA safe harbour cases if platform liability is at issue
- Verify copyright duration for any work whose status may be in question
- Save results to `/tmp/legalcode-copyright-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box Audit Trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box Audit Trail: `legalcode_mcp: "Not connected"`
- Focus the analysis on structural risk assessment and flag that legal citations require
  independent verification before reliance
- Include a prominent notice at the top of the output that citations require verification

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Copyright Infringement Assessment

**Assessment Date**: [date]
**Assessing Party's Role**: [Claimant / Respondent / Clearance]
**Original Work**: [title, type, author/owner, registration number if known]
**Allegedly Infringing Work / Use**: [description, defendant, platform/distribution channel]
**Governing Jurisdiction(s)**: [US / EU / UK / Other]
**Assessment Basis**: [legalcode-mcp verified / General knowledge — all citations marked [VERIFY]]

---

### 1. Copyrightability and Protectable Expression

**Protected Elements Identified**: [Yes / Partial / Minimal]
**Originality Threshold**: [Met / Borderline / Not met]
**Unprotectable Elements Filtered**:

- [Element 1 — filtered as: idea / scènes à faire / merger / fact / public domain]
- [Element 2 — ...]

**Net protectable expression**: [Description of what remains after filtering]
**Registration Status**: [Registered [date] / Not registered / Unknown]
**Statutory Damages Eligible**: [Yes / No — [reason] / Unknown]

---

### 2. Substantial Similarity Analysis

**Test Applied**: [9th Cir. Extrinsic/Intrinsic / 2d Cir. Ordinary Observer / AFC (software) /
EU Essential Characteristics / UK Substantial Part]

| Element     | Original Expression | Allegedly Infringing Expression | Protectable? | Substantially Similar?         |
| ----------- | ------------------- | ------------------------------- | ------------ | ------------------------------ |
| [Element 1] | [Description]       | [Description]                   | Yes / No     | Yes / Probably / Possibly / No |
| [Element 2] | ...                 | ...                             | ...          | ...                            |

**Qualitative substantiality ("heart" of the work)**: [Was the most recognisable /
economically significant portion taken?]
**Access evidence**: [Confirmed / Probable / Unknown / No access possible]
**Overall finding**: [Clearly similar / Probably similar / Ambiguous / Not similar]
**Confidence**: [0.X — Definite / High / Probable / Possible / Unlikely]

---

### 3. Defence Analysis

#### 3.1 Fair Use / Fair Dealing / EU Exceptions

**[US] Fair Use Four-Factor Analysis (17 USC 107)**:

| Factor                        | Finding                                                        | Weight                                              |
| ----------------------------- | -------------------------------------------------------------- | --------------------------------------------------- |
| 1. Purpose and character      | [Commercial/non-commercial; transformative purpose assessment] | [Favours infringement / Neutral / Favours fair use] |
| 2. Nature of copyrighted work | [Creative/factual; published/unpublished]                      | [Favours infringement / Neutral / Favours fair use] |
| 3. Amount and substantiality  | [Quantity taken; heart of work?]                               | [Favours infringement / Neutral / Favours fair use] |
| 4. Market effect              | [Actual harm; licensing market impact]                         | [Favours infringement / Neutral / Favours fair use] |

**Overall Fair Use Assessment**: [Likely succeeds / Arguable / Likely fails]
**Confidence**: [X.X]

**[UK] Fair Dealing Analysis**: [Applicable section(s); fairness; source acknowledgment]
**[EU] Exception Analysis**: [Applicable article; three-step test compliance]

#### 3.2 Other Defences

| Defence                    | Applicable?           | Strength                   | Basis                                 |
| -------------------------- | --------------------- | -------------------------- | ------------------------------------- |
| DMCA Safe Harbour (512(c)) | [Yes / No / N/A]      | [Strong / Moderate / Weak] | [Key requirement met/unmet]           |
| De Minimis                 | [Yes / No]            | [Strong / Moderate / Weak] | [Quantitative/qualitative assessment] |
| Independent Creation       | [Yes / No / Possible] | [Strong / Moderate / Weak] | [Evidence available]                  |
| Licence / Permission       | [Yes / No]            | [Strong / N/A]             | [Express / Implied / Open source]     |
| Public Domain              | [Yes / No]            | [Strong / N/A]             | [Copyright duration; work type]       |
| Merger Doctrine            | [Yes / No]            | [Strong / Moderate / N/A]  | [Idea/expression merger]              |

---

### 4. Overall Risk Classification

**Classification**: [CLEAR INFRINGEMENT / PROBABLE INFRINGEMENT / BORDERLINE /
PROBABLE DEFENSE / CLEAR DEFENSE]
**Confidence**: [X.X] — [Definite / High / Probable / Possible / Unlikely]

**Rationale**: [2–3 sentence summary of the key factors driving the classification,
naming the most decisive legal issues]

---

### 5. Damages Exposure (if infringement likely)

| Category                    | Assessment                                           |
| --------------------------- | ---------------------------------------------------- |
| Statutory damages available | [Yes / No — [registration timing reason]]            |
| Estimated statutory range   | [$X–$Y per work / N/A]                               |
| Willfulness indicators      | [None identified / [list]]                           |
| Willful enhancement risk    | [Yes — up to $150,000 per work / No / Low]           |
| EU/UK additional damages    | [Flagrant infringement indicators: [list] / None]    |
| Actual damages estimate     | [Not assessable on current information / [estimate]] |

---

### 6. Recommended Actions

#### If Claimant

- **Immediate (Tier 1)**: [specific action]
- **Near-term (Tier 2)**: [specific action]
- **Strategic (Tier 3)**: [specific action]

#### If Respondent / Defendant

- **Immediate (Tier 1)**: [specific action]
- **Near-term (Tier 2)**: [specific action]
- **Strategic (Tier 3)**: [specific action]

#### If Clearance Assessment

- **Recommendation**: [Proceed / Proceed with modifications / Obtain licence / Avoid]
- **Conditions**: [What changes would reduce risk to an acceptable level]
- **Risk remaining after mitigation**: [assessment]

---

### Glass Box Audit Trail

[YAML block as specified in the Glass Box section above]
```

---

## Localization Notes

For jurisdictions outside US/EU/UK, adapt the assessment as follows:

1. **Confirm Berne Union membership**: Most jurisdictions are members; verify that
   automatic protection (no formalities required) applies.

2. **Research local fair dealing / exceptions**: Canada (Copyright Act, fair dealing
   for education/parody/satire since 2012); Australia (fair dealing under Copyright Act
   1968, enumerated purposes only); India (Section 52, fair dealing); Singapore (fair
   dealing with transformative use factors similar to US, Copyright Act 2021). [VERIFY all]

3. **Confirm copyright term**: Life + 70 years is common but not universal. Some
   jurisdictions retain life + 50 years. Some jurisdictions have special terms for
   anonymous works, works of applied art, or audiovisual works.

4. **Check moral rights**: Especially in civil law jurisdictions (France, Germany, Italy),
   moral rights (droit moral) are inalienable and imprescriptible — they survive the
   economic rights term and can generate separate infringement claims.

5. **Platform liability**: Jurisdictions outside the US do not have a direct equivalent
   to the DMCA safe harbour. Research local ISP liability frameworks (e.g., EU DSM
   Directive Art. 17; Canada's Notice-and-Notice regime; Australia's graduated response).

---

## Provenance

Created by Legalcode (2026-03-20). Legalcode original synthesis covering the US/EU/UK
copyright infringement assessment framework. Research sources: 17 USC (Copyright Act 1976,
including DMCA 1998 and MMA 2018); CDPA 1988 (as amended including ERRA 2013 s.30A);
EU InfoSoc Directive 2001/29/EC; DSM Directive 2019/790; Berne Convention 1886 (Paris Act
1971); US Copyright Office Circulars 1, 15a, 21, 22; EUIPO and UKIPO guidance; leading
case law including Feist (1991), Campbell v. Acuff-Rose (1994), Harper & Row (1985), AWF
v. Goldsmith (2023), Oracle v. Google (2021), Infopaq C-5/08, Pelham C-476/17, Designers
Guild [2000] UKHL 58; Viacom v. YouTube (2d Cir. 2012); Computer Associates v. Altai (2d
Cir. 1992); Thomson Reuters v. ROSS (D. Del. 2025). All citations should be independently
verified against authoritative legal databases before reliance.
