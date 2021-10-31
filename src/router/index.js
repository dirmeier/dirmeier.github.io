import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Books from "../views/Books.vue";
import Consulting from "../views/Consulting.vue";
import Studies from "../views/Studies.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/consulting",
    name: "Consulting",
    component: Consulting
  },
  {
    path: "/case-studies",
    name: "Case studies",
    component: Studies
  },
  {
    path: "/books",
    name: "Books",
    component: Books
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
