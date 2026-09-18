#!/usr/bin/env python3
"""Turn one sample Word document into a clean template.

Usage:  python3 make_template.py <sample.docx> <template.docx> --edits edits.json [--force]

The template keeps the sample's wording, styles, numbering, page setup, header and footer.
edits.json says what to change (every key is optional):

    {"replace":           {"Borealis Seafood ehf.": "[Client name]", "4 March 2024": "[Date]"},
     "replace_paragraph": [{"containing": "You have asked us to", "with": "[Scope of work: what the client asked for and what we will do]"}],
     "insert_after":      [{"after": "We record time in units", "text": "[IF fixed fee] We will carry out the work for a fixed fee of [Fee]."}],
     "delete_paragraph":  ["We also act for"]}

  replace            swaps a string wherever it occurs (body, tables, header, footer, notes),
                     longest first, even where Word has split it across formatting runs
  replace_paragraph  replaces the whole paragraph that contains the text; the new text takes the
                     paragraph's formatting and its first run's, so mark what must stay
                     **bold**, *italic* or __underlined__ in the text you write
  insert_after       adds a paragraph, formatted like the one it follows ("insert_before" with
                     "before" does the same in front of a paragraph; "at": "start" puts it first
                     in the document). "like": "text of another paragraph" copies that
                     paragraph's formatting instead, which is how a heading and the text under
                     it are added where the sample has none. With "instruction": true
                     the paragraph is set in grey italics and must start with [NOTE], [ATH],
                     [LEIÐBEINING], [HINWEIS], [OBS], [BEMÆRK], [HUOM], [NOTA] or [REMARQUE]:
                     advice for whoever opens the template, left out of every created document
  delete_paragraph   removes the paragraph that contains the text

Order: delete_paragraph, replace_paragraph, insert_after and insert_before, then replace.
"containing", "after", "before" and "like" match the first paragraph that contains the text,
case-sensitively, as the document stands at that point, so an insert may anchor on text an
earlier edit wrote. Text an edit writes is final: replace works only on the sample's own
text and never reaches into a paragraph you replaced or inserted. A blank with its note
may run to 700 characters.

Conventions create_docx.py understands, all written in the language of the document:
[Name] is a blank; [Name: what goes here, how much, what to leave out] is a blank that carries
its own note, which is how a section of free text should be left; a paragraph that starts
with a choice marker in capitals ([IF ...], [EF ...], [HVIS ...], [OM ...], [WENN ...],
[FALLS ...], [SI ...], [SE ...], [JOS ...], [ALS ...]) is kept only when that choice is on,
and the same marker at the start of a line inside a paragraph switches that line alone.

Cleanup covers supported tracked changes (insertions accepted, deletions
dropped), comments, directly hidden runs, author and revision metadata, custom properties, custom
XML, document variables, the attached-template path, the thumbnail, embedded objects,
picture descriptions, hyperlink tooltips, content-control labels, bookmark names, mailto and
other non-web links, fields that fetch remote content or read document properties, and
original media file names. Footnotes stay, because they are part of the page.
Hidden style/default declarations cause a refusal, even in unused styles: this helper does
not resolve inherited visibility. Review retained XML, attributes, links and media as well
as the printed text; cleanup is not a guarantee that all matter data has been removed.
The finished template is printed as text at the end: read it.

Standard library only, Python 3.9+. The XML is edited as text and never re-serialised,
because a round trip through an XML library drops namespace declarations Word needs.
"""
import bisect
import datetime
import json
import os
import posixpath
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape, unescape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docxlib import read_zip, safe_xml, dump_text, hidden_style_parts, strip_hidden_runs  # noqa: E402

IMPLICIT = {"officeDocument", "core-properties", "extended-properties", "styles", "numbering", "settings",
            "theme", "fontTable", "webSettings", "footnotes", "endnotes", "stylesWithEffects"}
TEXT_PARTS = re.compile(r"word/(document|header\d*|footer\d*|footnotes|endnotes)\.xml$")
T_OR_PEND = re.compile(r"(<w:t(?:\s[^>]*)?>)([^<]*)(</w:t>)|(</w:p>)")
PARA = re.compile(r"<w:p(?:\s[^>]*)?>(?:(?!</w:p>|<w:p[ >]).)*</w:p>", re.S)
REL = re.compile(r"<Relationship\b[^>]*?(?:/>|>\s*</Relationship\s*>)", re.S)
OVERRIDE = re.compile(r"<Override\b[^>]*?(?:/>|>\s*</Override\s*>)", re.S)


