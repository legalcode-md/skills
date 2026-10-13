#!/usr/bin/env python3
"""Fill named text blanks in template.pptx, retaining untouched package parts.

    python3 create_pptx.py --list
    python3 create_pptx.py --text
    python3 create_pptx.py values.json draft.pptx
    python3 create_pptx.py --template sample.pptx --replace edits.json template.pptx

Blanks are [Name] or [Name: guidance]. Values are single-line strings or numbers.
Split-run blanks are supported; inserted text inherits the first affected run.
Source backgrounds, colours, fonts, themes, masters, layouts and media are retained;
the helper edits text-node contents without reconstructing the slide design.
Missing blanks remain visible and are reported. Choices, repeated slides, rich
text, multiline values, chart data and media replacement need a presentation tool.
--replace accepts an exact old-text -> new-text JSON object for template preparation;
it does not sanitise metadata, notes, hidden slides, media or embedded files.
Existing output is protected unless --force is used; the source is never replaced.
Python 3.9+, standard library only. No network access or renderer required.
"""
import argparse
import json
import os
import posixpath
import re
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from xml.parsers import expat
from xml.sax.saxutils import escape

A = "http://schemas.openxmlformats.org/drawingml/2006/main"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
TEXT_PARTS = re.compile(r"ppt/(?:slides/slide|notesSlides/notesSlide|slideLayouts/slideLayout|slideMasters/slideMaster|notesMasters/notesMaster)\d+\.xml$")
BLANK = re.compile(r"\[(?!\d+\]|[^\W\d_]{1,2}\d{1,3}\])[^\[\]\n]{1,700}\]")


def read_package(path):
    parts, total = {}, 0
    with zipfile.ZipFile(path) as archive:
        for info in archive.infolist():
            total += info.file_size
            if info.file_size > 50 * 1024**2 or total > 300 * 1024**2:
                raise ValueError("Package exceeds helper size limits; use a presentation tool.")
            if info.filename in parts:
                raise ValueError("Duplicate package part: " + info.filename)
            parts[info.filename] = archive.read(info)
    return parts


def parse_xml(data):
    # OOXML has no DTD. Use parser callbacks so UTF-16 cannot bypass this check.
    parser = expat.ParserCreate()
    def reject(*args):
        raise ValueError("DTD/entity declarations are unsupported.")
    parser.StartDoctypeDeclHandler = reject
    parser.EntityDeclHandler = reject
    parser.Parse(data, True)
    return ET.fromstring(data)


def relationships(parts, name):
    rel_name = posixpath.join(posixpath.dirname(name), "_rels", posixpath.basename(name) + ".rels")
    root = parse_xml(parts[rel_name]) if rel_name in parts else []
    return {el.get("Id"): (posixpath.normpath(posixpath.join(posixpath.dirname(name), el.get("Target", "")))
                             if not el.get("Target", "").startswith("/") else el.get("Target").lstrip("/"),
                             el.get("Type", ""), el.get("TargetMode")) for el in root}


def slides(parts):
    root = parse_xml(parts["ppt/presentation.xml"])
    rels = relationships(parts, "ppt/presentation.xml")
    result = []
    for el in root.findall("{%s}sldIdLst/{%s}sldId" % (P, P)):
        target, kind, mode = rels[el.get("{%s}id" % R)]
        if mode == "External" or not kind.endswith("/slide") or target not in parts:
            raise ValueError("Unreadable slide relationship: " + target)
        result.append(target)
    return result


def paragraphs(data):
    root = parse_xml(data)
    return ["".join((el.text or "") if el.tag == "{%s}t" % A else "\n"
                    for el in para.iter() if el.tag in ("{%s}t" % A, "{%s}br" % A))
            for para in root.iter("{%s}p" % A)]


