# Heroes, Villains, & Mavericks

Personal comics hub — character guides, Multiverse art, and Screen Now shop sections.

## Live site (GitHub Pages)

After Pages is enabled, the public URL is:

**https://jaidandekar.github.io/heroes-villains-mavericks/**

Every push to `main` that changes `site/` deploys automatically via GitHub Actions.

> Free GitHub Pages requires a **public** repository (or a paid GitHub plan for private Pages).

## Layout

| Path | What it is |
|------|------------|
| `site/` | Public website (what Pages publishes) |
| `tools/` | Generators and refresh scripts |

## Secrets

Copy `tools/config.example.json` → `tools/config.json` and add API keys locally.  
`tools/config.json` is gitignored — never commit it.

## Common commands

```bash
cd tools
python3 generate_guides.py
python3 refresh_shop.py
python3 refresh_finale_covers.py --dry-run
```
