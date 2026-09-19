---
name: legalcode-open-source-license-compliance
description: Audit open-source software license compliance for any project or dependency inventory. Use
  when reviewing a software project for OSS license obligations before distribution, when assessing license
  compatibility in combined works, when evaluating copyleft obligations triggered by binary distribution
  or SaaS network use, when reviewing contributor license agreements (CLAs) and Developer Certificate
  of Origin (DCO) frameworks, when generating SBOM documentation to meet EO 14028 or EU CRA (Reg. 2024/2847)
  requirements, or when designing an enterprise open-source policy.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Audit open-source software license compliance for any project or dependency inventory. Use when reviewing a software project for OSS license obligations before distribution, when assessing license compatibility in combined works, when evaluating copyleft obligations triggered by binary distribution or SaaS network use, when reviewing contributor license agreements (CLAs) and Developer Certificate of Origin (DCO) frameworks, when generating SBOM documentation to meet EO 14028 or EU CRA (Reg. 2024/2847) requirements, or when designing an enterprise open-source policy. Covers: license identification and classification (permissive / weak copyleft / strong copyleft / network copyleft); license compatibility analysis for combined works; attribution and NOTICE file requirements (MIT, Apache 2.0, BSD, GPL, AGPL); copyleft obligation triggers (distribution, static/dynamic linking, AGPL § 13 network use); patent grant and retaliation clause analysis (Apache 2.0 § 3, GPL v3 § 11); commercial distribution requirements; SaaS network use implications; CLA and DCO review; open-source policy framework development; SBOM generation requirements; dependency chain analysis for transitive obligations; and remediation strategies for license conflicts. Produces a compliance audit report with severity- classified findings and prioritized action items. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers for US, EU, Germany, and France.


# Legalcode Open-Source License Compliance

> **Disclaimer**: This skill provides a framework for AI-assisted open-source license
> compliance analysis. It does not constitute legal advice and does not create an
> attorney-client relationship. All outputs should be reviewed by qualified legal
> counsel before use in distribution decisions, procurement requirements, or
> regulatory filings. Laws, license interpretations, and enforcement precedents
> change; verify current applicability before relying on any provision described here.
> Statutory references, license text provisions, and case citations sourced from
> memory carry hallucination risk — always verify against authoritative sources
> (OSI, SPDX, FSF, official license texts) before relying on them. License
> compatibility analysis involves jurisdiction-dependent legal questions not
> definitively resolved by courts; treat analysis as guidance, not legal opinion.

---

## Purpose and Scope

This skill audits software projects for open-source license compliance obligations. It
identifies all licenses present in a dependency tree, classifies them by copyleft strength
and compatibility, determines which obligations are triggered by the distribution model,
flags attribution gaps and missing SBOM documentation, and produces a confidence-scored,
auditable compliance report with a prioritized remediation plan.

**Covers:**

- License classification (permissive, weak copyleft, strong copyleft, network copyleft,
  source-available, no license) across npm, Maven, PyPI, Go modules, Cargo, and other ecosystems
- License compatibility analysis for combined works (especially GPL v2/v3, Apache 2.0,
  LGPL, MPL 2.0, AGPL interactions)
- Copyleft obligation triggers: distribution, static/dynamic linking, AGPL § 13 network use
- Attribution and NOTICE file requirements (MIT, Apache 2.0, BSD, GPL, AGPL, MPL)
- Patent grant and patent retaliation clause analysis (Apache 2.0 § 3, GPL v3 § 11, MPL 2.0 § 2.1)
- CLA review (ICLA, CCLA, DCO, Harmony Agreements)
- SBOM generation requirements under EO 14028, NTIA minimum elements, and EU CRA
  (Regulation 2024/2847 Articles 13–14, Annex I Part II)
- Dependency chain analysis for transitive license obligations
- Open-source policy development (inbound/outbound, license approval tiers, governance)
- Remediation strategies for license conflicts

**Does not:**

- Provide legal advice or replace qualified IP/copyright counsel
- Draft or modify license texts (use only canonical license text from official sources)
- Guarantee enforceability analysis in any specific jurisdiction
- Perform binary-level code scanning (requires external SCA tooling)
- Conduct trademark clearance analysis
- Apply exclusively to one distribution model — analysis adapts to the stated model

**Related skills:**

- `legalcode-saas-agreement-drafter` — for commercial license terms in SaaS agreements
- `legalcode-software-license-agreement` — for commercial software licensing
- `legalcode-eu-ai-act-high-risk-compliance` — AI-specific IP and licensing obligations
- `legalcode-dpa-review-and-negotiation` — data protection elements in OSS components
- `legalcode-compliance-program-builder` — enterprise compliance program incorporating OSS policy

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. OSS license compliance involves federal copyright
law, contract law, and increasingly regulatory law across multiple jurisdictions. Key
jurisdictional notes apply throughout:

[JURISDICTION-SPECIFIC: United States] Federal copyright law (17 U.S.C. §§ 101–1332)
governs the enforceability of OSS licenses. **Jacobsen v. Katzer** (Fed. Cir. 2008)
established that OSS license conditions are copyright conditions (not mere covenants) —
violation is copyright infringement, not just breach of contract, enabling statutory
damages up to $150,000 per work (willful infringement). The abstraction-filtration-
comparison test from _Computer Associates v. Altai_ (2d Cir. 1992) applies to derivative
work analysis. **Oracle LLC v. Google** (US Supreme Court, April 2021) held that
reimplementing API declaring code for interoperability purposes was fair use; confirm
applicability to specific facts. EO 14028 (May 2021) + NTIA minimum elements (June 2021)
mandate SBOM for software sold to US federal agencies. [VERIFY current CISA/NIST guidance.]

[JURISDICTION-SPECIFIC: European Union] EU Cyber Resilience Act (Regulation 2024/2847,
CRA) entered into force December 2024. Most manufacturer obligations apply from
September 2026; conformity assessment from December 2027. Article 13(1)(h) + Annex I
Part II require SBOMs in machine-readable format (top-level dependencies minimum; full
transitive tree best practice). SBOMs must be retained for 10 years. Pure non-commercial
OSS developers are largely exempt; commercial integrators and redistributors are fully
in scope. [VERIFY current transitional period status against EUR-Lex Regulation 2024/2847.]

[JURISDICTION-SPECIFIC: Germany] German courts are the most active OSS license
enforcement jurisdiction. Harald Welte's gpl-violations.org has obtained dozens of
injunctions for GPL v2 violations. German copyright law treats OSS licenses as
restrictive grants; violation is copyright infringement (Urheberrechtsverletzung).
Injunctions (einstweilige Verfügung) are efficient and widely used. [VERIFY current
German UrhG provisions.]

[JURISDICTION-SPECIFIC: France] **Entr'Ouvert v. Orange** (Paris Court of Appeal,
February 14, 2024): €800,000 damages award (€500k IP rights violation, €150k R&D savings
unjustly obtained, €150k moral prejudice) for Orange's 2005 incorporation of GPL v2-
licensed Lasso library into a government identity management platform. First major European
damages award for GPL non-compliance; decided after 12 years of litigation. Confirmation
that GPL violations are economically significant in EU civil law courts. [VERIFY damages
amounts are final; case may still be under appeal.]

[JURISDICTION-SPECIFIC: License Enforcement Universe] **SFC v. Vizio** (California
Superior Court, Orange County, ongoing): The Software Freedom Conservancy sued Vizio in
2021 for Linux/BusyBox GPL violations in smart TVs. In January 2024, the court denied
Vizio's motion for summary judgment, holding SFC had standing as a **third-party
beneficiary** to the GPL contract — potentially allowing consumers (not just copyright
holders) to enforce GPL obligations. Appellate ruling pending; outcome could dramatically
expand the enforcement universe. [VERIFY current case status.]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. The compliance
analysis depends critically on distribution model, risk tolerance, and organizational
context — the same dependency tree can be COMPLIANT for internal-use-only and
NON-COMPLIANT for binary distribution.

Use the **⟁ CLARIFY** pattern wherever marked below. Present structured options with
descriptions. If the user has already provided the information, skip the question. For
batch/non-interactive runs, proceed with reasonable defaults and state assumptions
explicitly at the start of the analysis.

---

## Workflow

### Step 1: Accept Input and Determine Analysis Mode

Accept the software inventory in any of these formats:

- **SBOM file**: SPDX JSON/tag-value, CycloneDX XML/JSON, NTIA-compliant CSV
- **Repository URL**: GitHub, GitLab, Bitbucket — scan via API
- **Package manifest files**: package.json, package-lock.json, yarn.lock, pom.xml,
  build.gradle, requirements.txt, Pipfile, Cargo.toml, go.mod, go.sum, Gemfile.lock
- **Scan output**: Results from FOSSA, Black Duck, Syft, Trivy, scancode-toolkit
- **Freeform list**: Package names + versions with known licenses
- **Directory path**: Local source tree for scanning

If no inventory is provided, prompt the user to supply one. If a partial inventory is
provided (e.g., only direct dependencies), note that transitive dependencies are not
analyzed and flag this as a scope limitation in the Glass Box audit trail.

