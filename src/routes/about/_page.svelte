<script>
  import Fa from 'svelte-fa';
  import { faEnvelope } from '@fortawesome/free-solid-svg-icons';
  import { faLinkedin, faGithub } from '@fortawesome/free-brands-svg-icons';
</script>

<div class="landing" id="about">
  <img class="avatar" src="ego.jpg" alt="Simon Dirmeier" />
  <h1 class="name">Simon Dirmeier</h1>
  <p class="role">Research/ML engineer | PhD ETH</p>
  
  <p class="intro">
    Hello! I am a research/ML engineer currently working at Logitech.   
    Please reach me via LinkedIn or Email. Check out my work on GitHub. 
  </p>
  <div class="links">
    <a href="https://github.com/dirmeier">
      <Fa icon={faGithub} size="1x" /> GitHub
    </a>
    <a href="https://linkedin.com/in/simon-dirmeier">
      <Fa icon={faLinkedin} size="1x" /> LinkedIn
    </a>
    <a href="mailto:simd23 @ pm me">
      <Fa icon={faEnvelope} size="1x" /> Email
    </a>
  </div>
</div>
