<template>
  <section class="section" style="margin-top: 1%" id="home">
    <div class="container">
      <div class="columns">
        <div class="column is-5">
          <h1>Consulting</h1>
        </div>
        <div class="column is-5" style="margin-top: 2%;">
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
  data: () => ({
    error: "",
    messages: []
  }),
  watch: {
    title: {
      immediate: true,
      handler() {
        document.title = "Home";
      }
    }
  }
};
</script>
