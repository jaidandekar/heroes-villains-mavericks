#!/usr/bin/env python3
"""Download cover art into images/covers/. Run: python3 scripts/download-covers.py [--screen-only]"""
import json
import os
import re
import shutil
import ssl
import sys
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS_DIR = os.path.join(ROOT, "images/covers/runs")
VERSIONS_DIR = os.path.join(ROOT, "images/covers/versions")
SCREEN_DIR = os.path.join(ROOT, "images/covers/screen")
INDEX_HTML = os.path.join(ROOT, "index.html")
UA = {"User-Agent": "BatmanGuide/1.0 (local cover downloader)"}

RUN_ISBN = {
    "year-one": "9781401207526",
    "long-halloween": "9781401232597",
    "dark-victory": "9781401233309",
    "killing-joke": "9781401284272",
    "death-in-the-family": "9781401293623",
    "knightfall": "9781401233217",
    "no-mans-land": "9781401295277",
    "hush": "9781401297244",
    "under-the-red-hood": "9781401231453",
    "batman-rip": "9781401220325",
    "court-of-owls": "9781401235420",
    "death-of-the-family": "9781401242370",
    "earth-two-golden-age": "9781563890433",
    "dark-knight-returns": "9781563893421",
    "flashpoint-knight-of-vengeance": "9781401234054",
    "crime-syndicate": "9781401249367",
    "red-rain": "9781563890369",
    "hush-beyond": "9781401229887",
    "earth-2-planetfall": "9781401242819",
    "batman-who-laughs": "9781779504463",
    "grim-knight": "9781779504463",
    "red-death": "9781401289072",
    "dawnbreaker": "9781401289072",
    "murder-machine": "9781401289072",
    "gotham-by-gaslight": "9781779524058",
    "white-knight": "9781401274527",
    "thrillkiller": "9781401204214",
    "holy-terror": "9781563892034",
    "batman-66-vol-1": "9781401244737",
    "in-darkest-knight": "9781563891266",
    "the-drowned": "9781401289072",
}

RUN_ASIN = {
    "year-one": "1401207529",
    "long-halloween": "1401232590",
    "dark-victory": "1401233309",
    "killing-joke": "1401284272",
    "death-in-the-family": "1401293623",
    "knightfall": "140123321X",
    "no-mans-land": "1401295271",
    "hush": "1401297242",
    "under-the-red-hood": "1401231454",
    "batman-rip": "1401220322",
    "court-of-owls": "1401235425",
    "death-of-the-family": "1401242370",
    "earth-two-golden-age": "1563890439",
    "dark-knight-returns": "1563893428",
    "flashpoint-knight-of-vengeance": "1401234054",
    "crime-syndicate": "1401249367",
    "red-rain": "1563890364",
    "hush-beyond": "1401229887",
    "earth-2-planetfall": "1401242818",
    "batman-who-laughs": "1779504462",
    "grim-knight": "1779504462",
    "red-death": "1401289072",
    "dawnbreaker": "1401289072",
    "murder-machine": "1401289072",
    "gotham-by-gaslight": "1779524056",
    "white-knight": "1401274527",
    "thrillkiller": "1401204219",
    "holy-terror": "1563892030",
    "batman-66-vol-1": "1401244737",
    "in-darkest-knight": "1563891265",
    "the-drowned": "1401289072",
}

