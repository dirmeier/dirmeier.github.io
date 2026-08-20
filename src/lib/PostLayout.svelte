<script>
  import 'katex/dist/katex.min.css';
  import { formatDate } from '$lib/date.js';

  let { title, date, lede, children } = $props();

  /** @type {HTMLElement | undefined} */
  let article = $state();
  /** @type {{ id: string, level: string, text: string }[]} */
  let headings = $state([]);
  let activeId = $state('');

  // Marks the section the reader is currently in: the last heading whose top
  // has passed the reading line near the top of the viewport.
  $effect(() => {
    if (!article) return;
    const nodes = [...article.querySelectorAll('h2[id], h3[id]')];
    if (nodes.length === 0) return;

    const update = () => {
      let current = nodes[0].id;
      for (const node of nodes) {
        if (node.getBoundingClientRect().top <= 120) current = node.id;
      }
      activeId = current;
    };

    update();
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    return () => {
      window.removeEventListener('scroll', update);
      window.removeEventListener('resize', update);
    };
  });

  // The contents are read back off the rendered article, so the nav can live
  // outside it. rehype-slug has already put an id on every heading.
  $effect(() => {
    if (!article) return;
    headings = [...article.querySelectorAll('h2[id], h3[id]')].map((h) => ({
      id: h.id,
      level: h.tagName.toLowerCase(),
      text: h.textContent?.trim() ?? ''
    }));
  });
</script>

<svelte:head>
  <title>{title} · Simon Dirmeier</title>
</svelte:head>

<div class="post-layout">
  {#if headings.length > 1}
    <nav class="post-toc">
      <ol>
        {#each headings as heading (heading.id)}
          <li class="toc-{heading.level}" class:active={heading.id === activeId}>
            <a href="#{heading.id}">{heading.text}</a>
          </li>
        {/each}
      </ol>
    </nav>
  {/if}

  <article class="post" bind:this={article}>
    <h1>{title}</h1>
    <div class="post-meta">
      <div>
        <div class="post-meta-heading">Author</div>
        <div class="post-meta-contents">Simon Dirmeier &lt;simd23 at pm dot me&gt;</div>
      </div>
      {#if date}
        <div>
          <div class="post-meta-heading">Published</div>
          <div class="post-meta-contents">{formatDate(date)?.replace(' ', ', ')}</div>
        </div>
      {/if}
    </div>
    {#if lede}<p class="lede">{lede}</p>{/if}
    {@render children?.()}
  </article>
</div>
