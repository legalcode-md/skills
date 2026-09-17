---
name: legalcode-mcp-setup
description: Connect the canonical Legalcode MCP endpoint to Claude, ChatGPT, Codex, Cursor, Windsurf,
  or another MCP-compatible client and verify account-plan access.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode MCP Setup

Use this skill when connecting an AI agent to Legalcode or verifying that legal source lookup is available.

## Endpoint

Use the same Streamable HTTP endpoint for every account plan:

```text
https://mcp.legalcode.md/mcp
```

The connector requests the ordinary Legalcode read scopes. Free and Pro capabilities are resolved from the authenticated account; users do not replace the endpoint after changing plans.

## Setup Flow

1. Open the agent's connector, app, or MCP server settings.
2. Add Legalcode as a remote Streamable HTTP MCP server.
3. Paste `https://mcp.legalcode.md/mcp`.
4. Complete OAuth when prompted.
5. Start a new chat or thread so the newly added connector is visible.
6. Call `legalcode_discover` and run a simple law or case search to confirm the connection.

The connector always exposes `legalcode_discover`, `legalcode_search`, `legalcode_fetch`, `legalcode_analyze`, and `legalcode_trace`. Core law and case-family operations are included in Free. Advanced sources, signed downloads, legislative-history trace, and EU/EEA implementation trace depend on an active Pro plan.

## Privacy Boundary

The agent keeps documents and matter context. Legalcode provides legal source lookup. Send source lookup queries to MCP; do not upload client documents to Legalcode.

## Links

- Legalcode: https://legalcode.md
- Install docs: https://legalcode.md/docs/install
- Legalcode MCP: https://mcp.legalcode.md/mcp
