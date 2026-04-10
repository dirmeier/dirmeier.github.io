<script>
  import projects from './_projects.json';
</script>

<div>
  <h4 class="title is-4">Code</h4>
  You can find my software on
  <a href="https://github.com/dirmeier">GitHub</a>
  . Some recent projects are:
  <div class="columns">
    <div class="column is-9">
      <ul>
        {#each projects as project (project.name)}
          <li>
            <a href={project.url} target="_blank" rel="noopener noreferrer">
              <span style="font-family: monospace;">{project.name}</span>
            </a>
            : {project.description}
          </li>
        {/each}
      </ul>
    </div>
  </div>
</div>
