/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import { createRouter, createWebHistory } from 'vue-router/auto'
import { setupLayouts } from 'virtual:generated-layouts'
import { routes } from 'vue-router/auto-routes'
import Links from '@/pages/users/Links.vue'
import Dashboard from '@/layouts/Dashboard.vue'
import Users from '@/components/Users.vue'
import Products from '@/components/Products.vue'
import ProductForm from '@/components/ProductForm.vue'
import Orders from '@/components/Orders.vue'
import Profile from '@/components/Profile.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: Dashboard,
      children: [
        { path: '', redirect: '/users' },
        { path: '/users', component:  Users},
        { path: '/users/:id/links', component: Links},
        { path: '/profile', component: Profile },
        { path: '/orders', component: Orders },
        { path: '/products', component: Products },
        { path: '/products/create', component: ProductForm },
        { path: '/products/:id/edit', component: ProductForm },
      ]
    },
    ...setupLayouts(routes), 
  ]
})

// Workaround for https://github.com/vitejs/vite/issues/11804
router.onError((err, to) => {
  if (err?.message?.includes?.('Failed to fetch dynamically imported module')) {
    if (!localStorage.getItem('vuetify:dynamic-reload')) {
      console.log('Reloading page to fix dynamic import error')
      localStorage.setItem('vuetify:dynamic-reload', 'true')
      location.assign(to.fullPath)
    } else {
      console.error('Dynamic import error, reloading page did not fix it', err)
    }
  } else {
    console.error(err)
  }
})

router.isReady().then(() => {
  localStorage.removeItem('vuetify:dynamic-reload')
})

export default router