COVER_OVERRIDES = {
    "year-one": "https://upload.wikimedia.org/wikipedia/en/1/10/Batman_-_Year_One_%28softcover%29.jpg",
    "long-halloween": "https://upload.wikimedia.org/wikipedia/en/2/2f/The_Long_Halloween.jpg",
    "dark-victory": "https://upload.wikimedia.org/wikipedia/en/4/4c/Batman_-_Dark_Victory_%28softcover%29.jpg",
    "killing-joke": "https://upload.wikimedia.org/wikipedia/en/b/bc/Batman_The_Killing_Joke.jpg",
    "death-in-the-family": "https://upload.wikimedia.org/wikipedia/en/3/37/Batman_-_A_Death_in_the_Family_%28softcover%29.jpg",
    "knightfall": "https://upload.wikimedia.org/wikipedia/en/2/2d/Batman_-_Knightfall_Vol._1_%28softcover%29.jpg",
    "no-mans-land": "https://upload.wikimedia.org/wikipedia/en/8/8e/Batman_-_No_Man%27s_Land_Vol._1_%28softcover%29.jpg",
    "hush": "https://upload.wikimedia.org/wikipedia/en/9/9d/Batman_Hush_TPB_cover.jpg",
    "under-the-red-hood": "https://upload.wikimedia.org/wikipedia/en/6/6e/Batman_-_Under_the_Red_Hood_%28softcover%29.jpg",
    "batman-rip": "https://upload.wikimedia.org/wikipedia/en/9/9a/Batman_R.I.P._TPB.jpg",
    "court-of-owls": "https://upload.wikimedia.org/wikipedia/en/4/4d/Batman_-_The_Court_of_Owls_%28softcover%29.jpg",
    "death-of-the-family": "https://upload.wikimedia.org/wikipedia/en/1/1e/Batman_-_Death_of_the_Family_%28softcover%29.jpg",
    "dark-knight-returns": "https://upload.wikimedia.org/wikipedia/en/5/50/Batman_-_The_Dark_Knight_Returns_%28softcover%29.jpg",
    "red-rain": "https://upload.wikimedia.org/wikipedia/en/d/d9/Batman_%26_Dracula_-_Red_Rain.jpg",
    "gotham-by-gaslight": "https://upload.wikimedia.org/wikipedia/en/4/4f/Gotham_by_Gaslight.jpg",
    "white-knight": "https://upload.wikimedia.org/wikipedia/en/8/8f/Batman_-_White_Knight_%28softcover%29.jpg",
    "batman-who-laughs": "https://upload.wikimedia.org/wikipedia/en/9/9f/The_Batman_Who_Laughs_%28softcover%29.jpg",
    "flashpoint-knight-of-vengeance": "https://upload.wikimedia.org/wikipedia/en/0/0d/Flashpoint_-_Batman_Knight_of_Vengeance_%28softcover%29.jpg",
    "hush-beyond": "https://upload.wikimedia.org/wikipedia/en/5/5c/Batman_Beyond_-_Hush_Beyond_%28softcover%29.jpg",
    "in-darkest-knight": "https://upload.wikimedia.org/wikipedia/en/9/9b/Batman_-_In_Darkest_Knight_%28softcover%29.jpg",
    "holy-terror": "https://upload.wikimedia.org/wikipedia/en/2/2a/Batman_-_Holy_Terror_%28softcover%29.jpg",
    "batman-66-vol-1": "https://upload.wikimedia.org/wikipedia/en/1/1f/Batman_%2766_Vol._1_%28softcover%29.jpg",
}

