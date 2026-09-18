# Runtime requirements

Use the user's chosen agent and available tools. Creating a template and filling it
requires Python 3.9+ and the standard library. The supplied scripts run locally;
no Legalcode connection or particular model is required for extraction or generation.
Keep client documents and private build records local unless the user authorises
another destination.

Paths in this package are relative to the skill directory. Invoke scripts from that
directory or use explicit paths. The generated drafting skill carries its own template,
generator and relevant references, without relying on the builder's installation.

Visual inspection needs a suitable document renderer or editor. Check availability
and report unverified appearance when it cannot be inspected. XML comparison alone
does not establish rendered fidelity.

If separately authorised legal research is needed, discover the connected client's
current tools and verify primary texts for the matter. Do not infer current law from
a sample or require a research connector merely to learn its structure and style.
A helper or companion named in a document is not necessarily installed or authorised.
