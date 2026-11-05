"""Assemble the redesigned pages and the remaining legacy guides for Pages."""
import argparse
from html import escape
from html.parser import HTMLParser
import json
import re
from pathlib import Path
from posixpath import dirname, relpath
from shutil import copytree, ignore_patterns
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.references = []
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key == 'id':
                self.ids.add(value)
            if key in {'href', 'src'} and value:
                self.references.append(value)


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=root.parent)
    parser.add_argument('--public-url', required=True, help='Public HTTPS base URL for this Pages artifact')
    parser.add_argument('--output', type=Path, required=True, help='New output directory')
    args = parser.parse_args()
    public_url = urlsplit(args.public_url)
    if public_url.scheme != 'https' or not public_url.netloc or public_url.query or public_url.fragment:
        parser.error('--public-url must be an HTTPS base URL with no query or fragment')
    output = args.output.resolve()
    if output.exists():
        parser.error('--output must be a new directory')
    site = args.repo.resolve() / 'site'
    routes = json.loads((args.repo / 'tools/legacy_routes.json').read_text())
    guides = json.loads((root / 'src/data/guides.json').read_text())
    redesigned = ['index.html', *(f'{slug}-guide/index.html' for slug in guides)]
    for route in redesigned:
        if not (root / 'dist' / route).is_file():
            parser.error(f'Build the preview first. Missing {route}')

    redesigned_dirs = {site / f'{slug}-guide' for slug in guides}
    common_ignores = ignore_patterns('.DS_Store', '.git')

    def ignore_replaced_images(directory, names):
        ignored = common_ignores(directory, names)
        if Path(directory) in redesigned_dirs and 'images' in names:
            ignored.add('images')
        return ignored

    copytree(site, output, ignore=ignore_replaced_images)
    copytree(root / 'dist', output, dirs_exist_ok=True)
    for route in routes:
        file = output / route
        if not file.is_file():
            raise SystemExit(f'Missing legacy route: {route}')
        if route == 'heroesvillainsmavericks.html':
            continue
        suffix = route.removesuffix('index.html')
        canonical = escape(args.public_url.rstrip('/') + '/' + suffix, quote=True)
        html = file.read_text(encoding='utf-8')
        if route not in redesigned:
            # Retained routes get the same identity-only masthead as redesigned pages.
            html = re.sub(r'<a class="site-header-portfolio"[^>]*>.*?</a>', '', html, flags=re.S)
            html = re.sub(r'<div class="guide-bar">.*?</header>', '</header>', html, flags=re.S)

        html = html.replace('<meta name="robots" content="noindex">', '')
        html = html.replace('</head>', f'  <link rel="canonical" href="{canonical}">\n</head>', 1)
        file.write_text(html, encoding='utf-8')

    (output / 'heroesvillainsmavericks.html').write_bytes((output / 'index.html').read_bytes())
    # Preserve links from the original branch-based Pages layout under /site/.
    compatibility_routes = []
    for route in routes:
        alias = 'site/' + route
        destination = relpath(route, dirname(alias))
        canonical = args.public_url.rstrip('/') + '/' + route.removesuffix('index.html')
        redirect = (
            '<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Page moved | Heroes, Villains &amp; Mavericks</title>'
            + '<link rel="canonical" href="' + escape(canonical, quote=True) + '">'
            + '<meta http-equiv="refresh" content="0;url=' + escape(destination, quote=True) + '">'
            + '<script>location.replace(' + json.dumps(destination) + ' + location.search + location.hash);</script>'
            + '</head><body><a href="' + escape(destination, quote=True) + '">Continue to Heroes, Villains &amp; Mavericks</a></body></html>'
        )
        file = output / alias
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(redirect, encoding='utf-8')
        compatibility_routes.append(alias)
    pages = {route: Page(output / route) for route in [*routes, *compatibility_routes]}
    for slug, guide in guides.items():
        route = f'{slug}-guide/index.html'
        expected = {guide['who_id'], 'verses', 'all-versions', 'graphic-novels', 'on-screen'}
        expected.update('run/' + row['slug'] for row in guide['runs'])
        expected.update('version/' + row['slug'] for row in guide['versions'])
        if missing := expected - pages[route].ids:
            raise SystemExit(f'{route} is missing anchors: {sorted(missing)}')
    for route, page in pages.items():
        for value in page.references:
            url = urlsplit(value)
            if url.scheme or url.netloc:
                continue
            target = (output / route).parent / unquote(url.path) if url.path else output / route
            target = target.resolve()
            if target.is_dir():
                target /= 'index.html'
            if not target.is_relative_to(output) or not target.is_file():
                raise SystemExit(f'{route}: missing local reference {value}')
            if url.fragment and target.relative_to(output).as_posix() in redesigned:
                destination = pages[target.relative_to(output).as_posix()]
                if unquote(url.fragment) not in destination.ids:
                    raise SystemExit(f'{route}: missing local anchor {value}')
    print(f'Prepared {len(routes)} compatible routes plus {len(compatibility_routes)} /site/ redirects with {len(guides)} redesigned guides at {output}')


if __name__ == '__main__':
    main()
