---
name: legalcode-workflow-compound
description: >
  Extract and store learnings from completed legal and knowledge work to make the next task
  easier. Use after completing any significant piece of legal work — transactions, litigation
  milestones, regulatory filings, contract negotiations, compliance audits, corporate governance
  actions — to capture patterns, create templates, update preferences, and compound institutional
  legal knowledge. Triggers on requests like 'that went well, let's capture what worked',
  'what did we learn from that deal/case/negotiation', 'that motion failed — let's analyze why',
  or after completing high-stakes legal work. Supports 11 insight types including 6 legal-specific
  types (precedent, clause-library, jurisdiction-note, regulatory-update, opposing-counsel-pattern,
  judge-pattern) with privilege-safe storage, ethical obligation compliance, and legal knowledge
  compounding across matters.
disable-model-invocation: true
---

# Legalcode Compound: Legal Knowledge Compounding Workflow

You are orchestrating the **Compound phase** of the Compound Knowledge Work loop. Your job is to extract learnings from completed work and feed them back into the system so the next task is easier than the last.

## Scope Boundary for Country Onboarding

This skill is primarily for compounding and status bookkeeping. It is **not** the end-to-end country execution workflow by itself.

- Use `country-law-caselaw-onboarding` (or equivalent onboarding execution skill) for full law + case-law implementation/execution.
- Use this skill to capture learnings and keep the country status matrix current while onboarding progresses.

> **Disclaimer**: This skill provides a framework for AI-assisted legal knowledge management
> and organizational learning. It does not constitute legal advice. All stored insights should
> be reviewed for accuracy and privilege compliance before being relied upon in future matters.
> Laws change; verify current applicability of any legal insight before relying on it. Statutory
> and case law references cited from memory carry hallucination risk — verify against
> authoritative sources before storing or relying on them. Never store attorney-client privileged
> communications, work product, or information that could waive privilege if disclosed.

**The magic is in the compounding.** Skip this phase and you're just working, not building.

## Philosophy

Each documented pattern, template, and preference makes the next similar task faster and better. First attempt at negotiating a multi-jurisdictional data processing agreement takes 40 hours of research, drafting, and negotiation. Document the approach — the clause formulations that survived pushback, the jurisdiction-specific requirements discovered, the opposing counsel patterns observed — and the next one takes 15 hours. That's compounding.

In legal practice, compounding is especially powerful because:

- **Precedent compounds**: Research done for one matter often applies to dozens of future matters in the same practice area or jurisdiction
- **Negotiation intelligence compounds**: Understanding opposing counsel's patterns, a particular judge's preferences, or a regulator's enforcement priorities applies across cases
- **Clause formulations compound**: A well-drafted indemnification clause that survived challenge in arbitration is worth more than any template — it's battle-tested
- **Risk assessment compounds**: Knowing which contract provisions actually caused disputes (and which never did) calibrates future risk analysis
- **Regulatory knowledge compounds**: Tracking enforcement actions, guidance documents, and audit findings builds a compliance intelligence layer that makes every future filing and audit smoother
- **Client relationship knowledge compounds**: Understanding each client's risk tolerance, communication preferences, and business objectives across matters builds a relationship intelligence layer that improves client satisfaction and retention
- **Procedural knowledge compounds**: Court-specific filing requirements, agency submission formats, and local rule nuances — once learned, these apply to every future matter in the same forum
- **Failure knowledge compounds most powerfully**: A missed deadline, a lost motion, a failed deal negotiation — these painful lessons, properly captured, prevent the same mistake from recurring across the entire practice

## Scope and Coverage

This skill applies to all types of legal work product and knowledge work. While the legal-specific enhancements focus on common practice areas, the compound workflow is equally applicable to:

- **Transactional work**: M&A, venture capital, debt financing, real estate transactions, joint ventures
- **Litigation**: Civil, commercial, IP, employment, class action, arbitration, regulatory enforcement
- **Regulatory and compliance**: Securities, banking, data privacy, environmental, healthcare, trade
- **Corporate governance**: Board advisory, fiduciary duty analysis, stockholder matters, entity management
- **Intellectual property**: Patent prosecution, trademark registration, copyright, trade secrets, licensing
- **Employment**: Executive compensation, restrictive covenants, workplace policies, immigration
- **Tax**: Planning, controversy, compliance, transfer pricing
- **Real estate**: Acquisitions, leasing, land use, environmental compliance, construction
- **General knowledge work**: Strategy, analysis, communication, decision-making, project management