def attr(tag, name):
    """Value of an attribute in a start tag, whichever quotes the writer used."""
    m = re.search(r"\b%s\s*=\s*(?:\"([^\"]*)\"|'([^']*)')" % name, tag)
    return None if m is None else (m.group(1) if m.group(1) is not None else m.group(2))


APP_XML = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Properties xmlns="http://schemas.openxmlformats'
           '.org/officeDocument/2006/extended-properties"><Application>Microsoft Office Word</Application></Properties>')


def para_plain(xml):
    text = re.sub(r"<w:tab\s*/>|<w:br\s*/>", " ", xml)
    text = "".join(unescape(t) for t in re.findall(r"<w:t(?:\s[^>]*)?>([^<]*)</w:t>", text))
    return re.sub(r"\s+", " ", text).strip()


INLINE = re.compile(r"(\*\*[^*\n]+\*\*|__[^_\n]+__|(?<!\\)\*[^*\n]+(?<!\\)\*)")
AFTER_U = ("<w:effect", "<w:bdr", "<w:shd", "<w:fitText", "<w:vertAlign", "<w:rtl", "<w:cs", "<w:em ", "<w:lang",
           "<w:eastAsianLayout", "<w:specVanish", "<w:oMath")
NEW = ' new="1"'       # marks text written by an edit; removed again before the file is saved


def with_format(rpr, kind):
    tag = {"b": "<w:b/>", "i": "<w:i/>", "u": '<w:u w:val="single"/>'}[kind]
    if not rpr:
        return "<w:rPr>%s</w:rPr>" % tag
    if re.search(r"<w:%s[ />]" % kind, rpr):
        return rpr
    if kind == "u":
        spots = [rpr.find(t) for t in AFTER_U if rpr.find(t) >= 0]
        at = min(spots) if spots else rpr.rindex("</w:rPr>")
    else:
        head = re.match(r"<w:rPr>(?:\s*<w:(?:rStyle|rFonts)\b[^>]*/>)*(?:\s*<w:b\b[^>]*/>)?(?:\s*<w:bCs\b[^>]*/>)?", rpr)
        at = head.end() if head else len("<w:rPr>")
    return rpr[:at] + tag + rpr[at:]


def run_xml(text, rpr):
    """Runs for text an edit writes: line breaks kept, **bold**, *italic* and __underline__ honoured."""
    out = []
    for seg in INLINE.split(text):
        if not seg:
            continue
        kind = "b" if seg.startswith("**") else "u" if seg.startswith("__") else "i" if seg.startswith("*") else None
        if kind and len(seg) > (4 if kind in "bu" else 2):
            seg, r = (seg[2:-2] if kind in "bu" else seg[1:-1]), with_format(rpr, kind)
        else:
            r = rpr
        inner = "<w:br/>".join('<w:t xml:space="preserve"%s>%s</w:t>' % (NEW, escape(line.replace("\\*", "*")))
                               for line in seg.split("\n"))
        out.append("<w:r>%s%s</w:r>" % (r, inner))
    return "".join(out)


def pieces(para):
    ppr = re.search(r"<w:pPr>.*?</w:pPr>", para, re.S)
    rest = para[ppr.end():] if ppr else para
    rpr = re.search(r"<w:rPr>.*?</w:rPr>", rest, re.S)
    return (ppr.group(0) if ppr else ""), (rpr.group(0) if rpr else "")


INSTRUCTION_PPR = '<w:pPr><w:spacing w:before="60" w:after="120"/><w:jc w:val="left"/></w:pPr>'


def instruction_rpr(rpr):
    """The anchor's font and size, in grey italics: an instruction should not pass for the document's own text."""
    fonts = re.search(r"<w:rFonts\b[^>]*/>", rpr or "")
    size = re.search(r"<w:sz\b[^>]*/>", rpr or "")
    return "<w:rPr>%s<w:i/><w:color w:val=\"7F7F7F\"/>%s</w:rPr>" % (fonts.group(0) if fonts else "",
                                                                     size.group(0) if size else "")


def find_para(xml, needle):
    want = re.sub(r"\s+", " ", needle).strip()
    for m in PARA.finditer(xml):
        if want and want in para_plain(m.group(0)):
            return m
    return None


