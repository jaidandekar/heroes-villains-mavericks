#!/usr/bin/env python3
"""Resolve run covers via the Cursor browser (Open Library + Google Books),
with title-aware matching — avoids first-hit false positives.

Writes local JPGs to <guide>/images/covers/runs/<slug>.jpg
"""
from __future__ import annotations

import base64
import json
import re
import time
from pathlib import Path

ROOT = Path('/Users/jaidandekar')
HERE = ROOT / 'character-guides'
TARGETS = HERE / '.cache' / 'run_cover_targets.json'
OUT_REPORT = HERE / '.cache' / 'run_cover_report.json'

# Injected into the browser; returns [{slug, guide, ok, source, url, b64?, reason?}]
BROWSER_RESOLVER = r'''
async function resolveCovers(targets) {
  function norm(s) {
    return String(s || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  }
  function tokens(s) {
    return norm(s).split(' ').filter(t => t.length > 2 && !['the','and','vol','volume','omnibus'].includes(t));
  }
  function scoreDoc(doc, title) {
    const want = tokens(title);
    const hay = norm([doc.title, doc.subtitle, (doc.author_name||[]).join(' ')].join(' '));
    if (!want.length) return 0;
    let hit = 0;
    for (const t of want) if (hay.includes(t)) hit++;
    let score = hit / want.length;
    // Prefer subtitle / title containing distinctive trailing phrase
    const tail = want.slice(-2).join(' ');
    if (tail && hay.includes(tail)) score += 0.35;
    if (doc.cover_i) score += 0.05;
    return score;
  }
  function pickOl(docs, title) {
    let best = null, bestScore = 0;
    for (const d of docs || []) {
      if (!d.cover_i) continue;
      const s = scoreDoc(d, title);
      if (s > bestScore) { best = d; bestScore = s; }
    }
    if (best && bestScore >= 0.55) return best;
    return null;
  }
  async function imgToB64(url) {
    const resp = await fetch(url);
    if (!resp.ok) return null;
    const buf = await resp.arrayBuffer();
    if (buf.byteLength < 3000) return null;
    const bytes = new Uint8Array(buf);
    let bin = '';
    for (let i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
    return btoa(bin);
  }
  const out = [];
  for (const t of targets) {
    const row = { guide: t.guide, slug: t.slug, title: t.title, ok: false };
    try {
      const olResp = await fetch('https://openlibrary.org/search.json?q=' + encodeURIComponent(t.title) + '&limit=12', {
        headers: { 'Accept': 'application/json' }
      });
      const ol = olResp.ok ? await olResp.json() : null;
      const doc = pickOl((ol && ol.docs) || [], t.title);
      if (doc) {
        const url = 'https://covers.openlibrary.org/b/id/' + doc.cover_i + '-L.jpg';
        const b64 = await imgToB64(url);
        if (b64) {
          row.ok = true; row.source = 'openlibrary'; row.url = url; row.b64 = b64;
          row.matched = [doc.title, doc.subtitle].filter(Boolean).join(': ');
          out.push(row);
          continue;
        }
      }
      // Google Books fallback
      const gResp = await fetch('https://www.googleapis.com/books/v1/volumes?q=' + encodeURIComponent('intitle:' + t.title) + '&maxResults=8', {
        headers: { 'Accept': 'application/json' }
      });
      const g = gResp.ok ? await gResp.json() : null;
      let won = null;
      for (const item of (g && g.items) || []) {
        const info = item.volumeInfo || {};
        const s = scoreDoc({ title: info.title, subtitle: info.subtitle, author_name: info.authors }, t.title);
        const links = info.imageLinks || {};
        const raw = links.extraLarge || links.large || links.medium || links.thumbnail;
        if (s >= 0.55 && raw) {
          won = { url: String(raw).replace('http://', 'https://').replace('&edge=curl', '').replace('zoom=5', 'zoom=1').replace('zoom=2', 'zoom=1'), score: s, matched: info.title };
          if (s >= 0.85) break;
        }
      }
      if (won) {
        const b64 = await imgToB64(won.url);
        if (b64) {
          row.ok = true; row.source = 'google-books'; row.url = won.url; row.b64 = b64; row.matched = won.matched;
          out.push(row);
          continue;
        }
      }
      row.reason = doc ? 'image-download-failed' : 'no-confident-match';
      out.push(row);
    } catch (e) {
      row.reason = String(e && e.message || e);
      out.push(row);
    }
  }
  return out;
}
'''


def main() -> int:
    targets = json.loads(TARGETS.read_text(encoding='utf-8'))
    print(f'{len(targets)} targets — resolve in browser, then write files')
    # Print a payload the agent will feed to CDP in chunks
    chunk_size = 8
    chunks = [targets[i:i + chunk_size] for i in range(0, len(targets), chunk_size)]
    meta = {
        'chunk_count': len(chunks),
        'chunk_size': chunk_size,
        'resolver_ready': True,
    }
    (HERE / '.cache' / 'run_cover_chunks.json').write_text(json.dumps(chunks), encoding='utf-8')
    (HERE / '.cache' / 'run_cover_resolver.js').write_text(BROWSER_RESOLVER, encoding='utf-8')
    print(json.dumps(meta))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
