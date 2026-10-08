#!/usr/bin/env python3
"""Rebuild heroesvillainsmavericks.html from screen_slate.json + TMDB.

Manual / on-demand only — do not schedule this for automatic date updates.
Reclassifies now vs upcoming from TMDB, refreshes posters, and re-embeds shop
sections from screen_shop.json.

For bestsellers-only updates (comics / toys / games) without touching dates,
use refresh_shop.py instead (it patches shop sections into the live page).

Usage:
  python3 refresh_screen_now.py
  python3 refresh_screen_now.py --dry-run
  python3 refresh_screen_now.py --verbose
"""
from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
SITE_ROOT = REPO / 'site'
ROOT = SITE_ROOT
SLATE_PATH = HERE / 'screen_slate.json'
CONFIG_PATH = HERE / 'config.json'
OUT_PATH = SITE_ROOT / 'heroesvillainsmavericks.html'
INDEX_PATH = SITE_ROOT / 'index.html'
SHOP_SECTIONS_PATH = HERE / 'screen_shop_sections.html'
CACHE_PATH = HERE / '.cache' / 'tmdb_screen.json'
TMDB_BASE = 'https://api.themoviedb.org/3'
TMDB_IMG = 'https://image.tmdb.org/t/p'


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        raise SystemExit(f'Missing {CONFIG_PATH} — copy config.example.json and add keys.')
    cfg = json.loads(CONFIG_PATH.read_text(encoding='utf-8'))
    key = (cfg.get('tmdb') or {}).get('api_key') or ''
    if not key or key.startswith('PASTE_'):
        raise SystemExit('TMDB api_key missing in config.json')
    return cfg


def load_tmdb_cache() -> dict:
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            return {}
    return {}


def save_tmdb_cache(cache: dict) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=2), encoding='utf-8')


def tmdb_get(path: str, api_key: str, user_agent: str, params: dict | None = None) -> dict:
    query = dict(params or {})
    query['api_key'] = api_key
    url = f'{TMDB_BASE}/{path.lstrip("/")}?' + urllib.parse.urlencode(query)
    req = urllib.request.Request(
        url,
        headers={'User-Agent': user_agent, 'Accept': 'application/json'},
    )
    with urllib.request.urlopen(req, timeout=25) as resp:
        return json.loads(resp.read().decode())