def replace_text(xml, old, new):
    """Replace every occurrence of a string in w:t text, even where Word has split it across runs; the new
    text lands in the first run it touched. One pass: the text is laid out once, every hit is found in it,
    and hits are applied last to first so that earlier offsets stay true."""
    if not old:
        return xml, 0
    nodes, virtual, pos = [], [], 0                     # [match, start, current text]
    for m in T_OR_PEND.finditer(xml):
        if m.group(4):
            virtual.append("\n")
            pos += 1
        elif NEW in m.group(1):
            virtual.append("\n")           # text an edit wrote is final: replace never reaches into it
            pos += 1
        else:
            t = unescape(m.group(2))
            nodes.append([m, pos, t])
            virtual.append(t)
            pos += len(t)
    joined = "".join(virtual)
    hits, at = [], joined.find(old)
    while at >= 0:
        hits.append(at)
        at = joined.find(old, at + len(old))
    ends = [n[1] + len(n[2]) for n in nodes]
    changed = set()
    for hit in reversed(hits):
        end, k, first = hit + len(old), bisect.bisect_right(ends, hit), True
        while k < len(nodes) and nodes[k][1] < end:
            s, t = nodes[k][1], nodes[k][2]
            last = k + 1 == len(nodes) or nodes[k + 1][1] >= end
            nodes[k][2] = (t[:max(hit - s, 0)] + new if first else "") + (t[end - s:] if last else "")
            changed.add(k)
            first = False
            k += 1
    for k in sorted(changed, reverse=True):
        m, _, t = nodes[k]
        tag = m.group(1)
        if t != t.strip() and "xml:space" not in tag:
            tag = tag[:-1] + ' xml:space="preserve">'
        xml = xml[:m.start()] + tag + escape(t) + m.group(3) + xml[m.end():]
    return xml, len(hits)


def clean(xml, log):
    """Remove supported non-page content; retained package parts still need review."""
    def drop(pattern, what, flags=re.S):
        nonlocal xml
        xml, n = re.subn(pattern, "", xml, flags=flags)
        if n:
            log[what] = log.get(what, 0) + n
    drop(r"<w:(del|moveFrom)\b[^>]*?(?<!/)>.*?</w:\1>", "tracked deletions removed")
    drop(r"<w:(\w+Change)\b[^>]*?(?<!/)>.*?</w:\1>", "formatting-change records removed")
    drop(r"<w:(?:del|ins|moveFrom|moveTo|\w+Change)\b[^>]*/>", "tracked-change marks removed")
    drop(r"</?w:(?:ins|moveTo)\b[^>]*>", "tracked insertions accepted")
    drop(r"<w:(?:moveFromRange|moveToRange|commentRange)(?:Start|End)\b[^>]*/>", "range marks removed")
    drop(r"<w:commentReference\b[^>]*/>", "comments removed")
    drop(r"<w:object\b[^>]*?(?<!/)>.*?</w:object>", "embedded objects removed (spreadsheets and the like are content)")
    xml, hidden = strip_hidden_runs(xml)
    if hidden:
        log["hidden-text runs removed"] = log.get("hidden-text runs removed", 0) + hidden
    xml = re.sub(r'\b(w:tooltip|descr|title)="[^"]*"', r'\1=""', xml)
    xml = re.sub(r"<w:tbl(?:Caption|Description)\b[^>]*/>", "", xml)                      # table alt text
    xml = re.sub(r'(<w:(?:alias|tag)\b[^>]*?w:val=")[^"]*(")', r"\1\2", xml)          # content-control labels
    names = {}
    for name in re.findall(r'<w:bookmarkStart\b[^>]*?w:name="([^"]+)"', xml):          # author-chosen bookmark names
        if not name.startswith("_") and name not in names:
            names[name] = "bm%d" % (len(names) + 1)
    for old, new in names.items():          # the name, links to it, and cross-reference fields, in both field forms
        xml = re.sub(r'(w:(?:name|anchor)=")%s(")' % re.escape(old), r"\g<1>%s\g<2>" % new, xml)
        xml = re.sub(r'((?:<w:instrText[^>]*>|w:instr=")[^<"]*?)\b%s\b' % re.escape(old), r"\g<1>" + new, xml)
    xml = re.sub(r'(<(?:wp:docPr|pic:cNvPr)\b[^>]*?\bname=")[^"]*(")', r"\1Picture\2", xml)
    xml, n = re.subn(r"(<w:instrText[^>]*>)\s*(?:INCLUDEPICTURE|INCLUDETEXT|LINK|DDEAUTO|DDE|DOCPROPERTY|DOCVARIABLE)\b[^<]*", r"\1", xml)
    xml, n2 = re.subn(r'(w:instr=")\s*(?:INCLUDEPICTURE|INCLUDETEXT|LINK|DDEAUTO|DDE|DOCPROPERTY|DOCVARIABLE)\b[^"]*', r"\1", xml)
    if n + n2:
        log["remote-content and property fields blanked"] = log.get("remote-content and property fields blanked", 0) + n + n2
    return xml


