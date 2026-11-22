"""Unit tests for the CampusNotes note storage workflow."""

import json
import tempfile
import unittest
from pathlib import Path

from src.campusnotes import add_note, find_notes, load_notes


class CampusNotesTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.store = Path(self.temporary_directory.name) / "notes.json"

    def tearDown(self):
        self.temporary_directory.cleanup()

    def test_add_note_persists_trimmed_content(self):
        note = add_note("  Operating Systems  ", "  Revise scheduling  ", self.store)
        self.assertEqual(note["title"], "Operating Systems")
        self.assertEqual(note["body"], "Revise scheduling")
        self.assertEqual(load_notes(self.store), [note])

    def test_blank_title_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "title cannot be empty"):
            add_note("   ", "A body", self.store)

    def test_blank_body_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "body cannot be empty"):
            add_note("A title", "  ", self.store)

    def test_search_matches_title_and_body_case_insensitively(self):
        add_note("Database Systems", "Practice SQL joins", self.store)
        self.assertEqual(len(find_notes("database", self.store)), 1)
        self.assertEqual(len(find_notes("SQL", self.store)), 1)
        self.assertEqual(find_notes("networking", self.store), [])

    def test_invalid_json_shape_is_rejected(self):
        self.store.write_text(json.dumps({"not": "a list"}), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "JSON list"):
            load_notes(self.store)


if __name__ == "__main__":
    unittest.main()
