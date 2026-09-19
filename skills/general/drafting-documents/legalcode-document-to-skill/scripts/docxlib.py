"""Shared OOXML helpers for the document-to-skill scripts.

Standard library only, Python 3.9+. A .docx is a zip of XML parts; these helpers
read the parts directly so nothing has to be installed on the lawyer's machine.
"""
import os
import re
import shutil
import subprocess
import zipfile
import xml.etree.ElementTree as ET
from xml.parsers import expat

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
MC = "http://schemas.openxmlformats.org/markup-compatibility/2006"
PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"


def q(tag):
    return "{%s}%s" % (W, tag)


def wval(el, child, attr="val", default=None):
    """Value of <w:child w:attr="..."/> under el, or default."""
    if el is None:
        return default
    c = el.find(q(child))
    if c is None:
        return default
    return c.get(q(attr), default)


def onoff(el, child):
    """Tri-state toggle: True / False when the element is present, None when absent."""
    if el is None:
        return None
    c = el.find(q(child))
    if c is None:
        return None
    return c.get(q("val"), "true") not in ("0", "false", "off")


MAX_PART, MAX_TOTAL = 50 * 1024 * 1024, 300 * 1024 * 1024


def read_zip(path):
    """Parts of a docx as {name: bytes}. Oversized or absurdly compressed members are skipped:
    samples can come from a counterparty and a small file can be built to exhaust memory."""
    out, total = {}, 0
    with zipfile.ZipFile(path) as z:
        for info in z.infolist():
            ratio = info.file_size / float(info.compress_size or 1)
            if info.file_size > MAX_PART or (info.file_size > 1024 * 1024 and ratio > 200):
                continue
            total += info.file_size
            if total > MAX_TOTAL:
                break
            out[info.filename] = z.read(info)
    return out


def safe_xml(data):
    """False for XML that declares a DTD or entities. OOXML never does; entity expansion is an attack."""
    return not re.search(br"<!(DOCTYPE|ENTITY)", data[:4096] if len(data) > 4096 else data) and b"<!ENTITY" not in data


STRICT = ((b"http://purl.oclc.org/ooxml/wordprocessingml/main", W.encode()),
          (b"http://purl.oclc.org/ooxml/officeDocument/relationships", R.encode()))


def main_part(parts):
    """Name of the main document part. Usually word/document.xml; some tools write word/document2.xml."""
    m = re.search(rb"<Relationship\b[^>]*officeDocument[\"'][^>]*>", parts.get("_rels/.rels", b""))
    t = re.search(rb"Target=[\"']/?([^\"']+)", m.group(0)) if m else None
    name = t.group(1).decode() if t else "word/document.xml"
    return name if name in parts else "word/document.xml"


def parse(parts, name):
    data = parts.get(name)
    if not data or not safe_xml(data):
        return None
    for strict, transitional in STRICT:      # "Strict Open XML" differs from ordinary .docx only in these names
        data = data.replace(strict, transitional)
    try:
        return ET.fromstring(data)
    except ET.ParseError:
        return None


def rels(parts, name):
    """{rId: target} for a part's relationships file."""
    root = parse(parts, name)
    out = {}
    if root is not None:
        for r in root:
            out[r.get("Id")] = (r.get("Target"), r.get("Type", ""))
    return out


def iter_paragraphs(el):
    """Every w:p under el in reading order, including table cells and text boxes.

    mc:Fallback is skipped: Word stores text boxes twice (Choice and Fallback) and
    reading both would double every paragraph inside them.
    """
    for child in el:
        if child.tag == "{%s}Fallback" % MC:
            continue
        if child.tag == q("p"):
            yield child
        for p in iter_paragraphs(child):
            yield p


def is_hidden(run):
    """A run formatted as hidden text. The lawyer cannot see it on the page, so it is never house text."""
    rpr = run.find(q("rPr"))
    return rpr is not None and onoff(rpr, "vanish") is True


def hidden_style_parts(parts):
    """Conservatively flag hidden style/default declarations, including unused styles.

    Resolving Word's inherited/toggle properties needs more than direct-run inspection.
    Callers must not claim sanitisation when these declarations are present.
    """
    found = []
    for name in ("word/styles.xml", "word/stylesWithEffects.xml"):
        root = parse(parts, name)
        if root is not None and any(
                el.get(q("val"), "true").strip() not in ("0", "false", "off")
                for el in root.iter(q("vanish"))):
            found.append(name)
    return found


