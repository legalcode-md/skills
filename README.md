# Legalcode Skills

Public Agent Skills for Legalcode.

Legalcode gives AI agents access to primary legal sources, legal research workflows, and reusable legal skills. This repository is the public skills distribution surface for agents that support `SKILL.md` files and the `skills` CLI.

Website: https://legalcode.md

## Install with skills.sh / skills CLI

```bash
npx skills add legalcode-md/skills --list --full-depth
npx skills add legalcode-md/skills --skill legalcode-public-search --full-depth
```

Install all public Legalcode skills:

```bash
npx skills add legalcode-md/skills --all --full-depth
```

## MCP Endpoints

Anonymous public MCP:

```text
https://mcp.legalcode.md
```

Authenticated MCP for Legalcode Pro accounts:

```text
https://mcppro.legalcode.md
```

Anonymous access supports laws and case law, with rate limits. Pro adds stronger search, more results per query, downloadable results, guidance, and agreements.

## Included Skills

This repository includes 50 public Legalcode skills, with supporting `references/`,
`scripts/`, templates, and agent files copied alongside each `SKILL.md` where used.

The bundle covers:

- MCP setup and public legal source search.
- Legal work orchestration workflows: research, work, review, compounding, tabular review, and case timeline generation.
- Contract review, drafting, redlining, comparison, playbook, obligation, NDA, SaaS, MSA, services, terms, DPA, limitation of liability, indemnity, and AI clause workflows.
- Privacy, data protection, AI governance, EU directive, NIS2, DORA, AML/KYC, sanctions, vendor, third-party, policy gap, and regulatory change workflows.
- Corporate transaction workflows for startups, SAFEs, term sheets, and due diligence.

Run `npx skills add legalcode-md/skills --list --full-depth` to inspect the current skill list.

## Notes

These skills are instructions for agents. They do not send your documents to Legalcode. Your agent works with your data; Legalcode provides legal source lookup.

## Legal Disclaimer

These skills and support files are provided as-is as agent instructions. They
are not legal advice and do not create an attorney-client relationship.
Legalcode is not responsible for how any agent, model, application, workflow, or
user applies these skills, or for any output, recommendation, document,
citation, filing, decision, omission, or other result generated from them.

See [LICENSE.md](LICENSE.md) for the full license and disclaimer.
