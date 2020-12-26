<template>
  <section class="section" style="margin-top: 1%" id="home">
    <books />
    <bot />
  </section>
</template>

<script>
import books from "../components/Books.vue";
import bot from "../components/Bottom.vue";

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