**⟁ CLARIFY** — If the input format is unclear or potentially incomplete:

- Is this a complete dependency tree (direct + transitive), or only direct dependencies?
- Are there multiple repositories or projects to audit as a combined work?
- Is this a pre-distribution audit, a retrospective compliance review, or a procurement
  evaluation of a third-party vendor's software?

---

### Step 2: Gather Organization Context and Risk Posture

**⟁ CLARIFY** — Before beginning the analysis, ask the user:

1. **What is your role?**
   - Options: Developer (single-project compliance), Compliance officer (enterprise audit),
     Legal counsel (IP risk assessment), Security officer (procurement/vendor evaluation),
     Open-source program officer (policy development)
   - _Why this matters_: Scope, depth of analysis, and escalation paths differ
     fundamentally between a developer reviewing one project and an enterprise-wide audit.

2. **What is the distribution model?**
   - Options: **Internal use only** (employees/contractors only; no external distribution),
     **SaaS / network service** (users interact remotely via HTTP/API),
     **Binary distribution** (executables, mobile apps, embedded firmware),
     **Source code release** (open-source project; full source distributed),
     **License sale** (proprietary software sold with binary distribution rights),
     **Multiple models** (describe combination)
   - _Why this matters_: This single question determines which copyleft obligations trigger.
     GPL does not apply to internal use only. AGPL applies to SaaS and internal use.
     All models trigger attribution requirements for permissive licenses.

3. **What is your organization's copyleft risk posture?**
   - Options: **Conservative** (avoid all GPL/AGPL; only permissive licenses acceptable),
     **Pragmatic** (GPL/AGPL acceptable with proper isolation and source release plan),
     **Open-source aligned** (GPL/AGPL acceptable; organization willing to open-source code)
   - _Why this matters_: Determines ATTENTION vs. NON-COMPLIANT classification thresholds
     and which remediation options to prioritize.

4. **Are you accepting contributions to this software?**
   - Options: No contributions (closed internal development), Yes — informal contributions,
     Yes — formal contributor program with CLA/DCO
   - _Why this matters_: If yes, CLA and DCO review is material. Without CLA/DCO,
     copyright chain is broken and may prevent relicensing.

If the user provides partial context, proceed with defaults below and state assumptions
explicitly:

- **Default distribution model**: Binary distribution (most conservative trigger analysis)
- **Default copyleft posture**: Pragmatic (flag GPL/AGPL; not automatically prohibited)
- **Default contributions**: Not accepted (CLA/DCO analysis skipped unless triggered)

---

### Step 3: Load or Define Open-Source Policy

Check for the organization's open-source compliance policy in local settings
(e.g., `legal.local.md`, `oss-policy.md`, or similar configuration files).

The policy should define:

- **License approval tiers**: Which licenses are pre-approved, which require review,
  which are prohibited
- **Distribution-specific rules**: Different tier thresholds for SaaS vs. binary release
- **CLA/contributor requirements**: Which contributor agreements are accepted
- **SBOM requirements**: Format, frequency, distribution requirements
- **Governance**: Who approves Tier 3 decisions; escalation chain

**If no policy is found:**

**⟁ CLARIFY** — Inform the user that no organizational policy was found, and ask:

- **Option A: Configure policy now** — Walk through defining license approval tiers for
  this organization's specific distribution model and risk posture. Takes 5–10 minutes
  but makes this and all future audits precisely calibrated.
- **Option B: Use Legalcode default standards** — Apply the default tier framework below.
  Clearly label the audit: "Based on Legalcode default standards — not organizational policy."
- **Option C: Provide positions as findings arise** — Begin the audit and ask about
  organizational positions when classification depends on context.

**Default Policy Framework** (used when no organizational policy is configured):

| Tier       | Classification                    | Licenses                                                                                         | Distribution Models | Default Decision                                                       |
| ---------- | --------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------- | ---------------------------------------------------------------------- |
| **Tier 1** | Pre-approved                      | MIT, Apache 2.0, BSD-2-Clause, BSD-3-Clause, ISC, CC0-1.0, Unlicense, Boost, zlib                | All                 | Auto-approve; retain notices                                           |
| **Tier 2** | Conditional                       | LGPL v2.1, LGPL v3 (dynamic linking only), MPL 2.0 (file-level isolation), EPL 1.0/2.0, EUPL 1.2 | Binary + SaaS       | Approve with documented isolation strategy; legal review recommended   |
| **Tier 3** | Escalate to counsel               | GPL v2, GPL v3, AGPL v3, CDDL, OSL, custom licenses, dual-licensed with unclear terms            | Any                 | Legal review required before use in distribution                       |
| **Tier 4** | Prohibited (proprietary projects) | SSPL, BSL 1.1, Elastic License 2.0, Commons Clause (wrapper), non-commercial restrictions        | Any proprietary     | General prohibition; confirm with legal if business case exists        |
| **Tier X** | Unknown                           | No license specified, unidentified license, modified standard license                            | Any                 | Treat as "All Rights Reserved"; cannot use without explicit permission |

---

### Step 4: Scan or Validate the SBOM

If a pre-generated SBOM was provided, validate it:

- Confirm format (SPDX, CycloneDX, or NTIA-compliant)
- Verify completeness: are transitive dependencies included?
- Identify components with missing or ambiguous license data
- Note SBOM generation date; flag if older than 30 days for evolving projects

If no SBOM was provided, build one from the package manifests:

**By ecosystem:**

| Ecosystem     | Manifest Files                                           | Scanning Commands                                    |
| ------------- | -------------------------------------------------------- | ---------------------------------------------------- |
| npm / Node.js | package.json, package-lock.json, yarn.lock               | `npm list --all --json`, `syft .`, `trivy fs .`      |
| Python        | requirements.txt, Pipfile.lock, pyproject.toml, setup.py | `pip-licenses --format=json`, `syft .`               |
| Java / Kotlin | pom.xml, build.gradle, build.gradle.kts                  | Maven dependency:tree plugin, `syft .`               |
| Go            | go.mod, go.sum                                           | `go list -m all`, `syft .`                           |
| Rust          | Cargo.toml, Cargo.lock                                   | `cargo license`, `syft .`                            |
| Ruby          | Gemfile, Gemfile.lock                                    | `bundle exec license_finder`, `syft .`               |
| .NET / C#     | .csproj, packages.config, nuget.config                   | `dotnet list package --include-transitive`, `syft .` |

**Normalize to SBOM fields:**
For each direct and transitive dependency:

- Component name and version
- SPDX license identifier (or "NOASSERTION" if unknown)
- Copyright holder(s) if determinable
- Unique identifier (Package URL / PURL preferred; CPE as fallback)
- Source repository URL
- Dependency type (direct vs. transitive)
- Dependency path (which direct dependency requires this transitive)

**Scope note**: Record in the Glass Box audit trail whether the SBOM includes transitive
dependencies (complete) or direct-only (partial). Partial SBOMs may miss material
copyleft obligations.

---

### Step 5: Identify and Classify All Licenses

For each component in the SBOM, identify the applicable license and classify it.

**License identification confidence tiers:**

- **CONFIRMED** (>95%): SPDX identifier present in package metadata AND verified against
  LICENSE file in source repository. Machine-readable REUSE headers present in source files.
- **HIGH** (80–95%): SPDX identifier in package metadata; LICENSE file consistent.
- **MEDIUM** (60–80%): License inferred from package registry data or source code headers;
  not confirmed against full license text.
- **LOW** (<60%): License ambiguous, multiple candidate licenses, custom license text,
  or no license file found. Flag for manual verification.

**License classification (apply to each component):**

| License Family       | Examples                                           | Copyleft Strength                    | Patent Grant                             | Attribution Burden            |
| -------------------- | -------------------------------------------------- | ------------------------------------ | ---------------------------------------- | ----------------------------- |
| **Permissive**       | MIT, Apache 2.0, BSD-2, BSD-3, ISC, CC0            | None                                 | Silent (MIT/BSD) / Explicit (Apache 2.0) | Low                           |
| **Weak Copyleft**    | LGPL v2.1, LGPL v3, MPL 2.0, EPL 1.0/2.0, EUPL 1.2 | Library/file level                   | Explicit                                 | Medium                        |
| **Strong Copyleft**  | GPL v2, GPL v3, GPL-2.0-or-later                   | Full combined work                   | Silent (GPL v2) / Explicit (GPL v3)      | High                          |
| **Network Copyleft** | AGPL v3                                            | Full combined work + network service | Explicit                                 | High + Network source offer   |
| **Source-Available** | SSPL, BSL 1.1, Elastic License 2.0                 | N/A (non-OSI)                        | Varies                                   | Varies — read carefully       |
| **Creative Commons** | CC BY, CC BY-SA                                    | Varies — NOT for software            | None                                     | Medium                        |
| **No License**       | Unlicensed / missing                               | All Rights Reserved                  | N/A                                      | Cannot use without permission |

**Special classifications to flag explicitly:**

- **Dual-licensed**: Component offered under (License A OR License B). Identify which
  license the consumer is applying; document the choice. [VERIFY if upstream allows
  choice or requires specific selection criteria.]
