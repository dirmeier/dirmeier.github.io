# Personal site restyle — design

Date: 2026-07-05
Repo: `dirmeier.github.io` (SvelteKit + Bulma 1.0, monospace restyle)

## Goal

Restyle the personal site so its "optics" read as a **research engineer**
(large-scale CUDA on GPU clusters, expert JAX), not primarily a past-ML-research
academic. Improve visual polish, reposition the copy, and reorder sections.

## Decisions

### Visual style — "light terminal"

- **Font:** monospace throughout, via the system `ui-monospace, 'SF Mono',
  monospace` stack. No web-font network load. (JetBrains Mono is a possible
  swap-in later; not in scope.)
- **Background:** light (white) **always**, including under
  `prefers-color-scheme: dark`. Preserves the existing dark-mode override so the
  page never turns grey. `html` and `body` both pinned to white in the dark
  media query.
- **Terminal accents:**
  - `~ ` prefix before the name (muted grey `#a1a1aa`).
  - `## ` prefix before each section heading (muted grey), heading text green
    `#2f9e44`.
- **Colors (tuned for light bg):** links blue `#2563a8` with a subtle
  underline; `code` / project names violet `#6d28d9`; section headings green.
- **Layout:** refined spacing; bio/prose capped at ~64ch reading width.
- **Capitalization:** normal sentence/title case (no forced lowercase).

### Content / copy — "interests, not job title"

- Bio stays **factual about employment, with no current-task claims**. Drop the
  "I build high-performance ML systems" opening line so nothing implies that is
  the Logitech role.
- Header:
  - Name: `Simon Dirmeier`
  - Role subtitle: `Research engineer — GPU clusters, CUDA, JAX`
  - Prose: keep existing "currently a senior AI/ML engineer at Logitech;
    previously research at the Swiss Data Science Center; PhD in computational
    statistics at ETH Zurich; studied at TU Munich" with existing links.
  - Contact icons (email, LinkedIn, GitHub) retained.
- New **Focus** chips row directly under the bio — this carries the specialty
  signal instead of the prose: `CUDA` `JAX` `C++` `Generative models` `HPC`.
  (Chip set is easy to adjust.)

### Structure — section order

1. Bio + Focus chips
2. Code (projects) — restyled as a two-column `name → description` grid
3. Recent work (research / arXiv list)
4. Interests
5. Reading

## Scope of changes

- `src/app.scss` — monospace font stack, terminal-accent colors, section
  heading styling, chip styling, keep light-in-dark-mode override for `html` +
  `body` + `.title`.
- `src/routes/about/_header.svelte` — role subtitle, drop the current-work
  claim, add Focus chips block.
- `src/routes/about/_page.svelte` — reorder sections (Code → Recent work →
  Interests → Reading).
- `src/routes/about/_projects.svelte` — two-column grid markup for the project
  list.
- Section heading components (`_projects`, `_research`, `_interests`,
  `_reading`) — consistent `## ` heading treatment (via shared class or CSS on
  `.title.is-4`).

Out of scope: framework changes, new dependencies, web fonts, performance/SEO
work, content of the Research/Reading lists themselves.

## Success criteria

- Page uses the monospace light-terminal aesthetic in both light and dark OS
  modes (background stays white in both).
- Bio makes no claim that CUDA/JAX/HPC is the current Logitech role.
- Focus chips + projects visibly signal the CUDA/JAX/HPC specialty.
- Sections appear in the new order.
- `npm run dev` renders cleanly; no console errors.