## Privilege Preservation

**This section is non-negotiable. Every participant in the compound workflow must honor these rules.**

### What Must Never Be Stored

- Attorney-client privileged communications (advice given by counsel to client)
- Mental impressions, conclusions, opinions, or legal theories of an attorney (core work product)
- Client confidences and secrets not already in the public record
- Information that would identify a client without their consent (use anonymized references)
- Settlement negotiations or mediation communications protected by FRE 408 or equivalent rules
- Grand jury materials or sealed court records

### What Can Be Stored Safely

- General legal principles and their application (without client-specific context)
- Publicly available case law, statutes, and regulatory guidance
- Anonymized patterns observed across multiple matters (e.g., "in SaaS negotiations, data portability clauses are increasingly non-negotiable")
- Template language and clause formulations (stripped of client-identifying information)
- Procedural knowledge (court filing requirements, agency submission formats)
- Published enforcement actions and their implications
- Market-standard terms and negotiation ranges
- General observations about judicial or regulatory behavior based on public records

### Work Product Doctrine Considerations

Some insights may qualify as attorney work product (prepared in anticipation of litigation). When compounding work from litigation matters:

- Strip all litigation-specific strategy and mental impressions
- Retain only the procedural and generalizable legal knowledge
- Note in the insight metadata: `privilege-reviewed: true`
- When in doubt, do not store — ask the supervising attorney

### Client/Matter Anonymization Rules

When referencing specific matters in stored insights:

- Replace client names with generic descriptors: "a mid-market SaaS company" not "Acme Corp"
- Replace opposing party names: "the acquiring company" not "BigTech Inc."
- Replace specific deal values with ranges: "$10-50M transaction" not "$23.7M"
- Replace dates with approximate timeframes: "Q3 2025" not "September 14, 2025"
- Never include matter numbers, billing codes, or internal references

## Cross-Border and Multi-Jurisdictional Considerations

When compounding legal knowledge across jurisdictions, observe these additional principles:

- **Jurisdiction-tag every insight**: A legal pattern without a jurisdiction tag is unreliable. What is standard in one jurisdiction may be prohibited in another.
- **Note conflict-of-laws issues**: When insights span jurisdictions, note where the law differs and how conflict-of-laws principles would resolve the difference.
- **Track regulatory divergence**: Different jurisdictions often implement similar regulations differently (e.g., GDPR implementation varies across EU member states). Note these divergences in jurisdiction-note insights.
- **Distinguish binding from persuasive authority**: A precedent that is binding in one jurisdiction may be only persuasive in another. Always note the authority level.
- **Monitor legal harmonization trends**: Some legal areas are converging across jurisdictions (e.g., data privacy, anti-corruption). Others are diverging (e.g., non-compete enforceability, AI regulation). Note these trends in regulatory-update insights.
- **Consider cultural and practical differences**: Beyond the black letter law, jurisdictions differ in litigation culture, regulatory enforcement intensity, negotiation norms, and judicial behavior. These practical differences are as important as statutory differences.
- **Language considerations**: When compounding knowledge from non-English jurisdictions, note whether the insight is based on the original language text or a translation, and flag any terms where translation may lose legal precision.

## Ethical Obligations

### Duty of Competence (ABA Model Rule 1.1)

Knowledge management is a component of competence. A lawyer who fails to capture and maintain institutional knowledge risks:

- Repeating research unnecessarily (inefficiency that may be passed to clients)
- Missing relevant precedent discovered in prior matters
- Failing to identify conflicts or related matters
- Losing institutional knowledge when team members depart

The compound workflow directly supports the duty of competence by ensuring that legal knowledge is preserved, organized, and retrievable.

### Duty of Diligence (ABA Model Rule 1.3)

Diligent representation includes learning from past failures. The failure analysis component of this workflow ensures that missed deadlines, evidentiary gaps, procedural missteps, and other failures are analyzed and prevented from recurring.

### Duty of Communication (ABA Model Rule 1.4)

Client communication preferences captured through the preference learner support consistent, client-appropriate communication. Understanding how a particular client or matter type requires information to be presented improves the quality of representation.

### Malpractice Prevention

The compound workflow serves as a malpractice prevention tool by:

- Documenting what went wrong and systemic fixes to prevent recurrence
- Creating checklists from past failures (deadline management, conflict checks, filing requirements)
- Building institutional knowledge that survives attorney turnover
- Identifying patterns that indicate elevated malpractice risk

### Supervision Obligations (ABA Model Rules 5.1, 5.3)

