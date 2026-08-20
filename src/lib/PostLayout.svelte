<script>
  import 'katex/dist/katex.min.css';
  import { formatDate } from '$lib/date.js';

  let { title, date, lede, children } = $props();

  /** @type {HTMLElement | undefined} */
  let article = $state();
  /** @type {{ id: string, text: string }[]} */
  let sections = $state([]);
  let activeId = $state('');

  // mdsvex posts carry the id on the heading (rehype-slug); imported Quarto
  // posts put it on the wrapping <section> and leave data-anchor-id behind.
  // Imported Quarto posts open their sections with <h1>, mdsvex posts with
  // <h2>, so the shallowest heading present is the section level; deeper
  // headings are sub-sections and stay out of the contents. The layout's own
  // title is skipped.
  /** @param {HTMLElement} root */
  function anchored(root) {
    const found = [...root.querySelectorAll('h1, h2, h3')]
      .filter((el) => !el.classList.contains('post-title'))
      .map((el) => ({
        el,
        depth: Number(el.tagName[1]),
        id:
          el.id ||
          el.getAttribute('data-anchor-id') ||
          el.closest('section')?.id ||
          ''
      }))
      .filter((entry) => entry.id);

    const top = Math.min(...found.map((entry) => entry.depth));
    return found.filter((entry) => entry.depth === top);
  }

  // Marks the section the reader is currently in: the last heading whose top
  // has passed the reading line near the top of the viewport.
  $effect(() => {
    if (!article) return;
    const nodes = anchored(article);
    if (nodes.length === 0) return;

    const update = () => {
      let current = nodes[0].id;
      for (const node of nodes) {
        if (node.el.getBoundingClientRect().top <= 120) current = node.id;
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
    sections = anchored(article).map(({ el, id }) => ({
      id,
      text: el.textContent?.trim() ?? ''
    }));
  });
</script>

<svelte:head>
  <title>{title} · Simon Dirmeier</title>
</svelte:head>

<div class="post-layout">
  {#if sections.length > 1}
    <nav class="post-toc">
      <ol>
        {#each sections as section (section.id)}
          <li class:active={section.id === activeId}>
            <a href="#{section.id}">{section.text}</a>
          </li>
        {/each}
      </ol>
    </nav>
  {/if}

  <article class="post" bind:this={article}>
    <h1 class="post-title">{title}</h1>
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