def owner_of(rels_name):
    d, f = posixpath.split(rels_name)
    return posixpath.join(posixpath.dirname(d), f[:-5])


def tidy_links_and_media(parts, log):
    """Drop links that are not web links, list the web links kept, and give media neutral names."""
    kept, renamed, n = [], {}, 0
    for name in [x for x in parts if x.endswith(".rels")]:
        owner, rels = owner_of(name), parts[name].decode("utf-8")
        owner_xml = parts.get(owner, b"").decode("utf-8", "replace")
        for rel in REL.findall(rels):
            rid, target = attr(rel, "Id") or "", attr(rel, "Target") or ""
            if attr(rel, "TargetMode") == "External":
                if rel.count("/hyperlink") and re.match(r"https?://", unescape(target)):
                    kept.append(unescape(target))
                    continue
                rels = rels.replace(rel, "")
                owner_xml = re.sub(r'<w:hyperlink\b[^>]*r:id="%s"[^>]*>(.*?)</w:hyperlink>' % re.escape(rid), r"\1",
                                   owner_xml, flags=re.S)
                owner_xml = re.sub(r'\s+r:(?:link|id)="%s"' % re.escape(rid), "", owner_xml)
                log["non-web links removed"] = log.get("non-web links removed", 0) + 1
            elif "/image" in rel and "media/" in target:
                full = posixpath.normpath(posixpath.join(posixpath.dirname(owner), target))
                if full in parts or full in renamed:
                    if full not in renamed:
                        n += 1
                        renamed[full] = posixpath.join(posixpath.dirname(full), "image%d%s" % (n, posixpath.splitext(full)[1]))
                    new_target = posixpath.join(posixpath.dirname(target), posixpath.basename(renamed[full]))
                    rels = rels.replace(rel, rel.replace('Target="%s"' % target, 'Target="%s"' % new_target))
        parts[name] = rels.encode("utf-8")
        if owner in parts:
            parts[owner] = owner_xml.encode("utf-8")
    moved = {new: parts.pop(old) for old, new in renamed.items() if old in parts}   # pop all first: names overlap
    parts.update(moved)
    return kept


def prune(parts):
    """Drop relationships the owning part no longer uses, then every part nothing points to."""
    for name in [n for n in parts if n.endswith(".rels")]:
        owner_xml = parts.get(owner_of(name), b"").decode("utf-8", "replace")

        def keep(m):
            rel = m.group(0)
            rid, kind = attr(rel, "Id"), (attr(rel, "Type") or "").rsplit("/", 1)[-1]
            return rel if kind in IMPLICIT or (rid and ('"%s"' % rid in owner_xml or "'%s'" % rid in owner_xml)) else ""
        parts[name] = REL.sub(keep, parts[name].decode("utf-8")).encode("utf-8")
    reachable, queue = set(), [""]
    while queue:
        owner = queue.pop()
        d, f = posixpath.split(owner)
        rels_name = posixpath.join(d, "_rels", f + ".rels") if owner else "_rels/.rels"
        if rels_name not in parts:
            continue
        reachable.add(rels_name)
        for m in REL.finditer(parts[rels_name].decode("utf-8")):
            target = attr(m.group(0), "Target")
            if attr(m.group(0), "TargetMode") == "External" or not target:
                continue
            full = target.lstrip("/") if target.startswith("/") else posixpath.normpath(posixpath.join(d, target))
            if full in parts and full not in reachable:
                reachable.add(full)
                queue.append(full)
    removed = [n for n in parts if n not in reachable and n != "[Content_Types].xml"]
    for n in removed:
        del parts[n]
    ct = parts["[Content_Types].xml"].decode("utf-8")
    ct = OVERRIDE.sub(lambda m: m.group(0) if (attr(m.group(0), "PartName") or "").lstrip("/") in parts else "", ct)
    parts["[Content_Types].xml"] = ct.encode("utf-8")
    return removed


