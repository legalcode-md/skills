---
name: legalcode-public-search
description: Use the canonical Legalcode connector for primary-source legal research. Discover coverage,
  inspect facets, search, fetch, analyze, trace, and report coverage gaps.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Search

## Connected Surface

- MCP endpoint: `https://mcp.legalcode.md/mcp`
- Main site: `https://legalcode.md`
- Free allowance: 30 MCP requests per 24 hours
- Pro allowance: 1,500 MCP requests per 24 hours
- Core Free sources: laws and the case family
- Advanced plan sources: guidance, agreements, pre-law, and patents

The connector exposes the same five tools and schemas to every account. Advanced operations depend on the connected account plan; do not switch endpoints or start a new OAuth flow after a `subscription_required` response.

## Recommended Workflow

1. Start with `legalcode_discover` for coverage and valid filters.
2. Search by source family with `legalcode_search`.
3. Fetch the top sources before reasoning over the law.
4. Use `legalcode_analyze` for aggregates and `legalcode_trace` for deterministic relationships.
5. Cite returned primary-source identifiers and report coverage gaps instead of guessing.

Concise search responses contain five detailed results plus result stubs where applicable; this is response shaping, not a separate Free-versus-Pro result limit.

## Privacy Boundary

The agent keeps user data. Legalcode processes source lookups and does not store search content as research history.
