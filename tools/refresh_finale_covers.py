#!/usr/bin/env python3
"""Download final-issue covers for Multiverse / version banners.

Writes:
    <guide>/images/covers/runs/<runSlug>-last.jpg

These are preferred over trade dress on Multiverse cards. Reading Order still
uses the regular <runSlug>.jpg trade cover.

Usage:
    python3 refresh_finale_covers.py --only vision
    python3 refresh_finale_covers.py --only vision --force
    python3 refresh_finale_covers.py --dry-run
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from cover_sources import (
    ComicVineClient,
    ConfigError,
    RateLimitExceeded,
    ResolutionCache,
    download_image,
    key_is_placeholder,
    load_config,
    local_image_ok,
    parse_finale_from_collects,
)
from generate_guides import ALL_GENERATED_PACKS, ROOT
from refresh_covers import DC_IDS, IMAGE_IDS, publisher_hint


def guide_dir(pack_id: str) -> Path:
    return ROOT / f'{pack_id}-guide'


def year_hint_for(run: dict) -> str:
    return str(run.get('years') or run.get('year') or '')


def plan_targets(pack: dict) -> list[dict]:
    base = guide_dir(pack['id']) / 'images' / 'covers' / 'runs'
    targets: list[dict] = []
    for slug, run in pack['runs'].items():
        finale = parse_finale_from_collects(run.get('collects') or '')
        if not finale:
            targets.append({
                'slug': slug,
                'title': run.get('title') or slug,
                'collects': run.get('collects') or '',
                'dest': base / f'{slug}-last.jpg',
                'skip_reason': 'no-issue-range',
                'finale': None,
                'years': year_hint_for(run),
            })
            continue
        targets.append({
            'slug': slug,
            'title': run.get('title') or slug,
            'collects': run.get('collects') or '',
            'dest': base / f'{slug}-last.jpg',
            'skip_reason': None,
            'finale': finale,
            'years': year_hint_for(run),
        })
    return targets


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--only', action='append', help='Guide id (repeatable)')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--force', action='store_true')
    parser.add_argument('--limit', type=int, default=0)
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

    all_targets: list[tuple[dict, dict]] = []
    for pack in packs:
        for target in plan_targets(pack):
            all_targets.append((pack, target))

    resolvable = [(p, t) for p, t in all_targets if not t['skip_reason']]
    skipped = [(p, t) for p, t in all_targets if t['skip_reason']]
    pending = [
        (p, t) for p, t in resolvable
        if args.force or not local_image_ok(t['dest'])
    ]

    print(f'Guides: {len(packs)}')
    print(f'Runs: {len(all_targets)} ({len(resolvable)} with issue ranges, {len(skipped)} skip)')
    print(f'To fetch: {len(pending)}')
    if args.dry_run:
        for pack, target in pending[:40]:
            fin = target['finale'] or {}
            print(f'  · {pack["id"]}/{target["slug"]}: {fin.get("series")} #{fin.get("issue")} ({target["collects"]})')
        if len(pending) > 40:
            print(f'  … {len(pending) - 40} more')
        for _, target in skipped[:12]:
            print(f'  – skip {target["slug"]}: {target["skip_reason"]} ({target["collects"]})')
        return 0

    try:
        cfg = load_config()
    except ConfigError as exc:
        print(exc, file=sys.stderr)
        return 2

    cv_key = (cfg.get('comicvine') or {}).get('api_key')
    if key_is_placeholder(cv_key):
        print('Comic Vine API key missing in config.json', file=sys.stderr)
        return 2

    cache = ResolutionCache()
    comicvine = ComicVineClient(cv_key, cfg['user_agent'], cache, verbose=args.verbose)
    downloaded = 0
    misses = 0

    try:
        for pack, target in pending:
            fin = target['finale']
            print(f'  {pack["id"]}/{target["slug"]}: {fin["series"]} #{fin["issue"]} …', end=' ', flush=True)
            try:
                hit = comicvine.find_last_issue_cover(
                    fin['series'],
                    fin['issue'],
                    year_hint=target['years'],
                    publisher_hint=publisher_hint(pack['id']),
                )
            except RateLimitExceeded as exc:
                print(f'RATE LIMIT ({exc})')
                break
            url = (hit or {}).get('url')
            if not url:
                print('miss')
                misses += 1
                continue
            target['dest'].parent.mkdir(parents=True, exist_ok=True)
            if download_image(url, target['dest'], cfg['user_agent'], referer='https://comicvine.gamespot.com/'):
                label = hit.get('issue_number') or fin['issue']
                print(f'OK (#{label} via {hit.get("volume")})')
                downloaded += 1
                if args.limit and downloaded >= args.limit:
                    break
            else:
                print('download-failed')
                misses += 1
    finally:
        cache.save()

    print(f'Done. downloaded={downloaded} misses={misses} cv_calls={comicvine.calls}')
    return 0 if downloaded or not pending else 1


if __name__ == '__main__':
    raise SystemExit(main())
