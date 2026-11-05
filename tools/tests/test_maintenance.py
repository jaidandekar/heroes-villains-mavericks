"""Offline regression checks for maintenance write boundaries."""
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import generate_guides as guides
import refresh_screen_now as screen
import refresh_shop as shop


class MaintenanceSafetyTests(unittest.TestCase):
    def test_guide_check_never_writes(self):
        with patch.object(sys, 'argv', ['generate_guides.py', '--check']), patch.object(Path, 'write_text', side_effect=AssertionError('unexpected write')), contextlib.redirect_stdout(io.StringIO()):
            guides.main()

    def test_guide_check_detects_stale_output(self):
        pack = guides.ALL_GENERATED_PACKS[0]
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(guides, 'ROOT', Path(directory)), patch.object(guides, 'ALL_GENERATED_PACKS', [pack]), patch.object(sys, 'argv', ['generate_guides.py', '--check']), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaisesRegex(SystemExit, 'Generated guides differ'):
                    guides.main()

    def test_generation_writes_inventory_inside_tools(self):
        pack = guides.ALL_GENERATED_PACKS[0]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(guides, 'ROOT', root), patch.object(guides, 'TOOLS', root), patch.object(guides, 'ALL_GENERATED_PACKS', [pack]), patch.object(sys, 'argv', ['generate_guides.py']), contextlib.redirect_stdout(io.StringIO()):
                guides.main()
            self.assertTrue((root / (pack['id'] + '-guide') / 'index.html').exists())
            self.assertIn(pack['brand'], (root / 'GENERATED.md').read_text())

    def run_screen_refresh(self, directory, dry_run):
        root = Path(directory)
        slate = root / 'slate.json'
        slate.write_text(json.dumps({'titles': []}))
        paths = {name: root / name for name in ['CACHE_PATH', 'SHOP_SECTIONS_PATH', 'OUT_PATH', 'INDEX_PATH']}
        for path in paths.values():
            path.write_text('original')
        argv = ['refresh_screen_now.py', '--as-of', '2026-11-03'] + (['--dry-run'] if dry_run else [])
        with contextlib.ExitStack() as stack:
            for name, value in paths.items():
                stack.enter_context(patch.object(screen, name, value))
            stack.enter_context(patch.object(screen, 'SLATE_PATH', slate))
            stack.enter_context(patch.object(screen, 'load_config', return_value={'tmdb': {'api_key': 'test'}}))
            stack.enter_context(patch.object(screen, 'load_tmdb_cache', return_value={'fixture': True}))
            stack.enter_context(patch.object(shop, 'load_json', return_value={}))
            stack.enter_context(patch.object(shop, 'render_all', return_value='<section>fixture</section>'))
            stack.enter_context(patch.object(sys, 'argv', argv))
            stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            if dry_run:
                stack.enter_context(patch.object(Path, 'write_text', side_effect=AssertionError('unexpected dry-run write')))
            screen.main()
        return paths

    def test_screen_dry_run_never_writes_any_output(self):
        with tempfile.TemporaryDirectory() as directory:
            paths = self.run_screen_refresh(directory, True)
            self.assertTrue(all(path.read_text() == 'original' for path in paths.values()))

    def test_screen_refresh_persists_consistent_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            paths = self.run_screen_refresh(directory, False)
            page = paths['OUT_PATH'].read_text()
            self.assertEqual(page, paths['INDEX_PATH'].read_text())
            self.assertIn('<section>fixture</section>', page)
            self.assertEqual(json.loads(paths['CACHE_PATH'].read_text()), {'fixture': True})
            self.assertEqual(paths['SHOP_SECTIONS_PATH'].read_text(), '<section>fixture</section>')


if __name__ == '__main__':
    unittest.main()
