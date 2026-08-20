<script>
  import { page } from '$app/state';
  import { resolve } from '$app/paths';

  // Inside a post the button goes back to the blog index; from the index
  // itself it goes home.
  let onPost = $derived(/^\/blog\/.+/.test(page.url.pathname));
  let onBlogIndex = $derived(page.url.pathname.replace(/\/$/, '') === '/blog');
</script>

<nav class="navbar">
  {#if onPost}
    <a href={resolve('/blog')} class="blog-button">Blog</a>
  {:else if onBlogIndex}
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
</style>
