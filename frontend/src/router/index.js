import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/in',
      name: 'auth',
      component: () => import('../views/AuthView.vue'),
    }
  ],
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('token') !== null
  if (to.name === 'auth' && isAuthenticated) {
    next({ name: 'home' })
  } else if (to.name !== 'auth' && !isAuthenticated) {
    next({ name: 'auth' })
  } else {
    next()
  }
});

export default router
