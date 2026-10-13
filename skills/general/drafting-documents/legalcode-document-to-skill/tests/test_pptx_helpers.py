"""Synthetic PPTX extraction and isolated-package generation regressions."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL = "http://schemas.openxmlformats.org/package/2006/relationships"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PPTX = load("pptx_test_generator", ROOT / "assets/create_pptx.py")
DOCX = load("pptx_test_loader", ROOT / "scripts/docxlib.py")


class PptxHelpersTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.work = Path(self.temporary.name)

    def deck(self, hidden=False):
        # Physical names and ZIP order differ from the presentation's slide order.
        shape = '<p:cSld><p:spTree><p:sp><p:nvSpPr><p:cNvPr id="2" name="Example shape"/></p:nvSpPr><p:spPr><a:xfrm><a:off x="10" y="20"/><a:ext cx="100" cy="200"/></a:xfrm></p:spPr><p:txBody><a:bodyPr/><a:lstStyle/><a:p>{}</a:p></p:txBody></p:sp></p:spTree></p:cSld>'
        slide = '<p:sld xmlns:p="%s" xmlns:a="%s" show="{}">{}<p:clrMapOvr/></p:sld>' % (P, A)
        parts = {
            "[Content_Types].xml": b'<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"/>',
            "ppt/presentation.xml": ('<p:presentation xmlns:p="%s" xmlns:r="%s"><p:sldIdLst><p:sldId id="256" r:id="s2"/><p:sldId id="257" r:id="s1"/></p:sldIdLst><p:sldSz cx="9144000" cy="5143500"/></p:presentation>' % (P, R)).encode(),
            "ppt/_rels/presentation.xml.rels": ('<Relationships xmlns="%s"><Relationship Id="s1" Type="%s/slide" Target="slides/slide1.xml"/><Relationship Id="s2" Type="%s/slide" Target="slides/slide2.xml"/></Relationships>' % (REL, R, R)).encode(),
            "ppt/slides/slide1.xml": slide.format("0" if hidden else "1", shape.format('<a:r><a:t>Second displayed slide.</a:t></a:r>')).encode(),
            "ppt/slides/slide2.xml": slide.format("1", shape.format('<a:r><a:rPr b="1"/><a:t>Dear [Cli</a:t></a:r><a:r><a:rPr i="1"/><a:t>ent: name], [Topic].</a:t></a:r>')).encode(),
            "ppt/slides/_rels/slide2.xml.rels": ('<Relationships xmlns="%s"><Relationship Id="n1" Type="%s/notesSlide" Target="../notesSlides/notesSlide2.xml"/><Relationship Id="web" Type="%s/hyperlink" Target="https://example.invalid/private" TargetMode="External"/></Relationships>' % (REL, R, R)).encode(),
            "ppt/notesSlides/notesSlide2.xml": ('<p:notes xmlns:p="%s" xmlns:a="%s">%s</p:notes>' % (P, A, shape.format('<a:r><a:t>Private rehearsal note.</a:t></a:r>'))).encode(),
            "ppt/media/image1.png": b"SYNTHETIC-IMAGE",
            "ppt/embeddings/data.xlsx": b"SYNTHETIC-WORKBOOK",
            "ppt/theme/theme1.xml": b'<theme xmlns="http://schemas.openxmlformats.org/drawingml/2006/main"/>',
            "docProps/core.xml": b'<properties><author>Private Author</author></properties>',
        }
        path = self.work / "sample.pptx"
        PPTX.write_package(parts, path)
        return path, parts

    def run_script(self, script, *args, cwd=None):
        return subprocess.run([sys.executable, str(script), *map(str, args)], cwd=cwd,
            capture_output=True, text=True, timeout=30,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})

    def styled_deck(self):
        source, parts = self.deck()
        name = "ppt/slides/slide2.xml"
        parts[name] = parts[name].replace(b'<p:cSld>', b'<p:cSld><p:bg><p:bgPr><a:solidFill><a:srgbClr val="112233"/></a:solidFill></p:bgPr></p:bg>')
        parts[name] = parts[name].replace(b'<a:rPr b="1"/>', b'<a:rPr b="1" sz="2400"><a:solidFill><a:schemeClr val="accent1"/></a:solidFill><a:latin typeface="House Sans"/></a:rPr>')
        rel = "ppt/slides/_rels/slide2.xml.rels"
        parts[rel] = parts[rel].replace(b'</Relationships>', ('<Relationship Id="layout" Type="%s/slideLayout" Target="../slideLayouts/slideLayout1.xml"/></Relationships>' % R).encode())
        parts['ppt/slideLayouts/slideLayout1.xml'] = ('<p:sldLayout xmlns:p="%s" xmlns:a="%s"><p:cSld><p:bg><p:bgPr><a:gradFill><a:gsLst><a:gs pos="0"><a:srgbClr val="ABCDEF"/></a:gs></a:gsLst></a:gradFill></p:bgPr></p:bg></p:cSld></p:sldLayout>' % (P, A)).encode()
        parts['ppt/slideLayouts/_rels/slideLayout1.xml.rels'] = ('<Relationships xmlns="%s"><Relationship Id="master" Type="%s/slideMaster" Target="../slideMasters/slideMaster1.xml"/></Relationships>' % (REL, R)).encode()
        parts['ppt/slideMasters/slideMaster1.xml'] = ('<p:sldMaster xmlns:p="%s" xmlns:a="%s" xmlns:r="%s"><p:cSld><p:bg><p:bgPr><a:blipFill><a:blip r:embed="image"/></a:blipFill></p:bgPr></p:bg></p:cSld><p:clrMap accent1="accent1"/><p:txStyles><p:titleStyle><a:lvl1pPr><a:defRPr sz="3600"><a:latin typeface="+mj-lt"/></a:defRPr></a:lvl1pPr></p:titleStyle></p:txStyles></p:sldMaster>' % (P, A, R)).encode()
        parts['ppt/slideMasters/_rels/slideMaster1.xml.rels'] = ('<Relationships xmlns="%s"><Relationship Id="theme" Type="%s/theme" Target="../theme/theme1.xml"/><Relationship Id="image" Type="%s/image" Target="../media/image1.png"/></Relationships>' % (REL, R, R)).encode()
        parts['ppt/theme/theme1.xml'] = ('<a:theme xmlns:a="%s"><a:themeElements><a:clrScheme name="House"><a:accent1><a:srgbClr val="445566"/></a:accent1></a:clrScheme><a:fontScheme name="House"><a:majorFont><a:latin typeface="House Display"/></a:majorFont><a:minorFont><a:latin typeface="House Body"/></a:minorFont></a:fontScheme><a:fmtScheme name="House"/></a:themeElements></a:theme>' % A).encode()
        parts['ppt/fonts/font1.fntdata'] = b'SYNTHETIC-EMBEDDED-FONT'
        PPTX.write_package(parts, source, force=True)
        return source, parts

    def test_inspector_reports_direct_and_inherited_backgrounds_colours_and_fonts(self):
        source, _ = self.styled_deck()
        report = self.work / "design.json"
        result = self.run_script(ROOT / 'scripts/inspect_pptx.py', source, '--json', report)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        data = json.loads(report.read_text())
        self.assertEqual(data['slides'][0]['design_sources'], ['ppt/slides/slide2.xml',
            'ppt/slideLayouts/slideLayout1.xml', 'ppt/slideMasters/slideMaster1.xml', 'ppt/theme/theme1.xml'])
        local = data['style_sources']['ppt/slides/slide2.xml']
        self.assertIn('112233', str(local['backgrounds']))
        self.assertIn('House Sans', str(local['fonts']))
        self.assertIn('accent1', str(local['text_formatting']))
        theme = data['style_sources']['ppt/theme/theme1.xml']
        for value in ('445566', 'House Display', 'House Body'):
            self.assertIn(value, str(theme['theme_schemes']))
        self.assertIn('ppt/fonts/font1.fntdata', [p['part'] for p in data['review_parts']])

    def test_styled_output_preserves_backgrounds_fonts_palette_layouts_media_and_font_data(self):
        source, before = self.styled_deck()
        values = self.work / 'values.json'
        values.write_text(json.dumps({'Client':'New Client', 'Topic':'New Topic'}))
        output = self.work / 'styled-output.pptx'
        result = self.run_script(ROOT / 'assets/create_pptx.py', '--template', source, values, output)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        comparison = self.run_script(ROOT / 'scripts/inspect_pptx.py', '--compare', source, output)
        self.assertEqual(comparison.returncode, 0, comparison.stdout + comparison.stderr)
        self.assertIn('does not establish identical rendered slides', comparison.stdout)
        after = PPTX.read_package(output)
        for name in before:
            if name != 'ppt/slides/slide2.xml':
                self.assertEqual(before[name], after[name], name)
        root = ET.fromstring(after['ppt/slides/slide2.xml'])
        self.assertEqual(root.find('.//{%s}bg//{%s}srgbClr' % (P,A)).get('val'), '112233')
        self.assertEqual(root.find('.//{%s}rPr/{%s}latin' % (A,A)).get('typeface'), 'House Sans')
        self.assertEqual(root.find('.//{%s}rPr' % A).get('sz'), '2400')

    def test_design_comparison_detects_style_and_asset_changes(self):
        source, before = self.styled_deck()
        cases = [
            ('ppt/slides/slide2.xml', b'112233', b'998877'),
            ('ppt/slides/slide2.xml', b'House Sans', b'Other Font'),
            ('ppt/theme/theme1.xml', b'445566', b'556677'),
            ('ppt/theme/theme1.xml', b'House Body', b'Other Body'),
            ('ppt/slideLayouts/slideLayout1.xml', b'ABCDEF', b'FEDCBA'),
            ('ppt/slideMasters/slideMaster1.xml', b'sz="3600"', b'sz="4800"'),
            ('ppt/media/image1.png', b'SYNTHETIC-IMAGE', b'OTHER-IMAGE'),
            ('ppt/fonts/font1.fntdata', b'SYNTHETIC-EMBEDDED-FONT', b'OTHER-FONT'),
        ]
        for i, (name, old, new) in enumerate(cases):
            with self.subTest(part=name, old=old):
                altered = dict(before)
                altered[name] = altered[name].replace(old, new)
                output = self.work / ('changed-%s.pptx' % i)
                PPTX.write_package(altered, output)
                result = self.run_script(ROOT / 'scripts/inspect_pptx.py', '--compare', source, output)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(name, result.stdout)

    def test_extraction_uses_presentation_order_and_excludes_notes_and_hidden_slides(self):
        source, _ = self.deck(hidden=True)
        self.assertEqual(DOCX.load_paragraphs(source), ["Dear [Client: name], [Topic]."])
        self.assertEqual(DOCX.load_units(source, "sentence"), ["Dear [Client: name], [Topic]."])

    def test_inspector_exposes_notes_hidden_slide_geometry_and_private_surfaces(self):
        source, _ = self.deck(hidden=True)
        report = self.work / "inspection.json"
        result = self.run_script(ROOT / "scripts/inspect_pptx.py", source, "--json", report)
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(report.read_text())
        self.assertEqual([s["part"] for s in data["slides"]], ["ppt/slides/slide2.xml", "ppt/slides/slide1.xml"])
        self.assertTrue(data["slides"][1]["hidden"])
        self.assertIn("Private rehearsal note.", str(data["slides"][0]["notes"]))
        self.assertEqual(data["slides"][0]["shapes"][0]["geometry"][1]["x"], "10")
        self.assertIn("ppt/embeddings/data.xlsx", [p["part"] for p in data["review_parts"]])
        self.assertEqual(data["external_relationships"][0]["Target"], "https://example.invalid/private")

    def test_comparison_accepts_pptx_and_mixed_text_inputs(self):
        source, _ = self.deck()
        text = self.work / "sample.txt"
        text.write_text("Dear [Client: name], [Topic].\nSecond displayed slide.")
        for other in (source, text):
            with self.subTest(other=other):
                result = self.run_script(ROOT / "scripts/compare_samples.py", source, other)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("FIXED", result.stdout)

    def test_generator_runs_from_isolated_delivered_folder_preserving_untouched_bytes(self):
        source, before = self.deck()
        package = self.work / "delivered"
        package.mkdir()
        shutil.copy2(source, package / "template.pptx")
        shutil.copy2(ROOT / "assets/create_pptx.py", package / "create_pptx.py")
        values = self.work / "values.json"
        values.write_text(json.dumps({"Client": "Nýr & <Client>", "Topic": "Advice"}))
        destination = self.work / "draft.pptx"
        result = self.run_script(package / "create_pptx.py", values, destination, cwd=package)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        after = PPTX.read_package(destination)
        self.assertEqual(PPTX.paragraphs(after["ppt/slides/slide2.xml"]), ["Dear Nýr & <Client>, Advice."])
        for name, data in before.items():
            if name != "ppt/slides/slide2.xml":
                self.assertEqual(after[name], data, name)
        self.assertIn(b'<a:rPr b="1"/>', after["ppt/slides/slide2.xml"])
        self.assertIn(b'<a:rPr i="1"/>', after["ppt/slides/slide2.xml"])
        for name, data in after.items():
            if name.endswith(".xml") or name.endswith(".rels"):
                ET.fromstring(data)

    def test_template_preparation_replaces_split_runs_and_does_not_reprocess_new_text(self):
        source, _ = self.deck()
        edits = self.work / "edits.json"
        edits.write_text(json.dumps({"Dear [Client: name]": "[Greeting]", "Second displayed slide.": "[Topic]", "[Topic]": "[Title]"}))
        destination = self.work / "template.pptx"
        result = self.run_script(ROOT / "assets/create_pptx.py", "--template", source, "--replace", edits, destination)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        parts = PPTX.read_package(destination)
        self.assertEqual(PPTX.paragraphs(parts["ppt/slides/slide2.xml"]), ["[Greeting], [Title]."])
        self.assertEqual(PPTX.paragraphs(parts["ppt/slides/slide1.xml"]), ["[Topic]"])

    def test_missing_anchor_fails_without_output(self):
        source, _ = self.deck()
        edits = self.work / "edits.json"
        edits.write_text('{"Absent text": "[Blank]"}')
        destination = self.work / "template.pptx"
        result = self.run_script(ROOT / "assets/create_pptx.py", "--template", source, "--replace", edits, destination)
        self.assertEqual(result.returncode, 2)
        self.assertFalse(destination.exists())

    def test_missing_values_remain_visible_and_reported(self):
        source, _ = self.deck()
        values = self.work / "values.json"
        values.write_text("{}")
        destination = self.work / "draft.pptx"
        result = self.run_script(ROOT / "assets/create_pptx.py", "--template", source, values, destination)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Unresolved blanks: [Client: name], [Topic]", result.stdout)
        self.assertIn("[Client: name]", DOCX.load_paragraphs(destination)[0])

    def test_no_clobber_and_force_never_overwrites_template(self):
        source, _ = self.deck()
        original = source.read_bytes()
        values = self.work / "values.json"
        values.write_text('{"Client":"Synthetic"}')
        destination = self.work / "draft.pptx"
        destination.write_bytes(b"Edited draft")
        result = self.run_script(ROOT / "assets/create_pptx.py", "--template", source, values, destination)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(destination.read_bytes(), b"Edited draft")
        result = self.run_script(ROOT / "assets/create_pptx.py", "--force", "--template", source, values, source)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(source.read_bytes(), original)
        result = self.run_script(ROOT / "assets/create_pptx.py", "--force", "--template", source, values, destination)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Synthetic", DOCX.load_paragraphs(destination)[0])
        self.assertEqual(list(self.work.glob(".pptx-*")), [])

    def test_unsupported_values_fail_before_writing(self):
        source, _ = self.deck()
        values = self.work / "values.json"
        destination = self.work / "draft.pptx"
        for value in (True, ["one"], {"key": "value"}, "first\nsecond", "invalid\x00text"):
            with self.subTest(value=value):
                values.write_text(json.dumps({"Client": value}))
                result = self.run_script(ROOT / "assets/create_pptx.py", "--template", source, values, destination)
                self.assertEqual(result.returncode, 2)
                self.assertFalse(destination.exists())

    def test_xml_entities_rejected_in_utf8_and_utf16(self):
        xml = '<!DOCTYPE root [<!ENTITY secret "value">]><root>&secret;</root>'
        for encoding in ("utf-8", "utf-16"):
            with self.subTest(encoding=encoding):
                with self.assertRaisesRegex(ValueError, "DTD/entity"):
                    PPTX.parse_xml(xml.encode(encoding))

    def test_replacements_preserve_prefixes_entities_and_multiple_occurrences(self):
        xml = ('<x:p xmlns:x="%s"><x:r><x:t>[One] &amp; [Two] [One]</x:t></x:r></x:p>' % A).encode()
        result, counts = PPTX.replace_text(xml, {"[One]": "Á", "[Two]": "Long replacement"})
        self.assertEqual(PPTX.paragraphs(result), ["Á & Long replacement Á"])
        self.assertEqual(counts, {"[One]": 2, "[Two]": 1})
        self.assertTrue(result.startswith(b"<x:p"))


if __name__ == "__main__":
    unittest.main()
