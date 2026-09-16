#!/usr/bin/env python3
"""Smoke checks for the Speak Software skeleton (stdlib only).

The book is in development; these guard the invariants that already
hold — clean sources, series-standard licences, the boundary statement,
no staged content — and will grow as chapters are written.
"""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STALE_LINKS = (
    "michaelborck.dev",
    "michaelborck.education",
    "ship-it-python-in-production",
)


def skip_appledouble(paths):
    return [p for p in paths if not p.name.startswith("._")]


def qmd_files():
    return skip_appledouble(sorted(ROOT.glob("**/*.qmd")))


class ManuscriptChecks(unittest.TestCase):
    def test_all_configured_files_exist(self):
        import re
        config = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
        names = re.findall(r"^\s*-\s+(\S+\.qmd)\s*$", config, re.M)
        self.assertGreaterEqual(len(names), 22)
        for name in names:
            with self.subTest(file=name):
                self.assertTrue((ROOT / name).is_file(), name)

    def test_licence_files_present_and_adapted(self):
        for name in ("LICENSE", "LICENSE-CONTENT.md", "LICENSE-CODE.md"):
            with self.subTest(file=name):
                self.assertTrue((ROOT / name).is_file(), name)
        licence = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Speak Software", licence)
        self.assertNotIn("Absolute Minimum", licence)
        legal = (ROOT / "LICENSE-CONTENT.md").read_text(encoding="utf-8")
        self.assertIn("Attribution 4.0 International", legal)

    def test_boundary_statement_present(self):
        text = (ROOT / "index.qmd").read_text(encoding="utf-8")
        for marker in ("not a Python book",
                       "mini CEO",
                       "Converse Python, Partner AI"):
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_sources_are_clean(self):
        for path in qmd_files():
            text = path.read_text(encoding="utf-8")
            with self.subTest(file=str(path)):
                self.assertNotIn("{mermaid}", text)
                for target in STALE_LINKS:
                    self.assertNotIn(target, text)
                path.read_text(encoding="utf-8")  # utf-8 decodable

    def test_prospectus_exists(self):
        prospectus = (ROOT / "PROSPECTUS.md").read_text(encoding="utf-8")
        self.assertIn("mini CEO", prospectus)
        self.assertIn("Slop in the Supply Chain", prospectus)


if __name__ == "__main__":
    unittest.main(verbosity=2)
