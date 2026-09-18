#!/usr/bin/env python3
"""Align several samples of one document type and sort their text by how it behaves.

Usage:  python3 compare_samples.py <a.docx> <b.docx> [c.pdf d.txt ...]
                                   [--json out.json] [--full] [--base N] [--min-sim 0.55]
                                   [--unit paragraph|sentence]

Text is compared paragraph by paragraph when every sample is the same format, and sentence
by sentence when a PDF or mixed formats are involved, because formats break paragraphs
differently. --unit sentence is also worth a second run on Word samples: it separates the
fixed sentences of a paragraph from the one sentence that changes.

Each unit of the base sample (the longest unless --base says otherwise) is matched
to the other samples and labelled:

  FIXED      identical everywhere            -> stays in the template as it is
  SLOTTED    same sentence, some words move  -> a [blank] for each part that changes
  REWRITTEN  same place, mostly new wording  -> one [blank] for the passage, plus drafting guidance
  OPTIONAL   present in some samples only    -> an [IF choice] paragraph; find what switches it on
  ONLY       present in one sample           -> bespoke, or half of a pair of alternatives

Matching is textual. Paragraphs that do the same job in different words will not pair
up and show as ONLY in each sample; pair those by reading. A paragraph that moved shows
as missing in one place and extra in another. With a single sample there is nothing to
compare: skip this script and sort matter details from standard wording by reading.

Hidden text and tracked deletions are left out. Standard library only; makes no network
calls. The output holds the samples' full text: keep it in the working folder, not in a
skill folder or a repository.
"""
import argparse
import difflib
import json
import os
import re
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docxlib import load_units  # noqa: E402



def norm(s):
    return re.sub(r"\d", "#", re.sub(r"\s+", " ", s).strip().lower())


_WORDS = {}


def words(s):
    w = _WORDS.get(s)
    if w is None:
        w = _WORDS[s] = frozenset(s.split())
    return w


def sim(a, b, floor=0.4):
    """Similarity of two strings, or 0 when it cannot reach floor. The quick ratios are upper bounds."""
    wa, wb = words(a), words(b)
    if min(len(wa), len(wb)) >= 6 and len(wa & wb) < 0.3 * min(len(wa), len(wb)):
        return 0.0          # passages sharing under a third of their words never reach min_sim; skips the slow ratio
    m = difflib.SequenceMatcher(None, a, b, autojunk=False)
    if m.real_quick_ratio() < floor or m.quick_ratio() < floor:
        return 0.0
    return m.ratio()