- **GPL with Classpath Exception**: Allows linking with non-GPL code in specific
  circumstances. Verify exact exception text. [VERIFY: OpenJDK Classpath Exception
  text differs from GNU Classpath Exception.]
- **GPL "or later"**: SPDX `GPL-2.0-or-later` allows treating the code as GPL v3,
  unlocking Apache 2.0 compatibility. SPDX `GPL-2.0-only` does not permit this.
- **Modified / custom license**: Any license with modifications to a standard text.
  Treat as unknown; escalate to legal counsel. Do not assume standard license terms apply.

---

### Step 6: Analyze License Compatibility

**⟁ CLARIFY** — For complex projects with many license families, ask the user:

- Are all components used in a single combined binary, or are some distributed in separate
  executables/services? The combined-work analysis depends on architectural boundaries.

**Compatibility assessment matrix** (apply to every pair of license families present):

|                 | Permissive (MIT/BSD/ISC) | Apache 2.0  | LGPL | MPL 2.0 | GPL v2-only | GPL v3 / v2-or-later | AGPL v3     |
| --------------- | ------------------------ | ----------- | ---- | ------- | ----------- | -------------------- | ----------- |
| **Permissive**  | ✓                        | ✓           | ✓    | ✓       | ✓           | ✓                    | ✓           |
| **Apache 2.0**  | ✓                        | ✓           | ✓    | ✓       | ✗ ⚠         | ✓ (inbound)          | ✓ (inbound) |
| **LGPL**        | ✓                        | ✓           | ✓    | ✓       | ✓ → GPL     | ✓ → GPL v3           | ✓ → AGPL    |
| **MPL 2.0**     | ✓                        | ✓           | ✓    | ✓       | ✓ (§ 10.3)  | ✓ (§ 10.3)           | ✓ (§ 10.3)  |
| **GPL v2-only** | ✓                        | ✗ ⚠         | ✓    | ✓       | ✓           | ✗                    | ✗           |
| **GPL v3**      | ✓                        | ✓ (inbound) | ✓    | ✓       | ✗           | ✓                    | ✓ (→ AGPL)  |
| **AGPL v3**     | ✓                        | ✓ (inbound) | ✓    | ✓       | ✗           | ✓                    | ✓           |

**Legend**: ✓ = Compatible | ✗ = Incompatible | ⚠ = Special conditions — see below |
→ = Compatible but resulting combined work must be under the stronger license |
(inbound) = Code can be used IN the stronger-licensed project but not relicensed back

**Critical incompatibilities to flag immediately (HIGH/NON-COMPLIANT):**

1. **Apache 2.0 + GPL v2-only**: The Apache 2.0 patent retaliation clause (§ 3) conflicts
   with GPL v2's prohibition on "additional terms" (§ 6). A combined work containing both
   licenses cannot be legally distributed under either. Remediation: relicense GPL v2
   dependency to GPL v3 (if `GPL-2.0-or-later`), replace GPL v2 dependency with a
   permissive-licensed alternative, or use an architectural separation. [VERIFY per ASF
   license compatibility guidance at apache.org/licenses/GPL-compatibility.html]

2. **GPL v2-only + GPL v3**: The two versions are incompatible. A combined work with
   GPL-2.0-only and GPL-3.0-only code has no valid outbound license. [VERIFY: FSF's
   license compatibility list at gnu.org/licenses/license-compatibility.en.html]

3. **AGPL v3 + proprietary SaaS**: Even without distribution, an AGPL-licensed component
   used in a modified network service triggers source disclosure obligations under § 13.

4. **SSPL / BSL / non-OSI "source-available"**: These are not genuine open-source licenses.
   Commercial use restrictions vary significantly — read license text in full. Do not assume
   OSI/FSF compatibility. Escalate to Tier 4 (prohibited for most proprietary projects).

For each incompatibility found, identify:

- The specific components involved
- The applicable license provision driving the conflict
- The distribution model under which the conflict is triggered
- Whether the conflict is triggered in the organization's current distribution model

---

### Step 7: Analyze Copyleft Obligation Triggers

For each Strong Copyleft (GPL v2/v3) or Network Copyleft (AGPL v3) component, determine
whether obligations are triggered under the stated distribution model.

**GPL v2 / v3 triggers:**

| Action                                               | Trigger?      | Analysis                                                                                                                                                                 |
| ---------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Internal use only (no distribution)                  | No            | "Conveying" requires distribution to third parties; employees of one legal entity are not third parties                                                                  |
| Binary distribution to customers                     | **YES**       | Must provide Corresponding Source with the binary                                                                                                                        |
| SaaS (run on own servers, no binary distributed)     | No (GPL)      | The "SaaS loophole" — no distribution occurs; no obligation under GPL v2/v3                                                                                              |
| Static linking with proprietary code + distribution  | **YES**       | Static linking creates a combined work; entire distribution must be GPL                                                                                                  |
| Dynamic linking with proprietary code + distribution | **Contested** | FSF position: creates combined work even via dynamic linking if "designed to work together." Legal question unresolved. Treat as ATTENTION; escalate for counsel review. |
| Subsidiary use                                       | Depends       | Whether subsidiaries are "the same legal entity" is jurisdiction-specific. Treat inter-company transfers as external distribution conservatively.                        |

**LGPL v2.1 / v3 triggers:**

| Action                                                    | Trigger?                    | Analysis                                                                                           |
| --------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------- |
| Dynamic linking to unmodified LGPL library + distribution | No (LGPL v2.1)              | The LGPL exception: can use in proprietary software if dynamically linked and user can relink      |
| Static linking to LGPL library + distribution             | **YES**                     | Source disclosure obligation for the library; must provide object files for relinking              |
| Modifying the LGPL library + distribution                 | **YES (library only)**      | Source of the modified LGPL library must be distributed; proprietary application code is protected |
| LGPL v3 dynamic linking                                   | No (if relinking preserved) | LGPL v3 also prohibits preventing user from relinking; anti-tivoization applies                    |

**AGPL v3 triggers (§ 13 "Network Use"):**

| Action                                                                               | Trigger? | Analysis                                                                                                                                                            |
| ------------------------------------------------------------------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Internal use (employees only, no external users)                                     | No       | No "remote network interaction" by outside users                                                                                                                    |
| SaaS where users interact with **unmodified** AGPL code                              | **NO**   | § 13 only applies to "modified versions" — if no modifications, no source to disclose. Confirm precisely whether any modification has been made.                    |
| SaaS where users interact with **modified** AGPL code                                | **YES**  | Must "prominently offer" Corresponding Source to all users interacting remotely; typically: prominent link to source code from application UI                       |
| API service providing AGPL-powered functionality                                     | **YES**  | API interaction constitutes "remote network interaction" under § 13 if code is modified                                                                             |
| Unmodified AGPL used internally; external users interact only with proprietary layer | Depends  | If the proprietary layer is a "modified version" of the AGPL work, disclosure required. If they are separate works, no obligation. Architectural analysis required. |

**⟁ CLARIFY** — When trigger status is ambiguous (e.g., dynamic linking, SaaS + AGPL
modifications, inter-subsidiary distribution), ask:

- "Is the [AGPL/GPL] library statically or dynamically linked in the binary distribution?"
- "Have any modifications been made to the [AGPL] library, or is it used unmodified?"
- "Is the SaaS deployment internal to one legal entity, or accessible by external users?"

For each trigger analysis, record in the Glass Box:

- Trigger determination: YES / NO / CONTESTED
- Basis: Specific license provision
- Confidence: HIGH / MEDIUM / LOW with rationale

---

### Step 8: Analyze Attribution and NOTICE File Requirements

For each component, determine the attribution obligations and assess current compliance.

**Per-license attribution obligations:**

| License      | Copyright Notice                 | License Text                | NOTICE File                              | Modification Notice            | Source Headers                        |
| ------------ | -------------------------------- | --------------------------- | ---------------------------------------- | ------------------------------ | ------------------------------------- |
| MIT          | Required (all copies)            | Required                    | Not required                             | Not required                   | Preserve existing                     |
| Apache 2.0   | Required                         | Required                    | **Required if upstream has NOTICE file** | Required in modified files     | Preserve; add SPDX headers            |
| BSD-2-Clause | Required (source + binary)       | Required                    | Not required                             | Not required                   | Preserve existing                     |
| BSD-3-Clause | Required (source + binary)       | Required                    | Not required                             | Not required                   | Preserve; non-endorsement applies     |
| GPL v2/v3    | Required (all copies)            | Required (full text)        | Recommended                              | **Required** (prominent; date) | Required in each file                 |
| LGPL v2.1/v3 | Required                         | Required (LGPL + GPL texts) | Recommended                              | Required in modified files     | Required                              |
| AGPL v3      | Required                         | Required                    | Recommended                              | Required                       | Required; + source offer notice in UI |
| MPL 2.0      | Required (in modified MPL files) | Required                    | Recommended                              | Required in modified files     | Required for MPL files                |
| ISC          | Required                         | Required                    | Not required                             | Not required                   | Preserve existing                     |