VERSION_ART = {
    "prime-earth-batman": "https://upload.wikimedia.org/wikipedia/en/1/1a/Batman_%28DC_Comics_character%29.jpg",
    "earth-two-batman": "https://upload.wikimedia.org/wikipedia/en/1/1a/Batman_%28DC_Comics_character%29.jpg",
    "earth-31-batman": "https://upload.wikimedia.org/wikipedia/en/5/50/Batman_-_The_Dark_Knight_Returns_%28softcover%29.jpg",
    "thomas-wayne-batman": "https://upload.wikimedia.org/wikipedia/en/0/0d/Flashpoint_-_Batman_Knight_of_Vengeance_%28softcover%29.jpg",
    "owlman": "https://upload.wikimedia.org/wikipedia/en/9/9e/Owlman_%28DC_Comics%29.jpg",
    "vampire-batman": "https://upload.wikimedia.org/wikipedia/en/d/d9/Batman_%26_Dracula_-_Red_Rain.jpg",
    "batman-beyond": "https://upload.wikimedia.org/wikipedia/en/a/a6/Batman_Beyond_%28character%29.jpg",
    "earth-2-batman-new-52": "https://upload.wikimedia.org/wikipedia/en/4/4d/Batman_-_The_Court_of_Owls_%28softcover%29.jpg",
    "batman-who-laughs": "https://upload.wikimedia.org/wikipedia/en/9/9f/The_Batman_Who_Laughs_%28softcover%29.jpg",
    "grim-knight": "https://upload.wikimedia.org/wikipedia/en/9/9f/The_Batman_Who_Laughs_%28softcover%29.jpg",
    "red-death": "https://upload.wikimedia.org/wikipedia/en/9/9f/The_Batman_Who_Laughs_%28softcover%29.jpg",
    "dawnbreaker": "https://upload.wikimedia.org/wikipedia/en/9/9f/The_Batman_Who_Laughs_%28softcover%29.jpg",
    "murder-machine": "https://upload.wikimedia.org/wikipedia/en/9/9f/The_Batman_Who_Laughs_%28softcover%29.jpg",
    "gaslight-batman": "https://upload.wikimedia.org/wikipedia/en/4/4f/Gotham_by_Gaslight.jpg",
    "white-knight-batman": "https://upload.wikimedia.org/wikipedia/en/8/8f/Batman_-_White_Knight_%28softcover%29.jpg",
    "thrillkiller-batman": "https://upload.wikimedia.org/wikipedia/en/1/1a/Batman_%28DC_Comics_character%29.jpg",
    "holy-terror-batman": "https://upload.wikimedia.org/wikipedia/en/2/2a/Batman_-_Holy_Terror_%28softcover%29.jpg",
    "batman-66": "https://upload.wikimedia.org/wikipedia/en/1/1f/Batman_%2766_Vol._1_%28softcover%29.jpg",
    "darkest-knight-batman": "https://upload.wikimedia.org/wikipedia/en/9/9b/Batman_-_In_Darkest_Knight_%28softcover%29.jpg",
    "the-drowned": "https://upload.wikimedia.org/wikipedia/en/9/9f/The_Batman_Who_Laughs_%28softcover%29.jpg",
}

VERSION_TO_RUN = {
    "prime-earth-batman": "year-one",
    "earth-two-batman": "earth-two-golden-age",
    "earth-31-batman": "dark-knight-returns",
    "thomas-wayne-batman": "flashpoint-knight-of-vengeance",
    "owlman": "crime-syndicate",
    "vampire-batman": "red-rain",
    "batman-beyond": "hush-beyond",
    "earth-2-batman-new-52": "earth-2-planetfall",
    "batman-who-laughs": "batman-who-laughs",
    "grim-knight": "grim-knight",
    "red-death": "red-death",
    "dawnbreaker": "dawnbreaker",
    "murder-machine": "murder-machine",
    "gaslight-batman": "gotham-by-gaslight",
    "white-knight-batman": "white-knight",
    "thrillkiller-batman": "thrillkiller",
    "holy-terror-batman": "holy-terror",
    "batman-66": "batman-66-vol-1",
    "darkest-knight-batman": "in-darkest-knight",
    "the-drowned": "the-drowned",
}


def unique(urls):
    seen = set()
    out = []
    for u in urls:
        if u and u not in seen:
            seen.add(u)
            out.append(u)
    return out


def run_source_urls(slug):
    isbn13 = RUN_ISBN.get(slug)
    isbn10 = isbn13.replace("978", "", 1) if isbn13 else None
    asin = RUN_ASIN.get(slug)
    urls = []
    if slug in COVER_OVERRIDES:
        urls.append(COVER_OVERRIDES[slug])
    if isbn13:
        urls.append(f"https://covers.openlibrary.org/b/isbn/{isbn13}-L.jpg?default=false")
        urls.append(f"https://covers.openlibrary.org/b/isbn/{isbn13}-M.jpg?default=false")
        urls.append(f"https://books.google.com/books/content?vid=ISBN:{isbn13}&printsec=frontcover&img=1&zoom=1")
    if isbn10:
        urls.append(f"https://covers.openlibrary.org/b/isbn/{isbn10}-L.jpg?default=false")
    if asin:
        urls.append(f"https://images-na.ssl-images-amazon.com/images/P/{asin}.01._SCMZZZZZZZ_.jpg")
        urls.append(f"https://images-na.ssl-images-amazon.com/images/P/{asin}.01.LZZZZZZZ.jpg")
    return unique(urls)


