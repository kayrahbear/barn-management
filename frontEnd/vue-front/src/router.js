import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      alias: "/horses",
      name: "horses",
      component: () => import("./components/HorseList")
    },
    {
      path: "/horses/:id",
      name: "horse-details",
      component: () => import("./components/Horse")
    },
    {
      path: "/addLesson",
      name: "addLesson",
      component: () => import("./components/AddLesson")
    }
  ]
});
