---
name: legalcode-privilege-review
description: Run defensible privilege review for litigation, investigations, and regulatory responses.
  Classify attorney-client / legal-advice privilege, litigation privilege, and work-product protection;
  detect waiver risk; produce privilege logs and challenge-ready rationale across U.S., UK, AU, and CA
  workflows with jurisdiction markers.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Privilege Review

> **Disclaimer**: This skill provides a framework for AI-assisted privilege review. It does
> not constitute legal advice. All outputs must be reviewed by qualified counsel licensed in
> the governing jurisdiction before use. Legal-privilege doctrine is fact-sensitive and can
> change by jurisdiction, court, and procedural posture; verify all authorities before filing
> or production.

## Purpose and Scope

Use this skill to perform a structured, defensible review of documents and communications for
privilege and protection claims before disclosure.

This skill does:

- Classify attorney-client / legal-advice privilege, litigation privilege, and work-product
  protection
- Identify waiver-risk patterns (distribution, mixed business/legal use, inadvertent handling)
- Produce document-level and categorical privilege-log outputs
- Prepare challenge-ready rationale for meet-and-confer, motion practice, and in camera review
- Generate an auditable quality record with confidence scoring

This skill does not:

- Replace outside or local counsel advice
- Guarantee privilege outcomes in contested motion practice
- Decide final production positions without human legal sign-off

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic by default and must be localized to the forum.

[JURISDICTION-SPECIFIC] Confirm and apply:

- **US**: FRCP 26(b)(5), FRCP 26(f), FRE 502; federal/common-law or state-law privilege choice
- **England & Wales**: Legal advice privilege vs litigation privilege; CPR Part 31 disclosure
  mechanics and withholding/inspection rules
- **Australia**: Client legal privilege framework under Evidence Act 1995 (Cth) [VERIFY],
  including dominant-purpose analysis
- **Canada**: Solicitor-client and litigation privilege framework; dominant-purpose and waiver
  approach [VERIFY]

If governing law/forum is uncertain, classify as `DISPUTED` and escalate immediately.

## Interactive Clarification

Use CLARIFY prompts when answers materially change classification or defensibility.

**CLARIFY 1: Matter frame**

- Options: `civil litigation`, `arbitration`, `regulatory`, `internal investigation`, `mixed`
- Why it matters: Changes privilege baseline and disclosure burden.

**CLARIFY 2: Jurisdiction and rule set**

- Options: `US federal`, `US state`, `England & Wales`, `Australia`, `Canada`, `other`
- Why it matters: Privilege tests and waiver consequences differ.

**CLARIFY 3: Review objective**

- Options: `pre-production privilege log`, `challenge response`, `spot audit`, `full corpus`
- Why it matters: Controls depth and sampling strategy.

**CLARIFY 4: Risk posture**

- Options: `conservative (over-withhold)`, `balanced`, `aggressive (narrow claims)`
- Why it matters: Affects tie-break treatment for borderline records.

**CLARIFY 5: Time and volume constraints**

- Inputs: corpus size, deadline, available reviewers
- Why it matters: Determines categorical-log usage, batching, and QC level.

## Workflow

### Step 1: Confirm Legal Frame

- Capture forum, governing law, production obligations, and dispute stage.
- Output: `matter_frame`.

### Step 2: Build Corpus Inventory

- Map custodians, systems, date ranges, document families, and duplicates.
- Output: `inventory_register`.

### Step 3: Define Privilege Taxonomy

- Activate jurisdiction-appropriate definitions for:
  - legal-advice / attorney-client privilege
  - litigation privilege / work-product
  - common-interest / joint-defense [JURISDICTION-SPECIFIC][VERIFY]
- Output: `taxonomy_profile`.

### Step 4: CLARIFY Missing Parameters

- If legal role, jurisdiction, or objective is missing, run CLARIFY blocks before coding.
- Output: `clarification_log`.

### Step 5: First-Pass Coding

- Apply decision rules to each item or category.
- Assign one status from the classification framework.
- Output: `pass1_coding`.

### Step 6: Waiver-Risk Analysis

- Evaluate confidentiality integrity, dissemination scope, and inconsistency risk.
- Flag inadvertent-production and subject-matter-waiver exposure.
- Output: `waiver_risk_register`.

### Step 7: Privilege-Log Drafting

- Draft document-level or categorical entries using required minimum fields.
- Ensure descriptions support assessment without revealing privileged substance.
- Output: `draft_privilege_log`.

### Step 8: Challenge Readiness

- For `DISPUTED` and high-risk items, prepare concise challenge memos with authority anchors.
- Output: `challenge_packet`.

### Step 9: Quality Controls

- Run Citation Quality Gates, Self-Interrogation, and Confidence Scoring.
- Output: `qa_record`.

### Step 10: Final Deliverable

- Publish final package using the Output Template.
- Output: `privilege_review_report`.

## Deep Privilege Analysis Framework

Evaluate each record against these elements:

