#!/usr/bin/env python3
"""API clients for resolving cover art.

Sources (tried in cascade by refresh_covers.py):
  Open Library — ISBN covers (no API key)
  Amazon       — product images via ASIN (no API key)
  Google Books — ISBN / title cover links (optional API key)
  Comic Vine   — comic covers and character art (non-commercial)
  TMDB         — film and TV posters

Standard library only, so there is nothing to pip install.
"""
from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path

HERE = Path(__file__).resolve().parent
CACHE_DIR = HERE / '.cache'
RESOLUTION_CACHE = CACHE_DIR / 'resolution.json'

COMICVINE_BASE = 'https://comicvine.gamespot.com/api'
TMDB_BASE = 'https://api.themoviedb.org/3'
TMDB_IMAGE_BASE = 'https://image.tmdb.org/t/p/w500'
OPENLIBRARY_COVER = 'https://covers.openlibrary.org/b/isbn/{isbn}-L.jpg?default=false'
AMAZON_COVER = 'https://images-na.ssl-images-amazon.com/images/P/{asin}.01.LZZZZZZZ.jpg'
AMAZON_COVER_ALT = 'https://images-na.ssl-images-amazon.com/images/P/{asin}.01._SCLZZZZZZZ_.jpg'
AMAZON_COVER_MEDIA = 'https://m.media-amazon.com/images/P/{asin}.01.LZZZZZZZ.jpg'
GOOGLE_BOOKS_API = 'https://www.googleapis.com/books/v1/volumes'

PLACEHOLDER_MARKER = 'PASTE_'


class ConfigError(RuntimeError):
    pass


def load_config(path: Path | None = None) -> dict:
    path = path or (HERE / 'config.json')
    if not path.exists():
        raise ConfigError(
            f'Missing {path.name}. Copy config.example.json to config.json and add your keys.'
        )
    with path.open(encoding='utf-8') as fh:
        cfg = json.load(fh)
    cfg.setdefault('user_agent', 'ComicCharacterGuides/1.0 (personal non-commercial fan project)')
    return cfg


def key_is_placeholder(value: str | None) -> bool:
    if not value:
        return True
    upper = value.upper()
    return (
        value.startswith(PLACEHOLDER_MARKER)
        or upper.startswith('OPTIONAL_')
        or 'PASTE_' in upper
    )


# ───────────────────────────── caching ─────────────────────────────


class ResolutionCache:
    """Remembers resolved image URLs (including misses) between runs."""

    def __init__(self, path: Path = RESOLUTION_CACHE):
        self.path = path
        self._data: dict[str, dict] = {}
        if path.exists():
            try:
                self._data = json.loads(path.read_text(encoding='utf-8'))
            except (json.JSONDecodeError, OSError):
                self._data = {}
        self._dirty = False

    def get(self, key: str):
        return self._data.get(key)

    def put(self, key: str, value: dict) -> None:
        self._data[key] = value
        self._dirty = True

    def save(self) -> None:
        if not self._dirty:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self._data, indent=2, sort_keys=True), encoding='utf-8')
        self._dirty = False

    def __len__(self) -> int:
        return len(self._data)


# ────────────────────────── rate limiting ──────────────────────────


@dataclass
class RateLimiter:
    """Minimum spacing between calls, plus an optional hourly cap per resource."""

    min_interval: float = 1.0
    hourly_cap: int | None = None
    _last_call: float = field(default=0.0, repr=False)
    _window_start: float = field(default_factory=time.monotonic, repr=False)
    _window_count: int = field(default=0, repr=False)

    def wait(self) -> None:
        now = time.monotonic()

        if self.hourly_cap is not None:
            if now - self._window_start >= 3600:
                self._window_start = now
                self._window_count = 0
            if self._window_count >= self.hourly_cap:
                sleep_for = 3600 - (now - self._window_start)
                if sleep_for > 0:
                    raise RateLimitExceeded(
                        f'Hourly cap of {self.hourly_cap} reached; retry in {int(sleep_for / 60)} min'
                    )

        gap = now - self._last_call
        if gap < self.min_interval:
            time.sleep(self.min_interval - gap)

        self._last_call = time.monotonic()
        self._window_count += 1


class RateLimitExceeded(RuntimeError):
    pass


# ─────────────────────────── http helper ───────────────────────────


