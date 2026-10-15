# Runtime requirements

Use the user's chosen agent and available tools. Creating a template and filling it
with the supplied DOCX or PPTX text helpers requires Python 3.9+ and the standard library. Do not assume Python is installed on
the user's computer. Check the environment where the helpers will actually run;
an available agent runtime may already provide it. The supplied scripts run locally;
no Legalcode connection or particular model is required for extraction or generation.
Keep client documents and private build records local unless the user authorises
another destination.

## Python availability

Reuse a working Python 3.9+ interpreter supplied by the platform or already
available in the execution environment. Use its actual launcher for the documented
commands; `python3` is only an example. No additional Python packages are needed.

If Python is unavailable, let the platform choose its normal supported installation
or execution method within existing permissions. Do not require a particular
installer, package manager or Python version beyond the scripts' minimum requirement.
Respect managed-environment restrictions and report a concrete blocker if no
supported method is available.

## Files, rendering and research

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