| Dimension                | Questions                                                          | Typical Red Flags                                 |
| ------------------------ | ------------------------------------------------------------------ | ------------------------------------------------- |
| Confidentiality          | Was communication confidential at creation and handling?           | Broad internal forwarding, external recipients    |
| Legal-purpose nexus      | Was legal advice sought/provided (or litigation dominant purpose)? | Business-only context, policy/commercial routing  |
| Participant role         | Are counsel and client roles clear?                                | Non-lawyer summaries presented as legal advice    |
| Litigation anticipation  | Was litigation reasonably contemplated?                            | Post-hoc litigation labeling                      |
| Dominant purpose         | Is legal/litigation purpose primary?                               | Mixed-purpose docs without dominant legal purpose |
| Waiver behavior          | Any express/implied waiver acts?                                   | Selective disclosure, reliance defenses           |
| Metadata coherence       | Do dates/threads/attachments align with claim?                     | Broken chains, orphan attachments                 |
| Production defensibility | Can claim be explained without privileged substance?               | Boilerplate privilege log text                    |

### Privilege Status Classification

| Status                | Meaning                                                       | Default Action                               |
| --------------------- | ------------------------------------------------------------- | -------------------------------------------- |
| `PROTECTED`           | Privilege/protection criteria satisfied with low dispute risk | Withhold; log entry required                 |
| `PARTIALLY_PROTECTED` | Only portion is privileged/protected                          | Redact privileged content; produce remainder |
| `NOT_PROTECTED`       | Criteria not met                                              | Produce (subject to other bases)             |
| `DISPUTED`            | Material uncertainty or likely challenge                      | Escalate for counsel decision                |

### Waiver Severity Classification

| Severity   | Meaning                                       | Typical Triggers                                  |
| ---------- | --------------------------------------------- | ------------------------------------------------- |
| `LOW`      | Minimal waiver risk                           | Limited controlled circulation                    |
| `MEDIUM`   | Contestable waiver risk                       | Mixed legal/business use, unclear role separation |
| `HIGH`     | Significant waiver exposure                   | External sharing, selective disclosure            |
| `CRITICAL` | Likely loss of protection absent intervention | Broad dissemination, inconsistent court position  |

## Actionable Output Per Finding

For each `PARTIALLY_PROTECTED` or `DISPUTED` record, provide:

- Short rationale for current status
- Jurisdiction anchor (rule/case) with `VERIFIED` or `[VERIFY]`
- Recommended action (`withhold`, `redact`, `produce`, `escalate`)
- Waiver-mitigation step (if any)
- Owner and due window

## Prioritization Framework

| Tier     | Applies To                                                                      | SLA      |
| -------- | ------------------------------------------------------------------------------- | -------- |
| `Tier 1` | `CRITICAL` waiver risk, court deadline conflicts, contested cornerstone records | 0-24h    |
| `Tier 2` | `HIGH` waiver risk, broad-volume categorical issues                             | 1-3 days |
| `Tier 3` | `MEDIUM/LOW` clarifications and hygiene improvements                            | 3+ days  |

## Citation Quality Gates

Run these gates before release:

| Gate       | Rule                                                       | Fail Action                           |
| ---------- | ---------------------------------------------------------- | ------------------------------------- |
| Source     | Tie each legal proposition to authority or mark `[VERIFY]` | Add authority or downgrade confidence |
| Format     | Use recognizable citation format for forum                 | Normalize citation style              |
| Currency   | Confirm current procedural rule / doctrinal status         | Add `[CHECK CURRENCY]`                |
| Domain     | Avoid cross-jurisdiction bleed without marker              | Re-scope or annotate                  |
| Confidence | Match legal certainty to evidentiary support               | Reduce certainty + escalate           |

## Self-Interrogation (For DISPUTED/HIGH/CRITICAL)

Apply three-pass challenge before final status:

1. **Legal Chain Integrity**

- Does the status follow from the governing test and available facts?

2. **Completeness Test**

- What contrary facts or authorities could change the result?

3. **Adversarial Challenge**

- How would opposing counsel attack this privilege claim?

If unresolved after pass 3, keep `DISPUTED` and escalate.

## Confidence Scoring

| Level      | Range     | Meaning                        | Delivery Rule                        |
| ---------- | --------- | ------------------------------ | ------------------------------------ |
| `Definite` | 0.95-1.00 | Strong authority + clean facts | Present as primary recommendation    |
| `High`     | 0.80-0.94 | Strong but not absolute        | Include short caveat                 |
| `Probable` | 0.60-0.79 | Competing arguments plausible  | Provide both sides                   |
| `Possible` | 0.40-0.59 | Material uncertainty           | Escalate before final position       |
| `Unlikely` | 0.00-0.39 | Weak support                   | Do not rely without counsel override |

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-privilege-review"
  topic: "privilege review and privilege-log preparation"
  jurisdiction: "[selected forum]"
  enhancement_type: "Legalcode original scaffold + enhancement"
  legalcode_mcp: "Not connected"
  research_reference_file: "/tmp/legalcode-enhancement-research.md"
  source_skills_analyzed: "1 scaffold + legalcode reference standard"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_verified: "[count VERIFIED] / [count VERIFY]"
  confidence: "HIGH | MEDIUM | LOW"
  assumptions:
    - "[assumption]"
  limitations:
    - "Jurisdiction-specific doctrine varies by court and facts"
    - "Some non-US authorities marked [VERIFY] in this run"
  reviewer: "AI-assisted; qualified legal review required"
