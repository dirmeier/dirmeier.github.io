<template>
  <div>
    <navv />
    <home />
  </div>
</template>

<script>
import navv from "./views/Navbar.vue";
import home from "./views/Home.vue";

export default {
  components: {
    navv,
    home
  }
};
</script>

<style>
@import "./assets/css/bulma.min.css";
@import "./assets/css/style.css";
</style>
