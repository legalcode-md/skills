---
name: legalcode-mcp-setup
description: >
  Connect Legalcode MCP to an AI agent and choose the right endpoint. Use when setting up
  Legalcode in Claude, Claude Code, ChatGPT, Codex, Cursor, Windsurf, or another
  MCP-compatible client; when deciding between anonymous public MCP and Pro MCP; or when
  verifying that legal source lookup is available to an agent.
---

# Legalcode MCP Setup

Use this skill when the task is to connect an AI agent to Legalcode or decide which Legalcode endpoint to use.

## Endpoints

Public anonymous MCP:

```text
https://mcp.legalcode.md
```

Pro MCP:

```text
https://mcppro.legalcode.md
```

Some clients expect an explicit MCP path. If the root URL does not connect, use:

```text
https://mcp.legalcode.md/mcp
https://mcppro.legalcode.md/mcp
```

## Choose Public or Pro

Use public MCP when:

- the user needs anonymous law and case law lookup
- top 5 results per query is enough
- 30 requests per IP per day is enough
- no account or OAuth flow is desired

Use Pro MCP when:

- the user needs stronger search or AND/OR search
- the user needs up to 20 results per query
- the user needs guidance or agreements
- the user needs downloads/direct-to-file workflows
- the user needs authenticated higher-throughput access

## Setup Flow

1. Open the agent's connector, app, or MCP server settings.
2. Add Legalcode as a remote MCP server.
3. Paste the public or Pro endpoint.
4. If using Pro, complete the OAuth/authentication flow when prompted.
5. Run a simple jurisdiction or law search to confirm the connection.

## Privacy Boundary

Your agent keeps your documents and matter context. Legalcode provides legal source lookup. Send source lookup queries to MCP; do not upload client documents to Legalcode.

## Links

- Legalcode: https://legalcode.md
- Install docs: https://legalcode.md/docs/install
- Public MCP: https://mcp.legalcode.md
- Pro MCP: https://mcppro.legalcode.md
