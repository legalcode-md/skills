"""Exercise publication failures that break independently installed skills."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "scripts/validate-public-skills.py")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class PackageIntegrityTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.name = "legalcode-example"
        self.path = "skills/general/legal-research/" + self.name
        directory = self.root / self.path
        (directory / "references").mkdir(parents=True)
        license_text = (ROOT / "LICENSE.md").read_bytes()
        (self.root / "LICENSE.md").write_bytes(license_text)
        (directory / "LICENSE.md").write_bytes(license_text)
        (directory / "SKILL.md").write_text(
            "---\nname: legalcode-example\ndescription: Check example sources.\n"
            "license: Legalcode Skills Source-Available License 1.0; see LICENSE.md\n---\n"
            "Read [requirements](references/runtime-compatibility.md).\n"
        )
        (directory / "references/runtime-compatibility.md").write_text("Fetch the source before relying on it.\n")
        self.entry = {"name": self.name, "path": self.path, "practice_area": "legal-research", "jurisdiction": None,
                      "files": {str(p.relative_to(directory)): hashlib.sha256(p.read_bytes()).hexdigest()
                                for p in directory.rglob("*") if p.is_file()}}
        (self.root / "catalog.json").write_text(json.dumps({"total_count": 1, "practice_areas": {"legal-research": {}}, "skills": [self.entry]}))
        (self.root / "collection-coverage.json").write_text(json.dumps({
            "total_count": 1, "definition_count": 1, "unique_collection_names": 1,
            "definitions": [{"published_name": self.name}], "preserved_public_workflows": [],
            "previous_published_count": 0, "new_skill_names": [self.name]}))
        (self.root / "CATALOG.md").write_text("[Research](catalog/practice-areas/legal-research.md)\n")
        self.area_page = self.root / "catalog/practice-areas/legal-research.md"
        self.area_page.parent.mkdir(parents=True)
        self.area_page.write_text(f"[Example](../../{self.path}/SKILL.md)\n")

    def validate(self):
        with contextlib.redirect_stdout(io.StringIO()):
            VALIDATOR.validate(self.root)

    def test_nested_individual_package_is_valid(self):
        self.validate()

    def test_missing_support_file_is_rejected(self):
        (self.root / self.path / "references/runtime-compatibility.md").unlink()
        with self.assertRaises(AssertionError):
            self.validate()

    def test_modified_package_is_rejected(self):
        (self.root / self.path / "references/runtime-compatibility.md").write_text("Changed without review.")
        with self.assertRaisesRegex(SystemExit, "Hash mismatch"):
            self.validate()

    def test_broken_category_link_is_rejected(self):
        self.area_page.write_text(f"[Example](../../skills/missing/{self.name}/SKILL.md)\n")
        with self.assertRaisesRegex(SystemExit, "Broken navigation link"):
            self.validate()

    def test_missing_collection_skill_is_rejected(self):
        coverage = json.loads((self.root / "collection-coverage.json").read_text())
        coverage["definitions"].append({"published_name": "legalcode-missing"})
        coverage["definition_count"] += 1
        coverage["unique_collection_names"] += 1
        (self.root / "collection-coverage.json").write_text(json.dumps(coverage))
        with self.assertRaises(AssertionError):
            self.validate()


if __name__ == "__main__":
    unittest.main()
