#!/usr/bin/env python3
"""Categorize the public catalogue and generate browsable GitHub indexes."""

import argparse
from collections import Counter, defaultdict
import json
import os
from pathlib import Path
import re
import shutil

AREAS = {
    "contracts-commercial": ("Contracts & commercial", "Drafting, negotiation, clause review and contract lifecycle work."),
    "corporate-financing": ("Corporate & financing", "Formation, governance documents, M&A and venture financing."),
    "privacy-data-protection": ("Privacy & data protection", "Privacy programmes, data rights, breach response and assessments."),
    "ai-technology": ("AI & technology", "AI governance, automated decisions and technology risk."),
    "employment-workplace": ("Employment & workplace", "Employment contracts, pay, investigations and worker protections."),
    "financial-regulation": ("Financial regulation", "Financial services, lending, securities and regulatory compliance."),
    "governance-compliance": ("Governance & compliance", "Corporate compliance, competition, anti-corruption and reporting."),
    "eu-eea-implementation": ("EU & EEA implementation", "Directives, incorporation, transposition, conformity and gold-plating."),
    "litigation-disputes": ("Litigation & disputes", "Case preparation, pleadings, evidence, discovery and settlement."),
    "intellectual-property": ("Intellectual property", "Copyright, patents, trademarks, licensing and trade secrets."),
    "real-estate-construction": ("Real estate & construction", "Property transactions, leases, land use and building contracts."),
    "legal-research": ("Legal research", "Source discovery, authority verification and comparative analysis."),
    "drafting-documents": ("Drafting & document analysis", "Writing, document review, extraction and reusable document skills."),
    "legal-operations": ("Legal operations", "Intake, matter management, budgets, knowledge and legal-team processes."),
    "tools-orchestration": ("Tools & orchestration", "MCP setup and coordinated research, review and delivery workflows."),
}

JURISDICTIONS = {
    "australia": "Australia", "brazil": "Brazil", "canada": "Canada", "china": "China",
    "european-union": "European Union", "france": "France", "germany": "Germany", "iceland": "Iceland",
    "india": "India", "ireland": "Ireland", "japan": "Japan", "new-zealand": "New Zealand",
    "nordic": "Nordic region", "poland": "Poland", "singapore": "Singapore",
    "switzerland": "Switzerland", "united-kingdom": "United Kingdom", "united-states": "United States",
}


def classify(entry):
    """Ordered topic rules; source folders provide the fallback, not release history."""
    name, source = entry["name"], entry["source"]
    if name in {"legalcode-mcp-setup", "legalcode-tabular-review-orchestrator"} or name.startswith("legalcode-workflow-"):
        return "tools-orchestration"
    if any(t in name for t in ("gold-plating", "eea-", "eu-directive", "eu-transposition", "eu-correlation", "eu-conformity", "eu-infringement")):
        return "eu-eea-implementation"
    if any(t in name for t in ("case-timeline", "litigation-hold")):
        return "litigation-disputes"
    if any(t in name for t in ("ai-training-data", "ip-", "copyright", "patent", "trademark", "trade-secret", "technology-license", "open-source-license", "licensing-agreement")):
        return "intellectual-property"
    if any(t in name for t in ("ai-", "algorithmic", "admt")):
        return "ai-technology"
    if any(t in name for t in ("employment", "employee", "labor-", "workplace", "fair-work", "non-compete", "termination", "severance", "wage-", "pay-equity", "erisa", "pensions-", "accommodation", "ada-", "warn-act", "contractor-classification", "collective-bargaining", "immigration", "offer-letter", "betriebsrat", "kuendigung", "contrat-de-travail", "clt-")):
        return "employment-workplace"
    if any(t in name for t in ("real-estate", "lease", "tenancy", "bail-commercial", "construction", "jct-nec", "title-review", "zoning")):
        return "real-estate-construction"
    if any(t in name for t in ("privacy", "data-mapping", "data-processing", "data-protection", "breach", "gdpr", "dpia", "dpa-", "ropa", "dsar", "cookie", "consent", "cross-border-transfer", "legitimate-interest", "pipeda", "ndsg", "cnil", "biometric", "coppa", "hipaa", "canned-responses-")):
        return "privacy-data-protection"
    if any(t in name for t in ("aml-", "sanctions", "ofac", "fintech", "lending", "loan-agreement", "security-collateral", "structured-finance", "securities", "sec-filing", "prospectus", "offering", "fca-", "asic-", "dora-", "pci-dss", "private-placement")):
        return "financial-regulation"
    if any(t in name for t in ("precedent", "statute-analysis", "legislation-verification", "citation-checker", "jurisdiction-mapper", "public-search", "cantonal-law")):
        return "legal-research"
    if any(t in name for t in ("document-", "grill-document", "minnisblad", "malstadur", "proofread", "plain-language", "defined-term", "cross-reference", "legal-memorandum", "tabular-review", "tabulate", "faq-generator", "estate-plan", "demand-letter")):
        return "drafting-documents"
    if any(t in name for t in ("litigation-budget", "clause-library", "contract-playbook", "obligation-tracker", "entity-compliance")):
        return "legal-operations"
    if "/litigation/" in source:
        return "litigation-disputes"
    if "/corporate" in source or "venture-financing" in name or "entity-formation" in name or "company-formation" in name:
        return "corporate-financing"
    if "/contracts/" in source:
        return "contracts-commercial"
    if "/ip/" in source:
        return "intellectual-property"
    if "/compliance/" in source or "/risk-assessment/" in source:
        return "governance-compliance"
    return "legal-operations"


