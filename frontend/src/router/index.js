import { createRouter, createWebHistory } from 'vue-router'

// My imports
// import Login from '../components/Login.vue'
import { isAuthenticated } from '../auth-guard';

// hr
import { hrRoutes } from './hrRoutes'

// Views
import Login from '../views/LoginView.vue'
// import AssetView from '../views/AssetView.vue'
import Dashboard from '../views/ClientsViewEx.vue'
// import PayrollView from '../views/PayrollView.vue'
// import ManagerView from '../views/ManagerView.vue'
// import DriverView from '../views/DriverView.vue'
// import AdministratorView from '../views/AssetView.vue'



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


  // Driver
  // {
  //   path: '/driver',
  //   name: 'Driver',
  //   component: DriverView,
  //   beforeEnter: (to, from, next) => {
  //     if (!isAuthenticated()) {
  //       next('/')
  //     } else {
  //       next();
  //     }
  //   },
  // },

  // Administrator
  // {
  //   path: '/admin',
  //   name: 'Administrator',
  //   component: AdministratorView,
  //   beforeEnter: (to, from, next) => {
  //     if (!isAuthenticated()) {
  //       next('/')
  //     } else {
  //       next();
  //     }
  //   },
  // },
  ...hrRoutes,
]



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})


export default router
