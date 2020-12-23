<template>
  <section class="section" style="margin-top: 1%" id="home">
    <blog />
    <bot />
  </section>
</template>

<script>
import abt from "../components/Books.vue";
import bot from "../components/Bottom";

export default {
  components: {
    books,
    bot
  },
  data: () => ({
    error: "",
    messages: []
  }),
  watch: {
    title: {
      immediate: true,
      handler() {
        document.title = "Books";
      }
    }
  }
};
</script>
