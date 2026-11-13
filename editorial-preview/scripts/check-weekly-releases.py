"""Validate the weekly release manifest and the deliberately narrow publishing scope."""
import argparse
from datetime import date, timedelta
import json
from pathlib import Path
import re
import struct
import subprocess
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = 'editorial-preview/src/data/weekly-releases.json'
MARKER_PATH = 'editorial-preview/release-request.txt'
SOURCE_HOSTS = {'www.dc.com', 'dc.com', 'www.marvel.com', 'marvel.com', 'prhcomics.com', 'www.prhcomics.com'}
COVER_HOSTS = {'static.dc.com', 'cdn.marvel.com', 'i.annihil.us', 'images.penguinrandomhouse.com'}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def jpeg_size(path):
    data = path.read_bytes()
    require(data[:2] == b'\xff\xd8', f'{path.name}: expected a JPEG cover')
    offset = 2
    while offset + 4 < len(data):
        if data[offset] != 255:
            offset += 1
            continue
        marker = data[offset + 1]
        offset += 2
        if marker in {0xD8, 0xD9} or 0xD0 <= marker <= 0xD7:
            continue
        length = struct.unpack('>H', data[offset:offset + 2])[0]
        require(length >= 2, 'Invalid JPEG segment')
        if marker in {0xC0, 0xC1, 0xC2}:
            height, width = struct.unpack('>HH', data[offset + 3:offset + 7])
            return width, height
        offset += length
    raise ValueError(f'{path.name}: missing JPEG dimensions')

def trusted_url(value, hosts):
    url = urlsplit(value)
    require(url.scheme == 'https' and url.hostname in hosts and not url.username and not url.password, 'Untrusted source URL: ' + value)

def validate(batch, root=ROOT, publish_on=None):
    require(batch.get('schemaVersion') == 1, 'Unknown weekly data schema')
    start, end = date.fromisoformat(batch['weekStart']), date.fromisoformat(batch['weekEnd'])
    verified = date.fromisoformat(batch['verifiedOn'])
    require(start.weekday() == 0 and end == start + timedelta(days=6), 'Release week must run Monday through Sunday')
    require(start <= verified <= end, 'Verification must belong to the displayed week')
    if publish_on:
        today = date.fromisoformat(publish_on)
        require(start <= today <= end and verified == today, 'Publishing requires an edition verified today for the current week')
    guides = json.loads((root / 'src/data/guides.json').read_text())
    entries = batch['entries']
    require(1 <= len(entries) <= 16, 'Expected between 1 and 16 selected releases')
    ids, urls, isbns = set(), set(), set()
    for entry in entries:
        ident = entry['id']
        require(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', ident) and ident not in ids, 'Invalid or duplicate release ID: ' + ident)
        ids.add(ident)
        require(entry['publisher'] in {'Marvel', 'DC'}, ident + ': publisher outside agreed scope')
        require(entry['format'] in {'single-issue', 'collected-edition'}, ident + ': invalid format')
        for field in ['title', 'creators', 'summary', 'sourceLabel']:
            require(isinstance(entry[field], str) and entry[field].strip(), ident + ': missing ' + field)
        if entry['format'] == 'collected-edition':
            require(entry.get('binding') in {'Paperback', 'Hardcover'}, ident + ': collected edition needs its binding')
        release = date.fromisoformat(entry['releaseDate'])
        require(start <= release <= end and release <= verified, ident + ': release is outside this week or has not reached its release date')
        require(entry['verifiedOn'] == batch['verifiedOn'], ident + ': stale verification')
        require(isinstance(entry['guideIds'], list) and all(g in guides for g in entry['guideIds']), ident + ': unknown related guide')
        require(len(set(entry['guideIds'])) == len(entry['guideIds']), ident + ': duplicate guide connection')
        trusted_url(entry['source'], SOURCE_HOSTS)
        trusted_url(entry['coverSource'], COVER_HOSTS)
        require(entry['source'] not in urls, ident + ': duplicate edition/variant source')
        urls.add(entry['source'])
        if entry.get('isbn'):
            require(re.fullmatch(r'\d{13}|\d{17}', entry['isbn']) and entry['isbn'] not in isbns, ident + ': invalid or duplicate ISBN/UPC')
            isbns.add(entry['isbn'])
        require(entry['cover'] == 'media/weekly/' + ident + '.jpg', ident + ': cover must use the dedicated weekly asset directory')
        image = root / 'public' / entry['cover']
        require(image.is_file(), ident + ': missing cover image')
        width, height = jpeg_size(image)
        require(width >= 400 and height >= 600, ident + ': cover resolution too low')
        require(image.stat().st_size < 2_000_000, ident + ': cover file exceeds 2 MB')
        for metric in ['significance', 'quality']:
            require(type(entry.get(metric, 0)) is int and 0 <= entry.get(metric, 0) <= 3, ident + ': invalid ranking score')
    return len(entries)

def validate_scope(paths):
    require(bool(paths), 'No update to publish')
    for path in paths:
        require(path in {DATA_PATH, MARKER_PATH} or re.fullmatch(r'editorial-preview/public/media/weekly/[a-z0-9-]+\.jpg', path), 'Weekly publication must not include unrelated changes: ' + path)
    require(DATA_PATH in paths, 'A weekly publish must update the release manifest')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, default=ROOT / 'src/data/weekly-releases.json')
    parser.add_argument('--publish-on', help='YYYY-MM-DD in America/Chicago; enforces current-week freshness')
    parser.add_argument('--check-diff', help='Base commit SHA for an isolated production update')
    args = parser.parse_args()
    count = validate(json.loads(args.manifest.read_text()), publish_on=args.publish_on)
    if args.check_diff:
        paths = subprocess.check_output(['git', 'diff', '--name-only', args.check_diff], cwd=ROOT.parent, text=True).splitlines()
        paths += subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], cwd=ROOT.parent, text=True).splitlines()
        validate_scope(list(dict.fromkeys(paths)))
    print(f'Validated {count} sourced weekly releases, dates, guide connections, and cover dimensions.')

if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        raise SystemExit('Weekly release validation failed: ' + str(error))
