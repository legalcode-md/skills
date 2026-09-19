#!/usr/bin/env python3
"""Create a new Word document from template.docx.

    python3 create_docx.py --list                       the blanks and choices the template asks for
    python3 create_docx.py --text                       the template as text, blanks shown in place
    python3 create_docx.py values.json "New document.docx"
    python3 create_docx.py --force values.json "Existing draft.docx"  only when replacement is intended

The template is written in the language of the documents it came from, and so are its
blanks. A blank is [Name] or [Name: a note on what goes here]; values.json is keyed by
the name, spelt as --list prints it. A paragraph that starts with a choice marker, such
as [IF substitution allowed] or [EF varakrafa á við], is kept or dropped as a whole.
An example for a template with [Principal name], [IF substitution allowed] and one
[Attorney name], [Attorney id] line per attorney. All identities and dates below
are illustrative placeholders, not details from a real matter:

    {"Principal name": "EXAMPLE COMPANY ehf.",
     "Date": "EXAMPLE DATE",
     "Powers granted": "First line\\nSecond line of the same paragraph",
     "IF substitution allowed": true,
     "IF limited in time": false,
     "Attorney name": [{"Attorney name": "EXAMPLE PERSON 1", "Attorney id": "EXAMPLE ID 1"},
                       {"Attorney name": "EXAMPLE PERSON 2", "Attorney id": "EXAMPLE ID 2"}]}

  [Name]        is replaced by its value wherever it appears, header and footer included;
                the note after a colon is guidance and goes when the blank is filled
  [IF choice]   at the start of a paragraph (IF, EF, HVIS, OM, WENN, FALLS, SI, SE, JOS or
                ALS, in capitals): true keeps the paragraph and removes the marker, false
                removes the paragraph; leave the key out and the paragraph stays with its
                marker. The key is the marker's text: "EF varakrafa á við". A blank inside
                a kept paragraph still needs its own value.
                The same marker at the start of a line inside a paragraph (a signature
                block built with line breaks) keeps or drops just that line.
                [IF NOT choice] ([EF EKKI ...], [HVIS IKKE ...], [WENN NICHT ...]) is the
                other branch: it follows the same key and is kept when that key is false.
  [NOTE] ...    a paragraph that starts with [NOTE], [ATH], [LEIÐBEINING], [HINWEIS], [OBS],
                [BEMÆRK], [HUOM], [NOTA] or [REMARQUE] is an instruction to whoever works
                with the template. --text shows it; it is never part of a created document.
  a list        repeats what holds that blank, once per item. A list of strings repeats the
                paragraph (or table row): several paragraphs of free text under one heading,
                one line per party. A list of {"Blank": "value", ...} repeats the whole run
                of adjacent paragraphs that hold those blanks, so a heading and the text
                under it can come any number of times; a value inside may itself be a list
                of paragraphs. The list's key is the name of one blank in the run, and a
                blank filled from a list must have a name used nowhere else. [] removes it.

Order of work: choices first, then lists, then single values, so a paragraph behind a
choice may hold a list. A blank with its note is read up to 700 characters.

Inside a value, **bold**, *italic* and __underline__ are honoured (write \\* for a literal
asterisk); everything else about the text's look comes from the place it lands in.

Anything not supplied stays in the document as a yellow [blank] and is listed at the end,
so nothing is ever filled with a guess. The wording, styles, numbering, header and footer
all come from the template; this script changes nothing else.

Existing output is protected unless --force is supplied. Output is written to a temporary
file and published only after the ZIP is complete. The template can never be overwritten.
Standard library only, Python 3.9+. The template lives beside this file unless --template
says otherwise.
"""
import bisect
import datetime
import json
import os
import re
import sys
import tempfile
import zipfile
from xml.sax.saxutils import escape, unescape

