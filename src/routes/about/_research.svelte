<script>
  import research from './_research.json';
</script>

<div>
  <h4 class="title is-4">Recent work</h4>
  <div class="columns">
    <div class="column is-9" style="text-align: justify;">
      <ul>
        {#each research as item (item.arxiv_id)}
          <li>
            <b>{item.title}</b>
            (<a href={item.arxiv_url} target="_blank" rel="noopener noreferrer">
              arXiv:{item.arxiv_id}
            </a>): {item.description}
            <br />
            <i>
              Keywords: {item.keywords.join(', ')}
            </i>
          </li>
        {/each}
        <li>More to come soon...</li>
      </ul>
    </div>
  </div>
</div>
