#!/usr/bin/env python3
"""Report a Word document's layout and structure, read straight from its XML.

Usage:  python3 inspect_docx.py <file.docx> [more.docx ...] [--json out.json]
        python3 inspect_docx.py <file.docx> --text      the document as text: header, body, footer, notes
        python3 inspect_docx.py --compare <original.docx> <new.docx>
                                                        differences in selected formatting declarations;
                                                        not proof of identical page appearance

Prints, per file: page setup, fonts, the paragraph styles actually in use with their
resolved values, how much formatting was applied by hand, the heading outline, the
numbering scheme, header and footer text, tables, and features a drafter has to know
about (footnotes, cross-references, tracked changes, hidden text, blanks, metadata). REVIEW
lines, which need a decision, come only in the last block; sample text is shown after "|"
or in quotes, so a line inside a sample cannot pass for the script's own.

Standard library only. It measures what the file declares; it cannot see what the
page looks like. Open the file in Word and look when appearance matters.
"""
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docxlib import (R, q, wval, onoff, read_zip, parse, rels, iter_paragraphs,  # noqa: E402
                     para_text, core_metadata, is_hidden, dump_text, main_part)

PAPER = {"A4": (11906, 16838), "Letter": (12240, 15840), "Legal": (12240, 20160),
         "A5": (8391, 11906), "A3": (16838, 23811)}
MANUAL_NUM = re.compile(
    r"^\s*(?:\(?\d+(?:\.\d+)*[.)]|\d+(?:\.\d+)+|\(?[a-zA-Z][.)]|\(?[ivxlcIVXLC]+[.)]|"
    r"(?:Article|Section|Clause|Schedule|Annex|Appendix|Part|Artikel|Kapitel|§)\s*\d+|"
    r"\d+\.\s*(?:gr|mgr|kafli)\.?)(?:\s|$)")
BLANKS = re.compile(r"\[\s*[●•xX_. ]*\s*\]|_{4,}|\{\{[^}]+\}\}|<<[^>]+>>|\[[A-Z][A-Z _/-]{2,}\]")


def cm(twips):
    return round(int(twips) / 1440.0 * 2.54, 2)


def pt(twips):
    return round(int(twips) / 20.0, 1)


def theme_fonts(parts):
    out = {}
    for name, data in parts.items():
        if name.startswith("word/theme/") and name.endswith(".xml"):
            s = data.decode("utf-8", "replace")
            for kind in ("major", "minor"):
                m = re.search(r"<a:%sFont>.*?<a:latin typeface=\"([^\"]*)\"" % kind, s, re.S)
                if m:
                    out[kind] = m.group(1)
            break
    return out


def rpr_props(rpr, theme):
    p = {}
    if rpr is None:
        return p
    f = rpr.find(q("rFonts"))
    if f is not None:
        th = f.get(q("asciiTheme")) or f.get(q("hAnsiTheme")) or ""
        name = theme.get("major" if th.startswith("major") else "minor") if th else None
        if not name:                       # a theme font, when set on the same element, overrides the named one
            name = f.get(q("ascii")) or f.get(q("hAnsi"))
        if name:
            p["font"] = name
    sz = wval(rpr, "sz")
    if sz and sz.isdigit():
        p["size"] = int(sz) / 2.0
    for k, tag in (("bold", "b"), ("italic", "i"), ("caps", "caps"), ("smallCaps", "smallCaps")):
        v = onoff(rpr, tag)
        if v is not None:
            p[k] = v
    u = wval(rpr, "u")
    if u:
        p["underline"] = u != "none"
    c = wval(rpr, "color")
    if c and c != "auto":
        p["color"] = c
    return p


