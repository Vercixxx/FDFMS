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
            <li @click="selectedRole = 'All'; loadUsers(); defineColumnsByUserRole();"><a
                class="dropdown-item fw-bolder ">All</a></li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li @click="selectedRole = 'HR'; loadUsers(); defineColumnsByUserRole();"><a class="dropdown-item ">HR</a>
            </li>
            <li @click="selectedRole = 'Asset'; loadUsers(); defineColumnsByUserRole();"><a
                class="dropdown-item ">Asset</a></li>
            <li @click="selectedRole = 'Payroll'; loadUsers(); defineColumnsByUserRole();"><a
                class="dropdown-item ">Payroll</a></li>
            <li @click="selectedRole = 'Clients'; loadUsers(); defineColumnsByUserRole();"><a
                class="dropdown-item ">Clients</a></li>
            <li @click="selectedRole = 'Manager'; loadUsers(); defineColumnsByUserRole();"><a
                class="dropdown-item ">Manager</a></li>
            <li @click="selectedRole = 'Driver'; loadUsers(); defineColumnsByUserRole();"><a
                class="dropdown-item ">Driver</a></li>
          </ul>
        </div>



        <div class="btn-group dropdown mx-2">
          <span class="input-group-text rounded-0 rounded-start" id="basic-addon1">User status</span>

          <button type="button" class="btn btn-outline-secondary dropdown-toggle" data-bs-toggle="dropdown"
            aria-expanded="false">

            <span v-if="selectedActive === 'True'">Yes</span>
            <span v-else-if="selectedActive === 'False'">No</span>
            <span v-else>All</span>
          </button>
          <ul class="dropdown-menu">
            <li @click="selectedActive = 'All'; loadUsers();"><a class="dropdown-item fw-bolder ">All</a></li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li @click="selectedActive = 'True'; loadUsers();"><a class="dropdown-item ">Active</a></li>
            <li @click="selectedActive = 'False'; loadUsers();"><a class="dropdown-item ">Not active</a></li>
          </ul>
        </div>



        <div class="btn-group mx-2">
          <input type="number" name="" id="" class="form-control rounded-0 rounded-start w-25 no-spinners text-center"
            v-model="users_per_site" @keyup.enter="loadUsers">
          <span class="input-group-text rounded-0 rounded-end" id="basic-addon1">Users per site</span>
        </div>

      </div>


      <form role="search" method="POST" action="" @submit.prevent="search">
        {{ theme }}
        <div class="input-group">

          <input class="form-control " type="search" placeholder="Search" aria-label="Search" v-model="query">
          <button type="button" class="btn btn-outline-success d-flex align-items-center px-3" @click="search">

            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search me-2"
              viewBox="0 0 16 16">
              <path
                d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z" />
            </svg>
          </button>

        </div>
        <p class="fw-light">{{ page_flip.count }} records</p>
      </form>

    </div>

    <!-- End of search bar section -->



    <!-- Pagination -->
    <div class="d-flex justify-content-center mb-4">

      <!-- Button previous -->
      <button type="button" class="btn btn-outline-secondary" @click="previousPage" :disabled="!page_flip.previous">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-left"
          viewBox="0 0 16 16">
          <path
            d="M10 12.796V3.204L4.519 8 10 12.796zm-.659.753-5.48-4.796a1 1 0 0 1 0-1.506l5.48-4.796A1 1 0 0 1 11 3.204v9.592a1 1 0 0 1-1.659.753z" />
        </svg>
      </button>

      <!-- Current page -->
      <p class="fw-bolder mx-2">Page {{ currentPage + 1 }}</p>

      <!-- Button next -->
      <button type="button" class="btn btn-outline-secondary " @click="nextPage" :disabled="!page_flip.next">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-right"
          viewBox="0 0 16 16">
          <path
            d="M6 12.796V3.204L11.481 8 6 12.796zm.659.753 5.48-4.796a1 1 0 0 0 0-1.506L6.66 2.451C6.011 1.885 5 2.345 5 3.204v9.592a1 1 0 0 0 1.659.753z" />
        </svg>
      </button>

    </div>

    <!-- Pagination -->

    <!-- Table -->
    <div v-if="users.length === 0" class="text-danger fs-2">
      No records.
    </div>

    <div v-else class="table-responsive">
      <table
        :class="{ 'table table-hover table-striped': !theme, 'table table-hover table-striped table-dark ': theme }">
        <thead>
          <tr class="text-center">
            <th v-for="column in columns" :key="column.attribute">
              <span v-if="column.label === 'Active'" class="text-info">
                {{ column.label }}
                <span class="material-symbols-outlined align-middle">
                  block
                </span>
              </span>
              <span v-else>
                {{ column.label }}
              </span>
            </th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody class="table-group-divider">
          <tr v-for="user in users" :key="user.id" class="text-center align-middle "
            :class="{ 'text-decoration-line-through': user.is_active === 'false' ? false : !user.is_active }">
            <td v-for="column in columns" :key="column.attribute">

              <!-- Mapping "is_active" -->
              <span v-if="column.attribute === 'is_active'">

                <!-- SVG when user is active -->
                <svg v-if="user[column.attribute]" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="green"
                  class="bi bi-check-lg" viewBox="0 0 16 16">
                  <path
                    d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z" />
                </svg>

                <!-- SVG when user is not active -->
                <svg v-else xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="red" class="bi bi-x-lg"
                  viewBox="0 0 16 16">
                  <path
                    d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z" />
                </svg>


              </span>
              <!-- other columns -->

              <span v-else>
                <span v-if="user[column.attribute] !== null">{{ user[column.attribute] }}</span>
                <svg v-else xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-x"
                  viewBox="0 0 16 16">
                  <path
                    d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 1 1 .708.708L8.707 8l2.647 2.646a.5.5 0 1 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z" />
                </svg>
              </span>

            </td>
            <td>
              <!-- Button status -->
              <button class="btn btn-outline-info m-1"
                @click="changeStateConfirm(user.username, user.user_role, user.is_active)"
                :class="{ 'btn-outline-danger': user.is_active === 'false' ? false : !user.is_active }">
                <span class="material-symbols-outlined d-flex">
                  block
                </span>
                <v-tooltip activator="parent" location="top">Change active status</v-tooltip>
              </button>

              <!-- Button edit -->
              <button class="btn btn-outline-success m-1" @click="editUser(user.username, user.user_role)">
                <span class="material-symbols-outlined d-flex">
                  edit
                </span>
                <v-tooltip activator="parent" location="top">Edit</v-tooltip>
              </button>

              <!-- Button delete -->
              <button class="btn btn-outline-danger m-1" @click="deleteConfirm(user.username)">
                <span class="material-symbols-outlined d-flex">
                  delete
                </span>
                <v-tooltip activator="parent" location="top">Delete</v-tooltip>
              </button>
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
          <div class="modal-header d-flex justify-content-between">
            <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="red" class="bi bi-exclamation-triangle"
              viewBox="0 0 16 16">
              <path
                d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
              <path
                d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
            </svg>
            <h1 class="modal-title fs-5" id="confirmModalLabel">
              Caution
            </h1>
            <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="red" class="bi bi-exclamation-triangle"
              viewBox="0 0 16 16">
              <path
                d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
              <path
                d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
            </svg>
          </div>
          <div class="modal-body text-danger fs-5">
            <p>
              You are trying to delete {{ usernameDelete }}, this operation is <span class="fw-bold">irreversible</span>.
              Are you sure?
            </p>
          </div>
          <div class="modal-footer d-flex justify-content-center">
            <button type="button" class="btn btn-outline-secondary fs-5 w-25" data-bs-dismiss="modal">No</button>
            <button type="button" class="btn btn-danger fs-5 w-25" data-bs-dismiss="modal"
              @click="deleteUser(usernameDelete)">Yes</button>
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
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body text-center text-danger">
            <div v-if="dataError">
              <p> {{ dataError }}</p>
            </div>
            <div v-if="dataSuccess">
              <p class="text-success">{{ dataSuccess }}
              </p>
            </div>


          </div>

        </div>
      </div>
    </div>
    <!-- Message modal -->

    <!-- Change state active modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#StateModal" id="state_modal"
      style="display: none;">
    </button>
    <div class="modal fade" id="StateModal" tabindex="-1" aria-labelledby="StateModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header d-flex justify-content-between">
            <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="red" class="bi bi-exclamation-triangle"
              viewBox="0 0 16 16">
              <path
                d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
              <path
                d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
            </svg>
            <h1 class="modal-title fs-5" id="confirmModalLabel">
              Caution
            </h1>
            <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="red" class="bi bi-exclamation-triangle"
              viewBox="0 0 16 16">
              <path
                d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
              <path
                d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
            </svg>
          </div>
          <div class="modal-body text-center">

            <div>
              This operation will change active state of
              <span class='fw-bolder'>
                {{ change_state.username }}
              </span>
              from
              <span v-if="change_state.state === true"> active </span>
              <span v-else> not active </span>
              to
              <span v-if="change_state.state === true"> not active </span>
              <span v-else> active </span>
              <p class="text-warning fs-4">Are you sure?</p>

            </div>

          </div>

          <div class="modal-footer d-flex justify-content-center">

            <button type="button" class="btn btn-secondary w-25 me-2 fs-4" data-bs-dismiss="modal">No</button>
            <button type="button" class="btn btn-danger w-25 fs-4" data-bs-dismiss="modal"
              @click="changeState(change_state.username)">Yes</button>

          </div>

        </div>
      </div>
    </div>
    <!-- Change state active modal -->



  </div>