Stored patterns, templates, and checklists support supervisory obligations by providing junior lawyers and non-lawyer staff with structured guidance that embodies the firm's quality standards and accumulated expertise.

## Process

### Phase 0: Country Matrix Sync (Required for Country Onboarding Tasks)

For any country onboarding task (laws, case law, guidance, tax/trade/labour), you must read and update the repository's country onboarding matrix files when they are present.

Look for:

- Primary country matrix at the repository root.
- Mirror under the ingest documentation tree, typically `apps/ingest/docs/country-onboarding/`.

Rules:

1. **At task start for a country**, set `Status` to `IN PROGRESS` for that row.
2. **During execution**, update `Remaining` as each modality is completed (law, case-law, guidance, tax, trade, labour).
3. **At completion**, set `Status` to `COMPLETE` only when the requested scope for that country is implemented, ingested/upserted, and manually validated.
4. Keep `Vetted` aligned with completion reality (`confirmed` only when validation is done).
5. If work is partial or blocked, keep `Status = IN PROGRESS` and record the unresolved items in `Remaining`.
6. Treat this matrix as the ingest-order control file and source of truth for sequencing/prioritization.

### Phase 1: Parallel Analysis

Launch these research agents in parallel:

1. **Pattern Extractor** — Analyze the completed work and conversation history:
   - What approach was taken?
   - What worked well? What didn't?
   - What would you do differently next time?
   - What frameworks or structures proved effective?
   - **Legal-specific**: What negotiation positions held or were conceded? What motion strategies succeeded? What compliance approaches passed audit? What clause formulations survived challenge? What judicial patterns were observed? What legislative interpretation approaches prevailed?

2. **Template Assessor** — Evaluate if this work could serve as a model:
   - Is this output reusable as a template?
   - What parts are situation-specific vs. generalizable?
   - How would you parameterize this for future use?
   - **Legal-specific**: Can this be added to the clause library? Does this memo structure work as a template for the practice area? Can the court filing format be reused? Does the corporate resolution template need updating?

3. **Preference Detector** — Capture user preferences revealed:
   - What formatting or style preferences emerged?
   - What level of detail does the user prefer?
   - What communication style resonates?
   - What frameworks does the user gravitate toward?
   - **Legal-specific**: Drafting style (plain language vs. traditional legalese)? Negotiation approach (aggressive vs. collaborative)? Client communication preferences (detail level, frequency, format)? Jurisdiction preferences (choice of law, forum selection)? Risk tolerance calibration (conservative vs. aggressive on ambiguous questions)?

