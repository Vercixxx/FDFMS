import axios from 'axios';
import store from '@/store'; 

// console.log(store.getters.jwt.accessToken)

// const accessToken = store.getters.jwt.accessToken;
// axios.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`;

axios.defaults.baseURL = 'http://127.0.0.1:8000/';
