<template>
  <section class="section" style="margin-top: 1%" id="home">
    <div class="container">
      <div class="columns">
        <div class="column is-offset-1 is-3">
          <h1>Case studies</h1>
        </div>
        <div class="column is-6" style="margin-top: 2%;">
          <studies />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import studies from "../components/Studies.vue";

export default {
  components: {
    studies
  },  
  watch: {
    title: {
      immediate: true,
      handler() {
        document.title = "Case studies";
      }
    }
  }
};
</script>
