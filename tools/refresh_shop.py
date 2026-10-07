#!/usr/bin/env python3
"""Resolve Screen Now shop products and render shop HTML sections.

Related bestsellers must be tied to a real Amazon ASIN (SKU) and populated
dynamically — never invent ASINs or ship fragile search-only links as "done".

  1. Cached asin/image already in screen_shop.json
  2. Amazon Creators API / PA-API if configured in config.json
  3. Browser Amazon search → --merge-resolutions (comics/toys/games)
  4. Unresolved items keep a search fallback + are reported by sku_coverage()

Comics may use Open Library ISBN covers for art until ASIN packaging is known;
the href still prefers /dp/ASIN whenever asin is set.

By default this also patches shop sections into the live main page without
re-running TMDB date classification (movie/streaming dates stay frozen).

Usage:
  python3 refresh_shop.py                 # render + patch live page
  python3 refresh_shop.py --resolve-toys  # try API resolve for missing ASINs
  python3 refresh_shop.py --merge-resolutions .cache/toy_resolutions.json
  python3 refresh_shop.py --force         # re-query even when asin present
  python3 refresh_shop.py --no-live-patch # fragment only
"""
from __future__ import annotations

import argparse
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
SITE_ROOT = REPO / 'site'
ROOT = SITE_ROOT
SHOP_PATH = HERE / 'screen_shop.json'
OUT_HTML = HERE / 'screen_shop_sections.html'
CONFIG_PATH = HERE / 'config.json'
LIVE_PAGE = SITE_ROOT / 'heroesvillainsmavericks.html'
INDEX_PAGE = SITE_ROOT / 'index.html'
SHOP_START = '<!-- SHOP_SECTIONS_START -->'
SHOP_END = '<!-- SHOP_SECTIONS_END -->'


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        return {}
    return json.loads(CONFIG_PATH.read_text(encoding='utf-8'))


def esc(s: str) -> str:
    return (
        str(s or '')
        .replace('&', '&amp;')
        .replace('<', '&lt;')
        .replace('>', '&gt;')
        .replace('"', '&quot;')
    )


def affiliate_tag(shop: dict, cfg: dict) -> str:
    return (
        (cfg.get('amazon') or {}).get('partner_tag')
        or shop.get('affiliate_tag')
        or 'YOURTAG-20'
    )


def amazon_search_url(query: str, tag: str) -> str:
    return (
        'https://www.amazon.com/s?k='
        + urllib.parse.quote_plus(query)
        + '&tag='
        + urllib.parse.quote(tag)
    )


def amazon_dp_url(asin: str, tag: str) -> str:
    return f'https://www.amazon.com/dp/{asin}?tag={urllib.parse.quote(tag)}'


def isbn_cover(isbn: str) -> str:
    return f'https://covers.openlibrary.org/b/isbn/{isbn}-L.jpg'


def larger_amazon_image(url: str | None) -> str | None:
    if not url:
        return None
    # Promote thumbnail variants to a larger product image when possible.
    return re.sub(r'\._AC_[^.]+_\.', '._AC_SL500_.', url)


def try_creators_or_paapi_search(query: str, cfg: dict) -> dict | None:
    """Optional Amazon Creators / PA-API search when credentials exist."""
    amazon = cfg.get('amazon') or {}
    access = amazon.get('access_key') or amazon.get('credential_id')
    secret = amazon.get('secret_key') or amazon.get('credential_secret')
    tag = amazon.get('partner_tag') or amazon.get('tag')
    if not access or not secret or not tag:
        return None
    if str(access).startswith('PASTE_') or str(secret).startswith('PASTE_'):
        return None

    # Prefer the lightweight REST Creators API search if the SDK isn't installed.
    # Without the official SDK we only store credentials readiness; full signed
    # requests need amazon-creatorsapi / amazon-paapi packages.
    try:
        from amazon_creatorsapi import AmazonCreatorsApi, Country  # type: ignore
    except ImportError:
        try:
            from amazon_paapi import AmazonApi, Country  # type: ignore
        except ImportError:
            return None
        else:
            api = AmazonApi(access, secret, tag, Country.US)
            result = api.search_items(keywords=query, item_count=5)
            items = getattr(result, 'items', None) or []
            for item in items:
                asin = getattr(item, 'asin', None)
                title = None
                image = None
                try:
                    title = item.item_info.title.display_value
                except Exception:
                    title = None
                try:
                    image = item.images.primary.large.url
                except Exception:
                    try:
                        image = item.images.primary.medium.url
                    except Exception:
                        image = None
                if asin and title:
                    return {
                        'asin': asin,
                        'resolved_title': title,
                        'image': larger_amazon_image(image),
                        'source': 'paapi',
                    }
            return None
    else:
        api = AmazonCreatorsApi(
            credential_id=access,
            credential_secret=secret,
            version=amazon.get('version') or '2.2',
            tag=tag,
            country=Country.US,
        )
        results = api.search_items(keywords=query)
        for item in getattr(results, 'items', []) or []:
            asin = getattr(item, 'asin', None)
            title = None
            image = None
            try:
                title = item.item_info.title.display_value
            except Exception:
                pass
            try:
                image = item.images.primary.large.url
            except Exception:
                pass
            if asin and title:
                return {
                    'asin': asin,
                    'resolved_title': title,
                    'image': larger_amazon_image(image),
                    'source': 'creators-api',
                }
        return None


