import postsRaw from '$lib/posts.jsonl?raw';

export const prerender = true;

export function load() {
  const posts = postsRaw
    .split('\n')
    .filter((line) => line.trim().length > 0)
    .map((line) => JSON.parse(line))
    .sort((a, b) => (b.date ?? '').localeCompare(a.date ?? ''));

  return { posts };
}
