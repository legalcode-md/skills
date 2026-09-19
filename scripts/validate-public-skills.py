#!/usr/bin/env python3
"""Validate a built public catalogue, including individually installable resources."""

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

import yaml


def prose_links(text):
    """Find reference links outside fenced examples, which may describe generated files."""
    lines, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            run, rest = marker.groups()
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence) and not rest.strip():
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return re.findall(r"\[([^\]\n]+)\]\(([^)\n]+)\)", "\n".join(lines))


def validate(root):
    catalog = json.loads((root / "catalog.json").read_text())
    coverage = json.loads((root / "collection-coverage.json").read_text())
    entries = catalog["skills"]
    names = [item["name"] for item in entries]
    errors = []
    license_text = (root / "LICENSE.md").read_bytes()
    assert len(names) == len(set(names)) == catalog["total_count"] == coverage["total_count"]
    collection_names = {item["published_name"] for item in coverage["definitions"]}
    assert len(coverage["definitions"]) == coverage["definition_count"]
    assert len(collection_names) == coverage["unique_collection_names"]
    assert set(names) == collection_names | set(coverage["preserved_public_workflows"])
    assert len(names) == coverage["previous_published_count"] + len(coverage["new_skill_names"])
    paths = {str(p.parent.relative_to(root)) for p in (root / "skills").rglob("SKILL.md")}
    assert paths == {item["path"] for item in entries}
    file_count = 0
    for entry in entries:
        directory = root / entry["path"]
        assert directory.resolve().is_relative_to((root / "skills").resolve())
        assert directory.name == entry["name"]
        area = entry["practice_area"]
        assert area in catalog["practice_areas"]
        expected = (f"skills/jurisdictions/{entry['jurisdiction']}/{area}/{entry['name']}"
                    if entry["jurisdiction"] else f"skills/general/{area}/{entry['name']}")
        assert entry["path"] == expected
        files = {str(p.relative_to(directory)): p for p in directory.rglob("*") if p.is_file()}
        assert set(files) == set(entry["files"]), f"Inventory mismatch: {entry['name']}"
        if "LICENSE.md" not in files or files["LICENSE.md"].read_bytes() != license_text:
            errors.append(f"Missing or inconsistent package license: {entry['name']}")
        for relative, path in files.items():
            file_count += 1
            if path.is_symlink():
                errors.append(f"Symlink: {path}")
            if hashlib.sha256(path.read_bytes()).hexdigest() != entry["files"][relative]:
                errors.append(f"Hash mismatch: {path}")
            if path.suffix != ".md":
                continue
            for label, target in prose_links(path.read_text()):
                target = target.split(' "')[0].split("#")[0]
                if not target or re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:|#", target):
                    continue
                # Legal citations and template fields are not filesystem links.
                if any(char in target for char in "{}[]"):
                    continue
                resolved = (path.parent / unquote(target)).resolve()
                if not resolved.is_relative_to(directory.resolve()) or not resolved.exists():
                    errors.append(f"Unbundled local link: {entry['name']}/{relative}: {target}")
        text = (directory / "SKILL.md").read_text()
        match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not match:
            errors.append(f"Missing frontmatter: {entry['name']}")
            continue
        metadata = yaml.safe_load(match[1])
        if metadata.get("license") != "Legalcode Skills Source-Available License 1.0; see LICENSE.md":
            errors.append(f"Missing or inconsistent license metadata: {entry['name']}")
        if set(metadata) - {"name", "description", "license", "metadata", "allowed-tools"}:
            errors.append(f"Unsupported frontmatter: {entry['name']}")
        if metadata.get("name") != entry["name"] or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", entry["name"]) or len(entry["name"]) > 64:
            errors.append(f"Name mismatch: {entry['name']}")
        description = metadata.get("description", "")
        if not isinstance(description, str) or not 1 <= len(description) <= 1024 or any(c in description for c in "<>"):
            errors.append(f"Invalid description: {entry['name']}")
        if "references/runtime-compatibility.md" not in text:
            errors.append(f"Missing runtime guidance: {entry['name']}")
    # Every browsing page must resolve locally; every skill must be reachable by
    # practice area and, when applicable, by jurisdiction.
    docs = [root / "CATALOG.md", *sorted((root / "catalog").rglob("*.md")),
            *[p for p in (root / "skills").rglob("README.md") if not any(p.is_relative_to(root / e["path"]) for e in entries)]]
    for doc in docs:
        for label, target in prose_links(doc.read_text()):
            target = target.split("#")[0]
            if not target or re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            if not (doc.parent / unquote(target)).exists():
                errors.append(f"Broken navigation link: {doc.relative_to(root)}: {target}")
    for entry in entries:
        pages = [root / "catalog/practice-areas" / f"{entry['practice_area']}.md"]
        if entry["jurisdiction"]:
            pages.append(root / "catalog/jurisdictions" / f"{entry['jurisdiction']}.md")
        for page in pages:
            if f"/{entry['name']}/SKILL.md" not in page.read_text():
                errors.append(f"Skill absent from browse page: {entry['name']}: {page.name}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(entries)} skills, {file_count} verified files; collection coverage, licenses, metadata, hashes and category navigation valid.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    validate(parser.parse_args().root.resolve())