def download_first(urls, dest):
    ctx = ssl.create_default_context()
    headers = {"User-Agent": "BatmanReadingGuide/1.0 (cover downloader)"}
    for url in urls:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
                data = resp.read()
                ctype = resp.headers.get("Content-Type", "")
            if len(data) < 1500:
                print(f"  skip tiny ({len(data)}b) {url}")
                continue
            if "image" not in ctype and "openlibrary" not in url and "wikimedia" not in url:
                print(f"  skip non-image {ctype} {url}")
                continue
            with open(dest, "wb") as f:
                f.write(data)
            return len(data)
        except Exception as e:
            print(f"  skip {url}: {e}")
    return 0


def parse_screen_tmdb_posters():
    """Read SCREEN_TMDB_POSTERS from index.html."""
    with open(INDEX_HTML, encoding="utf-8") as f:
        html = f.read()
    block = re.search(r"const SCREEN_TMDB_POSTERS = \{([\s\S]*?)\n    \};", html)
    if not block:
        return {}
    out = {}
    for match in re.finditer(r"'([^']+)': '(/[^']+)'", block.group(1)):
        out[match.group(1)] = [tmdb_poster_url(match.group(2))]
    return out


def tmdb_poster_url(path):
    path = path if path.startswith("/") else "/" + path
    return "https://image.tmdb.org/t/p/w500" + path


def parse_screen_poster_overrides():
    return parse_screen_tmdb_posters()


def parse_batman_screen_items():
    """Read id / wikipedia / imdb from BATMAN_SCREEN in index.html."""
    with open(INDEX_HTML, encoding="utf-8") as f:
        html = f.read()
    items = []
    for match in re.finditer(
        r"\{ id: '([^']+)'[^}]*wikipedia: '([^']+)'(?:[^}]*imdb: '([^']+)')?",
        html,
    ):
        items.append({"id": match.group(1), "wikipedia": match.group(2), "imdb": match.group(3) or ""})
    return items


def wiki_title_from_url(url):
    return urllib.parse.unquote(url.split("/wiki/")[-1])


def thumb_to_full_wikimedia(url):
    """Convert a Wikimedia thumb URL to the full-size file URL."""
    if "/thumb/" not in url:
        return url
    prefix, rest = url.split("/thumb/", 1)
    parts = rest.split("/")
    if len(parts) >= 3:
        return f"{prefix}/" + "/".join(parts[:3])
    return url


