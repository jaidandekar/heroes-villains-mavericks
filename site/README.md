# Heroes, Villains, & Mavericks — public site folder

Published by GitHub Pages from this `site/` directory.

- `index.html` — main page (GitHub Pages home)
- `heroesvillainsmavericks.html` — same landing (kept for guide “back” links)
- `*-guide/` — character reading guides
- `assets/` — studio logos and shop media

## Maintenance

- **Movie / streaming dates are frozen** — no automatic TMDB refresh loop.
- **Bestsellers** (comics, toys, games): from `../tools/`:

```bash
cd ../tools
python3 refresh_shop.py
```

That patches shop sections into the live page without changing Now/Upcoming dates.
Push to `main` afterward so GitHub Pages redeploys.