def resolve_toys(shop: dict, cfg: dict, force: bool = False) -> tuple[int, int]:
    resolved = skipped = 0
    for item in shop.get('toys') or []:
        if item.get('asin') and item.get('image') and not force:
            skipped += 1
            continue
        hit = try_creators_or_paapi_search(item['search'], cfg)
        if not hit:
            continue
        item['asin'] = hit['asin']
        item['image'] = hit.get('image')
        item['resolved_title'] = hit.get('resolved_title')
        item['resolve_source'] = hit.get('source')
        resolved += 1
        print(f"  ok  toys/{item['id']} <- {hit['asin']}: {hit.get('resolved_title')}")
    return resolved, skipped


def render_shop_item(item: dict, tag: str, kind: str) -> str:
    """Render one card. Prefer /dp/ASIN links; search URLs are fallback only."""
    asin = (item.get('asin') or '').strip() or None
    image = item.get('image')
    title = item.get('resolved_title') or item.get('title') or ''
    kicker = item.get('kicker') or ''
    note = item.get('note') or ''
    search = item.get('search') or title

    # Comics: ISBN cover is fine as art, but link must still prefer ASIN when known.
    if kind == 'comics' and item.get('isbn') and not image:
        image = isbn_cover(item['isbn'])
    elif kind == 'comics' and item.get('isbn') and not asin:
        # Keep ISBN art until ASIN packaging is resolved.
        image = isbn_cover(item['isbn'])

    if asin:
        href = amazon_dp_url(asin, tag)
    else:
        # Fragile fallback — resolve ASIN before treating the section as done.
        href = amazon_search_url(search, tag)

    cta = 'Shop Amazon →' if asin else 'Find on Amazon →'
    if image:
        return (
            f'        <a class="shop-item" href="{esc(href)}" target="_blank" rel="noopener sponsored">\n'
            f'          <img class="shop-item-media" src="{esc(image)}" alt="{esc(title)}" width="88" height="120" loading="lazy">\n'
            f'          <div class="shop-item-copy">\n'
            f'            <span class="shop-kicker">{esc(kicker)}</span>\n'
            f'            <span class="shop-title">{esc(item.get("title") or title)}</span>\n'
            f'            <span class="shop-note">{esc(note)}</span>\n'
            f'            <span class="shop-cta">{esc(cta)}</span>\n'
            f'          </div>\n'
            f'        </a>'
        )
    return (
        f'        <a class="shop-item shop-item--no-media" href="{esc(href)}" target="_blank" rel="noopener sponsored">\n'
        f'          <div class="shop-item-copy">\n'
        f'            <span class="shop-kicker">{esc(kicker)}</span>\n'
        f'            <span class="shop-title">{esc(item.get("title") or title)}</span>\n'
        f'            <span class="shop-note">{esc(note)}</span>\n'
        f'            <span class="shop-cta">{esc(cta)}</span>\n'
        f'          </div>\n'
        f'        </a>'
    )


def render_section(section_id: str, heading: str, lede: str, items: list, tag: str, kind: str, disclosure: str) -> str:
    body = '\n'.join(render_shop_item(it, tag, kind) for it in items)
    return (
        f'    <section class="section" id="{section_id}">\n'
        f'      <div class="section-head">\n'
        f'        <h2>{heading}</h2>\n'
        f'        <p>{lede}</p>\n'
        f'      </div>\n'
        f'      <div class="shop-grid">\n'
        f'{body}\n'
        f'      </div>\n'
        f'      <p class="shop-disclosure">{disclosure}</p>\n'
        f'    </section>\n'
    )


def render_all(shop: dict, cfg: dict) -> str:
    tag = affiliate_tag(shop, cfg)
    parts = [
        render_section(
            'shop-comics',
            'Bestsellers in comics &amp; graphic novels',
            'Landmark trades resolved to Amazon product SKUs when available.',
            shop.get('comics') or [],
            tag,
            'comics',
            'As an Amazon Associate we earn from qualifying purchases.',
        ),
        render_section(
            'shop-toys',
            'Related bestsellers in toys &amp; collectibles',
            'SKU-specific Funko and figures — each card is a resolved Amazon product.',
            shop.get('toys') or [],
            tag,
            'toys',
            'As an Amazon Associate we earn from qualifying purchases. Cards show official product packaging when an ASIN is resolved.',
        ),
        render_section(
            'shop-games',
            'Related bestsellers in video games',
            'Named titles resolved to product SKUs with that game’s box art — not character placeholders.',
            shop.get('games') or [],
            tag,
            'games',
            'As an Amazon Associate we earn from qualifying purchases. Box art shown is for that named game title.',
        ),
    ]
    return '\n'.join(parts)


