<template>
  <section class="section" style="margin-top: 1%" id="home">
    <div class="container" >
      <div class="columns">
        <div class="column is-5">
          <heads />
        </div>
        <div class="column is-5" style="margin-top: 1%">
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
