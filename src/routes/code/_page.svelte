<script>
    import logo from '$lib/profile.jpg';
    import Fa from "svelte-fa/src/fa.svelte"

    function getLogo(language) {
        return '/logos/' + language + '_logo.svg';
    }
</script>

<div>
    <div class="columns">
        <div class="column is-9">
            <div>
                <h3 style="font-size: 1.35em; margin-bottom: 5%">a selection of packages I developed</h3>
                <ul style="list-style: none;">
                    <li style="padding-bottom: 0; list-style: none">
                        <p><img src={getLogo("Python")} width="15" height="15"/>
                            <a href="https://github.com/dirmeier/reconcile"> <span
                                    style="font-family: monospace">reconcile</span></a>
                            is another Python package for probabilistic reconciliation of time series forecasts.
                        </p>
                    </li>
                    <li style="padding-bottom: 0; list-style: none">
                        <p><img src={getLogo("Python")} width="15" height="15"/> <a
                                href="https://ramsey.readthedocs.io/en/latest/"> <span
                                style="font-family: monospace">Ramsey</span></a>
                            is a Python package for probabilistic modelling using JAX and Haiku. It implements recent
                            developments in probabilistic machine and deep learning and among other things aims to bring
                            these methods to a larger audience.
                        </p>
                    </li>
                    <li style="padding-bottom: 0; list-style: none">
                        <p><img src={getLogo("Clojure")} width="15" height="15"/> <a
                                href="https://github.com/dirmeier/clad"> <span
                                style="font-family: monospace">clad</span></a>
                            is a proof-of-concept reverse-mode automatic differentiation package written in Clojure.
                        </p>
                    </li>
                    <li style="padding-bottom: 0; list-style: none">
                        <p><img src={getLogo("Python")} width="15" height="15"/> <a
                                href="https://github.com/cbg-ethz/shm"> <span
                                style="font-family: monospace">shm</span></a>
                            is a Python package for probabilistic inference in
                            <it>structured hierarchical models</it>
                            ,
                            a class of models introduced in <i>Dirmeier and Beerenwinkel., 2022</i>
                            (<a href="https://www.doi.org/10.1214/21-AOAS1580">doi:10.1214/21-AOAS1580</a>).
                        </p>
                    </li>
                    <li style="padding-bottom: 0; list-style: none">
                        <p><img src={getLogo("c++")} width="15" height="15"/> <a
                                href="https://github.com/dirmeier/R--"> <span
                                style="font-family: monospace">R--</span></a>
                            is an interpreter for the R language written in C++.
                        </p>
                    </li>
                    <li style="padding-bottom: 0; list-style: none">
                        <p><img src={getLogo("R")} width="15" height="15"/> <a
                                href="https://github.com/dirmeier/netReg"> <span
                                style="font-family: monospace">netReg</span></a>
                            implements network-regularized regression models in R/C++.
                        </p>
                    </li>
                    <li style="padding-bottom: 0; list-style: none">
                        <p><img src={getLogo("CUDA")} width="15" height="15"/> <a
                                href="https://github.com/dirmeier/cuda-etudes"> <span
                                style="font-family: monospace">cuda-etudes</span></a>
                            is a selection of numerical CUDA recipes.
                        </p>
                    </li>
                    <li style="padding-bottom: 0; list-style: none">
                        <p><img src={getLogo("JavaScript")} width="15" height="15"/> <a
                                href="https://github.com/dirmeier/cluedo"> <span
                                style="font-family: monospace">cluedo</span></a>
                            implements the well known board game in JavaScript.
                            This version plays in ancient Greece where Socrates, a true champion of the open society,
                            has been murdered by one of his enemies.
                        </p>
                    </li>

                    <li style="padding-bottom: 0; list-style: none">
                        <p><img src={getLogo("Python")} width="15" height="15"/> <a
                                href="https://github.com/dirmeier/pybda"> <span
                                style="font-family: monospace">pybda</span></a> is a Python library and command line
                            tool for big data analytics and machine learning scaling to tera byte sized data sets.
                        </p>
                    </li>
                </ul>
            </div>
            <div>
                <h3 style="font-size: 1.35em; margin-top: 10%; margin-bottom: 5%">
                    a selection of packages I like contribute code to and/or co-develop</h3>
                <ul>
                    <li style="padding-bottom: 0; list-style: none">
                        <p><img src={getLogo("c++")} width="15" height="15"/>
                            <a href="https://mc-stan.org/n"> <span
                                    style="font-family: monospace">Stan</span></a>
                            is a state-of-the-art probabilistic programming langauge for Bayesian modeling and
                            high-performance statistical computation.
                        </p>
                    </li>
                    <li style="padding-bottom: 0; list-style: none">
                        <p><img src={getLogo("Python")} width="15" height="15"/> <a
                                href="https://num.pyro.ai/en/stable/"> <span
                                style="font-family: monospace">NumPyro</span></a>
                            is a lightweight probabilistic programming library that provides a
                            NumPy backend for Pyro. It relies on JAX for automatic differentiation
                            and JIT compilation to CPU/GPU/TPU.
                        </p>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</div>