def replace_text(data, replacements):
    """Patch only text-node contents, preserving namespace declarations and other bytes."""
    parse_xml(data)
    encoding = re.search(br"encoding\s*=\s*['\"]([^'\"]+)", data[:150], re.I)
    if b"\x00" in data[:150] or (encoding and encoding.group(1).lower() != b"utf-8"):
        raise ValueError("Text editing requires UTF-8 XML; re-save in a presentation editor.")
    parser = expat.ParserCreate(namespace_separator="}")
    current, node, patches = None, None, []
    pattern = re.compile("|".join(re.escape(k) for k in sorted(replacements, key=len, reverse=True))) if replacements else None
    counts = {key: 0 for key in replacements}

    def start(name, attrs):
        nonlocal current, node
        if name == A + "}p":
            current = []
        elif current is not None and name == A + "}br":
            current.append([None, None, "\n"])
        elif current is not None and name == A + "}t":
            at = parser.CurrentByteIndex
            stop = data.index(b">", at) + 1
            node = None if data[at:stop].rstrip().endswith(b"/>") else [stop, None, ""]

    def chars(value):
        if node is not None:
            node[2] += value

    def end(name):
        nonlocal current, node
        if name == A + "}t" and node is not None:
            node[1] = parser.CurrentByteIndex
            current.append(node)
            node = None
        elif name == A + "}p" and current is not None:
            joined = "".join(n[2] for n in current)
            offsets, offset = [], 0
            for n in current:
                offsets.append(offset)
                offset += len(n[2])
            updated = [n[2] for n in current]
            for match in reversed(list(pattern.finditer(joined)) if pattern else []):
                counts[match.group()] += 1
                first = True
                for i, n in enumerate(current):
                    left, right = offsets[i], offsets[i] + len(n[2])
                    if n[0] is None or right <= match.start() or left >= match.end():
                        continue
                    updated[i] = (updated[i][:max(0, match.start() - left)]
                                  + (replacements[match.group()] if first else "")
                                  + updated[i][min(len(n[2]), match.end() - left):])
                    first = False
            for n, value in zip(current, updated):
                if n[0] is not None and value != n[2]:
                    patches.append((n[0], n[1], escape(value).encode("utf-8")))
            current = None

    parser.StartElementHandler, parser.EndElementHandler = start, end
    parser.CharacterDataHandler = chars
    parser.Parse(data, True)
    for left, right, replacement in sorted(patches, reverse=True):
        data = data[:left] + replacement + data[right:]
    parse_xml(data)  # Reject invalid control characters before publishing any output.
    return data, counts


def write_package(parts, destination, force=False):
    fd, temporary = tempfile.mkstemp(prefix=".pptx-", dir=os.path.dirname(os.path.abspath(destination)))
    os.close(fd)
    try:
        with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED) as archive:
            for name, data in parts.items():
                archive.writestr(name, data)
        if force:
            os.replace(temporary, destination)
        else:
            os.link(temporary, destination)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--template", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "template.pptx"))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--list", action="store_true")
    mode.add_argument("--text", action="store_true")
    mode.add_argument("--replace", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("values", nargs="?")
    parser.add_argument("output", nargs="?")
    args = parser.parse_args()
    try:
        parts = read_package(args.template)
        slides(parts)  # Require a readable presentation, not an arbitrary ZIP.
        names = sorted(n for n in parts if TEXT_PARTS.fullmatch(n))
        texts = {n: "\n".join(paragraphs(parts[n])) for n in names}
        blanks = sorted({b for text in texts.values() for b in BLANK.findall(text)})
        if args.list:
            print("\n".join(blanks) or "No text blanks.")
            return 0
        if args.text:
            for name, text in texts.items():
                print("--- %s\n%s" % (name, text))
            return 0
        if not args.values or not args.output:
            parser.error("provide values.json and output.pptx")
        if os.path.realpath(args.template) == os.path.realpath(args.output) or (os.path.exists(args.output) and os.path.samefile(args.template, args.output)):
            raise ValueError("The source/template cannot be overwritten.")
        with open(args.values, encoding="utf-8") as source:
            values = json.load(source)
        if not isinstance(values, dict) or any(not isinstance(k, str) or not k for k in values):
            raise ValueError("Values must be an object with nonempty string keys.")
        replacements = {}
        for key, value in values.items():
            if isinstance(value, (bool, list, dict)) or value is None or any(c in str(value) for c in "\r\n\t"):
                raise ValueError("Use single-line text or numbers; unsupported value for " + key)
        if args.replace:
            if any(any(c in key for c in "\r\n\t") for key in values):
                raise ValueError("Replacement anchors must be single-line text.")
            replacements = {key: str(value) for key, value in values.items()}
        else:
            replacements = {b: str(values[b[1:-1].split(":", 1)[0].strip()]) for b in blanks
                            if b[1:-1].split(":", 1)[0].strip() in values}
        counts = {key: 0 for key in replacements}
        for name in names:
            parts[name], found = replace_text(parts[name], replacements)
            for key, count in found.items():
                counts[key] += count
        if args.replace and any(count == 0 for count in counts.values()):
            raise ValueError("Replacement text not found: " + ", ".join(k for k, v in counts.items() if not v))
        write_package(parts, args.output, args.force)
        remaining = sorted({b for n in names for text in paragraphs(parts[n]) for b in BLANK.findall(text)})
        print("Created " + args.output)
        if remaining:
            print("Unresolved blanks: " + ", ".join(remaining))
        return 0
    except (OSError, ValueError, KeyError, zipfile.BadZipFile, ET.ParseError, expat.ExpatError) as error:
        print(str(error))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
