const guideWeight = 100;
export function rankWeekly(entries) {
  return [...entries].sort((a, b) => score(b) - score(a) || a.title.localeCompare(b.title));
}
function score(entry) {
  // Verified sources and dates are eligibility gates, not soft ranking signals.
  return (entry.guideIds.length ? guideWeight : 0) + (entry.significance ?? 0) * 5 + Date.parse(entry.releaseDate) / 86400000 / 100 + (entry.quality ?? 0);
}
export function weekLabel(batch) {
  const fmt = new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric', timeZone: 'UTC' });
  return `${fmt.format(new Date(batch.weekStart + 'T12:00:00Z'))}–${fmt.format(new Date(batch.weekEnd + 'T12:00:00Z'))}, ${batch.weekStart.slice(0, 4)}`;
}
