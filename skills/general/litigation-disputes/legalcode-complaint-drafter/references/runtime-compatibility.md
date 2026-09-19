# Runtime and evidence requirements

Use the user's chosen agent, model and available tools. This public distribution does
not require a particular provider or model. Provider-specific tool names, delegation
commands and request examples in the workflow are illustrative: inspect the connected
client's actual capabilities before using them. If a requested helper or sibling skill
is unavailable, perform the supported work directly or report the concrete gap.

For Legalcode research, connect to `https://mcp.legalcode.md/mcp` and complete the
client's authentication flow. Use live tool discovery and the connected account's
entitlements; do not infer access from old plan names, quotas or examples.

The current tool family is `legalcode_discover`, `legalcode_search`, `legalcode_fetch`,
`legalcode_analyze` and `legalcode_trace`; a client may namespace these names. Discover
coverage, source profiles and valid filters before unfamiliar searches. Follow the
current tool schemas instead of copying historical request examples in a workflow.
Copy each `sourceRef` exactly from Search or Trace and Fetch the relevant text before
relying on it. Search snippets and aggregate counts are not verified legal authority.
Keep jurisdiction and structured filters explicit; query text does not set them.

Treat dated statutory examples, thresholds, deadlines, case citations and regulator
positions as research leads. Verify the relevant jurisdiction, version, effective date
and primary text for the user's matter. Record gaps and uncertainty; do not present a
workflow's historical reference material as current law. Keep confidential documents
local and minimize matter facts in source queries.

Install companion skills only when needed for the task. A companion's name in the
workflow does not mean it is already installed. Packaged scripts and local references
are relative to this skill's installation directory. External software prerequisites
must be checked before running scripts. Example output placeholders belong in templates,
not in completed deliverables.
