<template>
  <section class="section" style="margin-top: 1%" id="home">
    <div class="container">
      <div class="columns">
        <div class="column is-offset-1 is-3">
          <h1>Consulting</h1>
        </div>
        <div class="column is-6" style="margin-top: 2%;">
          <consulting />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import consulting from "../components/Consulting.vue";

export default {
  components: {
    consulting
  },
  watch: {
    title: {
      immediate: true,
      handler() {
        document.title = "Consulting";
      }
    }
  }
};
</script>
