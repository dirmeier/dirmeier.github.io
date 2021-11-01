<template>
  <section class="section" style="margin-top: 1%" id="home">
    <div class="container">
      <div class="columns">
        <div class="column is-offset-1 is-3">
          <h1>About</h1>
        </div>
        <div class="column is-6" style="margin-top: 2%;">
          <about />
          <publications />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import about from "../components/About.vue";
import publications from "../components/Research.vue";

export default {
  components: {
    about,
    publications
  },
  watch: {
    title: {
      immediate: true,
      handler() {
        document.title = "About";
      }
    }
  }
};
</script>
