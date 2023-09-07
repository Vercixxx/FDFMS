import { createRouter, createWebHistory } from 'vue-router'

// My imports
import Login from '../components/Login.vue'

// hr
import { hrRoutes } from './hrRoutes'



const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  ...hrRoutes,
]



const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


export default router
