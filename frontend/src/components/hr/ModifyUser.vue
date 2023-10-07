<template>
  <div>

    <p class="p-2 fw-bolder fs-5">Filters</p>

    <!-- Search bar section -->
    <v-row class="mb-5 d-flex justify-content-between">

      <v-col cols="auto">
        <!-- User role -->
        <span>

          <div class="btn-group dropdown mx-2">
            <v-btn disabled class="rounded-s-xl rounded-0"
              :class="{ 'bg-green-lighten-5': !theme, 'bg-grey-darken-3': theme }">
              User role
            </v-btn>
            <v-btn id="role-activator" variant="tonal" class="rounded-e-xl rounded-0"
              :class="{ 'bg-green-lighten-5': !theme, 'bg-grey-darken-3': theme }">

              {{ selectedRole }}

              <span class="material-symbols-outlined">
                arrow_drop_down
              </span>
            </v-btn>
          </div>

          <v-menu activator="#role-activator">
            <v-list>
              <v-list-item v-for="option in userRoleList" :key="option.name" :value="option.property"
                @click="chooseRole(option.property)">
                <v-list-item-title>
                  {{ option.name }}
                </v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>

        </span>
        <!-- User role -->

        <!-- User status -->
        <span>

          <div class="btn-group dropdown mx-2">

            <v-btn disabled class="rounded-s-xl rounded-0"
              :class="{ 'bg-green-lighten-5': !theme, 'bg-grey-darken-3': theme }">
              User status
            </v-btn>

            <v-btn id="status-activator" variant="tonal" class="rounded-e-xl rounded-0"
              :class="{ 'bg-green-lighten-5': !theme, 'bg-grey-darken-3': theme }">

              <span v-if="selectedActive === 'True'">Active</span>
              <span v-else-if="selectedActive === 'False'">Not active</span>
              <span v-else>All</span>
              <span class="material-symbols-outlined">
                arrow_drop_down
              </span>
            </v-btn>

          </div>
          <v-menu activator="#status-activator">

            <v-list>
              <v-list-item v-for="option in userStatusList" :key="option.name" :value="option.property"
                @click="chooseStatus(option.property)">
                <v-list-item-title>{{ option.name }}</v-list-item-title>
              </v-list-item>
            </v-list>

          </v-menu>

        </span>
        <!-- User status -->

      </v-col>

      <v-col cols="5">
        <!-- Search bar -->
        <v-text-field variant="solo-filled" v-model="search2" label="Search" class="px-1" prepend-icon="mdi-magnify"
          hide-actions clearable/>
        <!-- Search bar -->
      </v-col>

    </v-row>

    <!-- End of search bar section -->






    <!-- Table -->
    <v-data-table :headers="allHeaders" :items="users" :search="search2" class="elevation-1" item-value="id"
      v-model:items-per-page="itemsPerPage" hover no-data-text="No data">




      <!-- Maping is active -->
      <template #item.is_active="{ item }">

        <v-btn variant="plain"
          @click="changeStateConfirm(item.columns.username, item.columns.user_role, item.columns.is_active)">
          <v-tooltip activator="parent" location="top">Click to change status</v-tooltip>

          <span v-if="item.columns.is_active" class="material-symbols-outlined" style="color:green">
            check
          </span>

          <span v-else class="material-symbols-outlined" style="color:red">
            check_indeterminate_small
          </span>
        </v-btn>

      </template>
      <!-- Maping is active -->


      <!-- Email -->
      <template v-slot:item.email="{ item }">

        <v-btn variant="plain" v-ripple="{ class: 'text-success' }" @click="copyElement(item.columns.email)">

          {{ item.columns.email }}

          <v-tooltip activator="parent" location="top">
            Click email to copy
          </v-tooltip>

        </v-btn>
      </template>
      <!-- Email -->



      <!-- Buttons -->
      <template v-slot:item.action="{ item }">
        <!-- Button show info -->
        <v-btn variant="plain" color="blue" @click="userDetails(item.columns.username, item.columns.user_role)">
          <span class="material-symbols-outlined">
            description
          </span>
          <v-tooltip activator="parent" location="top">Show user details</v-tooltip>
        </v-btn>
        <!-- Button show info -->


        <!-- Button edit -->
        <v-btn variant="plain" color="green" @click="editUser(item.columns.username, item.columns.user_role)">
          <span class="material-symbols-outlined d-flex">
            edit
          </span>
          <v-tooltip activator="parent" location="top">Edit</v-tooltip>
        </v-btn>
        <!-- Button edit -->


        <!-- Button delete -->
        <v-btn variant="plain" color="red" @click="deleteConfirm(item.columns.username)">
          <span class="material-symbols-outlined d-flex">
            delete
          </span>
          <v-tooltip activator="parent" location="top">Delete</v-tooltip>
        </v-btn>
        <!-- Button delete -->
      </template>
      <!-- Buttons -->


    </v-data-table>
    <!-- Table -->



    <!-- Dialaogs section -->

    <!-- Delete user dialog -->
    <v-dialog v-model="dialogDelete" width="400">
      <v-card>
        <div class="text-warning text-h6 text-md-h5 text-lg-h4">

          <div class="d-flex justify-content-between align-items-center px-4 pt-4">
            <span class="material-symbols-outlined">
              warning
            </span>
            <span>
              Warning
            </span>
            <span class="material-symbols-outlined">
              warning
            </span>
          </div>
          <hr>
        </div>

        <div class="pa-3" align="center">

          You are trying to delete
          <span class='fw-bolder'>
            {{ usernameDelete }}
          </span>
          , this operation is <span class="fw-bold">irreversible</span>.
          Are you sure?

        </div>
        <hr>

        <div class="justify-center d-flex align-items-center mb-3">
          <v-btn variant="outlined" width="150" class="mr-5" @click="dialogDelete = false">No</v-btn>
          <v-btn width="150" @click="deleteUser(usernameDelete)" color="red">Yes</v-btn>
        </div>

      </v-card>
    </v-dialog>
    <!-- Delete user dialog -->

    <!-- Change state of user dialog -->
    <v-dialog v-model="dialogState" width="400">
      <v-card>
        <div class="text-warning text-h6 text-md-h5 text-lg-h4">

          <div class="d-flex justify-content-between align-items-center px-4 pt-4">
            <span class="material-symbols-outlined">
              warning
            </span>
            <span>
              Warning
            </span>
            <span class="material-symbols-outlined">
              warning
            </span>
          </div>
          <hr>
        </div>

        <div class="pa-3" align="center">

          This operation will change active state of
          <span class='fw-bolder'>
            {{ change_state.username }}
          </span>
          from
          <span v-if="change_state.state === true" class="text-success"> active </span>
          <span v-else class="text-danger"> not active </span>
          to
          <span v-if="change_state.state === true" class="text-danger"> not active </span>
          <span v-else class="text-success"> active </span>
          Are you sure?

        </div>
        <hr>

        <div class="justify-center d-flex align-items-center mb-3">
          <v-btn variant="outlined" width="150" class="mr-5" @click="dialogState = false">No</v-btn>
          <v-btn width="150" @click="changeState(change_state.username)" color="red">Yes</v-btn>
        </div>

      </v-card>
    </v-dialog>
    <!-- Change state of user dialog -->


    <!-- dialog -->
    <v-dialog v-model="UserDetailsDialog" width="auto">
      <v-card>
        <v-card-text>
          <v-table>
            <thead>
              <tr>
                <th class="text-left">
                  Name
                </th>
                <th class="text-left">
                  Value
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(value, key) in userDetailData" :key="key">
                <td>{{ key }}</td>
                <td v-if="value === null">
                  <span class="material-symbols-outlined">
                    check_indeterminate_small
                  </span>
                </td>
                <td v-else>
                  {{ value }}
                </td>

              </tr>
            </tbody>
          </v-table>

        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" block @click="UserDetailsDialog = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <!-- dialog -->

    <!-- Dialaogs section -->

    <!-- Snackbar -->
    <v-snackbar v-model="alert" :timeout="3000" location="bottom" color="success">
      {{ snackContent }}
      <template v-slot:actions>
        <v-btn color="pink" variant="text" @click="alert = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>

    <!-- Snackbar -->


  </div>
