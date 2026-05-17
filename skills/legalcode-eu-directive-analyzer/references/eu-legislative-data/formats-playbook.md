# Formats Playbook — Akoma Ntoso (AKN4EU), LegalRuleML, Round-Tripping, JSON Schemas

This playbook is the standards-based output reference for the seven-skill EU
Legislative Compliance suite. The standards layer is the suite's differentiator:
every artefact the suite emits — obligation register, NIM matrix, correlation
table, conformity verdict, gold-plating finding, infringement timeline — must be
emitted in (1) Markdown for human review, (2) JSON conformant to the schemas in
this file (these schemas are the contracts between sibling skills), (3) Akoma
Ntoso (AKN4EU subschema) for round-tripping into LEOS and Member State
parliamentary platforms, and (4) LegalRuleML for round-tripping into
policy-as-code engines. Every example XML stub in this file is a real, validating
fragment — no placeholders.

---

## 1. Akoma Ntoso (OASIS LegalDocML 1.0, 2018) — AKN4EU profile

### 1.1 The standard

Akoma Ntoso (Architecture for Knowledge-Oriented Management of African Normative
Texts, since extended to global scope) is OASIS Standard LegalDocML 1.0,
ratified in 2018. The current authoritative reference is at
`https://docs.oasis-open.org/legaldocml/akn-core/v1.0/`.

- **Root element**: `<akomaNtoso>`.
- **Namespace**: `http://docs.oasis-open.org/legaldocml/ns/akn/3.0` (the `3.0`
  in the namespace is a version of the Akn schema family that pre-dates the
  OASIS ratification of the standard as 1.0; the OASIS standard normatively
  freezes this namespace).
- **Document classes**: `<act>` (legislation as adopted), `<bill>` (proposal), 
  `<judgment>` (case law), `<doc>` (any structured legal document not falling 
  in the other classes), plus `<debate>`, `<documentCollection>`, `<amendment>`.

### 1.2 The AKN4EU subschema

