#!/usr/bin/env python3
"""One-off download of guide hero/header images.

Priority per guide:
  1. TMDB backdrop (wide, cinematic) when a title id is configured
  2. Wikipedia REST original image for the character/team page
  3. Comic Vine character art (last resort)

Writes to:
  <guide>/images/<header_img>

Usage:
  python3 refresh_heroes.py
  python3 refresh_heroes.py --force
  python3 refresh_heroes.py --only spiderman --verbose
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE_ROOT = HERE.parent / 'heroesvillainsmavericks'
ROOT = SITE_ROOT
sys.path.insert(0, str(HERE))

from cover_sources import (  # noqa: E402
    ComicVineClient,
    ConfigError,
    ResolutionCache,
    download_image,
    key_is_placeholder,
    load_config,
    local_image_ok,
)
from generate_guides import ALL_GENERATED_PACKS  # noqa: E402

TMDB_BASE = 'https://api.themoviedb.org/3'
TMDB_BACKDROP = 'https://image.tmdb.org/t/p/w1280'
WIKI_SUMMARY = 'https://en.wikipedia.org/api/rest_v1/page/summary/{title}'

# Prefer wide screen key art when the guide is tied to something currently on Screen Now.
TMDB_HERO = {
    'green-lantern': ('tv', 95350),          # Lanterns
    'spiderman': ('movie', 969681),          # Brand New Day
    'supergirl': ('movie', 1081003),         # Supergirl (2026)
    'clayface': ('movie', 1400940),          # Clayface
    'vision': ('tv', 213375),                # VisionQuest
    'x-men': ('tv', 138502),                 # X-Men '97
    'avengers': ('movie', 299534),           # Endgame (wide team shot)
    'doctor-doom': ('movie', 1003596),       # Avengers: Doomsday
}


def wiki_title_from_url(url: str | None) -> str | None:
    if not url:
        return None
    m = re.search(r'/wiki/([^?#]+)', url)
    if not m:
        return None
    return urllib.parse.unquote(m.group(1))


def http_json(url: str, user_agent: str, timeout: int = 25) -> dict | None:
    req = urllib.request.Request(url, headers={
        'User-Agent': user_agent,
        'Accept': 'application/json',
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, json.JSONDecodeError):
        return None


def tmdb_backdrop(kind: str, tmdb_id: int, api_key: str, user_agent: str) -> str | None:
    endpoint = 'tv' if kind == 'tv' else 'movie'
    url = f'{TMDB_BASE}/{endpoint}/{tmdb_id}?api_key={urllib.parse.quote(api_key)}'
    data = http_json(url, user_agent)
    path = (data or {}).get('backdrop_path')
    if not path:
        return None
    return TMDB_BACKDROP + path


def wikipedia_hero(wiki_url: str | None, user_agent: str) -> str | None:
    title = wiki_title_from_url(wiki_url)
    if not title:
        return None
    url = WIKI_SUMMARY.format(title=urllib.parse.quote(title, safe=''))
    data = http_json(url, user_agent)
    if not data:
        return None
    original = (data.get('originalimage') or {}).get('source')
    thumb = (data.get('thumbnail') or {}).get('source')
    return original or thumb


def comicvine_hero(name: str, publisher: str, client: ComicVineClient | None) -> str | None:
    if client is None:
        return None
    hit = client.find_character(name, publisher)
    return (hit or {}).get('url')


def publisher_for(pack_id: str) -> str:
    if pack_id in {'green-lantern', 'supergirl', 'clayface'}:
        return 'DC Comics'
    return 'Marvel'


def resolve_candidates(pack: dict, cfg: dict, comicvine: ComicVineClient | None) -> list[tuple[str, str]]:
    """Ordered (source, url) candidates for a guide hero."""
    out: list[tuple[str, str]] = []
    ua = cfg['user_agent']
    tmdb_key = (cfg.get('tmdb') or {}).get('api_key')
    pack_id = pack['id']

    if not key_is_placeholder(tmdb_key) and pack_id in TMDB_HERO:
        kind, tid = TMDB_HERO[pack_id]
        url = tmdb_backdrop(kind, tid, tmdb_key, ua)
        if url:
            out.append(('tmdb', url))

    wiki = wikipedia_hero((pack.get('profile') or {}).get('wikipedia'), ua)
    if wiki:
        out.append(('wikipedia', wiki))

    cv = comicvine_hero(pack.get('brand') or pack_id, publisher_for(pack_id), comicvine)
    if cv:
        out.append(('comicvine', cv))

    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--only', action='append', help='Guide id (repeatable)')
    parser.add_argument('--force', action='store_true', help='Re-download even if a healthy file exists')
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()

    packs = ALL_GENERATED_PACKS
    if args.only:
        wanted = set(args.only)
        packs = [p for p in packs if p['id'] in wanted]
        missing = wanted - {p['id'] for p in packs}
        if missing:
            print(f'Unknown guide id(s): {", ".join(sorted(missing))}', file=sys.stderr)
            return 2

    try:
        cfg = load_config()
    except ConfigError as exc:
        print(exc, file=sys.stderr)
        return 2

    ua = cfg['user_agent']
    cv_key = (cfg.get('comicvine') or {}).get('api_key')
    cache = ResolutionCache()
    comicvine = None if key_is_placeholder(cv_key) else ComicVineClient(cv_key, ua, cache, args.verbose)

    ok = failed = skipped = 0
    print(f'Hero refresh for {len(packs)} guide(s)\n')

    for pack in packs:
        dest = ROOT / f"{pack['id']}-guide" / 'images' / pack['header_img']
        dest.parent.mkdir(parents=True, exist_ok=True)

        if not args.force and local_image_ok(dest, min_bytes=8000):
            skipped += 1
            print(f'  skip [{pack["id"]}] already have {dest.name} ({dest.stat().st_size} bytes)')
            continue

        candidates = resolve_candidates(pack, cfg, comicvine)
        if args.verbose:
            print(f'  [{pack["id"]}] candidates: ' + ', '.join(s for s, _ in candidates) or '(none)')

        won = None
        for source, url in candidates:
            # Wikimedia originals can be PNG/WebP; still fine as long as browsers load them.
            # Keep .jpg filename the guides already expect.
            if download_image(url, dest, ua, min_bytes=8000, referer='https://en.wikipedia.org/' if source == 'wikipedia' else None):
                won = source
                break
            if args.verbose:
                print(f'    · miss {source}')

        if won:
            ok += 1
            print(f'  ok  [{pack["id"]}] <- {won}: {dest.name} ({dest.stat().st_size} bytes)')
        else:
            failed += 1
            print(f'  !!  [{pack["id"]}] no hero image resolved')

    cache.save()
    print(f'\nDownloaded {ok} · skipped {skipped} · failed {failed}')
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    raise SystemExit(main())
