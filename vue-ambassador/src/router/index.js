import { createRouter, createWebHistory } from "vue-router";
import Layout from '../layouts/Layout.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Profile from "../views/Profile.vue";
import ProductsFrontend from "../views/ProductsFrontend.vue";
import Backend from "../views/Backend.vue";
import Stats from "../views/Stats.vue";
import Rankings from "../views/Rankings.vue";

const routes = [
   { path: '/login', component: Login, },
   { path: '/register', component: Register, },
   {
         path: '',
         component: Layout,
         children: [
            { path: '', component: ProductsFrontend, },
            { path: '/profile', component: Profile, },
            { path: '/backend', component: Backend },
            { path: '/rankings', component: Rankings },
            { path: '/stats', component: Stats },
         ]
   },
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})

export default router