<template>
  <div>

    <p class="p-2 fw-bolder fs-5">Filters</p>
    <!-- Search bar section -->
    <div class="text-center mb-5 d-flex justify-content-between">

      <div class="p-2">
        <div class="btn-group dropdown mx-2">
          <span class="input-group-text rounded-0 rounded-start" id="basic-addon1">User role</span>

          <button type="button" class="btn btn-outline-secondary dropdown-toggle" data-bs-toggle="dropdown"
            aria-expanded="false">
            {{ selectedRole }}
          </button>
          <ul class="dropdown-menu">
            <li @click="selectedRole = 'All'; loadUsers();"><a class="dropdown-item fw-bolder ">All</a></li>
            <li @click="selectedRole = 'HR'; loadUsers();"><a class="dropdown-item ">HR</a></li>
            <li @click="selectedRole = 'Asset'; loadUsers();"><a class="dropdown-item ">Asset</a></li>
            <li @click="selectedRole = 'Payroll'; loadUsers();"><a class="dropdown-item ">Payroll</a></li>
            <li @click="selectedRole = 'Client'; loadUsers();"><a class="dropdown-item ">Client</a></li>
            <li @click="selectedRole = 'Manager'; loadUsers();"><a class="dropdown-item ">Manager</a></li>
            <li @click="selectedRole = 'Driver'; loadUsers();"><a class="dropdown-item ">Driver</a></li>
          </ul>
        </div>



        <div class="btn-group dropdown">
          <span class="input-group-text rounded-0 rounded-start" id="basic-addon1">User status</span>

          <button type="button" class="btn btn-outline-secondary dropdown-toggle" data-bs-toggle="dropdown"
            aria-expanded="false">

            <span v-if="selectedActive === 'True'">Yes</span>
            <span v-else-if="selectedActive === 'False'">No</span>
            <span v-else>All</span>
          </button>
          <ul class="dropdown-menu">
            <li @click="selectedActive = 'All'; loadUsers();"><a class="dropdown-item fw-bolder ">All</a></li>
            <li @click="selectedActive = 'True'; loadUsers();"><a class="dropdown-item ">Active</a></li>
            <li @click="selectedActive = 'False'; loadUsers();"><a class="dropdown-item ">Not active</a></li>
          </ul>
        </div>

      </div>


      <form role="search" method="POST" action="" @submit.prevent="search">

        <div class="input-group">

          <input class="form-control " type="search" placeholder="Search" aria-label="Search" v-model="search_content">
          <button type="submit" class="btn btn-outline-success" @click="search">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search me-2"
              viewBox="0 0 16 16">
              <path
                d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z" />
            </svg>
          </button>
          <button type="button" class="btn btn-outline-success dropdown-toggle dropdown-toggle-split"
            data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false">
            <span class="visually-hidden">Toggle Dropdown</span>
          </button>

          <div class="dropdown-menu">
            <li><a class="dropdown-item disabled text-center">Choose filters</a></li>
            <li>
              <hr class="dropdown-divider">
            </li>

            <div class="mb-1">
              <input type="checkbox" class="btn-check dropdown-item" id="btncheck1" name="checkbox_title"
                autocomplete="off" checked>
              <label class="btn btn-outline-secondary w-100 rounded-0 border-0" for="btncheck1">Username</label>
            </div>

            <div class="mb-1">
              <input type="checkbox" class="btn-check dropdown-item" id="btncheck2" name="checkbox_content"
                autocomplete="off">
              <label class="btn btn-outline-secondary w-100 rounded-0 border-0" for="btncheck2">Email</label>
            </div>

          </div>

        </div>
      </form>

    </div>

    <!-- End of search bar section -->

    <div v-if="users.length === 0" class="text-danger fs-2">
      No records.
    </div>

    <div v-else class="table-responsive">
      <table class="table table-hover table-striped">
        <thead>
          <tr class="text-center">
            <th>USERNAME</th>
            <th>EMAIL</th>
            <th>USER ROLE</th>
            <th>ACTIVE</th>
            <th>ACTION</th>
          </tr>
        </thead>
        <tbody class="table-group-divider">
          <tr v-for="user in users" :key="user.id" class="text-center">
            <td>{{ user.username }}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.user_role }}</td>
            <td>
              <span v-if="user.is_active">Yes</span>
              <span v-else>No</span>
            </td>
            <td>
              <button class="btn btn-outline-secondary m-3" @click="editUser(user)">Edit</button>
              <button class="btn btn-outline-danger" @click="deleteConfirm(user.username, user.user_role)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>


    <!-- Confirmation modal -->
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#confirmModal"
      id="confirm_modal_button" style="display: none;">
    </button>

    <!-- Modal -->
    <div class="modal fade" id="confirmModal" tabindex="-1" aria-labelledby="confirmModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="confirmModalLabel">Confirm delete operation</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body text-danger fs-5">
            <p>
              You are trying to delete {{ dataConfirmUsername }}, are you sure?
            </p>
          </div>
          <div class="modal-footer d-flex justify-content-center">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">No</button>
            <button type="button" class="btn btn-danger" data-bs-dismiss="modal"
              @click="deleteUser(dataConfirmUsername, dataConfirmUserRole)">Yes</button>
          </div>
        </div>
      </div>
    </div>
    <!-- Confirmation modal -->

    <!-- Message modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#ErrorModal" id="hiddenButton"
      style="display: none;">
    </button>
    <div class="modal fade" id="ErrorModal" tabindex="-1" aria-labelledby="ErrorModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="ErrorModalLabel">
              <p v-if="dataError">Error</p>
              <p v-else>Success</p>
            </h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"
              @click='loadUsers'></button>
          </div>
          <div class="modal-body text-center text-danger">
            <div v-if="dataError">
              <p> {{ dataError }}</p>
            </div>
            <div v-if="dataSuccess">
              <p class="text-success">Succesfully created new user with username {{ dataSuccess.username }}
              </p>
            </div>


          </div>

        </div>
      </div>
    </div>
    <!-- Message modal -->

      <button type="button" class="btn btn-primary" @click="reloadComponent">reload</button>


  </div>