def parse_iso(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return datetime.strptime(value[:10], '%Y-%m-%d').date()
    except ValueError:
        return None


def format_short(d: date) -> str:
    return d.strftime('%b ') + str(d.day)


def format_since(d: date) -> str:
    return f'since {d.strftime("%b")} {d.day}'


def format_long(d: date) -> str:
    day = d.day
    if 10 <= day % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
    return f'{d.strftime("%B")} {day}{suffix}, {d.year}'


def year_end(today: date) -> date:
    return date(today.year, 12, 31)


def fetch_title(entry: dict, api_key: str, user_agent: str, verbose: bool, cache: dict) -> dict:
    """Merge slate entry with live TMDB fields (cache fallback on network failure)."""
    kind = entry['kind']
    tmdb_id = entry['tmdb_id']
    path = f'{"tv" if kind == "tv" else "movie"}/{tmdb_id}'
    payload: dict = {}
    try:
        payload = tmdb_get(path, api_key, user_agent)
        cache[path] = payload
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        payload = cache.get(path) or {}
        if verbose:
            src = 'cache' if payload else 'empty'
            print(f'  ! {entry["id"]}: {type(exc).__name__} — using {src}')

    name = payload.get('title') or payload.get('name') or entry['title']
    poster = payload.get('poster_path') or entry.get('poster_path')
    backdrop = payload.get('backdrop_path')

    if entry.get('manual_date'):
        release = parse_iso(entry['manual_date'])
    elif kind == 'tv':
        next_ep = (payload.get('next_episode_to_air') or {}).get('air_date')
        last_ep = (payload.get('last_episode_to_air') or {}).get('air_date')
        release = parse_iso(next_ep) or parse_iso(payload.get('first_air_date')) or parse_iso(last_ep)
    else:
        release = parse_iso(payload.get('release_date'))

    status = (payload.get('status') or '').lower()
    in_production = bool(payload.get('in_production'))
    last_air = parse_iso(((payload.get('last_episode_to_air') or {}).get('air_date')))
    next_air = parse_iso(((payload.get('next_episode_to_air') or {}).get('air_date')))
    first_air = parse_iso(payload.get('first_air_date')) if kind == 'tv' else None

    display_title = entry['title']
    if entry.get('season_label'):
        display_title = f"{entry['title']} · {entry['season_label']}"

    tmdb_score = payload.get('vote_average')
    if tmdb_score in (None, '', 0, 0.0):
        tmdb_score = entry.get('tmdb_score')

    return {
        **entry,
        'display_title': display_title,
        'resolved_name': name,
        'poster_path': poster,
        'backdrop_path': backdrop,
        'release': release,
        'status': status,
        'in_production': in_production,
        'last_air': last_air,
        'next_air': next_air,
        'first_air': first_air,
        'tmdb_score': tmdb_score,
    }


def classify(entry: dict, today: date) -> str | None:
    """Return 'now', 'upcoming', or None (out of window / too old)."""
    end = year_end(today)
    release = entry.get('release')

    if entry['kind'] == 'tv':
        airing = entry.get('in_production') or entry.get('status') in {
            'returning series', 'in production', 'pilot', 'planned'
        }
        # Still dropping episodes
        if entry.get('keep_now_while_airing') and (airing or (entry.get('next_air') and entry['next_air'] >= today)):
            if entry.get('first_air') and entry['first_air'] <= today:
                return 'now'
        if entry.get('next_air') and today < entry['next_air'] <= end:
            return 'upcoming'
        if release and today < release <= end:
            return 'upcoming'
        if release and release <= today:
            # Recently premiered this year
            if release.year == today.year:
                return 'now'
            window = entry.get('current_window_days', 120)
            if today - release <= timedelta(days=window):
                return 'now'
        return None

    # Movies
    if release is None:
        return None
    if today < release <= end:
        return 'upcoming'
    if release <= today:
        window = entry.get('current_window_days', 120)
        if today - release <= timedelta(days=window):
            return 'now'
        # Still "current year" prestige titles stay lightly visible until year end if recent enough
        if release.year == today.year and today - release <= timedelta(days=180):
            return 'now'
    return None


def poster_url(path: str | None, width: str = 'w342') -> str:
    if not path:
        return ''
    return f'{TMDB_IMG}/{width}{path}'


def esc(text: str) -> str:
    return (
        text.replace('&', '&amp;')
        .replace('<', '&lt;')
        .replace('>', '&gt;')
        .replace('"', '&quot;')
    )


def kicker_for(entry: dict, bucket: str) -> str:
    if entry.get('kicker_override'):
        return entry['kicker_override']
    universe = entry.get('universe', '')
    if entry['kind'] == 'tv':
        if bucket == 'now':
            return f"Series · {'airing' if entry.get('in_production') or entry.get('next_air') else 'streaming'}"
        return f"Series premiere · {universe}" if universe else 'Series premiere'
    if bucket == 'now':
        return 'Film · in theaters' if 'Theater' in (entry.get('where') or '') else 'Film · out now'
    return f"Film · {universe}" if universe else 'Film'


def upcoming_status_line(entry: dict) -> str:
    """Natural-language availability + date line for Coming soon cards."""
    if entry.get('status_override'):
        return entry['status_override']

    where = (entry.get('where') or '').strip()
    where_l = where.lower()
    kicker = (entry.get('kicker_override') or '').lower()
    is_rerelease = 're-release' in kicker or 'rerelease' in entry.get('id', '')
    release = entry.get('release')
    when = f' on {format_long(release)}' if release else ''

    if entry['kind'] == 'tv':
        if where:
            return f'Series premiere on {where}{when}'
        return f'Series premiere{when}'

    if is_rerelease:
        if 'theater' in where_l:
            return f'Re-release in theaters{when}'
        if where:
            return f'Re-release on {where}{when}'
        return f'Re-release{when}'

    if 'theater' in where_l:
        return f'In theaters{when}'
    if where:
        return f'Streaming on {where}{when}'
    return f'Coming soon{when}'


def where_line(entry: dict, bucket: str) -> str:
    if entry.get('where_override'):
        return entry['where_override']
    where = entry.get('where') or ''
    release = entry.get('release')
    if not release:
        return where
    if bucket == 'upcoming':
        return where
    if entry['kind'] == 'tv' and entry.get('next_air') and entry['next_air'] >= date.today():
        return f"{where} · through {format_short(entry['next_air'])}"
    return f"{where} · {format_since(release)}"


def guide_links_html(entry: dict, class_name: str = 'guide-link') -> str:
    chunks = []
    for key in ('guide', 'guide_secondary'):
        g = entry.get(key)
        if g:
            chunks.append(
                f'<a class="{class_name}" href="{esc(g["href"])}">{esc(g["label"])}</a>'
            )
    return '\n            '.join(chunks)


STUDIO_LOGOS = {
    'Marvel': {
        'src': 'assets/studio-logos/marvel.svg',
        'alt': 'Marvel',
        'class': 'now-studio now-studio-marvel',
    },
    'DC': {
        'src': 'assets/studio-logos/dc.svg',
        'alt': 'DC',
        'class': 'now-studio now-studio-dc',
    },
}


def studio_logo_html(entry: dict) -> str:
    logo = STUDIO_LOGOS.get(entry.get('universe') or '')
    if not logo:
        return ''
    return (
        f'<img class="{logo["class"]}" src="{esc(logo["src"])}" '
        f'alt="{esc(logo["alt"])}" width="80" height="80" loading="lazy">'
    )


def ratings_html(entry: dict) -> str:
    """Render up to three key scores: Rotten Tomatoes, IMDb, Metacritic (or TMDB)."""
    ratings = dict(entry.get('ratings') or {})
    chips = []

    def add(key: str, default_label: str, formatter):
        raw = ratings.get(key)
        if raw is None:
            return
        if isinstance(raw, dict):
            value = raw.get('value')
            label = raw.get('label') or default_label
            href = raw.get('href')
            note = raw.get('note')
        else:
            value, label, href, note = raw, default_label, None, None
        if value is None:
            return
        score = formatter(value)
        title_attr = f' title="{esc(note)}"' if note else ''
        inner = f'<span class="now-rating-score">{esc(score)}</span><span class="now-rating-label">{esc(label)}</span>'
        if href:
            chips.append(f'<a class="now-rating" href="{esc(href)}" target="_blank" rel="noopener"{title_attr}>{inner}</a>')
        else:
            chips.append(f'<span class="now-rating"{title_attr}>{inner}</span>')

    add('rt_critics', 'Rotten Tomatoes', lambda v: f'{int(round(float(v)))}%')
    add('imdb', 'IMDb', lambda v: f'{float(v):.1f}')
    add('metacritic', 'Metacritic', lambda v: f'{int(round(float(v)))}')

    # Live TMDB score fills a third slot when Metacritic is missing
    if 'metacritic' not in ratings and entry.get('tmdb_score') not in (None, 0, 0.0):
        score = float(entry['tmdb_score'])
        chips.append(
            f'<span class="now-rating" title="TMDB user score">'
            f'<span class="now-rating-score">{score:.1f}</span>'
            f'<span class="now-rating-label">TMDB</span></span>'
        )

    if not chips:
        return ''
    return '<div class="now-ratings" aria-label="Ratings">' + ''.join(chips[:3]) + '</div>'


def render_now_card(entry: dict) -> str:
    backdrop = poster_url(entry.get('backdrop_path') or entry.get('poster_path'), 'w1280')
    blurb = entry.get('date_note') and f"{entry['blurb']} {entry['date_note']}" or entry['blurb']
    actions = []
    trailer = entry.get('trailer') or {}
    if trailer.get('youtube'):
        actions.append(
            '<a class="now-trailer" href="https://www.youtube.com/watch?v=%s" target="_blank" rel="noopener">%s</a>'
            % (esc(trailer['youtube']), esc(trailer.get('label') or 'Watch trailer'))
        )
    guide_html = guide_links_html(entry, 'now-guide')
    if guide_html:
        actions.append(guide_html)
    actions_html = '\n            '.join(actions)
    ratings = ratings_html(entry)
    ratings_block = f'\n          {ratings}' if ratings else ''
    studio = studio_logo_html(entry)
    studio_block = f'\n        {studio}' if studio else ''
    return f'''      <article class="now-card" id="now-{esc(entry['id'])}">
        <div class="now-card-media" aria-hidden="true" style="background-image: url('{esc(backdrop)}')"></div>
        <div class="now-card-veil" aria-hidden="true"></div>
        {studio_block}
        <div class="now-card-copy">
          <span class="now-kicker">{esc(kicker_for(entry, 'now'))}</span>
          <h3 class="now-title">
            <a href="{esc(entry.get('external') or '#')}" target="_blank" rel="noopener">{esc(entry['display_title'])}</a>
          </h3>
          {ratings_block}
          <p class="now-blurb">{esc(blurb)}</p>
          <p class="now-where">{esc(where_line(entry, 'now'))}</p>
          <div class="now-actions">
            {actions_html}
          </div>
        </div>
      </article>'''


def render_upcoming_row(entry: dict) -> str:
    poster = poster_url(entry.get('poster_path'), 'w500')
    blurb = entry['blurb']
    if entry.get('date_note'):
        blurb = f"{blurb} {entry['date_note']}"
    status = upcoming_status_line(entry)
    trailer = entry.get('trailer') or {}
    trailer_html = ''
    if trailer.get('youtube'):
        trailer_html = (
            '\n              <a class="upcoming-trailer" href="https://www.youtube.com/watch?v=%s" '
            'target="_blank" rel="noopener">%s</a>'
            % (esc(trailer['youtube']), esc(trailer.get('label') or 'Watch trailer'))
        )
    return f'''        <article class="upcoming-card">
          <img class="upcoming-card-poster" src="{esc(poster)}" alt="{esc(entry['display_title'])} poster" width="200" height="300" loading="lazy">
          <div class="upcoming-card-body">
            <a class="title-name" href="{esc(entry.get('external') or '#')}" target="_blank" rel="noopener">{esc(entry['display_title'])}</a>
            <span class="title-blurb">{esc(blurb)}</span>
            {guide_links_html(entry)}
            <div class="upcoming-card-meta">
              <p class="date-status">{esc(status)}</p>{trailer_html}
            </div>
          </div>
        </article>'''


CSS = r'''
    :root {
      --bg: #f5f5f5;
      --ink: #1a1c1e;
      --muted: #6a6e75;
      --line: rgba(26, 28, 30, 0.06);
      --accent: #e4572e;
      --accent-deep: #c2410c;
      --link: #5BA4E6;
      --link-hover: #3D8FD9;
      --on-media: #f7f4ef;
      --on-media-muted: rgba(247, 244, 239, 0.72);
      --font-display: 'Google Sans Flex', 'Helvetica Neue', Helvetica, Arial, sans-serif;
      --font-body: 'Google Sans Flex', 'Helvetica Neue', Helvetica, Arial, sans-serif;
      --ease: cubic-bezier(0.22, 1, 0.36, 1);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      font-family: var(--font-body);
      color: var(--ink);
      background: var(--bg);
      min-height: 100vh;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }
    a { color: inherit; }
    .site {
      width: min(100%, 72rem);
      max-width: none;
      margin: 0 auto;
      padding: 1.5rem 1rem 3rem;
      background: transparent;
    }
    .nav {
      display: flex; align-items: center; justify-content: space-between; gap: 1rem;
      padding: 0.35rem 0 1.5rem; border-bottom: 1px solid var(--line); margin-bottom: 2rem;
      opacity: 0; animation: rise 0.7s var(--ease) 0.05s forwards;
    }
    .nav-brand { font-family: var(--font-display); font-size: 1.35rem; letter-spacing: 0.08em; text-decoration: none; }
    .nav-links { display: flex; gap: 1.25rem; font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; }
    .nav-links a { text-decoration: none; color: var(--muted); transition: color 0.2s ease; }
    .nav-links a:hover, .nav-links a[aria-current="page"] { color: var(--ink); }
    .hero {
      position: relative; min-height: min(72vh, 580px); display: grid; align-items: end;
      overflow: hidden; margin: 0 -1.25rem 0;
      opacity: 0; animation: rise 0.85s var(--ease) 0.15s forwards;
    }
    .hero-media {
      position: absolute; inset: 0;
      background:
        linear-gradient(90deg, rgba(14, 17, 20, 0.92) 0%, rgba(14, 17, 20, 0.55) 42%, rgba(14, 17, 20, 0.2) 100%),
        linear-gradient(0deg, rgba(14, 17, 20, 0.98) 0%, transparent 42%),
        var(--hero-image) center / cover no-repeat;
      transform: scale(1.04); animation: ken 18s ease-in-out infinite alternate;
    }
    .hero-copy { position: relative; z-index: 1; padding: 2.5rem 1.25rem 2.75rem; max-width: 34rem; color: var(--on-media); }
    .brand { font-family: var(--font-display); font-size: clamp(3.5rem, 12vw, 6.5rem); letter-spacing: 0.04em; line-height: 0.9; margin-bottom: 0.85rem; }
    .brand span { display: block; color: var(--accent); }
    .hero h1 { font-size: clamp(1.35rem, 3.2vw, 1.85rem); font-weight: 700; letter-spacing: -0.02em; line-height: 1.2; margin-bottom: 0.65rem; max-width: 18ch; }
    .hero-lede { color: var(--on-media-muted); font-size: 1rem; max-width: 34ch; margin-bottom: 1.35rem; }
    .cta-row { display: flex; flex-wrap: wrap; gap: 0.75rem; }
    .cta {
      display: inline-flex; align-items: center; gap: 0.45rem; padding: 0.7rem 1.15rem;
      font-size: 0.8125rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase;
      text-decoration: none; border: 1px solid transparent;
      transition: transform 0.2s var(--ease), background 0.2s ease, border-color 0.2s ease;
    }
    .cta-primary { background: var(--accent); color: #fff; }
    .cta-primary:hover { transform: translateY(-1px); background: #f06a3f; }
    .cta-ghost { background: transparent; border-color: rgba(247, 244, 239, 0.35); color: var(--on-media); }
    .cta-ghost:hover { border-color: var(--on-media); }
    .as-of { margin-top: 1.1rem; font-size: 0.75rem; letter-spacing: 0.06em; text-transform: uppercase; color: var(--muted); }

    /* Site header */
    .site-header {
      position: sticky;
      top: 0;
      z-index: 50;
      background: #ffffff;
      transition: box-shadow 0.28s var(--ease);
    }
    .site-header-inner {
      width: min(100%, 72rem);
      margin: 0 auto;
      padding: 1.05rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }
    .site-header-title {
      font-family: var(--font-display);
      font-size: clamp(0.95rem, 1.6vw, 1.1rem);
      font-weight: 900;
      letter-spacing: -0.01em;
      color: var(--ink);
      line-height: 1.2;
    }
    .site-header-by {
      font-weight: 600;
      letter-spacing: 0;
      color: var(--link);
      text-decoration: none;
      transition: color 0.2s ease;
    }
    .site-header-by:hover { color: var(--link-hover); }
    .site-header-portfolio {
      flex-shrink: 0;
      font-size: 0.8125rem;
      font-weight: 600;
      letter-spacing: -0.01em;
      text-decoration: none;
      color: var(--link);
      transition: color 0.2s ease;
      text-align: right;
      white-space: nowrap;
    }
    .site-header-portfolio:hover { color: var(--link-hover); }
    .site-header.is-scrolled {
      box-shadow: 0 10px 28px rgba(26, 28, 30, 0.1);
    }

    /* Now section head */
    .now-stage-head {
      margin: 0.35rem 0 0.85rem;
      padding-bottom: 0;
    }
    .now-stage-head h2 {
      font-family: var(--font-display);
      font-size: clamp(1.2rem, 2.4vw, 1.55rem);
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.15;
      color: #c4c7ce;
    }
    .now-cards {
      display: grid;
      gap: 1.15rem;
      margin-bottom: 4.5rem;
      width: 100%;
    }
    .now-card {
      position: relative;
      width: 100%;
      min-height: clamp(20rem, 70vw, 26rem);
      display: grid;
      align-items: end;
      overflow: hidden;
      isolation: isolate;
      border-radius: 0.85rem;
      border: 1px solid rgba(26, 28, 30, 0.08);
      box-shadow: 0 18px 40px rgba(26, 28, 30, 0.08);
      background: #2a2e33;
      color: var(--on-media);
    }
    .now-studio {
      position: absolute;
      top: 1.15rem;
      right: 1.15rem;
      z-index: 3;
      width: auto;
      object-fit: contain;
      filter: drop-shadow(0 4px 14px rgba(0, 0, 0, 0.45));
      pointer-events: none;
    }
    .now-studio-marvel {
      height: 1.85rem;
    }
    .now-studio-dc {
      height: 2.65rem;
      width: 2.65rem;
    }
    .now-card-media {
      position: absolute;
      inset: 0;
      z-index: 0;
      background-position: center;
      background-size: cover;
      background-repeat: no-repeat;
      transform: scale(1.03);
      filter: saturate(1.06) contrast(1.04);
    }
    .now-card-veil {
      position: absolute;
      inset: 0;
      z-index: 1;
      background:
        linear-gradient(90deg, rgba(12, 14, 16, 0.92) 0%, rgba(12, 14, 16, 0.7) 42%, rgba(12, 14, 16, 0.28) 72%, rgba(12, 14, 16, 0.42) 100%),
        linear-gradient(0deg, rgba(12, 14, 16, 0.86) 0%, rgba(12, 14, 16, 0.18) 48%, rgba(12, 14, 16, 0.3) 100%);
      pointer-events: none;
    }
    .now-card-copy {
      position: relative;
      z-index: 2;
      padding: 1.5rem 1.15rem 1.6rem;
      width: min(100%, 36rem);
      padding-right: 4.5rem;
    }
    .now-kicker {
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #f0a27a;
      margin-bottom: 0.7rem;
    }
    .now-title {
      font-family: var(--font-display);
      font-size: clamp(2.1rem, 5.5vw, 3.75rem);
      letter-spacing: 0.01em;
      line-height: 0.98;
      margin-bottom: 0.85rem;
      font-weight: 700;
    }
    .now-title a {
      text-decoration: none;
      color: var(--on-media);
      text-shadow: 0 2px 28px rgba(0, 0, 0, 0.4);
    }
    .now-title a:hover { color: #f0a27a; }
    .now-ratings {
      display: flex;
      flex-wrap: wrap;
      gap: 0.65rem 1.1rem;
      margin: 0 0 1rem;
    }
    .now-rating {
      display: flex;
      flex-direction: column;
      gap: 0.15rem;
      text-decoration: none;
      color: inherit;
      min-width: 4.5rem;
    }
    a.now-rating:hover .now-rating-score { color: #f0a27a; }
    .now-rating-score {
      font-family: var(--font-display);
      font-size: clamp(1.25rem, 2.5vw, 1.65rem);
      line-height: 1;
      letter-spacing: 0.02em;
      color: var(--on-media);
      font-weight: 700;
    }
    .now-rating-label {
      font-size: 0.62rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: rgba(247, 244, 239, 0.5);
    }
    .now-blurb {
      font-size: clamp(0.95rem, 1.6vw, 1.08rem);
      color: var(--on-media-muted);
      margin-bottom: 0.75rem;
    }
    .now-where {
      font-size: 0.8rem;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: rgba(247, 244, 239, 0.55);
      margin-bottom: 1.2rem;
    }
    .now-actions { display: flex; flex-wrap: wrap; gap: 0.75rem; }
    .now-guide, .now-trailer {
      display: inline-flex;
      align-items: center;
      padding: 0.7rem 1.35rem;
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-decoration: none;
      border: 0;
      border-radius: 999px;
      cursor: pointer;
      font-family: inherit;
      transition: transform 0.2s var(--ease), background 0.2s ease, border-color 0.2s ease, color 0.2s ease;
    }
    .now-guide {
      color: #fff;
      background: var(--accent);
    }
    .now-guide:hover { transform: translateY(-1px); background: #f06a3f; }
    .now-trailer {
      color: var(--on-media);
      background: transparent;
      border: 1px solid rgba(247, 244, 239, 0.4);
    }
    .now-trailer:hover {
      transform: translateY(-1px);
      border-color: var(--on-media);
      background: rgba(247, 244, 239, 0.1);
    }

    .section { margin-bottom: 3.25rem; }
    .section-head {
      display: flex; flex-wrap: wrap; align-items: baseline; justify-content: space-between;
      gap: 0.5rem 1.5rem; margin: 0 0 0.85rem; padding-bottom: 0;
    }
    .section-head h2 { font-family: var(--font-display); font-size: clamp(1.2rem, 2.4vw, 1.55rem); font-weight: 800; letter-spacing: -0.02em; line-height: 1.15; color: #c4c7ce; }
    .section-head p { color: var(--muted); font-size: 0.9rem; max-width: 28rem; }
    .upcoming-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.15rem;
    }
    .upcoming-card {
      display: grid;
      grid-template-columns: 120px 1fr;
      gap: 0;
      align-items: stretch;
      background: #ffffff;
      border-radius: 1rem;
      border: 1px solid rgba(26, 28, 30, 0.05);
      box-shadow: 0 14px 34px rgba(26, 28, 30, 0.07);
      padding: 0;
      overflow: hidden;
    }
    .upcoming-card-poster {
      width: 100%;
      height: 100%;
      min-height: 11.5rem;
      object-fit: cover;
      background: #e8e8e8;
      display: block;
      border-radius: 0;
    }
    .upcoming-card-body {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
      min-width: 0;
      height: 100%;
      padding: 1.05rem 1.1rem 1.1rem 1.2rem;
    }
    .title-name { font-size: 1.25rem; font-weight: 700; letter-spacing: -0.02em; text-decoration: none; color: var(--ink); transition: color 0.2s ease; }
    .title-name:hover { color: var(--link-hover); }
    .title-blurb { color: var(--muted); font-size: 0.88rem; }
    .guide-link { display: inline-flex; margin-top: 0.1rem; font-size: 0.78rem; font-weight: 600; color: var(--link); text-decoration: none; width: fit-content; }
    .guide-link:hover { color: var(--link-hover); text-decoration: underline; }
    .upcoming-card .guide-link {
      align-items: center;
      gap: 0.35rem;
    }
    .upcoming-card .guide-link::after {
      content: '→';
      font-size: 0.85em;
      line-height: 1;
      transform: translateY(0.02em);
    }
    .upcoming-card-meta {
      margin-top: auto;
      padding-top: 0.85rem;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 0.15rem;
    }
    .date-status {
      margin: 0;
      font-family: var(--font-body);
      font-size: 0.82rem;
      font-weight: 600;
      letter-spacing: 0.01em;
      line-height: 1.35;
      color: var(--ink);
    }
    .upcoming-trailer {
      display: inline-flex;
      align-items: center;
      margin-top: 0.65rem;
      padding: 0.55rem 1.05rem;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-decoration: none;
      border-radius: 999px;
      color: var(--ink);
      background: transparent;
      border: 1px solid rgba(26, 28, 30, 0.18);
      transition: transform 0.2s var(--ease), background 0.2s ease, border-color 0.2s ease, color 0.2s ease;
      white-space: nowrap;
    }
    .upcoming-trailer:hover,
    .upcoming-trailer:active {
      transform: translateY(-1px);
      color: #ffffff;
      background: var(--ink);
      border-color: var(--ink);
    }
    .shop-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.85rem;
    }
    .shop-item {
      display: grid;
      grid-template-columns: 88px 1fr;
      gap: 0.95rem;
      align-items: stretch;
      padding: 0;
      background: #ffffff;
      border-radius: 0.85rem;
      border: 1px solid rgba(26, 28, 30, 0.05);
      box-shadow: 0 10px 28px rgba(26, 28, 30, 0.06);
      text-decoration: none;
      color: inherit;
      overflow: hidden;
      transition: transform 0.2s var(--ease), box-shadow 0.2s ease, border-color 0.2s ease;
    }
    .shop-item:hover {
      transform: translateY(-2px);
      border-color: rgba(26, 28, 30, 0.1);
      box-shadow: 0 16px 34px rgba(26, 28, 30, 0.1);
    }
    .shop-item-media {
      width: 100%;
      height: 100%;
      min-height: 7.25rem;
      border-radius: 0;
      object-fit: cover;
      object-position: center top;
      background: #e8e8e8;
      display: block;
      align-self: stretch;
    }
    .shop-item-media--square {
      object-fit: cover;
      padding: 0;
      background: #e8e8e8;
    }
    .shop-item-copy {
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
      min-width: 0;
      padding: 0.9rem 1rem 0.9rem 0;
      justify-content: center;
    }
    .shop-item--no-media {
      grid-template-columns: 1fr;
      padding: 0.95rem 1.05rem;
    }
    .shop-item--no-media .shop-item-copy {
      padding: 0;
    }
    .shop-kicker {
      font-size: 0.7rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--muted);
    }
    .shop-title {
      font-size: 1rem;
      font-weight: 700;
      letter-spacing: -0.015em;
      line-height: 1.25;
      color: var(--ink);
    }
    .shop-note {
      font-size: 0.82rem;
      color: var(--muted);
      line-height: 1.35;
    }
    .shop-cta {
      margin-top: 0.35rem;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--link);
    }
    .shop-item:hover .shop-cta { color: var(--link-hover); }
    .shop-disclosure {
      margin-top: 0.85rem;
      font-size: 0.75rem;
      color: var(--muted);
    }
    .about-body {
      max-width: 38rem;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }
    .about-body p {
      font-size: 1rem;
      line-height: 1.55;
      color: var(--ink);
    }
    .about-link {
      display: inline-flex;
      align-items: center;
      margin-top: 0.35rem;
      width: fit-content;
      font-size: 0.8125rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-decoration: none;
      color: var(--link);
      transition: color 0.2s ease;
    }
    .about-link:hover { color: var(--link-hover); }
    .footer {
      margin-top: 1rem; padding-top: 1.5rem; border-top: 1px solid var(--line); font-size: 0.8rem;
      color: var(--muted); display: flex; flex-wrap: wrap; gap: 0.75rem 1.5rem; justify-content: space-between;
    }
    .footer a { color: var(--link); text-decoration: none; }
    .footer a:hover { text-decoration: underline; }
    @keyframes rise { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes ken { from { transform: scale(1.04); } to { transform: scale(1.1) translate3d(-1.5%, -1%, 0); } }
    @media (min-width: 640px) {
      .site {
        width: min(100%, 78rem);
        padding: 1.75rem 1.25rem 3.5rem;
      }
      .site-header-inner {
        width: min(100%, 78rem);
        padding: 1.2rem 1.25rem;
      }
      .now-cards { gap: 1.25rem; }
      .now-card {
        min-height: clamp(22rem, 48vw, 28rem);
        border-radius: 1rem;
      }
      .now-card-copy {
        padding: 1.85rem 1.5rem 2rem;
        padding-right: 5.5rem;
        width: min(100%, 40rem);
      }
      .upcoming-card {
        grid-template-columns: 148px 1fr;
      }
      .title-name { font-size: 1.35rem; }
      .shop-grid {
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
      }
    }
    @media (min-width: 900px) {
      .site {
        width: min(100%, 88rem);
        padding-left: 1.75rem;
        padding-right: 1.75rem;
        padding-bottom: 4rem;
      }
      .site-header-inner {
        width: min(100%, 88rem);
        padding-left: 1.75rem;
        padding-right: 1.75rem;
      }
      .hero { margin: 0 -1.75rem 0; }
      .hero-copy { padding: 3rem 2rem 3.25rem; }
      .now-cards { gap: 1.5rem; }
      .now-card {
        min-height: clamp(26rem, 38vw, 32rem);
      }
      .now-card-copy {
        padding: 2.25rem 2rem 2.4rem;
        width: min(52%, 38rem);
      }
      .now-studio {
        top: 1.5rem;
        right: 1.5rem;
      }
      .now-studio-marvel { height: 2.1rem; }
      .now-studio-dc { height: 3rem; width: 3rem; }
      .now-title {
        font-size: clamp(2.4rem, 4.2vw, 4rem);
      }
      .upcoming-grid {
        grid-template-columns: 1fr 1fr;
        gap: 1.25rem;
      }
      .upcoming-card {
        grid-template-columns: 168px 1fr;
      }
      .shop-grid {
        grid-template-columns: 1fr 1fr 1fr;
        gap: 1.1rem;
      }
    }
    @media (min-width: 1280px) {
      .site {
        width: min(100%, 96rem);
        padding-left: 2rem;
        padding-right: 2rem;
      }
      .site-header-inner {
        width: min(100%, 96rem);
        padding-left: 2rem;
        padding-right: 2rem;
      }
      .now-card {
        min-height: clamp(28rem, 30vw, 34rem);
      }
      .now-card-copy {
        width: min(48%, 42rem);
        padding: 2.5rem 2.35rem 2.6rem;
      }
      .now-title {
        font-size: clamp(2.75rem, 3.4vw, 4.25rem);
      }
    }
    @media (min-width: 1600px) {
      .site {
        width: min(100%, 108rem);
      }
      .site-header-inner {
        width: min(100%, 108rem);
      }
      .now-card {
        min-height: clamp(34rem, 32vw, 42rem);
      }
      .now-card-copy {
        width: min(42%, 46rem);
      }
    }
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after { animation: none !important; transition: none !important; }
      .nav, .hero { opacity: 1; }
      .hero-media { transform: none !important; }
      .site-header, .site-header-inner, .site-header-title { transition: none !important; }
    }
'''

HEADER_JS = r'''
(function () {
  var header = document.querySelector('.site-header');
  if (!header) return;
  var ticking = false;
  // Hysteresis avoids sticky-header shrink/grow fighting scrollY near the threshold.
  var ON = 24;
  var OFF = 8;
  var scrolled = false;
  function update() {
    ticking = false;
    var y = window.scrollY || 0;
    if (!scrolled && y > ON) {
      scrolled = true;
      header.classList.add('is-scrolled');
    } else if (scrolled && y < OFF) {
      scrolled = false;
      header.classList.remove('is-scrolled');
    }
  }
  function onScroll() {
    if (!ticking) {
      ticking = true;
      window.requestAnimationFrame(update);
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  update();
})();
'''


def build_html(slate: dict, now_items: list, upcoming: list, today: date) -> str:
    now_html = '\n\n'.join(
        render_now_card(e) for e in now_items
    ) or '      <p class="now-blurb">Nothing currently marked as playing — check back after the next refresh.</p>'
    up_html = '\n\n'.join(render_upcoming_row(e) for e in upcoming) or '        <p class="title-blurb">No remaining dated titles through year-end in the slate.</p>'
    shop_html = ''
    if SHOP_SECTIONS_PATH.exists():
        shop_html = '\n' + SHOP_SECTIONS_PATH.read_text(encoding='utf-8').rstrip() + '\n'
    year = today.year
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(slate.get('page_title', 'Heroes, Villains, & Mavericks'))}</title>
  <meta name="description" content="Comic book movies and series playing now, plus everything lined up through the end of {year}.">
  <meta name="screen-now-generated" content="{today.isoformat()}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans+Flex:opsz,wght@8..144,100..900&display=swap" rel="stylesheet">
  <style>
{CSS}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="site-header-inner">
      <p class="site-header-title">Heroes, Villains &amp; Mavericks <a class="site-header-by" href="https://www.linkedin.com/in/jaidandekar" target="_blank" rel="noopener">by Jai Dandekar</a></p>
      <a class="site-header-portfolio" href="https://indypendee.com/" target="_blank" rel="noopener">View Jai Dandekar’s work →</a>
    </div>
  </header>
  <div class="site">
    <header class="now-stage-head">
      <h2>In theaters &amp; streaming now</h2>
    </header>

    <section class="now-cards" id="now" aria-label="In theaters and streaming now">
{now_html}
    </section>

    <section class="section" id="upcoming">
      <div class="section-head">
        <h2>Coming soon to theaters &amp; streaming</h2>
      </div>
      <div class="upcoming-grid">
{up_html}
      </div>
    </section>