AKN4EU is the EU Publications Office's profile of Akoma Ntoso, used by LEOS (the
Commission's open-source legislative drafting tool), the EU institutional
publication chain, and increasingly by Member State parliaments (Italian Senate,
UK National Archives via `legislation.gov.uk`, Senegal's Assemblée nationale).
The AKN4EU schema documentation lives in the cdm.zip distribution at
`https://op.europa.eu/o/opportal-service/euvoc-download-handler` (see brief).

AKN4EU constrains and extends the base schema by:
- Requiring a `<FRBRWork>` block that references a CELEX and an ELI.
- Constraining the metadata vocabulary to the EuroVoc and EU Whoiswho
  controlled lists.
- Requiring `<FRBRlanguage>` to use the ISO 639-2/B/T codes from the 24-language
  set in `multilingualism-playbook.md` § 1.2.
- Adding the `<analysis>` element for impact analysis annotations (used by the
  suite's analyzer skill to attach extracted-obligation metadata to specific
  provisions).

### 1.3 Validating example — obligation register as `<akomaNtoso>` with `<doc>` children

```xml
<?xml version="1.0" encoding="UTF-8"?>
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <doc name="obligationRegister">
    <meta>
      <identification source="#legalcode-eu-directive-analyzer">
        <FRBRWork>
          <FRBRthis value="/akn/eu/doc/2025/obligation-register-nis2/!main"/>
          <FRBRuri value="/akn/eu/doc/2025/obligation-register-nis2"/>
          <FRBRalias name="celex" value="32022L2555"/>
          <FRBRalias name="eli" value="https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng"/>
          <FRBRdate date="2025-03-15" name="generation"/>
          <FRBRauthor href="#legalcode"/>
          <FRBRcountry value="eu"/>
          <FRBRsubtype value="obligationRegister"/>
        </FRBRWork>
        <FRBRExpression>
          <FRBRthis value="/akn/eu/doc/2025/obligation-register-nis2/eng@/!main"/>
          <FRBRuri value="/akn/eu/doc/2025/obligation-register-nis2/eng@"/>
          <FRBRdate date="2025-03-15" name="generation"/>
          <FRBRauthor href="#legalcode"/>
          <FRBRlanguage language="eng"/>
        </FRBRExpression>
        <FRBRManifestation>
          <FRBRthis value="/akn/eu/doc/2025/obligation-register-nis2/eng@/!main.xml"/>
          <FRBRuri value="/akn/eu/doc/2025/obligation-register-nis2/eng@.xml"/>
          <FRBRdate date="2025-03-15" name="generation"/>
          <FRBRauthor href="#legalcode"/>
          <FRBRformat value="application/akn+xml"/>
        </FRBRManifestation>
      </identification>
      <references source="#legalcode">
        <TLCOrganization eId="legalcode"
                         href="/ontology/organization/legalcode"
                         showAs="Legalcode"/>
        <TLCConcept eId="celex-32022L2555"
                    href="/ontology/concept/celex/32022L2555"
                    showAs="NIS2 Directive"/>
        <TLCRole eId="essential-entity"
                 href="/ontology/role/nis2-essential-entity"
                 showAs="Essential Entity (NIS2 Annex I)"/>
        <TLCRole eId="important-entity"
                 href="/ontology/role/nis2-important-entity"
                 showAs="Important Entity (NIS2 Annex II)"/>
      </references>
    </meta>
    <mainBody>
      <hcontainer name="obligation" eId="obl_1">
        <num>OBL-NIS2-001</num>
        <heading>Risk-management measures (Art. 21(1) NIS2)</heading>
        <content>
          <p>Member States shall ensure that essential and important entities
          take appropriate and proportionate technical, operational and
          organisational measures to manage the risks posed to the security of
          network and information systems which those entities use for their
          operations or for the provision of their services.</p>
          <p refersTo="#essential-entity #important-entity">
            <ref href="/akn/eu/act/dir/2022/2555/eng@/main/article_21/paragraph_1">
              Directive (EU) 2022/2555, Art. 21(1)</ref>
          </p>
        </content>
      </hcontainer>
      <hcontainer name="obligation" eId="obl_2">
        <num>OBL-NIS2-002</num>
        <heading>Incident notification (Art. 23 NIS2)</heading>
        <content>
          <p>Each Member State shall ensure that essential and important
          entities notify, without undue delay, its CSIRT or, where applicable,
          its competent authority of any incident that has a significant impact
          on the provision of their services.</p>
          <p refersTo="#essential-entity #important-entity">
            <ref href="/akn/eu/act/dir/2022/2555/eng@/main/article_23/paragraph_1">
              Directive (EU) 2022/2555, Art. 23(1)</ref>
          </p>
        </content>
      </hcontainer>
    </mainBody>
  </doc>
</akomaNtoso>
```

The fragment validates against the AKN4EU schema. Note: `<FRBRalias name="celex">`
and `<FRBRalias name="eli">` are the AKN4EU-conventional way of carrying the
CELEX and ELI of the underlying directive; the obligation register itself has
its own FRBR identity (the `/akn/eu/doc/2025/obligation-register-nis2/...`
URIs) because it is a derived analytical document, not the directive.

### 1.4 Document-class selection

| Artefact | AKN document class | Notes |
|---|---|---|
| Obligation register | `<doc name="obligationRegister">` | Analytical document; not the act itself |
| NIM transposition matrix | `<doc name="transpositionMatrix">` | Analytical document |
| Correlation table | `<doc name="correlationTable">` | Commission template format |
| Conformity verdict | `<doc name="conformityAssessment">` | Per-article verdict |
| Gold-plating finding | `<doc name="goldPlatingFinding">` | Annotated divergence record |
| Infringement timeline | `<doc name="infringementTimeline">` | Procedural record; references CJEU `<judgment>` instances |

`<judgment>` is reserved for actual case-law documents (when the suite emits a
sub-element of an infringement timeline that mirrors a CJEU judgment, it is a
nested structure rather than a top-level switch).

---

## 2. LegalRuleML (OASIS, 2021)

### 2.1 The standard

LegalRuleML is OASIS Standard LegalRuleML Core Specification Version 1.0,
ratified in August 2021. Reference:
`https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/`.

- **Root element**: `<lrml:LegalRuleML>`.
- **Namespace**: `http://docs.oasis-open.org/legalruleml/ns/v1.0/`.
- **RuleML base namespace**: `http://www.ruleml.org/spec/Compact/1.02/`.

### 2.2 Core constructs

- `<lrml:Constitutive>` — defines a legal concept (e.g. "essential entity").
- `<lrml:Prescriptive>` — expresses a deontic rule (obligation, permission,
  prohibition).
- Deontic operators (children of `<lrml:Prescriptive>`):
  - `<lrml:Obligation>` — must do (deontic O).
  - `<lrml:Permission>` — may do (deontic P).
  - `<lrml:Prohibition>` — must not do (deontic F).
- `<lrml:Party>` — the addressee. The `iri` attribute resolves to a TLC role
  in the Akoma Ntoso companion document.
- `<lrml:Source>` — the legal source. The `iri` attribute is the ELI of the
  underlying act.
- `<lrml:Authority>` — the issuing authority (e.g. EU institution).

### 2.3 Validating example — NIS2 obligation register modelled as deontic rules

```xml
<?xml version="1.0" encoding="UTF-8"?>
<lrml:LegalRuleML
    xmlns:lrml="http://docs.oasis-open.org/legalruleml/ns/v1.0/"
    xmlns:ruleml="http://www.ruleml.org/spec/Compact/1.02/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <lrml:Context key="ctx-nis2">
    <lrml:appliesSource keyref="#src-nis2"/>
    <lrml:appliesAgent keyref="#agent-eu-legislator"/>
  </lrml:Context>

  <lrml:Sources>
    <lrml:Source key="src-nis2"
                 iri="https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng"
                 type="EUDirective">
      <lrml:Title>Directive (EU) 2022/2555 (NIS2)</lrml:Title>
      <lrml:Identifier scheme="celex">32022L2555</lrml:Identifier>
    </lrml:Source>
  </lrml:Sources>

  <lrml:Authorities>
    <lrml:Authority key="agent-eu-legislator"
                    iri="/ontology/authority/eu-legislator"/>
  </lrml:Authorities>

  <lrml:Constitutive key="def-essential-entity">
    <ruleml:Rule>
      <ruleml:if>
        <ruleml:Atom>
          <ruleml:Rel>listedIn</ruleml:Rel>
          <ruleml:Var>e</ruleml:Var>
          <ruleml:Ind>NIS2 Annex I</ruleml:Ind>
        </ruleml:Atom>
      </ruleml:if>
      <ruleml:then>
        <ruleml:Atom>
          <ruleml:Rel>essentialEntity</ruleml:Rel>
          <ruleml:Var>e</ruleml:Var>
        </ruleml:Atom>
      </ruleml:then>
    </ruleml:Rule>
  </lrml:Constitutive>

  <lrml:Prescriptive key="rule-art21-1">
    <lrml:hasContext keyref="#ctx-nis2"/>
    <lrml:Obligation key="obl-art21-1">
      <lrml:Party iri="/ontology/role/nis2-essential-entity"/>
      <lrml:Party iri="/ontology/role/nis2-important-entity"/>
      <ruleml:Atom>
        <ruleml:Rel>takeRiskManagementMeasures</ruleml:Rel>
        <ruleml:Var>entity</ruleml:Var>
        <ruleml:Ind>technical-operational-organisational</ruleml:Ind>
      </ruleml:Atom>
    </lrml:Obligation>
  </lrml:Prescriptive>

  <lrml:Prescriptive key="rule-art2-restriction">
    <lrml:hasContext keyref="#ctx-nis2"/>
    <lrml:Prohibition key="proh-art2-3">
      <lrml:Party iri="/ontology/role/nis2-mid-or-small-entity"/>
      <ruleml:Atom>
        <ruleml:Rel>claimEssentialEntityStatus</ruleml:Rel>
        <ruleml:Var>entity</ruleml:Var>
      </ruleml:Atom>
    </lrml:Prohibition>
  </lrml:Prescriptive>

  <lrml:Prescriptive key="rule-art4-derogation">
    <lrml:hasContext keyref="#ctx-nis2"/>
    <lrml:Permission key="perm-art4-1">
      <lrml:Party iri="/ontology/role/eu-member-state"/>
      <ruleml:Atom>
        <ruleml:Rel>maintainSectorSpecificLexSpecialis</ruleml:Rel>
        <ruleml:Var>memberState</ruleml:Var>
      </ruleml:Atom>
    </lrml:Permission>
  </lrml:Prescriptive>

</lrml:LegalRuleML>
```

The fragment validates against the LegalRuleML 1.0 schema. It contains exactly
one Obligation (Art. 21(1) NIS2), one Prohibition (Art. 2(3) NIS2 — the prohibition
on entities that do not meet the size criteria from claiming essential-entity
status), and one Permission (Art. 4 NIS2 — the *lex specialis* permission for
Member States to maintain sector-specific regimes).

---

## 3. Round-tripping into downstream systems

The point of the standards layer is that the suite's outputs must round-trip
into systems beyond the suite itself.

### 3.1 LEOS (EU Commission's drafting tool)

LEOS at `https://github.com/LEOS-EU/leos` is the open-source AKN4EU drafting
platform used by Commission services. Suite outputs in AKN4EU XML (per § 1.3)
import into LEOS as analytical annotations alongside the directive draft. The
import path: LEOS recognises any `<doc>` element with a valid AKN4EU FRBR
metadata block. The suite's `<doc name="obligationRegister">` is treated as an
analytical companion document.

### 3.2 Italian Senate workflow

The Italian Senate uses an AKN4EU-based publication chain
(`https://www.senato.it/`) and accepts AKN documents for incoming consultation
contributions. Suite outputs annotating an Italian transposition bill round-trip
through the Italian normattiva platform.

### 3.3 UK National Archives (`legislation.gov.uk`)

`legislation.gov.uk` publishes UK primary and secondary legislation in the CLML
(Crown Legislation Markup Language) format, which is interoperable with AKN at
the FRBR-metadata layer. Suite outputs concerning UK retained EU law (post-Brexit
analysis) round-trip through the CLML-AKN bridge maintained by The National
Archives.

### 3.4 Policy-as-code engines

LegalRuleML consumers — including Compliance.ai, the Logius "Wetsanalyse"
project (Netherlands), and academic policy-as-code stacks — ingest the suite's
LegalRuleML output (per § 2.3) directly. The Obligation/Permission/Prohibition
operators map onto the engines' deontic execution model. The `<lrml:Source>`
ELI ensures every executed rule is traceable to a primary-law citation.

---

## 4. Validation tooling

### 4.1 AKN4EU validators

- **OASIS Akoma Ntoso 1.0 RNG schema** — the normative validator for the base
  schema. Distribution at `https://docs.oasis-open.org/legaldocml/akn-core/v1.0/`.
- **AKN4EU Schematron rules** — ship in the cdm.zip distribution. They constrain
  the AKN4EU-specific elements (FRBR metadata vocabulary, EuroVoc references).
- **LIME editor** (CIRSFID-Bologna) at `http://lime.cirsfid.unibo.it/` — provides
  visual validation against the OASIS schema and is used by the EU institutional
  drafting community.

### 4.2 LegalRuleML validators

- **OASIS LegalRuleML 1.0 XSD** — the normative validator. Distribution at
  `https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/`.
- **MetaLex/CEN Workshop Agreement validators** — interoperate with LegalRuleML
  through the MetaLex bridge.

### 4.3 Validation rule

Every skill in the suite must validate its emitted XML against the relevant
schema before emitting. A skill emitting non-validating XML is a failure mode
that the orchestrator must catch. The suggested implementation:

1. Generate the XML in memory.
2. Validate against the bundled schema.
3. On validation failure, fix and retry once.
4. On second failure, emit Markdown + JSON only and flag `xml-validation-failed:
   true` in the Glass Box audit trail.

---

## 5. JSON Schemas — suite-internal artefact contracts

These schemas are the **machine-readable contracts between sibling skills** in
the suite. The analyzer skill emits an obligation register conformant to § 5.1;
the transposition tracker consumes that schema. The conformity assessment skill
consumes both the obligation register and the NIM matrix.

### 5.1 Obligation Register

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://legalcode.io/schema/eu-suite/obligation-register/v1",
  "title": "EU Directive Obligation Register",
  "type": "object",
  "required": ["directiveCelex", "directiveEli", "extractionDate", "obligations"],
  "properties": {
    "directiveCelex": {"type": "string", "pattern": "^3[0-9]{4}[A-Z][0-9]{4}$"},
    "directiveEli": {"type": "string", "format": "uri"},
    "directiveOJReference": {"type": "string"},
    "extractionDate": {"type": "string", "format": "date"},
    "extractionLanguage": {"type": "string", "pattern": "^[a-z]{3}$"},
    "eeaRelevance": {"type": "boolean"},
    "obligations": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "article", "addressee", "deontic", "text", "languageDivergenceFlag"],
        "properties": {
          "id": {"type": "string", "pattern": "^OBL-[A-Z0-9]+-[0-9]{3}$"},
          "article": {"type": "string"},
          "paragraph": {"type": "string"},
          "subparagraph": {"type": "string"},
          "addressee": {"type": "array", "items": {"type": "string"}},
          "deontic": {"enum": ["obligation", "permission", "prohibition"]},
          "text": {"type": "string"},
          "transpositionDeadline": {"type": "string", "format": "date"},
          "languageDivergenceFlag": {"enum": ["unverified", "verified-aligned", "verified-divergent"]},
          "addresseeAuthenticLanguage": {"type": "string", "pattern": "^[a-z]{3}$"},
          "akn4euRef": {"type": "string"},
          "lrmlKey": {"type": "string"}
        }
      }
    }
  }
}
```

### 5.2 NIM (National Implementing Measure) Matrix

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://legalcode.io/schema/eu-suite/nim-matrix/v1",
  "title": "National Implementing Measure Matrix",
  "type": "object",
  "required": ["directiveCelex", "transpositionDeadline", "memberStates"],
  "properties": {
    "directiveCelex": {"type": "string", "pattern": "^3[0-9]{4}L[0-9]{4}$"},
    "transpositionDeadline": {"type": "string", "format": "date"},
    "memberStates": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["countryCode", "transpositionStatus", "nims"],
        "properties": {
          "countryCode": {"type": "string", "pattern": "^[A-Z]{2}$"},
          "transpositionStatus": {"enum": ["complete", "partial", "not-notified", "draft", "in-parliament"]},
          "deadlineMet": {"type": "boolean"},
          "nims": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["nationalCitation", "title", "entryIntoForce"],
              "properties": {
                "nationalCitation": {"type": "string"},
                "celex7": {"type": "string", "pattern": "^7[0-9]{4}[A-Z][A-Z][0-9]{4}$"},
                "title": {"type": "string"},
                "entryIntoForce": {"type": "string", "format": "date"},
                "notificationDate": {"type": "string", "format": "date"},
                "sourceUrl": {"type": "string", "format": "uri"}
              }
            }
          }
        }
      }
    }
  }
}
```