HERE = os.path.dirname(os.path.abspath(__file__))
TEXT_PARTS = re.compile(r"word/(document|header\d*|footer\d*|footnotes|endnotes)\.xml$")
T_OR_PEND = re.compile(r"(<w:t(?:\s[^>]*)?>)([^<]*)(</w:t>)|(</w:p>)")
PARA = re.compile(r"<w:p(?:\s[^>]*)?>(?:(?!</w:p>|<w:p[ >]).)*</w:p>", re.S)
ROW = re.compile(r"<w:tr(?:\s[^>]*)?>(?:(?!</w:tr>|<w:tr[ >]).)*</w:tr>", re.S)
SIMPLE_RUN = re.compile(r"<w:r(?:\s[^>]*)?>(<w:rPr>(?:(?!</w:rPr>).)*</w:rPr>)?(<w:t(?:\s[^>]*)?>)([^<]*)</w:t></w:r>", re.S)
BLANK = re.compile(r"\[(?!\d+\]|[^\W\d_]{1,2}\d{1,3}\])[^\[\]\n]{1,700}\]")   # [Name] or [Name: note]; not [2015], not a reference key like [L1]
IF_WORDS = "IF|EF|HVIS|OM|WENN|FALLS|SI|SE|JOS|ALS"
NOT_WORDS = "NOT|EKKI|IKKE|INTE|NICHT|PAS|NO|EI|NIET"
NOTE_WORDS = "NOTE|ATH|LEIÐBEINING|LEIÐBEININGAR|HINWEIS|OBS|BEMÆRK|HUOM|NOTA|REMARQUE"
INLINE = re.compile(r"(\*\*[^*\n]+\*\*|__[^_\n]+__|(?<!\\)\*[^*\n]+(?<!\\)\*)")
LINE_TOKEN = re.compile(r"(<w:br\s*/>)|(<w:t(?:\s[^>]*)?>)([^<]*)(</w:t>)")
AFTER_U = ("<w:effect", "<w:bdr", "<w:shd", "<w:fitText", "<w:vertAlign", "<w:rtl", "<w:cs", "<w:em ", "<w:lang",
           "<w:eastAsianLayout", "<w:specVanish", "<w:oMath")
MARK = "\ue000"      # stands in for the inserted value while offsets are worked out in plain text
AFTER_HIGHLIGHT = ("<w:u ", "<w:u/>", "<w:effect", "<w:bdr", "<w:shd", "<w:fitText", "<w:vertAlign", "<w:rtl",
                   "<w:cs", "<w:em ", "<w:lang", "<w:eastAsianLayout", "<w:specVanish", "<w:oMath")


def plain(xml):
    text = re.sub(r"<w:tab\s*/>|<w:br\s*/>", " ", xml)
    return re.sub(r"\s+", " ", "".join(unescape(t) for t in re.findall(r"<w:t(?:\s[^>]*)?>([^<]*)</w:t>", text))).strip()


def lines_xml(text):
    return '</w:t><w:br/><w:t xml:space="preserve">'.join(escape(line) for line in text.split("\n"))


def with_format(rpr, kind):
    """The run properties rpr with bold, italic or underline switched on, in the order Word expects."""
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


def value_xml(value, rpr=""):
    """A value as XML to splice inside a w:t element. Line breaks become Word line breaks; **bold**, *italic*
    and __underline__ become runs of their own that otherwise look like the run they sit in."""
    out = []
    for seg in INLINE.split(str(value)):
        if not seg:
            continue
        kind = "b" if seg.startswith("**") else "u" if seg.startswith("__") else "i" if seg.startswith("*") else None
        if kind and len(seg) > (4 if kind in "bu" else 2):
            inner = seg[2:-2] if kind in "bu" else seg[1:-1]
            out.append('</w:t></w:r><w:r>%s<w:t xml:space="preserve">%s</w:t></w:r><w:r>%s<w:t xml:space="preserve">'
                       % (with_format(rpr, kind), lines_xml(inner.replace("\\*", "*")), rpr))
        else:
            out.append(lines_xml(seg.replace("\\*", "*")))
    return "".join(out)


def run_rpr(xml, pos):
    """Run properties of the run that contains position pos."""
    start = max(xml.rfind("<w:r>", 0, pos), xml.rfind("<w:r ", 0, pos))
    m = re.match(r"<w:r(?:\s[^>]*)?>\s*(<w:rPr>.*?</w:rPr>)?", xml[start:pos], re.S) if start >= 0 else None
    return (m.group(1) or "") if m else ""


def replace_text(xml, old, value):
    """Replace every occurrence of text with a value, even where Word has split the text across runs.
    One pass: lay the text out once, find every hit, apply them last to first so earlier offsets stay true."""
    if not old:
        return xml
    nodes, virtual, pos = [], [], 0
    for m in T_OR_PEND.finditer(xml):
        if m.group(4):
            virtual.append("\n")
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
            nodes[k][2] = (t[:max(hit - s, 0)] + MARK if first else "") + (t[end - s:] if last else "")
            changed.add(k)
            first = False
            k += 1
    for k in sorted(changed, reverse=True):
        m, _, t = nodes[k]
        tag = m.group(1) if "xml:space" in m.group(1) else m.group(1)[:-1] + ' xml:space="preserve">'
        inner = escape(t).replace(MARK, value_xml(value, run_rpr(xml, m.start()))) if MARK in t else escape(t)
        xml = xml[:m.start()] + tag + inner + m.group(3) + xml[m.end():]
    return xml


