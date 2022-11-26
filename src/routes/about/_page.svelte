<script>
    import logo from '$lib/profile.jpg';
    import Fa from "svelte-fa/src/fa.svelte"
    import {faEnvelope} from "@fortawesome/free-solid-svg-icons"
    import {faLinkedin} from "@fortawesome/free-brands-svg-icons"
</script>

<div>
    <div class="columns">
        <div class="column is-3" style="margin-top: 3%;">
            <img src={logo} width="150"/>
        </div>
        <div class="column is-8" style="margin-top: 3%;">
            <div>
                <h6 >Hello!</h6>
                <p>
                    I am Simon. Currently, I am working as a senior data scientist at the
                    <a href="https://datascience.ch/">Swiss Data Science Center</a> in the academic cell.
                </p>
                <p>
                    In my spare time, I enjoy spending developing <a href="/code">open-source software</a> and writing
                    <a href="/case-studies">case studies</a>. I also occasionally offer
                    <a href="/consulting">ML/statistical consulting</a>.
                </p>
                <p>
                    I've conducted my doctoral studies at
                    <a href="https://ethz.ch/en.html">ETHZ</a> in Switzerland, where I developed probabilistic methods
                    for the analysis of genetic interventional data. Before that, I have studied computer science
                    and bioinformatics at <a href="https://www.tum.de/en/">TU</a>/<a
                        href="https://www.lmu.de/en/index.html">LMU</a>
                    in Munich, Germany (and seven semesters of philosophy at LMU).
                </p>
            </div>
            <div>
                <p>
                    As a computer scientist turned applied statistician, I am particularly enthusiastic about
                    probabilistic programming which, as a discipline, lies at the interface of both fields.
                    Probabilistic programming languages (PPLs) use computer programs to represent probabilistic
                    models and are able to automatically infer quantities of interest (usually posterior
                    distributions) without users needing to manually implement samplers or optimizers. In that line
                    of research, I frequently contribute to modern PPLs, e.g., the frameworks
                    <a href="https://mc-stan.org/">Stan</a> or
                    <a href="https://num.pyro.ai/en/latest/index.html">NumPyro</a>, to learn more about
                    computational and mathematical nuances of methods. As a former researcher in computational
                    biology and wannabe-philosopher, I am keen on causal inference (CI) due to its relatedness to
                    philosophy of science, epistemology and scientific discovery, and since it mathematically
                    formalizes how (and if) cause-and-effect relationships can be established (CI concerns itself
                    with the discovery and inference of cause-and-effect relationships).
                </p>
                <p>I interact with computers mainly via Python, JavaScript and C++, but recently also have begun
                    developing software in Clojure and Julia. For ML, my tech stack currently consists of Stan, NumPyro, and
                    Deepmind's <a href="https://www.deepmind.com/blog/using-jax-to-accelerate-our-research"
                >JAX ecosystem</a
                > (e.g., JAX, Haiku, Distrax, Optax, ...). I am an advocate of open science, reproducible research
                    and principled coding practices, and employ tools such as Docker and computational pipelines, like
                    Snakemake, for robust data analysis. Other than that, I have some experience with high-performance
                    and cloud computing, e.g., via OpenMP, AVX, GPGPU (CUDA) and Azure/Google Cloud.
                </p>
            </div>
            <div>
                <p>You can reach me here: </p>
                <a href="mailto:simon.dirmeier @ protonmail com" style="color: black; margin-right: 1%;">
                    <Fa icon={faEnvelope} size="1.25x"/>
                </a>
                <a href="https://linkedin.com/in/simon-dirmeier" style="color: black; margin-left: 10px; margin-right: 10px">
                    <Fa icon={faLinkedin} size="1.25x"/>
                </a>
            </div>
        </div>

    </div>
</div>
