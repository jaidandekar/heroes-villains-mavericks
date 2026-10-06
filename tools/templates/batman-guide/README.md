# Batman Reading Guide

A static multiverse Batman catalog. Characters are curated for strong Wikipedia coverage (dedicated articles, linkable art, documented media). Each character page shows major runs, issue inventories with optional per-issue cover art, and IMDb/Wikipedia links for TV and film where applicable.

## Open the site

**Use the project folder** (required for local cover images):

```
batman-guide/index.html
```

Open in your browser: double-click `index.html`, or from Terminal:

```bash
open /Users/jaidandekar/batman-guide/index.html
```

> The older `~/batman-guide.html` file still works but won't find local images unless you run the download script into `~/images/covers/`.

## Download cover art (recommended)

Local covers load instantly and don't depend on external CDNs. Run once (or after adding new runs):

```bash
cd /Users/jaidandekar/batman-guide
python3 scripts/download-covers.py
```

This tries each source in order until one works:

1. Wikipedia / Wikimedia (curated URLs)
2. Open Library (ISBN)
3. Google Books (ISBN)
4. Amazon (ASIN)

Files are saved to:

- `images/covers/runs/{slug}.jpg` — comic run covers
- `images/covers/versions/{slug}.jpg` — character card art
- `images/covers/issues/{coverSlug}.jpg` — individual issue covers (e.g. `bb99-1.jpg` for Batman Beyond #1)

The site tries **local files first**, then falls back to live external URLs in the browser.

## Why local bundling instead of Comic Vine API?

| Approach | Pros | Cons |
|----------|------|------|
| **Local bundled covers** ✓ | No API key, no CORS, works offline, fast, fine for static hosting | One-time download step; ~2MB of images |
| **Comic Vine API** | Great metadata | Requires API key; **blocked from browser** (CORS); key would be exposed in client code; needs a backend proxy |
| **Live external only** | No setup | Many missing/broken covers; depends on third-party uptime |

For a single HTML static site, **local bundling is the right call**. Comic Vine makes sense if you later add a small backend (Node/Python) to proxy API requests.

## Project structure

```
batman-guide/
├── index.html          # The site
├── images/covers/      # Downloaded art (run script above)
├── scripts/
│   ├── download-covers.py   # Python (recommended)
│   └── download-covers.mjs  # Node alternative
└── README.md
```

## Affiliate tag

Replace `YOURTAG-20` in `index.html` with your Amazon Associates tracking ID.
