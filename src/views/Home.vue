<template>
  <section class="section" style="margin-top: 10%" id="home">
    <div class="container">
      <div class="columns">
        <div class="column is-offset-3 is-6">
          <heads />
          <intro />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import heads from "../components/Head.vue";
import intro from "../components/Introduction.vue";

export default {
  components: {
    heads,
    intro
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
