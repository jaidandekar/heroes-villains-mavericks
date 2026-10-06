#!/usr/bin/env python3
"""Backfill local cover art for every generated character guide.

Downloads land in the exact paths the guides already check first:

    <char>-guide/images/covers/runs/<runSlug>.jpg
    <char>-guide/images/covers/versions/<versionSlug>.jpg
    <char>-guide/images/covers/screen/<screenId>.jpg

so no HTML changes are needed for the images to appear.

Cover cascade (runs):
    Open Library (ISBN) → Amazon (ASIN) → Google Books → Comic Vine

Versions:
    Wikipedia (article image) → Google Books (title) → Comic Vine

Screen:
    TMDB (unchanged)

Usage:
    python3 refresh_covers.py                    # everything
    python3 refresh_covers.py --only flash       # a single guide
    python3 refresh_covers.py --kind screen      # posters only
    python3 refresh_covers.py --dry-run          # plan without calling APIs
    python3 refresh_covers.py --force            # re-fetch existing files
    python3 refresh_covers.py --limit 50         # cap downloads this run
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from attribution import ensure_attribution
from cover_sources import (
    ComicVineClient,
    ConfigError,
    GoogleBooksClient,
    RateLimitExceeded,
    ResolutionCache,
    TmdbClient,
    collect_run_cover_candidates,
    collect_version_cover_candidates,
    download_image,
    key_is_placeholder,
    load_config,
    local_image_ok,
)
from generate_guides import ALL_GENERATED_PACKS, ROOT

KINDS = ('runs', 'versions', 'screen')

DC_IDS = {'green-lantern', 'supergirl', 'clayface'}
IMAGE_IDS = set()


def publisher_hint(pack_id: str) -> str:
    if pack_id in DC_IDS:
        return 'DC Comics'
    if pack_id in IMAGE_IDS:
        return 'Image Comics'
    return 'Marvel'


def guide_dir(pack_id: str) -> Path:
    return ROOT / f'{pack_id}-guide'


def run_identifiers(run: dict) -> tuple[str | None, str | None]:
    isbn = run.get('isbn')
    amazon = run.get('amazon') or []
    asin = None
    if amazon and isinstance(amazon[0], dict):
        asin = amazon[0].get('asin')
    return isbn, asin


def plan_targets(pack: dict, kinds: tuple[str, ...]) -> list[dict]:
    """Build the list of images this guide wants, independent of any API."""
    base = guide_dir(pack['id']) / 'images' / 'covers'
    targets: list[dict] = []

    if 'runs' in kinds:
        for slug, run in pack['runs'].items():
            isbn, asin = run_identifiers(run)
            targets.append({
                'kind': 'runs',
                'slug': slug,
                'query': run['title'],
                'isbn': isbn,
                'asin': asin,
                'dest': base / 'runs' / f'{slug}.jpg',
            })

    if 'versions' in kinds:
        for version in pack['versions']:
            targets.append({
                'kind': 'versions',
                'slug': version['slug'],
                'query': version['name'],
                'wikipedia': version.get('wikipedia'),
                'dest': base / 'versions' / f'{version["slug"]}.jpg',
            })

    if 'screen' in kinds:
        for group in pack['screen']:
            for item in group['items']:
                targets.append({
                    'kind': 'screen',
                    'slug': item['id'],
                    'query': item['title'],
                    'item': item,
                    'dest': base / 'screen' / f'{item["id"]}.jpg',
                })

    return targets


def needs_fetch(dest: Path, force: bool) -> bool:
    if force:
        return True
    return not local_image_ok(dest)


def try_download_candidates(candidates: list[dict], dest: Path, user_agent: str, verbose: bool) -> dict | None:
    for cand in candidates:
        url = cand.get('url')
        if not url:
            continue
        if download_image(url, dest, user_agent, referer=cand.get('referer')):
            return cand
        if verbose:
            print(f'    · miss {cand.get("source")}: download failed')
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--only', action='append', help='Guide id (repeatable), e.g. --only flash')
    parser.add_argument('--kind', choices=KINDS, action='append', help='Limit to one kind (repeatable)')
    parser.add_argument('--dry-run', action='store_true', help='Show the plan without calling any API')
    parser.add_argument('--force', action='store_true', help='Re-download files that already exist')
    parser.add_argument('--limit', type=int, default=0, help='Stop after N successful downloads')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--skip-attribution', action='store_true', help='Do not touch guide HTML')
    args = parser.parse_args()

    kinds = tuple(args.kind) if args.kind else KINDS
    packs = ALL_GENERATED_PACKS
    if args.only:
        wanted = set(args.only)
        packs = [p for p in packs if p['id'] in wanted]
        missing = wanted - {p['id'] for p in packs}
        if missing:
            print(f'Unknown guide id(s): {", ".join(sorted(missing))}', file=sys.stderr)
            return 2
    if not packs:
        print('No guides selected.', file=sys.stderr)
        return 2

    # ── Plan ──
    all_targets: list[tuple[dict, dict]] = []
    for pack in packs:
        for target in plan_targets(pack, kinds):
            all_targets.append((pack, target))

    pending = [(p, t) for p, t in all_targets if needs_fetch(t['dest'], args.force)]
    have = len(all_targets) - len(pending)
    broken = sum(1 for _, t in pending if t['dest'].exists() and not local_image_ok(t['dest']) and not args.force)

    print(f'Guides:  {len(packs)}')
    print(f'Targets: {len(all_targets)} ({have} healthy on disk, {len(pending)} to fetch'
          + (f', including {broken} tiny/corrupt' if broken else '') + ')')
    by_kind: dict[str, int] = {}
    for _, t in pending:
        by_kind[t['kind']] = by_kind.get(t['kind'], 0) + 1
    for kind in KINDS:
        if by_kind.get(kind):
            print(f'  {kind:9s} {by_kind[kind]}')

    if args.dry_run:
        print('\nDry run — no API calls made.')
        for pack, t in pending[:15]:
            extra = ''
            if t['kind'] == 'runs':
                bits = []
                if t.get('isbn'):
                    bits.append(f'isbn={t["isbn"]}')
                if t.get('asin'):
                    bits.append(f'asin={t["asin"]}')
                if bits:
                    extra = '  (' + ', '.join(bits) + ')'
            print(f'  [{pack["id"]}] {t["kind"]}/{t["slug"]}  <- "{t["query"]}"{extra}')
        if len(pending) > 15:
            print(f'  ... and {len(pending) - 15} more')
        return 0

    if not pending:
        print('\nNothing to fetch.')
        return 0

    # ── Clients ──
    try:
        cfg = load_config()
    except ConfigError as exc:
        print(f'\n{exc}', file=sys.stderr)
        return 2

    ua = cfg['user_agent']
    cv_key = (cfg.get('comicvine') or {}).get('api_key')
    tmdb_key = (cfg.get('tmdb') or {}).get('api_key')
    gbooks_key = (cfg.get('google_books') or {}).get('api_key')

    cache = ResolutionCache()
    comicvine = None if key_is_placeholder(cv_key) else ComicVineClient(cv_key, ua, cache, args.verbose)
    tmdb = None if key_is_placeholder(tmdb_key) else TmdbClient(tmdb_key, ua, cache, args.verbose)
    google = GoogleBooksClient(
        ua,
        cache,
        api_key=None if key_is_placeholder(gbooks_key) else gbooks_key,
        verbose=args.verbose,
    )

    print('\nSources: Open Library · Amazon · Google Books'
          + (' · Comic Vine' if comicvine else ' (Comic Vine key missing)')
          + (' · TMDB' if tmdb else ' (TMDB key missing)'))

    needs_comic = any(t['kind'] in ('runs', 'versions') for _, t in pending)
    needs_screen = any(t['kind'] == 'screen' for _, t in pending)
    if needs_screen and tmdb is None:
        print('TMDB key not set — skipping film and TV posters.')
    if needs_comic and comicvine is None:
        print('Comic Vine key not set — runs/versions will still try Open Library / Amazon / Google Books.')

    # ── Fetch ──
    downloaded = unresolved = failed = 0
    by_source: dict[str, int] = {}
    print()

    try:
        for pack, target in pending:
            if args.limit and downloaded >= args.limit:
                print(f'\nReached --limit {args.limit}.')
                break

            kind, slug = target['kind'], target['slug']
            hint = publisher_hint(pack['id'])
            won = None

            if kind == 'screen':
                if tmdb is None:
                    continue
                resolved = tmdb.find_poster(target['item'])
                url = (resolved or {}).get('url')
                if url and download_image(url, target['dest'], ua):
                    won = {
                        'source': 'tmdb',
                        'name': (resolved or {}).get('name') or target['query'],
                    }
                elif not url:
                    unresolved += 1
                    if args.verbose:
                        print(f'  ?  [{pack["id"]}] {kind}/{slug} — no match for "{target["query"]}"')
                    continue
                else:
                    failed += 1
                    print(f'  !! [{pack["id"]}] {kind}/{slug} — download failed')
                    continue
            elif kind == 'runs':
                # Prefer key-free CDNs first; only hit APIs if those miss.
                candidates = collect_run_cover_candidates(
                    title=target['query'],
                    isbn=target.get('isbn'),
                    asin=target.get('asin'),
                )
                api_candidates: list[dict] = []
                won = try_download_candidates(candidates, target['dest'], ua, args.verbose)
                if not won:
                    api_candidates = collect_run_cover_candidates(
                        title=target['query'],
                        isbn=target.get('isbn'),
                        asin=target.get('asin'),
                        google=google,
                        comicvine=comicvine,
                        publisher_hint=hint,
                        include_api=True,
                    )
                    won = try_download_candidates(api_candidates, target['dest'], ua, args.verbose)
                if not won:
                    if not candidates and not api_candidates:
                        unresolved += 1
                        if args.verbose:
                            print(f'  ?  [{pack["id"]}] {kind}/{slug} — no candidates for "{target["query"]}"')
                    else:
                        failed += 1
                        print(f'  !! [{pack["id"]}] {kind}/{slug} — all sources failed')
                    continue
            else:  # versions
                candidates = collect_version_cover_candidates(
                    name=target['query'],
                    google=google,
                    comicvine=comicvine,
                    publisher_hint=hint,
                    wikipedia_url=target.get('wikipedia'),
                    user_agent=ua,
                )
                if not candidates:
                    unresolved += 1
                    if args.verbose:
                        print(f'  ?  [{pack["id"]}] {kind}/{slug} — no candidates for "{target["query"]}"')
                    continue
                won = try_download_candidates(candidates, target['dest'], ua, args.verbose)
                if not won:
                    failed += 1
                    print(f'  !! [{pack["id"]}] {kind}/{slug} — all sources failed')
                    continue

            downloaded += 1
            src = won.get('source', '?')
            by_source[src] = by_source.get(src, 0) + 1
            matched = won.get('name') or ''
            print(f'  ok [{pack["id"]}] {kind}/{slug}  <- {src}: {matched}')

    except RateLimitExceeded as exc:
        print(f'\nStopped: {exc}')
        print('Progress is cached — just re-run later to continue.')
    except KeyboardInterrupt:
        print('\nInterrupted.')
    finally:
        cache.save()

    # ── Attribution (required by Comic Vine / TMDB terms) ──
    if not args.skip_attribution:
        patched = 0
        for pack in packs:
            index = guide_dir(pack['id']) / 'index.html'
            if not index.exists():
                continue
            html = index.read_text(encoding='utf-8')
            updated = ensure_attribution(html)
            if updated != html:
                index.write_text(updated, encoding='utf-8')
                top = ROOT / f'{pack["id"]}-guide.html'
                if top.exists():
                    top.write_text(updated, encoding='utf-8')
                patched += 1
        if patched:
            print(f'\nAdded attribution footer to {patched} guide(s).')

    print(f'\nDownloaded {downloaded} · unresolved {unresolved} · failed {failed}')
    if by_source:
        print('By source: ' + ', '.join(f'{k}={v}' for k, v in sorted(by_source.items())))
    print(f'Google Books calls: {google.calls}')
    if comicvine:
        print(f'Comic Vine calls: {comicvine.calls}')
    if tmdb:
        print(f'TMDB calls: {tmdb.calls}')
    print(f'Cache entries: {len(cache)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
