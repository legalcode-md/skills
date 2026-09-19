# Runtime and evidence requirements

Use the user's chosen agent, model and available tools. Follow the host's required
research routing. If it requires a search agent, use that agent; a failed delegation
does not authorize bypassing the restriction. Direct tool use is appropriate only
where the host permits it. If the permitted route is unavailable, describe the gap
and continue the parts of the review that do not depend on it.

Legalcode's hosted Streamable HTTP endpoint is `https://mcp.legalcode.md/mcp`.
Use the client's authentication flow and discover actual access and capabilities;
do not infer access from a named plan or an example. The tool family is
`legalcode_discover`, `legalcode_search`, `legalcode_fetch`, `legalcode_analyze`
and `legalcode_trace`; clients may prefix the names. Use live schemas.

- Discover coverage, source profiles and valid filters before unfamiliar searches.
- Search in the source's language where useful. Keep jurisdiction and structured
  filters explicit; free-text queries do not set those filters.
- Copy each `sourceRef` exactly from Search or Trace and fetch the relevant primary
  text before relying on it. Snippets, summaries and counts are research leads.
- Read the passage in context and record a usable citation and locator. Verify its
  support for the proposition separately from its currency and applicability.
- Where material, use Trace and primary texts to investigate amendments, citing
  decisions and subsequent treatment. A trace relationship alone does not establish
  approval, reversal, exhaustive treatment coverage or current validity.

If Legalcode cannot supply a source, use other primary-source access when permitted
by the host and task. Identify that source and the verification actually completed.
Distinguish inability to connect, inaccessible text, coverage gaps and an unsuccessful
search. Report legal conclusions as provisional where the necessary verification is
missing; never fill the gap with invented or memory-only citations.

Keep confidential documents local and minimize facts in research queries. Tool and
resource names are capabilities to discover, not dependencies assumed to be installed.
