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
          <button type="submit" name="" id="" class="btn btn-outline-danger shadow" @click="logoutConfirmFunc">
            <span class="d-flex align-items-center">

              Logout
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                class="bi bi-box-arrow-right ms-2" viewBox="0 0 16 16">
                <path fill-rule="evenodd"
                  d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0v2z" />
                <path fill-rule="evenodd"
                  d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z" />
              </svg>
            </span>
          </button>
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
                <button class="nav-link  btn btn-outline p-2 fs-5 border shadow " role="button" data-bs-toggle="dropdown"
                  aria-expanded="false">
                  <span class="d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                      class="bi bi-people me-2" viewBox="0 0 16 16">
                      <path
                        d="M15 14s1 0 1-1-1-4-5-4-5 3-5 4 1 1 1 1h8Zm-7.978-1A.261.261 0 0 1 7 12.996c.001-.264.167-1.03.76-1.72C8.312 10.629 9.282 10 11 10c1.717 0 2.687.63 3.24 1.276.593.69.758 1.457.76 1.72l-.008.002a.274.274 0 0 1-.014.002H7.022ZM11 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm3-2a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM6.936 9.28a5.88 5.88 0 0 0-1.23-.247A7.35 7.35 0 0 0 5 9c-4 0-5 3-5 4 0 .667.333 1 1 1h4.216A2.238 2.238 0 0 1 5 13c0-1.01.377-2.042 1.09-2.904.243-.294.526-.569.846-.816ZM4.92 10A5.493 5.493 0 0 0 4 13H1c0-.26.164-1.03.76-1.724.545-.636 1.492-1.256 3.16-1.275ZM1.5 5.5a3 3 0 1 1 6 0 3 3 0 0 1-6 0Zm3-2a2 2 0 1 0 0 4 2 2 0 0 0 0-4Z" />
                    </svg>
                    Users
                  </span>
                </button>
                <ul class="dropdown-menu shadow">
                  <li><a class="dropdown-item " @click="showAddUserComponent" role="button">
                      <span class="d-flex align-items-center">

                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                          class="bi bi-plus-square me-2" viewBox="0 0 16 16">
                          <path
                            d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z" />
                          <path
                            d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z" />
                        </svg>
                        Add user
                      </span>
                    </a></li>
                  <li><a class="dropdown-item" @click="showModifyUserComponent" role="button">
                      <span class="d-flex align-items-center">

                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                          class="bi bi-pencil  me-2" viewBox="0 0 16 16">
                          <path
                            d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z" />
                        </svg>
                        Modify user
                      </span>
                    </a></li>
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
          <div class="modal-header d-flex justify-content-between">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor"
                class="bi bi-exclamation-triangle" viewBox="0 0 16 16">
                <path
                  d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
                <path
                  d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
              </svg>
            <h1 class="modal-title fs-5" id="confirmLogoutLabel">
              
              Logout
            </h1>
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor"
              class="bi bi-exclamation-triangle" viewBox="0 0 16 16">
              <path
                d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
              <path
                d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
            </svg>
            
          </div>
          <div class="modal-body fs-5 text-center">
            <p>
              Are you sure?
            </p>
          </div>
          <div class="mb-4 d-flex justify-content-center">
            <button type="button" class="btn btn-secondary w-25 me-2 fs-4" data-bs-dismiss="modal">No</button>
            <button type="button" class="btn btn-danger w-25 fs-4" data-bs-dismiss="modal" @click="logout">Yes</button>
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
        const response = await axios.get('api/gu/', {
          params: {
            user_role: user_role,
          }
        });

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
        const response2 = await axios.delete('api/auth/', { token });
        this.$router.push('/');
        console.log(response2)
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
  