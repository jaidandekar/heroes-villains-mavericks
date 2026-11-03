#!/usr/bin/env python3
"""Resolve Screen Now shop products and render shop HTML sections.

Related bestsellers must be tied to a real product SKU and that SKU's photo.
Amazon uses an ASIN. Hot Topic and BoxLunch use their own product number.
Never invent a SKU, a product URL, or a photo.

  1. Cached asin/image already in screen_shop.json
  2. Amazon Creators API / PA-API if configured in config.json
  3. Browser Amazon search → --merge-resolutions (comics/toys/games)
  4. Items with no ASIN product image are left in the catalog and omitted
     from the page. The section never renders a card without that image.

By default this also patches shop sections into the live main page without
re-running TMDB date classification (movie/streaming dates stay frozen).

Usage:
  python3 refresh_shop.py                 # render + patch live page
  python3 refresh_shop.py --resolve-toys  # try API resolve for missing ASINs
  python3 refresh_shop.py --merge-resolutions .cache/toy_resolutions.json
  python3 refresh_shop.py --force         # re-query even when asin present
  python3 refresh_shop.py --no-live-patch # fragment only
  python3 refresh_shop.py --refresh-prices # pull each store's current price
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


def amazon_dp_url(asin: str, tag: str) -> str:
    return f'https://www.amazon.com/dp/{asin}?tag={urllib.parse.quote(tag)}'


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


STORE_LABEL = {
    'amazon': 'Amazon',
    'hottopic': 'Hot Topic',
    'boxlunch': 'BoxLunch',
}

STORE_HOST = {
    'hottopic': 'www.hottopic.com',
    'boxlunch': 'www.boxlunch.com',
}

STORE_ORDER = ('amazon', 'hottopic', 'boxlunch')


def item_store(item: dict) -> str:
    return (item.get('store') or 'amazon').strip()


def has_sku_image(item: dict) -> bool:
    """True when the card can show the photo that belongs to its store SKU."""
    image = (item.get('image') or '').strip()
    store = item_store(item)
    if not image:
        return False
    if store == 'amazon':
        asin = (item.get('asin') or '').strip()
        return bool(asin) and any(
            host in image
            for host in ('media-amazon.com', 'ssl-images-amazon.com', 'images-amazon.com')
        )
    host = STORE_HOST.get(store)
    sku = (item.get('sku') or '').strip()
    url = (item.get('url') or '').strip()
    return bool(
        host
        and sku
        and url.startswith(f'https://{host}/product/')
        and 'cdn.media.amplience.net' in image
    )


def shop_href(item: dict, tag: str) -> str:
    if item_store(item) == 'amazon':
        return amazon_dp_url(item['asin'].strip(), tag)
    return item['url'].strip()


def render_shop_item(item: dict, tag: str, kind: str, kind_label: str = '') -> str:
    """Render one card. Only products with a store SKU image qualify."""
    if not has_sku_image(item):
        return ''
    store = item_store(item)
    image = item['image'].strip()
    title = item.get('resolved_title') or item.get('title') or ''
    # Category only. The store is the "Shop …" link, and the product title names the character.
    kicker = kind_label
    note = item.get('note') or ''
    href = shop_href(item, tag)
    rel = 'noopener sponsored' if store == 'amazon' else 'noopener'
    cta = f'Shop {STORE_LABEL.get(store, "the store")} →'
    price = format_price(item)
    price_html = f'            <span class="shop-price">{esc(price)}</span>\n' if price else ''
    return (
        f'        <a class="shop-item" href="{esc(href)}" target="_blank" rel="{rel}">\n'
        f'          <img class="shop-item-media" src="{esc(image)}" alt="{esc(title)}" width="256" height="320" loading="lazy">\n'
        f'          <div class="shop-item-copy">\n'
        f'            <span class="shop-kicker">{esc(kicker)}</span>\n'
        f'            <span class="shop-title">{esc(item.get("title") or title)}</span>\n'
        f'{price_html}'
        f'            <span class="shop-note">{esc(note)}</span>\n'
        f'            <span class="shop-cta">{esc(cta)}</span>\n'
        f'          </div>\n'
        f'        </a>'
    )


def format_price(item: dict) -> str:
    """Current store price. "From" when sizes of the same product are priced differently."""
    amount = item.get('price')
    if amount is None:
        return ''
    try:
        low = float(amount)
    except (TypeError, ValueError):
        return ''
    label = f'${low:.2f}'
    high = item.get('price_max')
    try:
        high_amount = float(high) if high is not None else low
    except (TypeError, ValueError):
        high_amount = low
    if high_amount - low > 0.009:
        return f'From {label}'
    return label


def _fetch_html(url: str, user_agent: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            'User-Agent': user_agent,
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept': 'text/html',
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode('utf-8', 'ignore')


def _amazon_buybox_price(html: str) -> float | None:
    match = re.search(
        r'desktop_buybox_group_1":\[\{"displayPrice":"[^"]+","priceAmount":([0-9.]+)',
        html,
    )
    return float(match.group(1)) if match else None


def _store_offer_prices(html: str) -> list[float]:
    """Prices from Hot Topic / BoxLunch offers that can be bought online."""
    prices: list[float] = []

    def walk(node) -> None:
        if isinstance(node, dict):
            if node.get('@type') == 'Offer' and node.get('price') is not None:
                availability = str(node.get('availability') or '')
                if availability.endswith('InStock') or availability.endswith('OnlineOnly'):
                    prices.append(float(node['price']))
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            walk(json.loads(block))
        except (json.JSONDecodeError, TypeError, ValueError):
            continue
    return prices


def refresh_prices(shop: dict, cfg: dict) -> tuple[int, int]:
    """Write each product's current store price. Leave the last price if a fetch fails."""
    user_agent = cfg.get('user_agent') or 'Mozilla/5.0'
    updated = 0
    missing = 0
    for kind in ('toys', 'apparel', 'collectibles'):
        for item in shop.get(kind) or []:
            if not has_sku_image(item):
                continue
            store = item_store(item)
            if store == 'amazon':
                asin = (item.get('asin') or '').strip()
                url = f'https://www.amazon.com/dp/{asin}' if asin else ''
            else:
                url = (item.get('url') or '').strip()
            if not url:
                continue
            try:
                html = _fetch_html(url, user_agent)
                amounts = [_amazon_buybox_price(html)] if store == 'amazon' else _store_offer_prices(html)
                amounts = [amount for amount in amounts if amount is not None]
            except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
                print(f'price {item["id"]}: kept previous ({type(exc).__name__})')
                missing += 1
                continue
            if not amounts:
                print(f'price {item["id"]}: no current price on the product page')
                missing += 1
                continue
            low, high = min(amounts), max(amounts)
            item['price'] = round(low, 2)
            item['price_currency'] = 'USD'
            if high - low > 0.009:
                item['price_max'] = round(high, 2)
            else:
                item.pop('price_max', None)
            updated += 1
            print(f'price {item["id"]}: {format_price(item)}')
    return updated, missing


