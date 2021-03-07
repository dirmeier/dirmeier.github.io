<template>
  <div class="container">
    <div class="columns">
      <div class="column is-8">
        <h3>Case studies and notebooks</h3>
        <p>
          Below you can find a collection of case studies and notebooks on
          machine learning, causal inference, and philosophy of science. The
          technical ones are mainly using the probabilistic programming
          languages Stan, TensorFlow Probability and PyMC3.
        </p>

        <div v-for="item in items" :key="item.date">
          <h4>{{ item.date }}</h4>
          <div class="columns" v-for="(entry, i) in item.posts" :key="i">
            <div class="column is-3">{{ entry.date }}</div>
            <div class="column is-9">
              <h6>{{ entry.title }}</h6>
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
    ]
  }),
  methods: {}
};
</script>