</template>
  
<script>
import axios from 'axios';

export default {
  name: 'App',

  data() {
    return {
      users: [],
      search_content: '',
      dataError: null,
      dataSuccess: null,
      dataConfirmUsername: null,
      dataConfirmUserRole: null,
      selectedRole: 'All',
      selectedActive: 'All',
      query_data: {},
    };
  },

  created() {
    this.loadUsers();

    // check for messages in local storage
    if (localStorage.getItem('message')) {
      const message = localStorage.getItem('message');
      console.log(message);
      localStorage.removeItem('message');
      //   this.dataError = message;
      //   document.getElementById('hiddenButton').click();
      // this.dataError = message;
      //       document.getElementById('hiddenButton').click();

    }
  },

  methods: {
    async loadUsers() {
      try {
        const query_data = {
          role: this.selectedRole,
          active: this.selectedActive,
        }

        const response = await axios.get(`get-users/${query_data.role}/${query_data.active}/`);

        this.users = response.data;
        console.log(response.data)
      }
      catch (error) {
        console.error('Error when fetching', error);
      }
    },

    deleteConfirm(username, user_role) {
      this.dataConfirmUsername = username;
      this.dataConfirmUserRole = user_role;
      document.getElementById('confirm_modal_button').click();
    },

    async deleteUser(username, user_role) {
      try {
        const response = await axios.delete(`remove-user/${username}/${user_role}/`);
        if (response.data.error) {
          this.dataError = response.data.error;
          document.getElementById('hiddenButton').click();
        }
        else if (response.data.message) {
          localStorage.setItem('message', response.data.message);
          this.loadUsers();
        }

      }
      catch (error) {
        console.error('Error when fetching', error);
      }
    },

    editUser(user) {

    },

    search() {
      console.log(this.search_content)
    },

    reloadComponent() {
      this.loadUsers();
    },


  },
};
</script>
  