<!-- SHOP_SECTIONS_START -->
{shop_html}<!-- SHOP_SECTIONS_END -->
    <section class="section about" id="about">
      <div class="section-head">
        <h2>Why this exists</h2>
      </div>
      <div class="about-body">
        <p>A vibe-coding project built end-to-end in Cursor — no hand-pushed pixels. It’s a living guide to comic book characters on screen: character deep dives, multiverse variants, what’s playing now, and what’s coming next.</p>
        <p>I made it to stay close to product systems and content craft while following stories I care about — and to show what a design director can ship when the tools do the production work.</p>
        <a class="about-link" href="https://indypendee.com/" target="_blank" rel="noopener">Back to Jai Dandekar’s portfolio →</a>
      </div>
    </section>
    <footer class="footer">
      <span>Built by <a href="https://indypendee.com/" target="_blank" rel="noopener">Jai Dandekar</a>. Poster art and dates via TMDB. Shop links use Amazon product pages when an ASIN is resolved.</span>
    </footer>
  </div>
  <script>
{HEADER_JS}
  </script>
</body>
</html>
"""



def main() -> None:
    parser = argparse.ArgumentParser(description='Refresh Screen Now from TMDB')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--as-of', help='YYYY-MM-DD override for classification')
    args = parser.parse_args()

    cfg = load_config()
    api_key = cfg['tmdb']['api_key']
    user_agent = cfg.get('user_agent') or 'ComicCharacterGuides/1.0'
    slate = json.loads(SLATE_PATH.read_text(encoding='utf-8'))
    today = parse_iso(args.as_of) or date.today()
    cache = load_tmdb_cache()

    resolved = []
    for entry in slate['titles']:
        item = fetch_title(entry, api_key, user_agent, args.verbose, cache)
        bucket = classify(item, today)
        item['bucket'] = bucket
        resolved.append(item)
        if args.verbose:
            rel = item['release'].isoformat() if item.get('release') else '—'
            print(f"  {item['id']:18} {bucket or 'skip':8}  date={rel}")

    save_tmdb_cache(cache)

    # Keep shop sections current from screen_shop.json (SKU art when resolved).
    try:
        from refresh_shop import render_all, load_json as load_shop_json, save_json as save_shop_json, SHOP_PATH
        shop = load_shop_json(SHOP_PATH)
        SHOP_SECTIONS_PATH.write_text(render_all(shop, cfg), encoding='utf-8')
        print(f'Rendered shop sections → {SHOP_SECTIONS_PATH.name}')
    except Exception as exc:
        print(f'Shop sections skipped: {exc}')

    now_items = [i for i in resolved if i['bucket'] == 'now']
    upcoming = sorted(
        [i for i in resolved if i['bucket'] == 'upcoming'],
        key=lambda i: i['release'] or year_end(today),
    )

    html = build_html(slate, now_items, upcoming, today)

    print(f'Now: {len(now_items)} · Upcoming through Dec {today.year}: {len(upcoming)}')
    if args.dry_run:
        print('Dry run — not writing', OUT_PATH)
        return

    OUT_PATH.write_text(html, encoding='utf-8')
    INDEX_PATH.write_text(html, encoding='utf-8')
    print('Wrote', OUT_PATH)


if __name__ == '__main__':
    main()