def strip_hidden_runs(xml):
    """Remove directly hidden runs by XML identity while retaining other original bytes.

    Expat supplies byte offsets; using those avoids reserialising Word's namespaces.
    Attribute quote style, attribute order and namespace prefixes do not affect detection.
    This deliberately does not resolve inherited styles; check hidden_style_parts first.
    """
    data = xml.encode("utf-8")
    parser = expat.ParserCreate(namespace_separator="}")
    word_namespaces = (W, "http://purl.oclc.org/ooxml/wordprocessingml/main")
    run_names = {ns + "}r" for ns in word_namespaces}
    property_names = {ns + "}rPr" for ns in word_namespaces}
    hidden_names = {ns + "}vanish" for ns in word_namespaces}
    stack, spans = [], []

    def start(name, attrs):
        if (name in hidden_names and len(stack) >= 2
                and stack[-1]["name"] in property_names
                and stack[-2]["name"] in run_names):
            value = attrs.get(name.rsplit("}", 1)[0] + "}val", "true").strip()
            if value not in ("0", "false", "off"):
                stack[-2]["hidden"] = True
        stack.append({"name": name, "start": parser.CurrentByteIndex, "hidden": False})

    def end(name):
        item = stack.pop()
        if name in run_names and item["hidden"]:
            # A run containing vanish cannot be self-closing. The callback points
            # at its closing tag, including for non-ASCII text earlier in the part.
            stop = data.index(b">", parser.CurrentByteIndex) + 1
            spans.append((item["start"], stop))

    parser.StartElementHandler, parser.EndElementHandler = start, end
    parser.Parse(data, True)
    outer = []
    for begin, stop in sorted(spans, key=lambda span: (span[0], -span[1])):
        if not outer or begin >= outer[-1][1]:
            outer.append((begin, stop))
    for begin, stop in reversed(outer):
        data = data[:begin] + data[stop:]
    return data.decode("utf-8"), len(outer)


def para_text(p):
    """Visible text of one paragraph. Hidden runs, tracked deletions and nested paragraphs are left out."""
    out = []

    def walk(el):
        for child in el:
            t = child.tag
            if t == q("r") and is_hidden(child):
                continue
            if t == q("t"):
                out.append(child.text or "")
            elif t == q("tab"):
                out.append("\t")
            elif t in (q("br"), q("cr")):
                out.append("\n")
            elif t == q("noBreakHyphen"):
                out.append("-")
            elif t in (q("p"), q("del"), q("moveFrom"), "{%s}Fallback" % MC):
                continue
            else:
                walk(child)

    walk(p)
    return "".join(out)


def marked_text(p):
    """A paragraph's text with **bold**, *italic* and __underlined__ runs marked, so set phrases show as set."""
    out, prev = [], None
    for r in p.iter(q("r")):
        if is_hidden(r):
            continue
        holder = ET.Element(q("p"))
        holder.append(r)
        text = para_text(holder)
        if not text:
            continue
        rpr = r.find(q("rPr"))
        u = rpr.find(q("u")) if rpr is not None else None
        mark = ("**" if onoff(rpr, "b") else "*" if onoff(rpr, "i") else
                "__" if u is not None and u.get(q("val")) not in (None, "none") else "") if text.strip() else prev
        if mark != prev:
            out.append((prev or "") + (mark or ""))
            prev = mark
        out.append(text)
    out.append(prev or "")
    return "".join(out)


def docx_paragraphs(path):
    """Non-empty paragraph texts of a docx body, in reading order."""
    parts = read_zip(path)
    root = parse(parts, main_part(parts))
    if root is None:
        raise ValueError("%s has no readable word/document.xml" % path)
    body = root.find(q("body"))
    out = []
    for p in iter_paragraphs(body if body is not None else root):
        t = re.sub(r"[ \t ]+", " ", para_text(p)).strip()
        if t:
            out.append(t)
    return out


def text_paragraphs(raw):
    """Split plain text into paragraphs: on blank lines when there are any, else per line."""
    raw = raw.replace("\r\n", "\n").replace("\r", "\n")
    blocks = re.split(r"\n\s*\n", raw) if re.search(r"\n\s*\n", raw) else raw.split("\n")
    out = []
    for b in blocks:
        t = re.sub(r"\s+", " ", b).strip()
        if t:
            out.append(t)
    return out


