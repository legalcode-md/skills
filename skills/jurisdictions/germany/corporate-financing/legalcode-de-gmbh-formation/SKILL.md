---
name: legalcode-de-gmbh-formation
description: 'Guide the formation of a German GmbH (Gesellschaft mit beschränkter Haftung) or UG (haftungsbeschränkt
  / Unternehmergesellschaft) from inception through operational status. Use when founding a German limited
  liability company, drafting or reviewing the Gesellschaftsvertrag (articles of association), deciding
  between Musterprotokoll and custom articles, structuring share capital (Stammkapital), appointing a
  Geschäftsführer (managing director), filing with the Handelsregister (commercial register), and registering
  with the Finanzamt (tax office). Also covers shareholder agreement (Gesellschaftervereinbarung) considerations,
  UG capital accumulation rules (§5a GmbHG), Vorgesellschaft liability during the pre-registration phase,
  and post-formation compliance obligations. Triggers on: GmbH gründen, GmbH formation, UG haftungsbeschränkt,
  Gesellschaftsvertrag, Musterprotokoll, Handelsregister, Stammkapital, Geschäftsführer appointment, German
  company formation, DiRUG online founding.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode: German GmbH / UG Formation

> **Disclaimer**: This skill provides a framework for AI-assisted guidance on German GmbH and
> UG (haftungsbeschränkt) formation. It does not constitute legal advice (Rechtsberatung) and
> does not substitute for advice from a qualified German Rechtsanwalt (attorney) or Notar
> (notary) licensed to practise German law. All statutory and case law references carry
> hallucination risk — verify against authoritative sources (gesetze-im-internet.de, dejure.org,
> or official Bundesanzeiger publications) before relying on them. Formation procedures,
> fees, and regulatory requirements change; verify current applicability before proceeding.

---

## Purpose and Scope

This skill guides the formation of a GmbH or UG (haftungsbeschränkt) under the German
_Gesetz betreffend die Gesellschaften mit beschränkter Haftung_ (GmbHG). It operates in
two modes:

- **Formation Mode**: Step-by-step guidance from entity selection through post-registration
  compliance. Covers structure design, document preparation, registration workflow, and
  tax registration.
- **Review Mode**: Analysis of an existing Gesellschaftsvertrag or draft formation documents
  against mandatory requirements and best practice, with severity-classified findings and
  recommended remediation.

**Covers:**

