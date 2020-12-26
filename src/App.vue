<template>
  <div>
    <navv />
    <router-view />
  </div>
</template>

<script>
import navv from "./views/Navbar.vue";

export default {
  components: {
    navv
  }
};
</script>

<style>
@import "./assets/css/bulma.min.css";
@import "./assets/css/style.css";
</style>