def load_paragraphs(path):
    """Paragraphs of a .docx, .txt, .md or (when pdftotext is installed) .pdf."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".docx":
        return docx_paragraphs(path)
    if ext in (".txt", ".md", ".markdown", ".text"):
        with open(path, encoding="utf-8", errors="replace") as f:
            return text_paragraphs(f.read())
    if ext == ".pdf":
        exe = shutil.which("pdftotext")
        if not exe:
            raise ValueError(
                "%s: no pdftotext on this machine. Extract the PDF's text with whatever PDF "
                "tool you have, save it as .txt, and pass that instead." % path)
        txt = subprocess.run([exe, "-enc", "UTF-8", path, "-"], capture_output=True).stdout
        return text_paragraphs(txt.decode("utf-8", "replace"))
    raise ValueError("%s: unsupported type. Pass .docx, .txt, .md or .pdf; re-save .doc as .docx first." % path)


SENTENCE_END = re.compile(r"[.!?][\"”“’)\]]*\s+")


def split_sentences(line):
    """Split after . ! ? (any closing quote or bracket stays with its sentence) when a capital letter or an
    opening quote or bracket follows. A digit does not start a sentence: 'nr. 90/2018', 'Art. 28',
    '2. mgr. 5. gr.' and 'kr. 500' must stay whole."""
    out, start = [], 0
    for m in SENTENCE_END.finditer(line):
        nxt = line[m.end():m.end() + 1]
        if nxt.isupper() or nxt in "\"“„«([":
            out.append(line[start:m.end()])
            start = m.end()
    out.append(line[start:])
    return out


def reflow(raw):
    """Undo hard line wraps in text extracted from a PDF: a short line ends a block, a full one continues."""
    lines = raw.replace("\r\n", "\n").replace("\r", "\n").replace("\f", "\n\n").split("\n")
    lengths = sorted(len(ln.strip()) for ln in lines if ln.strip())
    full = lengths[int(len(lengths) * 0.9)] if lengths else 0
    blocks, buf = [], []
    for ln in lines:
        t = ln.strip()
        if not t:
            if buf:
                blocks.append(" ".join(buf))
                buf = []
            continue
        buf.append(t)
        if len(t) < 0.7 * full:
            blocks.append(" ".join(buf))
            buf = []
    if buf:
        blocks.append(" ".join(buf))
    return blocks


def sentences(blocks):
    """Blocks split into sentences and lines. Abbreviations cause some false splits; they fall in the
    same place in every sample, so alignment survives them."""
    out = []
    for b in blocks:
        for line in b.split("\n"):
            for sent in split_sentences(line):
                t = re.sub(r"\s+", " ", sent or "").strip()
                if t:
                    out.append(t)
    return out


def load_units(path, unit="paragraph"):
    """Text of a sample as paragraphs or sentences. Sentences survive differences in how formats
    break paragraphs, so they are the safer unit when a PDF or mixed formats are involved."""
    ext = os.path.splitext(path)[1].lower()
    if unit == "paragraph":
        return load_paragraphs(path)
    if ext == ".pdf":
        exe = shutil.which("pdftotext")
        if not exe:
            return sentences(load_paragraphs(path))   # raises the explanatory error
        txt = subprocess.run([exe, "-enc", "UTF-8", path, "-"], capture_output=True).stdout
        return sentences(reflow(txt.decode("utf-8", "replace")))
    if ext == ".docx":
        parts = read_zip(path)
        root = parse(parts, main_part(parts))
        if root is None:
            raise ValueError("%s has no readable word/document.xml" % path)
        body = root.find(q("body"))
        return sentences([para_text(p) for p in iter_paragraphs(body if body is not None else root)])
    return sentences(load_paragraphs(path))


def all_text(parts):
    """Every piece of text a Word file holds, for harvesting identifiers: body, headers, footers, notes,
    comments, and tracked deletions, which still sit in the file after the page stops showing them."""
    out = []
    for name in sorted(parts):
        if re.match(r"word/(document|header\d*|footer\d*|footnotes|endnotes|comments)\.xml$", name):
            xml = parts[name].decode("utf-8", "replace")
            xml = re.sub(r"</w:p>|<w:br\s*/>|<w:tab\s*/>", "\n", xml)
            out.append(re.sub(r"<[^>]+>", "", xml))
    import html as _html
    return _html.unescape("\n".join(out))


def dump_text(path):
    """A Word file as readable text: header, body in reading order with style names, footer, notes."""
    parts = read_zip(path)
    styles = parse(parts, "word/styles.xml")
    names = {}
    if styles is not None:
        for st in styles.findall(q("style")):
            names[st.get(q("styleId"))] = wval(st, "name") or st.get(q("styleId"))
    lines = []
    for label, pattern in (("HEADER", r"word/header\d*\.xml$"), ("BODY", r"word/document\.xml$"),
                           ("FOOTER", r"word/footer\d*\.xml$"), ("NOTES", r"word/(footnotes|endnotes)\.xml$")):
        for name in sorted(n for n in parts if re.match(pattern, n)):
            root = parse(parts, name)
            if root is None:
                continue
            block = []
            for p in iter_paragraphs(root):
                t = marked_text(p).strip()
                style = names.get(wval(p.find(q("pPr")), "pStyle"), "")
                if t:
                    block.append("%s| %s" % (("[%s] " % style) if style and label == "BODY" else "", t.replace("\n", " / ")))
                elif label == "BODY":
                    block.append("| (empty paragraph)")
            if block:
                lines += ["--- %s (%s)" % (label, name)] + block
    return "\n".join(lines)


def core_metadata(parts):
    """Author-type metadata that must not travel with a reusable asset."""
    out = {}
    core = parse(parts, "docProps/core.xml")
    if core is not None:
        for el in core:
            name = el.tag.split("}")[-1]
            if name in ("creator", "lastModifiedBy", "title", "subject", "keywords",
                        "description", "category") and (el.text or "").strip():
                out[name] = el.text.strip()
    app = parse(parts, "docProps/app.xml")
    if app is not None:
        for el in app:
            name = el.tag.split("}")[-1]
            if name in ("Company", "Manager", "Template") and (el.text or "").strip() not in ("", "Normal.dotm", "Normal"):
                out[name] = el.text.strip()
    if "docProps/custom.xml" in parts:
        out["customProperties"] = "present (often document-management ids)"
    return out