**Apache 2.0 § 4 NOTICE file analysis:**
The NOTICE file obligation (§ 4(d)) is among the most commonly missed. If an upstream
Apache-2.0-licensed component ships a NOTICE file, its contents must be included in your
own NOTICE file, documentation, or a display shown to users. Check each Apache 2.0
dependency for an upstream NOTICE file. Failure to carry NOTICE content is an Apache
attribution violation, not a copyleft violation — lower risk, but still a compliance gap.

**AGPL v3 § 13 source offer notice:**
If an AGPL trigger is active, the application's interactive interface must display an
"Appropriate Legal Notice" that includes: (1) copyright notice, (2) GPL warranty disclaimer,
(3) notice that the program is covered by AGPL, and (4) a URL or means to receive the
Corresponding Source. This notice must be "prominent" — burying it in terms of service
or an obscure about page may not satisfy the requirement. [VERIFY: FSF guidance on what
constitutes "prominent" display under AGPL § 13.]

**Attribution gap assessment:**

- Does the project have a LICENSE file at root? Required for virtually all licenses.
- Does the project have a NOTICE file? Required for Apache 2.0 with upstream NOTICE files.
- Does the project have a THIRD-PARTY-NOTICES or LICENSES/ directory? Best practice for
  binary distributions with multiple dependencies.
- Are copyright notices preserved in source file headers?
- For binary distributions: Is license information available to end users? (Embedded in binary,
  bundled in distribution archive, linked from product UI or documentation.)

---

### Step 9: Analyze Patent Grant and Retaliation Clause Risk

Assess patent dimensions for each component with explicit patent terms.

**Patent grant presence by license:**

| License            | Patent Grant                                                                          | Retaliation Clause                                                          | Risk Level                                                   |
| ------------------ | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------ |
| MIT                | None (silent)                                                                         | None                                                                        | LOW (no explicit patent protection)                          |
| BSD variants       | None (silent)                                                                         | None                                                                        | LOW                                                          |
| ISC                | None (silent)                                                                         | None                                                                        | LOW                                                          |
| **Apache 2.0 § 3** | **Explicit — covers contributor's patents necessarily infringed by the contribution** | **YES: terminates if licensee sues Apache project for patent infringement** | MEDIUM (retaliation risk if org has active patent portfolio) |
| GPL v2             | Silent — no explicit grant                                                            | None                                                                        | LOW (implicit grant assumed but not guaranteed)              |
| **GPL v3 § 11**    | **Explicit — downstream protection; "no further restrictions" on patents**            | **YES: defensive termination (§ 8)**                                        | LOW — protective for downstream users                        |
| LGPL v3            | Same as GPL v3 (§ 11 incorporated)                                                    | YES (defensive)                                                             | LOW                                                          |
| **MPL 2.0 § 2.1**  | **Explicit — covers contributor's patents for contributions**                         | **YES: terminates if licensee sues contributor regarding covered software** | MEDIUM                                                       |
| EPL 1.0/2.0        | Explicit — covers contributor's patent claims                                         | YES                                                                         | MEDIUM                                                       |
| AGPL v3            | Same as GPL v3                                                                        | YES (defensive)                                                             | LOW                                                          |

**Apache 2.0 retaliation clause analysis (§ 3.3):**

The Apache 2.0 patent retaliation clause (§ 3.3) reads in relevant part: "If You institute
patent litigation against any entity... alleging that the Work or a Contribution incorporated
within the Work constitutes direct or contributory patent infringement, then any patent
licenses granted to You under this License... shall terminate." This is a **defensive**
clause protecting contributors from offensive patent assertions by downstream users.

Enterprise risk: If the organization has an **active offensive patent portfolio** and sues
any entity in relation to an Apache 2.0 project, all Apache 2.0 patent grants for that
project terminate. This may not affect usage rights (copyright license is separate) but
eliminates the patent license protection. Recommend flagging for patent counsel review
when the organization actively asserts patents.

**⟁ CLARIFY** — If the organization has an active patent portfolio that may overlap
with Apache 2.0 or MPL 2.0 projects in the SBOM:

- "Does your organization regularly assert patents offensively against third parties?"
- "Are any pending or planned patent assertions related to technologies used by
  Apache 2.0 or MPL 2.0 components in this project?"
- _Why this matters_: Patent retaliation clauses create a legal interdependency between
  OSS licensing strategy and offensive IP strategy that patent counsel should coordinate.

---

### Step 10: Review CLA and Contributor Agreement Status

Apply when the project accepts code contributions from external contributors.

Skip this step if: no external contributions are accepted (document in Glass Box).

**ICLA (Individual CLA) review checklist:**

- [ ] Copyright: Is the ICLA a copyright assignment (full ownership transfer) or a
      broad copyright license grant? Assignment allows project to relicense freely;
      license grant may restrict relicensing.
- [ ] Patent grant: Does the ICLA include an explicit patent license from the contributor?
      Without a patent grant, contributors retain patent rights over their contributions.
- [ ] Work confirmation: Does the ICLA require the contributor to confirm their contribution
      is original (not work-for-hire by another employer)?
- [ ] Employer consent: If contributor is employed, is employer consent addressed
      (separate employer/company CLA, or ICLA representation that employer has waived rights)?
- [ ] Moral rights: Does the ICLA address moral rights waiver? Material in EU jurisdictions
      where moral rights are inalienable. [JURISDICTION-SPECIFIC]
- [ ] Termination: Can contributors revoke the license grant? Best practice: irrevocable
      for accepted contributions.
- [ ] Relicensing rights: Does the project have the right to sublicense under different
      terms? If using a commercial dual-licensing model, the ICLA must grant this.
- [ ] Reference standard: Apache Software Foundation ICLA is the industry benchmark.
      [VERIFY current ASF ICLA text at apache.org/licenses/icla.pdf]

**CCLA (Corporate CLA) review checklist:**

- [ ] Signatory authority: Does the CCLA represent that the signatory has authority to
      bind the corporation?
- [ ] Employee scope: Does the CCLA require the employer to maintain a list of covered
      employees? Contributions from employees not on the list may create gaps.
- [ ] Scope of employment: Does the CCLA address contributions made within the scope of
      employment vs. personal contributions?
- [ ] Termination: Can the CCLA be terminated? What happens to existing contributions
      if the CCLA is terminated?

**DCO (Developer Certificate of Origin) review checklist:**

- [ ] Sign-off format: Does the project require `Signed-off-by:` in every commit? Is
      this enforced via CI/CD (e.g., GitHub DCO check)?