KIND_LABEL = {
    'comics': 'Graphic novel',
    'toys': 'Toys',
    'apparel': 'Clothes',
    'collectibles': 'Collectibles',
}

# Every priced product tied to a title on the page, not a short sample.
TRENDING_LIMIT = 24

# Characters in theaters, streaming, or coming soon. Supergirl and X-Men stay off this grid.
SLATE_TERMS = (
    'lantern',
    'hal jordan',
    'john stewart',
    'clayface',
    'vision',
    'doom',
    'doomsday',
    'spider-man',
    'peter parker',
    'miles',
    'superman',
)


def mix_stores(items: list[dict]) -> list[dict]:
    """Alternate Amazon, Hot Topic, and BoxLunch so one store does not run first."""
    groups: dict[str, list[dict]] = {store: [] for store in STORE_ORDER}
    for item in items:
        groups.setdefault(item_store(item), []).append(item)
    mixed: list[dict] = []
    while any(groups.values()):
        for store in list(groups):
            if groups[store]:
                mixed.append(groups[store].pop(0))
    return mixed


def is_slate_item(item: dict) -> bool:
    text = " ".join(str(item.get(key) or "") for key in ("id", "title", "kicker", "note")).lower()
    if "supergirl" in text or "wolverine" in text or "x-men" in text:
        return False
    return any(term in text for term in SLATE_TERMS)


