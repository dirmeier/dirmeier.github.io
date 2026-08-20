import postsRaw from '$lib/posts.jsonl?raw';

export const prerender = true;

// Dates are month-granular, so posts sharing a month compare equal. The sort
// is stable, which leaves those in the order posts.jsonl lists them — the file
// is kept newest-first so that order is the one on the page.
export function load() {
  const posts = postsRaw
    .split('\n')
    .filter((line) => line.trim().length > 0)
    .map((line) => JSON.parse(line))
    .sort((a, b) => (b.date ?? '').localeCompare(a.date ?? ''));

  return { posts };
}
