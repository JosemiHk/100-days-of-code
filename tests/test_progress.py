import copy
import tempfile
import unittest
from datetime import date
from pathlib import Path

from tools.progress import validate


class ProgressTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'evidence.txt').write_text('Observed result', encoding='utf-8')
        self.entry = dict(day=1, date='2026-11-03', summary='Implemented input validation',
                          learned='Why path containment matters', verification='Ran tests',
                          assistance='AI-assisted; manually inspected', evidence=['evidence.txt'])

    def check(self, entries):
        return validate(entries, self.root, date(2026, 11, 3))

    def test_empty_log_is_zero(self):
        self.assertEqual(self.check([]), 0)

    def test_valid_entry(self):
        self.assertEqual(self.check([self.entry]), 1)

    def test_duplicate_day_rejected(self):
        with self.assertRaises(ValueError):
            self.check([self.entry, copy.deepcopy(self.entry)])

    def test_future_date_rejected(self):
        self.entry['date'] = '2026-11-04'
        with self.assertRaises(ValueError):
            self.check([self.entry])

    def test_invalid_days_rejected(self):
        for day in (0, 101, True, '1'):
            with self.subTest(day=day), self.assertRaises(ValueError):
                self.check([dict(self.entry, day=day)])

    def test_missing_and_empty_evidence_rejected(self):
        (self.root / 'empty.txt').touch()
        for name in ('missing.txt', 'empty.txt'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.check([dict(self.entry, evidence=[name])])

    def test_external_path_rejected(self):
        for name in ('../outside.txt', str(self.root / 'evidence.txt')):
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.check([dict(self.entry, evidence=[name])])

    def test_required_reflection_rejected(self):
        with self.assertRaises(ValueError):
            self.check([dict(self.entry, learned=' ')])

    def test_malformed_structures_rejected(self):
        for entries in ({}, ['text'], [dict(self.entry, date=None)],
                        [dict(self.entry, evidence=[])], [dict(self.entry, evidence=[1])]):
            with self.subTest(entries=entries), self.assertRaises(ValueError):
                self.check(entries)


if __name__ == '__main__':
    unittest.main()
