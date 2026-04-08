<script>
  import Research from './_research.svelte';
  import Projects from './_projects.svelte';
  import Fa from 'svelte-fa';
  import { faEnvelope } from '@fortawesome/free-solid-svg-icons';
  import { faLinkedin, faGithub } from '@fortawesome/free-brands-svg-icons';

  let imageUrl = 'ego.jpg';
</script>

<div id="about" style="margin-top: 1%">
  <section>
    <div class="columns">
      <div class="column is-2"><img src={imageUrl} alt="None" /></div>
      <div class="column is-7">
        <div style="margin-top: 20px">
          Hello, I am Simon <span>👋</span>
        </div>
        <div style="margin-top: 20px">
          I am currently working as a senior AI/ML engineer at
          <a href="https://www.logitech.com/en-ch">Logitech</a>
          . Previously, I was working in the research team at the
          <a href="https://www.datascience.ch/">Swiss Data Science Center</a>
          , conducting my doctoral studies in computational statistics at
          <a href="https://ethz.ch/en.html">ETH Zurich</a>
          , and studying at
          <a href="https://www.tum.de/en/">TU Munich</a>
          .
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
  </section>
  <section>
    <Projects />
  </section>
  <section>
    <h4 class="title is-4">Research interests</h4>
    Generative modelling, (causal) representation learning, semi-supervised learning,
    time series models, signal processing, numerical computing.
  </section>
  <section>
    <Research />
  </section>
  <section>
    <h4 class="title is-4">Currently reading</h4>
    <ul>
      <li>Erich Fromm, Fear of Freedom</li>
      <li>Erich Fromm, The Sane Society</li>
      <li>Hartmut Rosa, Resonance</li>
      <li>
        Francois Le Gall, Brownian Motion, Martingales, and Stochastic Calculus
      </li>
    </ul>
  </section>
</div>