- GmbH vs UG entity selection and capital structure
- Musterprotokoll vs bespoke Gesellschaftsvertrag design
- Notarization requirements (including DiRUG electronic founding, §2 Abs. 3 GmbHG)
- Capital contribution mechanics (Bareinlage / Sacheinlage), Stammkapital, Einzahlungsnachweis
- Vorgesellschaft liability during the pre-registration phase
- Managing director (Geschäftsführer) appointment, duties, and service agreement
- Handelsregister filing with the competent Amtsgericht
- Finanzamt registration: Fragebogen zur steuerlichen Erfassung, Steuernummer, USt-IdNr
- Gewerbeanmeldung (trade registration) and knock-on registrations
- Gesellschaftervereinbarung (shareholders' agreement) considerations
- UG capital accumulation obligations (§5a GmbHG) and conversion to GmbH
- Post-formation compliance: Transparenzregister, Bundesanzeiger annual filing, Impressumspflicht

**Does not:**

- Provide legal advice or replace a German Notar or Rechtsanwalt
- Draft bespoke Gesellschaftsvertrag text (provides structural guidance and issues to address)
- Cover AG (Aktiengesellschaft) formation or GmbH & Co. KG structures
- Cover cross-border mergers or reorganisations into GmbH form
- Address industry-specific licensing beyond standard Gewerbeanmeldung

---

## Jurisdiction and Governing Law

This skill applies exclusively to the laws of the **Federal Republic of Germany (Bundesrepublik
Deutschland)**. The GmbH is a creature of federal statute; there is no state-level variation
in formation law (unlike US LLC law). Key governing instruments:

| Instrument                                                       | Relevance                                                                |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **GmbHG** (Gesetz betr. Gesellschaften mit beschränkter Haftung) | Primary statute; governs all aspects of GmbH/UG formation and governance |
| **BGB** (Bürgerliches Gesetzbuch)                                | Supplementary general civil law; governs service agreements, obligations |
| **HGB** (Handelsgesetzbuch) §§6, 8, 10, 13                       | Commercial register obligations, merchant status, firm name rules        |
| **GNotKG** (Gerichts- und Notarkostengesetz)                     | Notary and court fee schedule                                            |
| **AO** (Abgabenordnung)                                          | General tax procedural law                                               |
| **KStG** (Körperschaftsteuergesetz)                              | Corporate income tax                                                     |
| **GewStG** (Gewerbesteuergesetz)                                 | Business (trade) tax                                                     |
| **UStG** (Umsatzsteuergesetz)                                    | Value added tax                                                          |
| **GwG** §3 (Geldwäschegesetz)                                    | Beneficial owner registration (Transparenzregister)                      |
| **GewO** (Gewerbeordnung)                                        | Trade registration (Gewerbeanmeldung)                                    |
| **DiRUG** (Gesetz zur Umsetzung der Digitalisierungsrichtlinie)  | Electronic / online founding since August 2022                           |

---

## Interactive Clarification

This skill uses **interactive clarification** (marked **⟁ CLARIFY**) at decision points where:

- The user's choice would substantially change the formation path or document structure
- Multiple equally valid approaches exist (e.g., Musterprotokoll vs bespoke articles)
- Business context is needed to classify a finding correctly
- Jurisdictional nuance depends on facts not yet provided

When you reach a **⟁ CLARIFY** point, present structured options with short descriptions. If
the user has already provided the relevant information in the conversation, skip the question
and proceed. Do not silently assume — state assumptions explicitly.

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Formation request**: User describes their intended business, number of founders,
  capital available, and desired governance structure → run in **Formation Mode**
- **Document review**: User provides a draft Gesellschaftsvertrag (as file, pasted text,
  or URL) → run in **Review Mode**
- **Specific question**: User asks about one aspect of GmbH formation → answer with
  reference to the relevant workflow step and legal framework

If no clear mode is indicated, default to **Formation Mode** and ask the context questions
in Step 2.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Ask the following before proceeding. Present as structured options:

**1. Entity type preference:**

- **GmbH** — minimum EUR 25,000 share capital; established credibility; full flexibility
- **UG (haftungsbeschränkt)** — minimum EUR 1; lower startup cost; mandatory profit retention
  (§5a GmbHG) until reserves reach EUR 25,000; cash contributions only; mandatory name suffix
- **Undecided** — walk me through the decision

_Why this matters_: UG and GmbH follow different capital rules, contribution restrictions,
and naming requirements. The decision controls the entire formation path.

**2. Number of founders / shareholders:**

- 1 founder (Einpersonengründung)
- 2-3 founders
- 4 or more founders

_Why this matters_: The Musterprotokoll (simplified standard articles) is limited to a
maximum of 3 shareholders and 1 managing director. More than 3 founders requires a
bespoke Gesellschaftsvertrag.

**3. Managing directors:**

- Single Geschäftsführer (one of the founders, or an external person)
- Multiple Geschäftsführer

_Why this matters_: The Musterprotokoll permits only one managing director.

**4. Governance complexity:**

- **Simple** — equal shares, single purpose, no external investors anticipated
- **Moderate** — unequal shares, custom voting thresholds, some governance provisions
- **Complex** — investor/founder split, vesting, drag-along/tag-along, custom profit
  distribution, multiple classes of interest anticipated

_Why this matters_: Determines whether Musterprotokoll is viable or a bespoke
Gesellschaftsvertrag is required.

**5. Location of founders:**

- All founders physically in Germany
- Some or all founders located abroad

_Why this matters_: Foreign founders may use DiRUG electronic founding (§2 Abs. 3 GmbHG)
for cash contributions; in-person notarization is still required for non-cash (Sachgründung)
contributions. Bank KYC timelines differ for non-residents.

---

### Step 3: GmbH vs UG Decision

Using the context from Step 2, produce a **GmbH / UG Decision Matrix** covering the
criteria below. Present as a structured comparison table.

| Factor                                | GmbH                                  | UG (haftungsbeschränkt)                                                                      |
| ------------------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------- |
| Minimum share capital                 | EUR 25,000                            | EUR 1                                                                                        |
| Minimum deposit at registration       | EUR 12,500 (50%)                      | Full amount (100%)                                                                           |
| Non-cash contributions (Sachgründung) | Permitted (with valuation report)     | **Prohibited** (§5a Abs. 2 S. 2 GmbHG)                                                       |
| Mandatory profit retention            | None                                  | 25% of annual profit → statutory reserve until capital reaches EUR 25,000 (§5a Abs. 3 GmbHG) |
| Profit distributions                  | Freely distributable from free assets | Restricted until reserve threshold met                                                       |
| Name requirement                      | Ends with "GmbH"                      | Must include "UG (haftungsbeschränkt)" or "Unternehmergesellschaft (haftungsbeschränkt)"     |
| Creditor / market perception          | Strong                                | Weaker (some lenders, clients wary)                                                          |
| Formation cost (notary)               | EUR 350-850+                          | EUR 300-500                                                                                  |
| Conversion path                       | N/A                                   | Can convert to GmbH once share capital + reserves ≥ EUR 25,000 (§5a Abs. 5 GmbHG)            |

**⟁ CLARIFY** — If after presenting the matrix the user is still undecided, ask:

- "Do you have EUR 12,500 available to deposit as startup capital?" (yes → GmbH likely
  preferable; no → UG may be necessary)
- "Will you be contributing non-cash assets (equipment, IP, business)?" (yes → GmbH required)
- "Is the name/brand perception critical in early customer or investor conversations?" (yes → GmbH preferred)

---

### Step 4: Articles of Association Design

Determine whether to use the **Musterprotokoll** or a **bespoke Gesellschaftsvertrag**.

#### 4a. Musterprotokoll Suitability Check

The Musterprotokoll (§2 Abs. 1a GmbHG, Anlage 1 GmbHG) is a fixed standardized form.
It is suitable **only** when ALL of the following are true:

| Condition                                                                   | Required |
| --------------------------------------------------------------------------- | -------- |
| Maximum 3 shareholders                                                      | ✓        |
| Exactly 1 managing director                                                 | ✓        |
| Calendar year as financial year is acceptable                               | ✓        |
| No custom profit distribution rules needed                                  | ✓        |
| No vesting, drag-along, tag-along, or investor-protective provisions needed | ✓        |
| Non-cash contributions are not being made                                   | ✓        |
| No special voting thresholds or quorum requirements needed                  | ✓        |
| No shareholder non-compete provisions in the articles                       | ✓        |
| Simple equal or defined shares with no restrictions on transfer             | ✓        |

If any condition fails → **bespoke Gesellschaftsvertrag required**.

**Musterprotokoll advantages**: Lower notary cost (~EUR 300-350), faster processing,
no drafting required.
**Musterprotokoll disadvantage**: Zero customization; cannot be modified in any way.

#### 4b. Bespoke Gesellschaftsvertrag: Mandatory Provisions

Per §3 GmbHG, every Gesellschaftsvertrag must contain:

1. **Firma** (company name) — must end with "GmbH" or "UG (haftungsbeschränkt)"; must be
   distinctive (§18 HGB); must not be misleading; IHK name pre-check recommended
2. **Sitz** (registered office) — must be in Germany; need not be the operating address
3. **Unternehmensgegenstand** (business purpose) — must be specific enough to be lawful;
   vague purpose clauses ("all lawful commercial activities") are risky for trade registration
4. **Stammkapital** (share capital amount) — minimum EUR 25,000 (GmbH) or EUR 1 (UG)
5. **Stammeinlagen** (individual shares) — number and nominal value of each shareholder's
   share; all in whole euros; must sum to Stammkapital

#### 4c. Bespoke Gesellschaftsvertrag: Key Optional Provisions to Consider

These provisions are not mandatory for registration but are strongly recommended for any
substantive formation:

| Provision                                                  | Purpose                                                                  | Omission Risk                                                          |
| ---------------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| Geschäftsführer authority limits (Zustimmungsvorbehalte)   | Defines which MD actions require shareholder approval                    | MD can bind company to large contracts without approval                |
| Shareholder meeting quorum and voting thresholds           | Defines majority requirements for ordinary and extraordinary resolutions | Default statutory majority (§47 GmbHG) may not reflect parties' intent |
| Profit distribution rules (§29 GmbHG default: pro rata)    | Custom distribution (e.g., preferred return, reallocation)               | Pro rata distribution may be inequitable where contributions differ    |
| Transfer restrictions on shares (Vinkulierung, §15 GmbHG)  | Restricts share transfers without shareholder consent                    | Unwanted third parties may acquire shares                              |
| Right of first refusal (Vorkaufsrecht)                     | Existing shareholders can match any third-party offer                    | Existing holders lose priority                                         |
| Compulsory share transfer triggers (Einziehung, §34 GmbHG) | Enables forced buyout on death, insolvency, or breach                    | Difficult to remove problematic co-shareholder                         |
| Managing director appointment and removal procedures       | Defines who can appoint/remove and with what majority                    | Deadlock risk in multi-shareholder structures                          |
| Non-compete for shareholders and managing directors        | Prohibits competing activity during and post-membership                  | Exiting founder can immediately start competing company                |
| Capital call (Nachschusspflicht, §26 GmbHG)                | Allows demand for additional capital from shareholders                   | No mechanism to fund shortfalls without formal capital increase        |
| Dispute resolution / deadlock mechanism                    | Provides path when shareholders cannot agree                             | Disputes lead to costly litigation or wind-up                          |

**⟁ CLARIFY** — For formations with external investors or more than 2 shareholders, ask:

- "Will there be a separate Gesellschaftervereinbarung (shareholders' agreement) covering
  governance matters?" (Yes → some optional provisions can move there; No → must be in articles)
- "Are any shareholders contributing non-cash assets?" (Yes → Sacheinlage valuation report
  required; see Step 5e)

---

### Step 5: Formation Checklist

Walk through each phase of the GmbH formation process. For each item, confirm status
(Pending / In Progress / Complete / Not Applicable).

#### Phase 1 — Pre-Notarization

| #   | Action                                                               | Notes                                                                             |
| --- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| 1.1 | Name availability check (IHK pre-approval)                           | IHK pre-check is free and informal; formal registration only at Amtsgericht       |
| 1.2 | Registered office address secured                                    | Must be physical address in Germany; virtual office permitted for Handelsregister |
| 1.3 | Articles of association drafted / Musterprotokoll selected           | See Step 4                                                                        |
| 1.4 | Shareholder identities confirmed (natural persons or legal entities) | For legal entity shareholders: certified Handelsregisterauszug required           |
| 1.5 | Managing director(s) identified and confirmed as eligible            | Natural persons only; not subject to disqualifying convictions (§6 Abs. 2 GmbHG)  |
| 1.6 | Capital contribution structure agreed                                | Cash or in-kind (GmbH only); UG cash only                                         |
| 1.7 | Notary appointed                                                     | In-person or DiRUG video (§2 Abs. 3 GmbHG) for cash-only formations               |

#### Phase 2 — Notarization

| #   | Action                                                                   | Notes                                                                                      |
| --- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| 2.1 | All shareholders appear before notary (in person or video)               | Must have valid ID (Personalausweis/Reisepass); foreign nationals: apostille may be needed |
| 2.2 | Notary certifies Gesellschaftsvertrag (or Musterprotokoll)               | Creates notarielle Urkunde                                                                 |
| 2.3 | Gesellschafterliste (initial shareholder list) certified                 | Required by §40 GmbHG                                                                      |
| 2.4 | Managing director appointment document certified                         | If not included in Gesellschaftsvertrag                                                    |
| 2.5 | For Sachgründung: valuation report (Sachgründungsbericht) notarized      | GmbH only; auditor-verified valuation of non-cash assets                                   |
| 2.6 | Notary retains original; provides certified copies for bank and register | Typically same-day delivery                                                                |

#### Phase 3 — Capital Deposit

| #   | Action                                                                | Notes                                                                                                  |
| --- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 3.1 | Corporate bank account opened in name of company "i.G." (in Gründung) | Use notarized articles to open account; account name must include i.G. suffix                          |
| 3.2 | Capital deposited by each shareholder                                 | GmbH: minimum 25% per shareholder of their Stammeinlage; minimum 50% total (§7 Abs. 2 GmbHG); UG: 100% |
| 3.3 | Einzahlungsnachweis obtained from bank                                | Written confirmation of deposit; required for Handelsregister filing                                   |
| 3.4 | Capital is "at the disposal of the managing director"                 | Funds must be freely available; not encumbered by third-party claims                                   |

#### Phase 4 — Handelsregister Registration

| #   | Action                                                                                                                                         | Notes                                                                                      |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 4.1 | Notary submits application to competent Amtsgericht                                                                                            | Electronic submission via XJustiz/ELRV; competence = GmbH's registered office jurisdiction |
| 4.2 | Application includes: certified Gesellschaftsvertrag, Gesellschafterliste, MD appointment, Einzahlungsnachweis, MD affidavit (§8 Abs. 2 GmbHG) | MD must declare no disqualifying circumstances (§8 Abs. 3 GmbHG)                           |
| 4.3 | Court reviews filing for completeness and legal conformity                                                                                     | Typical timeline: 1-3 weeks after notarization                                             |
| 4.4 | Handelsregister entry published                                                                                                                | Company exists as legal entity from moment of entry (§11 Abs. 1 GmbHG)                     |
| 4.5 | Obtain certified Handelsregisterauszug                                                                                                         | Used for bank, tax office, and trade registration                                          |

> **Critical**: The GmbH does not exist as a separate legal entity, and limited liability does
> not apply, until the moment of Handelsregister entry. See Vorgesellschaft section below.

#### Phase 5 — Trade Registration and Tax Registration

| #   | Action                                                                         | Notes                                                                                                                                                   |
| --- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5.1 | Gewerbeanmeldung at local Gewerbeamt                                           | Required for most commercial activities (§14 GewO); cost: ~EUR 20-60; automatically triggers Finanzamt notification                                     |
| 5.2 | Fragebogen zur steuerlichen Erfassung filed with Finanzamt                     | Via ELSTER (mandatory electronic filing since 2021); must include opening balance sheet (Eröffnungsbilanz); submit within 1 month of commencement       |
| 5.3 | Steuernummer issued by Finanzamt                                               | 10-digit domestic tax number; required for tax filings and payroll                                                                                      |
| 5.4 | USt-IdNr (VAT ID) applied for (if applicable)                                  | Required for intra-EU B2B transactions; apply via Bundeszentralamt für Steuern                                                                          |
| 5.5 | Transparenzregister: beneficial owners (wirtschaftlich Berechtigte) registered | §3 GwG; any natural person holding >25% shares or voting rights; deadline: within 2 weeks of formation; public register; failure: fine up to EUR 25,000 |
| 5.6 | IHK membership (automatic)                                                     | No separate filing; IHK notified automatically by commercial register                                                                                   |
| 5.7 | Social insurance registration (if employees or MD in employment relationship)  | Register with Deutsche Rentenversicherung and relevant Berufsgenossenschaft                                                                             |

---

### Step 6: Gesellschaftsvertrag Analysis (Review Mode)

When reviewing an existing draft Gesellschaftsvertrag, analyze it against the following
checklist. Classify each item as **REQUIRED / RECOMMENDED / OPTIONAL** and flag issues
as **CRITICAL / MATERIAL / ADVISORY** (see Severity Classification section).

#### Mandatory Provisions Checklist (§3 GmbHG)

| Provision                                 | Present | Notes / Issues                                                             |
| ----------------------------------------- | ------- | -------------------------------------------------------------------------- |
| Company name (Firma)                      |         | Complies with §18 HGB distinctiveness? Ends with GmbH/UG designation?      |
| Registered office in Germany (Sitz)       |         | Street address or just municipality? (just municipality sufficient for §3) |
| Business purpose (Unternehmensgegenstand) |         | Specific enough for Gewerbeamt? Not misleading?                            |
| Share capital amount (Stammkapital)       |         | At or above EUR 25,000 (GmbH) or EUR 1 (UG)?                               |
| Individual share amounts (Stammeinlagen)  |         | Sum equals Stammkapital? All in whole euros?                               |
| Shareholder names and share allocations   |         | Names match ID documents?                                                  |

#### Governance Provisions Review

| Provision                                      | Present | Quality Assessment                                                            |
| ---------------------------------------------- | ------- | ----------------------------------------------------------------------------- |
| Managing director authority (scope and limits) |         | Any Zustimmungsvorbehalte (catalog of actions requiring shareholder consent)? |
| Shareholder meeting notice requirements        |         | Notice period, method, and quorum defined?                                    |
| Voting majority thresholds                     |         | Simple vs. qualified majority defined? Certain decisions require 75%+?        |
| Profit distribution                            |         | Default (pro rata per §29) or custom? Tax implications considered?            |
| Share transfer restrictions (Vinkulierung)     |         | Pre-emption rights? Consent requirements?                                     |
| Compulsory transfer triggers (Einziehung, §34) |         | Bad leaver / good leaver provisions? Pricing mechanism?                       |
| Dispute resolution / deadlock                  |         | Arbitration clause? Deadlock mechanism?                                       |
| Non-compete provisions                         |         | Duration, scope, geographic limits? Adequately compensated?                   |
| Liquidation provisions                         |         | Distribution waterfall on wind-up?                                            |

---

### Step 7: Managing Director (Geschäftsführer) Framework

#### 7a. Appointment and Eligibility

Per §6 GmbHG, a Geschäftsführer must be:

- A natural person (juristische Personen cannot be Geschäftsführer)
- Of full legal capacity (not under guardianship / Betreuung)
- Not subject to a **business disqualification** (Berufsverbot, §6 Abs. 2 GmbHG)
- Not convicted of certain offences (insolvency crimes, fraud, § 6 Abs. 2 S. 2 No. 3 GmbHG) [VERIFY current list]

The Gesellschaftsvertrag or a separate shareholder resolution appoints the Geschäftsführer.
The Handelsregister must record the appointment (§10 GmbHG).

#### 7b. Duties and Liability (§43 GmbHG)

The Geschäftsführer owes the company the standard of care of **"a diligent businessperson"**
(Sorgfalt eines ordentlichen Geschäftsmannes, §43 Abs. 1 GmbHG). Key duties:

| Duty                            | Description                                                                                     | Liability Exposure                                                            |
| ------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Business judgment duty**      | Act in company's best interest with adequate information                                        | §43 Abs. 2 GmbHG civil liability to company for breach                        |
| **Capital maintenance**         | Must not authorize distributions below Stammkapital floor (§30/31 GmbHG)                        | Personal liability to reimburse illegal distributions                         |
| **Accounting duty**             | Maintain proper books and records; file annual accounts                                         | Fines; criminal liability under §41 GmbHG for persistent default              |
| **Tax payment duty**            | Remit wage tax, corporate tax, VAT on time                                                      | Personal liability under §69 AO for Körperschaftsteuer / Lohnsteuer arrears   |
| **Insolvency filing duty**      | File for insolvency within **3 weeks** of confirmed insolvency or over-indebtedness (§15a InsO) | Criminal liability (§15a Abs. 4 InsO); civil liability to creditors for delay |
| **Competition prohibition**     | Must not compete with GmbH without shareholder consent                                          | Breach grounds for removal and damages                                        |
| **Loyalty and confidentiality** | Protect company secrets; disclose conflicts                                                     | Grounds for dismissal; damages                                                |

**⟁ CLARIFY** — For the Geschäftsführer service agreement (Geschäftsführervertrag), ask:

- "Is the Geschäftsführer a shareholder (Gesellschafter-Geschäftsführer) or an external
  manager?" — affects employment law applicability, tax treatment, and social insurance
- "Will a separate Geschäftsführervertrag be drafted?" — strongly recommended even when
  Musterprotokoll is used; the Musterprotokoll does not contain MD compensation or duty terms

#### 7c. Geschäftsführervertrag Key Provisions

A written Geschäftsführervertrag (not required to be notarized unless the MD is also a
shareholder making commitments relating to shares) should address:

| Clause                                   | Content                                                                                                                          | Risk if Absent                                                                                          |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Scope of authority                       | Management authority including Zustimmungsvorbehalte catalog                                                                     | MD acts outside scope; disputes                                                                         |
| Remuneration                             | Fixed salary, bonus, benefits, pension contribution                                                                              | Disputes; tax compliance issues                                                                         |
| Duration and termination                 | Fixed term or indefinite; notice period; for-cause termination triggers                                                          | No clear exit mechanism                                                                                 |
| Non-compete (Wettbewerbsverbot)          | Duration (max 2 years), geographic scope, business scope, compensation (Karenzentschädigung, typically 50% of last remuneration) | MD leaves and immediately competes                                                                      |
| IP assignment                            | All inventions, software, designs created in scope of role vest in GmbH                                                          | **ArbnErfG does NOT apply to Geschäftsführer** [VERIFY] — IP remains with MD absent explicit assignment |
| Confidentiality                          | Scope, duration post-termination                                                                                                 | Company secrets leak to competitors                                                                     |
| Director's and Officers' (D&O) insurance | Confirm whether GmbH will provide D&O cover                                                                                      | MD exposed to personal liability claims                                                                 |
| Garden leave / non-solicitation          | Cannot solicit employees or customers post-termination                                                                           | Key staff and clients at risk                                                                           |

> **Critical**: German law's Employee Invention Act (ArbnErfG) grants employee inventors
> rights that must be claimed by the employer within 4 months. **The ArbnErfG does not apply
> to Geschäftsführer** (who are not legally "employees"). Without an explicit IP assignment
> clause in the Geschäftsführervertrag, inventions and software developed by the Geschäftsführer
> may remain their personal property. [VERIFY with Rechtsanwalt for specific circumstances]

---

### Step 8: Shareholder Agreement (Gesellschaftervereinbarung)

A Gesellschaftervereinbarung (GV) is a private contract between shareholders supplementing
the articles of association. Unlike the Gesellschaftsvertrag, it does not require notarization
(unless it commits parties to transfer shares or form a GmbH) and is not filed with the
Handelsregister.

**When a Gesellschaftervereinbarung is strongly advisable:**

- 2+ founders with unequal contributions or roles
- External investor involvement anticipated
- Vesting schedules for founder shares
- Complex exit provisions (drag-along, tag-along, put/call options)
- Confidential governance arrangements not suitable for public register

**Key provisions to include in a Gesellschaftervereinbarung:**

| Provision                                                            | Purpose                                                                  |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Vesting schedule for founder shares (Zeitvesting / Milesteinvesting) | Protect company if a founder departs early                               |
| Good leaver / bad leaver definitions and pricing                     | Fair vs. punitive pricing on share return depending on departure reason  |
| Tag-along right (Mitveräußerungsrecht)                               | Minority shareholders can join majority in any share sale at same price  |
| Drag-along right (Mitnahmerecht / Schlepprecht)                      | Majority can force minority to sell in exit transaction                  |
| Anti-dilution (Verwässerungsschutz)                                  | Protects early investors against dilutive issuances below original price |
| Investor protective provisions (Zustimmungsvorbehalte)               | Specific actions require investor consent                                |
| Information rights                                                   | Investor receives periodic financial reports                             |
| Pre-emption rights on new share issuance (Bezugsrecht)               | Existing shareholders can maintain percentage                            |
| Deadlock resolution mechanism                                        | Escalation, mediation, buy-sell (Texas Shoot-Out)                        |
| Confidentiality and non-solicitation                                 | Among shareholders inter se                                              |

> **Note**: Provisions in the Gesellschaftervereinbarung bind only the shareholders who
> signed it (Schuldrecht/law of obligations). Unlike provisions in the Gesellschaftsvertrag,
> they do not bind the GmbH as a corporate entity or future shareholders unless the agreement
> is amended or a new party accedes. Transfer restrictions and governance provisions with
> company-level effect should be in the Gesellschaftsvertrag.

---

### Step 9: UG Capital Accumulation and Conversion

#### 9a. Mandatory Profit Retention (§5a Abs. 3 GmbHG)

A UG must, in each financial year, allocate **one quarter (25%) of the annual net profit**
(after loss carryforward) to a statutory reserve (_gesetzliche Rücklage_) until the
combined share capital and reserves reach EUR 25,000.

**Thesaurierungspflicht mechanics:**

```
Annual net profit (Jahresüberschuss)
  – Loss carryforward (Verlustvortrag)
  = Basis for mandatory retention

25% × Basis = mandatory annual allocation to reserve

Reserve + Share capital → once ≥ EUR 25,000: obligation ceases
```

**Permitted use of the statutory reserve (§5a Abs. 3 S. 2 GmbHG):**

- Capital increase from company funds (Kapitalerhöhung aus Gesellschaftsmitteln, §57c GmbHG)
- Offsetting balance sheet losses
- No other use permitted

**Consequence**: Until the threshold is reached, the UG cannot freely distribute profits.
Distributions from remaining net profit (after the mandatory 25% retention) are permissible
if the Gesellschaftsvertrag provides for them. [VERIFY calculation with tax advisor for
specific year-end accounting]

#### 9b. UG Conversion to GmbH (§5a Abs. 5 GmbHG)

Conversion is permitted (not mandatory) once the aggregate of share capital and statutory
reserves equals or exceeds EUR 25,000. Process:

1. **Shareholder resolution** to convert UG to GmbH and increase share capital to EUR 25,000
2. **Capital increase** — may be funded from accumulated statutory reserves (no new cash
   required if reserves are sufficient) or via new cash contributions from shareholders
3. **Articles amendment** — change entity name from "UG (haftungsbeschränkt)" to "GmbH";
   update share capital figure; must be notarized
4. **Handelsregister filing** — notary submits amended articles; court records the conversion
5. **New Handelsregisterauszug** reflects GmbH status

**Costs**: Notary ~EUR 300-800 + court ~EUR 100-200 = total ~EUR 400-1,000

---

### Step 10: Vorgesellschaft (Pre-GmbH Liability)

The period from notarization of the Gesellschaftsvertrag until Handelsregister entry is
the **Vorgesellschaft** (also called _GmbH i.G._ — in Gründung / in formation) phase.

#### Legal Status

- The Vor-GmbH is a legal entity (rechtsfähige Personengesellschaft) capable of entering
  contracts and owning assets, but it is **not yet a GmbH**
- Limited liability does **not** apply — founders and acting managing directors are
  **personally and jointly liable** for all obligations entered during this phase
- The company must identify itself as "GmbH i.G." or "[Name] in Gründung" in all documents,
  correspondence, and contracts

#### Risk Mitigation Strategies

| Strategy                                      | Implementation                                                                                                                                                        |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compress the formation timeline               | Submit Handelsregister application same day as notarization; deposit capital before notary appointment                                                                |
| Condition contracts on registration           | Include _aufschiebende Bedingung_ (condition precedent): "Dieses Angebot/dieser Vertrag steht unter dem Vorbehalt der Eintragung der Gesellschaft im Handelsregister" |
| Always use "i.G." designation                 | Sign all contracts as "[Name] GmbH i.G." — puts counterparties on notice of pre-registration status                                                                   |
| Avoid high-value commitments pre-registration | Defer signing of office leases, significant supplier contracts, employment agreements until after Handelsregister entry                                               |
| Capital deposit before notarization           | Bank account opened and capital deposited before notary appointment enables same-day submission                                                                       |

**⟁ CLARIFY** — If the user indicates they need to enter contracts before Handelsregister
entry, advise:

- Clearly identify the pre-registration status in every contract
- Include a condition precedent clause
- Consider whether personal liability exposure is acceptable for the intended commitment
- Explore whether the counterparty will agree to contract with the company effective from
  the date of registration

---

### Step 11: Post-Formation Compliance

#### 11a. Ongoing Corporate Obligations

| Obligation                                                        | Frequency                                                                                    | Authority                 | Failure Consequences                                     |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------- | -------------------------------------------------------- |
| Annual financial statements (Jahresabschluss)                     | Annually (within 3 months of year-end for preparation; shareholder approval within 6 months) | §41 GmbHG, HGB §§ 242-256 | Fines; personal liability                                |
| Filing annual accounts with Bundesanzeiger (Unternehmensregister) | Annually (within 12 months of balance sheet date)                                            | §325 HGB                  | Fines up to EUR 25,000                                   |
| Shareholder meetings / resolutions                                | At least annually (§46 GmbHG)                                                                | GmbHG                     | Governance invalidity; disputes                          |
| Handelsregister change notifications                              | On any change to name, address, MD, share capital                                            | §10 GmbHG                 | Unregistered changes not effective against third parties |
| Gesellschafterliste update                                        | On any share transfer or capital change                                                      | §40 GmbHG                 | Invalid share transfers                                  |
| Transparenzregister update                                        | On any change to beneficial ownership (>25% threshold)                                       | §3 GwG                    | Fine up to EUR 25,000                                    |

#### 11b. Tax Compliance Calendar (General)

| Tax                                                        | Frequency            | Due Date (typical)                           | Authority  |
| ---------------------------------------------------------- | -------------------- | -------------------------------------------- | ---------- |
| Körperschaftsteuer (corporate income tax) advance payments | Quarterly            | 10 March / June / September / December       | §31 KStG   |
| Gewerbesteuer (trade tax) advance payments                 | Quarterly            | 15 February / May / August / November        | §21 GewStG |
| Umsatzsteuervoranmeldung (VAT pre-declaration)             | Monthly or quarterly | 10th of following month                      | §18 UStG   |
| Annual tax return                                          | Annually             | 31 July (or 28/29 February with tax advisor) | AO §149    |

#### 11c. Impressumspflicht (Imprint Requirement)

Any GmbH with a website, social media profile, or online presence must maintain a legally
compliant Impressum (imprint) per §5 TMG (Telemediengesetz):

- Company full name (including "GmbH" or "UG (haftungsbeschränkt)")
- Registered address
- Name(s) of managing director(s)
- Commercial register number and court (e.g., "HRB 12345, Amtsgericht Berlin-Charlottenburg")
- Contact details (email and phone)
- USt-IdNr (if applicable)
- Links to dispute resolution platform (required under EU ODR Regulation for B2C e-commerce)

Failure: Fine up to EUR 50,000 under §16 Abs. 3 TMG.

---

### Step 12: Quality Verification

Before delivering any formation guidance or review output, run the following checks:

1. Run the 5 **Citation Quality Gates** (below). Revise any failures before delivery.
2. For every **CRITICAL** finding, run the 3-pass **Self-Interrogation** (below).
3. Assign a **Confidence Score** to each material legal statement.
4. Verify completeness: confirm all 5 formation phases have been addressed.
5. Generate the **Glass Box Audit Trail** and append it to the output.

---

## Formation Topic Deep Reference

### GmbH Share Capital Structure

**Stammkapital** (§5 GmbHG): The total registered capital of the GmbH. Minimum EUR 25,000.
Each unit of Stammkapital is called a **Geschäftsanteil** (business share).

**Stammeinlage**: Each shareholder's individual share contribution. Must be stated in whole
euros. Sum of all Stammeinlagen = Stammkapital.

**Capital contribution types (Einlagearten):**

| Type                                            | GmbH                                             | UG               |
| ----------------------------------------------- | ------------------------------------------------ | ---------------- |
| Bareinlage (cash)                               | ✓                                                | ✓ (only)         |
| Sacheinlage (non-cash: property, IP, equipment) | ✓ (with valuation report — Sachgründungsbericht) | **✗ Prohibited** |
| Mixed (Mischeinlage)                            | ✓                                                | ✗                |

**Sacheinlage requirements (GmbH only)**:

- A Sachgründungsbericht by founders explaining the contribution (§5 Abs. 4 GmbHG)
- Where contribution ≥ EUR 25,000, an auditor (Wirtschaftsprüfer or vereidigter Buchprüfer)
  must confirm the value equals or exceeds the stated Stammeinlage (§9a GmbHG)
- If overvalued: shareholder must make up the difference in cash (§9 GmbHG) [VERIFY]

**Capital maintenance (Kapitalerhaltung, §30/31 GmbHG)**:
Distributions to shareholders are prohibited if they would reduce net assets below the
Stammkapital figure. Shareholders who receive illegal distributions must reimburse the
company. Managing director who authorizes illegal distributions is personally liable.

---

## Severity Classification

Use this three-tier system for formation review findings. Adapted from the contract-review
standard to the corporate formation context:

### CRITICAL — Must Resolve Before Registration Proceeds

The finding creates a statutory defect, invalid formation, or personal liability exposure
so severe that formation should not proceed without resolution.

**Examples:**

- Gesellschaftsvertrag lacks a mandatory provision (§3 GmbHG) — registration will be refused
- Stammkapital stated below statutory minimum (EUR 25,000 for GmbH)
- UG articles permit Sachgründung (explicitly prohibited by §5a Abs. 2 S. 2 GmbHG)
- Capital not fully at the disposal of the MD at registration (§7 Abs. 2, 3 GmbHG) — registration will be refused
- Proposed Geschäftsführer is disqualified (§6 Abs. 2 GmbHG) — registration will be refused
- Company operating commercially before Handelsregister entry without "i.G." designation

**Action**: Stop. Identify specific statutory requirement. Draft corrective language. Confirm
with qualified Notar or Rechtsanwalt before proceeding.

### MATERIAL — Address Before Launch or Within 30 Days of Registration

The finding does not prevent Handelsregister registration but creates significant governance
gaps, liability exposure, or regulatory non-compliance.

**Examples:**

- No Geschäftsführervertrag — MD duties, compensation, and non-compete undocumented
- Missing IP assignment clause in Geschäftsführervertrag for tech company
- Gesellschaftsvertrag has no share transfer restrictions in multi-founder company
- UG mandatory profit retention mechanics not reflected in profit distribution clause
- No deadlock mechanism in equal-split two-founder GmbH
- Transparenzregister registration not filed within statutory deadline

**Action**: Prepare corrective document or amendment. Set timeline. Note in output.

### ADVISORY — Best Practice; Address at Convenience

The finding represents a deviation from best practice or a missing optional provision,
but does not create immediate risk.

**Examples:**

- No Gesellschaftervereinbarung when one would be useful
- Business purpose clause broader than ideal for trade registration purposes
- No D&O insurance provision in Geschäftsführervertrag
- No dispute resolution / mediation clause in articles
- Annual meeting mechanics not specified beyond statutory default

**Action**: Note and recommend. Include in "next steps" output section.

---

## Actionable Output per Finding

For each finding, structure the output as follows:

```
### Finding [N]: [Short Title]
**Severity**: CRITICAL / MATERIAL / ADVISORY
**Location**: §[X] GmbHG / Gesellschaftsvertrag §[X] / Phase [X] of checklist
**Issue**: [What is wrong or missing]
**Legal Basis**: [Specific statutory provision or principle]
**Risk**: [Concrete harm if not addressed]
**Recommended Action**: [Specific corrective step — what to add, change, or do]
**Draft Language** (if applicable):
  [Example clause or document language]
**Confidence**: [Score from Confidence Scoring scale]
```

---

## Prioritization Framework

When multiple findings exist, prioritize remediation in this order:

**Tier 1 — Pre-Registration Blockers (CRITICAL)**
Issues that will cause Handelsregister rejection or create immediate personal liability.
Must be resolved before any registration filing.

**Tier 2 — Early Post-Registration (MATERIAL)**
Issues that do not block registration but expose founders, shareholders, or the company to
significant risk. Address within 30 days of registration:

- Execute Geschäftsführervertrag
- Complete tax registrations
- Register with Transparenzregister
- File Gewerbeanmeldung

**Tier 3 — Within First Quarter (ADVISORY)**
Best-practice improvements that reduce friction or risk in the medium term:

- Draft Gesellschaftervereinbarung if warranted
- Put D&O insurance in place
- Set up accounting / bookkeeping system
- Implement compliance calendar

**Tier 4 — Ongoing (Compliance)**
Recurring obligations that form part of the operating compliance cadence:

- Annual accounts and Bundesanzeiger filing
- Tax advance payments
- Handelsregister change notifications
- Transparenzregister updates

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise before delivery if any gate
fails.

| Gate           | Rule                                                                                                                                | Fail Action                                         |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **Source**     | Every legal claim cites a specific provision of GmbHG, BGB, HGB, or other named statute                                             | Add citation or mark "[UNVERIFIED]"                 |
| **Format**     | Citations follow standard German legal form: §[number] [law abbreviation] (e.g., §43 GmbHG)                                         | Fix format                                          |
| **Currency**   | Cited provisions reflect current law (GmbHG last substantially amended by MoMiG 2008; DiRUG 2022)                                   | Flag "[CHECK CURRENCY — law may have been amended]" |
| **Domain**     | Analysis stays within German law scope; does not import foreign law concepts (e.g., US-style "veil-piercing") without flagging them | Remove or flag cross-border concepts                |
| **Confidence** | Uncertainty explicitly stated ("appears to require", "verify with Notar"), not hidden                                               | Add confidence qualifier                            |

### Self-Interrogation for CRITICAL Findings

For any CRITICAL finding, apply this 3-pass review:

**Pass 1 — Statutory Chain Integrity**: Does the finding follow directly from the cited
statutory provision? Would the competent Amtsgericht or a qualified Notar reach the same
conclusion? Are there alternative interpretations of the provision?

**Pass 2 — Completeness**: Have all relevant GmbHG provisions been considered? Are there
BGB general law provisions that may modify the conclusion? Does the finding interact with
other provisions in the same document?

**Pass 3 — Counter-Challenge**: What is the strongest argument that this finding is not
CRITICAL? Could the defect be cured after registration? Is the risk theoretical or does it
arise in practice? Under what circumstances might a qualified professional accept the risk?

### Confidence Scoring

| Level        | Range     | Meaning                                        | Action                                                   |
| ------------ | --------- | ---------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled statutory text; unambiguous            | State with confidence                                    |
| **High**     | 0.80-0.94 | Strong authority; minor interpretive questions | State with brief caveat                                  |
| **Probable** | 0.60-0.79 | Good arguments; some room for interpretation   | State with reasoning and qualifications                  |
| **Possible** | 0.40-0.59 | Genuinely uncertain; depends on facts          | Flag for Rechtsanwalt / Notar review; present both sides |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                        | Do not assert; flag "[UNCERTAIN — verify]"               |

---

## Anti-Patterns

The following are the most common and consequential mistakes in German GmbH / UG
formation. Flag any of these patterns when identified.

### 1. Operating as GmbH Before Handelsregister Entry (Vorgesellschaft Trap)

Entering significant commercial commitments — leases, supplier contracts, employment
agreements — without "i.G." designation or condition-precedent clause. Founders bear
unlimited personal joint liability for all pre-registration obligations. Mitigation: use
"GmbH i.G." in all documents; insert _aufschiebende Bedingung_ (condition precedent clause).

### 2. Using Musterprotokoll When Structure Is Too Complex

Choosing the Musterprotokoll to save notary costs when the company has 4+ shareholders,
multiple MDs, or needs custom governance. The Musterprotokoll cannot be modified at all.
Result: expensive articles amendment shortly after formation. Mitigation: complete the
Musterprotokoll suitability check (see Step 4a) before choosing.

### 3. UG with Sacheinlage Attempt

Attempting to contribute non-cash assets (IP, equipment, client lists) to a UG. This is
explicitly prohibited by §5a Abs. 2 S. 2 GmbHG. If non-cash contributions are needed,
a GmbH must be used. Mitigation: if assets are to be contributed, form a GmbH.

### 4. Missing IP Assignment in Geschäftsführervertrag

Assuming that software, inventions, or designs created by the Geschäftsführer in their
role automatically belong to the GmbH. The ArbnErfG does not apply to Geschäftsführer;
absent an explicit written assignment, the MD retains ownership. Critical for tech, SaaS,
and creative businesses. Mitigation: include an express IP assignment clause in the
Geschäftsführervertrag covering present and future creations.

### 5. Undercapitalization Creating Piercing Risk

Forming a GmbH with the minimum EUR 25,000 capital for a business that requires
EUR 500,000 in operational capital. German courts in extreme cases apply liability
_Durchgriff_ (piercing) where the Stammkapital is grossly inadequate relative to the
business risk undertaken. Mitigation: supplement Stammkapital with properly documented
shareholder loans (Gesellschafterdarlehen) rather than underfunding the company.

### 6. Forgetting the Transparenzregister

Failing to register beneficial owners (wirtschaftlich Berechtigte) within the statutory
deadline (2 weeks post-formation, per §3 GwG). The Transparenzregister is now a public
register. Non-compliance triggers fines up to EUR 25,000. Mitigation: add to post-formation
checklist as a Day 1 action.

### 7. No Geschäftsführervertrag (or Inadequate One)

Relying on the Gesellschaftsvertrag or Musterprotokoll alone to define the managing
director relationship. The Gesellschaftsvertrag does not cover compensation, confidentiality,
non-compete, or IP assignment. A Geschäftsführer without a proper service agreement is
a governance risk. Mitigation: draft a comprehensive Geschäftsführervertrag before or
immediately after registration.

### 8. Ignoring the Non-Compete Compensation Requirement

Inserting a post-termination non-compete in the Geschäftsführervertrag without providing
for Karenzentschädigung (non-compete compensation). German courts treat non-competes
without adequate compensation as either unenforceable or avoidable by the MD. Mitigation:
provide at least 50% of last fixed remuneration for the duration of the non-compete (by
analogy to §74 HGB; exact standard for Geschäftsführer varies — verify with counsel). [VERIFY]

### 9. Equal-Split Two-Founder GmbH Without Deadlock Mechanism

Two founders each holding exactly 50% of shares with no mechanism to resolve disagreements.
On any fundamental dispute, neither can pass a resolution without the other. This can lead
to company paralysis and potentially forced wind-up. Mitigation: include a deadlock
resolution procedure (escalation, casting vote for one MD, buy-sell mechanism such as
Texas Shoot-Out / _Andienungsrecht_) in either the Gesellschaftsvertrag or the
Gesellschaftervereinbarung.

### 10. Tax Registration Delay (Fragebogen)

Failing to file the Fragebogen zur steuerlichen Erfassung within 1 month of commencing
business or Handelsregister entry. The Finanzamt cannot issue a Steuernummer until this
form is received. Without a Steuernummer, the company cannot issue tax-compliant invoices,
and cannot register for VAT. Mitigation: prepare the Fragebogen before registration and
file on the same day as or immediately after Handelsregister entry.

### 11. Distributing UG Profits Before Reserve Threshold

Distributing profits from a UG without first allocating 25% to the statutory reserve per
§5a Abs. 3 GmbHG. Any distribution that violates the capital maintenance rules (§30
GmbHG applied by analogy) is repayable to the company by the receiving shareholder.
Mitigation: build mandatory 25% retention into profit distribution resolutions and check
annually against reserve threshold.

### 12. Vague Business Purpose Clause

Drafting an overly broad Unternehmensgegenstand (e.g., "all lawful commercial activities
permitted under applicable law"). This can cause problems at the Gewerbeamt (trade
registration may be refused or restricted) and with the Finanzamt (broad purpose raises
audit scrutiny). Mitigation: state the primary business activity concisely but specifically;
may include a catch-all secondary purpose clause.

### 13. Failing to Update Gesellschafterliste on Share Transfers

When shares change hands, the managing director must file an updated Gesellschafterliste
with the Handelsregister promptly (§40 GmbHG). An outdated Gesellschafterliste means
the share transfer is not effective against the company. The registered list is the
definitive record of who is a shareholder. Mitigation: treat Gesellschafterliste update
as a mandatory step in any share transfer transaction.

### 14. Employment Contract Surviving MD Promotion

Promoting a company employee to Geschäftsführer without properly terminating the existing
employment contract by mutual consent (Aufhebungsvertrag). The original employment
contract goes dormant but may revive when the MD service agreement ends, with all
accumulated employment law protections (unfair dismissal, notice periods, etc.) intact.
Mitigation: execute a written Aufhebungsvertrag for the employment agreement simultaneously
with signing the Geschäftsführervertrag.

### 15. Missing Imprint on Website (Impressumspflicht)

Launching a website or social media presence without a legally compliant Impressum per §5
TMG. Common omissions: missing commercial register number, missing Geschäftsführer name,
missing USt-IdNr. Regulators and competitors monitor compliance; warning letters
(Abmahnungen) from competitors are common and commercially disruptive. Fine up to EUR 50,000.
Mitigation: generate the Impressum as part of post-registration Day 1 checklist.

### 16. Ignoring Insolvency Filing Timeline

Managing director becomes aware of company insolvency or over-indebtedness but delays
filing for insolvency beyond the 3-week statutory window (§15a InsO). Late filing
triggers personal criminal liability (§15a Abs. 4 InsO) and civil liability to creditors
for losses sustained during the delay. Mitigation: MD should seek immediate legal advice
if company faces liquidity crisis; do not delay to seek turnaround.

### 17. Single-Founder GmbH Without Documented Resolutions

Sole shareholder-managing director treating the GmbH as a personal account without
maintaining corporate formalities (shareholder resolutions, documented decisions, separate
bank accounts). Under German law, failure to observe corporate formalities is relevant
evidence in a Durchgriff (piercing) claim. Mitigation: maintain complete resolution records
even for single-person GmbHs; always keep company and personal finances strictly separate.

---

## Writing Standards

Before delivering any output from this skill:

**Plain language discipline:**

- Introduce German legal terms with English explanation on first use
- Do not use technical shorthand without defining it (e.g., "Vinkulierung (share transfer
  restriction)" not simply "Vinkulierung")
- Use active voice: "The Geschäftsführer must file..." not "A filing obligation exists for..."
- Use specific amounts, timeframes, and thresholds rather than vague language

**Citation discipline:**

- Every statutory claim references the specific paragraph: §5a Abs. 3 GmbHG, not just "GmbHG"
- Mark unverified or potentially outdated references with [VERIFY]
- Mark research-backed but not independently confirmed references with [CONFIRM WITH NOTAR]

**Completeness gates (check before delivery):**

- [ ] All 5 formation phases addressed (or clearly scoped out)
- [ ] Entity type (GmbH vs UG) explicitly identified and confirmed
- [ ] All CRITICAL findings resolved or escalated
- [ ] Confidence scores assigned to material legal claims
- [ ] Glass Box Audit Trail generated
- [ ] Anti-patterns check run against proposed structure

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

Use legalcode-mcp to verify the current text of:

- §§2-11 GmbHG (formation provisions)
- §5a GmbHG (UG provisions)
- §43 GmbHG (Geschäftsführer duties)
- §15a InsO (insolvency filing duty)
- §3 GwG (beneficial owner registration)

Search legalcode-mcp for:

- Recent Bundesgerichtshof (BGH) decisions on Vorgesellschaft liability
- Recent amendments to GmbHG (MoMiG 2008 was last major reform; DiRUG 2022 for
  electronic founding)
- Current Handelsregister fee schedule and Finanzamt registration forms

Mark all legalcode-mcp-sourced provisions as VERIFIED in the Glass Box audit trail.

### Without legalcode-mcp (Graceful Degradation)

- Mark every statutory provision with [VERIFY — check current text at gesetze-im-internet.de]
- Advise the user to confirm all formation steps with a qualified Notar before proceeding
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`
- Focus the output on structural guidance, process overview, and anti-pattern identification
  rather than definitive legal conclusions

**Reference sources for manual verification:**

- Statutory text: [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gmbhg/)
- Commentary: dejure.org for annotated provisions
- Notary guidance: Bundesnotarkammer (bnotk.de)
- Chamber of Commerce: ihk.de (regional IHKs provide free startup guidance)
- Federal tax: elster.de (Fragebogen forms and ELSTER filing)
- Commercial register: handelsregister.de (public register extracts)

---

## Output Format Template

````markdown
# GmbH / UG Formation: [Company Name or "Draft Structure"]

**Date**: [date]
**Mode**: Formation Guide / Document Review
**Entity Type**: GmbH / UG (haftungsbeschränkt)

---

## Executive Summary

[2-3 sentences: overall formation readiness, key risks, and recommended priority actions]

**Overall Status**: ✅ Ready to proceed / ⚠️ Issues to resolve / ❌ Blocked — CRITICAL issues present

---

## Entity Selection

| Factor                 | Assessment                              |
| ---------------------- | --------------------------------------- |
| Entity type chosen     | GmbH / UG                               |
| Rationale              | [Key reasons for choice]                |
| Capital required       | EUR [X] (minimum EUR [25,000 / 1])      |
| Non-cash contributions | Applicable / Not applicable             |
| UG mandatory retention | N/A / EUR [X] per year until EUR 25,000 |

---

## Articles of Association Assessment

**Type**: Musterprotokoll / Bespoke Gesellschaftsvertrag

| Provision                         | Status       | Finding |
| --------------------------------- | ------------ | ------- |
| Company name (Firma)              | ✅ / ⚠️ / ❌ | [Notes] |
| Registered office (Sitz)          | ✅ / ⚠️ / ❌ | [Notes] |
| Business purpose                  | ✅ / ⚠️ / ❌ | [Notes] |
| Share capital (Stammkapital)      | ✅ / ⚠️ / ❌ | [Notes] |
| Individual shares (Stammeinlagen) | ✅ / ⚠️ / ❌ | [Notes] |
| [Additional provisions]           |              |         |

---

## Formation Checklist Status

### Phase 1 — Pre-Notarization

| Action                  | Status       | Notes |
| ----------------------- | ------------ | ----- |
| Name availability check | ✅ / ⏳ / ❌ |       |
| Registered address      | ✅ / ⏳ / ❌ |       |
| Articles drafted        | ✅ / ⏳ / ❌ |       |
| [etc.]                  |              |       |

### Phase 2 — Notarization

[Same format]

### Phase 3 — Capital Deposit

[Same format]

### Phase 4 — Handelsregister Registration

[Same format]

### Phase 5 — Trade & Tax Registration

[Same format]

---

## Findings

### CRITICAL Findings ([N])

[List each CRITICAL finding using the Finding template]

### MATERIAL Findings ([N])

[List each MATERIAL finding using the Finding template]

### ADVISORY Findings ([N])

[List each ADVISORY finding using the Finding template]

---

## Geschäftsführer Framework

| Element                                 | Status                  | Notes |
| --------------------------------------- | ----------------------- | ----- |
| Geschäftsführer identified and eligible |                         |       |
| Geschäftsführervertrag                  | Drafted / Needed / N/A  |       |
| IP assignment clause                    | Present / Missing / N/A |       |
| Non-compete clause                      | Present / Missing / N/A |       |
| Karenzentschädigung                     | Present / Missing / N/A |       |

---

## Post-Formation Action Plan

**Immediate (Day 1-5 post-registration):**

- [ ] Gewerbeanmeldung at Gewerbeamt
- [ ] Fragebogen zur steuerlichen Erfassung via ELSTER
- [ ] Transparenzregister beneficial owner registration
- [ ] Update website Impressum

**Within 30 days:**

- [ ] Execute Geschäftsführervertrag (if not done pre-registration)
- [ ] Open operational bank account (distinct from formation account)
- [ ] Set up bookkeeping / accounting system
- [ ] Apply for USt-IdNr (if EU transactions expected)

**Within 90 days:**

- [ ] [ADVISORY items]
- [ ] Gesellschaftervereinbarung (if recommended)
- [ ] D&O insurance (if recommended)

---

## Compliance Calendar

| Obligation                  | Frequency           | Next Due |
| --------------------------- | ------------------- | -------- |
| Körperschaftsteuer advance  | Quarterly           | [Date]   |
| Gewerbesteuer advance       | Quarterly           | [Date]   |
| VAT pre-declaration         | Monthly / Quarterly | [Date]   |
| Annual financial statements | Annually            | [Date]   |
| Bundesanzeiger filing       | Annually            | [Date]   |

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-de-gmbh-formation"
  run_date: "[date]"
  mode: "Formation Guide / Document Review"
  entity_type: "GmbH / UG (haftungsbeschränkt)"
  jurisdiction: "Federal Republic of Germany"
  governing_statutes:
    - "GmbHG (primary)"
    - "BGB (supplementary)"
    - "HGB §§6, 8, 10, 13"
    - "GwG §3 (beneficial ownership)"
    - "§15a InsO (insolvency filing)"
  legalcode_mcp: "Connected — provisions VERIFIED / Not connected — manual verification required"
  external_sources_used: "[List any sources consulted]"
  critical_findings: "[N]"
  material_findings: "[N]"
  advisory_findings: "[N]"
  anti_patterns_checked: "17 patterns reviewed"
  confidence_overall: "HIGH / MEDIUM / LOW — [rationale]"
  citations_verified: "[N VERIFIED] / [N marked VERIFY]"
  limitations:
    - "This skill does not draft Gesellschaftsvertrag text; structural guidance only"
    - "All statutory references require verification against current text at gesetze-im-internet.de"
    - "Notary and Rechtsanwalt review required before any filing"
    - "Tax analysis is structural overview only; detailed tax planning requires Steuerberater"
  reviewer: "AI-assisted — qualified Notar and/or Rechtsanwalt review required before relying on output"
```
````

---

## Localization Notes

This skill covers **federal German law only**. Note:

- **No state-level variation** in GmbH formation law (contrast US LLC law)
- **EU-level interactions**: A German GmbH is recognized across the EU as a limited liability
  entity under the EU Company Law Directives; branches in other EU member states require
  local registration
- **Foreign shareholder considerations**: Non-EU shareholders may require additional notarized
  and apostilled documents; bank KYC for non-residents typically takes 4-6 weeks — plan ahead
- **Language**: The Gesellschaftsvertrag must be in German for Handelsregister filing; English
  translations may be provided alongside but the German text governs
- **DiRUG electronic founding** is available to foreign founders for cash-only formations;
  in-person notarization remains required for Sachgründung and complex arrangements

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- Comprehensive research of GmbHG, BGB, HGB, GwG, InsO, and related statutes
- IHK formation guidance materials
- Bundesnotarkammer (BNotK) guidance on notarial procedures and DiRUG reform
- firma.de comprehensive GmbH formation guides
- Taylor Wessing, Deloitte Legal, Rose & Partner, and Commenda formation practice notes
- Academic commentary on §§1-15, 43, 46 GmbHG and §5a GmbHG UG provisions

**Key statutory changes since last full GmbHG reform:**

- MoMiG 2008: Introduced UG (§5a GmbHG), online-accessible Gesellschafterliste, simplified
  formation procedures
- DiRUG 2022: Introduced electronic/video notarization (§2 Abs. 3 GmbHG) effective August 2022
- DiREG 2023: Extended digital procedures

All statutory references carry [VERIFY] obligation — verify against current text before reliance.

```

```