def apply_edits(parts, edits, problems):
    done = {}
    doc = parts["word/document.xml"].decode("utf-8")
    for item in edits.get("delete_paragraph", []):
        m = find_para(doc, item)
        if not m:
            problems.append("delete_paragraph: no paragraph contains %r" % item)
            continue
        alone = doc[:m.start()].rstrip().endswith(("</w:tcPr>", "<w:tc>")) and doc[m.end():].lstrip().startswith("</w:tc>")
        doc = doc[:m.start()] + ("<w:p/>" if alone else "") + doc[m.end():]
        done["paragraphs deleted"] = done.get("paragraphs deleted", 0) + 1
    for item in edits.get("replace_paragraph", []):
        m = find_para(doc, item.get("containing", ""))
        if not m:
            problems.append("replace_paragraph: no paragraph contains %r" % item.get("containing"))
            continue
        ppr, rpr = pieces(m.group(0))
        doc = doc[:m.start()] + "<w:p>%s%s</w:p>" % (ppr, run_xml(item.get("with", ""), rpr)) + doc[m.end():]
        done["paragraphs replaced"] = done.get("paragraphs replaced", 0) + 1
    for item in edits.get("insert_after", []) + edits.get("insert_before", []):
        anchor = item.get("after") or item.get("before") or ""
        m = PARA.search(doc, doc.find("<w:body")) if item.get("at") == "start" else find_para(doc, anchor)
        if not m:
            problems.append("insert: no paragraph contains %r" % anchor)
            continue
        model = find_para(doc, item["like"]) if item.get("like") else m
        if not model:
            problems.append("insert: no paragraph contains the \"like\" text %r" % item["like"])
            continue
        ppr, rpr = pieces(model.group(0))
        ppr = re.sub(r"<w:sectPr\b.*?</w:sectPr>", "", ppr, flags=re.S)
        if item.get("instruction"):
            ppr, rpr = INSTRUCTION_PPR, instruction_rpr(rpr)
        new = "<w:p>%s%s</w:p>" % (ppr, run_xml(item.get("text", ""), rpr))
        at = m.end() if "after" in item and item.get("at") != "start" else m.start()
        doc = doc[:at] + new + doc[at:]
        done["paragraphs inserted"] = done.get("paragraphs inserted", 0) + 1
    parts["word/document.xml"] = doc.encode("utf-8")
    for old, new in sorted(edits.get("replace", {}).items(), key=lambda kv: -len(kv[0])):
        total = 0
        for name in [n for n in parts if TEXT_PARTS.match(n)]:
            xml, n = replace_text(parts[name].decode("utf-8"), old, new)
            parts[name] = xml.encode("utf-8")
            total += n
        if not total:
            problems.append("replace: %r does not occur" % old)
        done["strings replaced"] = done.get("strings replaced", 0) + total
    for name in [n for n in parts if TEXT_PARTS.match(n)]:
        parts[name] = parts[name].decode("utf-8").replace(NEW, "").encode("utf-8")
    return done


