#!/usr/bin/env python3
"""Apply tools/character_art.json to the homepage character tiles.

Each slug owns one image URL. The script refuses to write a file that uses
the same image for two people. Add a character by adding one record to the
JSON, then run this script.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
REPO = TOOLS.parent
ART = TOOLS / 'character_art.json'
PAGES = [
    REPO / 'site' / 'index.html',
    REPO / 'site' / 'heroesvillainsmavericks.html',
]


def load_art() -> list[dict]:
    data = json.loads(ART.read_text(encoding='utf-8'))
    characters = data['characters']
    srcs = [c['src'] for c in characters]
    dupes = sorted({src for src in srcs if srcs.count(src) > 1})
    if dupes:
        raise SystemExit('Duplicate character images:\n' + '\n'.join(dupes))
    slugs = [c['slug'] for c in characters]
    if len(slugs) != len(set(slugs)):
        raise SystemExit('Duplicate character slugs')
    return characters


def patch(html: str, characters: list[dict]) -> str:
    missing = []
    for character in characters:
        slug = character['slug']
        src = character['src']
        position = character.get('position')
        style = f' style="object-position: {position}"' if position else ''
        pattern = (
            rf'(href="{re.escape(slug)}-guide/index\.html">\s*'
            rf'<img class="character-card-art" src=")[^"]+"'
            rf'(?: style="object-position:[^"]*")?'
        )
        html, count = re.subn(pattern, rf'\g<1>{src}"{style}', html, count=1)
        if count != 1:
            missing.append(slug)
    if missing:
        raise SystemExit('Character cards not found: ' + ', '.join(missing))
    return html


def main() -> None:
    characters = load_art()
    for page in PAGES:
        updated = patch(page.read_text(encoding='utf-8'), characters)
        page.write_text(updated, encoding='utf-8')
        print(f'{page.name}: {len(characters)} tiles')


if __name__ == '__main__':
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
