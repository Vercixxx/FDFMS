// My packages
import 'jquery';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap';

import './axios'
// My packages


import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'


// import { createPopper } from '@popperjs/core';
// import PortalVue from 'portal-vue'

createApp(App).use(store).use(router).mount('#app')
