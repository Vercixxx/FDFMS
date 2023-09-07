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
          <button type="submit" name="" id="" class="btn btn-danger btn-lg shadow" @click="logoutConfirmFunc">Logout</button>
        </div>

      </div>
      <!-- Navbar -->
      <nav class="navbar navbar-expand-lg ">
        <div class="container-fluid">
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
    </div>


    <!-- Confirmation modal -->
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#confirmLogout"
      id="confirmLogoutButton" style="display: none;">
    </button>

    <!-- Modal -->
    <div class="modal fade" id="confirmLogout" tabindex="-1" aria-labelledby="confirmLogoutLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="confirmLogoutLabel">Confirm log-out</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body fs-5">
            <p>
              Are you sure you want to log out?
            </p>
          </div>
          <div class="modal-footer d-flex justify-content-center">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">No</button>
            <button type="button" class="btn btn-danger" data-bs-dismiss="modal" @click="logout">Yes</button>
          </div>
        </div>
      </div>
    </div>
    <!-- Confirmation modal -->



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
      confirmLogout: null,
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

    logoutConfirmFunc() {
      document.getElementById('confirmLogoutButton').click();
    },

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
  