def ppr_props(ppr):
    p = {}
    if ppr is None:
        return p
    jc = wval(ppr, "jc")
    if jc:
        p["align"] = {"both": "justified", "start": "left", "end": "right"}.get(jc, jc)
    sp = ppr.find(q("spacing"))
    if sp is not None:
        for k, a in (("before", "before"), ("after", "after")):
            v = sp.get(q(a))
            if v and v.lstrip("-").isdigit():
                p[k] = pt(v)
        line = sp.get(q("line"))
        if line and line.isdigit():
            rule = sp.get(q("lineRule"), "auto")
            p["line"] = ("%sx" % round(int(line) / 240.0, 2)) if rule == "auto" else "%s %spt" % (rule, pt(line))
    ind = ppr.find(q("ind"))
    if ind is not None:
        for k, a in (("left", "left"), ("left", "start"), ("right", "right"),
                     ("firstLine", "firstLine"), ("hanging", "hanging")):
            v = ind.get(q(a))
            if v and v.lstrip("-").isdigit() and int(v):
                p["indent_" + k] = cm(v)
    for k in ("keepNext", "keepLines", "pageBreakBefore"):
        if onoff(ppr, k):
            p[k] = True
    ol = wval(ppr, "outlineLvl")
    if ol is not None and ol.isdigit():
        p["outlineLvl"] = int(ol)
    num = ppr.find(q("numPr"))
    if num is not None:
        p["numId"] = wval(num, "numId")
        p["ilvl"] = wval(num, "ilvl", default="0")
    return p


def load_styles(parts, theme):
    root = parse(parts, "word/styles.xml")
    styles, defaults, default_para = {}, {}, None
    if root is None:
        return styles, defaults, default_para
    dd = root.find(q("docDefaults"))
    if dd is not None:
        r = dd.find("%s/%s" % (q("rPrDefault"), q("rPr")))
        defaults.update(rpr_props(r, theme))
        if r is not None:
            lang = r.find(q("lang"))
            if lang is not None and lang.get(q("val")):
                defaults["lang"] = lang.get(q("val"))
        defaults.update(ppr_props(dd.find("%s/%s" % (q("pPrDefault"), q("pPr")))))
    for s in root.findall(q("style")):
        sid = s.get(q("styleId"))
        info = {"id": sid, "name": wval(s, "name") or sid, "type": s.get(q("type")),
                "basedOn": wval(s, "basedOn"), "props": {}}
        info["props"].update(ppr_props(s.find(q("pPr"))))
        info["props"].update(rpr_props(s.find(q("rPr")), theme))
        styles[sid] = info
        if info["type"] == "paragraph" and s.get(q("default")) in ("1", "true"):
            default_para = sid
    return styles, defaults, default_para


def resolve(styles, defaults, sid):
    chain, seen = [], set()
    while sid and sid in styles and sid not in seen:
        seen.add(sid)
        chain.append(styles[sid])
        sid = styles[sid]["basedOn"]
    out = dict(defaults)
    for s in reversed(chain):
        out.update(s["props"])
    return out


def load_numbering(parts):
    root = parse(parts, "word/numbering.xml")
    nums, abstract, links, linked = {}, {}, {}, {}
    if root is None:
        return nums
    for a in root.findall(q("abstractNum")):
        if wval(a, "numStyleLink"):
            links[a.get(q("abstractNumId"))] = wval(a, "numStyleLink")
        if wval(a, "styleLink"):
            linked[wval(a, "styleLink")] = a.get(q("abstractNumId"))
        levels = {}
        for lvl in a.findall(q("lvl")):
            levels[lvl.get(q("ilvl"))] = {"fmt": wval(lvl, "numFmt"), "text": wval(lvl, "lvlText"),
                                          "start": wval(lvl, "start"), "style": wval(lvl, "pStyle")}
        abstract[a.get(q("abstractNumId"))] = levels
    for aid, name in links.items():      # an abstractNum that only points at a list style takes that style's levels
        if not abstract[aid] and name in linked:
            abstract[aid] = abstract[linked[name]]
    for n in root.findall(q("num")):
        nums[n.get(q("numId"))] = abstract.get(wval(n, "abstractNumId"), {})
    return nums


