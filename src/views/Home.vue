<template>
  <section class="section" style="margin-top: 1%" id="home">
    <abt />
    <blog />
    <pubs />
    <contact />
    <bot />
  </section>
</template>

<script>
import abt from "../components/About.vue";
import blog from "../components/Not-a-blog.vue";
import pubs from "../components/Publications.vue";
import contact from "../components/Contact.vue";
import bot from "../components/Bottom.vue";

export default {
  components: {
    abt,
    blog,
    contact,
    pubs,
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
        document.title = "Home";
      }
    }
  }
};
</script>
