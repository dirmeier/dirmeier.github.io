<template>
  <section class="section">
    <div class="container">
      <div class="columns">
        <div class="column is-offset-4 is-6">
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
