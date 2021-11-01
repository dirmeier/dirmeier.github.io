<template>
  <section class="section" style="margin-top: 1%" id="about">
    <div class="container">
      <div class="columns">
        <div class="column is-offset-1 is-3">
        </div>
        <div class="column is-6" style="margin-top: 2%;">
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