- [ ] DCO version: Is the DCO version specified? Reference the Linux Foundation DCO v1.1.
- [ ] Limitations: DCO is NOT a CLA. It does not provide an explicit patent grant from
      contributors; it certifies only provenance, not a grant of additional rights. If the
      project intends to pursue dual licensing or needs explicit patent grants, a CLA is
      required. [VERIFY: Kyle E. Mitchell's "DCO Is Not a CLA" is the key reference.]
- [ ] Retroactive coverage: DCO does not retroactively cover contributions made before
      DCO adoption. If historical contributions were made without CLA/DCO, their license status
      depends on implied license from project context.

**CLA gap risk assessment:**

If the project accepts contributions without any CLA or DCO:

- Copyright chain is broken: Multiple contributors retain independent copyrights
- Relicensing is impossible without tracking down and obtaining consent from all contributors
- If a contributor asserts employment-related ownership, the contribution may need to be
  removed
- Patent risk: Contributor retains patent rights over their contributions; no implicit
  patent grant for the project

Classification: ATTENTION (if contributions are informal/recent and low-volume) or
NON-COMPLIANT (if the project is commercially distributed and has hundreds of contributors
without any contributor agreement).

---

### Step 11: Assess SBOM Completeness Against Regulatory Requirements

Evaluate the SBOM against applicable regulatory standards based on distribution model
and geography.

**EO 14028 / NTIA minimum elements (US federal software sales):**

| Field                               | Required | Present in SBOM? | Gap? |
| ----------------------------------- | -------- | ---------------- | ---- |
| Supplier name                       | Required | [Yes/No]         |      |
| Component name                      | Required | [Yes/No]         |      |
| Version of the component            | Required | [Yes/No]         |      |
| Other unique identifiers (PURL/CPE) | Required | [Yes/No]         |      |
| Dependency relationship             | Required | [Yes/No]         |      |
| Author of the SBOM data             | Required | [Yes/No]         |      |
| Timestamp (SBOM data creation date) | Required | [Yes/No]         |      |

**EU CRA (Regulation 2024/2847) requirements (commercial products in EU market):**

From September 2026, manufacturers of products with digital elements must:

- Identify and document components in the product
- Generate SBOM in a "commonly used and machine-readable format" covering at minimum
  top-level dependencies (Annex I Part II)
- Maintain SBOM in technical documentation for **10 years** after market placement
- Make SBOM available to market surveillance authorities on request
- Keep SBOM current through the product maintenance cycle

[JURISDICTION-SPECIFIC: EU CRA applicability] Applies to commercial software products
placed on the EU market by manufacturers with a commercial presence. Pure non-commercial
OSS developers without monetization are largely exempt. "Stewards" of non-commercial OSS
projects have lighter obligations. Confirm applicability based on organizational structure
and commercialization model. [VERIFY current CRA delegated acts and technical standards
issued by ENISA.]

**SBOM format assessment:**

| Format                          | Standard         | Recommended Use                                                                |
| ------------------------------- | ---------------- | ------------------------------------------------------------------------------ |
| **SPDX** (ISO/IEC 5962:2021)    | Linux Foundation | License compliance; primary format for EO 14028 compliance                     |
| **CycloneDX**                   | OWASP            | Security/vulnerability management; preferred for CRA and supply chain analysis |
| **SWID Tags** (ISO/IEC 19770-2) | ISO              | Enterprise software asset management                                           |

Best practice: Generate both SPDX (for license compliance) and CycloneDX (for vulnerability
management) as part of the release pipeline.

---

### Step 12: Generate Compliance Classification and Action Plan

Synthesize findings from Steps 5–11 into an overall compliance classification.

Apply the three-tier classification system:

**COMPLIANT**: All license obligations satisfied for the stated distribution model.
No unresolved compatibility conflicts. Attribution requirements met. SBOM complete.
No untriggered copyleft obligations.
→ Action: Document compliance status; schedule re-audit before next release or
significant dependency update.

**ATTENTION**: Minor compliance gaps or risk areas requiring review before next
production release. Low-to-medium risk. Typically resolvable with moderate effort.
→ Action: Implement recommended remediations within defined timeline; re-audit
before next release.

**NON-COMPLIANT**: Critical compliance gaps that prevent lawful distribution in the
current form under the stated distribution model. Requires immediate action.
→ Action: Halt distribution of affected build until remediated; escalate to legal
counsel; implement remediation on defined timeline.

---

## License Analysis Reference

### License Deep-Dive: Apache 2.0

**Legal nature**: Permissive with explicit patent grant. The most commercially important
permissive license after MIT. Apache Software Foundation template.

**Key provisions:**

- § 3: Explicit patent grant from each contributor covering "patent claims necessary
  to make, use, sell, and distribute the Contribution alone or as part of the Licensed Work"
- § 3.3 (retaliation): Patent grants terminate if licensee initiates patent litigation
  alleging the Licensed Work infringes a patent
- § 4(a): Must retain copyright, patent, trademark, and attribution notices
- § 4(b): Must include a copy of the License
- § 4(c): Must carry prominent notice in modified files stating changes were made
- § 4(d): If the Work includes a NOTICE text file, must reproduce that file's
  attribution notices in all derivative works

**Common compliance failures**: Failing to carry upstream NOTICE file contents; stripping
copyright headers from modified files; not stating modifications in file headers.

**Compatibility risk**: Incompatible with GPL v2-only (due to patent retaliation clause
vs. GPL v2 § 6 no-additional-restrictions rule). Compatible with GPL v3. [VERIFY]

---

### License Deep-Dive: GPL v2 and GPL v3

**GPL v2 key provisions:**

- § 2(a): Must cause modified files to carry prominent notices stating changes were made
- § 3: May copy and distribute source code (or provide binding written offer to provide
  source code for three years)
- § 4: License terminates automatically upon any violation; no cure period specified
- § 5: Mere aggregation is not a combined work; independent programs on same storage medium
  do not trigger GPL
- § 6: No further restrictions on recipients' exercise of GPL rights
- § 7: If conditions (patent license, court order, etc.) impose restrictions that conflict
  with GPL, distributors must refrain from distributing rather than add restrictions

**GPL v3 additions over GPL v2:**

- § 6: Anti-tivoization — must provide installation information for User Products
- § 7: Additional permissions allowed (enables Apache 2.0 → GPL v3 compatibility)
- § 8: Explicit 30-day cure period for first-time violations; license reinstated if
  compliant within 30 days of notice [VERIFY: cure period is conditioned on specific facts]
- § 11: Explicit patent grant and "no additional restrictions" on patents; automatic
  downstream patent protection; defensive termination

**GPL v3 cure provision (§ 8):**
First-time violations are automatically cured if the violator complies within 30 days of
notice by the copyright holder AND has not received prior notice of violation. This is a
meaningful commercial benefit: enterprises that discover a GPL compliance gap can cure
without automatic copyright termination if they act promptly. [VERIFY: cure provision
applies to GPL v3 only; GPL v2 has no explicit cure mechanism.]

---

### License Deep-Dive: AGPL v3

**§ 13 (Remote Network Interaction):**
Adds to the GPL v3 framework: "if you modify the Program, your modified version must
prominently offer all users interacting with it remotely through a computer network... an
opportunity to receive the Corresponding Source of your version by providing access to
the Corresponding Source from a network server at no charge."

**Trigger analysis:**

- "Modify the Program": If no modifications, § 13 does not apply (no Corresponding Source
  to disclose for an unmodified copy). This is the key distinction from GPL v3.
- "Remotely through a computer network": HTTP, HTTPS, gRPC, WebSocket, REST, SOAP — any
  mechanism for remote interaction. Not limited to "interactive" use in the traditional sense.
- "Prominently offer": Typical implementation: a link in the application's "About" page,
  in the API response headers, or in the service's documentation. FSF guidance: must be
  as easy to find as the service itself.

**Design implications for SaaS:**
AGPL is functionally incompatible with a "black box" SaaS architecture built on AGPL
components. If your SaaS relies on modified AGPL code, your source must be available
to all users. Many enterprises maintain categorical AGPL prohibitions for this reason.

**Notable AGPL-licensed projects**: PostgreSQL has its own license; Nextcloud, Mastodon,
Grafana OSS, SuiteCRM, ownCloud core.

---

### License Deep-Dive: LGPL v2.1 and v3

**The dynamic linking exception:**
LGPL v2.1 § 6 allows proprietary code to be combined with an LGPL library if: (1) the
library is linked dynamically (not statically compiled into the binary); (2) the licensee
provides a copy of the LGPL library source or a reference to where it can be obtained;
(3) the user can relink the proprietary application with a modified version of the library.

**LGPL v2.1 vs. v3:**
LGPL v3 builds on GPL v3 (incorporating it by reference) and adds LGPL-specific provisions.
The key difference from LGPL v2.1: LGPL v3 also prohibits tivoization with respect to
the library — manufacturers of embedded devices must allow users to replace the LGPL
library even on otherwise locked hardware.

**Static linking consequences:**
Static linking triggers the LGPL copyleft for the library itself. The proprietary
application code does not need to be disclosed, but: (1) the LGPL library source must
be provided; (2) object files sufficient for relinking must be provided; (3) all LGPL
requirements (license text, copyright notices, source offer) must be met.

---

## Compliance Severity Classification

### COMPLIANT

**Definition:** All license obligations satisfied for the stated distribution model.

**Sub-classifications:**

- **COMPLIANT — Fully Permissive**: Only MIT, Apache 2.0, BSD, ISC, CC0 licenses present.
  Minimal compliance burden; only attribution requirements apply.
- **COMPLIANT — Weak Copyleft Isolated**: LGPL/MPL components present and properly isolated
  (dynamic linking verified; no static linking; source release plan for library documented).
- **COMPLIANT — Open-Source Release**: Project is fully open-sourced under GPL/AGPL;
  source code is publicly distributed. All copyleft obligations satisfied by open-source release.
- **COMPLIANT — Internal Use Only**: Strong copyleft present but distribution model is
  internal-only; no conveyance occurs; no copyleft obligations triggered.

**Required evidence for COMPLIANT classification:**

- Complete SBOM confirming all licenses identified
- Attribution requirements documented and implemented
- No unresolved compatibility conflicts
- Copyleft trigger analysis documented (NOT TRIGGERED for each strong/network copyleft component)
- SBOM completeness confirmed for applicable regulatory standards

---

### ATTENTION

**Definition:** Compliance gaps or risk areas requiring review before next production release.

**Sub-classifications (list all that apply):**

| Sub-Classification                             | Description                                                                                                               | Typical Severity                |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| ATTENTION — Apache 2.0 Patent Retaliation Risk | Org has active patent portfolio; Apache 2.0 retaliation clause creates patent strategy dependency                         | LOW–MEDIUM                      |
| ATTENTION — Weak Copyleft Unverified Isolation | LGPL/MPL present; dynamic vs. static linking not confirmed                                                                | MEDIUM                          |
| ATTENTION — Weak Copyleft Source Obligation    | LGPL library modified and distributed; source release obligation triggered for library                                    | MEDIUM                          |
| ATTENTION — Attribution Gaps                   | Missing NOTICE file, copyright notices, or Apache upstream NOTICE content                                                 | LOW–MEDIUM                      |
| ATTENTION — CLA/Contributor Agreement Gaps     | Contributions accepted without formal CLA or DCO                                                                          | MEDIUM                          |
| ATTENTION — Dual-Licensed (Unresolved Choice)  | Component dual-licensed; distribution license not documented                                                              | MEDIUM                          |
| ATTENTION — Unknown / Unverified License       | Component license not confirmed against source                                                                            | MEDIUM                          |
| ATTENTION — SBOM Incomplete                    | Transitive dependencies not included; gaps in SBOM fields                                                                 | MEDIUM                          |
| ATTENTION — Tier 3 License Present             | GPL v2/v3 or AGPL present; distribution model analysis indicates no current trigger but trigger possible if model changes | HIGH (if model change imminent) |
| ATTENTION — Non-OSI License                    | Source-available license (SSPL, BSL) present; commercial use terms require legal review                                   | MEDIUM–HIGH                     |
| ATTENTION — GPL v2 "or later" Missing          | GPL v2-only dependency creates Apache 2.0 incompatibility; resolution depends on whether "or later" is available          | HIGH                            |

---

### NON-COMPLIANT

**Definition:** Critical compliance gaps preventing lawful distribution in current form.

**Sub-classifications:**

| Sub-Classification                                              | Description                                                                                                               | Legal Risk                                                                                    |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| NON-COMPLIANT — GPL in Proprietary Binary Distribution          | GPL v2/v3 component statically linked or otherwise creating combined work in proprietary binary; source code not provided | Copyright infringement; injunction risk; statutory damages                                    |
| NON-COMPLIANT — AGPL in Modified Proprietary SaaS               | AGPL component modified; network service provided to external users; source code not disclosed                            | Same as GPL + AGPL enforcement risk                                                           |
| NON-COMPLIANT — Unresolvable License Conflict                   | Two incompatible licenses (e.g., Apache 2.0 + GPL v2-only) in combined work with no resolution path                       | Distribution of combined work is unlicensed; copyright infringement by both copyright holders |
| NON-COMPLIANT — No License Specified (Critical Dependency)      | Material dependency has no license file; "All Rights Reserved" applies                                                    | Using unlicensed software is copyright infringement without explicit permission               |
| NON-COMPLIANT — Missing Source Code (GPL/AGPL)                  | Copyleft obligation triggered; binary/service distributed without corresponding source offer                              | GPL license termination; copyright infringement; injunction risk                              |
| NON-COMPLIANT — Static Linking LGPL Proprietary                 | LGPL library statically linked in proprietary distribution; source and object files not provided                          | Weaker than GPL violation but still LGPL infringement                                         |
| NON-COMPLIANT — Contributor IP Unclear                          | Commercial distribution from project with unverified contributor IP ownership; no CLA/DCO                                 | Potential copyright infringement claims from contributors; relicensing impossible             |
| NON-COMPLIANT — Non-OSI License Commercial Restriction Violated | Software used in violation of commercial-use restriction in source-available license                                      | Breach of license terms; potential contractual liability                                      |

---

## Actionable Output per Finding

For each finding at ATTENTION or NON-COMPLIANT severity, produce:

```
**Finding ID**: [YYYY-MM-DD-NNN]
**Component**: [name@version] (path: [dependency path])
**License**: [SPDX identifier]
**Classification**: [NON-COMPLIANT / ATTENTION] — [Sub-classification]
**Trigger**: [Distribution model + license provision triggering the finding]
**Current State**: [What is present; what is missing; what is violated]

**Legal Risk**:
- [Specific risk: copyright infringement, license termination, injunction, damages]
- [Relevant case law or statutory authority — mark [VERIFY] if unconfirmed]
- [Confidence: HIGH / MEDIUM / LOW with rationale]

**Remediation Options** (ranked by feasibility):
1. [Option 1]: [Description, effort, timeline, tradeoffs]
2. [Option 2]: [Description, effort, timeline, tradeoffs]
3. [Option 3]: [Description, effort, timeline, tradeoffs]

**Recommended Action**: [Specific action + timeline]
**Escalation**: [Who to involve: Engineering / Legal / Product / Patent Counsel]
```

---

## Prioritization Framework

### Tier 1 — Immediate (Block Distribution Until Resolved)

Issues where distribution in current form constitutes copyright infringement:

- GPL/AGPL copyleft obligation triggered; source code not provided
- Unresolvable license conflict (two incompatible licenses in combined work)
- Non-OSI commercial restriction violated
- Critical dependency with no license; all rights reserved

### Tier 2 — Short-Term (Resolve Before Next Release)

Issues that do not currently trigger infringement but create material legal risk if
the distribution model or architecture changes:

- LGPL isolation not verified (static vs. dynamic linking unconfirmed)
- GPL/AGPL present in Tier 3; close monitoring required
- Attribution gaps (NOTICE file missing; copyright notices stripped)
- CLA/contributor agreement gaps in commercially distributed project
- SBOM incomplete (transitive dependencies missing)

### Tier 3 — Medium-Term (Address in Next Quarter)

Issues that are informational, strategic, or lower-severity:

- Apache 2.0 patent retaliation clause risk (active patent portfolio)
- GPL v2-only + Apache 2.0 conflict in non-distributed internal tools
- Dual-licensed component with undocumented license choice
- SBOM format upgrade (SPDX only → add CycloneDX for security compliance)
- Open-source policy documentation gaps

**Negotiation strategy**: Resolve Tier 1 before any distribution. Tier 2 items can be
scheduled but must be tracked; do not allow them to become Tier 1 by deferring as
distribution model changes. Tier 3 items are candidates for quarterly compliance sprints.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                    | Fail Action                                                 |
| -------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific license provision (§ number), statute, or established precedent                      | Add citation or mark "[UNVERIFIED — counsel to confirm]"    |
| **Format**     | License citations use SPDX identifiers; case citations follow standard format (Parties, Court, Year)                    | Fix format                                                  |
| **Currency**   | Every license text reference checked for version accuracy; statutory references checked for amendments                  | Flag "[CHECK CURRENCY — may have been amended or replaced]" |
| **Domain**     | Analysis stays within the license's governing law scope; no jurisdiction-specific concepts stated as universal          | Remove or flag with [JURISDICTION-SPECIFIC] marker          |
| **Confidence** | Uncertainty explicitly stated; contested legal questions (dynamic linking, AGPL modification threshold) flagged as such | Add confidence qualifier; recommend legal counsel review    |

### Self-Interrogation for NON-COMPLIANT Items

For any finding classified as NON-COMPLIANT, apply this 3-pass review before delivery:

**Pass 1 — Trigger Chain Integrity**: Does the copyleft/attribution obligation
actually apply to this component under this distribution model? Is there an exception
(Classpath Exception, mere aggregation, internal-use-only, no modifications to AGPL
code) that changes the analysis? Would the copyright holder's own published guidance
(FSF FAQ, ASF guidance) support or contradict this classification?

**Pass 2 — Completeness**: Have all relevant factors been considered? Is the dependency
path correctly traced? Is the linking type correctly characterized? Has the
distribution model been verified with the user? Are there alternative interpretations
supported by industry practice or enforcement guidelines?

**Pass 3 — Challenge**: What is the strongest argument that this finding is ATTENTION,
not NON-COMPLIANT? Under what facts or architectural assumptions would the obligation
not be triggered? Is remediation feasible within the production timeline, or does
escalation need to happen first?

Mark the audit trail: `self_interrogation: PASS` or `self_interrogation: REVISED [reason]`.

### Confidence Scoring

For each material finding, assign a confidence level:

| Level        | Range     | Meaning                                                                             | Action                                                           |
| ------------ | --------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear license text; settled by enforcement guidance; unambiguous trigger            | State with confidence                                            |
| **High**     | 0.80–0.94 | Strong authority; minor interpretive questions; consistent with industry practice   | State with brief caveat                                          |
| **Probable** | 0.60–0.79 | Good arguments; some ambiguity (e.g., dynamic linking analysis)                     | State with explicit reasoning + contra-indicators                |
| **Possible** | 0.40–0.59 | Genuinely uncertain (e.g., "combined work" analysis for loosely coupled components) | Flag for legal counsel review with both positions                |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                                             | Do not assert; flag as "[UNCERTAIN — legal counsel must advise]" |

---

## Glass Box Audit Trail

Every compliance audit output MUST include a Glass Box section at the end:

```yaml
glass_box:
  skill: "legalcode-open-source-license-compliance"
  audit_date: "[ISO 8601 date]"
  project: "[Project name / repository path]"
  sbom_source: "[Pre-supplied SBOM / Generated from manifests / Partial (direct only)]"
  sbom_format: "[SPDX / CycloneDX / Custom / Not generated]"
  total_components: "[N direct + N transitive]"
  licenses_identified: "[N unique SPDX identifiers]"
  licenses_unidentified: "[N components with unknown/missing license]"
  distribution_model: "[User-stated model + any assumptions made]"
  organizational_policy: "[Custom policy loaded / Legalcode defaults applied]"
  copyleft_triggers_analyzed:
    - "[Component] — [Trigger] — [Determination: YES/NO/CONTESTED] — [Confidence]"
  compatibility_conflicts: "[N found — list by pair]"
  legalcode_mcp: "Connected / Not connected"
  citation_verification:
    - "[Case/statute cited] — VERIFIED (legalcode-mcp) / UNVERIFIED [VERIFY]"
  self_interrogation: "PASS / REVISED [items] / NOT APPLICABLE (no NON-COMPLIANT findings)"
  overall_classification: "COMPLIANT / ATTENTION / NON-COMPLIANT"
  overall_confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Transitive dependencies not fully analyzed]"
    - "[CLA review skipped — no contributions accepted]"
    - "[SBOM generated from manifests; binary scanning not performed]"
    - "[Dynamic vs. static linking not confirmed for LGPL components]"
  reviewer: "AI-assisted — requires qualified IP/copyright counsel review before distribution"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in open-source license compliance analysis:

1. **Analyzing only direct dependencies** — 80–90% of code in modern projects is transitive
   dependencies. A clean top-level dependency tree can hide GPL/AGPL obligations several
   layers deep. Always analyze the full transitive tree.

2. **Treating MIT and Apache 2.0 as equivalent** — MIT has no explicit patent grant; Apache
   2.0 has an explicit patent grant but adds a retaliation clause. For organizations with
   offensive patent portfolios, Apache 2.0 creates an IP strategy dependency that MIT does not.

3. **Assuming "open source = free to use commercially"** — Source-available licenses (SSPL,
   BSL 1.1, Elastic License 2.0) are not open-source by OSI definition. They may prohibit
   specific commercial uses. Always check whether a license is OSI-approved before assuming
   commercial use is unrestricted.

4. **Confusing the SaaS loophole and AGPL** — GPL (v2 and v3) does NOT require source
   disclosure for SaaS deployments. AGPL v3 does — but only for **modified** versions
   provided to external network users. The analysis differs by license AND by modification
   status AND by user type. Treating all copyleft as triggering SaaS source disclosure is
   incorrect; treating AGPL as irrelevant to SaaS is also incorrect.

5. **Treating dynamic linking as a universal LGPL escape hatch** — LGPL v2.1's dynamic
   linking exception is real but conditioned: the user must be able to relink with a
   modified version of the library. For embedded systems, IoT, or static architectures
   where relinking is prevented, the dynamic linking exception may not apply even if the
   linking is technically dynamic at the OS level.

6. **Claiming GPL v2 compatibility with Apache 2.0** — Apache 2.0's patent retaliation
   clause conflicts with GPL v2's prohibition on additional restrictions. This is one of
   the most common license mistakes in enterprise codebases. The Apache Software Foundation
   explicitly documents this incompatibility at apache.org. Do not claim compatibility
   without citing a specific analysis showing why it does not apply.

7. **Ignoring the "or later" clause** — A GPL-licensed dependency that specifies
   "GPL-2.0-or-later" (SPDX) can be used under GPL v3, resolving many incompatibilities.
   A dependency that specifies "GPL-2.0-only" cannot. Verify the exact SPDX identifier;
   do not assume a deprecated GPL v2 reference means "or later."

8. **Skipping NOTICE file propagation for Apache 2.0 dependencies** — The Apache 2.0
   § 4(d) NOTICE file obligation is commonly missed. If any transitive dependency ships
   an upstream NOTICE file, those attributions must be propagated. Binary distributions
   must include these notices in documentation, a bundled file, or a displayed attribution.

9. **Relying on CLA without reviewing CLA terms** — Not all CLAs are equivalent. A CLA
   that assigns copyright outright may prevent contributors from using their own code
   later. A CLA that grants only a license may prevent the project from relicensing
   commercially. Review CLA terms against project needs before accepting contributions.

10. **Using DCO when the project needs a CLA** — DCO is a provenance certification, not
    a contributor license agreement. It does not provide an explicit patent grant from
    contributors. If the project requires explicit patent grants (e.g., for dual licensing
    or patent-sensitive commercial use), a CLA is required. "We use the DCO therefore we
    have IP clarity" is incorrect for projects with patent exposure.

11. **Generating SBOM only from declared dependencies** — Package.json `dependencies` and
    `devDependencies` may not reflect all code present in the distributed artifact. Build
    tools may bundle unlisted dependencies; vendored code may not be tracked. Binary-level
    scanning (Black Duck, FOSSA) is required for full SBOM accuracy.

12. **Treating license compliance as a one-time event** — Dependencies update continuously;
    licenses can change between versions (e.g., HashiCorp's switch from MPL 2.0 to BSL 1.1
    in August 2023). A compliance status that is COMPLIANT today may be NON-COMPLIANT after
    a dependency update. Integrate SBOM generation and license scanning into CI/CD pipelines.

13. **Applying enforcement precedent extraterritorially** — GPL enforcement cases are highly
    jurisdiction-specific. US precedent (Jacobsen v. Katzer) does not automatically apply in
    EU courts; German enforcement procedure (injunctions via gpl-violations.org) does not
    reflect US practice. Analyze enforcement risk under the jurisdictions relevant to your
    distribution territory.

14. **Assuming open-source contributors have clear IP ownership** — Contributors may be
    creating code within the scope of their employment (making the employer the copyright
    holder), using code from other projects with license restrictions, or incorporating
    AI-generated code with contested provenance. Without a CLA that includes a provenance
    warranty, these risks are unmanaged.

15. **Treating "no license means it's public domain"** — Absence of a license file means
    "All Rights Reserved" under default copyright law in most jurisdictions. A project
    with no LICENSE file cannot legally be forked, distributed, or incorporated without
    explicit permission from the copyright holder. This is one of the most expensive
    assumptions in enterprise development.

16. **Ignoring source-available license commercial restrictions in M&A context** — In
    acquisitions or asset purchases, SSPL/BSL/Elastic License components in the target's
    codebase create limitations on the acquirer's ability to operate the product at scale
    or change the commercialization model. Due diligence must identify source-available
    license exposure.

17. **Assuming GPL enforcement requires the FSF** — Copyright enforcement can be brought
    by any copyright holder. For projects with contributions from many developers, any
    individual contributor may independently enforce GPL compliance. The SFC enforces on
    behalf of member projects. Consumers may soon have standing as third-party beneficiaries
    (SFC v. Vizio). The enforcement universe is wider than most organizations assume.

18. **Confusing license compatibility with license relicensing** — Apache 2.0 code can be
    included in a GPL v3 project (inbound compatibility), but that does not mean the
    Apache-licensed code is now GPL v3. The individual files retain their Apache 2.0 license;
    only the combined work is distributed under GPL v3. Relicensing requires copyright
    holder consent.

19. **Missing the EU CRA SBOM retention obligation** — The EU CRA requires 10-year SBOM
    retention (Regulation 2024/2847, Annex I Part II). Organizations generating SBOMs only
    for current releases without archiving them will be non-compliant with CRA documentation
    requirements. Build SBOM archival into the release management process.

20. **Skipping the Glass Box audit trail** — An OSS compliance audit without documented
    reasoning is not reproducible, auditable, or defensible if challenged. The Glass Box
    audit trail is not optional — it is the evidence that the analysis was performed
    systematically and that limitations were disclosed.

---

## Writing Standards

Apply plain-language discipline to all compliance output:

**For finding descriptions** (may be shared with engineering teams):

- Active voice: "This component uses a GPL v3 license that requires..." not "It has been
  determined that GPL v3 requires..."
- Name the license and provision: "Apache 2.0 § 4(d) requires reproducing the NOTICE file"
  not "attribution requirements may apply"
- Specific, not vague: "The LGPL v2.1 dynamic linking exception applies only if the
  user can relink with a modified library" not "LGPL may allow commercial use"
- Short sentences. One obligation per sentence.
- Mark uncertainty: Any contested legal question (dynamic linking, combined work test)
  must be flagged as contested; do not present debated positions as settled law.

**For remediation recommendations** (used by product and engineering teams):

- Action-first: "Replace [component] with [alternative]" not "Consideration should be
  given to replacing [component]"
- Specify the effort and timeline: "Medium effort (code refactoring); target 2-4 weeks"
- Provide specific alternatives: Name the competing library, not just "an alternative"
- Include fallback position: If the primary remediation is not feasible, provide Option 2

**For escalation recommendations** (used by legal and business stakeholders):

- Name the legal risk precisely: "Copyright infringement under GPL v3 § 4; exposure to
  statutory damages up to $150,000 per work (willful infringement) under 17 U.S.C. § 504(c)
  [VERIFY current statute and damages scale]"
- Reference recent enforcement precedent where applicable
- Distinguish between clear violations and contested interpretations

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool
for verifying license texts, statutory provisions, and case law.

**With legalcode-mcp connected (preferred):**

- In Step 4 and Step 9, search for current license texts in SPDX database
- In Step 7, verify current FSF/OSI guidance on specific copyleft trigger questions
- Verify case law citations (Jacobsen v. Katzer, SFC v. Vizio current status, Entr'Ouvert v. Orange)
- Check current NTIA SBOM requirements and CISA guidance currency
- Verify EU CRA Regulation 2024/2847 provisions and current transitional period status
- Save verified references to `/tmp/legalcode-oss-compliance-research.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with analysis using general knowledge of license texts
- Mark all case law and statutory references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — all references unverified"`
- Recommend legal counsel confirmation before relying on any specific provision

**CI/CD integration (for automated audits):**

Recommended tooling stack for continuous compliance:

| Tool                        | Type           | Primary Use                                                                    | SBOM Output     |
| --------------------------- | -------------- | ------------------------------------------------------------------------------ | --------------- |
| **FOSSA**                   | Commercial SCA | Policy enforcement, CI/CD gating, legal review workflows                       | SPDX, CycloneDX |
| **Black Duck (Synopsys)**   | Commercial SCA | Binary scanning, enterprise license/vulnerability management                   | SPDX, CycloneDX |
| **Syft** (Anchore)          | Open-source    | SBOM generation from containers, filesystems, manifests                        | SPDX, CycloneDX |
| **Trivy** (Aqua)            | Open-source    | Container and filesystem scanning; vulnerability + license                     | SPDX, CycloneDX |
| **scancode-toolkit** (nexB) | Open-source    | Source-level license detection; SPDX output                                    | SPDX            |
| **REUSE tool** (FSFE)       | Open-source    | REUSE Specification 3.3 compliance validation; machine-readable source headers | SPDX            |
| **Dependabot** (GitHub)     | Integrated     | License alerts in PRs; dependency review action; GHSA vulnerability alerts     | N/A             |

**REUSE Specification 3.3 (FSFE):**
The REUSE Specification provides machine-readable license compliance through:

- `SPDX-License-Identifier:` headers in every source file
- `SPDX-FileCopyrightText:` headers in every source file
- `LICENSES/` directory containing full license texts
  The REUSE tool validates compliance. Increasingly adopted as the standard for
  machine-readable attribution in enterprise OSS projects.

---

## Output Format Template

```markdown
# Open-Source License Compliance Audit Report

**Project**: [Project name and repository path / URL]
**Audit Date**: [ISO 8601 date]
**Distribution Model**: [SaaS | Binary | Source Release | Internal Only]
**Overall Classification**: [COMPLIANT | ATTENTION | NON-COMPLIANT]
**Overall Confidence**: [HIGH | MEDIUM | LOW]

---

## Executive Summary

[2-3 sentences: overall compliance posture, highest-risk finding, top remediation priority]

**Key Metrics:**
| Metric | Count |
|--------|-------|
| Total components scanned | [N] |
| Direct dependencies | [N] |
| Transitive dependencies | [N] |
| Unique licenses identified | [N] |
| Unknown / missing licenses | [N] |
| Critical findings (NON-COMPLIANT) | [N] |
| Review items (ATTENTION) | [N] |
| Informational notes (COMPLIANT) | [N] |

---

## 1. SBOM Summary

### 1.1 Dependency Inventory

| Component | Version | Type       | License      | PURL   | Confidence |
| --------- | ------- | ---------- | ------------ | ------ | ---------- |
| [name]    | [ver]   | Direct     | MIT          | [purl] | HIGH       |
| [name]    | [ver]   | Transitive | Apache-2.0   | [purl] | HIGH       |
| [name]    | [ver]   | Transitive | GPL-3.0-only | [purl] | MEDIUM     |
| [name]    | [ver]   | Transitive | NOASSERTION  | [purl] | LOW ⚠      |

### 1.2 License Family Distribution

| License Family                     | Count | % of Total | Risk Level             |
| ---------------------------------- | ----- | ---------- | ---------------------- |
| Permissive (Tier 1)                | [N]   | [%]        | Low                    |
| Weak Copyleft (Tier 2)             | [N]   | [%]        | Medium                 |
| Strong / Network Copyleft (Tier 3) | [N]   | [%]        | High                   |
| Source-Available (Tier 4)          | [N]   | [%]        | High — review required |
| Unknown / Missing (Tier X)         | [N]   | [%]        | Critical               |

---

## 2. License Compatibility Analysis

### 2.1 Compatibility Matrix

[Table of license pairs found in SBOM with compatibility assessment]

### 2.2 Conflicts Detected

| Finding ID | Components | Conflict                                      | Classification | Confidence |
| ---------- | ---------- | --------------------------------------------- | -------------- | ---------- |
| [ID]       | [A] + [B]  | Apache-2.0 patent clause vs. GPL-2.0-only § 6 | NON-COMPLIANT  | HIGH       |

---

## 3. Copyleft Trigger Analysis

| Component | License  | Trigger Action                        | Triggered?      | Basis                   | Confidence                           |
| --------- | -------- | ------------------------------------- | --------------- | ----------------------- | ------------------------------------ |
| [name]    | GPL-3.0  | Binary distribution                   | YES             | GPL v3 § 4-6            | HIGH                                 |
| [name]    | LGPL-2.1 | Binary distribution (dynamic linking) | NO              | LGPL v2.1 § 6 exception | MEDIUM — verify dynamic linking      |
| [name]    | AGPL-3.0 | SaaS with external users              | YES if modified | AGPL v3 § 13            | MEDIUM — confirm modification status |

---

## 4. Attribution and NOTICE Analysis

### 4.1 Attribution Gaps

| Component | License    | Missing Requirement                           | Severity  |
| --------- | ---------- | --------------------------------------------- | --------- |
| [name]    | Apache-2.0 | Upstream NOTICE file not propagated           | ATTENTION |
| [name]    | MIT        | Copyright notice stripped from source headers | ATTENTION |

### 4.2 SBOM Completeness vs. Regulatory Standards

| Standard               | Applicable | Elements Missing | Compliant? |
| ---------------------- | ---------- | ---------------- | ---------- |
| EO 14028 / NTIA        | [Yes/No]   | [list]           | [Yes/No]   |
| EU CRA Annex I Part II | [Yes/No]   | [list]           | [Yes/No]   |

---

## 5. Compliance Findings by Severity

### 5.1 NON-COMPLIANT Findings

[Finding template for each NON-COMPLIANT item — see Actionable Output per Finding above]

### 5.2 ATTENTION Findings

[Finding template for each ATTENTION item]

### 5.3 Informational Notes

[COMPLIANT items with notable characteristics; patent risk notes; CLA status]

---

## 6. Action Plan

### Immediate (Block Distribution)

- [ ] [Action] — Finding [ID] — Owner: [Role] — Due: [date]

### Short-Term (Before Next Release)

- [ ] [Action] — Finding [ID] — Owner: [Role] — Due: [date]

### Medium-Term (Next Quarter)

- [ ] [Action] — Finding [ID] — Owner: [Role] — Due: [date]

### Policy and Governance

- [ ] Integrate OSS license scanning into CI/CD pipeline ([tool recommendation])
- [ ] Establish SBOM generation and archival in release pipeline (EU CRA: 10-year retention)
- [ ] Define license approval policy and approval workflow
- [ ] Conduct developer training on license compliance basics

---

## 7. Glass Box Audit Trail

[Complete YAML template from Glass Box Audit Trail section above]

---

_Report generated by legalcode-open-source-license-compliance skill_
_Classification and findings require review by qualified IP/copyright counsel before reliance_
_Re-audit recommended before any change to distribution model, major dependency update, or before US federal procurement_
```

---

## Localization Notes

This skill is jurisdiction-agnostic by design. When analyzing for a specific geography:

- **US federal procurement**: Apply EO 14028 + NTIA minimum elements; use CISA SBOM
  resources for tooling guidance. [VERIFY current CISA/NIST guidance currency.]
- **EU market (commercial products)**: Apply EU CRA Regulation 2024/2847 obligations
  from September 2026. Confirm whether organization is a "manufacturer" or "steward"
  under the CRA taxonomy. [VERIFY current CRA delegated acts and transitional period.]
- **Germany**: Heightened GPL enforcement risk (gpl-violations.org injunctions); stronger
  copyright protection; stricter derivative works analysis. Legal counsel strongly recommended.
- **France**: Post-Entr'Ouvert v. Orange (2024), French courts have demonstrated willingness
  to award substantial GPL damages. Civil law enforcement path effective.
- **UK post-Brexit**: UK CDPA governs; EU CRA does not directly apply but UK equivalent
  legislation may be enacted. [VERIFY current UK product security and software legislation.]

---

## Provenance

Created by Legalcode (2026-03-02). Legalcode original synthesis based on:

- 2-agent research pipeline: Structural Analyst (workflow, classification system, output
  template) + Legal Research Agent (case law, statutory analysis, enforcement landscape)
- Legal authority: Jacobsen v. Katzer (Fed. Cir. 2008); SFC v. Vizio (Cal. Superior Court,
  ongoing, Jan. 2024 ruling); Entr'Ouvert v. Orange (Paris Court of Appeal, Feb. 2024,
  €800,000 damages); Oracle LLC v. Google (US Supreme Court, Apr. 2021)
- Regulatory authority: EO 14028 (May 2021); NTIA SBOM minimum elements (June 2021);
  EU Cyber Resilience Act Regulation 2024/2847 (in force Dec. 2024); CISA SBOM
  Framing Document (Oct. 2024); REUSE Specification 3.3 (FSFE)
- Reference skills: legalcode-contract-review (QA framework), legalcode-compliance-program-builder
  (compliance structure), imported-skala-open-source-license (foundational OSS concepts)
- Note: All case citations and statutory references should be verified against authoritative
  sources before reliance in legal or compliance proceedings. [VERIFY all citations.]
