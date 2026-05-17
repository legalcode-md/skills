---
name: legalcode-saas-agreement-drafter
description: >
  Draft and review SaaS/cloud service agreements from both vendor and customer perspectives —
  generate clause-by-clause guidance, flag market deviations, and produce auditable dual-perspective
  analysis with confidence-scored redlines. Use when negotiating SaaS terms, drafting customer-facing
  service agreements, building vendor playbooks, managing SaaS compliance obligations (GDPR, CCPA,
  SOC 2, HIPAA BAA), assessing SaaS-specific risk allocation, reviewing subscription mechanics,
  SLA uptime commitments, data processing obligations, AI training restrictions, data portability,
  or exit assistance terms. Covers B2B, B2C, and B2B2C models. Jurisdiction-agnostic with
  localization markers for US, EU, UK, and AU. Produces structured guidance with Glass Box audit trail.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode SaaS Agreement Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted SaaS agreement drafting and
> review. It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. Laws change; verify current
> applicability before relying on any provision described here. SaaS-specific regulatory requirements
> (GDPR, CCPA, HIPAA, EU Data Act, NIS2, auto-renewal statutes) evolve rapidly — verify compliance
> obligations against current regulatory guidance before finalizing agreements. Statutory and case law
> references cited from memory carry hallucination risk — verify against authoritative sources before
> relying on them. Compliance certifications described (SOC 2, ISO 27001) reflect general industry
> standards — verify the specific vendor's current certification scope and audit period before relying
> on any certification claim.

---

## Purpose and Scope

This skill drafts and reviews SaaS/cloud service agreements that allocate commercial, operational,
and compliance risk between the vendor/platform and the customer. It provides clause-by-clause
guidance from **both vendor and customer perspectives**, identifies deviations from market standards
or organizational playbooks, and surfaces SaaS-specific issues: subscription mechanics, uptime
metrics, data processing obligations, AI training restrictions, compliance certifications, data
portability, and exit assistance.

**Covers:**
- SaaS Master Service Agreements (B2B enterprise, B2B SMB/scale, B2C consumer, B2B2C platform)
- Subscription and consumption-based pricing with tiered seats, usage limits, true-ups, and overages
- Service Level Agreements: uptime metrics, measurement methodology, credit structures, and exclusions
- Data processing and security obligations: encryption standards, SOC 2/ISO 27001, penetration testing, breach notification timelines
- Intellectual property: platform IP ownership, customer data rights, AI-generated output ownership, AI training restrictions
- Acceptable Use Policy: SaaS-specific abuse vectors, enforcement rights, suspension mechanics
- Data portability and exit assistance: export formats, migration timelines, post-termination retention, destruction certification
- SaaS-specific liability caps: data loss, security breach, API failures, and service interruption carveouts
- Auto-renewal and termination mechanics: notice periods, pricing change notifications, seat reduction rights
- Change management: feature deprecation, API versioning, breaking changes, platform migrations
- Compliance addenda: GDPR DPA, CCPA service provider terms, HIPAA BAA, NIS2 supply chain obligations
- Consumer protection compliance: jurisdiction-specific auto-renewal laws, unfair terms analysis (B2C)
- Dual-perspective analysis: vendor-favorable vs. customer-favorable positions, with redlines for each side
- Quality-verified output with Glass Box audit trail and confidence scoring

**Does not:**
- Draft on-premises or perpetual software licenses (see `software-license-agreement`)
- Review non-SaaS commercial agreements clause-by-clause (see `legalcode-contract-review`)
- Replace specialized legal counsel for HIPAA BAA, sector-specific SaaS regulation (FERPA, GLBA, FedRAMP), or complex data localization arrangements
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers throughout

**Related skills**:
- `legalcode-contract-review` — clause-by-clause review of any commercial agreement
- `legalcode-dpa-review-and-negotiation` — specialized DPA clause analysis under GDPR/UK GDPR/CCPA/LGPD
- `legalcode-nda-triage` — for screening standalone NDAs embedded in or ancillary to SaaS agreements
- `legalcode-contract-risk-scorer` — quantified risk scoring of final SaaS agreement terms

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The SaaS agreement's own governing law clause determines
which legal framework applies. The drafting process identifies the governing law early and adapts
the analysis accordingly.

[JURISDICTION-SPECIFIC] When localizing, research and apply:
- **Data protection regime**: GDPR + SCCs (EU/EEA), UK GDPR + UK IDTA (UK), CCPA/CPRA service provider terms (US/California), PIPEDA/Law 25 (Canada/Quebec), LGPD (Brazil), PDPA (Singapore/Thailand), Privacy Act + APPs (AU)
- **Cloud switching and portability**: EU Data Act (Regulation 2023/2854, fully applicable September 12, 2025) — mandatory switching rights, 30-day porting window, no switching fees from January 2027
- **SaaS characterization**: UCC Article 2 applicability (US — courts split; most treat SaaS as services, not goods), UCITA (Virginia and Maryland only [VERIFY])
- **Limitation of liability**: UCTA 1977 reasonableness test (UK B2B), Consumer Rights Act 2015 (UK B2C), ACL unfair terms regime + civil penalties from November 2023 (AU), statutory unconscionability (US states)
- **Consumer protection for auto-renewal**: California B&P Code §§17600-17606 (amended effective July 1, 2025), New York GBL §527-A (amended effective November 5, 2025), FTC Click-to-Cancel Rule (vacated by Eighth Circuit July 8, 2025 — state laws unaffected), EU Unfair Contract Terms Directive 93/13/EEC (B2C), ACL (AU B2C and small business from November 2023)
- **IP ownership defaults**: work-for-hire (US), moral rights (EU/UK — not waivable in all circumstances), output ownership under AI Act (EU — emerging)
- **Warranty disclaimer enforceability**: conspicuous form requirement for UCC §2-316 disclaimer (if UCC applies), CRA implied performance standard (UK), ACL consumer guarantees (AU — cannot be excluded for consumers)
- **NIS2 security obligations**: applies to SaaS providers qualifying as cloud computing digital service providers with EU operations (Directive 2022/2555, fully applicable October 2024)
- **DSA transparency reporting**: applies to SaaS hosting services with EU presence, VLOPs at 45M+ EU monthly active users face enhanced obligations
- **Audit rights and confidentiality**: SOC 2 Type II report access, ISO 27001 certification verification, penetration testing report disclosure standards
- **HIPAA BAA**: mandatory for US SaaS vendors processing electronic protected health information on behalf of covered entities (45 CFR §164.504(e))
- **Penalty/liquidated damages enforceability**: service credit enforceability as liquidated damages vs. penalties (jurisdiction-dependent)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming the
user's perspective or context, the workflow pauses and asks when:

- The answer changes which side's position to analyze (vendor vs. customer)
- The business model (B2B, B2C, B2B2C) affects term negotiation strategy or compliance obligations
- Regulatory context (GDPR, HIPAA, CCPA) changes mandatory clause requirements
- Risk tolerance or deal stage determines whether to flag an issue as negotiable or deal-blocking
- Deal context (strategic relationship, commodity vendor, startup) affects negotiation posture
- Specific SaaS model (multi-tenant, single-tenant, hybrid) affects data isolation and security clauses

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

Accept one of these inputs:
- **Existing SaaS agreement** (PDF, DOCX, URL, or pasted text) for review, analysis, and redlines
- **Drafting request** ("Draft vendor-side SaaS MSA for B2B enterprise" or "Draft customer-friendly SaaS subscription terms")
- **Clause request** ("Draft an SLA with 99.9% uptime and tiered service credits")
- **Playbook review** ("Does our standard SaaS template protect us against EU Data Act obligations?")

If no input is provided, prompt the user to supply one.

### Step 2: Gather Perspective and Business Context

**⟁ CLARIFY** — Before beginning, ask:

1. **Which side are you on?**
   - Options: SaaS Vendor / Platform, Customer / Buyer, Both (analyzing for alignment or benchmarking)
   - *Why this matters*: Vendor and customer positions on liability caps, uptime commitments, audit rights,
     AI training restrictions, and IP ownership are fundamentally opposed. The entire analysis flips.

