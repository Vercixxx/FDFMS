import { createRouter, createWebHistory } from 'vue-router'

// My imports
import Login from '../components/Login.vue'
import HrView from '../views/HrView.vue'



const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/hr',
    name: 'HrView',
    component: HrView,
  },
]



const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


export default router
