import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/user/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // auth links
    {
      path: '/in',
      name: 'auth',
      component: () => import('../views/AuthView.vue'),
    },
    // admin links
    {
      path: '/admin',
      name: 'adminhome',
      component: () => import('../views/admin/HomeView.vue'),
      meta: {
        onlyAdmin: 'true',
      },
    },
    {
      path: '/admin/quotes',
      name: 'adminquotes',
      component: () => import('../views/admin/QuotesView.vue'),
      meta: {
        onlyAdmin: 'true',
      },
    },
    {
      path: '/admin/quotes/:id',
      name: 'adminquote',
      component: () => import('../views/admin/QuoteView.vue'),
      meta: {
        onlyAdmin: 'true',
      },
    },
    // user links
    {
      path: '/', // user dashboard
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
    }
  ],
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('token') !== null
  if (to.name === 'auth' && isAuthenticated) { 
    alert('You are already logged in')
    next({ name: 'home' })
  } else if (to.name !== 'auth' && !isAuthenticated) {
    alert('You are not authenticated to access this page')
    next({ name: 'auth' })
  } else { // logged in and trying to access a page
    const user = JSON.parse(localStorage.getItem('user'))
    const isAdmin = user?.role === 'admin';
    if (to.meta.onlyAdmin && !isAdmin) {
      alert('You are not authorized to access this page')
      next({ name: 'home' })
    } else { // trying to access a admin page
      next()
    }
  }
});

export default router