2. **Business model?**
   - Options: B2B Enterprise (negotiated terms), B2B SMB / Scale (standard form), B2C Consumer (regulated), B2B2C Platform (intermediary liability), Hybrid
   - *Why this matters*: B2C requires consumer protection compliance (auto-renewal, cancellation rights,
     unfair terms review); B2B2C adds downstream customer liability; enterprise B2B allows more negotiation.

3. **Regulatory scope?**
   - Options: GDPR (EU/EEA customers), UK GDPR, CCPA/CPRA (US/California), HIPAA BAA (health data),
     PIPEDA / Quebec Law 25 (Canada), Australian Privacy Act, NIS2 (EU cloud provider obligations), None / Not yet assessed
   - Allow multiple. *Why this matters*: Determines whether DPA / BAA addendum is required, data localization
     constraints, breach notification timelines, audit rights, and sub-processor controls.

4. **Focus areas?** (allow multiple)
   - Options: Subscription pricing / true-ups, SLA / uptime, Data security / breach notification,
     AI training restrictions, Data portability / exit, Liability caps / indemnification,
     Compliance certifications (SOC 2, ISO 27001), Auto-renewal / termination, Change management,
     No specific focus — full review
   - *Why this matters*: Allows analysis to lead with what the user cares about most.

5. **Deal context?**
   - Free text with examples: "Strategic 5-year partnership," "$2M ARR enterprise deal — vendor has leverage,"
     "SMB standard-form contract — no negotiation expected," "Startup vendor — no SOC 2 yet"
   - *Why this matters*: Deal size, strategic importance, and negotiation leverage determine how hard to push
     on each issue and what to concede.

If partial context is provided, proceed with stated assumptions: "I'm assuming vendor-side, B2B enterprise,
GDPR and CCPA scope. Let me know if that's wrong and I'll re-run the analysis."

### Step 3: Load Playbook or Market Standards

Check for an organizational SaaS agreement playbook in local settings (e.g., `legal.local.md`).

The playbook should define:
- **Standard positions**: Preferred terms per clause (uptime commitment, liability cap formula, audit rights scope)
- **Acceptable ranges**: Terms that can be agreed without escalation (uptime 99.5%-99.99%, cap 6-24 months of fees)
- **Escalation triggers**: Terms requiring senior sign-off (uncapped liability, exclusivity grants, AI training on customer data, DPA carveouts)
- **Deal workflow**: Routing by deal size or risk level

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user and ask which approach:
- **Option A: Set up playbook now** — Define standard positions for 8 key SaaS clauses (uptime target, liability cap formula, data security requirements, DPA / BAA scope, payment terms, term length, auto-renewal notice, AI training prohibition). More precise outputs; 10-15 minutes upfront.
- **Option B: Proceed with B2B SaaS market standards** — Use widely-accepted enterprise SaaS market positions (99.9% uptime, 12-month liability cap, annual-fee-only for data breach carveout, standard DPA terms). Faster; may not reflect organizational preferences.
- **Option C: Provide positions as we go** — Start the draft and I'll ask about your preferred position when it matters for each clause.