def section_info(sect, doc_rels, parts):
    info = {}
    sz = sect.find(q("pgSz"))
    if sz is not None and sz.get(q("w")) and sz.get(q("h")):
        w, h = int(sz.get(q("w"))), int(sz.get(q("h")))
        land = sz.get(q("orient")) == "landscape" or w > h
        a, b = min(w, h), max(w, h)
        name = next((n for n, (pw, ph) in PAPER.items() if abs(pw - a) <= 30 and abs(ph - b) <= 30), None)
        info["paper"] = "%s%s (%.1f x %.1f cm)" % (name or "custom", " landscape" if land else "", cm(w), cm(h))
    mar = sect.find(q("pgMar"))
    if mar is not None:
        info["margins_cm"] = {k: cm(mar.get(q(k))) for k in ("top", "right", "bottom", "left", "header", "footer")
                              if mar.get(q(k)) and mar.get(q(k)).lstrip("-").isdigit()}
    cols = sect.find(q("cols"))
    if cols is not None and (cols.get(q("num")) or "1") != "1":
        info["columns"] = int(cols.get(q("num")))
    if sect.find(q("titlePg")) is not None:
        info["different_first_page"] = True
    hf = []
    for kind in ("headerReference", "footerReference"):
        for ref in sect.findall(q(kind)):
            target = doc_rels.get(ref.get("{%s}id" % R), (None, ""))[0]
            if target:
                hf.append({"kind": kind[:6], "applies": ref.get(q("type")), "part": "word/" + target.lstrip("/")})
    info["header_footer"] = hf
    return info


def hf_text(parts, name):
    root = parse(parts, name)
    if root is None:
        return None
    raw = parts[name].decode("utf-8", "replace")
    fields = sorted(set(m.group(1).upper() for m in re.finditer(
        r"(?:instrText[^>]*>|w:instr=\")\s*([A-Za-z]+)", raw)))
    lines = [re.sub(r"\s+", " ", para_text(p)).strip() for p in iter_paragraphs(root)]
    return {"text": [ln for ln in lines if ln], "fields": fields,
            "has_image": "<w:drawing" in raw or "<w:pict" in raw}


