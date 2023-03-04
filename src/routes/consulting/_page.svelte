<script>
    import Fa from 'svelte-fa/src/fa.svelte';
    import {faEnvelope} from '@fortawesome/free-solid-svg-icons';
    import {faLinkedin} from '@fortawesome/free-brands-svg-icons';
</script>

<div>
    <div class="columns">
        <div class="column is-9">
            <div>
                <h3 style="font-size: 1.35em; margin-bottom: 5%">consulting in statistics and ai</h3>
                <div>
                    I am occasionally available for consulting on probabilistic modeling, causal inference, and
                    AI software development. In particular, I offer consulting on the following topics.
                </div>
                <div style="margin-bottom: 5%; margin-top: 5%">
                    <h5 style="font-weight: bold">Statistical and causal data analysis</h5>
                    I am an expert in statistical data analysis and causal inference, and can help you and your business
                    draw the right conclusions from data to improve decision making. I develop bespoke models using common probabilistic
                    programming languages(*) and can help set up a principled Bayesian workflow including model validation and model selection.
                    Since every insight drawn from data is only useful if communicated properly, I use web dashboards for
                    visualisation, e.g., using Shiny, Dash, Streamlit, or JavaScript frameworks like D3.<br/><br/>

                    (*) via, e.g, Stan, NumPyro or TensorFlow Probability (in Python, Julia or C++)
                </div>
                <div style="margin-bottom: 5%; margin-top: 5%">
                    <h5 style="font-weight: bold">Time-series forecasting</h5>
                    Time-series forecasting concerns itself with making predictions of the future from historical data and is crucial
                    in a wide variety of fields, such as finance, medicine or demand forecasting.
                    I have extensive theoretical and practical know-how in time-series forecasting using conventional tools, such as
                    exponential smoothing or ARIMA models, or modern approaches such as DeepAR, Prophet or using Gaussian processes, and can
                    help you implement a modern time-series forecasting application.
                </div>
                <div style="margin-bottom: 5%; margin-top: 5%">
                    <h5 style="font-weight: bold">Scientific computing</h5>
                    I have at least 10 years of experience in <b>scientific</b>, <b>high-performance</b> and <b>cloud</b> computing and
                    am knowledgeable in low-level programming languages such as C++ and frameworks such as GPGPU (CUDA), OpenMP
                    and <b>Azure/Google Cloud</b>. I can help you write low-level numerical code to speed up your applications, or
                    help you develop advanced mathematical algorithms.
                </div>
                <div style="margin-bottom: 5%; margin-top: 5%">
                    <p>
                        I interact with computers mainly via <b>Python</b>, <b>R</b>, <b>JavaScript</b> and <b>C++</b>, but recently also have
                        begun developing software in <b>Clojure</b> and <b>Julia</b>. For machine learning and AI, my <b>tech stack</b> currently consists
                        of <b>Stan</b>, <b>NumPyro</b>, and Deepmind's <a
                            href="https://www.deepmind.com/blog/using-jax-to-accelerate-our-research"
                    ><b>JAX ecosystem</b></a
                    > (e.g., JAX, Haiku, Distrax, Optax, ...). I am an advocate of open science, reproducible
                        research and principled coding practices, and employ tools such as <b>Docker</b> and computational
                        pipelines, like <b>Snakemake</b>, for robust data analysis.
                    </p>
                </div>
                <div>
                    <p>You can reach me here:</p>
                    <a href="mailto:simon.dirmeier @ protonmail com" style="color: black; margin-right: 1%;">
                        <Fa icon={faEnvelope} size="1.25x"/>
                    </a>
                    <a
                            href="https://linkedin.com/in/simon-dirmeier"
                            style="color: black; margin-left: 10px; margin-right: 10px"
                    >
                        <Fa icon={faLinkedin} size="1.25x"/>
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>
