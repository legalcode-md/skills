#!/usr/bin/env python3
"""Inspect PPTX slide order, text, design declarations, notes and retained parts.

    python3 scripts/inspect_pptx.py sample.pptx
    python3 scripts/inspect_pptx.py sample.pptx --text --include-notes
    python3 scripts/inspect_pptx.py sample.pptx --json inspection.json
    python3 scripts/inspect_pptx.py --compare template.pptx draft.pptx

Shape order is XML order, not guaranteed visual reading order. No rendering, OCR,
chart-data extraction or complete privacy audit is performed. Output may contain
private text and paths; keep it outside the distributable skill.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "assets"))
from create_pptx import A, P, paragraphs, parse_xml, read_package, relationships, slides


def declaration(element):
    """Keep namespace-qualified design declarations without sample text."""
    return {"tag": element.tag, "attributes": dict(element.attrib),
            "text": "" if element.tag == "{%s}t" % A else (element.text or "").strip(),
            "children": [declaration(child) for child in element]}


def design_sources(parts, name):
    """Follow inheritance links; declarations are not a resolved rendering style."""
    found, pending = [], [name]
    while pending:
        current = pending.pop(0)
        if current in found:
            continue
        if current not in parts:
            raise ValueError("Unreadable design relationship: " + current)
        found.append(current)
        pending.extend(target for target, kind, mode in relationships(parts, current).values()
                       if mode != "External" and kind.rsplit("/", 1)[-1] in
                       ("slideLayout", "slideMaster", "theme", "themeOverride", "notesMaster"))
    return found


def design_declarations(data):
    root = parse_xml(data)
    groups = {
        "backgrounds": (P, ("bg",)),
        "colour_maps": (P, ("clrMap", "clrMapOvr")),
        "theme_schemes": (A, ("clrScheme", "fontScheme", "fmtScheme")),
        "fonts": (A, ("latin", "ea", "cs", "sym", "font", "buFont")),
        "fills_and_outlines": (A, ("noFill", "solidFill", "gradFill", "blipFill", "pattFill", "grpFill", "ln")),
        "text_formatting": (A, ("rPr", "defRPr", "endParaRPr", "pPr", "bodyPr", "lstStyle")),
        "master_text_styles": (P, ("txStyles",)),
        "style_references": (P, ("style",)),
    }
    return {group: [declaration(el) for el in root.iter() if el.tag in
                    {"{%s}%s" % (namespace, tag) for tag in tags}]
            for group, (namespace, tags) in groups.items()}


def design_signatures(path):
    """Compare template structure with slide text ignored, retaining media/fonts."""
    parts = read_package(path)
    slides(parts)
    prefixes = ("ppt/slides/", "ppt/slideLayouts/", "ppt/slideMasters/", "ppt/notesSlides/",
                "ppt/notesMasters/", "ppt/theme/", "ppt/media/", "ppt/fonts/")
    selected = {name for name in parts if name.startswith(prefixes) or name in
                ("ppt/presentation.xml", "ppt/_rels/presentation.xml.rels", "ppt/tableStyles.xml")}
    result = {}
    for name in selected:
        data = parts[name]
        if name.endswith((".xml", ".rels")):
            data = json.dumps(declaration(parse_xml(data)), sort_keys=True, ensure_ascii=False).encode("utf-8")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def compare_design(a, b):
    before, after = design_signatures(a), design_signatures(b)
    changed = sorted(name for name in set(before) | set(after) if before.get(name) != after.get(name))
    print("Design/structure differences: " + (", ".join(changed) if changed else "none"))
    print("Checks template structure with DrawingML text ignored, including backgrounds, themes, "
          "fonts, layouts, formatting, geometry, relationships and retained media/font bytes. "
          "This does not establish identical rendered slides or available fonts. "
          "Intentional slide, link or media edits can produce differences; review them.")
    return 1 if changed else 0


def inspect(path):
    parts = read_package(path)
    presentation = parse_xml(parts["ppt/presentation.xml"])
    size = presentation.find("{%s}sldSz" % P)
    result = {"slide_size_emu": dict(size.attrib) if size is not None else None,
              "slides": [], "style_sources": {}, "review_parts": [], "external_relationships": []}
    for number, name in enumerate(slides(parts), 1):
        root = parse_xml(parts[name])
        rels = relationships(parts, name)
        notes = [target for target, kind, mode in rels.values() if kind.endswith("/notesSlide") and mode != "External"]
        if any(n not in parts for n in notes):
            raise ValueError("Unreadable notes relationship for " + name)
        shapes = []
        for shape in root.iter():
            if shape.tag not in ("{%s}sp" % P, "{%s}graphicFrame" % P, "{%s}pic" % P):
                continue
            properties = shape.find(".//{%s}cNvPr" % P)
            shapes.append({"type": shape.tag.split("}")[-1],
                           "properties": dict(properties.attrib) if properties is not None else {},
                           "geometry": [{"type": e.tag.split("}")[-1], **e.attrib} for e in shape.iter()
                                        if e.tag in ("{%s}off" % A, "{%s}ext" % A, "{%s}xfrm" % A)],
                           "text": ["".join(e.text or "" for e in para.iter("{%s}t" % A))
                                    for para in shape.iter("{%s}p" % A)]})
        sources = design_sources(parts, name)
        for source in sources:
            if source not in result["style_sources"]:
                result["style_sources"][source] = design_declarations(parts[source])
        result["slides"].append({"number": number, "part": name,
            "hidden": root.get("show", "1") in ("0", "false"),
            "text": paragraphs(parts[name]), "shapes": shapes,
            "design_sources": sources,
            "layout": [t for t, k, m in rels.values() if k.endswith("/slideLayout") and m != "External"],
            "notes": {n: paragraphs(parts[n]) for n in notes}})
    for name in sorted(parts):
        if name.startswith(("docProps/", "ppt/notes", "ppt/comments", "ppt/commentAuthors",
                            "ppt/media/", "ppt/embeddings/", "ppt/charts/", "ppt/slideMasters/",
                            "ppt/slideLayouts/", "ppt/theme/", "ppt/fonts/", "customXml/")):
            result["review_parts"].append({"part": name, "bytes": len(parts[name])})
        if name.endswith(".rels"):
            for rel in parse_xml(parts[name]):
                if rel.get("TargetMode") == "External":
                    result["external_relationships"].append({"part": name, **rel.attrib})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("sample", nargs="?")
    parser.add_argument("--compare", nargs=2, metavar=("TEMPLATE", "OUTPUT"))
    parser.add_argument("--text", action="store_true")
    parser.add_argument("--include-notes", action="store_true")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.compare:
        return compare_design(*args.compare)
    if not args.sample:
        parser.error("provide a sample or --compare TEMPLATE OUTPUT")
    result = inspect(args.sample)
    if args.json:
        args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.text:
        for slide in result["slides"]:
            print("--- SLIDE %s%s (%s)" % (slide["number"], " [hidden]" if slide["hidden"] else "", slide["part"]))
            print("\n".join(slide["text"]))
            if args.include_notes:
                for name, text in slide["notes"].items():
                    print("--- NOTES (%s)\n%s" % (name, "\n".join(text)))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
