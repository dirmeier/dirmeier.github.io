<template>
  <div class="container">
    <div class="columns">
      <div class="column is-8">
        <h3>Case studies and notebooks</h3>
        <p>
          Below you can find a collection of case studies and notebooks on
          probabilistic machine learning, causal inference and Bayesian statistics. The choice of topics
          is fairly random, but usually is related to an interesting paper I have read, a tool I discovered, or a problem I needed to solve.
          The notebooks mainly use Stan (from R) and TensorFlow Probability (from R and Python) for probabilistic inference,
          but I recently started to work more with Jax, Haiku and NumPyro.
        </p>

        <div v-for="item in items" :key="item.date">
          <h4>{{ item.date }}</h4>
          <div class="columns" v-for="(entry, i) in item.posts" :key="i">
            <div class="column is-3">{{ entry.date }}</div>
            <div class="column is-9">
              <h6>{{ entry.title }}
              <img v-if="entry.language" :src="getLogo(entry.language)" width="20" height="20" >
              </h6>
              {{ entry.description }}
              (<span v-for="(link, j) of entry.links" :key="link.name">
                <a :href="link.link" style="display: inline">{{ link.name }}</a>
                <span v-if="j + 1 < entry.links.length">, </span> </span
              >).
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import blog_2021 from "../assets/2021-blogentries.json";
import blog_2020 from "../assets/2020-blogentries.json";
import blog_2019 from "../assets/2019-blogentries.json";
import blog_2018 from "../assets/2018-blogentries.json";
export default {
  data: () => ({
    error: "",
    items: [
      { date: "2021", posts: blog_2021 },
      { date: "2020", posts: blog_2020 },
      { date: "2019", posts: blog_2019 },
      { date: "2018", posts: blog_2018 }
    ],
    getLogo(language) {
         return require('../assets/logos/' + language + '_logo.svg');
    }
  }),
  methods: {}
};
</script>