</template>
  

<script setup>
import { VDataTable } from 'vuetify/labs/VDataTable'
</script>

<script>
import axios, { all } from 'axios';
import useEventsBus from '../../plugins/eventBus.js'
import { ref, watch } from "vue";
import { useTheme } from 'vuetify'
import { VDataTable } from 'vuetify/labs/VDataTable'
import { resolveDirective } from 'vue';

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
      UserDetailsDialog: false,
      userDetailData: {},
      alert: false,
      snackContent: '',

      search2: '',
      itemsPerPage: 25,

      dialogState: false,
      dialogDelete: false,

      userRoleList: [
        {
          name: 'All',
          property: 'All',
        },
        {
          name: 'HR',
          property: 'HR',
        },
        {
          name: 'Asset',
          property: 'Asset',
        },
        {
          name: 'Payroll',
          property: 'Payroll',
        },
        {
          name: 'Clients',
          property: 'Clients',
        },
        {
          name: 'Manager',
          property: 'Manager',
        },
        {
          name: 'Driver',
          property: 'Driver',
        },
      ],
      userStatusList: [
        {
          name: 'All',
          property: 'All',
        },
        {
          name: 'Active',
          property: 'True',
        },
        {
          name: 'Not active',
          property: 'False',
        },
      ],
      allHeaders: [
        {
          title: 'Username',
          align: 'center',
          sortable: false,
          key: 'username',
        },
        { title: 'Email', align: 'center', key: 'email', sortable: false },
        { title: 'User role', align: 'center', key: 'user_role', sortable: false },
        { title: 'Active', align: 'center', key: 'is_active', sortable: false },
        { title: 'Joined', align: 'center', key: 'date_joined' },
        { title: 'Actions', align: 'center', key: 'action', sortable: false },

      ],

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


    // Check for messages
    const message = localStorage.getItem('message');
    if (message) {
      this.snackContent = message;
      this.$nextTick(() => {
        this.alert = true;
      });
      localStorage.removeItem('message');
    }

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


    copyElement(content) {
      const textarea = document.createElement('textarea');
      textarea.value = content;
      textarea.style.position = 'fixed';
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      document.body.removeChild(textarea);
    },

    previousPage() {
      this.currentPage -= 1;
      this.loadUsers();
    },
    nextPage() {
      this.currentPage += 1;
      this.loadUsers();
    },

    chooseRole(role) {
      this.selectedRole = role;
      this.defineColumnsByUserRole();
      this.loadUsers();
    },

    chooseStatus(status) {
      console.log(status);
      this.selectedActive = status;
      this.loadUsers()
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
          { label: 'Joined', attribute: 'date_joined' },

        ],

      };

      this.columns = columnDefinitions[this.selectedRole] || [];
    },


    deleteConfirm(username) {
      this.usernameDelete = username;
      this.dialogDelete = true;
    },

    async deleteUser() {
      try {
        const response = await axios.delete('api/users/delete/' + this.usernameDelete + '/');
        this.usernameDelete = '';
        this.dialogDelete = false;
        this.reloadComponent()


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
          this.$root.changeCurrentComponent('AddHrComponent');
          break;

        case 'Asset':
          this.$root.changeCurrentComponent('AddAssetComponent');
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
      this.dialogState = true;
    },


    async changeState(username) {
      const response = await axios.put(`api/users/change-state/${username}/`)
      this.dialogState = false;
      this.reloadComponent()

    },

    async userDetails(username, role) {
      const response = await axios.get(`api/users/get/${username}/${role}/`);
      this.userDetailData = response.data;
      this.UserDetailsDialog = true;
      console.log(this.userDetailData)

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