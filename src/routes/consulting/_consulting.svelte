<script>
    import Fa from "svelte-fa/src/fa.svelte"
    import {faEnvelope} from "@fortawesome/free-solid-svg-icons"
</script>


<div>
    <div class="columns">
        <div class="column is-10">
            <div id="consulting">
                <div>
                    I am occasionally available for statistical consulting on probabilistic modeling, causal
                    inference, and research software development. In particular, I offer consulting on
                    <ul>
                        <li>
                            statistical/causal data analysis, e.g., of biomedical, financial, or
                            astrophysical data sets
                        </li>
                        <li>development of web dashboards for visualization</li>
                        <li>implementation of bespoke probabilistic models using PPLs (*)</li>
                        <li>Bayesian workflow, model validation, model selection, etc.</li>
                        <li>
                            implementation of computational pipelines (e.g., of analysis workflows for
                            reproducible research)
                        </li>
                    </ul>
                    (*) via, e.g, Stan, NumPyro or TensorFlow Probability (in Python, Julia, C++ or R)<br/>
                    To find a sketch of topics that I have expertise with, please have a look at my
                    <a href="/case-studies">case studies</a>.
                </div>
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
                <div>
                    <p>You can reach me here: </p>
                    <a href="mailto:simon.dirmeier @ protonmail com" style="color: black; margin-right: 1%;">
                        <Fa icon={faEnvelope} size="1.25x"/>
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>