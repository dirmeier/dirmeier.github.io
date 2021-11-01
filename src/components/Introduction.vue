<template>
  <div>
    <p>
      Hello and welcome. I am Simon, a freelance machine learning scientist
      based in Switzerland. Currently, I spend most of my time developing
      open-source software and doing research, in particular on probabilistic
      machine/deep learning, causal inference and probabilistic programming.
      Along the same lines, I also write
      <a href="/case-studies">case studies</a> and occasionally offer
      <a href="/consulting">statistical consulting</a>.
    </p>
    <div>
      <div align="right">
        <button
          class="button is-light"
          style="font-size: 0.9rem; padding: 0px;  margin-top: -20px"
          v-on:click="button_is_pressed = ! button_is_pressed"
        >
          <span class="icon is-small">
            <font-awesome-icon :icon="['fas', 'book-open']" />
          </span>
          <span>
            {{ button_is_pressed ? "Hide" : "Read more" }}
          </span>
        </button>
      </div>
      <p v-if="button_is_pressed">
        My expertise and scientific interests lie broadly in probabilistic machine
        and deep learning, (nonparametric) Bayesian statistics and causal
        inference.<br />

        I am particularly enthusiastic about <i>probablistic programming</i> which
        are probabilistic I offer statistical consulting for probabilistic
        modeling
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    button_is_pressed: false
  }),
  methods: {}
};
</script>
