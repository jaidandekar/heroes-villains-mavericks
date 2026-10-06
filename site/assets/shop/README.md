# Screen Now shop product images

Related bestsellers must be **SKU-tied** (Amazon ASIN) and dynamically resolved.
See `.cursor/rules/related-bestsellers-sku.mdc`.

Movie/streaming dates on the main page are **not** auto-refreshed. Shop sections
are updated separately via `refresh_shop.py`.

## Comics
ISBN → Open Library cover is fine for art. Prefer resolving an `asin` so the
card links to `/dp/ASIN` instead of a search page.

## Toys
Require `asin` + official packaging `image`. Resolve via Amazon search/API:

```bash
cd ../../character-guides
python3 refresh_shop.py --merge-resolutions .cache/toy_resolutions.json
python3 refresh_shop.py --resolve-toys   # when config.json has amazon.* keys
```

## Games
Require `asin` for the durable link; box art must be that named title.

## Apply shop updates to the live page
```bash
cd ../../character-guides
python3 refresh_shop.py
```
Patches comics/toys/games sections without reclassifying Now/Upcoming dates.
