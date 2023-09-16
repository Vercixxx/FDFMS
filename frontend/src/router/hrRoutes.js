import HrView from '../views/HrView.vue'
import { isAuthenticated } from '../auth-guard';

export const hrRoutes = [
  {
    path: '/hr',
    name: 'HrView',
    component: HrView,
    beforeEnter: (to, from, next) => {
      if (!isAuthenticated()) {
        next('/')
      } else {
        next();
      }
    },
  },
]
