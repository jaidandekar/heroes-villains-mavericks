// Match catalog identities before publishing. Alternate display titles are explicit.
const aliases = {
  'doom-1994': 'Fantastic Four',
  'ff-first-steps': 'The Fantastic 4: First Steps',
  'cf-caped': 'The Batman',
  'sm-tas': 'Spider-Man',
};
const normalize = value => value.toLowerCase().replace(/[^a-z0-9]/g, '');
export function validateScreenArt(guides, artwork) {
  for (const guide of Object.values(guides)) {
    for (const group of guide.screen) {
      for (const item of group.items) {
        const art = artwork[item.id];
        const expectedTitle = aliases[item.id] || item.title;
        const year = String(item.year || item.years).match(/\d{4}/)?.[0];
        if (!art || normalize(art.resolvedTitle || '') !== normalize(expectedTitle)
          || art.releaseYear !== year || !['movie', 'tv'].includes(art.kind)
          || !art.source?.startsWith('https://www.themoviedb.org/' + art.kind + '/')
          || art.imdb !== item.imdb || !art.src || !art.verifiedAt) {
          throw new Error(`Review film/TV artwork identity for ${guide.id}: ${item.title} (${year})`);
        }
      }
    }
  }
}
