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


def validate(root):
    catalog = json.loads((root / "catalog.json").read_text())
    selection = json.loads((root / "selection-2026-09.json").read_text())
    entries = catalog["skills"]
    names = [item["name"] for item in entries]
    errors = []
    assert len(names) == len(set(names)) == catalog["total_count"] == selection["total_count"]
    selected = {item["name"] for item in selection["skills"]}
    assert selected == {item["name"] for item in entries if item["addition"]}
    assert len(selected) == selection["additional_count"] == 200
    assert Counter(item["scope"] for item in entries if item["addition"]) == {"general": 130, "jurisdictions": 70}
    assert {p.name for p in (root / "skills").iterdir()} == set(names)
    file_count = 0
    for entry in entries:
        directory = root / "skills" / entry["name"]
        files = {str(p.relative_to(directory)): p for p in directory.rglob("*") if p.is_file()}
        assert set(files) == set(entry["files"]), f"Inventory mismatch: {entry['name']}"
        for relative, path in files.items():
            file_count += 1
            if path.is_symlink():
                errors.append(f"Symlink: {path}")
            if hashlib.sha256(path.read_bytes()).hexdigest() != entry["files"][relative]:
                errors.append(f"Hash mismatch: {path}")
            if path.suffix != ".md":
                continue
            for label, target in re.findall(r"\[([^\]\n]+)\]\(([^)\n]+)\)", path.read_text()):
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
        if set(metadata) - {"name", "description", "license", "metadata", "allowed-tools"}:
            errors.append(f"Unsupported frontmatter: {entry['name']}")
        if metadata.get("name") != entry["name"] or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", entry["name"]) or len(entry["name"]) > 64:
            errors.append(f"Name mismatch: {entry['name']}")
        description = metadata.get("description", "")
        if not isinstance(description, str) or not 1 <= len(description) <= 1024 or any(c in description for c in "<>"):
            errors.append(f"Invalid description: {entry['name']}")
        if "references/runtime-compatibility.md" not in text:
            errors.append(f"Missing runtime guidance: {entry['name']}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(entries)} skills, {len(selected)} additions, {file_count} verified files; names, frontmatter, hashes and local links valid.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    validate(parser.parse_args().root.resolve())