def fuzzy_pairs(a, b, min_sim):
    """Order-preserving pairing of two paragraph lists that maximises total similarity."""
    m, n = len(a), len(b)
    if not m or not n:
        return []
    band = None if m * n <= 400000 else 250    # very long documents: look near the diagonal only
    if m * n > 40000:
        sys.stderr.write("comparing %d x %d passages, this can take a minute...\n" % (m, n))
    score = [[0.0] * (n + 1) for _ in range(m + 1)]
    sims = {}
    for i in range(1, m + 1):
        centre = int(i * n / float(m))
        lo, hi = (1, n) if band is None else (max(1, centre - band), min(n, centre + band))
        for j in range(1, n + 1):
            best = max(score[i - 1][j], score[i][j - 1])
            if lo <= j <= hi:
                s = sim(a[i - 1], b[j - 1], min_sim)
                if s >= min_sim:
                    sims[(i, j)] = s
                    best = max(best, score[i - 1][j - 1] + s)
            score[i][j] = best
    out, i, j = [], m, n
    while i > 0 and j > 0:
        if (i, j) in sims and abs(score[i][j] - (score[i - 1][j - 1] + sims[(i, j)])) < 1e-9:
            out.append((i - 1, j - 1))
            i, j = i - 1, j - 1
        elif score[i - 1][j] >= score[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return out[::-1]


def align(a, b, min_sim):
    """({index in a: index in b}, indexes paired by position only).

    Exact matches anchor the alignment and the gaps between them are paired by similarity.
    Where a gap then holds the same small number of unpaired paragraphs on both sides, they
    are paired in order: same place, different words, which is what REWRITTEN means.
    """
    pairs, positional = {}, set()
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                pairs[i1 + k] = j1 + k
        elif tag == "replace":
            found = [(i1 + i, j1 + j) for i, j in fuzzy_pairs(a[i1:i2], b[j1:j2], min_sim)]
            pairs.update(found)
            pi, pj = i1, j1
            for fi, fj in found + [(i2, j2)]:
                if 0 < fi - pi == fj - pj <= 3:
                    for k in range(fi - pi):
                        pairs[pi + k] = pj + k
                        positional.add(pi + k)
                pi, pj = fi + 1, fj + 1
    return pairs, positional


MONTHS = (r"(?:jan\w{0,7}|feb\w{0,7}|mar\w{0,4}|apr\w{0,4}|ma[iíy]|j[uú]n\w{0,2}|j[uú]l\w{0,2}|[aá]g[uú]\w{0,3}|"
          r"aug\w{0,4}|sep\w{0,7}|o[ck]t\w{0,5}|n[oó]v\w{0,6}|de[sc]\w{0,6})")
TOKEN = re.compile(r"\d{1,2}\.?\s+%s\s+\d{4}|[\w.+-]{1,64}@[\w.-]{1,100}\w|\d[\d.,/:-]{0,30}\d|"
                   r"\w+(?:[-'’]\w+){0,5}|[^\w\s]" % MONTHS, re.U | re.I)


def spans(s):
    return [m.span() for m in TOKEN.finditer(s)]


def cut_text(s, sp, a, b):
    """The original text covering tokens a..b-1, spacing and line breaks included."""
    return s[sp[a][0]:sp[b - 1][1]] if b > a else ""


def tokens(s):
    """Words, with a date, a number or an email each kept whole so that it becomes one blank, not three."""
    return TOKEN.findall(s)


def join(toks):
    s = " ".join(toks)
    s = re.sub(r"\s+([,.;:!?%)\]}»”])", r"\1", s)
    return re.sub(r"([(\[{«“])\s+", r"\1", s)


def map_boundary(ops, b, side, total):
    c = []
    for tag, i1, i2, j1, j2 in ops:
        if tag == "equal":
            if i1 <= b <= i2:
                c.append(j1 + (b - i1))
        else:
            if b == i1:
                c.append(j1)
            if b == i2:
                c.append(j2)
            if i1 < b < i2:
                c.append(j1 if side == "start" else j2)
    if not c:
        return 0 if side == "start" else total
    return min(c) if side == "start" else max(c)


def slot_template(base, others):
    """Template with {{n}} where wording changes, the values per sample, and the share that varies."""
    bt = tokens(base)
    n = len(bt)
    var, gap, all_ops = [False] * n, [False] * (n + 1), []
    for o in others:
        ot = tokens(o)
        ops = difflib.SequenceMatcher(None, bt, ot, autojunk=False).get_opcodes()
        all_ops.append((ops, ot))
        for tag, i1, i2, j1, j2 in ops:
            if tag in ("replace", "delete"):
                for i in range(i1, i2):
                    var[i] = True
            elif tag == "insert":
                gap[i1] = True
    ranges, i = [], 0
    while i < n:
        if var[i]:
            s = i
            while i < n and var[i]:
                i += 1
            ranges.append((s, i))
        else:
            i += 1
    for g in range(n + 1):
        if gap[g] and not any(s <= g <= e for s, e in ranges):
            ranges.append((g, g))
    ranges.sort()
    bsp, out, pos, values = spans(base), [], 0, []
    osp = [spans(o) for o in others]
    for k, (s, e) in enumerate(ranges, 1):
        start = bsp[s][0] if s < n else len(base)
        out.append(base[pos:start])
        out.append("{{%d}}" % k if e > s else ("{{%d}} " % k if s < n else " {{%d}}" % k))
        pos = bsp[e - 1][1] if e > s else start
        vals = [cut_text(base, bsp, s, e)]
        for (ops, ot), o, sp in zip(all_ops, others, osp):
            js, je = map_boundary(ops, s, "start", len(ot)), map_boundary(ops, e, "end", len(ot))
            vals.append(cut_text(o, sp, js, je))
        values.append(vals)
    out.append(base[pos:])
    varying = sum(1 for v in var if v) / float(n or 1)
    return "".join(out), values, varying


def shape(p):
    """A paragraph reduced to its pattern: names and numbers collapse, small words and punctuation stay."""
    out = []
    for t in tokens(p):
        k = "#" if t[0].isdigit() else ("A" if t[0].isupper() else t.lower())
        if not (k == "A" and out and out[-1] == "A"):
            out.append(k)
    return out


def repeats(paras):
    """Runs of consecutive paragraphs built on one pattern: party lists, schedule rows, signature lines."""
    runs, i = [], 0
    shapes = [shape(p) for p in paras]

    def alike(x, y):
        return (min(len(x), len(y)) >= 5 and
                difflib.SequenceMatcher(None, x, y, autojunk=False).ratio() >= 0.8)
    while i < len(paras) - 1:
        j = i
        while j + 1 < len(paras) and len(paras[j]) <= 300 and alike(shapes[j], shapes[j + 1]):
            j += 1
        if j > i:
            runs.append({"start": i, "count": j - i + 1, "first": paras[i]})
        i = j + 1
    return runs


def compare(paths, min_sim=0.55, base=None, unit="auto"):
    exts = set(os.path.splitext(p)[1].lower() for p in paths)
    if unit == "auto":
        unit = "sentence" if (".pdf" in exts or len(exts) > 1) else "paragraph"
    docs = [load_units(p, unit) for p in paths]
    names = ["S%d" % (i + 1) for i in range(len(docs))]      # not A, B, C: file names often use those
    if base is None:
        base = max(range(len(docs)), key=lambda k: len(docs[k]))
    normed = [[norm(p) for p in d] for d in docs]
    others = [k for k in range(len(docs)) if k != base]
    aligned = {k: align(normed[base], normed[k], min_sim) for k in others}
    maps = {k: aligned[k][0] for k in others}

    rows = []
    for i, text in enumerate(docs[base]):
        present = {base: i}
        for k in others:
            if i in maps[k]:
                present[k] = maps[k][i]
        rows.append({"present": present, "text": text, "base_index": i,
                     "by_position": any(i in aligned[k][1] for k in others)})

    # paragraphs the base lacks: group the ones that match each other across samples
    left = {k: [j for j in range(len(docs[k])) if j not in set(maps[k].values())] for k in others}
    parent = {}

    def find(x):
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a_i, ka in enumerate(others):
        for kb in others[a_i + 1:]:
            la, lb = left[ka], left[kb]
            for i, j in fuzzy_pairs([normed[ka][x] for x in la], [normed[kb][x] for x in lb], min_sim):
                parent[find((ka, la[i]))] = find((kb, lb[j]))
    groups = {}
    for k in others:
        inv = {j: i for i, j in maps[k].items()}
        for j in left[k]:
            anchor = max([inv[x] for x in inv if x < j] or [-1])
            root = find((k, j))
            if k in groups.get(root, {"present": {}})["present"]:
                root = (k, j)       # a second paragraph of this sample in one group gets a row of its own
            g = groups.setdefault(root, {"present": {}, "anchor": anchor, "order": (k, j)})
            g["present"][k] = j
            g["anchor"] = min(g["anchor"], anchor)
    extra = {}
    for g in sorted(groups.values(), key=lambda g: g["order"]):
        k0 = min(g["present"])
        extra.setdefault(g["anchor"], []).append({"present": g["present"], "text": docs[k0][g["present"][k0]],
                                                  "base_index": None})

    ordered = list(extra.get(-1, []))
    for r in rows:
        firm = dict((k, j) for k, j in r["present"].items() if k == base or r["base_index"] not in aligned[k][1])
        if r["by_position"] and len(r["present"]) < len(docs):
            # paired by place only and missing from other samples: two one-off paragraphs, not one optional clause
            for k in sorted(set(r["present"]) - set(firm)):
                extra.setdefault(r["base_index"], []).insert(0, {"present": {k: r["present"][k]},
                                                                 "text": docs[k][r["present"][k]], "base_index": None})
            r["present"], r["by_position"] = firm, False
        ordered.append(r)
        ordered += extra.get(r["base_index"], [])

    n = len(docs)
    for r in ordered:
        ks = sorted(r["present"])
        texts = [docs[k][r["present"][k]] for k in ks]
        r["samples"] = [names[k] for k in ks]
        r["words"] = len(r["text"].split())
        same = len(set(re.sub(r"\s+", " ", t).strip() for t in texts)) == 1
        if len(ks) == 1:
            r["label"] = "ONLY"
        else:
            if same:
                r["label"] = "FIXED"
            else:
                tpl, vals, varying = slot_template(texts[0], texts[1:])
                long_enough = len(tokens(texts[0])) > 12
                r["label"] = "REWRITTEN" if (r.get("by_position") or (varying > 0.6 and long_enough)) else "SLOTTED"
                r["template"], r["varying_share"] = tpl, round(varying, 2)
                r["slots"] = [dict(zip(r["samples"], v)) for v in vals]
            if len(ks) < n:
                r["label"] = "OPTIONAL"
                r["wording"] = "same" if same else "varies"
        r["texts"] = dict(zip(r["samples"], texts))
        del r["present"]
    return {"unit": unit,
            "samples": [{"id": names[k], "file": os.path.basename(paths[k]), "units": len(docs[k]),
                         "repeating_blocks": repeats(docs[k])} for k in range(n)],
            "base": names[base], "rows": ordered}


def render(res, full=False):
    full = full or sum(r["words"] for r in res["rows"]) <= 2500     # short documents are shown whole

    def cut(s):
        s = s.replace("\n", " / ")
        return s if full or len(s) <= 220 else s[:217] + "..."
    n = len(res["samples"])
    out = ["# Sample comparison", ""]
    for s in res["samples"]:
        out.append("- %s = %s (%d %ss)%s" % (s["id"], s["file"], s["units"], res["unit"],
                                                   "  <- base" if s["id"] == res["base"] else ""))
    tot = float(sum(r["words"] for r in res["rows"]) or 1)
    share = {}
    for r in res["rows"]:
        share[r["label"]] = share.get(r["label"], 0) + r["words"]
    out += ["", "Share of words: " + " | ".join("%s %d%%" % (k, round(100 * share.get(k, 0) / tot))
                                                 for k in ("FIXED", "SLOTTED", "REWRITTEN", "OPTIONAL", "ONLY")), ""]
    if n == 2:
        out += ["Two samples only: OPTIONAL cannot be told from ONLY, and a slot seen twice may still be a choice "
                "between two set wordings. Treat every label as provisional.", ""]
    out += ["## Text in reading order", ""]
    for r in res["rows"]:
        who = ",".join(r["samples"])
        if r["label"] == "FIXED":
            out.append("[FIXED] " + cut(r["text"]))
        elif r["label"] == "SLOTTED":
            out.append("[SLOTTED, %d%% of words vary] %s" % (round(100 * r["varying_share"]), cut(r["template"])))
            for k, slot in enumerate(r["slots"], 1):
                out.append("      {{%d}} " % k + " | ".join("%s=%r" % (s, cut(v)) for s, v in slot.items()))
        elif r["label"] == "REWRITTEN":
            out.append("[REWRITTEN%s]" % (", paired by position" if r.get("by_position") else ""))
            for sid, t in r["texts"].items():
                out.append("      %s: %s" % (sid, cut(t)))
        elif r["label"] == "OPTIONAL":
            out.append("[OPTIONAL %d/%d: %s; wording %s] %s" % (len(r["samples"]), n, who, r["wording"],
                                                               cut(r.get("template") or r["text"])))
            for k, slot in enumerate(r.get("slots", []), 1):
                out.append("      {{%d}} " % k + " | ".join("%s=%r" % (s, cut(v)) for s, v in slot.items()))
        else:
            out.append("[ONLY %s] %s" % (who, cut(r["text"])))
    reps = [(s["id"], b) for s in res["samples"] for b in s["repeating_blocks"]]
    if reps:
        out += ["", "## Repeating blocks (candidates for a list that grows with the facts)", ""]
        for sid, b in reps:
            out.append("- %s: %d look-alike paragraphs in a row, starting %r" % (sid, b["count"], cut(b["first"])))
    return "\n".join(out)


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("samples", nargs="+", help=".docx, .txt, .md or .pdf")
    ap.add_argument("--json", metavar="OUT")
    ap.add_argument("--full", action="store_true", help="do not shorten long text")
    ap.add_argument("--base", type=int, metavar="N", help="1-based number of the sample to use as base")
    ap.add_argument("--min-sim", type=float, default=0.55)
    ap.add_argument("--unit", choices=("auto", "paragraph", "sentence"), default="auto")
    a = ap.parse_intermixed_args(argv)
    if len(a.samples) < 2:
        ap.error("comparison needs two or more samples. One sample is enough to build from: skip this step and "
                 "sort what belongs to the matter from the standard wording by reading.")
    if a.base is not None and not 1 <= a.base <= len(a.samples):
        ap.error("--base must be between 1 and %d" % len(a.samples))
    try:
        res = compare(a.samples, a.min_sim, None if a.base is None else a.base - 1, a.unit)
    except (ValueError, OSError, zipfile.BadZipFile) as e:
        print("Cannot compare: %s" % e)
        return 1
    print(render(res, a.full))
    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