```

## Anti-Patterns

Avoid these failures:

1. Treating every counsel-involved communication as automatically privileged.
2. Using boilerplate log descriptions that hide legal basis.
3. Ignoring attachment-level differences (email privileged, attachment not).
4. Mixing business strategy and legal advice without dominant-purpose analysis.
5. Failing to separate legal-role communications from policy/operational advice.
6. Asserting privilege without preserving confidentiality controls.
7. Inconsistent treatment of the same thread across custodians.
8. Late or absent clawback workflow for inadvertent production.
9. Selectively disclosing favorable legal advice while withholding adverse advice.
10. Producing logs too late for dispute resolution before cutoff.
11. Overusing categorical logs for highly disputed cornerstone records.
12. Omitting jurisdiction-specific waiver standards.
13. Ignoring metadata conflicts (author, recipient, date anomalies).
14. Treating prior partial disclosure as irrelevant to waiver analysis.
15. Skipping counsel escalation for `DISPUTED` cornerstone items.
16. Shipping final output without QA gates and confidence labels.

## Writing Standards

- Write findings in plain, precise language.
- Distinguish fact from inference.
- Avoid categorical statements without authority support.
- Use explicit uncertainty labels (`[VERIFY]`, `[CHECK CURRENCY]`, `DISPUTED`).
- Keep rationale concise, reproducible, and challenge-ready.

## External Tool Integration

Use legalcode-mcp as preferred authority source when available:

- Query forum-specific privilege doctrine and current procedural rules.
- Pull controlling statutes/rules and recent appellate treatment.
- Mark confirmed references as `VERIFIED`.

If legalcode-mcp is unavailable:

- Proceed with official web sources and mark uncertain items `[VERIFY]`.
- Record tool availability in Glass Box.

## Localization Notes

For jurisdiction localization, keep these anchor checks:

- **US**: FRCP 26(b)(5), FRCP 26(f), FRE 502, work-product doctrine boundaries [VERIFY case fit]
- **England & Wales**: legal advice privilege vs litigation privilege, CPR Part 31 withholding mechanics
- **Australia**: dominant-purpose framework under Evidence Act 1995 (Cth) [VERIFY section-level text in forum]
- **Canada**: legal advice + litigation privilege branches and dominant-purpose analysis [VERIFY forum-specific precedent]

## Output Format Template

````markdown
# Privilege Review Report

## 1. Matter Frame

- Matter type:
- Forum / governing law:
- Review objective:
- Corpus size and date range:
- Assumptions:

## 2. Classification Summary

| Status              | Count | Percent |
| ------------------- | ----: | ------: |
| PROTECTED           |       |         |
| PARTIALLY_PROTECTED |       |         |
| NOT_PROTECTED       |       |         |
| DISPUTED            |       |         |

## 3. Waiver Risk Summary

| Severity | Count | Key Drivers |
| -------- | ----: | ----------- |
| LOW      |       |             |
| MEDIUM   |       |             |
| HIGH     |       |             |
| CRITICAL |       |             |

## 4. Priority Findings (Tier 1 / Tier 2)

| ID  | Status | Waiver Severity | Rationale | Action | Owner | Due |
| --- | ------ | --------------- | --------- | ------ | ----- | --- |

## 5. Draft Privilege Log (Core Fields)

| Log ID | Doc ID | Date | Author | Recipients | Privilege Basis | Description (non-revealing) | Status | Confidence |
| ------ | ------ | ---- | ------ | ---------- | --------------- | --------------------------- | ------ | ---------- |

## 6. Challenge-Readiness Notes

- Anticipated challenge themes:
- Counter-position summaries:
- In camera candidates:

## 7. QA and Confidence

- Citation gate outcomes:
- Self-interrogation outcomes:
- Confidence distribution:

## 8. Glass Box Audit

```yaml
[Insert Glass Box block]
```
````

```

## Provenance

Created by Legalcode (2026-02-28) from `SKILL_CREATION_TASKS.md` high-value backlog item.
Scaffold generated via legal-skill-creator workflow, then enhanced to Legalcode quality
using structural + prompt-analysis passes and web-backed research artifacts:
- `/tmp/legalcode-privilege-review-structural-analysis.md`
- `/tmp/legalcode-privilege-review-prompt-analysis.md`
- `/tmp/legalcode-enhancement-research.md`
```