def name_of(blank):
    """'[Name: note]' -> 'Name'. A choice marker keeps its whole text: '[EF varakrafa]' -> 'EF varakrafa'."""
    inner = blank[1:-1].strip()
    if re.match(r"(?:%s) " % IF_WORDS, inner):
        return inner
    return inner.split(":", 1)[0].strip()


def spellings(xml, key):
    """Every way the blank called key is written in this XML: with and without its note."""
    found = set(b for b in BLANK.findall(plain_all(xml)) if name_of(b) == key)
    return sorted(found, key=len, reverse=True) or ["[%s]" % key]


def plain_all(xml):
    return "\n".join(plain(p.group(0)) for p in PARA.finditer(xml))


def shown(xml):
    """A paragraph as --text prints it: line breaks inside it stay visible."""
    text = re.sub(r"<w:br\s*/>", "<w:t> / </w:t>", re.sub(r"<w:tab\s*/>", "<w:t> </w:t>", xml))
    return re.sub(r"[ \t]+", " ", "".join(unescape(t) for t in re.findall(r"<w:t(?:\s[^>]*)?>([^<]*)</w:t>", text))).strip()


def fill(xml, values):
    for key, value in values.items():
        if not isinstance(value, (list, dict, bool)) and value not in (None, ""):
            for written in spellings(xml, key):
                xml = replace_text(xml, written, value)
    return xml


def block_around(xml, start, end):
    """The table row around a span when there is one, else the span itself."""
    for m in ROW.finditer(xml):
        if m.start() <= start and end <= m.end():
            return m.start(), m.end()
    return start, end


def block_for(xml, names):
    """The first run of adjacent paragraphs that each hold a blank called one of names."""
    paras = list(PARA.finditer(xml))

    def holds(p):
        return any(name_of(b) in names for b in BLANK.findall(plain(p.group(0))))
    first = next((i for i, p in enumerate(paras) if holds(p)), None)
    if first is None:
        return None
    last = i = first
    while i + 1 < len(paras) and not xml[paras[i].end():paras[i + 1].start()].strip():
        i += 1
        if holds(paras[i]):
            last = i
        elif plain(paras[i].group(0)):
            break
    return block_around(xml, paras[first].start(), paras[last].end())


def repeat_lists(xml, values):
    for key, items in values.items():
        if not isinstance(items, list):
            continue
        names = set([key])
        for item in items:
            if isinstance(item, dict):
                names.update(item)
        span = block_for(xml, names)
        if not span:
            continue
        s, e = span
        built = []
        for item in items:
            one = xml[s:e]
            if isinstance(item, dict):
                one = fill(repeat_lists(one, item), item)
            else:
                for w in spellings(one, key):
                    one = replace_text(one, w, item)
            built.append(one)
        xml = xml[:s] + "".join(built) + xml[e:]
    return xml


def decide(name, values):
    """True, False or None (not said) for a choice marker's text such as 'EF varakrafa' or 'EF EKKI varakrafa'."""
    word, _, rest = name.partition(" ")
    rest = rest.strip()
    if name in values or rest in values:
        return values.get(name, values.get(rest))
    neg = re.match(r"(?:%s) (.+)" % NOT_WORDS, rest)
    if neg:
        base = values.get("%s %s" % (word, neg.group(1).strip()), values.get(neg.group(1).strip()))
        return None if base is None else not base
    return None


def line_choices(para, values, undecided):
    """A choice marker at the start of a line inside a paragraph keeps or drops that one line."""
    toks = list(LINE_TOKEN.finditer(para))
    lines, breaks, cur = [], [], []
    for t in toks:
        if t.group(1):
            lines.append(cur)
            breaks.append(t)
            cur = []
        else:
            cur.append(t)
    lines.append(cur)
    cuts, keep = [], []
    for i, line in enumerate(lines):
        if i == 0:
            continue
        mark = re.match(r"\s*\[((?:%s) [^\]]{1,200})\]" % IF_WORDS, "".join(unescape(t.group(3)) for t in line))
        if not mark:
            continue
        name = mark.group(1).strip()
        chosen = decide(name, values)
        if chosen is None:
            undecided.append(name)
        elif chosen:
            keep.append(name)
        else:
            cuts.append((breaks[i - 1].start(), breaks[i - 1].end(), ""))
            cuts += [(t.start(3), t.end(3), "") for t in line]
    for a, b, new in sorted(cuts, reverse=True):
        para = para[:a] + new + para[b:]
    for name in keep:
        para = replace_text(replace_text(para, "[%s] " % name, ""), "[%s]" % name, "")
    return para


