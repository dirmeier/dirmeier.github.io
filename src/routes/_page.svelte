<script>
    import logo from '$lib/profile.jpg';
    import Fa from "svelte-fa/src/fa.svelte"
    import { faEdit, faFlag } from "@fortawesome/free-solid-svg-icons"
</script>

<div>
    <div class="columns">
        <div class="column is-35">
            <img src={logo} width="150"/>

            <div style="font-size: 0.7em; margin-top: 1%">
                <a
                        href="mailto:simon.dirmeier @ protonmail com"
                        style="color: black; margin-right: 1%; font-size: 0.9em"
                >
                    <i class="fa fa-envelope fa-2x" />
                </a>
                <a href="https://linkedin.com/in/simon-dirmeier" style="color: black; margin-right: 1%">
                    <i class="fa fa-linkedin fa-2x" />
                </a>
                <a href="https://github.com/dirmeier" style="color: black; margin-right: 1%;">
                    <i class="fa fa-github fa-2x" />
                </a>
            </div>
        </div>
        <div class="column is-8">
            <div>
                <h6>Hello!</h6>
                <p><Fa icon={faFlag} />
                    I am Simon Currently, I am working as a senior data scientist at the
                    <a href="https://datascience.ch/">Swiss Data Science Center</a> in the academic cell. Apart from
                    that, I enjoy spending my time developing <a href="/code">open-source software</a> and writing
                    <a href="/case-studies">case studies</a>. I also occasionally offer
                    <a href="/consulting">ML/statistical consulting</a>.
                </p>
            </div>
        </div>
    </div>
    <div class="columns">
        <div class="row">
            <p>

                I've conducted my doctoral studies at
                <a href="https://ethz.ch/en.html">ETHZ</a> in Switzerland, where I developed statistical methods
                for the analysis of genetic interventional data. Before that, I have studied computer science
                and bioinformatics at <a href="https://www.tum.de/en/">TU</a>/<a
                    href="https://www.lmu.de/en/index.html">LMU</a>
                in Munich, Germany (and seven semesters of philosophy at LMU).
            </p>
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
            <p>
                I interact with computers mainly via Python, JavaScript and C++, but recently also have begun
                developing software in Clojure and Julia. For ML, my tech stack consists of Stan, NumPyro, and
                Deepmind's <a href="https://www.deepmind.com/blog/using-jax-to-accelerate-our-research"
            >JAX ecosystem</a
            > (e.g., JAX, Haiku, Distrax, Optax, ...). I am an advocate of open science, reproducible research
                and principled coding practices, and employ tools such as Docker and computational pipelines, like
                Snakemake, for robust data analysis. Other than that, I have some experience with high-performance
                and cloud computing, e.g., via OpenMP, GPGPU (CUDA) and Azure/Google Cloud.
            </p>
        </div>
    </div>
</div>
