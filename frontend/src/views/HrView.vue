<template>
  <div class="HRView">
    <div class="containter rounded-3 p-1 m-2 " style="--bs-bg-opacity: .5; background-image: var(--bs-gradient);">
      <div class="d-flex justify-content-between">

        <div class="p-2">

          <!-- Title -->
          <p class="fs-2 fst-italic mb-4 px-2">FDFMS - HR Management console</p>

        </div>
        <div class="p-2">

          <button type="submit" name="" id="" class="btn btn-danger btn-lg shadow" @click="logout" >Logout</button>
          <p class="fs-3 mb-1 px-2">Hi, {{ userData.username }}</p>
        </div>

      </div>

    </div>


    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg bg-body-secondary mx-2 rounded border border-success-subtle">
      <div class="container-fluid">
        <a class="navbar-brand fs-3" href="#">Menu</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
          aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <!-- Option 1 -->
            <li class="nav-item dropdown">
              <button class="nav-link dropdown-toggle btn btn-outline-secondary p-2 fs-5" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Users
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Add user</a></li>
                <li><a class="dropdown-item" href="#">Modify user</a></li>
                <li><a class="dropdown-item" href="#">Remove user</a></li>
              </ul>
            </li>
            <!-- Option 1 -->
          </ul>
        </div>
      </div>
    </nav>
    <!-- Navbar -->



    <button type="submit" name="" id="" class="btn btn-primary m-5 position-fixed start-0 bottom-0" @click="fetchTokenData">check token</button>


  </div>
</template>
  
<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  name: "HRView",

  data() {
    return {
      userData: {}, // Inicjalizuj pustym obiektem
    };
  },

  async created() {
    const token = Cookies.get('token');

    if (!token) {
      this.$router.push('/');

    } else {
      const user_model = localStorage.getItem('user_model')
      const response = await axios.post('user/', { 'user_model': user_model });
      this.userData = response.data;

      if (response.data.user_role != 'HR') {
        await axios.post('log-out/', { token });
        Cookies.remove('token')
        this.$router.push('/');
  
      }
    }



  },

  methods: {
    async logout() {

      const token = Cookies.get('token');

      if (token) {
        Cookies.remove('token');
        const response2 = await axios.post('log-out/', { token });
        this.$router.push('/');
      }
      else {
        console.warn('Brak tokena użytkownika w localStorage.');
      }

    },

    async fetchTokenData() {
      const token = Cookies.get('token');
      try {
        const response = await axios.get('get-token/');

        console.log('Username:', response.data.passed_for);

      } catch (error) {

        console.error('Error:', error);
      }
    },


  },

  components: {},
};
</script>
  