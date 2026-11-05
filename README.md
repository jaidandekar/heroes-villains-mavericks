# Heroes, Villains, & Mavericks

Personal comics hub — character guides, Multiverse art, and Screen Now shop sections.

## Live site (GitHub Pages)

After Pages is enabled, the public URL is:

**https://jaidandekar.github.io/heroes-villains-mavericks/**

Production deployment is a manual GitHub Actions dispatch from `main`. Get explicit owner approval for the exact revision before dispatching **Deploy site to GitHub Pages**. A normal push runs no production deployment once the manual-only workflow is in `main`.

> Free GitHub Pages requires a **public** repository (or a paid GitHub plan for private Pages).

## Layout

| Path | What it is |
|------|------------|
| `site/` | Public website (what Pages publishes) |
| `tools/` | Content packs, generators, refresh scripts, and offline checks |
| `preview/` | Layout prototype; outside the Pages artifact |

## Secrets

Copy `tools/config.example.json` → `tools/config.json` and add API keys locally.  
`tools/config.json` is gitignored — never commit it.

## Development checks

From the repository root (Python 3.12 matches CI):

```bash
python3 -B tools/check_project.py
python3 -B -m unittest discover -s tools/tests -v
python3 -B tools/test_resolver.py
```

These checks are offline and require no credentials. They check legacy routes, static local references, homepage alias parity, guide regeneration, and maintenance write boundaries. They do not exercise browser interactions or verify third-party images and availability.

## Maintenance commands

```bash
python3 -B tools/generate_guides.py --check  # no writes
python3 -B tools/generate_guides.py         # regenerate guides and inventory
python3 -B tools/refresh_screen_now.py --dry-run  # may contact TMDB; no files written
python3 -B tools/refresh_shop.py            # update both homepage files
```

See [Development and release notes](docs/development.md) before changing content or releasing.
