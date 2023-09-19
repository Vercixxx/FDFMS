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
import axios from 'axios';


// Access token refreshing
function refreshAccessToken() {
    const refreshToken = store.getters.jwt.refreshToken;
    const accessToken = store.getters.jwt.accessToken;

    if (refreshToken && refreshToken !== 'null') {
        axios.post('/api/v1/jwt/refresh/', { refresh: refreshToken })
        .then((response) => {
            const newAccessToken = response.data.access;
            store.commit('setAccessToken', newAccessToken);
            axios.defaults.headers.common['Authorization'] = `JWT ${newAccessToken}`;

        })
        .catch((error) => {
            console.error(error);
            store.commit('resetState');
            router.push('/');
        });
    }
}

// interval
setInterval(refreshAccessToken, 58 * 60 * 1000);
// Access token refreshing

// import PortalVue from 'portal-vue'

// import { createPopper } from '@popperjs/core';


createApp(App).use(store).use(router).mount('#app')


