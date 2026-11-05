# Editorial site

The homepage and ten featured guides share the Astro layout. The other guides are carried forward from `site/` in the release build.

From this directory, run `pnpm install --frozen-lockfile` and `pnpm build`. Open `dist/index.html` in a browser. To reimport the existing guide data and local artwork, run `python3 -B import-preview.py` before building.

To assemble a Pages artifact after building, run:

```sh
python3 -B scripts/prepare-release.py --public-url https://jaidandekar.github.io/heroes-villains-mavericks/ --output release
```

The output directory must be new. The release builder preserves the homepage alias, existing guide routes, and reading anchors. It adds canonical URLs and checks local references. The Pages workflow builds this artifact with the base URL reported by GitHub Pages. Production deployment requires owner approval and a manual dispatch from `main`.