def choices(xml, values, undecided):
    out, last = [], 0
    for m in PARA.finditer(xml):
        text = plain(m.group(0))
        alone = xml[:m.start()].rstrip().endswith(("</w:tcPr>", "<w:tc>")) and xml[m.end():].lstrip().startswith("</w:tc>")
        if re.match(r"\[(?:%s)\]" % NOTE_WORDS, text):
            out.append(xml[last:m.start()] + ("<w:p/>" if alone else ""))      # an instruction: never in a document
            last = m.end()
            continue
        mark = re.match(r"\[((?:%s) [^\]]{1,200})\]" % IF_WORDS, text)
        if not mark:
            if re.search(r"\[(?:%s) " % IF_WORDS, text):
                out.append(xml[last:m.start()] + line_choices(m.group(0), values, undecided))
                last = m.end()
            continue
        name = mark.group(1).strip()
        chosen = decide(name, values)
        out.append(xml[last:m.start()])
        last = m.end()
        if chosen is None:
            undecided.append(name)
            out.append(m.group(0))
        elif chosen:
            kept = replace_text(m.group(0), "[%s] " % name, "")
            out.append(line_choices(replace_text(kept, "[%s]" % name, ""), values, undecided))
        else:
            out.append("<w:p/>" if alone else "")
    return "".join(out) + xml[last:]


