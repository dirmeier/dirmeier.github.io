<script>
	import logo from '$lib/profile.jpg';
	import Fa from 'svelte-fa/src/fa.svelte';
	import { faEnvelope } from '@fortawesome/free-solid-svg-icons';
	import { faLinkedin, faGithub } from '@fortawesome/free-brands-svg-icons';
</script>

<div>
	<div class="columns">
		<div class="column is-3" style="margin-top: 3%;">
			<img src={logo} width="150" />
		</div>

		<div class="column is-9" style="margin-top: 3%;">
			<div>
				<h6>Hello!</h6>
				<p>
					I am Simon. Currently, I am working as a senior data scientist at the
					<a href="https://datascience.ch/">Swiss Data Science Center</a> in the academic cell.
				</p>
				<p>
					In my spare time, I enjoy developing <a href="/code">open-source software</a> and
					writing <a href="/case-studies">case studies</a>. I also occasionally offer
					consulting in statistics and ML, in particular on causal inference.
				</p>
				<p>
					I've conducted my doctoral studies at
					<a href="https://ethz.ch/en.html">ETHZ</a> in Switzerland, where I developed probabilistic
					methods for the analysis of genetic interventional data. Before that, I have studied
					computer science and bioinformatics at <a href="https://www.tum.de/en/">TU</a>/<a
						href="https://www.lmu.de/en/index.html">LMU</a
					> in Munich, Germany (and seven semesters of philosophy at LMU).
				</p>
				<p>My research interests revolve mainly around causal inference,
					generative and probabilistic modelling,
					Bayesian inference, and probabilistic programming languages.
				</p>
				<p>
					As a computer scientist turned applied statistician, I am particularly enthusiastic about
					probabilistic programming which, as a discipline, lies at the interface of both fields.
					Probabilistic programming languages (PPLs) use computer programs to represent
					probabilistic models and are able to automatically infer quantities of interest (usually
					posterior distributions) without users needing to manually implement specific samplers or
					optimizers. In that line of research, I frequently contribute to modern PPLs, e.g., the
					frameworks
					<a href="https://mc-stan.org/">Stan</a> or
					<a href="https://num.pyro.ai/en/latest/index.html">NumPyro</a>.
				</p>
				<p>
					As a former researcher in computational
					biology and wannabe-philosopher, I am keen on causal inference (CI) due to its relatedness
					to philosophy of science, epistemology and scientific discovery, and since it
					mathematically formalizes how (and if) cause-and-effect relationships can be established
					(CI concerns itself with the discovery and inference of cause-and-effect relationships).
				</p>
			</div>
			<div>
				<b>You can reach me here: </b>
				<a
						href="mailto:simon.dirmeier @ protonmail com"
						style="color: black; margin-left: 10px;"
					>
					<Fa icon={faEnvelope} size="1.3x" />
				</a>
				<a
						href="https://linkedin.com/in/simon-dirmeier"
						style="color: black; margin-left: 10px; margin-right: 10px"
				>
					<Fa icon={faLinkedin} size="1.3x"/>
				</a>
				<a
						href="https://github.com/dirmeier"
						style="color: black;"
				>
					<Fa icon={faGithub} size="1.3x" />
				</a>
			</div>
		</div>
	</div>
</div>