def http_json(url: str, user_agent: str, timeout: int = 20) -> dict:
    req = urllib.request.Request(url, headers={
        'User-Agent': user_agent,
        'Accept': 'application/json',
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode('utf-8'))


def download_image(url: str, dest: Path, user_agent: str, timeout: int = 30, min_bytes: int = 3000,
                   referer: str | None = None) -> bool:
    """Fetch an image to dest. Returns True on success. Writes atomically."""
    headers = {
        'User-Agent': user_agent,
        'Accept': 'image/avif,image/webp,image/jpeg,image/png,*/*',
    }
    if referer:
        headers['Referer'] = referer
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            ctype = (resp.headers.get('Content-Type') or '').lower()
            payload = resp.read()
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
        return False

    if 'image' not in ctype and not _looks_like_image(payload):
        return False
    if len(payload) < min_bytes:
        return False

    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + '.part')
    tmp.write_bytes(payload)
    tmp.replace(dest)
    return True


def local_image_ok(path: Path, min_bytes: int = 3000) -> bool:
    """True when dest looks like a usable downloaded image (not missing/tiny/corrupt)."""
    if not path.exists() or not path.is_file():
        return False
    try:
        size = path.stat().st_size
        if size < min_bytes:
            return False
        head = path.read_bytes()[:16]
    except OSError:
        return False
    return _looks_like_image(head)


def normalize_isbn(value: str | None) -> str | None:
    if not value:
        return None
    digits = re.sub(r'[^0-9Xx]', '', value)
    if len(digits) in (10, 13):
        return digits.upper()
    return None


def normalize_asin(value: str | None) -> str | None:
    if not value:
        return None
    asin = re.sub(r'[^0-9A-Za-z]', '', value).upper()
    return asin if len(asin) == 10 else None


