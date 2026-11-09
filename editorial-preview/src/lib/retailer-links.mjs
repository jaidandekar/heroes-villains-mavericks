const stores = {
  Amazon: ['https://www.amazon.com/s', 'k'],
  'Hot Topic': ['https://www.hottopic.com/search', 'q'],
  BoxLunch: ['https://www.boxlunch.com/search', 'q'],
};

export function retailerSearchUrl(store, query) {
  if (!stores[store]) return undefined;
  if (!query?.trim()) throw new Error(`Missing shopping search terms for ${store}`);
  const [base, parameter] = stores[store];
  const url = new URL(base);
  url.searchParams.set(parameter, query.trim().replace(/\s+/g, ' '));
  return url.href;
}

export function amazonBookSearch(title, creators = '') {
  const author = creators.split(/\s+(?:&|and)\s+|,/)[0].trim();
  const query = author && !title.toLowerCase().includes(author.toLowerCase()) ? `${title} ${author}` : title;
  return retailerSearchUrl('Amazon', query);
}
