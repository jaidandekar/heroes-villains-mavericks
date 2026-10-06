# Heroes, Villains, & Mavericks

Personal comics hub — character guides, Multiverse art, and Screen Now shop sections.

## Layout

| Path | What it is |
|------|------------|
| `site/` | **Upload this folder** to your live host (`heroesvillainsmavericks.html` + `*-guide/`) |
| `tools/` | Generators and refresh scripts (`generate_guides.py`, `refresh_shop.py`, etc.) |

## Secrets

Copy `tools/config.example.json` → `tools/config.json` and add your API keys locally.  
`tools/config.json` is gitignored and must never be committed.

## Common commands

```bash
cd tools
python3 generate_guides.py          # rebuild all guides into site/
python3 refresh_shop.py             # patch bestsellers into the landing page
python3 refresh_finale_covers.py    # Multiverse final-issue covers (needs Comic Vine key)
```

## GitHub

Private repo. Ask Cursor to refresh content and push when you want updates on GitHub.  
Pushing here updates GitHub only — your live host still needs upload **or** a connected host (Pages/Netlify/etc.).
