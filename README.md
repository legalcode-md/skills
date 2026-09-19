# Legalcode Skills

**327 legal skills**, organized into **15 practice areas** and **18 jurisdiction groups**.

[Browse the catalogue](CATALOG.md) · [General skills](skills/general/README.md) · [By jurisdiction](skills/jurisdictions/README.md)

## Start with a task

- [Review a contract](skills/general/contracts-commercial/legalcode-contract-review/SKILL.md)
- [Research primary law](skills/general/legal-research/legalcode-public-search/SKILL.md)
- [Build a skill from example documents](skills/general/drafting-documents/legalcode-document-to-skill/SKILL.md)
- [Question and improve a legal draft](skills/general/drafting-documents/legalcode-grill-document/SKILL.md)
- [Assess Icelandic EEA implementation](skills/jurisdictions/iceland/eu-eea-implementation/legalcode-eea-conformity-assessment-is/SKILL.md)
- [Review a data breach](skills/general/privacy-data-protection/legalcode-breach-severity-assessment/SKILL.md)

## Browse by practice area

Each area includes general and bespoke local workflows.

| Practice area | Skills |
| --- | ---: |
| [Contracts & commercial](catalog/practice-areas/contracts-commercial.md) | 36 |
| [Corporate & financing](catalog/practice-areas/corporate-financing.md) | 33 |
| [Privacy & data protection](catalog/practice-areas/privacy-data-protection.md) | 32 |
| [AI & technology](catalog/practice-areas/ai-technology.md) | 8 |
| [Employment & workplace](catalog/practice-areas/employment-workplace.md) | 35 |
| [Financial regulation](catalog/practice-areas/financial-regulation.md) | 19 |
| [Governance & compliance](catalog/practice-areas/governance-compliance.md) | 40 |
| [EU & EEA implementation](catalog/practice-areas/eu-eea-implementation.md) | 9 |
| [Litigation & disputes](catalog/practice-areas/litigation-disputes.md) | 39 |
| [Intellectual property](catalog/practice-areas/intellectual-property.md) | 14 |
| [Real estate & construction](catalog/practice-areas/real-estate-construction.md) | 12 |
| [Legal research](catalog/practice-areas/legal-research.md) | 8 |
| [Drafting & document analysis](catalog/practice-areas/drafting-documents.md) | 18 |
| [Legal operations](catalog/practice-areas/legal-operations.md) | 18 |
| [Tools & orchestration](catalog/practice-areas/tools-orchestration.md) | 6 |

## Browse by jurisdiction

[Australia](catalog/jurisdictions/australia.md) · [Brazil](catalog/jurisdictions/brazil.md) · [Canada](catalog/jurisdictions/canada.md) · [China](catalog/jurisdictions/china.md) · [European Union](catalog/jurisdictions/european-union.md) · [France](catalog/jurisdictions/france.md) · [Germany](catalog/jurisdictions/germany.md) · [Iceland](catalog/jurisdictions/iceland.md) · [India](catalog/jurisdictions/india.md) · [Ireland](catalog/jurisdictions/ireland.md) · [Japan](catalog/jurisdictions/japan.md) · [New Zealand](catalog/jurisdictions/new-zealand.md) · [Nordic region](catalog/jurisdictions/nordic.md) · [Poland](catalog/jurisdictions/poland.md) · [Singapore](catalog/jurisdictions/singapore.md) · [Switzerland](catalog/jurisdictions/switzerland.md) · [United Kingdom](catalog/jurisdictions/united-kingdom.md) · [United States](catalog/jurisdictions/united-states.md)

## Install

List available skills, then install only the workflows you need:

```sh
npx skills add legalcode-md/skills --list --full-depth
npx skills add legalcode-md/skills --skill legalcode-contract-review --full-depth
```

Install the full collection with:

```sh
npx skills add legalcode-md/skills --all --full-depth
```

Requires Node.js/npm for the skills CLI. Install names are unchanged. Skill folders now live under `skills/general/<practice-area>/` or `skills/jurisdictions/<jurisdiction>/<practice-area>/`. Use `--full-depth` for recursive discovery. Existing flat GitHub file links should be replaced with the paths in the catalogue; no reinstall is needed solely for the folder change.

Each package carries its scripts, references, templates and license. Check the skill's stated prerequisites before running external software or services. No model or provider is pinned.

## Legalcode connection

Add `https://mcp.legalcode.md/mcp` as a remote Streamable HTTP connector and complete authentication. Discover current coverage and permissions, then Search and Fetch primary texts before relying on them. Analyze and Trace support aggregate and relationship queries. Keep confidential documents local and minimize matter facts in source queries.

## Collection and validation

This release publishes every unique `legalcode-` name in the source collection, retaining previously published workflow tools. The [coverage record](collection-coverage.json) reconciles source definitions, the duplicate NDA-triage name, and retained tools. Internal development skills and imported skills without Legalcode names are outside this collection.

The [machine-readable catalogue](catalog.json) records categories, source provenance, package paths and file hashes. [Earlier selection records](selection-2026-09.json) remain available as release history.

With Python 3.10 or newer:

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate-public-skills.py .
python3 -m unittest discover -s scripts/tests
```

Maintainers can regenerate category pages with `python3 scripts/organize-catalog.py .`. The validator checks collection coverage, package licenses, metadata, hashes and navigation. Packaging validation does not certify current legal accuracy or exercise every workflow; verify dated legal examples and authorities for the relevant matter.

## License and permitted use

Legalcode-owned materials released under the [Legalcode Skills Source-Available
License 1.0](LICENSE.md) may be used for personal work, internal business use and
professional services, including paid legal work. Commercial embedding,
redistribution, resale and hosted or automated product offerings require a separate
written license from Legalcode. Using a skill in your own paid AI assistant is
permitted; incorporating it into an application offered to other users is not.

This is a source-available collection, not an open-source grant. Individual skill
packages include the license. Separately licensed components retain their terms.

## Legal Disclaimer

These skills and support files are provided as-is as agent instructions. They
are not legal advice and do not create an attorney-client relationship.
Legalcode is not responsible for how any agent, model, application, workflow, or
user applies these skills, or for any output, recommendation, document,
citation, filing, decision, omission, or other result generated from them.

See [LICENSE.md](LICENSE.md) for the full license and disclaimer.