def apply_browser_resolutions(shop: dict, resolutions: dict[str, dict]) -> int:
    """Merge agent/browser-resolved {id: {asin, image, resolved_title}} across comics/toys/games."""
    n = 0
    by_id: dict[str, dict] = {}
    for kind in ('comics', 'toys', 'games'):
        for it in shop.get(kind) or []:
            by_id[it['id']] = it
    for tid, hit in resolutions.items():
        item = by_id.get(tid)
        if not item:
            continue
        if hit.get('asin'):
            item['asin'] = hit['asin']
        if hit.get('image'):
            item['image'] = larger_amazon_image(hit['image'])
        if hit.get('resolved_title'):
            item['resolved_title'] = hit['resolved_title']
        item['resolve_source'] = hit.get('source') or 'amazon-search'
        n += 1
    return n


def sku_coverage(shop: dict) -> None:
    for kind in ('comics', 'toys', 'games'):
        items = shop.get(kind) or []
        with_asin = sum(1 for it in items if it.get('asin'))
        missing = [it['id'] for it in items if not it.get('asin')]
        print(f'{kind}: {with_asin}/{len(items)} with ASIN')
        if missing:
            print(f'  unresolved (search-link fallback): {", ".join(missing)}')


def patch_live_shop_sections(shop_html: str) -> bool:
    """Swap shop blocks into the live main page without touching Now/Upcoming dates."""
    if not LIVE_PAGE.exists():
        print(f'Live page missing — skipped patch: {LIVE_PAGE}')
        return False
    page = LIVE_PAGE.read_text(encoding='utf-8')
    block = f'{SHOP_START}\n{shop_html.rstrip()}\n{SHOP_END}'
    if SHOP_START in page and SHOP_END in page:
        before, _, rest = page.partition(SHOP_START)
        _, _, after = rest.partition(SHOP_END)
        page = before + block + after
    else:
        # First-time inject: replace existing shop sections ahead of the footer.
        footer = '    <footer class="footer">'
        idx = page.find('<section class="section" id="shop-comics">')
        foot = page.find(footer)
        if idx == -1 or foot == -1 or foot < idx:
            print('Could not locate shop sections in live page — skipped patch.')
            return False
        page = page[:idx] + block + '\n' + page[foot:]
    LIVE_PAGE.write_text(page, encoding='utf-8')
    # Keep GitHub Pages root URL in sync with the named landing file.
    INDEX_PAGE.write_text(page, encoding='utf-8')
    print(f'Patched shop sections → {LIVE_PAGE} (+ index.html)')
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--resolve-toys', action='store_true', help='Attempt API resolve for toys missing ASINs')
    parser.add_argument('--force', action='store_true')
    parser.add_argument(
        '--merge-resolutions',
        help='JSON map of browser-resolved SKUs {id: {asin, image, resolved_title}} for comics/toys/games',
    )
    parser.add_argument(
        '--no-live-patch',
        action='store_true',
        help='Only write screen_shop_sections.html; do not patch the live main page',
    )
    args = parser.parse_args()

    shop = load_json(SHOP_PATH)
    cfg = load_config()

    if args.merge_resolutions:
        data = load_json(Path(args.merge_resolutions))
        n = apply_browser_resolutions(shop, data)
        print(f'Merged {n} browser resolution(s)')
        save_json(SHOP_PATH, shop)

    if args.resolve_toys:
        print('Resolving toys via Amazon API (if configured)…')
        resolved, skipped = resolve_toys(shop, cfg, force=args.force)
        save_json(SHOP_PATH, shop)
        print(f'API resolved {resolved} · skipped cached {skipped}')
        amazon = cfg.get('amazon') or {}
        if resolved == 0 and not (amazon.get('access_key') or amazon.get('credential_id')):
            print(
                'No Amazon Creators/PA-API credentials in config.json.\n'
                'Add amazon.access_key, amazon.secret_key, amazon.partner_tag\n'
                'or merge browser search results with --merge-resolutions.'
            )

    html = render_all(shop, cfg)
    OUT_HTML.write_text(html, encoding='utf-8')
    print(f'Wrote {OUT_HTML}')
    if not args.no_live_patch:
        patch_live_shop_sections(html)
    sku_coverage(shop)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
