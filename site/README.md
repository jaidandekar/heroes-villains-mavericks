# Heroes, Villains, & Mavericks — upload this folder

Everything for the live site is here:

- `heroesvillainsmavericks.html` — main page (open this)
- `*-guide/` — character reading guides
- `assets/` — studio logos and shop media

## Maintenance

- **Movie / streaming dates are frozen** — no automatic TMDB refresh loop.
- **Bestsellers** (comics, toys, games): update on demand from `../character-guides/`:

```bash
cd ../character-guides
python3 refresh_shop.py
```

That patches shop sections into the live page without changing Now/Upcoming dates.
