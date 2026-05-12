# Legalcode Skills

Public Agent Skills for Legalcode.

Legalcode gives AI agents access to primary legal sources, legal research workflows, and reusable legal skills. This repository is the public skills distribution surface for agents that support `SKILL.md` files and the `skills` CLI.

Website: https://legalcode.md

## Install with skills.sh / skills CLI

```bash
npx skills add RobertHH-IS/legalcode-skills --list --full-depth
npx skills add RobertHH-IS/legalcode-skills --skill legalcode-public-search --full-depth
```

Install all public Legalcode skills:

```bash
npx skills add RobertHH-IS/legalcode-skills --all --full-depth
```

## MCP Endpoints

Anonymous public MCP:

```text
https://mcp.legalcode.md
```

Pro MCP:

```text
https://mcppro.legalcode.md
```

Anonymous access supports laws and case law, with rate limits. Pro adds stronger search, more results per query, downloadable results, guidance, and agreements.

## Included Skills

- `legalcode-mcp-setup` - connect Legalcode MCP to supported agents.
- `legalcode-public-search` - use public Legalcode law and case search.
- `legalcode-contract-review` - review contracts with legal-source grounding.
- `legalcode-nda-triage` - screen NDAs and flag negotiation issues.
- `legalcode-dpia-generator` - generate DPIA work product from local facts.
- `legalcode-document-qa` - answer questions across local documents.
- `legalcode-legal-memorandum` - structure legal analysis into a memo.
- `legalcode-statute-analysis` - analyze statutory provisions and source context.
- `legalcode-case-timeline-builder` - build case chronologies from local evidence.
- `legalcode-tabular-review` - create citation-backed document review tables.

## Notes

These skills are instructions for agents. They do not send your documents to Legalcode. Your agent works with your data; Legalcode provides legal source lookup.