def inspect(path):
    parts = read_zip(path)
    main = main_part(parts)
    doc = parse(parts, main)
    if doc is None or doc.find(q("body")) is None:
        raise ValueError("no readable word/document.xml; re-save the file as .docx from Word")
    body = doc.find(q("body"))
    theme = theme_fonts(parts)
    styles, defaults, default_para = load_styles(parts, theme)
    nums = load_numbering(parts)
    doc_rels = rels(parts, "word/_rels/%s.rels" % main.split("/")[-1])
    raw = parts[main].decode("utf-8", "replace")
    rep = {"file": os.path.basename(path), "review": []}

    # sections
    sects = [s for s in doc.iter(q("sectPr"))]
    rep["sections"] = [section_info(s, doc_rels, parts) for s in sects]

    # paragraphs
    style_count, style_sample = collections.Counter(), {}
    direct, outline, manual_num, used_nums = collections.Counter(), [], [], collections.Counter()
    direct_sample = {}
    n_para = n_words = n_default = n_default_direct = n_blanks = 0
    sentences = []
    for p in iter_paragraphs(body):
        text = re.sub(r"[ \t ]+", " ", para_text(p)).strip()
        if not text:
            continue
        if re.match(r"\[(?:NOTE|ATH|LEIÐBEINING|LEIÐBEININGAR|HINWEIS|OBS|BEMÆRK|HUOM|NOTA|REMARQUE)\]", text):
            continue                       # a template's instruction paragraph: never part of a document
        n_para += 1
        n_words += len(text.split())
        sentences += [s for s in re.split(r"(?<=[.!?])\s+", text) if len(s.split()) > 2]
        n_blanks += len(BLANKS.findall(text))
        ppr = p.find(q("pPr"))
        sid = wval(ppr, "pStyle") or default_para
        sname = styles.get(sid, {}).get("name", sid or "(none)")
        style_count[sname] += 1
        style_sample.setdefault(sname, text[:70])
        res = resolve(styles, defaults, sid)
        own = ppr_props(ppr)
        run_props = [rpr_props(r.find(q("rPr")), theme) for r in p.iter(q("r"))]
        run_props = [rp for rp in run_props if rp]
        num_id = own.get("numId") or res.get("numId")
        if num_id and num_id != "0":
            used_nums[(num_id, own.get("ilvl") or res.get("ilvl") or "0")] += 1
        elif MANUAL_NUM.match(text):
            manual_num.append(text[:60])
        all_runs = list(p.iter(q("r")))
        uniform = {}
        if run_props and len(run_props) == len(all_runs):
            for k in ("font", "size", "bold", "italic", "caps", "underline"):
                vals = set(rp.get(k) for rp in run_props)
                if len(vals) == 1 and None not in vals:
                    uniform[k] = vals.pop()
        if sid == default_para:
            n_default += 1
            sig = dict(uniform)
            sig.update({k: own[k] for k in ("align", "indent_left", "before", "after", "line") if k in own})
            if sig:
                n_default_direct += 1
                key = ", ".join("%s=%s" % kv for kv in sorted(sig.items()))
                direct[key] += 1
                direct_sample.setdefault(key, text[:60])
        # outline
        m = re.match(r"heading (\d)", sname, re.I)
        level = int(m.group(1)) if m else (0 if sname.lower() in ("title", "subtitle") else None)
        if level is None and "outlineLvl" in res and res["outlineLvl"] < 9:
            level = res["outlineLvl"] + 1
        inferred = False
        if level is None and len(text) <= 120 and not text.endswith((".", ";", ",")):
            bold = uniform.get("bold", res.get("bold"))
            caps = uniform.get("caps", res.get("caps")) or (text.isupper() and len(text) > 3)
            if bold or caps:
                level, inferred = 1 if caps else 2, True
        if level is not None:
            outline.append({"level": level, "text": text[:100], "style": sname, "inferred": inferred})

    rep["stats"] = {"paragraphs": n_para, "words": n_words,
                    "avg_sentence_words": round(sum(len(s.split()) for s in sentences) / float(len(sentences)), 1)
                    if sentences else None,
                    "blanks_or_placeholders": n_blanks}
    rep["defaults"] = dict(defaults, theme_fonts=theme)
    rep["styles_in_use"] = [{"name": n, "count": c, "sample": style_sample[n],
                             "values": resolve(styles, defaults, next((k for k, v in styles.items() if v["name"] == n), None))}
                            for n, c in style_count.most_common()]
    rep["direct_formatting"] = [{"formatting": k, "count": c, "sample": direct_sample[k]}
                                for k, c in direct.most_common(10)]
    rep["outline"] = outline
    rep["numbering"] = []
    grouped = collections.OrderedDict()   # lists that look the same are reported once
    for nid in sorted(set(n for n, _ in used_nums), key=lambda x: int(x) if x.isdigit() else 0):
        lv = nums.get(nid, {})
        levels = tuple((l, lv.get(l, {}).get("fmt"), lv.get(l, {}).get("text"))
                       for l in sorted(l for n, l in used_nums if n == nid))
        g = grouped.setdefault(levels, {"numIds": [], "paragraphs": 0})
        g["numIds"].append(nid)
        g["paragraphs"] += sum(c for (n, _), c in used_nums.items() if n == nid)
    for levels, g in grouped.items():
        rep["numbering"].append({"numIds": g["numIds"], "paragraphs": g["paragraphs"],
                                 "levels": [{"level": l, "format": f, "pattern": t} for l, f, t in levels]})
    rep["manual_numbering"] = {"count": len(manual_num), "examples": manual_num[:6]}

    # header / footer parts
    rep["header_footer_parts"] = {}
    for name in sorted(parts):
        if re.match(r"word/(header|footer)\d*\.xml$", name):
            info = hf_text(parts, name)
            if info and (info["text"] or info["fields"] or info["has_image"]):
                rep["header_footer_parts"][name] = info
                joined = " ".join(info["text"])
                if re.search(r"\d{3,}|@|\b(ref|matter|file|mál|nr)\b", joined, re.I):
                    rep["review"].append("%s carries a number, address or reference: %r. Keep what belongs to the "
                                         "firm; replace what belongs to one matter or person before the file is "
                                         "reused as an asset." % (name, joined[:120]))

    # tables
    rep["tables"] = []
    for t in body.iter(q("tbl")):
        rows = t.findall(q("tr"))
        ncols = max([len(r.findall(q("tc"))) for r in rows] or [0])
        first = []
        for c in (rows[0].findall(q("tc")) if rows else []):
            cell = re.sub(r"\s+", " ", " ".join(para_text(p) for p in iter_paragraphs(c))).strip()
            first.append(cell if len(cell) <= 60 else cell[:59] + "…")
        rep["tables"].append({"rows": len(rows), "cols": ncols, "style": wval(t.find(q("tblPr")), "tblStyle"),
                              "first_row": first})

    # other features
    fn = parse(parts, "word/footnotes.xml")
    feats = {
        "footnotes": len([f for f in fn.findall(q("footnote")) if f.get(q("type")) in (None, "normal")])
        if fn is not None else 0,
        "tracked_insertions": raw.count("<w:ins "), "tracked_deletions": raw.count("<w:del "),
        "comments": len(re.findall(r"<w:comment ", parts.get("word/comments.xml", b"").decode("utf-8", "replace"))),
        "content_controls": raw.count("<w:sdt>") + raw.count("<w:sdt "),
        "images": raw.count("<w:drawing"),
        "highlighted_runs": raw.count("<w:highlight "),
        "fields": dict(collections.Counter(m.group(1).upper() for m in re.finditer(
            r"(?:instrText[^>]*>|w:instr=\")\s*([A-Za-z]+)", raw))),
    }
    every = "".join(d.decode("utf-8", "replace") for n, d in parts.items()
                    if re.match(r"word/(document|header\d*|footer\d*|footnotes|endnotes)\.xml$", n))
    feats["tracked_insertions"], feats["tracked_deletions"] = every.count("<w:ins "), every.count("<w:del ")
    feats["hidden_runs"] = sum(1 for r in doc.iter(q("r")) if is_hidden(r))
    feats["positioned_content"] = raw.count("<w:tblpPr") + raw.count("<w:txbxContent") + raw.count("<w:framePr")
    all_rels = "".join(d.decode("utf-8", "replace") for n, d in parts.items() if n.endswith(".rels"))
    feats["external_links"] = len(re.findall(r'TargetMode="External"', all_rels))
    feats["remote_fields"] = len(re.findall(r"\b(?:INCLUDEPICTURE|INCLUDETEXT|DDEAUTO|DDE)\b", every))
    rep["features"] = feats
    rep["metadata"] = core_metadata(parts)
    if feats["hidden_runs"]:
        rep["review"].append("%d runs of hidden text. The lawyer cannot see it on the page; it was left out of "
                             "every reading and must not be carried. Mention it in the handover." % feats["hidden_runs"])
    if feats["positioned_content"]:
        rep["review"].append("%d floating tables, text boxes or frames. Positioned content, often the letterhead or "
                             "signature block, is not described by style values. Look at the page in Word."
                             % feats["positioned_content"])
    if feats["external_links"] or feats["remote_fields"]:
        rep["review"].append("%d external links and %d fields that fetch remote content. Opening the "
                             "file may contact those addresses; make_template.py removes all but web hyperlinks."
                             % (feats["external_links"], feats["remote_fields"]))

    # review lines
    if n_para and n_default / float(n_para) > 0.6 and n_default_direct / float(max(n_default, 1)) > 0.25:
        rep["review"].append("Mostly hand-formatted: %d of %d paragraphs sit in the default style and %d of those carry "
                             "direct formatting. The styles describe little; take the look from [direct formatting] "
                             "and from the page as Word shows it." % (n_default, n_para, n_default_direct))
    if len(manual_num) >= 3:
        rep["review"].append("%d paragraphs look numbered by typing, not by Word's numbering. A new document has to "
                             "reproduce the scheme in text or convert it; decide which." % len(manual_num))
    if feats["tracked_insertions"] or feats["tracked_deletions"]:
        rep["review"].append("Tracked changes are present, so this may be a draft rather than the final. Deleted text "
                             "was ignored; inserted text was read as final.")
    if feats["comments"]:
        rep["review"].append("%d comments present. They can show the author's reasoning; they must not travel into an "
                             "asset." % feats["comments"])
    if len(rep["sections"]) > 1:
        rep["review"].append("%d sections with their own page setup or header/footer. Note what each section is for."
                             % len(rep["sections"]))
    if rep["metadata"]:
        rep["review"].append("File metadata names people or systems (%s). make_template.py strips it; do not copy the "
                             "sample itself into a skill." % ", ".join(sorted(rep["metadata"])))
    return rep


