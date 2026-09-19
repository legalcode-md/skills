"""Synthetic regressions for cleanup, formatting checks and safe generation.

Run from the skill folder: python3 -m unittest discover -s tests -v
Fixtures are created in temporary directories; no client files or extra packages are used.
"""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
P = "http://schemas.openxmlformats.org/package/2006/relationships"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GENERATOR = load_module("generator_under_test", ROOT / "assets/create_docx.py")
DOCXLIB = load_module("docxlib_under_test", ROOT / "scripts/docxlib.py")


class DocxHelpersTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.work = Path(self.temporary.name)

    def document(self, name, body, default_size=24, style_extra="", default_extra="", header=None):
        parts = {
            "[Content_Types].xml": '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                '<Default Extension="xml" ContentType="application/xml"/>'
                '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
                '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>',
            "_rels/.rels": f'<Relationships xmlns="{P}"><Relationship Id="rId1" Type="{R}/officeDocument" Target="word/document.xml"/></Relationships>',
            "word/_rels/document.xml.rels": f'<Relationships xmlns="{P}"><Relationship Id="rId1" Type="{R}/styles" Target="styles.xml"/>'
                + (f'<Relationship Id="rId2" Type="{R}/header" Target="header1.xml"/>' if header else "") + '</Relationships>',
            "word/styles.xml": f'<w:styles xmlns:w="{W}"><w:docDefaults><w:rPrDefault><w:rPr>'
                f'<w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="{default_size}"/>{default_extra}'
                '</w:rPr></w:rPrDefault></w:docDefaults><w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
                f'<w:name w:val="Normal"/></w:style>{style_extra}</w:styles>',
            "word/document.xml": f'<w:document xmlns:w="{W}" xmlns:r="{R}"><w:body>{body}<w:sectPr>'
                + ('<w:headerReference w:type="default" r:id="rId2"/>' if header else "")
                + '<w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/>'
                '</w:sectPr></w:body></w:document>',
        }
        if header:
            parts["word/header1.xml"] = f'<w:hdr xmlns:w="{W}">{header}</w:hdr>'
        path = self.work / name
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as output:
            for part, data in parts.items():
                output.writestr(part, data)
        return path

    def run_script(self, script, *args):
        return subprocess.run([sys.executable, str(ROOT / script), *map(str, args)],
                              text=True, capture_output=True, timeout=30,
                              env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})

    def xml(self, path, part="word/document.xml"):
        with zipfile.ZipFile(path) as archive:
            return archive.read(part).decode("utf-8")

    def fill_input(self):
        template = self.document("template.docx", '<w:p><w:r><w:t>[Client</w:t></w:r><w:r><w:t> name]</w:t></w:r></w:p>'
            '<w:p><w:r><w:t>[IF optional] Optional sentence.</w:t></w:r></w:p>'
            '<w:p><w:r><w:t>[IF NOT optional] Alternative sentence.</w:t></w:r></w:p>'
            '<w:p><w:r><w:t>[Item]</w:t></w:r></w:p>')
        values = self.work / "values.json"
        values.write_text(json.dumps({"Client name": "Synthetic Client", "IF optional": False,
                                      "Item": ["First entry", "Second entry"]}), encoding="utf-8")
        return template, values

    def test_hidden_toggle_forms_are_removed_from_package(self):
        for index, toggle in enumerate(("<w:vanish w:val='true'/>", '<w:vanish w:val="true"/>',
                                       '<w:vanish/>', "<w:vanish w:val='1'></w:vanish>",
                                       "<w:vanish\n w:val = 'on' />")):
            with self.subTest(toggle=toggle):
                source = self.document(f"source-{index}.docx", '<w:p><w:r><w:t>Árleg prófun.</w:t></w:r>'
                    f'<w:r><w:rPr>{toggle}</w:rPr><w:t>SYNTHETIC_PRIVATE_TEXT</w:t></w:r></w:p>')
                destination = self.work / f"clean-{index}.docx"
                result = self.run_script("scripts/make_template.py", source, destination)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                with zipfile.ZipFile(destination) as archive:
                    for name in archive.namelist():
                        self.assertNotIn(b"SYNTHETIC_PRIVATE_TEXT", archive.read(name))
                self.assertIn("Árleg prófun.", self.xml(destination))

    def test_explicit_visible_toggles_are_preserved(self):
        for value in ("false", "0", "off"):
            with self.subTest(value=value):
                xml = f'<w:document xmlns:w="{W}"><w:p><w:r><w:rPr><w:vanish w:val=\'{value}\'/></w:rPr><w:t>Keep.</w:t></w:r></w:p></w:document>'
                cleaned, count = DOCXLIB.strip_hidden_runs(xml)
                self.assertEqual((cleaned, count), (xml, 0))

    def test_hidden_detection_uses_namespace_and_preserves_other_bytes(self):
        hidden = '<x:r><x:rPr><x:vanish x:val="true"/></x:rPr><x:t>Remove.</x:t></x:r>'
        xml = f'<x:document xmlns:x="{W}"><x:p><x:r><x:t>Þetta er sýnilegt.</x:t></x:r>{hidden}</x:p></x:document>'
        cleaned, count = DOCXLIB.strip_hidden_runs(xml)
        self.assertEqual(count, 1)
        self.assertEqual(cleaned, xml.replace(hidden, ""))
        ET.fromstring(cleaned)

    def test_nested_hidden_runs_do_not_corrupt_surrounding_xml(self):
        hidden = '<w:r><w:rPr><w:vanish/></w:rPr><w:drawing><w:p><w:r><w:rPr><w:vanish/></w:rPr><w:t>Nested.</w:t></w:r></w:p></w:drawing></w:r>'
        xml = f'<w:document xmlns:w="{W}"><w:p>{hidden}<w:r><w:t>Keep.</w:t></w:r></w:p></w:document>'
        cleaned, count = DOCXLIB.strip_hidden_runs(xml)
        self.assertEqual(count, 1)
        self.assertEqual(cleaned, xml.replace(hidden, ""))
        ET.fromstring(cleaned)

    def test_hidden_style_and_default_declarations_refuse_without_writing(self):
        for index, options in enumerate((
                {"style_extra": '<w:style w:type="character" w:styleId="Hidden"><w:rPr><w:vanish/></w:rPr></w:style>'},
                {"default_extra": "<w:vanish w:val='true'/>"})):
            with self.subTest(options=options):
                source = self.document(f"source-{index}.docx", '<w:p><w:r><w:t>Source.</w:t></w:r></w:p>', **options)
                destination = self.work / f"out-{index}.docx"
                result = self.run_script("scripts/make_template.py", source, destination)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("inherited visibility", result.stdout)
                self.assertFalse(destination.exists())

    def test_visible_default_does_not_block_cleanup(self):
        source = self.document("source.docx", '<w:p><w:r><w:t>Visible.</w:t></w:r></w:p>', default_extra='<w:vanish w:val="off"/>')
        result = self.run_script("scripts/make_template.py", source, self.work / "clean.docx")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_cleanup_also_removes_direct_hidden_header_runs(self):
        header = '<w:p><w:r><w:t>House heading.</w:t></w:r><w:r><w:rPr><w:vanish w:val=\'true\'/></w:rPr><w:t>PRIVATE_HEADER</w:t></w:r></w:p>'
        source = self.document("source.docx", '<w:p><w:r><w:t>Body.</w:t></w:r></w:p>', header=header)
        destination = self.work / "clean.docx"
        result = self.run_script("scripts/make_template.py", source, destination)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("House heading.", self.xml(destination, "word/header1.xml"))
        self.assertNotIn("PRIVATE_HEADER", self.xml(destination, "word/header1.xml"))

    def test_direct_font_change_returns_difference(self):
        a = self.document("a.docx", '<w:p><w:r><w:rPr><w:sz w:val="24"/></w:rPr><w:t>Same.</w:t></w:r></w:p>')
        b = self.document("b.docx", '<w:p><w:r><w:rPr><w:sz w:val="60"/></w:rPr><w:t>Same.</w:t></w:r></w:p>')
        result = self.run_script("scripts/inspect_docx.py", "--compare", a, b)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("DIFFERENT", result.stdout)
        self.assertNotIn("signatures match", result.stdout)

    def test_default_font_change_returns_difference(self):
        body = '<w:p><w:r><w:t>Same.</w:t></w:r></w:p>'
        a, b = self.document("a.docx", body), self.document("b.docx", body, default_size=60)
        self.assertEqual(self.run_script("scripts/inspect_docx.py", "--compare", a, b).returncode, 1)

    def test_same_document_passes_declared_comparison(self):
        source = self.document("source.docx", '<w:p><w:r><w:t>Same.</w:t></w:r></w:p>')
        result = self.run_script("scripts/inspect_docx.py", "--compare", source, source)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("does not establish identical rendered pages", result.stdout)

    def test_style_used_in_only_one_document_is_reported(self):
        a = self.document("a.docx", '<w:p><w:r><w:t>Same.</w:t></w:r></w:p>')
        b = self.document("b.docx", '<w:p><w:pPr><w:pStyle w:val="NewStyle"/></w:pPr><w:r><w:t>Same.</w:t></w:r></w:p>',
                          style_extra='<w:style w:type="paragraph" w:styleId="NewStyle"><w:name w:val="New Style"/></w:style>')
        result = self.run_script("scripts/inspect_docx.py", "--compare", a, b)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("styles only in", result.stdout)

    def test_delivered_generator_works_beside_a_cleaned_template(self):
        source = self.document("source.docx", '<w:p><w:r><w:t>Dear Sample Client,</w:t></w:r></w:p>'
                               '<w:p><w:r><w:t>Original matter prose.</w:t></w:r></w:p>')
        package = self.work / "generated-skill"
        package.mkdir()
        edits = self.work / "edits.json"
        edits.write_text(json.dumps({
            "replace": {"Sample Client": "[Client name]"},
            "replace_paragraph": [{"containing": "Original matter prose.", "with": "[Advice: new-matter advice]"}],
            "insert_before": [{"before": "Dear Sample Client,", "text": "[NOTE] Use new-matter instructions.", "instruction": True}],
        }), encoding="utf-8")
        result = self.run_script("scripts/make_template.py", source, package / "template.docx", "--edits", edits)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        shutil.copy2(ROOT / "assets/create_docx.py", package / "create_docx.py")
        values = self.work / "values.json"
        values.write_text(json.dumps({"Client name": "New Client", "Advice": "This sentence is synthetic trial content."}), encoding="utf-8")
        output = self.work / "new-draft.docx"
        result = subprocess.run([sys.executable, "create_docx.py", str(values), str(output)],
                                cwd=package, capture_output=True, text=True, timeout=30,
                                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        text = self.xml(output)
        self.assertIn("Dear New Client,", text)
        self.assertIn("This sentence is synthetic trial content.", text)
        for removed in ("Sample Client", "Original matter prose", "[Advice", "[NOTE]"):
            self.assertNotIn(removed, text)

    def test_split_runs_choices_and_lists_still_work(self):
        template, values = self.fill_input()
        destination = self.work / "draft.docx"
        result = self.run_script("assets/create_docx.py", "--template", template, values, destination)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        text = self.xml(destination)
        for expected in ("Synthetic Client", "Alternative sentence.", "First entry", "Second entry"):
            self.assertIn(expected, text)
        for absent in ("[Client", "Optional sentence.", "[IF"):
            self.assertNotIn(absent, text)
        ET.fromstring(text)

    def test_missing_values_and_choices_stay_visible(self):
        template, values = self.fill_input()
        values.write_text("{}", encoding="utf-8")
        destination = self.work / "draft.docx"
        result = self.run_script("assets/create_docx.py", "--template", template, values, destination)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        text = self.xml(destination)
        self.assertIn("[IF optional]", text)
        self.assertIn('w:val="yellow"', text)
        self.assertIn("choices not made", result.stdout)

    def test_existing_draft_is_preserved_without_force(self):
        template, values = self.fill_input()
        destination = self.document("edited.docx", '<w:p><w:r><w:t>Edited draft.</w:t></w:r></w:p>')
        original = destination.read_bytes()
        result = self.run_script("assets/create_docx.py", "--template", template, values, destination)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(destination.read_bytes(), original)

    def test_force_replaces_output_with_complete_docx(self):
        template, values = self.fill_input()
        original_template = template.read_bytes()
        destination = self.document("edited.docx", '<w:p><w:r><w:t>Edited draft.</w:t></w:r></w:p>')
        result = self.run_script("assets/create_docx.py", "--force", "--template", template, values, destination)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Synthetic Client", self.xml(destination))
        self.assertEqual(template.read_bytes(), original_template)
        self.assertEqual(list(self.work.glob(".docx-*.tmp")), [])

    def test_force_never_replaces_template(self):
        template, values = self.fill_input()
        original = template.read_bytes()
        result = self.run_script("assets/create_docx.py", "--force", "--template", template, values, template)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(template.read_bytes(), original)

    def test_failed_zip_write_preserves_existing_output(self):
        destination = self.work / "edited.docx"
        destination.write_bytes(b"Pre-existing edited draft")
        with mock.patch.object(GENERATOR.zipfile.ZipFile, "writestr", side_effect=OSError("Synthetic disk failure")):
            with self.assertRaises(OSError):
                GENERATOR.write_docx({"[Content_Types].xml": b"test"}, destination, force=True)
        self.assertEqual(destination.read_bytes(), b"Pre-existing edited draft")
        self.assertEqual(list(self.work.glob(".docx-*.tmp")), [])

    def test_publish_does_not_replace_a_late_existing_destination(self):
        destination = self.work / "edited.docx"
        destination.write_bytes(b"Created after an initial check")
        with self.assertRaises(FileExistsError):
            GENERATOR.write_docx({"[Content_Types].xml": b"test"}, destination)
        self.assertEqual(destination.read_bytes(), b"Created after an initial check")
        self.assertEqual(list(self.work.glob(".docx-*.tmp")), [])


if __name__ == "__main__":
    unittest.main()
