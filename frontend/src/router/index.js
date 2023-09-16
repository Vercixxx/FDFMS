import { createRouter, createWebHistory } from 'vue-router'

// My imports
import Login from '../components/Login.vue'
import { isAuthenticated } from '../auth-guard';

// hr
import { hrRoutes } from './hrRoutes'

// Asset
import AssetView from '../views/AssetView.vue'



const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/asset',
    name: 'Asset',
    component: AssetView,
    beforeEnter: (to, from, next) => {
      if (!isAuthenticated()) {
        next('/')
      } else {
        next();
      }
    },
  },
  ...hrRoutes,
]



const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


export default router
