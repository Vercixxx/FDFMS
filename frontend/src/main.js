// My packages
import 'jquery';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap';

import './axios'
// My packages


import { createApp, reactive, watch } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios';



// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import colors from 'vuetify/lib/util/colors'
import '@mdi/font/css/materialdesignicons.css'




const vuetify = createVuetify({
    components,
    directives,

    theme: {
        defaultTheme: 'dark',

    },
    
  })

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


const app = createApp(App);

app.use(store);
app.use(router);
app.use(vuetify);

app.mount('#app');

// Watch for color palette changes
const vuetifyTheme = reactive(vuetify.theme.current);
watch(() => vuetifyTheme.value.dark, (isDark) => {
    store.commit('setColorPalette', isDark);
  }, { immediate: true });

// Preventing page reload
window.addEventListener('beforeunload', (event) => {
  event.preventDefault();
  event.returnValue = '';
});