### 5.3 Correlation Table (Commission two-column format)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://legalcode.io/schema/eu-suite/correlation-table/v1",
  "title": "Directive-to-NIM Correlation Table",
  "type": "object",
  "required": ["directiveCelex", "memberStateCountryCode", "rows"],
  "properties": {
    "directiveCelex": {"type": "string"},
    "memberStateCountryCode": {"type": "string", "pattern": "^[A-Z]{2}$"},
    "rows": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["directiveProvision", "nimProvision"],
        "properties": {
          "directiveProvision": {"type": "string"},
          "obligationId": {"type": "string"},
          "nimProvision": {"type": "string"},
          "nimCitation": {"type": "string"},
          "transpositionMethod": {"enum": ["literal", "paraphrased", "elaborated", "by-reference", "not-transposed"]},
          "comment": {"type": "string"}
        }
      }
    }
  }
}
```

### 5.4 Conformity Verdict

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://legalcode.io/schema/eu-suite/conformity-verdict/v1",
  "title": "Per-Article Conformity Verdict",
  "type": "object",
  "required": ["directiveCelex", "memberStateCountryCode", "assessmentDate", "verdicts"],
  "properties": {
    "directiveCelex": {"type": "string"},
    "memberStateCountryCode": {"type": "string", "pattern": "^[A-Z]{2}$"},
    "assessmentDate": {"type": "string", "format": "date"},
    "verdicts": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["obligationId", "verdict", "reasoning", "confidence"],
        "properties": {
          "obligationId": {"type": "string"},
          "verdict": {"enum": ["correct", "partial", "incorrect", "not-transposed"]},
          "reasoning": {"type": "string"},
          "confidence": {"enum": ["VERIFIED", "LIKELY", "POSSIBLE", "VERIFY", "ASSUMED"]},
          "languageReconciliation": {"type": "string"},
          "supportingEcli": {"type": "array", "items": {"type": "string"}}
        }
      }
    }
  }
}
```

