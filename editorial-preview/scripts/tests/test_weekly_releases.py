import copy
import importlib.util
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('weekly', ROOT / 'scripts/check-weekly-releases.py')
weekly = importlib.util.module_from_spec(spec)
spec.loader.exec_module(weekly)

class WeeklyReleaseTests(unittest.TestCase):
    def setUp(self):
        self.batch = json.loads((ROOT / 'src/data/weekly-releases.json').read_text())
    def test_verified_edition_is_valid(self):
        self.assertEqual(weekly.validate(self.batch, ROOT, self.batch['verifiedOn']), len(self.batch['entries']))
    def test_wrong_week_and_future_releases_fail(self):
        for wrong in ['2026-11-03', '2026-11-16']:
            with self.subTest(wrong=wrong):
                changed = copy.deepcopy(self.batch)
                changed['entries'][0]['releaseDate'] = wrong
                with self.assertRaises(ValueError): weekly.validate(changed, ROOT)
    def test_duplicates_and_unknown_guides_fail(self):
        self.batch['entries'].append(copy.deepcopy(self.batch['entries'][0]))
        with self.assertRaises(ValueError): weekly.validate(self.batch, ROOT)
        self.batch['entries'].pop()
        self.batch['entries'][0]['guideIds'] = ['nonexistent']
        with self.assertRaises(ValueError): weekly.validate(self.batch, ROOT)
    def test_untrusted_source_and_missing_cover_fail(self):
        self.batch['entries'][0]['source'] = 'https://unverified.example/item'
        with self.assertRaises(ValueError): weekly.validate(self.batch, ROOT)
        self.setUp()
        self.batch['entries'][0]['cover'] = 'media/weekly/not-found.jpg'
        with self.assertRaises(ValueError): weekly.validate(self.batch, ROOT)
    def test_stale_edition_can_build_but_cannot_publish_as_fresh(self):
        weekly.validate(self.batch, ROOT)
        with self.assertRaises(ValueError): weekly.validate(self.batch, ROOT, '2026-11-18')
    def test_publish_scope_rejects_unfinished_design_and_code(self):
        allowed = [weekly.DATA_PATH, weekly.MARKER_PATH, 'editorial-preview/public/media/weekly/test.jpg']
        weekly.validate_scope(allowed)
        for path in ['editorial-preview/src/pages/index.astro', '.github/workflows/deploy-pages.yml', 'editorial-preview/public/media/weekly/../other.jpg']:
            with self.subTest(path=path), self.assertRaises(ValueError): weekly.validate_scope(allowed + [path])

if __name__ == '__main__': unittest.main()
