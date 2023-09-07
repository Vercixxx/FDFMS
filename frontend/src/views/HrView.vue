<template>
  <div class="HRView">
    <div class="containter rounded-3 p-1 m-2 " style="--bs-bg-opacity: .5; background-image: var(--bs-gradient);">
      <div class="d-flex justify-content-between">

        <div class="p-2">

          <!-- Title -->
          <p class="fs-2 fst-italic mb-4 px-2">FDFMS - HR Management console</p>

        </div>
        <div class="p-2 text-end">

          <p class="fs-3 mb-1 px-2">Hi, {{ userData.username }}</p>
          <button type="submit" name="" id="" class="btn btn-danger btn-lg shadow" @click="logout">Logout</button>
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
              <button class="nav-link dropdown-toggle btn btn-outline-secondary p-2 fs-5" href="#" role="button"
                data-bs-toggle="dropdown" aria-expanded="false">
                Users
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" @click="showAddUserComponent">Add user</a></li>
                <li><a class="dropdown-item" @click="showModifyUserComponent">Modify user</a></li>
                <!-- <li><a class="dropdown-item" @click="showRemoveUserComponent">Remove user</a></li> -->
              </ul>
            </li>
            <!-- Option 1 -->
          </ul>
        </div>
      </div>
    </nav>
    <!-- Navbar -->



    <button type="submit" name="" id="" class="btn btn-primary m-5 position-fixed start-0 bottom-0"
      @click="fetchTokenData">check token</button>


    <!-- content -->
    <div class="cointainter m-2 p-2">
      <component :is="currentComponent"></component>
    </div>
    <!-- content -->





  </div>
</template>
  
<script>
import axios from 'axios';
import Cookies from 'js-cookie';

// components
import AddUser from '../components/hr/AddUser';

// add users components
import HrUser from '../components/hr/users/AddHr';
import PayrollUser from '../components/hr/users/AddPayroll';
import AssetUser from '../components/hr/users/AddAsset';
import ClientUser from '../components/hr/users/AddClient';
import ManagerUser from '../components/hr/users/AddManager';
import DriverUser from '../components/hr/users/AddDriver';

import ModifyUser from '../components/hr/ModifyUser';
import RemoveUser from '../components/hr/RemoveUser';


export default {
  name: "HRView",

  data() {
    return {
      userData: {},
      currentComponent: null,
    };
  },

  async created() {
    const token = Cookies.get('token');

    if (!token) {
      this.$router.push('/');

    } 
    else {
      const user_role = localStorage.getItem('user_role')
      if (user_role != 'HR') {
        this.logout()
      }
      else {
        const response = await axios.post('user/', { 'user_role': user_role });
        this.userData = response.data;
        console.log(user_role)
        console.log(response.data)
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
        console.warn('Missing token');
      }

    },

    async fetchTokenData() {
      const token = Cookies.get('token');
      try {
        const response = await axios.get('get-token/');

        console.log('Username:', response.data.passed_for);

      } 
      catch (error) {

        console.error('Error:', error);
      }
    },

    showAddUserComponent() {
      this.currentComponent = AddUser;
    },
    showAddHrComponent() {
      this.currentComponent = HrUser;
    },
    showAddPayrollComponent() {
      this.currentComponent = PayrollUser;
    },
    showAddAssetComponent() {
      this.currentComponent = AssetUser;
    },
    showAddClientComponent() {
      this.currentComponent = ClientUser;
    },
    showAddManagerComponent() {
      this.currentComponent = ManagerUser;
    },
    showAddDriverComponent() {
      this.currentComponent = DriverUser;
    },
    showModifyUserComponent() {
      this.currentComponent = ModifyUser;
    },
    showRemoveUserComponent() {
      this.currentComponent = RemoveUser;
    },
  },

  components: {},
};
</script>
  