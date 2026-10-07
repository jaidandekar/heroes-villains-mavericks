#!/usr/bin/env python3
"""Generate character reading guides from the current Batman template."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from attribution import ensure_attribution
from packs_dc import DC_PACKS
from packs_marvel import MARVEL_PACKS
from packs_xmen import XMEN_PACKS
from packs_image import IMAGE_PACKS
from packs_marvel_more import MARVEL_MORE_PACKS
from packs_screen import SCREEN_PACKS

TOOLS = Path(__file__).resolve().parent
REPO = TOOLS.parent
SITE_ROOT = REPO / 'site'
ROOT = SITE_ROOT  # generated guides + public site live here
TEMPLATE = TOOLS / 'templates' / 'batman-guide' / 'index.html'

# Only guides linked from heroesvillainsmavericks / the Screen Now slate.
# Template lives under character-guides/templates/batman-guide (not a public guide).
ACTIVE_GUIDE_IDS = {
    'green-lantern',
    'spiderman',
    'supergirl',
    'clayface',
    'vision',
    'x-men',
    'avengers',
    'doctor-doom',
}

# Wide TMDB art used as the primary remote hero when a local header file is missing.
HERO_TMDB = {
    'green-lantern': 'https://image.tmdb.org/t/p/w1280/6gqezQJ2mkm4jreWwLyOZy2Vf6i.jpg',
    'spiderman': 'https://image.tmdb.org/t/p/w1280/qeQJx07rK2xm8SD2sJxFKhE7gs0.jpg',
    'supergirl': 'https://image.tmdb.org/t/p/w1280/54KIfdTEzOliHDKx0OkzYGqAICx.jpg',
    'x-men': 'https://image.tmdb.org/t/p/w1280/jIyEmnBrZtl6SEWyBoMO2hZnzMa.jpg',
    'avengers': 'https://image.tmdb.org/t/p/w1280/ulzhLuWrPK07P1YkdWQLZnQh1JL.jpg',
    'vision': 'https://image.tmdb.org/t/p/w1280/xK27l5uwaVyZSlENWnmLlWwDQNS.jpg',
    'clayface': 'https://image.tmdb.org/t/p/w1280/5jCpQnWPikggmQZoDp1eAi6BI6w.jpg',
    'doctor-doom': 'https://image.tmdb.org/t/p/w1280/jzPwsojjFStf5lR5Nm07w2hH56G.jpg',
}


def hero_remote_sources(pack_id: str) -> list[str]:
    url = HERO_TMDB.get(pack_id)
    return [url] if url else []

_ALL_PACKS = (
    DC_PACKS + MARVEL_PACKS + XMEN_PACKS + IMAGE_PACKS + MARVEL_MORE_PACKS + SCREEN_PACKS
)
ALL_GENERATED_PACKS = [p for p in _ALL_PACKS if p['id'] in ACTIVE_GUIDE_IDS]


def js_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def emit_run_isbn(runs: dict) -> str:
    lines = ['    const RUN_ISBN = {']
    for slug, r in runs.items():
        isbn = r.get('isbn')
        if isbn:
            lines.append(f'      {js_str(slug)}: {js_str(isbn)},')
    if len(lines) == 1:
        return '    const RUN_ISBN = {};'
    lines.append('    };')
    return '\n'.join(lines)


def emit_versions(versions: list) -> str:
    parts = ['    const versions = [']
    for v in versions:
        runs = ','.join(js_str(x) for x in v['runs'])
        parts.append(
            '      { slug: %s, name: %s, universe: %s, type: %s, firstAppearance: %s, '
            'tagline: %s, description: %s, wikipedia: %s, runs: [%s] },'
            % (
                js_str(v['slug']), js_str(v['name']), js_str(v['universe']), js_str(v['type']),
                js_str(v['firstAppearance']), js_str(v['tagline']), js_str(v['description']),
                js_str(v['wikipedia']), runs,
            )
        )
    parts.append('    ];')
    return '\n'.join(parts)


def emit_runs(runs: dict) -> str:
    parts = ['    const runs = {']
    for slug, r in runs.items():
        amazon = r['amazon'][0]
        reading = r['readingOrder'][0] if r.get('readingOrder') else r['title']
        parts.append(
            '      %s: { slug: %s, versionSlug: %s, title: %s, creators: %s, years: %s, '
            'collects: %s, era: %s, prerequisites: %s, summary: %s, readingOrder: [%s], '
            'amazon: [{ asin: %s, title: %s, format: %s, recommended: true }] },'
            % (
                js_str(slug), js_str(r['slug']), js_str(r['versionSlug']), js_str(r['title']),
                js_str(r['creators']), js_str(r['years']), js_str(r['collects']), js_str(r['era']),
                js_str(r['prerequisites']), js_str(r['summary']), js_str(reading),
                js_str(amazon['asin']), js_str(amazon['title']), js_str(amazon.get('format', 'Trade Paperback')),
            )
        )
    parts.append('    };')
    return '\n'.join(parts)


def emit_run_issues(issues: dict) -> str:
    if not issues:
        return '    const RUN_ISSUES = {};'
    parts = ['    const RUN_ISSUES = {']
    for slug, data in issues.items():
        if isinstance(data, dict):
            iss = data['issues']
            note = data.get('note')
            iss_js = ', '.join('{ id: %s, title: %s }' % (js_str(i['id']), js_str(i['title'])) for i in iss)
            if note:
                parts.append('      %s: { note: %s, issues: [%s] },' % (js_str(slug), js_str(note), iss_js))
            else:
                parts.append('      %s: { issues: [%s] },' % (js_str(slug), iss_js))
        else:
            iss_js = ', '.join('{ id: %s, title: %s }' % (js_str(i['id']), js_str(i['title'])) for i in data)
            parts.append('      %s: [%s],' % (js_str(slug), iss_js))
    parts.append('    };')
    return '\n'.join(parts)


def emit_profile(profile: dict) -> str:
    facts = ',\n        '.join(
        '{ label: %s, value: %s }' % (js_str(f['label']), js_str(f['value'])) for f in profile['facts']
    )
    return (
        '    const BATMAN_PROFILE = {\n'
        '      wikipedia: %s,\n'
        '      lead: %s,\n'
        '      summary: %s,\n'
        '      facts: [\n'
        '        %s\n'
        '      ]\n'
        '    };'
    ) % (js_str(profile['wikipedia']), js_str(profile['lead']), js_str(profile['summary']), facts)


def emit_home_runs(slugs: list) -> str:
    # Keep lines readable: 4 per line
    chunks = []
    for i in range(0, len(slugs), 4):
        chunks.append(', '.join(js_str(s) for s in slugs[i:i + 4]))
    inner = ',\n      '.join(chunks)
    return '    const HOME_ESSENTIAL_RUNS = [\n      %s\n    ];' % inner


def emit_screen(groups: list) -> str:
    parts = ['    const BATMAN_SCREEN = [']
    for g in groups:
        parts.append('      {')
        parts.append('        group: %s,' % js_str(g['group']))
        parts.append('        items: [')
        for it in g['items']:
            extra = ''
            if 'year' in it and it['year']:
                extra += ', year: %s' % js_str(it['year'])
            if 'years' in it and it['years']:
                extra += ', years: %s' % js_str(it['years'])
            parts.append(
                '          { id: %s, title: %s%s, note: %s, wikipedia: %s, imdb: %s },'
                % (js_str(it['id']), js_str(it['title']), extra, js_str(it['note']),
                   js_str(it['wikipedia']), js_str(it['imdb']))
            )
        parts.append('        ]')
        parts.append('      },')
    parts.append('    ];')
    return '\n'.join(parts)


def emit_type_labels(labels: dict) -> str:
    lines = ['    const typeLabels = {']
    for k, v in labels.items():
        lines.append('      %s: %s,' % (js_str(k), js_str(v)))
    lines.append('    };')
    return '\n'.join(lines)


def emit_themes(themes: dict) -> str:
    lines = ['    var FEATURED_THEME_COLORS = {']
    for k, c in themes.items():
        r, g, b = c
        lines.append('      %s: { r: %d, g: %d, b: %d },' % (js_str(k), r, g, b))
    lines.append('    };')
    return '\n'.join(lines)


def load_version_art() -> dict:
    path = Path(__file__).resolve().parent / 'version_art.json'
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (json.JSONDecodeError, OSError):
        return {}


def emit_version_art(pack_id: str) -> str:
    art = load_version_art().get(pack_id) or {}
    if not art:
        return '    const VERSION_ART = {};'
    lines = ['    const VERSION_ART = {']
    for slug, url in art.items():
        lines.append('      %s: %s,' % (js_str(slug), js_str(url)))
    lines.append('    };')
    return '\n'.join(lines)


def splice(text: str, start: str, end: str, new_block: str, label: str) -> str:
    s = text.find(start)
    if s < 0:
        raise SystemExit('MISSING START: ' + label)
    e = text.find(end, s)
    if e < 0:
        raise SystemExit('MISSING END: ' + label)
    return text[:s] + new_block + text[e:]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit('MISSING ANCHOR: ' + label + ' :: ' + old[:80])
    if text.count(old) != 1:
        raise SystemExit('NON-UNIQUE (%d): %s' % (text.count(old), label))
    return text.replace(old, new)


def filter_buttons(types: dict) -> str:
    # Keep All + each type key
    btns = ["'<button class=\"filter-btn active\" data-filter=\"all\">All</button>'"]
    for key, label in types.items():
        btns.append("'<button class=\"filter-btn\" data-filter=\"%s\">%s</button>'" % (key, label))
    # Join as JS string concatenation matching template style
    lines = []
    for i, b in enumerate(btns):
        if i == 0:
            lines.append("        '<div class=\"filters\">' +")
            lines.append('        ' + b + ' +')
        elif i < len(btns) - 1:
            lines.append('        ' + b + ' +')
        else:
            lines.append('        ' + b + ' + "</div>" +')
    # Actually original uses separate buttons without closing in last - look at batman
    # Batman:
    # '<div class="filters">' +
    # '<button ...>All</button>' +
    # ...
    # '<button ...>Future</button></div>' +
    out = ["        '<div class=\"filters\">' +"]
    keys = list(types.items())
    out.append("        '<button class=\"filter-btn active\" data-filter=\"all\">All</button>' +")
    for i, (key, label) in enumerate(keys):
        if i == len(keys) - 1:
            out.append(
                "        '<button class=\"filter-btn\" data-filter=\"%s\">%s</button></div>' +"
                % (key, label)
            )
        else:
            out.append(
                "        '<button class=\"filter-btn\" data-filter=\"%s\">%s</button>' +"
                % (key, label)
            )
    return '\n'.join(out)


def transform(template: str, char: dict) -> str:
    t = template
    cid = char['id']
    folder = cid + '-guide'
    top_html = cid + '-guide.html'
    brand = char['brand']

    t = replace_once(
        t,
        '<title>Batman — The Dark Knight in Every Form</title>',
        '<title>%s</title>' % char['title'],
        'title',
    )

    old_header = (
        '  <header class="site-chrome">\n'
        '    <div class="site-header">\n'
        '      <div class="site-header-inner">\n'
        '        <a class="site-header-title" href="../heroesvillainsmavericks.html">Heroes, Villains, &amp; Mavericks</a>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="guide-bar">\n'
        '      <div class="guide-bar-inner">\n'
        '        <div class="guide-bar-brand">\n'
        '          <a class="guide-back" href="../heroesvillainsmavericks.html" aria-label="Back to Heroes, Villains, &amp; Mavericks">←</a>\n'
        '          <a href="#home" class="logo">Learn more about Batman</a>\n'
        '        </div>\n'
        '        <nav>\n'
        '          <a href="#who-is-batman">Who is Batman</a>\n'
        '          <a href="#verses">Verses</a>\n'
        '          <a href="#graphic-novels">Comics</a>\n'
        '          <a href="#on-screen">Film &amp; TV</a>\n'
        '        </nav>\n'
        '      </div>\n'
        '    </div>\n'
        '  </header>'
    )
    new_header = (
        '  <header class="site-chrome">\n'
        '    <div class="site-header">\n'
        '      <div class="site-header-inner">\n'
        '        <a class="site-header-title" href="../heroesvillainsmavericks.html">Heroes, Villains, &amp; Mavericks</a>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="guide-bar">\n'
        '      <div class="guide-bar-inner">\n'
        '        <div class="guide-bar-brand">\n'
        '          <a class="guide-back" href="../heroesvillainsmavericks.html" aria-label="Back to Heroes, Villains, &amp; Mavericks">←</a>\n'
        '          <a href="#home" class="logo">Learn more about %s</a>\n'
        '        </div>\n'
        '        <nav>\n'
        '          <a href="#%s">%s</a>\n'
        '          <a href="#verses">%s</a>\n'
        '          <a href="#graphic-novels">Comics</a>\n'
        '          <a href="#on-screen">Film &amp; TV</a>\n'
        '        </nav>\n'
        '      </div>\n'
        '    </div>\n'
        '  </header>'
    ) % (brand, char['who_id'], char['nav_who'], char['nav_verses'])
    t = replace_once(t, old_header, new_header, 'header')

    data = '\n'.join([
        emit_run_isbn(char['runs']),
        '',
        emit_versions(char['versions']),
        '',
        emit_runs(char['runs']),
        '',
        emit_run_issues(char.get('issues') or {}),
        '',
        '    /* Per-issue cover art — local: images/covers/issues/{coverSlug}.jpg */',
        '    const ISSUE_COVER_OVERRIDES = {};',
        '',
        '    /* Curated cover URLs — tried first when available */',
        '    const COVER_OVERRIDES = {};',
        '',
        '    /* Character art when a run cover is unavailable (version cards) */',
        emit_version_art(char['id']),
        '',
        '',
    ])
    t = splice(t, '    const RUN_ISBN = {', '    const COVER_SOURCES = {};', data, 'data region')

    t = replace_once(
        t,
        "/* Resolve image folder whether you open batman-guide/index.html or ~/batman-guide.html */",
        "/* Resolve image folder whether you open %s/index.html or ~/%s */" % (folder, top_html),
        'imageRoot comment',
    )
    t = replace_once(
        t,
        "if (filename === 'batman-guide.html') return 'batman-guide/images/';",
        "if (filename === '%s') return '%s/images/';" % (top_html, folder),
        'imageRoot check',
    )

    # Empty poster maps (Wikipedia/TVMaze hydrate)
    posters = (
        '    const SCREEN_TMDB_POSTERS = {};\n\n'
        '    /* TVMaze poster URLs — reliable fallback for TV series */\n'
        '    const SCREEN_TVMAZE_POSTERS = {};\n\n'
    )
    t = splice(t, '    const SCREEN_TMDB_POSTERS = {', '    var WIKI_POSTER_CACHE = {};', posters, 'screen posters')

    # Clear local aliases (Batman-specific)
    # Find RUN_LOCAL_ALIASES block
    m = re.search(r'    const RUN_LOCAL_ALIASES = \{.*?\n    \};', t, re.S)
    if not m:
        raise SystemExit('MISSING RUN_LOCAL_ALIASES')
    t = t[:m.start()] + '    const RUN_LOCAL_ALIASES = {};' + t[m.end():]

    m = re.search(r'    const VERSION_LOCAL_ALIASES = \{.*?\n    \};', t, re.S)
    if not m:
        raise SystemExit('MISSING VERSION_LOCAL_ALIASES')
    t = t[:m.start()] + '    const VERSION_LOCAL_ALIASES = {};' + t[m.end():]

    m = re.search(r'    const typeLabels = \{.*?\n    \};', t, re.S)
    if not m:
        raise SystemExit('MISSING typeLabels')
    t = t[:m.start()] + emit_type_labels(char['types']) + t[m.end():]

    m = re.search(r'    var FEATURED_THEME_COLORS = \{.*?\n    \};', t, re.S)
    if not m:
        raise SystemExit('MISSING FEATURED_THEME_COLORS')
    t = t[:m.start()] + emit_themes(char['themes']) + t[m.end():]

    profile_block = '\n\n'.join([
        emit_profile(char['profile']),
        '',
        '    /* Best-selling / landmark graphic novels & runs for the home page */',
        emit_home_runs(char['home_runs']),
        '',
        '    /* On screen — live action & animated */',
        emit_screen(char['screen']),
        '',
        '',
    ])
    t = splice(t, '    const BATMAN_PROFILE = {', '    function renderWhoIsBatman() {', profile_block, 'profile')

    # Who-is branding + hero image cascade
    t = replace_once(
        t,
        "    const HERO_REMOTE_SOURCES = [];",
        "    const HERO_REMOTE_SOURCES = %s;" % json.dumps(hero_remote_sources(char['id']), ensure_ascii=False),
        'hero remote sources',
    )
    t = replace_once(
        t,
        "      var localHero = imageRoot() + 'batman-homepage-header-image.jpg';",
        "      var localHero = imageRoot() + %s;" % js_str(char['header_img']),
        'header img',
    )
    t = replace_once(
        t,
        "      return '<section class=\"home-section\" id=\"who-is-batman\">' +",
        "      return '<section class=\"home-section\" id=\"%s\">' +" % char['who_id'],
        'who section id',
    )
    t = replace_once(
        t,
        "      var gradient = 'radial-gradient(circle at 30% 25%, #1c2430, #0a0c10 55%, #000)';",
        "      var gradient = %s;" % js_str(char['hero_gradient']),
        'hero gradient',
    )
    t = replace_once(
        t,
        "        '<img src=\"' + imgSrc + '\" alt=\"Batman\" loading=\"eager\" referrerpolicy=\"no-referrer\" ' +",
        "        '<img src=\"' + imgSrc + '\" alt=\"%s\" loading=\"eager\" referrerpolicy=\"no-referrer\" ' +" % brand.replace("'", "\\'"),
        'banner img alt',
    )
    t = replace_once(
        t,
        "        '<h1>Who is Batman?</h1>' +",
        "        '<h1>%s?</h1>' +" % char['nav_who'],
        'who h1',
    )

    # Verses section header (no type filters)
    old_verses = (
        "        '<h2>Batman in Different Verses</h2>' +\n"
        "        '<p>All ' + versions.length + ' versions across DC\\'s multiverse — Prime Earth, Elseworlds, the far future, and every alternate Dark Knight.</p>' +\n"
        "        '</div><span class=\"section-badge\">' + versions.length + ' versions</span></div>' +"
    )
    new_verses = (
        "        '<h2>%s</h2>' +\n"
        "        '<p>All ' + versions.length + ' %s</p>' +\n"
        "        '</div><span class=\"section-badge\">' + versions.length + ' versions</span></div>' +"
    ) % (char['verses_h2'], char['verses_p'].replace("'", "\\'"))
    t = replace_once(t, old_verses, new_verses, 'verses section')

    t = replace_once(
        t,
        "        '<p>The most essential, best-selling Batman stories in print — from Frank Miller\\'s Year One and Dark Knight Returns to modern classics like Court of Owls and Hush.</p>' +",
        "        '<p>%s</p>' +" % char['comics_p'].replace("'", "\\'"),
        'comics copy',
    )
    t = replace_once(
        t,
        "        '<p>Every major live-action and animated appearance — from the 1966 camp classic and Burton films to the DCAU, Nolan trilogy, and The Batman.</p>' +",
        "        '<p>%s</p>' +" % char['screen_p'].replace("'", "\\'"),
        'screen copy',
    )

    # Soft scrub leftover bat emoji placeholder if any
    t = t.replace('\U0001F9A6', '\u2728')

    # Source attribution required by the Comic Vine / TMDB terms of use
    t = ensure_attribution(t)

    return t


def write_guide(char: dict, template: str) -> Path:
    cid = char['id']
    folder = ROOT / (cid + '-guide')
    images = folder / 'images' / 'covers'
    for sub in ('runs', 'versions', 'issues', 'screen'):
        (images / sub).mkdir(parents=True, exist_ok=True)

    html = transform(template, char)
    index_path = folder / 'index.html'
    index_path.write_text(html, encoding='utf-8')
    return index_path


def main():
    template = TEMPLATE.read_text(encoding='utf-8')
    packs = ALL_GENERATED_PACKS
    print('Template bytes:', len(template))
    print('Generating', len(packs), 'guides...')
    for char in packs:
        path = write_guide(char, template)
        # quick sanity
        text = path.read_text(encoding='utf-8')
        assert char['brand'] in text
        assert 'const versions = [' in text
        assert 'BATMAN_PROFILE' in text  # shared engine name
        assert '../heroesvillainsmavericks.html' in text
        assert 'Learn more about %s' % char['brand'] in text
        assert 'site-chrome' in text
        assert 'guide-back' in text
        print('  OK', char['id'], '->', path, '(%d bytes)' % path.stat().st_size)

    # Index README
    readme = HOME / 'character-guides' / 'GENERATED.md'
    lines = [
        '# Generated character guides\n\n',
        'Built from `character-guides/templates/batman-guide/index.html`.\n\n',
        '| Character | Folder |\n',
        '|-----------|--------|\n',
    ]
    for char in packs:
        lines.append('| %s | `%s-guide/` |\n' % (char['brand'], char['id']))
    lines.append(
        '\nLimited to Screen Now companions. See `UPLOAD.md` for the public upload set;\n'
        'unused drafts live in `archive/`.\n'
    )
    readme.write_text(''.join(lines), encoding='utf-8')
    print('Wrote', readme)


if __name__ == '__main__':
    main()
