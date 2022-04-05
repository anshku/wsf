import { createRouter, createWebHistory } from "vue-router";
import Players from "../views/Players.vue";
import EditMargin from "../views/EditMargin.vue";

const routes = [
  {
    path: "/",
    name: "Players",
    component: Players,
  },
  {
    path: "/player/:id",
    name: "EditMargin",
    component: EditMargin,
    props: true,
  },
];
const router = createRouter({
  routes,
  history: createWebHistory(process.env.BASE_URL),
});

export default router;
