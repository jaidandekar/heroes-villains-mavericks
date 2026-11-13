import assert from 'node:assert/strict';
import { rankWeekly } from '../src/lib/weekly-releases.mjs';
const item = (id, releaseDate, guideIds = [], significance = 0) => ({id, title: id, releaseDate, guideIds, significance, quality: 1});
const source = [item('unrelated', '2026-12-02'), item('older-guide', '2026-11-30', ['batman']), item('newer-guide', '2026-12-02', ['spiderman'])];
assert.deepEqual(rankWeekly(source).map(x => x.id), ['newer-guide', 'older-guide', 'unrelated']);
assert.equal(source[0].id, 'unrelated', 'Ranking must not mutate editorial data');
assert.equal(rankWeekly([item('regular', '2026-12-02', ['batman']), item('landmark', '2026-11-30', ['batman'], 2)])[0].id, 'landmark');
console.log('Guide relevance, significance, cross-month freshness, and immutable ranking passed.');
