"""Keep real package references distinct from examples of generated files."""
import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location("validator", Path(__file__).resolve().parents[1] / "validate-public-skills.py")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ReferenceLinksTest(unittest.TestCase):
    def test_template_example_does_not_require_generated_files_in_builder(self):
        text = "[Method](references/method.md)\n```markdown\n[Output](references/output.md)\n```\n[Checks](references/checks.md)"
        self.assertEqual(VALIDATOR.prose_links(text), [("Method", "references/method.md"), ("Checks", "references/checks.md")])

    def test_regular_missing_link_remains_available_for_validation(self):
        self.assertEqual(VALIDATOR.prose_links("Read [missing](missing.md)."), [("missing", "missing.md")])

    def test_inner_shorter_fence_does_not_end_outer_example(self):
        text = "````markdown\n```text\n[Example](output.md)\n```\n````\n[Real](real.md)"
        self.assertEqual(VALIDATOR.prose_links(text), [("Real", "real.md")])

    def test_tilde_examples_are_also_ignored(self):
        text = "~~~markdown\n[Example](output.md)\n~~~\n[Real](real.md)"
        self.assertEqual(VALIDATOR.prose_links(text), [("Real", "real.md")])


if __name__ == "__main__":
    unittest.main()
