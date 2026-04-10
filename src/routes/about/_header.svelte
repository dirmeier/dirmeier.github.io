<script>
  import Fa from 'svelte-fa';
  import { faEnvelope } from '@fortawesome/free-solid-svg-icons';
  import { faLinkedin, faGithub } from '@fortawesome/free-brands-svg-icons';

  let imageUrl = 'ego.jpg';
</script>

<div>
  <div class="columns">
    <div class="column is-2"><img src={imageUrl} alt="None" /></div>
    <div class="column is-7">
      <div style="margin-top: 20px">
        Hello, I am Simon <span>👋</span>
      </div>
      <div style="margin-top: 20px; text-align: justify;">
        I am currently working as a senior AI/ML engineer at
        <a href="https://www.logitech.com/en-ch">Logitech</a>. Previously, I was
        working in the research team at the
        <a href="https://www.datascience.ch/">Swiss Data Science Center</a>,
        conducting my doctoral studies in computational statistics at
        <a href="https://ethz.ch/en.html">ETH Zurich</a>, and studying at
        <a href="https://www.tum.de/en/">TU Munich</a>.
      </div>
      <div style="margin-top: 20px">
        If you want to chat, you can reach me here:
        <a
          href="mailto:simd23 @ pm me"
          style="color: black; margin-left: 10px;"
        >
          <Fa icon={faEnvelope} size="1x" />
        </a>
        <a
          href="https://www.linkedin.com/in/simon-dirmeier/"
          style="color: black; margin-left: 10px;"
        >
          <Fa icon={faLinkedin} size="1x" />
        </a>
        <a
          href="https://github.com/dirmeier"
          style="color: black; margin-left: 10px;"
        >
          <Fa icon={faGithub} size="1x" />
        </a>
      </div>
    </div>
  </div>
</div>
