#!/usr/bin/env python3
"""Check legacy routes, static local references, and guide regeneration offline."""
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import sys
from urllib.parse import unquote, urlsplit

TOOLS = Path(__file__).resolve().parent
SITE = TOOLS.parent / 'site'


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        self.urls.extend(value for key, value in attrs if key in {'href', 'src'} and value)


def main():
    routes = json.loads((TOOLS / 'legacy_routes.json').read_text(encoding='utf-8'))
    pages = sorted(SITE.rglob('*.html'))
    failures = [f'Missing legacy route: {route}' for route in routes if not (SITE / route).is_file()]
    home, alias = SITE / 'index.html', SITE / 'heroesvillainsmavericks.html'
    if home.is_file() and alias.is_file() and home.read_bytes() != alias.read_bytes():
        failures.append('The two legacy homepages differ.')
    for page in pages:
        references = References()
        references.feed(page.read_text(encoding='utf-8'))
        for value in references.urls:
            url = urlsplit(value)
            if url.scheme or url.netloc or not url.path:
                continue
            path = unquote(url.path)
            target = ((SITE / path.lstrip('/')) if path.startswith('/') else (page.parent / path)).resolve()
            if not target.is_relative_to(SITE):
                failures.append(f'{page.relative_to(SITE)}: local reference leaves the publish folder: {value}')
                continue
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                failures.append(f'{page.relative_to(SITE)}: missing local reference {value}')
    if failures:
        raise SystemExit('\n'.join(failures))
    print(f'Checked {len(routes)} legacy routes and static local references in {len(pages)} pages.', flush=True)
    subprocess.run([sys.executable, '-B', str(TOOLS / 'generate_guides.py'), '--check'], check=True)


if __name__ == '__main__':
    main()
