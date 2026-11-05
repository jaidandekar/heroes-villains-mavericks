"""Export pilot data from the existing guides without changing them."""
from pathlib import Path
import json
import shutil
import sys

root = Path(__file__).resolve().parent
repo = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else root.parent
sys.path.insert(0, str(repo / 'tools'))
import generate_guides as guides

site = repo / 'site'
media = root / 'public' / 'media'
media.mkdir(parents=True, exist_ok=True)
for name in ['lanterns', 'vision', 'doomsday', 'beyond', 'clayface']:
    shutil.copyfile(repo / 'preview' / 'art' / f'{name}.jpg', media / f'{name}.jpg')
covers = guides.load_reading()['covers']
result = {}
lineup = {entry["id"] for entry in json.loads((root / "src/data/guide-shelf.json").read_text())}
version_art = json.loads((repo / "tools/version_art.json").read_text())
art_sources = json.loads((root / 'src/data/art-sources.json').read_text())

for pack in guides.ALL_GENERATED_PACKS:
    slug = pack['id']
    if slug not in lineup:
        continue
    runs = []
    for run in pack['runs'].values():
        key = run['slug']
        local = site / f'{slug}-guide' / 'images/covers/runs' / f'{key}.jpg'
        cover = covers.get(key) or (f"https://covers.openlibrary.org/b/isbn/{run['isbn']}-L.jpg?default=false" if run.get("isbn") else None)
        if key in art_sources and (media / (key + ".jpg")).is_file():
            cover = f"media/{key}.jpg"
        elif local.is_file():
            shutil.copyfile(local, media / local.name)
            cover = f'media/{local.name}'
        runs.append({**run, 'cover': cover})
    result[slug] = dict(pack, runs=runs, versionArt=version_art.get(slug, {}))
(root / 'src/data/guides.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
