#!/usr/bin/env node
/**
 * Downloads cover art into images/covers/ for offline use.
 * Run: node scripts/download-covers.mjs
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const RUNS_DIR = path.join(ROOT, 'images/covers/runs');
const VERSIONS_DIR = path.join(ROOT, 'images/covers/versions');

const RUN_ISBN = {
  'year-one': '9781401207526',
  'long-halloween': '9781401232597',
  'dark-victory': '9781401233309',
  'killing-joke': '9781401284272',
  'death-in-the-family': '9781401293623',
  'knightfall': '9781401233217',
  'no-mans-land': '9781401295277',
  'hush': '9781401297244',
  'under-the-red-hood': '9781401231453',
  'batman-rip': '9781401220325',
  'court-of-owls': '9781401235420',
  'death-of-the-family': '9781401242370',
  'earth-two-golden-age': '9781563890433',
  'dark-knight-returns': '9781563893421',
  'flashpoint-knight-of-vengeance': '9781401234054',
  'crime-syndicate': '9781401249367',
  'red-rain': '9781563890369',
  'hush-beyond': '9781401229887',
  'earth-2-planetfall': '9781401242819',
  'batman-who-laughs': '9781779504463',
  'grim-knight': '9781779504463',
  'red-death': '9781401289072',
  'dawnbreaker': '9781401289072',
  'murder-machine': '9781401289072',
  'gotham-by-gaslight': '9781779524058',
  'white-knight': '9781401274527',
  'thrillkiller': '9781401204214',
  'holy-terror': '9781563892034',
  'batman-66-vol-1': '9781401244737',
  'in-darkest-knight': '9781563891266',
  'the-drowned': '9781401289072',
};

const RUN_ASIN = {
  'year-one': '1401207529',
  'long-halloween': '1401232590',
  'dark-victory': '1401233309',
  'killing-joke': '1401284272',
  'death-in-the-family': '1401293623',
  'knightfall': '140123321X',
  'no-mans-land': '1401295271',
  'hush': '1401297242',
  'under-the-red-hood': '1401231454',
  'batman-rip': '1401220322',
  'court-of-owls': '1401235425',
  'death-of-the-family': '1401242370',
  'earth-two-golden-age': '1563890439',
  'dark-knight-returns': '1563893428',
  'flashpoint-knight-of-vengeance': '1401234054',
  'crime-syndicate': '1401249367',
  'red-rain': '1563890364',
  'hush-beyond': '1401229887',
  'earth-2-planetfall': '1401242818',
  'batman-who-laughs': '1779504462',
  'grim-knight': '1779504462',
  'red-death': '1401289072',
  'dawnbreaker': '1401289072',
  'murder-machine': '1401289072',
  'gotham-by-gaslight': '1779524056',
  'white-knight': '1401274527',
  'thrillkiller': '1401204219',
  'holy-terror': '1563892030',
  'batman-66-vol-1': '1401244737',
  'in-darkest-knight': '1563891265',
  'the-drowned': '1401289072',
};

const COVER_OVERRIDES = {
  'year-one': 'https://upload.wikimedia.org/wikipedia/en/1/10/Batman_-_Year_One_%28softcover%29.jpg',
  'long-halloween': 'https://upload.wikimedia.org/wikipedia/en/2/2f/The_Long_Halloween.jpg',
  'dark-victory': 'https://upload.wikimedia.org/wikipedia/en/4/4c/Batman_-_Dark_Victory_%28softcover%29.jpg',
  'killing-joke': 'https://upload.wikimedia.org/wikipedia/en/b/bc/Batman_The_Killing_Joke.jpg',
  'death-in-the-family': 'https://upload.wikimedia.org/wikipedia/en/3/37/Batman_-_A_Death_in_the_Family_%28softcover%29.jpg',
  'knightfall': 'https://upload.wikimedia.org/wikipedia/en/2/2d/Batman_-_Knightfall_Vol._1_%28softcover%29.jpg',
  'no-mans-land': 'https://upload.wikimedia.org/wikipedia/en/8/8e/Batman_-_No_Man%27s_Land_Vol._1_%28softcover%29.jpg',
  'hush': 'https://upload.wikimedia.org/wikipedia/en/9/9d/Batman_Hush_TPB_cover.jpg',
  'under-the-red-hood': 'https://upload.wikimedia.org/wikipedia/en/6/6e/Batman_-_Under_the_Red_Hood_%28softcover%29.jpg',
  'batman-rip': 'https://upload.wikimedia.org/wikipedia/en/9/9a/Batman_R.I.P._TPB.jpg',
  'court-of-owls': 'https://upload.wikimedia.org/wikipedia/en/4/4d/Batman_-_The_Court_of_Owls_%28softcover%29.jpg',
  'death-of-the-family': 'https://upload.wikimedia.org/wikipedia/en/1/1e/Batman_-_Death_of_the_Family_%28softcover%29.jpg',
  'dark-knight-returns': 'https://upload.wikimedia.org/wikipedia/en/5/50/Batman_-_The_Dark_Knight_Returns_%28softcover%29.jpg',
  'red-rain': 'https://upload.wikimedia.org/wikipedia/en/d/d9/Batman_%26_Dracula_-_Red_Rain.jpg',
  'gotham-by-gaslight': 'https://upload.wikimedia.org/wikipedia/en/4/4f/Gotham_by_Gaslight.jpg',
  'white-knight': 'https://upload.wikimedia.org/wikipedia/en/8/8f/Batman_-_White_Knight_%28softcover%29.jpg',
  'batman-who-laughs': 'https://upload.wikimedia.org/wikipedia/en/9/9f/The_Batman_Who_Laughs_%28softcover%29.jpg',
  'flashpoint-knight-of-vengeance': 'https://upload.wikimedia.org/wikipedia/en/0/0d/Flashpoint_-_Batman_Knight_of_Vengeance_%28softcover%29.jpg',
  'hush-beyond': 'https://upload.wikimedia.org/wikipedia/en/5/5c/Batman_Beyond_-_Hush_Beyond_%28softcover%29.jpg',
  'in-darkest-knight': 'https://upload.wikimedia.org/wikipedia/en/9/9b/Batman_-_In_Darkest_Knight_%28softcover%29.jpg',
  'holy-terror': 'https://upload.wikimedia.org/wikipedia/en/2/2a/Batman_-_Holy_Terror_%28softcover%29.jpg',
  'batman-66-vol-1': 'https://upload.wikimedia.org/wikipedia/en/1/1f/Batman_%2766_Vol._1_%28softcover%29.jpg',
};

const VERSION_ART = {
  'prime-earth-batman': 'https://upload.wikimedia.org/wikipedia/en/1/1a/Batman_%28DC_Comics_character%29.jpg',
  'earth-two-batman': 'https://upload.wikimedia.org/wikipedia/en/1/1a/Batman_%28DC_Comics_character%29.jpg',
  'earth-31-batman': 'https://upload.wikimedia.org/wikipedia/en/5/50/Batman_-_The_Dark_Knight_Returns_%28softcover%29.jpg',
  'thomas-wayne-batman': 'https://upload.wikimedia.org/wikipedia/en/0/0d/Flashpoint_-_Batman_Knight_of_Vengeance_%28softcover%29.jpg',
  'owlman': 'https://upload.wikimedia.org/wikipedia/en/9/9e/Owlman_%28DC_Comics%29.jpg',
  'vampire-batman': 'https://upload.wikimedia.org/wikipedia/en/d/d9/Batman_%26_Dracula_-_Red_Rain.jpg',
  'batman-beyond': 'https://upload.wikimedia.org/wikipedia/en/a/a6/Batman_Beyond_%28character%29.jpg',
  'earth-2-batman-new-52': 'https://upload.wikimedia.org/wikipedia/en/4/4d/Batman_-_The_Court_of_Owls_%28softcover%29.jpg',
  'batman-who-laughs': 'https://upload.wikimedia.org/wikipedia/en/9/9f/The_Batman_Who_Laughs_%28softcover%29.jpg',
  'grim-knight': 'https://upload.wikimedia.org/wikipedia/en/9/9f/The_Batman_Who_Laughs_%28softcover%29.jpg',
  'red-death': 'https://upload.wikimedia.org/wikipedia/en/9/9f/The_Batman_Who_Laughs_%28softcover%29.jpg',
  'dawnbreaker': 'https://upload.wikimedia.org/wikipedia/en/9/9f/The_Batman_Who_Laughs_%28softcover%29.jpg',
  'murder-machine': 'https://upload.wikimedia.org/wikipedia/en/9/9f/The_Batman_Who_Laughs_%28softcover%29.jpg',
  'gaslight-batman': 'https://upload.wikimedia.org/wikipedia/en/4/4f/Gotham_by_Gaslight.jpg',
  'white-knight-batman': 'https://upload.wikimedia.org/wikipedia/en/8/8f/Batman_-_White_Knight_%28softcover%29.jpg',
  'thrillkiller-batman': 'https://upload.wikimedia.org/wikipedia/en/1/1a/Batman_%28DC_Comics_character%29.jpg',
  'holy-terror-batman': 'https://upload.wikimedia.org/wikipedia/en/2/2a/Batman_-_Holy_Terror_%28softcover%29.jpg',
  'batman-66': 'https://upload.wikimedia.org/wikipedia/en/1/1f/Batman_%2766_Vol._1_%28softcover%29.jpg',
  'darkest-knight-batman': 'https://upload.wikimedia.org/wikipedia/en/9/9b/Batman_-_In_Darkest_Knight_%28softcover%29.jpg',
  'the-drowned': 'https://upload.wikimedia.org/wikipedia/en/9/9f/The_Batman_Who_Laughs_%28softcover%29.jpg',
};

function unique(urls) {
  return [...new Set(urls.filter(Boolean))];
}

function runSourceUrls(slug) {
  const isbn13 = RUN_ISBN[slug];
  const isbn10 = isbn13 ? isbn13.replace(/^978/, '') : null;
  const asin = RUN_ASIN[slug];
  const urls = [];

  if (COVER_OVERRIDES[slug]) urls.push(COVER_OVERRIDES[slug]);
  if (isbn13) {
    urls.push(`https://covers.openlibrary.org/b/isbn/${isbn13}-L.jpg?default=false`);
    urls.push(`https://covers.openlibrary.org/b/isbn/${isbn13}-M.jpg?default=false`);
    urls.push(`https://books.google.com/books/content?vid=ISBN:${isbn13}&printsec=frontcover&img=1&zoom=1`);
  }
  if (isbn10) urls.push(`https://covers.openlibrary.org/b/isbn/${isbn10}-L.jpg?default=false`);
  if (asin) {
    urls.push(`https://images-na.ssl-images-amazon.com/images/P/${asin}.01._SCMZZZZZZZ_.jpg`);
    urls.push(`https://images-na.ssl-images-amazon.com/images/P/${asin}.01.LZZZZZZZ.jpg`);
  }
  return unique(urls);
}

async function downloadFirst(urls, dest) {
  for (const url of urls) {
    try {
      const res = await fetch(url, {
        headers: { 'User-Agent': 'BatmanReadingGuide/1.0 (cover downloader)' },
        redirect: 'follow',
      });
      if (!res.ok) {
        console.log(`  skip ${res.status} ${url}`);
        continue;
      }
      const type = res.headers.get('content-type') || '';
      const buf = Buffer.from(await res.arrayBuffer());
      if (buf.length < 1500) {
        console.log(`  skip tiny (${buf.length}b) ${url}`);
        continue;
      }
      if (!type.includes('image') && !url.includes('openlibrary') && !url.includes('wikimedia')) {
        console.log(`  skip non-image ${type} ${url}`);
        continue;
      }
      fs.writeFileSync(dest, buf);
      return { url, bytes: buf.length };
    } catch (err) {
      console.log(`  error ${url}: ${err.message}`);
    }
  }
  return null;
}

async function main() {
  fs.mkdirSync(RUNS_DIR, { recursive: true });
  fs.mkdirSync(VERSIONS_DIR, { recursive: true });

  let ok = 0;
  let fail = 0;

  console.log('\n📚 Downloading run covers...\n');
  for (const slug of Object.keys(RUN_ISBN)) {
    const dest = path.join(RUNS_DIR, `${slug}.jpg`);
    if (fs.existsSync(dest) && fs.statSync(dest).size > 1500) {
      console.log(`✓ ${slug} (cached)`);
      ok++;
      continue;
    }
    process.stdout.write(`${slug}... `);
    const result = await downloadFirst(runSourceUrls(slug), dest);
    if (result) {
      console.log(`✓ ${Math.round(result.bytes / 1024)}KB`);
      ok++;
    } else {
      console.log('✗ failed');
      fail++;
    }
  }

  console.log('\n🦇 Downloading version art...\n');
  const versionToRun = {
    'prime-earth-batman': 'year-one',
    'earth-two-batman': 'earth-two-golden-age',
    'earth-31-batman': 'dark-knight-returns',
    'thomas-wayne-batman': 'flashpoint-knight-of-vengeance',
    'owlman': 'crime-syndicate',
    'vampire-batman': 'red-rain',
    'batman-beyond': 'hush-beyond',
    'earth-2-batman-new-52': 'earth-2-planetfall',
    'batman-who-laughs': 'batman-who-laughs',
    'grim-knight': 'grim-knight',
    'red-death': 'red-death',
    'dawnbreaker': 'dawnbreaker',
    'murder-machine': 'murder-machine',
    'gaslight-batman': 'gotham-by-gaslight',
    'white-knight-batman': 'white-knight',
    'thrillkiller-batman': 'thrillkiller',
    'holy-terror-batman': 'holy-terror',
    'batman-66': 'batman-66-vol-1',
    'darkest-knight-batman': 'in-darkest-knight',
    'the-drowned': 'the-drowned',
  };

  for (const [slug, artUrl] of Object.entries(VERSION_ART)) {
    const dest = path.join(VERSIONS_DIR, `${slug}.jpg`);
    if (fs.existsSync(dest) && fs.statSync(dest).size > 1500) {
      console.log(`✓ ${slug} (cached)`);
      ok++;
      continue;
    }
    process.stdout.write(`${slug}... `);
    const runSlug = versionToRun[slug];
    const localRun = runSlug ? path.join(RUNS_DIR, `${runSlug}.jpg`) : null;
    const urls = unique([
      artUrl,
      localRun && fs.existsSync(localRun) ? `file://${localRun}` : null,
      ...(runSlug ? runSourceUrls(runSlug) : []),
    ]);
    // Use local run file directly if already downloaded
    let result = null;
    if (localRun && fs.existsSync(localRun) && fs.statSync(localRun).size > 1500) {
      fs.copyFileSync(localRun, dest);
      result = { url: 'local run copy', bytes: fs.statSync(dest).size };
    } else {
      result = await downloadFirst(urls.filter(u => !u.startsWith('file://')), dest);
    }
    if (result) {
      console.log(`✓ ${Math.round(result.bytes / 1024)}KB`);
      ok++;
    } else {
      console.log('✗ failed');
      fail++;
    }
  }

  console.log(`\nDone: ${ok} ok, ${fail} failed`);
  console.log(`Covers saved to ${path.join(ROOT, 'images/covers')}\n`);
}

main();