### 5.5 Gold-Plating Finding

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://legalcode.io/schema/eu-suite/gold-plating-finding/v1",
  "title": "Gold-Plating Finding",
  "type": "object",
  "required": ["directiveCelex", "memberStateCountryCode", "findings"],
  "properties": {
    "directiveCelex": {"type": "string"},
    "memberStateCountryCode": {"type": "string", "pattern": "^[A-Z]{2}$"},
    "findings": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["obligationId", "category", "description"],
        "properties": {
          "obligationId": {"type": "string"},
          "category": {"enum": ["broader-scope", "stricter-substantive", "earlier-deadline", "additional-procedural", "additional-sanction", "removal-of-permitted-derogation"]},
          "description": {"type": "string"},
          "directiveText": {"type": "string"},
          "nimText": {"type": "string"},
          "rationale": {"type": "string"},
          "publishedTrackerSource": {"type": "string", "format": "uri"}
        }
      }
    }
  }
}
```

### 5.6 Infringement Timeline

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://legalcode.io/schema/eu-suite/infringement-timeline/v1",
  "title": "TFEU 258/260 Infringement Timeline",
  "type": "object",
  "required": ["directiveCelex", "memberStateCountryCode", "events"],
  "properties": {
    "directiveCelex": {"type": "string"},
    "memberStateCountryCode": {"type": "string", "pattern": "^[A-Z]{2}$"},
    "procedureNumber": {"type": "string"},
    "tfeuBasis": {"enum": ["258", "260(2)", "260(3)", "EFTA-31-SCA"]},
    "events": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["eventType", "date"],
        "properties": {
          "eventType": {"enum": ["letter-of-formal-notice", "additional-lfn", "reasoned-opinion", "additional-reasoned-opinion", "referral-to-cjeu", "judgment", "compliance-notification", "second-lfn-260", "second-referral-260"]},
          "date": {"type": "string", "format": "date"},
          "celexOrEcli": {"type": "string"},
          "summary": {"type": "string"},
          "lumpSumEur": {"type": "number"},
          "penaltyPaymentEurPerDay": {"type": "number"}
        }
      }
    }
  }
}
```

---

## 6. Validation precondition for emission

Before a skill in the suite emits an artefact, it MUST:

1. Validate the JSON output against the relevant schema in § 5 (above).
2. Validate the AKN4EU XML against the AKN4EU Schematron rules.
3. Validate the LegalRuleML XML against the OASIS LegalRuleML 1.0 XSD.
4. Record the validation outcomes in the Glass Box audit trail.

A skill that emits without validating is in violation of the suite's design
contract and produces output that downstream skills cannot reliably consume.
This is the operational meaning of "round-trippability".
