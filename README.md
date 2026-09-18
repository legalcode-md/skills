# Legalcode Skills

**251 legal skills** for agents that support `SKILL.md` packages: practical general
workflows alongside bespoke jurisdiction-specific work.

Browse the [complete catalogue](CATALOG.md). The September 2026 expansion adds
**200 Legalcode-authored skills** to the existing 50-skill selection:

| Addition area | Skills |
| --- | ---: |
| Compliance, privacy, AI and EU/EEA implementation | 38 |
| Litigation and dispute resolution | 24 |
| Research, document quality and matter workflows | 20 |
| Contract drafting, review and lifecycle work | 18 |
| Corporate transactions, governance and financing | 16 |
| Intellectual property | 6 |
| Real estate | 4 |
| Banking and finance | 3 |
| Cross-practice legal risk assessment | 1 |
| Bespoke jurisdiction-specific workflows | 70 |
| **Total additions** | **200** |

Bespoke coverage spans Australia, Brazil, Canada, China, the EU, France, Germany,
Iceland, India, Ireland, Japan, New Zealand, the Nordic region, Poland, Singapore,
Switzerland, the UK and the US. Highlights include Icelandic gold-plating and EEA
conformity assessments, national employment and contract reviews, venture financing,
construction contracts and local regulatory compliance.

## Install

List the available skills:

```sh
npx skills add legalcode-md/skills --list --full-depth
```

Install the document-to-skill builder:

```sh
npx skills add legalcode-md/skills --skill legalcode-document-to-skill --full-depth
```

Install a general workflow:

```sh
npx skills add legalcode-md/skills --skill legalcode-contract-review --full-depth
```

Install a bespoke workflow:

```sh
npx skills add legalcode-md/skills --skill legalcode-eea-conformity-assessment-is --full-depth
```

To install the complete collection:

```sh
npx skills add legalcode-md/skills --all --full-depth
```

Choose the skills relevant to your work. Each folder includes its own required local
references and resources. Some workflows can use companion skills or external tools;
the workflow describes those prerequisites. No model or provider is pinned.

## Legalcode connection

Use the hosted Streamable HTTP endpoint:

```text
https://mcp.legalcode.md/mcp
```

Complete the client authentication flow and discover current coverage and access.
The Legalcode tools are Discover, Search, Fetch, Analyze and Trace. Fetch primary
texts before relying on sources. Keep confidential documents local and minimize
matter facts in source queries.

Website: [legalcode.md](https://legalcode.md).

## Selection and provenance

The 200 additions were selected from our source collection's **Legalcode original**
and **Complete** entries. Selection favors useful, distinct workflows, verification
and output guidance, and a balance of general and bespoke coverage. Imported entries
and overlapping variants were excluded from this expansion.

- [Selection record](selection-2026-09.json): source paths and rationale for all 200 additions.
- [Integrity manifest](catalog.json): source provenance, original metadata and hashes for every packaged file.

The 251 total preserves the existing 50-skill selection, adds 200 curated skills,
and includes the document-to-skill builder as a later addition.

The workflow bodies preserve their original legal analysis and attribution. Portable
frontmatter, shorter discovery descriptions, current runtime guidance and bundled
shared references make the collection installable across supported clients. Original
full descriptions remain available inside the skills.

Publication validation checks packaging and resource integrity. It does not certify
current legal accuracy or successful execution of every workflow. Verify dated legal
examples, citations, thresholds and deadlines against current primary authorities
for the relevant matter. Preserve embedded attribution and license notices.

## Validate a checkout

With Python 3.10 or newer:

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate-public-skills.py .
```

The validator checks all 251 names, metadata, the 200-addition selection, file hashes
and local Markdown references. `catalog.json` is generated with the source export;
rebuild it when changing packaged skill files.

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