def wiki_poster_urls(wikipedia_url):
    """Fetch poster/thumbnail URLs from Wikipedia's pageimages API."""
    title = wiki_title_from_url(wikipedia_url)
    query_url = (
        "https://en.wikipedia.org/w/api.php?"
        + urllib.parse.urlencode(
            {
                "action": "query",
                "titles": title,
                "prop": "pageimages",
                "format": "json",
                "pithumbsize": 1000,
                "pilicense": "any",
            }
        )
    )
    urls = []
    ctx = ssl.create_default_context()
    try:
        req = urllib.request.Request(query_url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            data = json.loads(resp.read())
        for page in data.get("query", {}).get("pages", {}).values():
            thumb = (page.get("thumbnail") or {}).get("source")
            if thumb:
                urls.append(thumb_to_full_wikimedia(thumb))
                urls.append(thumb)
    except Exception as e:
        print(f"  wiki api: {e}")
    return unique(urls)


def imdb_poster_urls(imdb_url):
    """Scrape og:image from an IMDb title page."""
    if not imdb_url:
        return []
    ctx = ssl.create_default_context()
    try:
        req = urllib.request.Request(imdb_url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
        match = re.search(r'property="og:image"\s+content="([^"]+)"', html)
        if match:
            return [match.group(1).replace("&amp;", "&")]
    except Exception as e:
        print(f"  imdb: {e}")
    return []


def screen_poster_source_urls(item, overrides):
    """Build ordered poster URL list for a screen item."""
    slug = item["id"]
    urls = []
    urls.extend(wiki_poster_urls(item["wikipedia"]))
    urls.extend(overrides.get(slug, []))
    urls.extend(imdb_poster_urls(item.get("imdb", "")))
    return unique(urls)


def download_screen_posters(force=False):
    os.makedirs(SCREEN_DIR, exist_ok=True)
    overrides = parse_screen_poster_overrides()
    items = parse_batman_screen_items()
    ok = fail = 0
    print(f"\nDownloading {len(items)} screen posters (Wikipedia → overrides → IMDb)...\n")
    for item in items:
        slug = item["id"]
        dest = os.path.join(SCREEN_DIR, f"{slug}.jpg")
        if not force and os.path.exists(dest) and os.path.getsize(dest) > 1500:
            print(f"✓ {slug} (cached)")
            ok += 1
            continue
        print(f"{slug}...", end=" ", flush=True)
        urls = screen_poster_source_urls(item, overrides)
        size = download_first(urls, dest)
        if size:
            print(f"✓ {size // 1024}KB")
            ok += 1
        else:
            print("✗ failed")
            fail += 1
    return ok, fail


def main():
    screen_only = "--screen-only" in sys.argv
    os.makedirs(RUNS_DIR, exist_ok=True)
    os.makedirs(VERSIONS_DIR, exist_ok=True)
    os.makedirs(SCREEN_DIR, exist_ok=True)
    ok = fail = 0

    if screen_only:
        s_ok, s_fail = download_screen_posters(force="--force" in sys.argv)
        print(f"\nDone: {s_ok} ok, {s_fail} failed")
        print(f"Saved to {SCREEN_DIR}\n")
        return

    print("\nDownloading run covers...\n")
    for slug in RUN_ISBN:
        dest = os.path.join(RUNS_DIR, f"{slug}.jpg")
        if os.path.exists(dest) and os.path.getsize(dest) > 1500:
            print(f"✓ {slug} (cached)")
            ok += 1
            continue
        print(f"{slug}...", end=" ", flush=True)
        size = download_first(run_source_urls(slug), dest)
        if size:
            print(f"✓ {size // 1024}KB")
            ok += 1
        else:
            print("✗ failed")
            fail += 1

    print("\nDownloading version art...\n")
    for slug, art_url in VERSION_ART.items():
        dest = os.path.join(VERSIONS_DIR, f"{slug}.jpg")
        if os.path.exists(dest) and os.path.getsize(dest) > 1500:
            print(f"✓ {slug} (cached)")
            ok += 1
            continue
        print(f"{slug}...", end=" ", flush=True)
        run_slug = VERSION_TO_RUN.get(slug)
        local_run = os.path.join(RUNS_DIR, f"{run_slug}.jpg") if run_slug else None
        if local_run and os.path.exists(local_run) and os.path.getsize(local_run) > 1500:
            shutil.copy2(local_run, dest)
            print(f"✓ copied from {run_slug}")
            ok += 1
            continue
        urls = unique([art_url] + (run_source_urls(run_slug) if run_slug else []))
        size = download_first(urls, dest)
        if size:
            print(f"✓ {size // 1024}KB")
            ok += 1
        else:
            print("✗ failed")
            fail += 1

    s_ok, s_fail = download_screen_posters()
    ok += s_ok
    fail += s_fail

    print(f"\nDone: {ok} ok, {fail} failed")
    print(f"Saved to {os.path.join(ROOT, 'images/covers')}\n")


if __name__ == "__main__":
    main()
