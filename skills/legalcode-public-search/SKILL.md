---
name: legalcode-public-search
description: >
  Use Legalcode's public search surface for anonymous legal research across laws and
  cases. Start with jurisdiction discovery, inspect facets, search laws or case law,
  fetch top sources, and escalate to Legalcode Pro when the task needs guidance,
  agreements, stronger search, or higher throughput.
---

# Legalcode Public Search

Use this skill when you need primary legal sources from Legalcode without authentication.

## Public Surface

- Public MCP endpoint: `https://mcp.legalcode.md`
- API docs: `https://api.legalcode.md/docs`
- Main site: `https://legalcode.md`
- Anonymous rate limit: 30 requests per IP per day
- Anonymous result cap: top 5 results per query
- Public source types: laws and case law

## Recommended Workflow

1. Start with jurisdiction discovery.
2. Inspect facets before filtering in an unfamiliar jurisdiction.
3. Search by source type:
   - use law search for statutes, regulations, directives, and codes
   - use case search for court decisions and precedent
4. Fetch the top sources before reasoning over the law.
5. Cite the returned primary source identifiers, not model memory.
6. If the task needs guidance, agreements, AND/OR search, result downloads, more than 5 results, or higher throughput, switch to Legalcode Pro at `https://mcppro.legalcode.md`.

## Search-Agent Pattern

For legal research, use an evidence-package workflow:

1. Identify the issue, jurisdiction, and source type.
2. Run a broad query.
3. Inspect facets and narrow with targeted follow-up searches.
4. Fetch the most relevant sources.
5. Package findings with source references, snippets, citations, and coverage gaps.
6. Only then synthesize the answer.

## Privacy Boundary

Your agent keeps your data. Legalcode processes source lookups and does not store search content as research history.
