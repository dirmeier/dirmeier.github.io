<script>
  import { page } from '$app/state';
  import { resolve } from '$app/paths';

  let onBlog = $derived(page.url.pathname.startsWith('/blog'));
</script>

<nav class="navbar">
  {#if onBlog}
    <a href={resolve('/')} class="blog-button">Home</a>
  {:else}
    <a href={resolve('/blog')} class="blog-button">Blog</a>
  {/if}
</nav>

<style>
  .navbar {
    display: flex;
    justify-content: flex-end;
    padding: 1.25rem 1.5rem;
  }

  .blog-button {
    font-family: 'Source Serif 4', Times, serif;
    color: #2563a8;
    background: transparent;
    border: 1px solid #2563a8;
    text-decoration: none;
    border-radius: 4px;
    padding: 0.4rem 1.2rem;
    font-size: 0.9rem;
    letter-spacing: 0.01em;
    transition:
      transform 0.15s ease,
      opacity 0.15s ease;
  }

  .blog-button:hover {
    opacity: 0.7;
    transform: translateY(-1px);
  }

  @media (prefers-color-scheme: dark) {
    .blog-button {
      color: #8ab4f8;
      border-color: #8ab4f8;
    }
  }
</style>