def fmt_values(v):
    keys = ("font", "size", "bold", "italic", "caps", "color", "align", "before", "after", "line",
            "indent_left", "indent_hanging", "indent_firstLine", "keepNext", "numId")
    return ", ".join("%s=%s" % (k, v[k]) for k in keys if k in v and v[k] not in (None, False))


def render(rep):
    out = ["=" * 78, rep["file"], "=" * 78]
    s = rep["stats"]
    out.append("[size] %d paragraphs, %d words, average sentence %s words, %d blanks/placeholders"
               % (s["paragraphs"], s["words"], s["avg_sentence_words"], s["blanks_or_placeholders"]))
    out.append("[page]")
    for i, sec in enumerate(rep["sections"], 1):
        out.append("  section %d: %s; margins cm %s%s%s" % (
            i, sec.get("paper", "size not stated"), sec.get("margins_cm", {}),
            "; %d columns" % sec["columns"] if sec.get("columns") else "",
            "; different first page" if sec.get("different_first_page") else ""))
        for hf in sec.get("header_footer", []):
            out.append("    %s (%s pages): %s" % (hf["kind"], hf["applies"], hf["part"]))
    d = rep["defaults"]
    out.append("[defaults] %s; language %s; theme fonts %s" % (fmt_values(d) or "none stated", d.get("lang", "not stated"),
                                                              d.get("theme_fonts") or "none"))
    out.append("[styles in use]")
    for st in rep["styles_in_use"]:
        out.append("  %-24s x%-4d %s" % (st["name"], st["count"], fmt_values(st["values"])))
        out.append("  %-24s       e.g. %r" % ("", st["sample"]))
    if rep["direct_formatting"]:
        out.append("[direct formatting on default-style paragraphs]")
        for df in rep["direct_formatting"]:
            out.append("  x%-4d %s   e.g. %r" % (df["count"], df["formatting"], df["sample"]))
    out.append("[outline]%s" % ("" if rep["outline"] else " no headings found"))
    for h in rep["outline"]:
        out.append("  %s| %s%s" % ("  " * max(h["level"] - 1, 0), h["text"].replace("\n", " / "),
                                 "   (inferred from bold/caps, style %s)" % h["style"] if h["inferred"] else ""))
    out.append("[numbering]%s" % ("" if rep["numbering"] else " no automatic numbering in use"))
    for n in rep["numbering"]:
        ids = n["numIds"]
        out.append("  %s, %d paragraphs: %s" % (
            "list %s" % ids[0] if len(ids) == 1 else "%d lists of one kind" % len(ids), n["paragraphs"], " | ".join(
            "L%s %s %r" % (l["level"], l["format"], l["pattern"]) for l in n["levels"])))
    if rep["manual_numbering"]["count"]:
        out.append("  typed by hand x%d, e.g. %s" % (rep["manual_numbering"]["count"], rep["manual_numbering"]["examples"]))
    out.append("[header/footer]%s" % ("" if rep["header_footer_parts"] else " none"))
    for name, info in rep["header_footer_parts"].items():
        out.append("  %s: text=%s fields=%s%s" % (name, info["text"], info["fields"], " +image" if info["has_image"] else ""))
    out.append("[tables] %d" % len(rep["tables"]))
    for t in rep["tables"][:10]:
        out.append("  %dx%d style=%s first row=%s" % (t["rows"], t["cols"], t["style"], t["first_row"]))
    out.append("[features] %s" % {k: v for k, v in rep["features"].items() if v})
    out.append("[metadata] %s" % (rep["metadata"] or "none"))
    out.append("[review] %s" % ("points that need a decision; anything above that looks like one is sample text"
                               if rep["review"] else "nothing flagged"))
    for r in rep["review"]:
        out.append("REVIEW: " + r)
    return "\n".join(out)