</template>
  



<script>
import axios from 'axios';
import useEventsBus from '../../plugins/eventBus.js'
import { ref, watch } from "vue"; // Importuj funkcję watch
import { useTheme } from 'vuetify'

export default {
  name: 'App',

  data() {
    return {
      users: [],
      columns: [],
      currentPage: 0,
      users_per_site: 20,
      page_flip: {
      },
      query: '',
      dataError: null,
      dataSuccess: null,

      selectedRole: 'All',
      selectedActive: 'All',
      usernameDelete: '',

      change_state: {
        username: '',
        user_role: '',
        state: '',
      },
      theme: false, 
    };
  },


  created() {
    this.loadUsers();
    this.defineColumnsByUserRole();
    // check for messages in local storage
    if (localStorage.getItem('message')) {
      const message = localStorage.getItem('message');
      console.log(message);
      localStorage.removeItem('message');
      //   this.dataError = message;
      //   document.getElementById('hiddenButton').click();
      // this.dataError = message;
      //       document.getElementById('hiddenButton').click();

    };
  },

  mounted() {
    const { bus } = useEventsBus();

    watch(
      () => bus.value.get('theme'),
      (val) => {
        const [themeBus] = val ?? [];
        this.theme = themeBus;
      }
    );

    const theme = useTheme();
    this.theme = theme.global.current.value.dark;
  },


  methods: {
    async loadUsers() {
      try {
        const response = await axios.get('api/get-gu/', {
          params: {
            limit: this.users_per_site,
            offset: this.currentPage,
            search: this.query,
            role: this.selectedRole,
            status: this.selectedActive,
          }
        });

        console.log(response.data)

        this.page_flip = {
          count: response.data.count,
          next: response.data.next,
          previous: response.data.previous,
        }

        this.users = response.data.results;
      }
      catch (error) {
        console.error('Error when fetching', error);
      }
    },

    previousPage() {
      this.currentPage -= 1;
      this.loadUsers();
    },
    nextPage() {
      this.currentPage += 1;
      this.loadUsers();
    },

    defineColumnsByUserRole() {
      const columnDefinitions = {
        Driver: [
          { label: 'Username', attribute: 'username' },
          { label: 'Email', attribute: 'email' },
          { label: 'Phone Number', attribute: 'phone' },
          { label: 'Active', attribute: 'is_active' },
          { label: 'Country', attribute: 'residence_country' },
          { label: 'City', attribute: 'residence_city' },
          { label: 'Zip code', attribute: 'residence_zip_code' },
          { label: 'State', attribute: 'residence_state' },
          { label: 'Street', attribute: 'residence_street' },
          { label: 'Home number', attribute: 'residence_home_number' },
          { label: 'Apartament', attribute: 'residence_apartament_number' },
        ],
        Asset: [
          { label: 'Username', attribute: 'username' },
          { label: 'Email', attribute: 'email' },
          { label: 'Phone Number', attribute: 'phone' },
          { label: 'Active', attribute: 'is_active' },
          { label: 'Country', attribute: 'residence_country' },
          { label: 'City', attribute: 'residence_city' },
          { label: 'Zip code', attribute: 'residence_zip_code' },
          { label: 'State', attribute: 'residence_state' },
          { label: 'Street', attribute: 'residence_street' },
          { label: 'Home number', attribute: 'residence_home_number' },
          { label: 'Apartament', attribute: 'residence_apartament_number' },

        ],
        HR: [
          { label: 'Username', attribute: 'username' },
          { label: 'Email', attribute: 'email' },
          { label: 'Phone Number', attribute: 'phone' },
          { label: 'Active', attribute: 'is_active' },
          { label: 'Country', attribute: 'residence_country' },
          { label: 'City', attribute: 'residence_city' },
          { label: 'Zip code', attribute: 'residence_zip_code' },
          { label: 'State', attribute: 'residence_state' },
          { label: 'Street', attribute: 'residence_street' },
          { label: 'Home number', attribute: 'residence_home_number' },
          { label: 'Apartament', attribute: 'residence_apartament_number' },

        ],
        Manager: [
          { label: 'Username', attribute: 'username' },
          { label: 'Email', attribute: 'email' },
          { label: 'Phone Number', attribute: 'phone' },
          { label: 'Active', attribute: 'is_active' },
          { label: 'Country', attribute: 'residence_country' },
          { label: 'City', attribute: 'residence_city' },
          { label: 'Zip code', attribute: 'residence_zip_code' },
          { label: 'State', attribute: 'residence_state' },
          { label: 'Street', attribute: 'residence_street' },
          { label: 'Home number', attribute: 'residence_home_number' },
          { label: 'Apartament', attribute: 'residence_apartament_number' },

        ],
        Payroll: [
          { label: 'Username', attribute: 'username' },
          { label: 'Email', attribute: 'email' },
          { label: 'Phone Number', attribute: 'phone' },
          { label: 'Active', attribute: 'is_active' },
          { label: 'Country', attribute: 'residence_country' },
          { label: 'City', attribute: 'residence_city' },
          { label: 'Zip code', attribute: 'residence_zip_code' },
          { label: 'State', attribute: 'residence_state' },
          { label: 'Street', attribute: 'residence_street' },
          { label: 'Home number', attribute: 'residence_home_number' },
          { label: 'Apartament', attribute: 'residence_apartament_number' },

        ],
        Clients: [
          { label: 'Username', attribute: 'username' },
          { label: 'Email', attribute: 'email' },
          { label: 'Phone Number', attribute: 'phone' },
          { label: 'Active', attribute: 'is_active' },
          { label: 'Country', attribute: 'residence_country' },
          { label: 'City', attribute: 'residence_city' },
          { label: 'Zip code', attribute: 'residence_zip_code' },
          { label: 'State', attribute: 'residence_state' },
          { label: 'Street', attribute: 'residence_street' },
          { label: 'Home number', attribute: 'residence_home_number' },
          { label: 'Apartament', attribute: 'residence_apartament_number' },

        ],
        All: [
          { label: 'Username', attribute: 'username' },
          { label: 'Email', attribute: 'email' },
          { label: 'User role', attribute: 'user_role' },
          { label: 'Active', attribute: 'is_active' },

        ],

      };

      this.columns = columnDefinitions[this.selectedRole] || [];
    },


    deleteConfirm(username) {
      this.usernameDelete = username
      document.getElementById('confirm_modal_button').click();
    },

    async deleteUser() {
      try {
        const response = await axios.delete('api/users/delete/' + this.usernameDelete + '/');
        this.usernameDelete = '';
        this.reloadComponent()
        console.log(response)

        if (response.status == 204) {
          this.dataSuccess = 'Success!';
          document.getElementById('hiddenButton').click();
        }
        else {
          console.log('Error')
          this.loadUsers();
        }

      }
      catch (error) {
        console.error('Error when fetching', error);
      }
    },

    editUser(username, user_role) {
      localStorage.setItem('username', username)
      localStorage.setItem('user_role', user_role)

      switch (user_role) {
        case 'HR':
          this.$parent.showAddHrComponent()
          break;

        case 'Asset':
          this.$parent.showAddAssetComponent()
          break;
      }



    },

    search() {
      this.loadUsers();
    },

    reloadComponent() {
      this.loadUsers();
    },

    changeStateConfirm(username, user_role, state) {
      this.change_state.username = username;
      this.change_state.user_role = user_role;
      this.change_state.state = state;
      document.getElementById('state_modal').click();
    },

    async changeState(username) {
      const response = await axios.put(`api/users/change-state/${username}/`)
      console.log(response)
      this.reloadComponent()

    },


  },

};
</script>
  
<style>
.no-spinners {
  -moz-appearance: textfield;
  -webkit-appearance: none;
  appearance: none;
}

input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  appearance: none;
  margin: 0;
}
</style>