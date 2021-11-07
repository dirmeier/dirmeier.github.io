<template>
  <section class="section">
    <div class="container">
      <div class="columns">
        <div class="column is-offset-4 is-6">
          <studies />
          <bottom />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import studies from "../components/Studies.vue";
import bottom from "../components/Bottom.vue";

export default {
  components: {
    studies,
    bottom
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
