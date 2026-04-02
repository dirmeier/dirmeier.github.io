<script>
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
    <h4 class="title is-4">Code</h4>
    You can find my software on
    <a href="https://github.com/dirmeier">GitHub</a>
    .
  </section>
  <section>
    <h4 class="title is-4">Research interests (in no particular order)</h4>
    Before Logitech, where I work on deep learning and signal processing, I was mainly
    interested in:
    <ul>
      <li>Causal inference</li>
      <li>
        Applied probability (probabilistic modelling, stochastic processes, ...)
      </li>
      <li>
        Approximate and Bayesian inference (Markov Chain Monte Carlo, VI,
        Simulation-Based Inference)
      </li>
      <li>Probabilistic programming</li>
      <li>Generative modelling (score and flow matching, normalizing flows)</li>
    </ul>
  </section>
  <section>
    <h4 class="title is-4">Recent work</h4>
    <div class="columns">
      <div class="column is-9">
        <ul>
          <li>
            <b>Causal posterior estimation</b>
            (
            <a href="https://arxiv.org/abs/2505.21468">arXiv:2505.21468</a>
            ): a new method for simulation-based inference that exploits the
            conditional independence structure of the posterior programs and
            encodes it into a new NN architecture.
            <br />
            <i>
              Keywords: simulation-based inference, flow matching, causality
            </i>
          </li>
          <li>
            <b>Simulated-Annealing ABC with multiple summary statistics</b>
            (
            <a href="https://arxiv.org/abs/2505.23261">arXiv:2505.23261</a>
            ): we propose a novel ABC method that works well on high-dimensional
            parameter and data spaces using Simulated Annealing.
            <br />
            <i>Keywords: ABC, MCMC</i>
          </li>
          <li>
            <b>Simulation-based Inference with the Python Package sbijax</b>
            (
            <a href="https://arxiv.org/abs/2409.19435">arXiv:2409.19435</a>
            ): a Python package implementing simulation-based inference and ABC
            methods in JAX.
            <br />
            <i>Keywords: simulation-based inference, ABC, Python, JAX</i>
          </li>
          <li>
            <b>
              High resolution seismic waveform generation using denoising
              diffusion
            </b>
            (
            <a href="https://arxiv.org/abs/2410.19343">arXiv:2410.19343</a>
            ): a bespoke diffusion model trained from scratch on real
            earthquakes to synthesize realistic, high-frequency seismic
            waveforms.
            <br />
            <i>
              Keywords: denoising diffusion, score matching, signal processing
            </i>
          </li>
        </ul>
      </div>
    </div>
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
