#!/usr/bin/env python3
"""Offline checks for the Comic Vine resolver, using real API payloads as fixtures."""
import tempfile
from pathlib import Path

import cover_sources as cs

FAILS = []


def check(label, got, want):
    if got != want:
        FAILS.append(f'{label}\n     got:  {got!r}\n     want: {want!r}')
        print(f'  FAIL  {label}')
    else:
        print(f'  ok    {label}')


print('\n-- filter sanitising (colons/commas break CV filter syntax) --')
check('colon stripped', cs.sanitize_filter_value('Green Lantern: Rebirth'), 'Green Lantern Rebirth')
check('comma stripped', cs.sanitize_filter_value('Hush, Vol. 1'), 'Hush Vol. 1')
check('apostrophe kept', cs.sanitize_filter_value("Kraven's Last Hunt"), "Kraven's Last Hunt")

print('\n-- title variants --')
check('arc name first', cs.title_variants('Green Lantern: Secret Origin'),
      ['Secret Origin', 'Green Lantern Secret Origin', 'Green Lantern'])
check('vol suffix dropped', cs.title_variants('Ultimate Spider-Man Vol. 1'),
      ['Ultimate Spider-Man'])

print('\n-- character variants --')
check('parenthetical dropped', cs.character_variants('Peni Parker (SP//dr)'),
      ['Peni Parker (SP//dr)', 'Peni Parker'])
check('slash split', cs.character_variants('Bart Allen / Impulse'),
      ['Bart Allen / Impulse', 'Bart Allen', 'Impulse'])
check('leading qualifier dropped', cs.character_variants('Flashpoint Barry Allen'),
      ['Flashpoint Barry Allen', 'Barry Allen'])

# Real payload from GET /characters/?filter=name:Hal Jordan — two different characters.
HAL = [
    {'id': 11202, 'name': 'Hal Jordan',
     'publisher': {'id': 10, 'name': 'DC Comics'},
     'image': {'super_url': 'https://comicvine.gamespot.com/a/uploads/scale_large/12/124259/9439462-gl.jpg'}},
    {'id': 105612, 'name': 'Hal Jordan',
     'publisher': {'id': 31, 'name': 'Marvel'},
     'image': {'super_url': 'https://comicvine.gamespot.com/a/uploads/scale_large/8/84205/3983652-hal.jpg'}},
]
KRAVEN = [
    {'id': 43327, 'name': '"Spider-Man" Kraven\'s Last Hunt',
     'image': {'super_url': 'https://comicvine.gamespot.com/a/uploads/scale_large/0/2357/110025-kraven.jpg'}},
]


class FakeCV(cs.ComicVineClient):
    """Swaps the HTTP layer for canned payloads and records the filters used."""

    def __init__(self, payloads):
        self.cache = cs.ResolutionCache(path=Path(tempfile.mkdtemp()) / 'cache.json')
        self.verbose = False
        self.payloads = payloads
        self.seen = []
        self.calls = 0

    def _query(self, resource, name, limit=10):
        self.seen.append((resource, name))
        self.calls += 1
        return self.payloads.get(resource, [])


print('\n-- publisher disambiguation --')
cv = FakeCV({'characters': HAL})
got = cv.find_character('Hal Jordan', 'DC Comics')
check('picks the DC Hal Jordan', got.get('id'), 11202)
check('publisher recorded', got.get('publisher'), 'DC Comics')

cv = FakeCV({'characters': HAL})
check('hint flips to Marvel Hal Jordan',
      cv.find_character('Hal Jordan', 'Marvel').get('id'), 105612)

print('\n-- cover resolution --')
cv = FakeCV({'story_arcs': KRAVEN})
got = cv.find_cover("Kraven's Last Hunt", 'Marvel')
check('resolves despite title prefix', got.get('id'), 43327)
check('uses story_arcs first', cv.seen[0][0], 'story_arcs')

print('\n-- misses and budgets --')
cv = FakeCV({})
check('miss returns null url', cv.find_cover('Nonexistent Book', 'Marvel').get('url'), None)
check('cover query budget capped', cv.calls <= 4, True)

cv = FakeCV({})
cv.find_character('Some Unknown Person Here', 'Marvel')
check('character query budget capped', cv.calls <= 3, True)

print('\n-- caching --')
cv = FakeCV({'characters': HAL})
cv.find_character('Hal Jordan', 'DC Comics')
first = cv.calls
cv.find_character('Hal Jordan', 'DC Comics')
check('second lookup served from cache', cv.calls, first)

print()
if FAILS:
    print(f'{len(FAILS)} failure(s):\n')
    for f in FAILS:
        print(f'  - {f}')
    raise SystemExit(1)
print('All resolver checks passed.')
