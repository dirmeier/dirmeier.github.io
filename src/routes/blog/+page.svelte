<script>
  let { data } = $props();

  const MONTHS = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
  ];

  function formatDate(date) {
    if (!date) return null;
    const [year, month] = date.split('-');
    return `${MONTHS[Number(month) - 1]} ${year}`;
  }
</script>

<svelte:head>
  <title>Blog · Simon Dirmeier</title>
</svelte:head>

<section class="blog">
  <h1>Blog</h1>
  <ul>
    {#each data.posts as post (post.url)}
      <li>
        <span class="post-date">{formatDate(post.date) ?? '—'}</span>
        <a href={post.url} rel="external">{post.title}</a>
        {#if post.description}
          <span class="post-description"> — {post.description}</span>
        {/if}
      </li>
    {/each}
  </ul>
</section>

<style>
  .blog {
    max-width: 38rem;
    margin: 0 auto;
    padding: 3rem 1.5rem 4rem;
  }

  .blog h1 {
    font-size: 1.6rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
  }

  .blog ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .blog li {
    margin-bottom: 1.1rem;
    line-height: 1.6;
  }

  .post-date {
    display: inline-block;
    min-width: 7rem;
    color: #9ca3af;
    font-size: 0.85rem;
  }

  .blog a {
    color: inherit;
    text-decoration: none;
    border-bottom: 1px solid transparent;
    padding-bottom: 1px;
    transition:
      border-color 0.15s ease,
      opacity 0.15s ease;
  }

  .blog a:hover {
    border-bottom-color: currentColor;
    opacity: 0.75;
  }

  .post-description {
    color: #6b7280;
  }

  @media (prefers-color-scheme: dark) {
    .post-date {
      color: #6b7280;
    }

    .post-description {
      color: #a1a1aa;
    }
  }
</style>