def head_ok(url: str, user_agent: str, timeout: int = 12, min_bytes: int = 3000) -> bool:
    """Cheap existence check for a remote image URL."""
    req = urllib.request.Request(url, method='HEAD', headers={
        'User-Agent': user_agent,
        'Accept': 'image/*,*/*',
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status >= 400:
                return False
            ctype = (resp.headers.get('Content-Type') or '').lower()
            length = resp.headers.get('Content-Length')
            if length is not None and int(length) < min_bytes:
                return False
            if ctype and 'image' not in ctype and 'octet-stream' not in ctype:
                return False
            return True
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, ValueError):
        # Some CDNs reject HEAD — fall through to a tiny ranged GET.
        pass

    req = urllib.request.Request(url, headers={
        'User-Agent': user_agent,
        'Accept': 'image/*,*/*',
        'Range': 'bytes=0-2048',
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status >= 400:
                return False
            payload = resp.read(2048)
            return _looks_like_image(payload)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
        return False


def _looks_like_image(blob: bytes) -> bool:
    return (
        blob.startswith(b'\xff\xd8\xff')          # jpeg
        or blob.startswith(b'\x89PNG\r\n\x1a\n')  # png
        or blob[:4] == b'RIFF'                    # webp
        or blob.startswith(b'GIF8')               # gif
    )


# ───────────────────────────── scoring ─────────────────────────────


_NOISE = re.compile(
    r'\b(vol|volume|book|tpb|omnibus|deluxe|edition|the|a|an|complete|epic|collection|classic)\b',
    re.I,
)


def normalize_title(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[\u2018\u2019\u201c\u201d]', "'", text)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = _NOISE.sub(' ', text)
    return re.sub(r'\s+', ' ', text).strip()


def score_match(query: str, candidate: str) -> float:
    a, b = normalize_title(query), normalize_title(candidate)
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    ratio = SequenceMatcher(None, a, b).ratio()
    # Reward full containment of the shorter phrase inside the longer one.
    if a in b or b in a:
        ratio = max(ratio, 0.9)
    return ratio


# ────────────────────────── Comic Vine ─────────────────────────────

# The /search/ endpoint returns empty result arrays for this key, so we query the
# filtered resource endpoints instead. They also carry publisher data, which lets
# us tell DC's Hal Jordan apart from Marvel's.
CV_FIELDS = {
    'characters': 'id,name,image,publisher',
    'volumes': 'id,name,image,publisher,start_year',
    'story_arcs': 'id,name,image',
    'issues': 'id,name,issue_number,image,cover_date,volume',
}

# Comic Vine's filter syntax is "field:value,field:value", so colons and commas
# inside a value break the parser and must be stripped.
_FILTER_UNSAFE = re.compile(r'[:,|]')
_VOLUME_SUFFIX = re.compile(r'\b(vol\.?|volume|book|part)\s*\.?\s*[0-9ivx]+\b', re.I)
_PARENTHETICAL = re.compile(r'\([^)]*\)')


def sanitize_filter_value(text: str) -> str:
    text = _FILTER_UNSAFE.sub(' ', text)
    return re.sub(r'\s+', ' ', text).strip()


def title_variants(title: str, limit: int = 3) -> list[str]:
    """Progressively looser forms of a collection title to try against Comic Vine."""
    out: list[str] = []

    def add(candidate: str) -> None:
        candidate = sanitize_filter_value(_VOLUME_SUFFIX.sub(' ', candidate))
        if candidate and len(candidate) > 2 and candidate.lower() not in {o.lower() for o in out}:
            out.append(candidate)

    # The part after a colon is usually the actual arc name, e.g.
    # "Green Lantern: Secret Origin" -> "Secret Origin".
    if ':' in title:
        add(title.split(':', 1)[1])
    add(title)
    if ':' in title:
        add(title.split(':', 1)[0])

    return out[:limit]


def character_variants(name: str, limit: int = 3) -> list[str]:
    """Loosen a version name toward something Comic Vine will recognise."""
    out: list[str] = []

    def add(candidate: str) -> None:
        candidate = sanitize_filter_value(candidate)
        if candidate and len(candidate) > 2 and candidate.lower() not in {o.lower() for o in out}:
            out.append(candidate)

    add(name)
    # "Peni Parker (SP//dr)" -> "Peni Parker"
    stripped = _PARENTHETICAL.sub(' ', name)
    add(stripped)
    # "Bart Allen / Impulse" -> both halves
    for half in re.split(r'\s*/\s*', stripped):
        add(half)
    # "Flashpoint Barry Allen" -> "Barry Allen"
    words = sanitize_filter_value(stripped).split()
    if len(words) > 2:
        add(' '.join(words[-2:]))

    return out[:limit]


class ComicVineClient:
    """Comic Vine API. Non-commercial use only; responses are cached locally."""

    def __init__(self, api_key: str, user_agent: str, cache: ResolutionCache, verbose: bool = False):
        self.api_key = api_key
        self.user_agent = user_agent
        self.cache = cache
        self.verbose = verbose
        # Comic Vine allows ~200 requests per resource per hour and throttles
        # bursts, so each resource gets its own bucket plus a ~1s global spacing.
        self.limiters = {res: RateLimiter(min_interval=1.1, hourly_cap=190) for res in CV_FIELDS}
        self.calls = 0

    def _get(self, resource: str, params: dict) -> dict | None:
        if resource not in self.limiters:
            self.limiters[resource] = RateLimiter(min_interval=1.1, hourly_cap=190)
        self.limiters[resource].wait()
        query = dict(params)
        query.update({'api_key': self.api_key, 'format': 'json'})
        url = f'{COMICVINE_BASE}/{resource}/?' + urllib.parse.urlencode(query)
        try:
            payload = http_json(url, self.user_agent)
        except urllib.error.HTTPError as exc:
            if exc.code == 420:
                raise RateLimitExceeded('Comic Vine returned 420 (rate limited)') from exc
            if self.verbose:
                print(f'    ! comicvine http {exc.code} on {resource}')
            return None
        except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
            if self.verbose:
                print(f'    ! comicvine {type(exc).__name__} on {resource}')
            return None

        self.calls += 1
        status = payload.get('status_code')
        if status == 107:
            raise RateLimitExceeded('Comic Vine rate limit hit (status 107)')
        if status == 100:
            raise ConfigError('Comic Vine rejected the API key (status 100)')
        if status != 1:
            if self.verbose:
                print(f'    ! comicvine status {status}: {payload.get("error")}')
            return None
        return payload

    def _query(self, resource: str, name: str, limit: int = 10) -> list[dict] | None:
        payload = self._get(resource, {
            'filter': f'name:{name}',
            'limit': limit,
            'field_list': CV_FIELDS[resource],
        })
        if payload is None:
            return None
        results = payload.get('results')
        return results if isinstance(results, list) else []

    @staticmethod
    def _pick_image(image: dict | None) -> str | None:
        if not isinstance(image, dict):
            return None
        for field_name in ('super_url', 'screen_large_url', 'original_url', 'medium_url'):
            url = image.get(field_name)
            if url and 'blank' not in url and 'no-image' not in url:
                return url
        return None

    @staticmethod
    def _publisher_of(item: dict) -> str:
        pub = item.get('publisher')
        return (pub or {}).get('name', '') if isinstance(pub, dict) else ''

    def _best_of(self, results: list[dict], target: str, resource: str,
                 publisher_hint: str) -> tuple[float, dict] | None:
        best: tuple[float, dict] | None = None
        for item in results:
            url = self._pick_image(item.get('image'))
            if not url:
                continue
            name = item.get('name') or ''
            score = score_match(target, name)
            publisher = self._publisher_of(item)
            if publisher and publisher_hint:
                # Nudge toward the right universe when several characters share a name.
                score += 0.15 if publisher_hint.lower() in publisher.lower() else -0.12
            score = max(0.0, min(score, 1.0))
            if best is None or score > best[0]:
                best = (score, {
                    'url': url,
                    'name': name,
                    'publisher': publisher,
                    'resource': resource,
                    'id': item.get('id'),
                    'score': round(score, 3),
                })
        return best

    def _resolve(self, cache_key: str, target: str, variants: list[str],
                 resources: tuple[str, ...], publisher_hint: str,
                 max_queries: int = 4) -> dict:
        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached

        best: tuple[float, dict] | None = None
        queries = 0
        saw_success = False

        for resource in resources:
            for variant in variants:
                if queries >= max_queries:
                    break
                queries += 1
                results = self._query(resource, variant)
                if results is None:
                    continue
                saw_success = True
                candidate = self._best_of(results, target, resource, publisher_hint)
                if candidate and (best is None or candidate[0] > best[0]):
                    best = candidate
                if best and best[0] >= 0.9:
                    break
            if best and best[0] >= 0.9:
                break

        if not saw_success and best is None:
            return {'url': None}  # network failure — do not cache a miss

        result = best[1] if best and best[0] >= 0.55 else {'url': None}
        self.cache.put(cache_key, result)
        return result

    def find_cover(self, title: str, publisher_hint: str = '') -> dict:
        return self._resolve(
            cache_key=f'cv:cover:{normalize_title(title)}',
            target=title,
            variants=title_variants(title),
            resources=('story_arcs', 'volumes'),
            publisher_hint=publisher_hint,
        )

    def find_character(self, name: str, publisher_hint: str = '') -> dict:
        return self._resolve(
            cache_key=f'cv:character:{normalize_title(name)}',
            target=name,
            variants=character_variants(name),
            resources=('characters',),
            publisher_hint=publisher_hint,
            max_queries=3,
        )

    def _best_volume(self, series: str, year_hint: str = '', publisher_hint: str = '') -> dict | None:
        """Pick the Comic Vine volume that best matches a series name + optional year."""
        year_num = None
        if year_hint:
            m = re.search(r'(19|20)\d{2}', year_hint)
            if m:
                year_num = int(m.group(0))

        best: tuple[float, dict] | None = None
        for variant in title_variants(series, limit=3):
            results = self._query('volumes', variant, limit=15)
            if not results:
                continue
            for item in results:
                name = item.get('name') or ''
                score = score_match(series, name)
                publisher = self._publisher_of(item)
                if publisher and publisher_hint:
                    score += 0.12 if publisher_hint.lower() in publisher.lower() else -0.1
                start_year = item.get('start_year')
                try:
                    start_i = int(start_year) if start_year not in (None, '') else None
                except (TypeError, ValueError):
                    start_i = None
                if year_num and start_i:
                    delta = abs(start_i - year_num)
                    if delta == 0:
                        score += 0.2
                    elif delta <= 1:
                        score += 0.12
                    elif delta <= 3:
                        score += 0.05
                    else:
                        score -= min(0.25, delta * 0.03)
                score = max(0.0, min(score, 1.0))
                if best is None or score > best[0]:
                    best = (score, item)
            if best and best[0] >= 0.92:
                break
        if not best or best[0] < 0.55:
            return None
        return best[1]

    def _issues_for_volume(self, volume_id: int) -> list[dict]:
        out: list[dict] = []
        offset = 0
        while offset < 400:
            payload = self._get('issues', {
                'filter': f'volume:{volume_id}',
                'field_list': CV_FIELDS['issues'],
                'limit': 100,
                'offset': offset,
                'sort': 'cover_date:asc',
            })
            if not payload:
                break
            batch = payload.get('results') or []
            if not isinstance(batch, list) or not batch:
                break
            out.extend(batch)
            if len(batch) < 100:
                break
            offset += 100
        return out

    @staticmethod
    def _issue_number_key(raw) -> float | None:
        if raw is None:
            return None
        text = str(raw).strip()
        if not text:
            return None
        m = re.match(r'^(\d+(?:\.\d+)?)', text)
        if not m:
            return None
        try:
            return float(m.group(1))
        except ValueError:
            return None

    def find_last_issue_cover(
        self,
        series: str,
        issue_number: str,
        year_hint: str = '',
        publisher_hint: str = '',
    ) -> dict:
        """Resolve cover art for the final issue of a collected run when possible."""
        cache_key = (
            f'cv:last-issue:{normalize_title(series)}:'
            f'{issue_number}:{normalize_title(year_hint)}:{normalize_title(publisher_hint)}'
        )
        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached

        volume = self._best_volume(series, year_hint=year_hint, publisher_hint=publisher_hint)
        if (not volume or not volume.get('id')) and year_hint:
            # Short titles like "Vision" collide hard on /volumes/; try /search/.
            volume = self._search_volume(series, year_hint=year_hint, publisher_hint=publisher_hint)
        if not volume or not volume.get('id'):
            result = {'url': None}
            self.cache.put(cache_key, result)
            return result

        volume_id = int(volume['id'])
        chosen = self._issue_by_number(volume_id, issue_number)
        if chosen is None:
            issues = self._issues_for_volume(volume_id)
            want = self._issue_number_key(issue_number)
            if want is not None:
                for issue in issues:
                    if self._issue_number_key(issue.get('issue_number')) == want:
                        chosen = issue
                        break
            if chosen is None and issues:
                ranked = []
                for issue in issues:
                    key = self._issue_number_key(issue.get('issue_number'))
                    if key is not None:
                        ranked.append((key, issue))
                if ranked:
                    ranked.sort(key=lambda pair: pair[0])
                    chosen = ranked[-1][1]

        url = self._pick_image((chosen or {}).get('image')) if chosen else None
        result = {
            'url': url,
            'name': (chosen or {}).get('name') or volume.get('name'),
            'issue_number': (chosen or {}).get('issue_number'),
            'volume': volume.get('name'),
            'volume_id': volume.get('id'),
            'resource': 'issues',
            'id': (chosen or {}).get('id'),
            'series': series,
            'wanted_issue': issue_number,
        } if url else {'url': None}
        self.cache.put(cache_key, result)
        return result

    def _issue_by_number(self, volume_id: int, issue_number: str) -> dict | None:
        payload = self._get('issues', {
            'filter': f'volume:{volume_id},issue_number:{issue_number}',
            'field_list': CV_FIELDS['issues'],
            'limit': 5,
        })
        if not payload:
            return None
        results = payload.get('results') or []
        return results[0] if results else None

    def _search_volume(self, series: str, year_hint: str = '', publisher_hint: str = '') -> dict | None:
        year_num = None
        if year_hint:
            m = re.search(r'(19|20)\d{2}', year_hint)
            if m:
                year_num = int(m.group(0))
        query = series
        if year_num:
            query = f'{series} {year_num}'
        payload = self._get('search', {
            'query': query,
            'resources': 'volume',
            'limit': 15,
            'field_list': 'id,name,image,publisher,start_year,count_of_issues',
        })
        if not payload:
            return None
        best: tuple[float, dict] | None = None
        for item in payload.get('results') or []:
            name = item.get('name') or ''
            score = score_match(series, name)
            publisher = self._publisher_of(item)
            if publisher and publisher_hint:
                score += 0.12 if publisher_hint.lower() in publisher.lower() else -0.1
            start_year = item.get('start_year')
            try:
                start_i = int(start_year) if start_year not in (None, '') else None
            except (TypeError, ValueError):
                start_i = None
            if year_num and start_i:
                delta = abs(start_i - year_num)
                if delta == 0:
                    score += 0.25
                elif delta <= 1:
                    score += 0.18
                elif delta <= 2:
                    score += 0.08
                else:
                    score -= min(0.3, delta * 0.04)
            # Prefer series lengths that look like a run, not one-shot HCs.
            count = item.get('count_of_issues') or 0
            try:
                count_i = int(count)
            except (TypeError, ValueError):
                count_i = 0
            if count_i >= 6:
                score += 0.05
            score = max(0.0, min(score, 1.0))
            if best is None or score > best[0]:
                best = (score, item)
        if not best or best[0] < 0.55:
            return None
        return best[1]


# ────────────────────────── collects parsing ───────────────────────


# "Vision #1–12", "West Coast Avengers #42-45", "Avengers #57–58, #74–75"
_COLLECTS_ISSUE = re.compile(
    r'(?:^|[,;/]|\band\b)\s*(?P<series>[A-Za-z0-9][^#]*?)?\s*#\s*(?P<start>\d+)'
    r'(?:\s*[–—\-]\s*(?P<end>\d+))?',
    re.I,
)


def parse_finale_from_collects(collects: str) -> dict | None:
    """Best-effort final issue from a run's collects string.

    Returns {'series': str, 'issue': str} or None when no issue range is present.
    """
    text = (collects or '').strip()
    if not text or re.match(r'^(selected|various|crossover|related|massive)\b', text, re.I):
        return None

    matches = list(_COLLECTS_ISSUE.finditer(text))
    if not matches:
        return None

    series = ''
    best_issue = None
    best_num = -1.0
    for match in matches:
        chunk_series = (match.group('series') or '').strip(' :-')
        if chunk_series:
            # Drop trailing words that are just connectors from prior clauses.
            chunk_series = re.sub(r'^(and|plus|with)\s+', '', chunk_series, flags=re.I).strip()
            series = chunk_series
        end = match.group('end') or match.group('start')
        try:
            num = float(end)
        except (TypeError, ValueError):
            continue
        if num >= best_num and series:
            best_num = num
            best_issue = str(int(num)) if num == int(num) else str(num)

    if not series or not best_issue:
        return None
    # Soft cleanup: "complete in one volume Avengers" style leftovers are rare;
    # keep the trailing series-looking phrase.
    series = re.sub(r'\s+', ' ', series).strip()
    return {'series': series, 'issue': best_issue}


# ──────────────────────────────  TMDB  ─────────────────────────────


IMDB_ID_RE = re.compile(r'(tt\d{6,})')


class TmdbClient:
    """TMDB posters, resolved by IMDb id when available (exact match)."""

    def __init__(self, api_key: str, user_agent: str, cache: ResolutionCache, verbose: bool = False):
        self.api_key = api_key
        self.user_agent = user_agent
        self.cache = cache
        self.verbose = verbose
        self.limiter = RateLimiter(min_interval=0.15)
        self.calls = 0

    def _get(self, endpoint: str, params: dict) -> dict | None:
        self.limiter.wait()
        query = dict(params)
        query['api_key'] = self.api_key
        url = f'{TMDB_BASE}/{endpoint}?' + urllib.parse.urlencode(query)
        try:
            payload = http_json(url, self.user_agent)
        except urllib.error.HTTPError as exc:
            if exc.code == 401:
                raise ConfigError('TMDB rejected the API key (401)') from exc
            if self.verbose:
                print(f'    ! tmdb http {exc.code}')
            return None
        except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError):
            return None
        self.calls += 1
        return payload

    def find_poster(self, item: dict) -> dict:
        """item is a screen entry: {id, title, year|years, imdb, wikipedia}."""
        cache_key = f'tmdb:{item.get("id")}'
        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached

        result = {'url': None}
        imdb_match = IMDB_ID_RE.search(item.get('imdb') or '')

        if imdb_match:
            payload = self._get(f'find/{imdb_match.group(1)}', {'external_source': 'imdb_id'})
            if payload:
                for bucket in ('movie_results', 'tv_results'):
                    for hit in payload.get(bucket) or []:
                        if hit.get('poster_path'):
                            result = {
                                'url': TMDB_IMAGE_BASE + hit['poster_path'],
                                'name': hit.get('title') or hit.get('name'),
                                'resource': bucket,
                                'id': hit.get('id'),
                            }
                            break
                    if result['url']:
                        break

        if not result['url']:
            title = item.get('title') or ''
            kind = 'tv' if item.get('years') else 'movie'
            payload = self._get(f'search/{kind}', {'query': title})
            best = None
            for hit in (payload or {}).get('results') or []:
                if not hit.get('poster_path'):
                    continue
                score = score_match(title, hit.get('title') or hit.get('name') or '')
                if best is None or score > best[0]:
                    best = (score, hit)
            if best and best[0] >= 0.6:
                hit = best[1]
                result = {
                    'url': TMDB_IMAGE_BASE + hit['poster_path'],
                    'name': hit.get('title') or hit.get('name'),
                    'resource': kind,
                    'id': hit.get('id'),
                    'score': round(best[0], 3),
                }

        self.cache.put(cache_key, result)
        return result


# ──────────────────────  Open Library / Amazon / Google Books  ──────────────────────


def openlibrary_cover_url(isbn: str) -> str:
    return OPENLIBRARY_COVER.format(isbn=isbn)


def amazon_cover_urls(asin: str) -> list[str]:
    return [
        AMAZON_COVER.format(asin=asin),
        AMAZON_COVER_ALT.format(asin=asin),
        AMAZON_COVER_MEDIA.format(asin=asin),
    ]


def asin_from_isbn(isbn: str | None) -> str | None:
    """Derive an Amazon-style ISBN-10 / ASIN from an ISBN-13 when possible."""
    isbn = normalize_isbn(isbn)
    if not isbn:
        return None
    if len(isbn) == 10:
        return isbn
    if len(isbn) != 13 or not isbn.startswith('978'):
        return None
    core = isbn[3:12]
    if not core.isdigit():
        return None
    total = sum(int(digit) * weight for digit, weight in zip(core, range(10, 1, -1)))
    check = (11 - (total % 11)) % 11
    return core + ('X' if check == 10 else str(check))


def prefer_large_google_cover(url: str | None) -> str | None:
    if not url:
        return None
    url = url.replace('http://', 'https://')
    url = re.sub(r'zoom=\d+', 'zoom=0', url)
    if 'zoom=' not in url:
        sep = '&' if '?' in url else '?'
        url = f'{url}{sep}zoom=0'
    return url


class GoogleBooksClient:
    """Google Books cover lookup by ISBN, then title search. API key optional."""

    def __init__(self, user_agent: str, cache: ResolutionCache,
                 api_key: str | None = None, verbose: bool = False):
        self.user_agent = user_agent
        self.cache = cache
        self.api_key = api_key
        self.verbose = verbose
        self.limiter = RateLimiter(min_interval=0.35)
        self.calls = 0

    def _search(self, query: str) -> dict | None:
        self.limiter.wait()
        params: dict[str, str] = {
            'q': query,
            'maxResults': '5',
            'printType': 'books',
            'fields': 'items(id,volumeInfo/title,volumeInfo/imageLinks,volumeInfo/industryIdentifiers)',
        }
        if self.api_key:
            params['key'] = self.api_key
        url = GOOGLE_BOOKS_API + '?' + urllib.parse.urlencode(params)
        try:
            payload = http_json(url, self.user_agent)
        except urllib.error.HTTPError as exc:
            if self.verbose:
                print(f'    ! google books http {exc.code}')
            return None
        except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError):
            return None
        self.calls += 1
        return payload

    def _from_items(self, items: list, target_title: str = '') -> dict:
        best: tuple[float, dict] | None = None
        for item in items or []:
            info = item.get('volumeInfo') or {}
            links = info.get('imageLinks') or {}
            raw = links.get('extraLarge') or links.get('large') or links.get('medium') or links.get('thumbnail')
            cover = prefer_large_google_cover(raw)
            if not cover:
                continue
            title = info.get('title') or ''
            score = score_match(target_title, title) if target_title else 0.85
            hit = {
                'url': cover,
                'name': title,
                'source': 'google-books',
                'id': item.get('id'),
                'score': round(score, 3),
            }
            if best is None or score > best[0]:
                best = (score, hit)
        if best and (not target_title or best[0] >= 0.55):
            return best[1]
        return {'url': None}

    def find_by_isbn(self, isbn: str) -> dict:
        isbn = normalize_isbn(isbn) or ''
        if not isbn:
            return {'url': None}
        cache_key = f'gbooks:isbn:{isbn}'
        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached
        payload = self._search(f'isbn:{isbn}')
        if payload is None:
            return {'url': None}  # transient failure — do not cache
        result = self._from_items((payload or {}).get('items') or [])
        self.cache.put(cache_key, result)
        return result

    def find_by_title(self, title: str) -> dict:
        title = (title or '').strip()
        if not title:
            return {'url': None}
        cache_key = f'gbooks:title:{normalize_title(title)}'
        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached
        payload = self._search(f'intitle:"{title}"')
        if payload is None:
            return {'url': None}
        result = self._from_items((payload or {}).get('items') or [], target_title=title)
        if not result.get('url'):
            payload = self._search(title)
            if payload is None:
                return {'url': None}
            result = self._from_items((payload or {}).get('items') or [], target_title=title)
        self.cache.put(cache_key, result)
        return result


def collect_run_cover_candidates(
    title: str,
    isbn: str | None,
    asin: str | None,
    google: GoogleBooksClient | None = None,
    comicvine: ComicVineClient | None = None,
    publisher_hint: str = '',
    *,
    include_api: bool = False,
) -> list[dict]:
    """Ordered cover candidates for a collected edition / run.

    By default only returns key-free CDN candidates (Open Library / Amazon).
    Pass include_api=True after those fail to add Google Books + Comic Vine.
    """
    candidates: list[dict] = []
    seen: set[str] = set()

    def add(source: str, url: str | None, name: str = '', referer: str | None = None, **extra):
        if not url or url in seen:
            return
        seen.add(url)
        candidates.append({
            'url': url,
            'name': name or title,
            'source': source,
            'referer': referer,
            **extra,
        })

    isbn_n = normalize_isbn(isbn)
    asin_n = normalize_asin(asin) or asin_from_isbn(isbn_n)

    if not include_api:
        if isbn_n:
            add('openlibrary', openlibrary_cover_url(isbn_n), title, id=isbn_n)
        if asin_n:
            for url in amazon_cover_urls(asin_n):
                add('amazon', url, title, referer='https://www.amazon.com/', id=asin_n)
        return candidates

    if google and isbn_n:
        hit = google.find_by_isbn(isbn_n)
        add('google-books', hit.get('url'), hit.get('name') or title, id=hit.get('id'))
    if google:
        hit = google.find_by_title(title)
        add('google-books', hit.get('url'), hit.get('name') or title, id=hit.get('id'), score=hit.get('score'))

    if comicvine:
        hit = comicvine.find_cover(title, publisher_hint)
        add('comicvine', hit.get('url'), hit.get('name') or title, id=hit.get('id'), score=hit.get('score'))

    return candidates


def wikipedia_image_from_url(wiki_url: str | None, user_agent: str) -> str | None:
    """Fetch original/thumbnail art from a Wikipedia article URL (same path as hero art)."""
    if not wiki_url:
        return None
    m = re.search(r'/wiki/([^?#]+)', wiki_url)
    if not m:
        return None
    title = urllib.parse.unquote(m.group(1).split('#')[0])
    if not title:
        return None
    api = 'https://en.wikipedia.org/api/rest_v1/page/summary/' + urllib.parse.quote(title, safe='')
    try:
        data = http_json(api, user_agent)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, json.JSONDecodeError):
        return None
    if not isinstance(data, dict):
        return None
    original = (data.get('originalimage') or {}).get('source')
    thumb = (data.get('thumbnail') or {}).get('source')
    return original or thumb


def collect_version_cover_candidates(
    name: str,
    google: GoogleBooksClient | None,
    comicvine: ComicVineClient | None,
    publisher_hint: str = '',
    wikipedia_url: str | None = None,
    user_agent: str | None = None,
) -> list[dict]:
    """Ordered art candidates for a character version (no ISBN).

    Cascade mirrors hero art: Wikipedia → Google Books → Comic Vine.
    """
    candidates: list[dict] = []
    seen: set[str] = set()

    def add(source: str, url: str | None, label: str = '', **extra):
        if not url or url in seen:
            return
        seen.add(url)
        candidates.append({
            'url': url,
            'name': label or name,
            'source': source,
            'referer': 'https://en.wikipedia.org/' if source == 'wikipedia' else None,
            **extra,
        })

    if wikipedia_url and user_agent:
        wiki = wikipedia_image_from_url(wikipedia_url, user_agent)
        add('wikipedia', wiki, name)

    if google:
        for query in (f'{name} comic', name):
            hit = google.find_by_title(query)
            if hit.get('url'):
                add('google-books', hit.get('url'), hit.get('name') or name, id=hit.get('id'), score=hit.get('score'))
                break

    if comicvine:
        hit = comicvine.find_character(name, publisher_hint)
        add('comicvine', hit.get('url'), hit.get('name') or name, id=hit.get('id'), score=hit.get('score'))

    return candidates
