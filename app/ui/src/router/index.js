import { createRouter, createWebHistory } from "vue-router";

import HomeView from "@/views/HomeView.vue";
import FindView from "@/views/FindView.vue";

const routes = [
    {
        path: "/",
        name: 'home',
        component: HomeView
    },
    {
        path: "/find",
        name: 'find',
        component: FindView
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;