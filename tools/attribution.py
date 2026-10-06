#!/usr/bin/env python3
"""Attribution footer for cover / poster sources used by the guides.

Comic Vine and TMDB require a link-back. Open Library, Amazon product images,
and Google Books are also credited when used by refresh_covers.py.

ensure_attribution() is idempotent for guides that already have the marker,
but will refresh the footer text when the marker is present so source copy
stays current after pipeline changes.
"""
from __future__ import annotations

import re

MARKER = 'data-attribution="sources"'

STYLE_ANCHOR = '  </style>'

STYLE_BLOCK = """
    /* ── Source attribution ── */
    .source-attribution {
      max-width: var(--max-width, 1240px);
      margin: 0 auto;
      padding: 2rem 1.5rem 3rem;
      border-top: 1px solid var(--border);
      font-size: 0.75rem;
      line-height: 1.6;
      color: var(--muted);
    }

    .source-attribution a {
      color: var(--muted);
      text-decoration: underline;
      text-underline-offset: 2px;
    }

    .source-attribution a:hover { color: var(--text); }
"""

FOOTER_HTML = """  <footer class="source-attribution" data-attribution="sources">
    <p>Collected-edition covers via <a href="https://openlibrary.org/" target="_blank" rel="noopener">Open Library</a>,
    <a href="https://www.amazon.com/" target="_blank" rel="noopener">Amazon</a> product images, and
    <a href="https://books.google.com/" target="_blank" rel="noopener">Google Books</a>,
    with additional comic art via <a href="https://comicvine.gamespot.com/" target="_blank" rel="noopener">Comic Vine</a>.
    Film and TV posters via <a href="https://www.themoviedb.org/" target="_blank" rel="noopener">TMDB</a>, which does not endorse this project.
    Character facts via <a href="https://www.wikipedia.org/" target="_blank" rel="noopener">Wikipedia</a>.</p>
    <p>This is a non-commercial fan project. All characters, cover art, and trademarks are the property of their respective publishers.</p>
  </footer>
"""


def ensure_attribution(html: str) -> str:
    """Ensure the attribution footer and its styles are present and up to date."""
    if STYLE_ANCHOR in html and '.source-attribution' not in html:
        html = html.replace(STYLE_ANCHOR, STYLE_BLOCK + STYLE_ANCHOR, 1)

    if MARKER in html:
        html = re.sub(
            r'<footer class="source-attribution"[^>]*>.*?</footer>\s*',
            FOOTER_HTML,
            html,
            count=1,
            flags=re.DOTALL,
        )
        return html

    if '</body>' in html:
        html = html.replace('</body>', FOOTER_HTML + '</body>', 1)

    return html