4. **Failure Analyzer** (if things didn't go well):
   - What went wrong and why?
   - Was it execution, planning, or assumptions?
   - What early warning signs were missed?
   - What would prevent this next time?
   - **Legal-specific**: What arguments failed and why? What evidentiary gaps existed? What procedural missteps occurred? What deal-breaker issues emerged? What compliance gaps were found? What malpractice risks were identified? What ethical obligation issues arose?

5. **Knowledge Curator** — Organize and index all insights:
   - How should each insight be categorized and tagged?
   - What existing knowledge does this connect to?
   - What search terms will surface this insight in the future?
   - **Legal-specific**: Is precedent still good law? Has the regulation changed since this insight was captured? Does this clause formulation reflect current market standards? Is the jurisdictional analysis still accurate? Has the judge or opposing counsel's pattern evolved?

### Phase 2: Produce Discrete Insights

From the analysis, produce **individual, self-contained insights**. Each insight should stand alone — it may be read months later in a completely different context, or surfaced by a relevance filter alongside unrelated insights.

Every task should produce at least one insight. Most will produce 2-5. Complex legal matters may produce 10+. Each insight gets its own type:

#### Standard Insight Types

| Insight Type | What It Captures | Example |
|-------------|-----------------|---------|
| `pattern` | An approach that worked or didn't | "Pre-mortem before board presentations surfaces risks the team glosses over" |
| `template` | A reusable structure for future work | A generalized board update template with section placeholders |
| `preference` | A user style/tone/detail preference | "Prefers bullet points over prose in executive summaries" |
| `failure` | What went wrong and how to prevent it | "Announcing reorgs by email before 1:1s caused trust damage" |
| `insight` | A non-obvious learning or connection | "Investors respond better when bad news is framed as decisions, not problems" |

#### Legal-Specific Insight Types

| Insight Type | What It Captures | Example |
|-------------|-----------------|---------|
| `precedent` | A case, statute, or regulatory decision that proved relevant — with full citation, jurisdiction, holding, and applicability notes | "*Waymo LLC v. Uber Techs., Inc.*, N.D. Cal. 2017 — trade secret misappropriation claim survived summary judgment where plaintiff demonstrated inevitable disclosure; relevant when drafting non-compete/NDA provisions for departing employees in technology sector" |
| `clause-library` | A contract clause or provision that worked well — with markup showing negotiable vs non-negotiable portions | "Limitation of liability clause with carve-outs for IP indemnification and data breach — **non-negotiable**: uncapped for willful misconduct and IP infringement; **negotiable**: cap multiplier (1x-3x annual fees) for general liability" |
| `jurisdiction-note` | A jurisdiction-specific nuance that matters — differences in law between jurisdictions that affected outcome | "California's statutory prohibition on non-compete agreements (Cal. Bus. & Prof. Code 16600) means garden leave provisions must substitute for post-employment restrictive covenants; Delaware approach to same issue differs materially" |
| `regulatory-update` | A regulatory change or enforcement action that affected the work | "SEC Final Rule on cybersecurity incident reporting (July 2023) requires 8-K filing within 4 business days of materiality determination — affects incident response playbook timing and board notification templates" |
| `opposing-counsel-pattern` | Patterns observed in opposing counsel's approach, arguments, or negotiation tactics | "Firm X consistently leads with aggressive IP indemnification demands as an anchor, then concedes to market standard when met with reasoned pushback citing comparable deals — don't over-concede on first pass" |
| `judge-pattern` | Patterns observed in a particular judge's rulings, preferences, or procedural requirements | "Judge Y in S.D.N.Y. consistently enforces page limits strictly, requires joint discovery plans before initial conference, and has ruled against boilerplate 'irreparable harm' assertions in TRO motions three times in the last two years — need specific harm showing with declarations" |

**Insight Format:**

```markdown
---
type: [pattern | template | preference | failure | insight | precedent | clause-library | jurisdiction-note | regulatory-update | opposing-counsel-pattern | judge-pattern]
date: [YYYY-MM-DD]
category: [communication | decision | analysis | meeting | coaching | operations | contract | litigation | regulatory | corporate | ip | employment | data-privacy | tax | real-estate]
task: [Brief description of the original task]
outcome: [success | partial | failure]
jurisdiction: [Jurisdiction tag if applicable — e.g., US-CA, US-DE, UK, EU, DE, FR, ES, SG]
practice-area: [contract-negotiation | m-and-a | litigation | regulatory-compliance | corporate-governance | ip-prosecution | employment | data-privacy | tax | real-estate | arbitration | antitrust | securities | banking | insolvency]
court-tribunal: [Court or tribunal if applicable — e.g., SDNY, Del-Ch, ICC, LCIA, AAA]
statute-regulation: [Relevant statute or regulation if applicable — e.g., GDPR-Art-28, UCC-2-207, DTSA, SOX-302]
privilege-reviewed: [true | false — whether this insight has been reviewed for privilege compliance]
tags: [comma-separated: anonymized matter descriptors, frameworks, topics, practice areas, jurisdictions]
takeaway: [One sentence - the key thing to remember. This is what gets searched.]
---

# [Descriptive Title]

## Context
[2-3 sentences: What task this came from, what the situation was. Anonymized — no client names, matter numbers, or privileged information.]

## The Learning
[The actual insight, pattern, template, preference, or failure analysis. Self-contained - a reader should understand this without seeing anything else.]

## Jurisdiction Applicability
[If legal-specific: which jurisdictions this applies to, and any known variations. If a precedent, note whether it is binding or persuasive authority in relevant jurisdictions.]

## When to Apply
[Specific situations where this insight is relevant. Be concrete.]

## Limitations and Caveats
[When this insight does NOT apply. Jurisdictional limitations. Time-sensitivity of the legal analysis. Whether the underlying law has changed or is likely to change.]

## Related
[References to related insights by filename, if any]
```

**Keep each insight focused.** One pattern per file, one preference per file, one template per file. If a task yielded a good pattern AND a template AND a preference, that's three separate insight files. This granularity is what makes retrieval work.

**For legal insights specifically:**
- One precedent per file (even if you discovered five relevant cases — each gets its own insight)
- One clause formulation per file (even if you refined three clauses — each gets its own entry)
- One jurisdictional note per file (even if you discovered differences across four jurisdictions — each comparison gets its own file)

### Phase 3: Store and Index

Insights must be stored so the **Research phase can find them quickly** by category, keyword, tag, jurisdiction, practice area, or court. This is how the loop closes.

1. **Save each insight** to a category subdirectory under `.context/learnings/`:
   - Path: `.context/learnings/[category]/YYYY-MM-DD-[type]-[brief-description].md`
   - **General categories**: `communication/`, `decision/`, `analysis/`, `meeting/`, `coaching/`, `operations/`
   - **Legal-specific categories**: `contract/`, `litigation/`, `regulatory/`, `corporate/`, `ip/`, `employment/`, `data-privacy/`, `tax/`, `real-estate/`
   - Create the directory if it doesn't exist
   - Use descriptive filenames that are greppable (e.g., `2026-02-12-precedent-trade-secret-inevitable-disclosure.md`, `2026-02-12-clause-library-lol-cap-ip-carveout.md`, `2026-02-12-jurisdiction-note-ca-noncompete-prohibition.md`)

2. **Update the learnings index** at `.context/learnings/INDEX.md`:
   - Add a row per insight with all searchable fields
   - Create the index with the table header if it doesn't exist

   Index format:
   ```markdown
   # Learnings Index

   | Date | Type | Category | Title | Outcome | Jurisdiction | Practice Area | Tags | Takeaway | File |
   |------|------|----------|-------|---------|--------------|---------------|------|----------|------|
   | 2026-02-12 | precedent | litigation | Trade secret inevitable disclosure doctrine | success | US-CA | litigation | trade-secret, non-compete, employee-departure, technology | Waymo v. Uber inevitable disclosure analysis survives summary judgment — cite when drafting NDA enforcement strategy | litigation/2026-02-12-precedent-trade-secret-inevitable-disclosure.md |
   | 2026-02-12 | clause-library | contract | LOL cap with IP indemnification carve-out | success | jurisdiction-agnostic | contract-negotiation | limitation-of-liability, ip-indemnification, saas, enterprise | Uncapped IP indemnification carve-out with 2x cap for general liability — survived pushback in 3 enterprise SaaS negotiations | contract/2026-02-12-clause-library-lol-cap-ip-carveout.md |
   | 2026-02-12 | pattern | decision | Pre-mortem for board decisions | success | — | corporate-governance | board, pre-mortem, risk | Pre-mortem surfaces risks the team glosses over in optimistic planning | decision/2026-02-12-pattern-premortem-board.md |
   ```

   The Research phase searches this index by: type, category, jurisdiction, practice area, tags, and full-text grep across the Takeaway column. **Every field matters for retrieval.**

3. **Tag deliberately.** Tags should include:

   **General tags:**
   - People/stakeholders involved (anonymized — e.g., `board`, `investors`, `outside-counsel`)
   - Frameworks used (e.g., `SPADE`, `pre-mortem`, `IRAC`, `CREAC`)
   - Topic area (e.g., `pricing`, `hiring`, `product-launch`)
   - Anything you'd search for when facing a similar task

   **Legal-specific tags:**
   - **Jurisdiction tags**: `US`, `US-CA`, `US-DE`, `US-NY`, `UK`, `EU`, `DE`, `FR`, `ES`, `SG`, `AU`, `CA-ON`, etc.
   - **Practice area tags**: `m-and-a`, `venture-capital`, `ip-licensing`, `employment`, `data-privacy`, `securities`, `antitrust`, `real-estate`, `tax`, `insolvency`, `arbitration`, `regulatory-compliance`
   - **Client/matter tags (anonymized)**: `series-b-saas-company`, `mid-market-acquisition`, `fintech-regulatory-filing` — never use actual client or matter names
   - **Opposing party tags (anonymized)**: `big-four-firm`, `boutique-ip-firm`, `in-house-tech-team` — patterns about opposing counsel or parties, anonymized
   - **Court/tribunal tags**: `sdny`, `del-ch`, `ndcal`, `icc`, `lcia`, `aaa`, `icsid`, `cas`
   - **Statute/regulation tags**: `gdpr`, `ccpa`, `dtsa`, `utsa`, `ucc`, `sox`, `fcpa`, `uk-bribery-act`, `securities-act-1933`, `exchange-act-1934`, `ai-act`
   - **Document type tags**: `nda`, `spa`, `sha`, `loi`, `term-sheet`, `employment-agreement`, `ip-assignment`, `dpa`, `msa`, `sow`, `board-resolution`

### Phase 4: Optional Enhancement

Based on what was learned, suggest improvements to the system:

- **New agent needed?** If a gap in review coverage was found (e.g., no one was checking compliance with a new regulation)
- **Agent update needed?** If an existing agent missed something it should catch (e.g., the contract review agent didn't flag a jurisdiction-specific issue)
- **Workflow improvement?** If the plan-work-review-compound flow could be better
- **Clause library update needed?** If a standard clause formulation proved inadequate or a better formulation was discovered
- **Precedent database update needed?** If a key case was overruled, distinguished, or a new case changed the analysis
- **Regulatory tracker update needed?** If a new regulation, enforcement action, or guidance document affects stored insights
- **Template update needed?** If a template needs updating to reflect new legal requirements or market standards
- **Checklist update needed?** If a failure revealed a missing step in an existing checklist

Present these suggestions to the user for approval.

## Legal Knowledge Compounding Examples

### Example 1: Contract Negotiation Compounding

**First negotiation of a SaaS enterprise agreement** (estimated: 60 hours)
- Research standard market terms from scratch
- Draft initial positions without precedent
- Negotiate without understanding opposing counsel patterns
- No clause library to draw from

**Insights captured after the first negotiation:**
- `clause-library`: Limitation of liability with IP carve-out that survived pushback
- `clause-library`: Data processing addendum tailored to GDPR and CCPA dual compliance
- `opposing-counsel-pattern`: Major law firm X anchors aggressively on IP indemnification but concedes to market standard
- `preference`: Client prefers redline comparison format with risk scoring for each change
- `pattern`: Leading with "mutual most-favored-nation" framing accelerated agreement on key commercial terms
- `jurisdiction-note`: California law requires express opt-out of implied warranty of merchantability under UCC 2-316

**Second negotiation of a similar SaaS agreement** (estimated: 25 hours)
- Pull relevant clause library entries — start from battle-tested language
- Apply opposing counsel patterns — don't over-concede on IP indemnification anchor
- Use preferred redline format — client satisfaction from day one
- Apply jurisdiction-specific knowledge — no re-research needed

**Fifth negotiation** (estimated: 12 hours)
- Comprehensive clause library covers 90% of provisions
- Pattern database covers most counterparty negotiation styles
- Jurisdiction matrix covers common governing law choices
- Focus time on genuinely novel issues only

### Example 2: Litigation Pattern Compounding

**First trade secret misappropriation case:**
- `precedent`: Five key cases on inevitable disclosure doctrine, annotated with holdings and limitations
- `judge-pattern`: Assigned judge requires specific harm declarations for TRO motions
- `pattern`: Early forensic imaging of departing employee devices proved critical to evidence preservation
- `failure`: Delayed sending litigation hold notice led to spoliation argument from opposing counsel
- `template`: Litigation hold notice template with device-specific preservation instructions

**Second trade secret case (different client, different jurisdiction):**
- Pull precedent database — three of five cases still good law; two need updating
- Apply forensic imaging pattern immediately — no evidence preservation mistakes
- Use litigation hold template — no delay this time
- Adapt judge-pattern analysis for new judge (different preferences, but the research framework carries over)

### Example 3: Regulatory Compliance Compounding

**First GDPR compliance audit:**
- `regulatory-update`: Latest DPA enforcement guidance on consent mechanisms
- `template`: Data processing agreement template meeting Article 28 requirements
- `pattern`: Starting with data mapping before policy review saved 30% of audit time
- `jurisdiction-note`: German DPA interpretation of "legitimate interest" is narrower than Irish DPA
- `failure`: Missed vendor sub-processor chain — standard audit checklist didn't cover fourth-party processors

**Subsequent compliance audits:**
- Updated checklist includes sub-processor chain review
- DPA template reflects latest enforcement guidance
- Jurisdiction-specific notes prevent incorrect assumptions about "legitimate interest"
- Data mapping approach applied first — consistent efficiency gains

### Example 4: Corporate Governance Compounding

**First board consent action for a portfolio company:**
- `template`: Written consent template with proper authorization language
- `pattern`: Secretary's certificate format that satisfies lender requirements
- `jurisdiction-note`: Delaware DGCL 141(f) allows written consent in lieu of meeting — but charter must not prohibit it
- `preference`: Board prefers consent actions circulated with a one-page "action summary" explaining the business context
- `failure`: Initial consent lacked unanimous signature — one director's electronic signature was insufficient under the company's bylaws

**Subsequent consent actions:**
- Template includes signature format guidance aligned with bylaws
- Action summary format standardized to board's preferred style
- Charter and bylaw review automated into the consent preparation checklist
- Secretary's certificate reflects lender's specific requirements

### Example 5: Employment Agreement Compounding

**First executive employment agreement in a new jurisdiction:**
- `jurisdiction-note`: Non-compete enforceability varies dramatically — California prohibits, Massachusetts requires garden leave, Delaware allows with reasonable scope
- `clause-library`: Inventions assignment clause with adequate consideration and state-specific carve-outs
- `pattern`: Starting with the restrictive covenant analysis before drafting saves time — no point drafting unenforceable provisions
- `regulatory-update`: FTC non-compete rule (even if stayed) signals trend toward federal restriction — include sunset clause
- `preference`: HR prefers employment agreements that can be explained to candidates in plain language

**Subsequent employment agreements:**
- Jurisdiction matrix instantly identifies enforceable restrictive covenant structures
- Inventions assignment clause library provides state-specific alternatives
- Regulatory tracker flags pending changes that may affect restrictive covenants
- Plain-language summaries prepared alongside legal documents per HR preference

## Compounding Principles

### Compound Everything Worth Repeating
- If you might do something similar again, compound it
- Even partial successes have valuable patterns
- Failures are the most valuable compounding opportunities
- **Legal-specific**: Every matter produces reusable knowledge — even routine contracts yield clause formulations, jurisdiction notes, and preference data

### Be Honest About Failures
- Don't sugarcoat what went wrong
- Root cause matters more than symptoms
- Prevention > cure
- **Legal-specific**: Malpractice prevention requires honest analysis of near-misses, not just actual failures. A deadline almost missed is as important to document as a deadline actually missed.

### Keep It Retrievable
- Descriptive filenames, deliberate tags, and one-sentence takeaways are what make retrieval work
- Cross-reference related insights in the "Related" section
- The index is sacred — keep it updated
- **Legal-specific**: Jurisdiction tags, practice area tags, court tags, and statute tags are critical for legal retrieval. A litigation insight without a jurisdiction tag is nearly useless.

### One Insight Per File
- Granular insights are findable; monolithic documents are not
- A pattern, a template, and a preference from the same task are three separate files
- Each file should be self-contained: readable without context
- **Legal-specific**: One precedent per file, one clause per file, one jurisdictional note per file. A "summary of everything we learned from the Jones deal" is useless for retrieval.

### Preferences Are Insights
- Style, tone, and detail preferences are project-scoped, not universal
- Store them as `preference` type insights alongside patterns and templates
- **Legal-specific**: Client preferences for communication style, risk tolerance, and drafting conventions are critical institutional knowledge that should survive attorney transitions

### Templates Compound Fastest
- A good template saves the most time on repeat tasks
- Store as `template` type insights with the generalized template in the body
- Include usage notes and "When to Apply" guidance
- **Legal-specific**: Clause libraries compound even faster than full templates — a battle-tested indemnification clause is the single highest-value unit of compounded legal knowledge

### Precedent Compounds Deepest
- Legal research compounds in ways that general knowledge work does not
- A well-annotated case that was researched for one matter may be cited in dozens of future matters
- Keep precedent insights current — note when cases are overruled, distinguished, or superseded by statute
- Cross-reference related precedents to build a case law map over time

### Privilege Is Non-Negotiable
- Never store privileged communications, regardless of how valuable the insight
- When in doubt, anonymize further or don't store
- Privilege review should be a required step before any insight from a client matter is stored
- Mark all stored insights with `privilege-reviewed: true` only after review

## When to Compound

| Situation | Compound? | Focus On |
|-----------|-----------|----------|
| Completed high-stakes work | Always | Full analysis — patterns, templates, preferences |
| Work received positive feedback | Yes | What worked, template creation |
| Work received negative feedback | Absolutely | Failure insights, prevention |
| Routine work done well | Sometimes | Efficiency patterns |
| New type of work attempted | Yes | Approach and framework learnings |
| Discovered user preference | Yes | Preference insight |
| **Completed a contract negotiation** | **Always** | **Clause formulations, opposing counsel patterns, jurisdiction notes, negotiation patterns** |
| **Completed a litigation milestone** | **Always** | **Precedent, judge patterns, motion strategies, evidentiary lessons** |
| **Completed a regulatory filing or audit** | **Always** | **Regulatory updates, compliance patterns, template updates, enforcement trend analysis** |
| **Received a court ruling** | **Always** | **Precedent analysis, judge pattern update, procedural lessons** |
| **Deal closed or fell through** | **Always** | **Full deal post-mortem — what worked, what failed, what to replicate or avoid** |
| **New regulation or enforcement action** | **Yes** | **Regulatory update insight, affected template review, compliance checklist update** |
| **Attorney departure or transition** | **Yes** | **Knowledge capture — ensure institutional knowledge is documented before it walks out the door** |
| **Malpractice near-miss** | **Absolutely** | **Failure analysis, systemic fix, checklist update, training need identification** |

## Insight Quality Standards

### What Makes a High-Quality Legal Insight

Every stored insight should meet these minimum quality standards before entering the knowledge base:

| Criterion | Minimum Standard | Gold Standard |
|-----------|-----------------|---------------|
| **Self-contained** | Readable without any other context | Reader could apply the insight to a new matter without additional research |
| **Anonymized** | No client names, matter numbers, or deal values | Impossible to identify the source matter even with effort |
| **Jurisdiction-tagged** | At least one jurisdiction tag | All applicable jurisdictions noted with variation descriptions |
| **Practice-area-tagged** | At least one practice area tag | All applicable practice areas noted |
| **Privilege-reviewed** | Marked `privilege-reviewed: true` | Reviewed by supervising attorney |
| **Actionable** | Contains a clear "when to apply" section | Contains specific trigger conditions, application guidance, and caveats |
| **Current** | Reflects law as of the stated date | Includes currency decay notes and review-by date |
| **Sourced** | States the authority level (primary, secondary, practical) | Includes full citations for all legal authorities |

### What Disqualifies an Insight

An insight should NOT be stored if any of the following are true:

- It contains attorney-client privileged communications
- It contains core work product (mental impressions, legal theories of counsel)
- It can be used to identify a specific client or matter
- It is based on authority that has been overruled, superseded, or withdrawn
- It is so generic that it provides no actionable guidance (e.g., "contracts should be reviewed carefully")
- It duplicates an existing insight without adding new information
- It has not been privilege-reviewed

### Insight Lifecycle

Every insight has a lifecycle. Not all insights remain valuable forever.

```
Created -> Active -> Review Needed -> Updated OR Superseded OR Archived
```

1. **Created**: New insight enters the knowledge base with `CURRENT` status
2. **Active**: Insight is used in subsequent matters, gaining validation
3. **Review Needed**: Time-based or event-based trigger indicates review is needed
4. **Updated**: Insight is confirmed current or modified to reflect changes
5. **Superseded**: A new insight replaces this one (link the new one, mark the old one)
6. **Archived**: Insight is no longer relevant but retained for historical reference

### Review Triggers

These events should trigger review of related stored insights:

| Event | Review Scope |
|-------|-------------|
| New case decided in relevant jurisdiction | Precedent database, litigation patterns |
| Statute amended or new regulation effective | Regulatory tracker, clause library, compliance templates |
| Major enforcement action | Regulatory tracker, compliance patterns |
| Significant negotiation outcome | Clause library, opposing counsel patterns, negotiation patterns |
| Court ruling affecting stored judge pattern | Judge pattern database |
| Attorney departure | Matter knowledge base — capture institutional knowledge |
| New practice area entered | CLE tracker, competence gap assessment |
| Malpractice claim or near-miss | Failure database, checklists, process knowledge |

## Next Step

The loop is complete. For your next task, start again with: **`/coworkpowers:workflow-research`**

## Anti-Patterns to Avoid

- Skipping compound because "we're too busy" (this is how knowledge debt accumulates)
- Compounding only successes (failures are more valuable)
- Creating insights that are too generic to be actionable
- Not indexing or tagging (unfindable knowledge is useless)
- Putting multiple learnings in one file (breaks retrieval granularity)
- Over-documenting routine work
- Forgetting to check existing learnings before starting new work
- **Storing privileged information** (privilege waiver risk — never store attorney-client communications or core work product)
- **Failing to anonymize** (storing client names, matter numbers, or deal values in insights)
- **Not updating precedent** (a stored case that has been overruled is worse than no case at all — it's misinformation)
- **Ignoring jurisdiction specificity** (a pattern that works in Delaware may fail in California — always tag jurisdiction)
- **Conflating what the law says with what the law should say** (store the law as it is, note policy arguments separately)
- **Storing insights without privilege review** (every insight from a client matter must be reviewed for privilege before storage)
- **Not capturing regulatory changes** (a stored template that doesn't reflect a regulatory update can cause compliance failures)
- **Skipping the compound phase after failures** (failures in legal work — lost motions, failed deals, compliance violations — are the highest-value compounding opportunities)