def highlight_blanks(xml):
    """Give every blank that is still open a yellow highlight, splitting the run so only the blank is marked."""
    def mark(rpr):
        tag = '<w:highlight w:val="yellow"/>'
        if not rpr:
            return "<w:rPr>%s</w:rPr>" % tag
        if "<w:highlight" in rpr:
            return rpr
        spots = [rpr.find(t) for t in AFTER_HIGHLIGHT if rpr.find(t) >= 0]
        at = min(spots) if spots else rpr.rindex("</w:rPr>")
        return rpr[:at] + tag + rpr[at:]

    def split(m):
        rpr, text = m.group(1) or "", unescape(m.group(3))
        if not BLANK.search(text):
            return m.group(0)
        out, pos = [], 0
        for b in BLANK.finditer(text):
            if b.start() > pos:
                out.append('<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (rpr, escape(text[pos:b.start()])))
            out.append('<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (mark(rpr), escape(b.group(0))))
            pos = b.end()
        if pos < len(text):
            out.append('<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (rpr, escape(text[pos:])))
        return "".join(out)
    return SIMPLE_RUN.sub(split, xml)


def write_docx(parts, destination, force=False):
    """Publish a complete ZIP, with no-clobber semantics unless replacement is intended."""
    directory = os.path.dirname(os.path.abspath(destination))
    fd, temporary = tempfile.mkstemp(prefix=".docx-", suffix=".tmp", dir=directory)
    os.close(fd)
    try:
        with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED) as z:
            for n in ["[Content_Types].xml"] + sorted(x for x in parts if x != "[Content_Types].xml"):
                z.writestr(n, parts[n])
        if force:
            os.replace(temporary, destination)
        else:
            # Same-directory hard link creates the name atomically and fails if
            # another process created it after the initial existence check.
            os.link(temporary, destination)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def main(argv):
    args, template, listing, as_text = [], os.path.join(HERE, "template.docx"), False, False
    force = False
    it = iter(argv)
    for a in it:
        if a == "--template":
            template = next(it, template)
        elif a == "--list":
            listing = True
        elif a == "--text":
            as_text = True
        elif a == "--force":
            force = True
        elif a in ("-h", "--help"):
            print(__doc__)
            return 0
        else:
            args.append(a)
    if not os.path.exists(template):
        print("No template at %s. Pass --template." % template)
        return 1
    with zipfile.ZipFile(template) as z:
        parts = {i.filename: z.read(i.filename) for i in z.infolist()}
    names = [n for n in sorted(parts) if TEXT_PARTS.match(n)]

    if as_text:
        for n in names:
            lines = [shown(p.group(0)) for p in PARA.finditer(parts[n].decode("utf-8"))]
            print("--- %s\n%s" % (n, "\n".join(ln for ln in lines if ln)))
        return 0
    is_choice = re.compile(r"\[(?:%s) " % IF_WORDS)
    if listing:
        seen, instructions = {}, 0
        for n in names:
            for b in BLANK.findall(plain_all(parts[n].decode("utf-8"))):
                if re.match(r"\[(?:%s)\]$" % NOTE_WORDS, b):
                    instructions += 1
                    continue
                note = b[1:-1].split(":", 1)[1].strip() if ":" in b and not is_choice.match(b) else ""
                seen[name_of(b)] = seen.get(name_of(b)) or note
        starts = set()
        for n in names:
            for para in PARA.finditer(parts[n].decode("utf-8")):
                for line in shown(para.group(0)).split(" / "):
                    head = re.match(r"\s*\[((?:%s) [^\]]{1,200})\]" % IF_WORDS, line)
                    if head:
                        starts.add(head.group(1).strip())
        for k in [k for k in seen if is_choice.match("[%s " % k.split(" ", 1)[0]) and k not in starts]:
            print("WARNING: [%s] starts neither a paragraph nor a line, so it cannot be switched." % k)
        if instructions:
            print("Instruction paragraphs: %d. Read them with --text; they are left out of every document." % instructions)
        print("Choices (true keeps the paragraph or line, false drops it):")
        for k in [k for k in seen if is_choice.match("[%s " % k.split(" ", 1)[0])] or ["  none"]:
            neg = re.match(r"(\S+) (?:%s) (.+)" % NOT_WORDS, k)
            print("  %s%s" % (k, "   <- the other branch of \"%s %s\"; takes no value of its own" % neg.groups() if neg else ""))
        print("Blanks:")
        for k, note in [(k, v) for k, v in seen.items() if not is_choice.match("[%s " % k.split(" ", 1)[0])] or [("none", "")]:
            print("  %s%s" % (k, "   <- " + note if note else ""))
        return 0
    if len(args) != 2:
        print(__doc__)
        return 2
    if os.path.exists(args[1]) and os.path.samefile(args[1], template):
        print("That would overwrite the template. Choose another file name.")
        return 2
    if os.path.lexists(args[1]) and not force:
        print("%s exists. Use a new file name or pass --force to replace it." % args[1])
        return 2
    with open(args[0], encoding="utf-8-sig") as f:
        values = json.load(f)
    values = {k.strip().strip("[]"): v for k, v in values.items()}

    undecided = []
    for n in names:
        xml = parts[n].decode("utf-8")
        xml = choices(xml, values, undecided)
        xml = repeat_lists(xml, values)
        xml = fill(xml, values)
        parts[n] = highlight_blanks(xml).encode("utf-8")
    if "docProps/core.xml" in parts:
        now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        core = parts["docProps/core.xml"].decode("utf-8")
        parts["docProps/core.xml"] = re.sub(r"(<dcterms:(?:created|modified)\b[^>]*>)[^<]*",
                                            lambda m: m.group(1) + now, core).encode("utf-8")
    try:
        write_docx(parts, args[1], force=force)
    except FileExistsError:
        print("%s now exists. Nothing was replaced; choose another file name." % args[1])
        return 2

    left = []
    for n in names:
        for b in BLANK.findall("\n".join(plain(p.group(0)) for p in PARA.finditer(parts[n].decode("utf-8")))):
            if name_of(b) not in left and not is_choice.match(b):
                left.append(name_of(b))
    with zipfile.ZipFile(template) as z:
        original = "\n".join(plain_all(z.read(n).decode("utf-8")) for n in names)
    asked = set(k for v in values.values() if isinstance(v, list) for i in v if isinstance(i, dict) for k in i)
    known = set(name_of(b) for b in BLANK.findall(original))
    known |= set(k.split(" ", 1)[1].strip() for k in known if is_choice.match("[%s " % k.split(" ", 1)[0]) and " " in k)
    known -= set(k for k in known if re.match(r"(?:\S+ )?(?:%s) " % NOT_WORDS, k))
    unused = [k for k in values if k not in known and k not in asked]
    print("Wrote %s" % args[1])
    print("  still open, highlighted yellow: %s" % (", ".join(left) or "nothing"))
    if undecided:
        print("  choices not made, paragraph left in with its marker: %s" % ", ".join(sorted(set(undecided))))
    if unused:
        print("  values with no matching blank in the template: %s" % ", ".join(unused))
    print("Open it and read it through before it goes anywhere.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