def look(rep):
    """Selected formatting signatures; not an exhaustive layout comparison."""
    first = rep["sections"][0] if rep["sections"] else {}
    return {
        "page": "%s; margins %s%s; %d section(s)" % (first.get("paper"), first.get("margins_cm"),
                                                    "; %s columns" % first["columns"] if first.get("columns") else "",
                                                    len(rep["sections"])),
        "defaults": fmt_values(rep["defaults"]),
        "styles": dict((st["name"], fmt_values(st["values"])) for st in rep["styles_in_use"]),
        "numbering": sorted(" | ".join("L%s %s %r" % (l["level"], l["format"], l["pattern"]) for l in n["levels"])
                            for n in rep["numbering"]),
        "typed numbering": "yes" if rep["manual_numbering"]["count"] >= 3 else "no",
        "header/footer": sorted("%s fields=%s%s%s" % (re.sub(r"\d+", "", name.split("/")[-1]), info["fields"],
                                                     " +image" if info["has_image"] else "",
                                                     " +text" if info["text"] else "")
                                for name, info in rep["header_footer_parts"].items()),
        "direct": set(df["formatting"] for df in rep["direct_formatting"]),
    }


def compare_look(path_a, path_b):
    a, b = look(inspect(path_a)), look(inspect(path_b))
    out, same = ["Formatting compared:  A = %s   B = %s" % (os.path.basename(path_a), os.path.basename(path_b))], True
    for key in ("page", "defaults", "numbering", "typed numbering", "header/footer"):
        if a[key] == b[key]:
            out.append("  %-16s same" % key)
        else:
            same = False
            out.append("  %-16s DIFFERENT\n      A: %s\n      B: %s" % (key, a[key], b[key]))
    both = [n for n in a["styles"] if n in b["styles"]]
    diff = [n for n in both if a["styles"][n] != b["styles"][n]]
    out.append("  %-16s %d used in both, %d differ" % ("styles", len(both), len(diff)))
    for n in diff:
        same = False
        out.append("      %s\n        A: %s\n        B: %s" % (n, a["styles"][n], b["styles"][n]))
    for label, x, y in (("A", a, b), ("B", b, a)):
        only = [n for n in x["styles"] if n not in y["styles"]]
        if only:
            same = False
            out.append("  DIFFERENT styles only in %s: %s  (may be expected when a section is absent)"
                       % (label, ", ".join(only)))
        extra = x["direct"] - y["direct"]
        if extra:
            same = False
            out.append("  DIFFERENT hand formatting only in %s: %s" % (label, "; ".join(sorted(extra))))
    out.append("Compared formatting signatures match." if same else
               "Formatting differences detected. Review whether they follow from intended content or a change to the form.")
    out.append("Coverage: first-section page geometry, style/default values, numbering summaries, "
               "header/footer feature summaries and direct-formatting signatures. This does not "
               "establish identical rendered pages; inspect appearance with a suitable renderer.")
    print("\n".join(out))
    return 0 if same else 1


def main(argv):
    args, json_out, as_text = [], None, False
    it = iter(argv)
    for a in it:
        if a == "--json":
            json_out = next(it, None)
        elif a == "--text":
            as_text = True
        elif a == "--compare":
            pair = [next(it, None), next(it, None)]
            if None in pair:
                print("--compare needs two files: the original and the new document.")
                return 2
            return compare_look(*pair)
        elif a in ("-h", "--help"):
            print(__doc__)
            return 0
        else:
            args.append(a)
    if not args:
        print(__doc__)
        return 2
    if as_text:
        for path in args:
            print("=" * 78 + "\n" + os.path.basename(path) + "\n" + "=" * 78)
            print(dump_text(path))
        return 0
    reports, failed = [], 0
    for path in args:
        try:
            rep = inspect(path)
        except Exception as e:  # one unreadable sample must not hide the others
            print("%s: could not inspect (%s)" % (path, e))
            failed += 1
            continue
        reports.append(rep)
        print(render(rep))
    if json_out:
        with open(json_out, "w", encoding="utf-8") as f:
            json.dump(reports, f, ensure_ascii=False, indent=2)
    return 1 if failed and not reports else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
