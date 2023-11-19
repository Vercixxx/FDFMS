import { createRouter, createWebHistory } from 'vue-router'

// My imports
import { isAuthenticated } from '../auth-guard';

// Views
import Login from '../views/LoginView.vue'
import Dashboard from '../views/MainPage.vue'




const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },

  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    beforeEnter: (to, from, next) => {
      if (!isAuthenticated()) {
        next('/')
      } else {
        next();
      }
    },
  },

]



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})


export default router
