# Runtime requirements

Use the user's chosen agent and available tools. Creating a template and filling it
requires Python 3.9+ and the standard library. Do not assume Python is installed on
the user's computer. Check the environment where the helpers will actually run;
an available agent runtime may already provide it. The supplied scripts run locally;
no Legalcode connection or particular model is required for extraction or generation.
Keep client documents and private build records local unless the user authorises
another destination.

## First use on Windows

Check for a working interpreter with `py -3 --version` or `python --version`;
`python3 --version` may also work. Confirm that the result is Python 3.9 or newer.
A missing `python3` command alone does not mean Python is absent. Use the working
launcher for the documented commands. No additional Python packages are needed.

If no suitable interpreter is available, use `uv` to obtain and run Python. Neither
Python nor pip needs to be installed first. If `uv --version` already works, reuse
it. Otherwise, where software installation is authorised and WinGet is available,
install uv from PowerShell:

```powershell
winget install --id=astral-sh.uv -e
```

If WinGet is unavailable, use Astral's [standalone Windows installer](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer), which also works without Python.
On a managed office computer that blocks installation or downloads, use the IT-approved
installation route or an already available execution environment; do not bypass restrictions.
Reuse existing installation authorisation rather than asking again.

Reopen the terminal after installation, then check the runtime:

```powershell
uv --version
uv run --no-project --python 3.12 python --version
```

By default, uv downloads Python 3.12 if it is missing. This first setup needs network
access; the document helpers themselves do not. In the documented helper commands,
replace `python3` with `uv run --no-project --python 3.12 python`, keeping the script
path and arguments. `--no-project` avoids loading an unrelated project's dependencies.
The version shown is a supported example, not a requirement to replace working Python.
See Astral's [Python installation](https://docs.astral.sh/uv/guides/install-python/)
and [script execution](https://docs.astral.sh/uv/guides/scripts/) guidance.

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
