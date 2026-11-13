# Weekly releases: editorial and publishing runbook

## Agreed scope and schedule

Marvel and DC U.S. print releases, prioritizing the ten redesigned character guides. Include single issues and collected editions, without treating alternate covers as separate recommendations. Run every Wednesday at 9:00 a.m. America/Chicago (follow daylight saving time). Show a curated selection of up to 16 items, not an exhaustive release catalog.

Codex automation ID: `weekly-marvel-and-dc-releases` (created PAUSED). Local scheduled runs require the desktop app and computer to remain available; this is not a GitHub-hosted research scheduler.

The initial section and schedule are local review work. The schedule is PAUSED until the section has been approved, published, and the isolated publication path has been tested. Do not publish the current redesign merely to enable the automation.

## Durable files

- `src/data/weekly-releases.json`: one dated edition, source URLs, creators, dates, cover provenance, and related guides.
- `public/media/weekly/`: dedicated release-cover assets only.
- `src/components/WeeklyReleases.astro`: compact card presentation and dated fallback for stale editions.
- `scripts/check-weekly-releases.py`: model, dates, image dimensions, and publication-diff checks.
- `scripts/tests/test_weekly_releases.py`: failure cases, including unrelated code/design updates.

## Research each edition

1. Calculate Monday–Sunday of the current week in America/Chicago. Use full ISO dates throughout the manifest.
2. Discover Marvel and DC releases from their official calendars and product pages and the Penguin Random House Comics Retail catalog. Search both single issues and collected editions separately. Never confuse FOC dates, announcements, original-story dates, digital subscription arrivals, or variant covers with print on-sale dates.
3. Follow product pages for the exact edition. Publisher or distributor product records must support the release date, format, title, creators, and cover. Retailer lists can help discovery; a retailer result alone does not establish a date. If a publisher and distributor disagree, resolve the edition/channel difference or omit that entry. Do not infer a date from a URL or search-snippet timestamp.
4. If a publisher blocks direct HTTP access, use the connected browser/web source tools to read its product page. If neither route verifies the details, omit that item and explain the gap in the run report. Do not pad the list to meet a count.
5. Paraphrase short, factual summaries. Do not write in Jai's voice, claim he read a book, invent reviews, rank sales, or add unverified entertainment connections. A related guide link needs a genuine character or story connection.
6. Prioritize guide-related releases, then significance (new series, collected entry points), date freshness, and source/artwork quality. Verification and current-week eligibility are hard gates. Use one main cover per release. Select a balanced Marvel/DC edition when the verified catalog supports it.
7. Download real publisher/distributor covers into the dedicated weekly directory. Visually confirm each image matches the correct release/edition, is not a placeholder, and contains the intended cover. Preserve aspect ratios. Minimum JPEG dimensions: 400 x 600; maximum 2 MB. The PRH `700jpg` rendition is larger than the default thumbnail.
8. Set the batch and every entry's `verifiedOn` to today's Central date only after actually rechecking their sources. Put no future-dated books in the released list. Leave the previous edition intact if research fails.

## Update and test locally

Update only the manifest and weekly covers. The source schema example is the current manifest; `guideIds` must resolve to `src/data/guides.json`. `single-issue` and `collected-edition` are distinct formats; a graphic novel reprinted in issue format remains a single issue.

Run from `editorial-preview`:

```sh
python3 -B scripts/check-weekly-releases.py --publish-on YYYY-MM-DD
python3 -B -m unittest discover -s scripts/tests -v
node scripts/test-weekly-ranking.mjs
pnpm build
python3 -B scripts/prepare-release.py --repo REPO --public-url https://jaidandekar.github.io/heroes-villains-mavericks/ --output NEW_TEMP_DIRECTORY
```

Review mobile and desktop layout, compact card content, cover images, the source and guide links, and stale-edition messaging. `pnpm build` always validates the dataset but deliberately permits a dated previous edition so a failed refresh does not break the site. The explicit `--publish-on` gate disallows publishing stale data as a fresh edition.

## Isolated publication after activation

1. Fetch the current production `main` through GitHub. Build a clean temporary checkout from that exact SHA. Do not publish from the local working branch or merge it into production.
2. Confirm production already contains the approved weekly section and validator. If absent, stop and report that initial publication is still needed.
3. Research and modify the manifest and covers in that clean checkout. Test the candidate as above. Update `editorial-preview/release-request.txt` with the weekly edition date to trigger the existing Pages workflow.
4. Before committing, use `python3 -B scripts/check-weekly-releases.py --publish-on YYYY-MM-DD --check-diff BASE_MAIN_SHA`. Every changed path must be exactly one of:
   - `editorial-preview/src/data/weekly-releases.json`
   - `editorial-preview/public/media/weekly/<release-id>.jpg`
   - `editorial-preview/release-request.txt`
5. Build GitHub blobs/tree/commit from that allowlist against the fetched main tree using the connected GitHub tools. Never include local template, CSS, logo, workflow, or other editorial changes. Verify the generated tree equals the tested candidate tree. Update `main` with `force=false` and `expected_sha=BASE_MAIN_SHA`.
6. If `main` moved, refetch and revalidate; do not force-push. If access, verification, or checks fail, keep the live edition and report the reason.
7. Monitor the deployment through completion. Check the live weekly heading/date, item count, loaded covers, links, and related guide links. Report the published edition and commit. Do not claim success before deployment and live checks pass.

## Rollback and failures

Git history is the edition archive. Record the pre-update production SHA in each run report. If deployment fails before publishing, leave the existing live artifact intact and report the failed workflow. For an incorrect weekly edition after deployment, restore only the previous manifest and its cover assets from the pre-update SHA, update the release marker, run validation for that dated edition without the fresh-publication gate, and publish a rollback commit through the same narrow path allowlist. The UI will identify a previous week as the latest verified edition instead of calling it new this week. Never reset or force-push the repository, or roll back unrelated site changes.

## First edition research notes

Week of November 9–15, 2026; checked November 12. Eight selections have DC or PRH product records linked in the manifest. Three collections have distributor on-sale dates of November 10. `Emperor Doom #1` is the 1987 story newly reprinted in comic-book format, not a newly written graphic novel. A Captain America collection was omitted because PRH dates it November 3 despite a retailer listing it this week.