def location(entry):
    parts = entry["source"].split("/")
    if "jurisdictions" in parts:
        return parts[parts.index("jurisdictions") + 1]
    # A small number of explicitly local workflows were stored in general/.
    if entry["name"] in {"legalcode-complaint-drafter-is", "legalcode-minnisblad", "legalcode-malstadur"}:
        return "iceland"
    if entry["name"] == "legalcode-complaint-drafter-ew":
        return "united-kingdom"
    return None


def title(entry):
    text = entry["name"].removeprefix("legalcode-").replace("-", " ").capitalize()
    for acronym in ("mcp", "nda", "gdpr", "eu", "eea", "ai", "dpa", "dpia", "dsar", "aml", "kyc", "ip", "us", "uk", "fca", "ofac", "sox", "hipaa", "coppa", "nist", "csf", "pci", "dss"):
        text = re.sub(rf"\b{acronym}\b", acronym.upper(), text, flags=re.I)
    return text


def rel(from_file, target):
    return Path(os.path.relpath(target, from_file.parent)).as_posix()


def generate(root, move=False):
    catalog = json.loads((root / "catalog.json").read_text())
    entries = catalog["skills"]
    for entry in entries:
        area = entry.get("practice_area") or classify(entry)
        jurisdiction = entry.get("jurisdiction") or location(entry)
        destination = f"skills/jurisdictions/{jurisdiction}/{area}/{entry['name']}" if jurisdiction else f"skills/general/{area}/{entry['name']}"
        old = root / entry.get("path", f"skills/{entry['name']}")
        new = root / destination
        if move and old != new:
            new.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(old), str(new))
        entry.update(path=destination, practice_area=area, jurisdiction=jurisdiction,
                     scope="jurisdictions" if jurisdiction else "general", category=area)
    catalog["layout_version"] = 2
    catalog["total_count"] = len(entries)
    catalog["practice_areas"] = {key: {"title": v[0], "description": v[1]} for key, v in AREAS.items()}
    (root / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n")
    by_area, by_jurisdiction, by_folder = defaultdict(list), defaultdict(list), defaultdict(list)
    for entry in entries:
        by_area[entry["practice_area"]].append(entry)
        if entry["jurisdiction"]:
            by_jurisdiction[entry["jurisdiction"]].append(entry)
        by_folder[Path(entry["path"]).parent].append(entry)

    def page(path, heading, intro, members):
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        lines = [f"# {heading}", "", intro, "", f"[Browse all categories]({rel(target, root / 'CATALOG.md')}) · [Installation]({rel(target, root / 'README.md')}#install)", "",
                 "| Skill | Scope |", "| --- | --- |"]
        for entry in sorted(members, key=lambda e: e["name"]):
            scope = JURISDICTIONS.get(entry["jurisdiction"], "General / cross-jurisdiction")
            lines.append(f"| [{title(entry)}]({rel(target, root / entry['path'] / 'SKILL.md')}) | {scope} |")
        lines += ["", "Install any skill by its exact folder name:", "", "```sh", f"npx skills add legalcode-md/skills --skill {sorted(members, key=lambda e: e['name'])[0]['name']} --full-depth", "```", ""]
        target.write_text("\n".join(lines))

    for area, members in by_area.items():
        page(Path("catalog/practice-areas") / f"{area}.md", AREAS[area][0], f"{len(members)} skills. {AREAS[area][1]}", members)
    for jurisdiction, members in by_jurisdiction.items():
        page(Path("catalog/jurisdictions") / f"{jurisdiction}.md", JURISDICTIONS[jurisdiction], f"{len(members)} jurisdiction-specific skills, across practice areas.", members)
    for folder, members in by_folder.items():
        page(folder / "README.md", AREAS[folder.name][0], f"{len(members)} skills in this folder.", members)

    def index(path, heading, items):
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(f"# {heading}\n\n" + "\n".join(f"- [{label}]({rel(target, root / dest)}) — {count} skills" for label, dest, count in items) + "\n")

    generals = Counter(e["practice_area"] for e in entries if not e["jurisdiction"])
    index(Path("skills/general/README.md"), "General skills by practice area", [(AREAS[k][0], f"skills/general/{k}/README.md", generals[k]) for k in AREAS if generals[k]])
    index(Path("skills/jurisdictions/README.md"), "Skills by jurisdiction", [(JURISDICTIONS[k], f"skills/jurisdictions/{k}/README.md", len(v)) for k, v in sorted(by_jurisdiction.items())])
    for jurisdiction, members in by_jurisdiction.items():
        counts = Counter(e["practice_area"] for e in members)
        index(Path(f"skills/jurisdictions/{jurisdiction}/README.md"), JURISDICTIONS[jurisdiction], [(AREAS[k][0], f"skills/jurisdictions/{jurisdiction}/{k}/README.md", counts[k]) for k in AREAS if counts[k]])
    index(Path("skills/README.md"), "Browse Legalcode skills", [("General skills", "skills/general/README.md", sum(generals.values())), ("Jurisdiction-specific skills", "skills/jurisdictions/README.md", sum(map(len, by_jurisdiction.values())))])

    lines = ["# Legalcode Skills Catalogue", "", f"**{len(entries)} unique skills.** Browse by the work you need to do or by jurisdiction. Install names stay the same across categories.", "",
             "## By practice area", "", "Each practice-area page includes both general and jurisdiction-specific skills.", "", "| Practice area | Skills | What you can do |", "| --- | ---: | --- |"]
    for key, (label, description) in AREAS.items():
        lines.append(f"| [{label}](catalog/practice-areas/{key}.md) | {len(by_area[key])} | {description} |")
    lines += ["", "## By jurisdiction", "", "| Jurisdiction | Skills |", "| --- | ---: |"]
    for key, members in sorted(by_jurisdiction.items()):
        lines.append(f"| [{JURISDICTIONS[key]}](catalog/jurisdictions/{key}.md) | {len(members)} |")
    lines += ["", "[Browse general skill folders](skills/general/README.md) · [Browse jurisdiction folders](skills/jurisdictions/README.md)", "",
              "## Installation", "", "```sh", "npx skills add legalcode-md/skills --list --full-depth", "```", "",
              "See the [README](README.md#install) for individual installation. The [machine-readable catalogue](catalog.json) records every package path and file hash.", ""]
    (root / "CATALOG.md").write_text("\n".join(lines))
    previous_readme = (root / "README.md").read_text()
    legal_sections = "## License and permitted use\n" + previous_readme.split("## License and permitted use\n", 1)[1]
    featured = [
        ("Review a contract", "legalcode-contract-review"),
        ("Research primary law", "legalcode-public-search"),
        ("Build a skill from example documents", "legalcode-document-to-skill"),
        ("Question and improve a legal draft", "legalcode-grill-document"),
        ("Assess Icelandic EEA implementation", "legalcode-eea-conformity-assessment-is"),
        ("Review a data breach", "legalcode-breach-severity-assessment"),
    ]
    by_name = {e["name"]: e for e in entries}
    readme = ["# Legalcode Skills", "", f"**{len(entries)} legal skills**, organized into **{len(by_area)} practice areas** and **{len(by_jurisdiction)} jurisdiction groups**.", "",
              "[Browse the catalogue](CATALOG.md) · [General skills](skills/general/README.md) · [By jurisdiction](skills/jurisdictions/README.md)", "",
              "## Start with a task", ""]
    for label, name in featured:
        readme.append(f"- [{label}]({by_name[name]['path']}/SKILL.md)")
    readme += ["", "## Browse by practice area", "", "Each area includes general and bespoke local workflows.", "", "| Practice area | Skills |", "| --- | ---: |"]
    for key, (label, _) in AREAS.items():
        readme.append(f"| [{label}](catalog/practice-areas/{key}.md) | {len(by_area[key])} |")
    readme += ["", "## Browse by jurisdiction", "",
               " · ".join(f"[{JURISDICTIONS[k]}](catalog/jurisdictions/{k}.md)" for k in sorted(by_jurisdiction)), "",
               "## Install", "", "List available skills, then install only the workflows you need:", "", "```sh",
               "npx skills add legalcode-md/skills --list --full-depth",
               "npx skills add legalcode-md/skills --skill legalcode-contract-review --full-depth", "```", "",
               "Install the full collection with:", "", "```sh", "npx skills add legalcode-md/skills --all --full-depth", "```", "",
               "Requires Node.js/npm for the skills CLI. Install names are unchanged. Skill folders now live under `skills/general/<practice-area>/` or `skills/jurisdictions/<jurisdiction>/<practice-area>/`. Use `--full-depth` for recursive discovery. Existing flat GitHub file links should be replaced with the paths in the catalogue; no reinstall is needed solely for the folder change.", "",
               "Each package carries its scripts, references, templates and license. Check the skill's stated prerequisites before running external software or services. No model or provider is pinned.", "",
               "## Legalcode connection", "", "Add `https://mcp.legalcode.md/mcp` as a remote Streamable HTTP connector and complete authentication. Discover current coverage and permissions, then Search and Fetch primary texts before relying on them. Analyze and Trace support aggregate and relationship queries. Keep confidential documents local and minimize matter facts in source queries.", "",
               "## Collection and validation", "",
               "This release publishes every unique `legalcode-` name in the source collection, retaining previously published workflow tools. The [coverage record](collection-coverage.json) reconciles source definitions, the duplicate NDA-triage name, and retained tools. Internal development skills and imported skills without Legalcode names are outside this collection.", "",
               "The [machine-readable catalogue](catalog.json) records categories, source provenance, package paths and file hashes. [Earlier selection records](selection-2026-09.json) remain available as release history.", "",
               "With Python 3.10 or newer:", "", "```sh", "python3 -m pip install -r requirements-dev.txt", "python3 scripts/validate-public-skills.py .", "python3 -m unittest discover -s scripts/tests", "```", "",
               "Maintainers can regenerate category pages with `python3 scripts/organize-catalog.py .`. The validator checks collection coverage, package licenses, metadata, hashes and navigation. Packaging validation does not certify current legal accuracy or exercise every workflow; verify dated legal examples and authorities for the relevant matter.", "",
               legal_sections]
    (root / "README.md").write_text("\n".join(readme))
    print(f"Organized {len(entries)} skills into {len(by_area)} practice areas and {len(by_jurisdiction)} jurisdictions.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path.cwd())
    parser.add_argument("--move", action="store_true", help="Move skill folders to their categorized paths")
    args = parser.parse_args()
    generate(args.root.resolve(), args.move)
