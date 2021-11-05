<template>
  <section class="section">
    <div class="container">
      <div class="columns">
        <div class="column is-offset-4 is-6">
          <about />
          <consulting />
          <bottom />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import about from "../components/About.vue";
import consulting from "../components/Consulting.vue";
import bottom from "../components/Bottom.vue";

export default {
  components: {
    about,
    consulting,
    bottom
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