def trending_items(shop: dict) -> list[tuple[str, dict]]:
    """Priced merchandise for the characters on screen. Other catalog items stay off this grid."""
    def keep(item: dict) -> bool:
        return has_sku_image(item) and is_slate_item(item) and item.get('price') is not None

    buckets = [
        ('toys', mix_stores([it for it in (shop.get('toys') or []) if keep(it)])),
        ('apparel', mix_stores([it for it in (shop.get('apparel') or []) if keep(it)])),
        ('collectibles', mix_stores([it for it in (shop.get('collectibles') or []) if keep(it)])),
    ]
    mixed: list[tuple[str, dict]] = []
    while any(items for _, items in buckets):
        for kind, items in buckets:
            if items:
                mixed.append((kind, items.pop(0)))
    return mixed[:TRENDING_LIMIT]


def section_lede(kinds: set[str]) -> str:
    labels = [
        label
        for kind, label in (
            ('toys', 'Toys'),
            ('apparel', 'clothes'),
            ('collectibles', 'other collectibles'),
        )
        if kind in kinds
    ]
    if not labels:
        return 'Products with a store photo.'
    if len(labels) == 1:
        word = labels[0]
        return word[:1].upper() + word[1:] + '.'
    if len(labels) == 2:
        return f'{labels[0]} and {labels[1]}.'
    return f'{", ".join(labels[:-1])}, and {labels[-1]}.'


def render_all(shop: dict, cfg: dict) -> str:
    tag = affiliate_tag(shop, cfg)
    items = trending_items(shop)
    body = '\n'.join(
        render_shop_item(item, tag, kind, KIND_LABEL.get(kind, ''))
        for kind, item in items
    )
    stores = {item_store(item) for _, item in items}
    disclosure = 'As an Amazon Associate we earn from qualifying purchases.'
    if stores & {'hottopic', 'boxlunch'}:
        disclosure += ' Hot Topic and BoxLunch links open those stores.'
    return (
        '    <section class="section" id="shop">\n'
        '      <div class="section-head">\n'
        '        <h2>Trending on Amazon, Hot Topic, and BoxLunch</h2>\n'
        '        <p>Toys and clothes for the characters in theaters, streaming, and coming soon.</p>\n'
        '      </div>\n'
        '      <div class="shop-grid">\n'
        f'{body}\n'
        '      </div>\n'
        f'      <p class="shop-disclosure">{esc(disclosure)}</p>\n'
        '    </section>\n'
    )


def apply_browser_resolutions(shop: dict, resolutions: dict[str, dict]) -> int:
    """Merge agent/browser-resolved {id: {asin, image, resolved_title}} across comics/toys/games."""
    n = 0
    by_id: dict[str, dict] = {}
    for kind in ('comics', 'toys', 'apparel', 'collectibles'):
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
    comic_ids = [it['id'] for it in (shop.get('comics') or [])]
    if comic_ids:
        print(f'comics: {len(comic_ids)} kept in the catalog, not shown')
    for kind in ('toys', 'apparel', 'collectibles'):
        items = shop.get(kind) or []
        shown = [it['id'] for it in items if has_sku_image(it)]
        hidden = [it['id'] for it in items if not has_sku_image(it)]
        print(f'{kind}: {len(shown)}/{len(items)} with SKU image')
        if hidden:
            print(f'  omitted (no SKU image): {", ".join(hidden)}')


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
        idx = page.find('<section class="section" id="shop">')
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
    parser.add_argument(
        '--refresh-prices',
        action='store_true',
        help='Pull the current price from each product page before rendering',
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

    if args.refresh_prices:
        updated, missing = refresh_prices(shop, cfg)
        save_json(SHOP_PATH, shop)
        print(f'Prices updated {updated} · missing {missing}')

    html = render_all(shop, cfg)
    OUT_HTML.write_text(html, encoding='utf-8')
    print(f'Wrote {OUT_HTML}')
    if not args.no_live_patch:
        patch_live_shop_sections(html)
    sku_coverage(shop)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
