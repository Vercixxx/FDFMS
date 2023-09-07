import axios from 'axios';
import Cookies from 'js-cookie';

const token = Cookies.get('token');

axios.defaults.baseURL = 'http://127.0.0.1:8000/';
axios.defaults.headers.common['Authorization'] = `Token ${token}`;