Label all output: "Based on [organizational playbook / B2B SaaS market standards]."

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the governing law (from the agreement or the user's drafting intent). Then use
**legalcode-mcp** to build a working legal reference for this analysis.

**⟁ CLARIFY** — If any of the following apply, ask the user:
- No governing law clause found in a reviewed agreement → flag as RED and ask which jurisdiction applies
- Multiple conflicting governing law references → ask which governs the main body
- Unusual jurisdiction for the deal type → confirm intentional

**With legalcode-mcp connected (preferred):**
Search for jurisdiction-relevant authority covering:
- Data protection statutes and mandatory DPA terms (GDPR Art. 28, CCPA Cal. Code Regs. §7051, HIPAA 45 CFR §164.504(e))
- EU Data Act portability and switching obligations (Regulation 2023/2854 Arts. 23-31)
- Auto-renewal notice requirements (California B&P §17600-17606, NY GBL §527-A, applicable state law)
- Limitation of liability enforceability (UCTA s.11 UK, ACL unfair terms AU, US Uniform Commercial Code §2-719 if applicable)
- SaaS warranty disclaimer requirements (conspicuous form, UCC §2-316, CRA UK)
- NIS2 cloud provider obligations (Directive 2022/2555 Annex I/II classification thresholds)
- Consumer protection mandatory terms that cannot be excluded by agreement
- Penalty / liquidated damages enforceability for SLA service credits
- AI training restrictions and output ownership (emerging: EU AI Act, CJEU pending cases)

Save results to `/tmp/legalcode-saas-authority.md`. Mark legalcode-mcp-sourced citations as VERIFIED in Glass Box.

**Without legalcode-mcp:**
- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `external_tools_used: "None — manual verification required"`

[JURISDICTION-SPECIFIC] For each governing law, the research should cover at minimum:
- Mandatory data protection terms that cannot be excluded by agreement
- Limitation of liability enforceability tests and caps
- Consumer protection / unfair terms rules (B2C or qualifying small business scope)
- Auto-renewal notification requirements and click-to-cancel obligations
- Data portability / switching obligations (EU Data Act if EU customers)

### Step 5: Dual-Perspective Clause Analysis — All 15 Topic Areas

Read the entire agreement before flagging issues — clauses interact. For example, a very low
liability cap combined with SLA credits as the "sole remedy" may leave customers with no effective
recourse for a major outage. Review holistically first, then clause-by-clause.

Analyze systematically across all 15 SaaS-specific topic areas (see **SaaS Clause Architecture**
section below). For each area, assess:

| Criterion | What to Evaluate |
|-----------|-----------------|
| **Presence** | Is this topic covered in the agreement? Missing entirely? Addressed in a schedule or addendum? |
| **Perspective** | Does current language favor vendor, customer, or is it balanced? |
| **Market deviation** | How far is this from B2B SaaS market standard? |
| **Classification** | GREEN (acceptable), YELLOW (negotiate), RED (escalate) |
| **Compliance gap** | Does this clause create or cure a regulatory obligation? |

For each topic area, produce both a **vendor-side assessment** and a **customer-side assessment**,
noting where positions diverge.

**⟁ CLARIFY** — For complex agreements (25+ pages, multiple schedules, or incorporated DPA/BAA/AUP):
- Ask whether to perform full analysis (all 15 topic areas) or priority review (user's focus areas + all RED items)
- If the agreement incorporates documents by reference (e.g., "Vendor's DPA at [URL]"), ask whether to include those

### Step 6: Missing Clause and Gap Detection

After analyzing clauses present, identify material topics entirely absent from the agreement.

**Common SaaS missing-clause issues:**

| Missing Clause | Customer Risk | Vendor Risk | Classification |
|---------------|---------------|-------------|----------------|
| No SLA / uptime commitment | No remedy for downtime | None | RED (customer), GREEN (vendor) |
| No DPA when GDPR/CCPA data is processed | Regulatory fine, no sub-processor control | Regulatory fine | RED (both) |
| No AI training restriction | Customer data used to train vendor's models | None | RED (customer) or YELLOW depending on sensitivity |
| No data portability / exit assistance | Vendor lock-in; data loss risk at exit | None | RED (customer), YELLOW (vendor if EU Data Act applies) |
| No HIPAA BAA for health data | Criminal HIPAA liability | Criminal HIPAA liability | RED (both if ePHI processed) |
| No destruction certificate | Cannot evidence data deletion | None | YELLOW–RED (customer) |
| No API deprecation notice period | Breaking changes without warning | Operational burden | YELLOW (customer) |
| No uptime measurement methodology | SLA unenforceable | Disputes over availability | YELLOW (both) |
| No seat reduction / downgrade rights | Locked into unused seats | Revenue certainty | YELLOW (customer), GREEN (vendor) |
| No auto-renewal notice obligation | Consumer law risk if B2C | None | RED (B2C), YELLOW (B2B with CA/NY customers) |

**⟁ CLARIFY** — When missing clause severity depends on context:
- "This agreement has no SLA. Is the vendor offering 'managed service' or 'best-efforts access'? If managed service, this is RED."
- "No data portability clause. Is customer data critical to exit? If yes, RED. If ephemeral, acceptable."
- "No AI training restriction. Does the vendor's platform use ML features that might train on customer content?"

### Step 7: Flag Deviations Using Three-Tier Classification

For each deviation from playbook or market standard, classify using the **Deviation Severity Classification** below. For each:

- **GREEN**: Note for awareness; no action required.
- **YELLOW**: Generate specific redline language with fallback position; estimate business impact of accepting vs. negotiating.
- **RED**: Explain the specific risk (with legal basis where verifiable), provide market-standard alternative language, estimate exposure, recommend escalation path.

**⟁ CLARIFY** — For borderline classifications:
- **YELLOW vs. RED**: "This liability cap is set at 3 months' fees. Market standard is 12 months. Should I classify as YELLOW (negotiate) or RED (escalate)? Depends on your risk tolerance for this deal."
- **GREEN vs. YELLOW**: "The auto-renewal notice period is 15 days. For an enterprise customer in New York, the legal minimum is 15-45 days. At exactly 15 days this may be technically compliant but leaves no buffer. Is this a concern?"
- **Risk tolerance check**: If multiple items trend in the same direction, ask whether to apply conservative (flag more) or pragmatic (flag only material items) classification.

### Step 8: Generate Guidance with Redlines

For each YELLOW and RED deviation, generate guidance using the **Redline Format** below.
Before generating redlines:

**⟁ CLARIFY** — Ask about negotiation posture if not already clear:
- **Relationship dynamic**: New vendor relationship, existing strategic partner, or must-have platform with leverage? Affects tone.
- **Volume of redlines**: If many YELLOW items exist: "I've found [N] items worth negotiating. Do you want guidance on all of them, or focus on the top [X] highest-impact?"

### Step 9: Perspective-Flip Analysis

For each material clause (YELLOW/RED), include a parallel analysis for the opposing perspective:

- **Vendor-side analysis**: Include "Customer will likely push back on this because..." section
- **Customer-side analysis**: Include "Vendor will typically resist this because..."
- **Both-sides analysis**: Present positions side-by-side

This prevents the common failure of preparing a negotiation position without understanding the counterparty's legitimate concerns.

### Step 10: SaaS-Specific Risk Scoring

For each material clause, assign a four-dimensional risk score:

| Dimension | High | Medium | Low |
|-----------|------|--------|-----|
| **Business impact** | Catastrophic loss potential (data breach, platform unavailability, revenue loss) | Moderate financial exposure | Minor inconvenience |
| **Enforceability risk** | Clause likely unenforceable under governing law | Contested enforceability | Well-established, enforceable |
| **Negotiation difficulty** | Counterparty historically won't move | Some flexibility expected | Typically negotiable |
| **Compliance risk** | Creates regulatory obligation vendor/customer cannot meet | Compliance gap that can be remediated | No compliance exposure |

### Step 11: Business Impact and Negotiation Strategy

Provide a summary covering:
- **Overall risk profile**: High-level SaaS-specific risk assessment across data security, compliance, exit, pricing escalation, and operational risk dimensions
- **Top 3-5 issues**: Most important items, with severity, perspective (vendor/customer/both), and legal basis
- **Negotiation sequencing**: Which issues to lead with, what to concede, how to trade-link (e.g., accept lower uptime SLA in exchange for uncapped data-breach indemnity)
- **Timeline considerations**: Urgency factors (go-live date, competitive pressure, contract expiry)
- **EU Data Act notice** (if EU customers): Flag whether the agreement embeds the mandatory switching rights from Regulation 2023/2854

**⟁ CLARIFY** — If deal context unclear:
- "Can you walk away from this deal, or is this platform essential?" — Determines whether strategy is assertive or accommodating.
- "Who signs off internally? Legal only, or also product / finance / executive?" — Determines how to frame escalation recommendations.

### Step 12: Quality Verification

Before delivery, run all quality checks (see **Quality Assurance Framework** section):

1. **Citation Quality Gates** (5 gates): Run silently. Revise any failures before delivery.
2. **Self-Interrogation** (3 passes): For every RED item, apply the 3-pass adversarial review. Revise if any pass reveals weaknesses.
3. **Confidence Scoring**: Assign confidence level to each material clause analysis.
4. **Completeness check**: Confirm all 15 SaaS topic areas have been addressed (present or flagged absent).
5. **Dual-perspective validation**: Confirm each material clause includes guidance for both sides.
6. **Regulatory compliance flag**: Cross-reference against applicable regulatory requirements (GDPR, CCPA, HIPAA).
7. **Glass Box Audit Trail**: Generate YAML and append to output.

### Step 13: Regulatory Compliance Flag (if applicable)

If GDPR, CCPA, HIPAA, NIS2, or other compliance obligations were identified in Step 2:
- Cross-reference relevant agreement provisions against the compliance checklists in **Jurisdiction-Specific Compliance Obligations** section
- Flag missing or inadequate compliance provisions with [COMPLIANCE-REQUIRED]
- Recommend specific addenda (DPA, BAA, Data Security Addendum, NIS2 supply chain clause)
- Assign RED classification to any unmet mandatory obligation

### Step 14: Delivery and Routing

Structure output per **Output Format Template** below. Route based on risk level:

| Risk Level | Recommended Action |
|---|---|
| All GREEN | Approve and proceed to signature; no negotiation needed |
| YELLOW items only | Flag for internal discussion; prepare negotiation talking points; legal review within 1-2 business days |
| Any RED items | Escalate to senior counsel; prepare counterproposal; external counsel may be needed |
| Regulatory gap (COMPLIANCE-REQUIRED) | Do not execute until gap remediated regardless of other risk levels |

---

## SaaS Clause Architecture — 15 Topic Areas

Analyze the SaaS agreement systematically across these 15 topic areas. Use **Deep** tier for the
most material and commercially contested clauses; **Standard** tier for important but less contested
provisions.

| # | Topic Area | Depth | Vendor Focal Points | Customer Focal Points |
|---|------------|-------|--------------------|-----------------------|
| 1 | **Subscription Terms** | Deep | Seat floors, true-up triggers, overage definitions, add-on pricing, volume discount protection | Seat reduction rights, downgrade paths, true-up frequency, overage caps, pricing change notice |
| 2 | **Service Level Agreement** | Deep | Uptime definition (monthly vs. annual), excluded downtime categories, credit as sole remedy, cap on credits | Uptime commitment level (target: 99.9%+), measurement methodology, credit formula, cash refunds, termination right for sustained outages |
| 3 | **Data Security and Processing** | Deep | Reasonable efforts standard, certification scope, audit rights limitation, breach notification period | Specific encryption standards (AES-256, TLS 1.2+), SOC 2 Type II report access, penetration testing scope, 72h breach notification, sub-processor controls |
| 4 | **Intellectual Property** | Deep | Vendor retains all platform IP; broad right to use aggregated data; output ownership ambiguity | Customer owns all input data and outputs; AI training prohibition; no vendor rights to customer data beyond service delivery |
| 5 | **AI Training Restrictions** | Deep | Right to use data for model improvement; opt-out option; aggregated / anonymized carveout | Explicit prohibition on training, fine-tuning, distillation; includes aggregated/anonymized outputs; no downstream use by vendor's AI suppliers |
| 6 | **Acceptable Use Policy** | Deep | Broad AUP terms; unilateral enforcement rights; suspension without notice; content moderation discretion | Objective AUP standards; notice-before-suspension obligation; appeal / cure period; no liability for user-generated content beyond knowledge threshold |
| 7 | **Data Portability and Exit Assistance** | Deep | No affirmative portability obligation; charge for data export; format at vendor's discretion | Machine-readable export format; 30-day post-termination data access; migration assistance; destruction certificate; EU Data Act compliance if applicable |
| 8 | **Liability Caps and Exclusions** | Deep | Low cap (3-6 months fees); broad consequential damages exclusion; credits as sole SLA remedy | 12-month cap minimum; carveouts for data breach, IP indemnification, fraud; consequential damages carveout for data loss; uncapped willful misconduct |
| 9 | **Indemnification** | Deep | Narrow indemnification scope; carve-outs for customer modifications; cross-indemnity for customer's infringement | Vendor indemnifies for platform IP claims; data-breach indemnity; vendor-caused compliance failures; customer indemnifies for misuse |
| 10 | **Auto-Renewal and Termination** | Standard | Auto-renewal default with short notice window; no mid-term cancellation; termination fees for early exit | 60-day auto-renewal notice; no fees for non-renewal; termination for convenience (30-90 days); termination for cause (material breach + cure period); termination right for sustained SLA failure |
| 11 | **Change Management** | Standard | Unilateral right to modify features, pricing, and API; reasonable notice; no compensation for breaking changes | Material change notice (90+ days); API deprecation notice (minimum 6 months); no unilateral price increase during committed term; termination right for material adverse changes |
| 12 | **Payment Terms and Pricing** | Standard | Annual subscription pre-paid; no refunds; interest on late payments; price escalation right on renewal | Monthly or quarterly billing; disputed invoice process; CPI-cap on renewal increases; pro-rata refunds for early termination; no retroactive price changes |
| 13 | **Compliance Certifications and Audit Rights** | Standard | SOC 2 Type I report only; audit by questionnaire or inspection of report; 30-day advance notice for on-site audit | SOC 2 Type II (annual audit report); ISO 27001; annual penetration test with summary report access; right to conduct or commission audit with reasonable notice |
| 14 | **Governing Law, Disputes, and Notices** | Standard | Vendor's jurisdiction; binding arbitration; class action waiver; attorneys' fees waiver | Neutral jurisdiction; litigation option for injunctive relief; class action right preserved (B2C); jury trial right in contested jurisdictions |
| 15 | **Representations, Warranties, and Disclaimers** | Standard | "As is" disclaimer; no implied warranties; narrow uptime warranty (already covered by SLA); no fitness for purpose | Warranty that platform complies with applicable law; SOC 2 / ISO 27001 compliance warranty; security posture warranty; warranty survival on termination |

---

## Deviation Severity Classification

### GREEN — Acceptable

The clause is within market-standard range or within the organizational playbook's acceptable zone.
No redline needed. Note for awareness only.

**All of the following must be true:**
- Clause is present and unambiguous
- Clause falls within the playbook's acceptable range or B2B SaaS market standard
- Clause presents no material compliance risk
- Clause does not create obligations the party cannot fulfill

### YELLOW — Negotiate

The clause deviates from market standard or organizational playbook in a material way, but the
risk is manageable and the clause is typically negotiable.

**Any of the following triggers YELLOW:**
- Liability cap below 12 months of annual fees (customer-side) or customer demands above 2x ARR (vendor-side)
- SLA uptime below 99.5% without justification, or uptime calculation on an annual (not monthly) basis
- Consequential damages exclusion without any carveout for data loss
- AI training restriction absent when vendor uses ML features that interact with customer data
- Auto-renewal notice period shorter than 30 days for B2B, or 45 days for applicable US states (CA, NY)
- Data portability period shorter than 30 days post-termination, or export format underdefined
- Audit rights limited to questionnaire only (no right to SOC 2 Type II report)
- Unilateral modification rights with fewer than 30 days' notice for material feature changes
- Governing law in a jurisdiction that significantly disadvantages one party without business reason
- Sub-processor list not maintained or no approval process for material new sub-processors

### RED — Escalate

The clause presents a material legal, financial, or compliance risk that cannot be accepted without
senior legal sign-off. Do not proceed to signature until addressed.

**Any of the following triggers RED:**
- No liability limitation at all, creating unlimited exposure (vendor-side)
- Liability cap below 1 month of fees, or sole remedy for data breach is SLA credit (customer-side)
- No DPA executed or DPA terms missing mandatory elements (GDPR Art. 28, CCPA Cal. Code Regs. §7051) when personal data is processed
- No HIPAA BAA when vendor processes electronic protected health information on behalf of a covered entity
- Vendor claims broad rights to use customer data for AI model training with no restriction or opt-out
- No governing law clause (creates enforcement uncertainty)
- Change management terms allow unilateral elimination of material features without notice or termination right
- Automatic assignment of IP created using customer data to vendor without customer consent
- Outright exclusion of all liability for data breaches (enforcement risk: void under UCTA s.2 UK, ACL AU, potentially unconscionable under US law)
- EU-customer agreement that does not embed mandatory EU Data Act switching rights (if applicable to covered services — Regulation 2023/2854, applicable September 12, 2025)
- Auto-renewal clause for B2C SaaS that does not comply with mandatory consumer protection law in applicable jurisdiction

### [COMPLIANCE-REQUIRED] — Regulatory Gap

A mandatory regulatory obligation (GDPR, CCPA, HIPAA, NIS2) is unmet. This is not negotiable —
execution of the agreement in this state creates legal liability for one or both parties. The
compliance gap must be remediated before signature regardless of other risk levels.

---

## SaaS Clause Depth Analysis

### 1. Subscription Terms

**Key drafting issues:**

*True-up Mechanics:*
- Define the true-up measurement period (annual, semi-annual, or monthly)
- Specify whether overages are billed at list price or at the contracted volume discount
- Include a reconciliation process for disputed true-up calculations
- Vendor-side: seek contractual minimum seats / minimum annual commitment
- Customer-side: negotiate cap on overage rate (e.g., "not to exceed X% above contracted per-seat rate") and a downgrade path after each contract year

*Seat and Usage Definitions:*
- Define "active user" or "seat" precisely to prevent disputes about named vs. concurrent users
- Specify how usage is measured for consumption-based models (API calls, data volume, compute hours)
- Address multi-tenant / shared accounts (family plans, department licenses)

*Pricing Changes:*
- Vendor-side: seek right to increase pricing on renewal with reasonable notice (e.g., 90 days; cap at CPI + X%)
- Customer-side: lock pricing for the committed term; require advance notice of renewal pricing before auto-renewal deadline; cap renewal increases at CPI or X% per year

*Common YELLOW Issues:*
- True-up at list price (not contracted rate): vendor charges overages at full list price even when committed volume qualifies for discount. Customer-side redline: "Overage pricing shall not exceed [contracted per-seat rate] × 1.1."
- No downgrade path: customer is locked into initial seat count for the entire term even if user count decreases. Customer-side redline: "Customer may reduce authorized users at each annual renewal with 90 days' notice."

### 2. Service Level Agreement

**Key drafting issues:**

*Uptime Commitment and Measurement Methodology:*

Industry standard uptime metrics and downtime equivalents:

| Uptime | Downtime/Year | Downtime/Month | Tier |
|--------|--------------|----------------|------|
| 99.0% | 87.6 hours | 7.3 hours | Basic |
| 99.5% | 43.8 hours | 3.65 hours | Standard |
| 99.9% | 8.76 hours | 43.8 minutes | Enterprise minimum |
| 99.95% | 4.38 hours | 21.9 minutes | High-availability |
| 99.99% | 52.6 minutes | 4.38 minutes | Mission-critical |

- **Measurement window**: Monthly calculation is more protective for customers than annual (monthly 99.9% = max 43.8 min/month; annual allows front-loading downtime)
- **Availability definition**: "Service is available" must be defined precisely — vendor should specify what endpoint or capability is being measured

*Service Credit Structures:*

Standard tiered credit formula (enterprise B2B SaaS):
```
Actual Uptime 99.0%-99.9%:  10% credit of monthly fee
Actual Uptime 95.0%-99.0%:  25% credit of monthly fee
Actual Uptime < 95.0%:      50% credit of monthly fee
Actual Uptime < 90.0%:     100% credit of monthly fee (monthly fee cap)
```

- **Credits vs. refunds**: Most vendors offer credits against future invoices, not cash refunds. Customer-side: push for cash refunds for sustained outages (>24 continuous hours) or for enterprise deals at significant ARR
- **Sole remedy limitation**: Vendor language making SLA credits the "sole and exclusive remedy" for uptime failures is a major RED flag for customers — this prevents damages claims for losses flowing from the outage
- **Credit claim deadline**: Most SaaS SLAs require credit claims within 30 days; track and claim or credits are forfeited
- **Termination right**: Customer-side: add right to terminate for cause if uptime falls below threshold (e.g., 95%) for three consecutive months

*Standard SLA Exclusions (vendor-side; review each for customer):*
- Scheduled maintenance (negotiate: maximum hours/month; must be outside business hours or during agreed maintenance window)
- Customer-caused outages (customer's misuse, misconfiguration, or use beyond permitted scope)
- Force majeure events
- Third-party infrastructure failures beyond vendor's reasonable control (e.g., internet backbone, upstream DNS)
- Customer's failure to implement required updates or patches

### 3. Data Security and Processing

**Encryption standards (minimum accepted in enterprise SaaS):**
- Encryption at rest: AES-256 (or equivalent)
- Encryption in transit: TLS 1.2+ (prefer TLS 1.3)
- Key management: Customer-controlled keys (BYOK) for high-sensitivity deployments
- Database-level field encryption for PII columns in multi-tenant environments

**Compliance certifications:**
- **SOC 2 Type II** (preferred over Type I): Covers operating effectiveness over minimum 6-month period (vs. point-in-time Type I); request annual current report
- **ISO 27001**: Third-party certification of information security management system; verify scope covers production environment
- **ISO 27701**: Privacy information management extension to ISO 27001 — increasingly expected for GDPR-regulated services
- **Penetration testing**: Annual third-party penetration test; customer right to receive executive summary (not necessarily full report); scope should cover production environment
- **Vulnerability management**: Patching SLA (e.g., critical within 24h, high within 7 days)

**GDPR / EU Data Protection Compliance (mandatory DPA elements — GDPR Art. 28(3)):**
1. Subject matter, duration, nature, and purpose of processing
2. Types of personal data and categories of data subjects
3. Processing only on documented controller instructions
4. Confidentiality obligation on authorized personnel
5. Security measures per Art. 32 (TOMs — technical and organizational measures)
6. Sub-processor controls: specific or general written authorization; equivalent obligations via written contract; [VERIFY: EDPB Opinion 22/2024 requires continuous verification of sub-processor compliance, not just initial authorization]
7. Data subject rights assistance (access, rectification, erasure, restriction, portability)
8. DPIA and prior consultation assistance
9. Data deletion or return on termination (at controller's election)
10. Audit rights: information provision + controller/auditor-commissioned audit rights

**HIPAA BAA Requirements (US — mandatory for ePHI processing):**
Any SaaS vendor creating, receiving, maintaining, or transmitting electronic protected health
information (ePHI) on behalf of a HIPAA-covered entity must execute a Business Associate Agreement
(BAA) per 45 CFR §164.504(e). Mandatory BAA terms:
- Limited uses and disclosures of ePHI to those specified in the BAA
- Appropriate safeguards under the HIPAA Security Rule (administrative, physical, technical)
- Breach reporting without unreasonable delay and within 60 days of discovery
- ePHI available for access, amendment, and accounting of disclosures
- HHS Secretary access to practices for compliance review
- Return or destruction of ePHI on termination
- Downstream subcontractor BAAs required when ePHI disclosed to sub-processors

HIPAA BAA breach notification obligations should be carved out from the general limitation of
liability cap — HIPAA violations generate separate regulatory penalties.

**NIS2 Directive obligations (EU — applicable to qualifying cloud providers, October 2024):**
- Risk management measures covering: incident handling, business continuity, supply chain security, access control, cryptography, multi-factor authentication, vulnerability management
- Significant incident reporting: 24h early warning → 72h incident notification → 1-month final report
- Supply chain security provisions requiring verification of sub-processor security posture
- Management accountability obligations; fines up to €10M or 2% global turnover (essential entities)

### 4. Intellectual Property

**Core IP allocation matrix:**

| Content Type | Vendor-Side Default | Customer-Side Standard | Balanced Position |
|-------------|--------------------|-----------------------|-------------------|
| Pre-existing vendor IP (platform, code, technology) | Vendor retains all | Vendor retains all | Vendor retains all |
| Customer data (input) | Vendor licensed to process | Customer owns; vendor licensed only for service delivery | Customer owns; vendor has narrow processing license |
| Customer-created outputs / exports | Customer owns | Customer owns | Customer owns |
| AI-generated outputs using customer prompts | Ambiguous; vendor claims rights | Customer owns | Customer owns |
| Platform improvements from aggregated data | Vendor retains | Customer retains if attributable to customer data | Vendor retains if anonymized and non-attributable |
| Developments specifically commissioned by customer | Negotiated | Customer owns (work-for-hire) | IP ownership per SOW; vendor retains background IP |

**Moral rights note** [JURISDICTION-SPECIFIC]: In EU and UK jurisdictions, moral rights (attribution,
integrity) cannot be fully waived by the original creator and may attach to certain vendor-created
materials. In US work-for-hire arrangements, moral rights in most works do not attach. [VERIFY]

### 5. AI Training Restrictions

This is a critical and rapidly evolving clause category. Standard market practice as of 2025-2026:

**What customers should require (minimum):**
- Explicit prohibition: "Vendor shall not use Customer Data, or any output, derivative, or
  processed form thereof, to train, fine-tune, evaluate, or otherwise improve any machine learning
  or artificial intelligence model, including without limitation any generative AI model, without
  Customer's prior written consent."
- Definition clarity: Ensure "train" covers fine-tuning, distillation, RLHF, synthetic data generation, and evaluation data set use
- Sub-vendor coverage: Restriction must flow through to vendor's AI infrastructure sub-processors (e.g., OpenAI, Anthropic, Google)
- Aggregation carveout scope: If vendor proposes an anonymized/aggregated data carveout, customer should require: (i) data is non-attributable; (ii) customer cannot be re-identified; (iii) carveout does not cover personal data
- Audit right: Customer right to request confirmation of compliance with AI training restriction

**What vendors typically resist:**
- Absolute prohibition including anonymized/aggregated data (impedes product improvement)
- Flowing restriction to all sub-processors (affects vendor's AI tooling stack)
- Audit rights on AI training practices (operational complexity)

**Vendor-side minimum acceptable:**
- Train only on vendor-owned data, public data, or data from customers who have opted in
- Provide opt-out mechanism for customers who object to aggregated / anonymized use
- Restrict restriction scope to identifiable customer data, not truly anonymized derivatives

[JURISDICTION-SPECIFIC] EU AI Act may impose additional transparency obligations on vendors
deploying general-purpose AI in their platforms that interact with or train on customer data.
Emerging EU guidance on output ownership and AI training data rights. [VERIFY current status]

### 7. Data Portability and Exit Assistance

**EU Data Act (Regulation 2023/2854) — Mandatory for EU Customers (applicable September 12, 2025):**

Key obligations for cloud/SaaS providers with EU customers:
1. **Termination right**: Customer may terminate for convenience with maximum 2-month notice regardless of original contract term; early termination penalties must be proportionate
2. **Switching initiation**: Provider must initiate switching process within the notice period
3. **30-day porting window**: Data transfer must be completed within 30 calendar days of termination notice (extendable to 7 months maximum for genuine technical complexity)
4. **Data format**: Machine-readable, structured format; if EUCS interoperability standards published for service category, those apply; otherwise best efforts toward standardized format
5. **Exportable data scope**: All input data, output data, metadata (logs, timestamps, contextual data), and (where technically feasible) applications and other digital assets
6. **Open interfaces**: Free of charge, to customer and successor provider, for portability and interoperability
7. **No switching fees**: All switching fees eliminated by January 2027; until then, capped at actual cost of switch
8. **Lock-in prohibition**: All contractual, technical, commercial, and organizational obstacles to switching prohibited

[VERIFY: Whether EUCS interoperability standards have been published for any SaaS category as of 2026]

**Market-standard data portability provisions (non-EU):**
- Post-termination data access: 30-90 days (30 days is common market minimum)
- Export format: Machine-readable (CSV, JSON, XML); documented schema
- Migration assistance: Reasonable assistance for 30-90 days post-termination at professional services rates
- Destruction certificate: Within 60-90 days of data destruction; certify against specific data categories
- Backup retention: Specify whether backup copies are destroyed and when

### 8. Liability Caps and Exclusions

**Market standard for B2B enterprise SaaS:**

| Liability Cap Position | Vendor-Side | Customer-Side | Balanced Enterprise |
|----------------------|-------------|---------------|---------------------|
| Annual subscription fees cap | 3-6 months | 24+ months | 12 months |
| Data breach carveout | Capped at annual fees | Uncapped | 2x annual fees (or insurance coverage limit) |
| IP indemnification carveout | Capped | Uncapped | Uncapped (vendor controls the risk) |
| Fraud/gross negligence | Capped | Uncapped | Uncapped |
| Willful misconduct | Capped | Uncapped | Uncapped |
| SLA credits as sole remedy | Vendor preference | Resist; retain damages right | SLA credits as primary remedy; damages preserved for prolonged failure |

**Consequential damages exclusion carveouts (customer-side must negotiate):**
- Carve out data loss damages from the consequential damages exclusion (data reconstruction cost is direct, not consequential)
- Carve out compliance fines and penalties arising from vendor's breach of data security obligations
- Carve out customer's revenue losses directly flowing from prolonged SaaS unavailability (especially for SaaS that is a critical business-enabling service)

**[JURISDICTION-SPECIFIC] Enforceability:**
- **UK B2B (UCTA s.2/s.3)**: Limitation must satisfy reasonableness test. Caps grossly disproportionate to foreseeable risk may fail; vendors on standard forms face higher scrutiny
- **AU (ACL)**: Small business contracts subject to unfair terms regime from November 2023; very low caps may constitute unfair terms
- **US**: No federal enforceability rule; state law varies; contract of adhesion doctrine applies to standard-form SaaS terms

---

## Jurisdiction-Specific Compliance Obligations

### EU / EEA
- **GDPR Art. 28 DPA**: Execute before personal data processing; include all mandatory terms [see Section 3]
- **EU Data Act**: Embed switching rights in any agreement with EU customers after September 12, 2025
- **NIS2**: Verify whether vendor qualifies as essential/important entity; include supply chain security obligations
- **AI Act (EU) 2024/1689**: Vendors deploying high-risk AI systems must satisfy Art. 9-15 requirements; B2C general-purpose AI transparency obligations apply from August 2025

### United Kingdom
- **UK GDPR**: Execute UK-compliant DPA; use UK IDTA or EU SCCs + UK Addendum for international transfers
- **UK-US Data Bridge**: Verify US vendor certification before relying on Data Bridge (effective October 2023)
- **UCTA 1977**: Limitation clause must satisfy reasonableness test for B2B standard-form SaaS agreements
- **CRA 2015**: B2C SaaS — unfair terms are void; services must be performed with reasonable care and skill

### United States
- **HIPAA BAA**: Mandatory before ePHI processing; cannot be waived by agreement
- **CCPA/CPRA Service Provider Terms**: Cal. Code Regs. §7051 mandatory provisions for California personal data
- **Auto-renewal compliance**: California B&P §17600-17606 (amended July 2025), NY GBL §527-A (amended November 2025), other state-specific laws for B2C and applicable B2B
- **State attorney general enforcement**: FTC, California, New York active enforcers of SaaS unfair practices

### Australia
- **Privacy Act 1988 + APPs**: Mandatory contractual privacy obligations for offshore processing; NDB scheme breach notification flows through to SaaS vendor
- **ACL unfair terms (post-November 2023)**: Standard-form B2C and small-business SaaS agreements subject to civil penalties for unfair terms; AUD $50M maximum per contravention
- **ACL consumer guarantees**: Cannot be excluded for consumer services; services must be rendered with reasonable care and skill

---

## Negotiation Priority Framework

### Tier 1 — Must-Have (Non-Negotiable)

These items require resolution before signature. Accept only after senior legal sign-off.

- **GDPR / CCPA / HIPAA compliance terms** (DPA, BAA, service provider terms) — regulatory obligation, not commercial position
- **EU Data Act switching rights** (if EU customers) — mandatory by law; void if excluded
- **Liability cap floor** (minimum 12 months' fees, customer-side) — below this level, effective recourse is impossible
- **Data breach liability carveout** (from liability cap) — standard market practice in enterprise SaaS
- **AI training restriction** (explicit prohibition or opt-in only) — customer data rights protection
- **IP ownership** (customer owns all input data and outputs) — fundamental ownership issue
- **Governing law** (neutral or applicable jurisdiction) — enforcement viability

### Tier 2 — Should-Have (Prioritize in Negotiation)

These items are important and should be pushed for, but a compromise may be acceptable given
deal dynamics.

- **SLA uptime level** (99.9%+ monthly calculation, tiered credits, termination right for sustained failure)
- **Data portability** (30-day post-termination access, machine-readable export, destruction certificate)
- **Auto-renewal notice** (60+ days for enterprise; statutory minimum for consumer-applicable deals)
- **Downgrade / seat reduction rights** (at annual renewal with 90 days' notice)
- **SOC 2 Type II report access** (annual report; ISO 27001 certification)
- **API deprecation notice** (6 months minimum for breaking changes)
- **Pricing change notice** (90+ days before renewal; CPI cap or stated percentage)
- **Consequential damages carveout** (data loss, compliance fines)
- **Audit right** (on-site or third-party audit right with reasonable notice beyond questionnaire)

### Tier 3 — Nice-to-Have (Concede Under Pressure)

These items are beneficial but not essential. Concede to achieve Tier 1 and Tier 2 positions.

- **Cash refunds** (vs. credits) for SLA failures below extended outage threshold
- **Customer-controlled encryption keys** (BYOK) for standard non-sensitive deployments
- **Specific penetration test report access** (vs. executive summary)
- **Individual SLA credits for individual service components** (vs. aggregate platform availability)
- **NPS / satisfaction survey obligations**
- **Dedicated success manager obligations**
- **Source code escrow** (for non-critical SaaS platforms)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before delivery.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal claim cites a specific statute, regulation, case, or established market practice | Add citation or mark [VERIFY] |
| **Format** | All citations follow a consistent, recognizable format for the jurisdiction | Fix format |
| **Currency** | Every cited provision verified for amendments or repeal (SaaS law changes fast: EU Data Act, auto-renewal statutes, AI Act) | Flag [CHECK CURRENCY] |
| **Domain** | Analysis stays within the skill's governing law scope; no jurisdiction bleed | Remove or flag out-of-scope references |
| **Confidence** | Uncertainty explicitly stated, not buried | Add confidence qualifier |

### Self-Interrogation for RED Items

For any item classified RED or [COMPLIANCE-REQUIRED], apply this 3-pass adversarial review:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the cited
authority? Would a court or regulator actually reach this conclusion based on these facts? Is the
cited statute current and applicable in this jurisdiction? [JURISDICTION-SPECIFIC: UCTA reasonableness,
ACL unfairness, GDPR mandatory terms — all jurisdiction-specific applications require Pass 1 verification]

**Pass 2 — Completeness**: Have all relevant statutes, regulations, and market practices been
considered? Are there SaaS-specific nuances (multi-tenant data isolation, API-mediated service
delivery, platform as infrastructure) not yet addressed? Are there regulatory dimensions (NIS2, DSA,
EU AI Act) that interact with this clause?

**Pass 3 — Challenge**: What is the strongest argument against this classification? Under what
circumstances might a sophisticated counterparty accept this risk? Is there a market-standard
alternative that satisfies both parties' core interests? For SaaS: could an insurance mechanism or
escrow arrangement mitigate the risk without changing the contract term?

### Confidence Scoring

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95-1.0 | Settled law or clear market standard | State with confidence |
| **High** | 0.80-0.94 | Strong authority, minor interpretive questions | State with brief caveat |
| **Probable** | 0.60-0.79 | Good arguments, could differ in jurisdiction or context | State with reasoning and contra-indicators |
| **Possible** | 0.40-0.59 | Genuinely uncertain (e.g., AI output ownership, EU Data Act edge cases) | Flag for professional review; present both sides |
| **Unlikely** | 0.0-0.39 | Weak basis, speculative | Do not assert; flag [UNCERTAIN] |

---

## Glass Box Audit Trail

Append this YAML block to every output. Fill all fields; mark unknowns explicitly.

```yaml
glass_box:
  skill_name: legalcode-saas-agreement-drafter
  date_of_analysis: "[YYYY-MM-DD]"
  mode: "[Review existing agreement / Drafting from scratch / Clause request]"
  agreement_reference: "[File name, URL, or 'Pasted text' with word count]"
  governing_law: "[Jurisdiction or 'Not specified']"

  # Perspective and context
  draft_perspective: "[Vendor / Customer / Both]"
  saas_model: "[B2B Enterprise / B2B SMB / B2C / B2B2C / Hybrid]"
  deal_context: "[Brief description or 'Not provided']"
  playbook_used: "[Organizational playbook / B2B SaaS market standards / Options provided as we go]"

  # Regulatory flags
  gdpr_scope: "[Yes / No / Not assessed]"
  ccpa_scope: "[Yes / No / Not assessed]"
  hipaa_baa_required: "[Yes / No / Not assessed]"
  eu_data_act_applicable: "[Yes / No — EU customers after 2025-09-12]"
  nis2_applicable: "[Yes / No / Not assessed]"
  auto_renewal_consumer_law: "[Applicable jurisdictions or 'B2B only']"

  # SaaS-specific fields
  sla_uptime_found: "[% commitment or 'None']"
  ai_training_restriction_present: "[Yes / No / Partial]"
  data_portability_provision: "[Present / Absent / EU Data Act compliant]"
  dpa_executed: "[Yes / No / Required but absent]"
  baa_executed: "[Yes / No / Required but absent]"
  compliance_certifications_claimed: "[SOC 2 Type I / SOC 2 Type II / ISO 27001 / None]"

  # Analysis quality
  topic_areas_covered: "[N of 15]"
  deviations_found: "GREEN: [N] / YELLOW: [N] / RED: [N] / COMPLIANCE-REQUIRED: [N]"
  perspective_flip_completed: "[Yes / No]"
  quality_score_estimate: "[X]/40 prompt-engineering dimensions"

  # Source quality
  external_tools_used: "[legalcode-mcp / None — manual verification required]"
  citations_verified: "[N verified] / [N marked VERIFY]"
  research_reference_file: "[/tmp/legalcode-saas-authority.md or 'Not created']"
  legalcode_mcp: "[Connected / Not connected]"

  # Confidence
  confidence_overall: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "[Scope limitations, assumptions, or caveats]"
    - "[Jurisdiction-specific items requiring specialist verification]"
    - "[AI training / EU Data Act items marked VERIFY where uncertain]"

  reviewer: "AI-assisted — requires qualified legal review before execution"
```

---

## Anti-Patterns

What NOT to do when drafting or reviewing SaaS agreements. These are SaaS-specific — not
generic contract drafting failures.

**SLA Anti-Patterns:**

1. **Undefined "availability" in the SLA**: Promising uptime without defining what "the service is available" means — measured from which endpoint, covering which components, at what response threshold. An undefined availability metric is unenforceable and guarantees disputes.

2. **Annual uptime calculation window**: Vendors who calculate SLA uptime annually can front-load all downtime in one period. Monthly calculation is the only customer-protective standard. An annual 99.9% SLA allows an outage of over 8 hours in a single day.

3. **SLA credits as the sole and exclusive remedy for all uptime failures**: Credits capped at one month's fees cannot compensate a customer whose $10M business was offline for 48 hours. Always negotiate: (a) damages preserved for prolonged failures, (b) termination right for repeated or sustained failures.

4. **Maintenance window as a blank check**: "Scheduled maintenance windows shall not count toward downtime." Without limiting the frequency and duration of scheduled maintenance (e.g., "not to exceed 8 hours per month; outside business hours"), vendors can schedule indefinite maintenance and exclude it from SLA obligations.

5. **Credit claim forfeiture**: Standard SaaS SLAs require customers to claim credits within 30 days. Customers who don't track SLA performance proactively will forfeit credits they are contractually entitled to.

**Data Handling Anti-Patterns:**

6. **Vague data portability language**: "Vendor will assist in exporting Customer Data" without specifying format, scope, timeline, or cost is commercially meaningless. At contract exit, disputes over "reasonableness" of vendor's export assistance are common and expensive.

7. **No destruction certificate**: A provision requiring data deletion on termination, without requiring the vendor to certify destruction, is unverifiable. For regulated data (GDPR, HIPAA, CCPA), uncertified deletion creates audit and enforcement risk.

8. **Backup tape carveout that swallows the deletion obligation**: "Vendor will delete Customer Data within 90 days, except for backup copies, which will be deleted in the ordinary course of backup rotation." If backup rotation takes 12 months, customer data persists for a year after termination. Negotiate: "Backup copies destroyed within 90 days of termination."

9. **Sub-processor list as a website link**: Vendor embeds sub-processor list by reference to a URL that can be updated at any time without notice. Customer-side: require email or in-app notification of material sub-processor changes with a 30-day objection window; this is also required under GDPR Art. 28(2).

10. **Post-termination data access window of 0 days**: Some SaaS agreements terminate data access immediately on contract expiry. Customer loses data access before they can export. Negotiate minimum 30-day post-termination read-only access for export.

**Intellectual Property Anti-Patterns:**

11. **Broad "service improvement" license that covers AI training**: Vendor license to use customer data "to improve our services" — if drafted broadly — may encompass training the vendor's AI models on customer data. Every license to "use, process, and analyze" customer data should be explicitly scoped to exclude AI training, fine-tuning, and evaluation data use.

12. **Ambiguous output ownership**: Vendor terms that state "all outputs generated by our platform are owned by Vendor." For AI-generated outputs derived from customer prompts and customer data, this is commercially unreasonable and likely unenforceable in many jurisdictions. Customer-side: "Customer owns all outputs generated using Customer Data."

13. **Work-for-hire trap in professional services addenda**: When a vendor's professional services team customizes the platform for the customer, a professional services SOW that defaults to vendor IP ownership may unintentionally transfer ownership of customizations the customer paid for. Negotiate IP ownership per SOW.

**Commercial Anti-Patterns:**

14. **Auto-renewal on a tight notice window**: B2B SaaS agreements with 30-day non-renewal notice windows embedded in agreements with annual payment cycles will often trap customers into another year of fees. California (July 2025), New York (November 2025), and other states impose advance notice requirements — and courts in non-CARL states are not sympathetic to vendors who provide notice that is technically compliant but practically impossible to act upon.

15. **Uncapped seat true-up at list price**: An annual true-up that charges overages at list price (not the contracted discounted rate) can generate invoices far exceeding the customer's budget. Negotiate: overages billed at contracted per-seat rate; pro-rata for partial periods; true-up mechanism that allows customer advance notice and a cure period before the true-up invoice issues.

16. **"All data generated by the platform belongs to Vendor" combined with no data portability**: This double-sided provision locks the customer into the platform (they cannot export their own data) while simultaneously giving the vendor commercial rights over what the customer generates. This combination is a RED flag and may be void under EU Data Act for EU customers.

17. **Illusory audit rights**: Audit right provisions that require: (i) 90 days' advance notice, (ii) agreement on scope in advance, (iii) a neutral third-party auditor approved by the vendor, (iv) costs borne by the customer, (v) no more than once per 36 months. In practice, this means no audit will ever happen. Negotiate: SOC 2 Type II report (annual) as primary audit mechanism, supplemented by a real on-site audit right (with 30 days' notice, reasonable scope, annually) that is not subject to vendor veto over auditor selection.

18. **Change management terms that are unilateral**: "Vendor may modify the Service at any time." Without a minimum notice period (90 days for material changes), a termination right for material adverse changes, and an API deprecation notice period (6 months for breaking changes), customers have no protection against the platform evolving in ways that break their integrations or workflows.

19. **SaaS agreement governing law in jurisdiction with no data protection law**: A SaaS processing EU personal data, governed by a jurisdiction with no meaningful data protection framework, and purporting to exclude GDPR DPA obligations, does not override GDPR — EU law applies regardless. Do not accept governing law arguments as a substitute for proper GDPR compliance terms.

20. **Vendor warranty for security certifications it doesn't currently hold**: "Vendor will maintain SOC 2 Type II certification" as a warranty when the vendor is pre-certification (only has a self-assessment or Type I) creates a breach on day one. Always verify current certification scope and audit period against vendor's actual compliance posture; require delivery of current SOC 2 Type II report as a condition precedent.

---

## Writing Standards

Before delivering any output, apply these quality gates:

1. **Redline specificity**: Every redline must include specific proposed language, not just a description of what to change. "Add a 30-day post-termination data access provision" is not a redline. Provide the actual clause text.

2. **Perspective discipline**: In dual-perspective mode, distinguish vendor and customer positions clearly. Do not present vendor-favorable positions as "balanced" or conflate the two.

3. **Active voice throughout**: "The vendor must notify the customer" not "notification by the vendor is required."

4. **SaaS terminology consistency**: Use "authorized users" (not "named users" or "seats" interchangeably), "Customer Data" (capitalized throughout, once defined), "Service" (capitalized when referring to the defined SaaS service), "Platform" (only if defined).

5. **Quantified commitments**: Never write "reasonable efforts" for a technical obligation that can be quantified. "Encryption in transit using TLS 1.2 or higher" is correct; "reasonable encryption in transit" is not enforceable.

6. **Jurisdiction markers**: Every legal claim tied to a specific jurisdiction must carry [JURISDICTION-SPECIFIC] in the section heading or [VERIFY] on the specific citation. Do not present US auto-renewal law as universal; do not present EU Data Act as applicable to non-EU customers.

7. **Audience calibration**: SaaS agreements are reviewed by product, engineering, finance, and legal stakeholders. Write findings in plain language without sacrifice of precision. A finding that can only be understood by a lawyer will be ignored by the procurement team that signs the contract.

8. **Completeness before delivery**: Run the 15-topic checklist before delivery. A SaaS agreement analysis that omits the AI training restriction or data portability review is materially incomplete as of 2025-2026.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

Use legalcode-mcp at Step 4 to gather jurisdiction-specific legal authority. Search for:
- GDPR Art. 28 mandatory DPA terms and EDPB guidance (especially EDPB Opinion 22/2024 on sub-processor verification)
- EU Data Act (Regulation 2023/2854) Article 23-31 switching rights obligations
- Auto-renewal state statutes for California, New York, and other applicable US states
- HIPAA 45 CFR §164.504(e) mandatory BAA terms
- UCTA 1977 s.2-3, s.11, Schedule 2 reasonableness factors (UK)
- ACL unfair terms provisions and penalty regime (AU, post-November 2023 reform)
- NIS2 Directive 2022/2555 classification criteria and security obligations

Save to `/tmp/legalcode-saas-authority.md`. Mark all legalcode-mcp-sourced citations as VERIFIED
in the Glass Box audit trail.

### Without legalcode-mcp

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed with general SaaS market knowledge
- Focus quality enhancement on structural completeness and prompt engineering quality rather than
  legal authority depth — legal citations require external verification before reliance

---

## Output Format Template

Structure every analysis output as follows:

---

# SaaS Agreement Analysis — [Agreement Name or Drafting Scope]

**Date**: [YYYY-MM-DD]
**Perspective**: [Vendor / Customer / Both]
**Governing Law**: [Jurisdiction]
**Business Model**: [B2B Enterprise / B2B SMB / B2C / B2B2C]
**Regulatory Scope**: [GDPR / CCPA / HIPAA BAA / EU Data Act / NIS2 / None]
**Based On**: [Organizational playbook / B2B SaaS market standards]
**Completeness**: [N of 15 topic areas analyzed]

---

## Executive Summary

**Overall Risk Profile**: [HIGH / MEDIUM / LOW]
**Key Issues**: [3-5 bullet points — the most important items to resolve before signature]
**Immediate Action Required**: [Yes — RED / COMPLIANCE-REQUIRED items identified | No — proceed with YELLOW negotiations]

**Issue Count**: GREEN: [N] / YELLOW: [N] / RED: [N] / COMPLIANCE-REQUIRED: [N]

---

## Clause-by-Clause Analysis

### [Topic Area] — [GREEN / YELLOW / RED / COMPLIANCE-REQUIRED] | Confidence: [Level]

**Status**: [Present and acceptable / Deviates from market standard / Absent]

**Vendor Position** (current language): "[Direct quote or summary]"
**Customer-side standard**: "[What customer should expect or push for]"
**Deviation**: "[How this deviates from market standard, if at all]"

**Business impact** (vendor perspective): "[Consequences if vendor accepts customer's position]"
**Business impact** (customer perspective): "[Consequences if customer accepts vendor's position]"

**Legal basis**: "[Statute, regulation, or market practice — or [VERIFY]]" [Confidence: X.XX]

**Vendor-side redline** (if current language favors customer):
> [Specific alternative language]

**Customer-side redline** (if current language favors vendor):
> [Specific alternative language]

**Fallback position** (if primary redline is rejected):
> [Compromise language both sides can accept]

**Risk Scoring**:
- Business impact: [HIGH / MEDIUM / LOW]
- Enforceability risk: [HIGH / MEDIUM / LOW]
- Negotiation difficulty: [HIGH / MEDIUM / LOW]
- Compliance risk: [HIGH / MEDIUM / LOW]

**Negotiation tier**: [Tier 1 Must-Have / Tier 2 Should-Have / Tier 3 Nice-to-Have]

[Repeat for each of 15 topic areas]

---

## Regulatory Compliance Flags

[If any compliance obligations identified]

| Obligation | Clause Status | Gap | Classification |
|-----------|--------------|-----|----------------|
| GDPR Art. 28 DPA | [Present / Absent] | [Description] | [GREEN / COMPLIANCE-REQUIRED] |
| HIPAA BAA | [Present / Absent / N/A] | [Description] | [GREEN / COMPLIANCE-REQUIRED / N/A] |
| EU Data Act switching rights | [Embedded / Absent / N/A] | [Description] | [GREEN / COMPLIANCE-REQUIRED / N/A] |
| CCPA service provider terms | [Present / Absent / N/A] | [Description] | [GREEN / COMPLIANCE-REQUIRED / N/A] |
| Auto-renewal consumer law | [Compliant / Non-compliant / N/A] | [Description] | [GREEN / RED / N/A] |

---

## Negotiation Strategy

**Tier 1 — Must Resolve Before Signature:**
[List with specific issues, legal basis, and recommended resolution]

**Tier 2 — Prioritize in Negotiation:**
[List with specific issues and recommended redlines]

**Tier 3 — Concede Under Pressure:**
[List with items that can be traded to win Tier 1 and 2 positions]

**Trade-link opportunities:**
[Specific pairs of issues where conceding on one gains position on the other]

**Negotiation posture**: [Assertive / Accommodating / Collaborative] — [reason]

---

## Glass Box Audit Trail

```yaml
[Glass Box YAML — see Glass Box section above]
```

---

## Localization Notes

This skill is jurisdiction-agnostic and designed for use with any governing law. When adapting
for specific jurisdictions:

**EU / EEA**: Embed EU Data Act switching rights in all agreements post-September 2025. Execute GDPR DPA before any personal data processing begins. Verify NIS2 applicability for vendor's cloud service classification. Address EU AI Act for AI-enabled SaaS platforms.

**UK**: Use UK IDTA for international data transfers (or EU SCCs + UK Addendum). Verify that limitation of liability satisfies UCTA s.11 reasonableness test, particularly for standard-form vendor agreements.

**US**: Address state auto-renewal laws for B2C and qualifying B2B customers (California, New York, and others). Execute HIPAA BAA before any ePHI processing. Include CCPA service provider terms for California personal data. Note FTC enforcement risks on unfair or deceptive SaaS practices even without a specific statute.

**Australia**: Verify ACL unfair terms applicability (consumers + small businesses from November 2023). Confirm vendor understanding of Privacy Act 1988 APP obligations, including NDB scheme breach notification flowing through to vendor as offshore data processor.

**Canada**: PIPEDA (federal) / Quebec Law 25 (Quebec) data processing obligations. Law 25 confidentiality incident reporting — 72h internal assessment, reporting to CAI for incidents affecting privacy interests.

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis incorporating:
- Structural patterns from `legalcode-contract-review` (Legalcode gold standard)
- 2-agent research pipeline: Agent 1 (structural analysis of reference skills, 15-clause SaaS architecture, dual-perspective framework, 14-step workflow, 20 anti-patterns, Glass Box YAML) + Agent 2 (deep legal research: EU Data Act 2023/2854 switching rights, NIS2 Directive 2022/2555, GDPR Art. 28/CCPA Cal. Code Regs. §7051, HIPAA 45 CFR §164.504(e), UK UCTA/CRA, ACL AU post-2023 reform, California B&P §17600-17606 amended July 2025, NY GBL §527-A amended November 2025, SLA market standards, AI training restriction emerging practice, UCC/UCITA SaaS characterization debate)
- Jurisdictions covered: US (50 states + federal overlays), EU/EEA (GDPR, EU Data Act, NIS2, DSA, AI Act), UK (UK GDPR, UCTA, CRA), AU (Privacy Act, ACL)
- AI training restrictions and EU Data Act provisions reflect law as of March 2026; verify currency before reliance
- All statutory citations marked [VERIFY] require verification against authoritative sources before legal reliance