def main(argv):
    args, edits_file, force = [], None, False
    it = iter(argv)
    for a in it:
        if a == "--edits":
            edits_file = next(it, None)
        elif a == "--force":
            force = True
        elif a in ("-h", "--help"):
            print(__doc__)
            return 0
        else:
            args.append(a)
    if len(args) != 2:
        print(__doc__)
        return 2
    src, dst = args
    if os.path.exists(dst) and os.path.samefile(src, dst):
        print("The template would overwrite the sample. Give the template its own file name.")
        return 2
    if os.path.exists(dst) and not force:
        print("%s exists. Pass --force to replace it." % dst)
        return 2
    edits = {}
    if edits_file:
        with open(edits_file, encoding="utf-8-sig") as f:
            edits = json.load(f)
    parts = read_zip(src)
    if "word/document.xml" not in parts:
        print("No word/document.xml in %s. Re-save the file as .docx from Word and try again." % src)
        return 1
    unsafe = [n for n, d in parts.items() if n.endswith((".xml", ".rels")) and not safe_xml(d)]
    if unsafe:
        print("Refusing %s: %s declares a DTD or entities, which no Word file needs." % (src, ", ".join(unsafe)))
        return 1

    inherited = hidden_style_parts(parts)
    if inherited:
        print("Nothing written: hidden style/default declarations in %s. This cleaner does not "
              "resolve inherited visibility, including unused styles. Remove or resolve hidden "
              "content in a reviewed working copy before creating the template." % ", ".join(inherited))
        return 1

    log, problems = {}, []
    for name in [n for n in parts if TEXT_PARTS.match(n)]:
        parts[name] = clean(parts[name].decode("utf-8"), log).encode("utf-8")
    links = tidy_links_and_media(parts, log)
    log.update(apply_edits(parts, edits, problems))

    if "word/settings.xml" in parts:
        s = parts["word/settings.xml"].decode("utf-8")
        for tag in ("docVars", "mailMerge", "rsids"):
            s = re.sub(r"<w:%s\b[^>]*?(?<!/)>.*?</w:%s>" % (tag, tag), "", s, flags=re.S)
        s = re.sub(r"<w:(?:attachedTemplate|docVars|mailMerge|rsids)\b[^>]*/>", "", s)
        parts["word/settings.xml"] = s.encode("utf-8")
    if "docProps/core.xml" in parts:
        now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        c = parts["docProps/core.xml"].decode("utf-8")
        for tag in ("dc:creator", "cp:lastModifiedBy", "dc:title", "dc:subject", "cp:keywords", "dc:description",
                    "cp:category", "cp:contentStatus", "cp:lastPrinted"):
            c = re.sub(r"(<%s\b[^>]*>).*?(</%s>)" % (tag, tag), r"\1\2", c, flags=re.S)
        c = re.sub(r"(<dcterms:(?:created|modified)\b[^>]*>)[^<]*", lambda m: m.group(1) + now, c)
        c = re.sub(r"(<cp:revision>)[^<]*", r"\g<1>1", c)
        parts["docProps/core.xml"] = c.encode("utf-8")
    if "docProps/app.xml" in parts:
        parts["docProps/app.xml"] = APP_XML.encode("utf-8")
    removed = prune(parts)
    links = sorted(set(unescape(attr(r, "Target") or "") for n in parts if n.endswith(".rels")
                       for r in REL.findall(parts[n].decode("utf-8")) if attr(r, "TargetMode") == "External"))
    if "word/document.xml" not in parts:
        print("Could not follow this file's relationships, so nothing was written. Open %s in Word, save it "
              "again as .docx, and rerun." % src)
        return 1

    bad = []
    for name, data in parts.items():
        if name.endswith((".xml", ".rels")):
            try:
                ET.fromstring(data)
            except ET.ParseError as e:
                bad.append("%s: %s" % (name, e))
    if bad:
        print("Nothing written; the result would not be well-formed:\n  " + "\n  ".join(bad))
        return 1
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
        for n in ["[Content_Types].xml"] + sorted(x for x in parts if x != "[Content_Types].xml"):
            z.writestr(n, parts[n])

    print("Wrote %s" % dst)
    for k in sorted(log):
        print("  %s: %d" % (k, log[k]))
    if removed:
        print("  parts removed: %s" % ", ".join(sorted(removed)))
    if links:
        print("  web links still in the template (keep only the firm's own): %s" % ", ".join(links))
    for p in problems:
        print("  PROBLEM  " + p)
    text = dump_text(dst)
    body_text = "\n".join(ln.split("| ", 1)[-1] for ln in text.split("\n"))
    names = []
    for b in re.findall(r"\[(?!\d+\]|[^\W\d_]{1,2}\d{1,3}\])[^\[\]\n]{1,700}\]", body_text):
        inner = b[1:-1].strip()
        name = inner if re.match(r"(?:IF|EF|HVIS|OM|WENN|FALLS|SI|SE|JOS|ALS) ", inner) else inner.split(":", 1)[0].strip()
        if name not in names and not re.match(r"(?:NOTE|ATH|LEIÐBEINING|LEIÐBEININGAR|HINWEIS|OBS|BEMÆRK|HUOM|NOTA|REMARQUE)$", name):
            names.append(name)
    print("  blanks and choices now in the template: %s" % ("; ".join(names) or "none"))
    for long_one in re.findall(r"\[[^\[\]\n]{701,}\]", body_text):
        print("  CHECK  bracketed text longer than 700 characters is not read as a blank by create_docx.py: %s..." % long_one[:60])
    for nested in re.findall(r"\[[^\[\]\n]{0,300}\[[^\[\]\n]{0,80}\]", body_text):
        print("  CHECK  square brackets inside square brackets are not read as one blank by create_docx.py: %s" % nested[:90])
    print("\nThe template as text. Read every line: anything here that belongs to one client or matter is a leak.\n")
    print(text)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
