<template>
  <div>

    <v-card elevation="1" class="pa-5 rounded-xl" color="teal-darken-2">

      <p class="p-2 fw-bolder text-h4">Filters</p>

      <!-- Search bar section -->
      <v-row class="mb-5 d-flex justify-content-between">

        <v-col cols="auto">
          <!-- User role -->
          <span>

            <div class="btn-group dropdown mx-2">

              <v-btn id="role-activator" variant="tonal" class="rounded-xl rounded-0 text-white">
                <span class="pr-2">User status - </span>
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

              <v-btn id="status-activator" variant="tonal" class="rounded-xl rounded-0 text-white">
                <span class="pr-2">User status - </span>
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
          <v-text-field variant="solo-filled" v-model="searchInput" @keydown.enter="searchTable = searchInput"
            label="Search" class="px-1 " prepend-inner-icon="mdi-magnify" hide-actions clearable
            hint="Press enter to search" />
          <!-- Search bar -->
        </v-col>

      </v-row>

      <!-- End of search bar section -->


      <!-- Combobox columns selection -->
      <v-col cols="12">
        <v-expansion-panels>
          <v-expansion-panel title="Choose columns" elevation="1">

            <v-expansion-panel-text>

              <v-combobox variant="outlined" v-model="selectedColumns" :items="avaliableColumns" label="Select columns"
                prepend-icon="mdi-table-edit" multiple chips>

              </v-combobox>
            </v-expansion-panel-text>

          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
      <!-- Combobox columns selection -->

    </v-card>

    <v-divider thickness="12" class="rounded-xl my-7"></v-divider>

    <div class="text-h3 ma-5">
      Data
    </div>

    <!-- Table -->
    <v-data-table :headers="updatedColumns" :items="users" :search="searchTable" :loading="tableLoading"
      class="elevation-4 rounded-xl" item-value="username" v-model:items-per-page="itemsPerPage" hover
      select-strategy="all" show-current-page>


      <!-- No data -->
      <template v-slot:no-data>
        <p class="text-h4 pa-5">
          <span class="material-symbols-outlined">
            database
          </span>
          No data
        </p>
      </template>
      <!-- No data -->



      <!-- Actions label -->
      <template v-slot:column.action="{ column }">
        <span class="text-success">
          {{ column.title }}
        </span>
      </template>
      <!-- Actions label -->



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
                  <v-icon icon="mdi-minus-thick"></v-icon>
                </td>

                <td v-else-if="value === true">
                  <v-icon icon="mdi-check-bold" style="color:green"></v-icon>
                </td>

                <td v-else-if="value === false">
                  <v-icon icon="mdi-close-thick" style="color:red"></v-icon>
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
  </div>
</template>
  

<script setup>
import { VDataTable } from 'vuetify/labs/VDataTable'
</script>

<script>
import axios, { all } from 'axios';
import useEventsBus from '../../plugins/eventBus.js'
const { emit } = useEventsBus()
import { ref, watch } from "vue";
import { useTheme } from 'vuetify'
import { VDataTable } from 'vuetify/labs/VDataTable'


export default {
  name: 'App',

  data() {
    return {
      users: [],


      users_per_site: 20,
      page_flip: {
      },
      query: '',


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

      searchInput: '',
      searchTable: '',
      itemsPerPage: 25,

      dialogState: false,
      dialogDelete: false,

      selectedColumns: [],
      avaliableColumns: [],

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

      tableLoading: true,

      necessaryHeaders: [
        { title: 'NO', align: 'center', sortable: false, key: 'rownumber' },
        { title: 'USERNAME', align: 'center', sortable: false, key: 'username' },
        { title: 'USER ROLE', align: 'center', key: 'user_role', sortable: false },
      ],

      allHeaders: [
        { title: 'EMAIL', align: 'center', key: 'email', sortable: false },
        { title: 'ACTIVE', align: 'center', key: 'is_active', sortable: false },
        { title: 'JOINED', align: 'center', key: 'date_joined' },
        { title: 'ACTIONS', align: 'center', key: 'action', sortable: false },
      ],
      DriverHeaders: [
        { title: 'EMAIL', align: 'center', key: 'email', sortable: false },
        { title: 'PHONE NUMBER', align: 'center', key: 'phone', sortable: false },
        { title: 'ACTIVE', align: 'center', key: 'is_active', sortable: false },
        { title: 'JOINED', align: 'center', key: 'date_joined' },
        { title: 'COUNTRY', align: 'center', key: 'residence_country', sortable: false },
        { title: 'STATE', align: 'center', key: 'residence_state', sortable: false },
        { title: 'ZIP', align: 'center', key: 'residence_zip_code', sortable: false },
        { title: 'CITY', align: 'center', key: 'residence_city', sortable: false },
        { title: 'STREET', align: 'center', key: 'residence_street', sortable: false },
        { title: 'HOME', align: 'center', key: 'residence_home_number', sortable: false },
        { title: 'APARTAMENT', align: 'center', key: 'residence_apartament_number', sortable: false },
        { title: 'ACTIONS', align: 'center', key: 'action', sortable: false },
      ],
      AssetHeaders: [
        { title: 'EMAIL', align: 'center', key: 'email', sortable: false },
        { title: 'PHONE NUMBER', align: 'center', key: 'phone', sortable: false },
        { title: 'ACTIVE', align: 'center', key: 'is_active', sortable: false },
        { title: 'JOINED', align: 'center', key: 'date_joined' },
        { title: 'COUNTRY', align: 'center', key: 'residence_country', sortable: false },
        { title: 'STATE', align: 'center', key: 'residence_state', sortable: false },
        { title: 'ZIP', align: 'center', key: 'residence_zip_code', sortable: false },
        { title: 'CITY', align: 'center', key: 'residence_city', sortable: false },
        { title: 'STREET', align: 'center', key: 'residence_street', sortable: false },
        { title: 'HOME', align: 'center', key: 'residence_home_number', sortable: false },
        { title: 'APARTAMENT', align: 'center', key: 'residence_apartament_number', sortable: false },
        { title: 'ACTIONS', align: 'center', key: 'action', sortable: false },
      ],
      HRHeaders: [
        { title: 'EMAIL', align: 'center', key: 'email', sortable: false },
        { title: 'PHONE NUMBER', align: 'center', key: 'phone', sortable: false },
        { title: 'ACTIVE', align: 'center', key: 'is_active', sortable: false },
        { title: 'JOINED', align: 'center', key: 'date_joined' },
        { title: 'COUNTRY', align: 'center', key: 'residence_country', sortable: false },
        { title: 'STATE', align: 'center', key: 'residence_state', sortable: false },
        { title: 'ZIP', align: 'center', key: 'residence_zip_code', sortable: false },
        { title: 'CITY', align: 'center', key: 'residence_city', sortable: false },
        { title: 'STREET', align: 'center', key: 'residence_street', sortable: false },
        { title: 'HOME', align: 'center', key: 'residence_home_number', sortable: false },
        { title: 'APARTAMENT', align: 'center', key: 'residence_apartament_number', sortable: false },
        { title: 'ACTIONS', align: 'center', key: 'action', sortable: false },
      ],
      ManagerHeaders: [
        { title: 'EMAIL', align: 'center', key: 'email', sortable: false },
        { title: 'PHONE NUMBER', align: 'center', key: 'phone', sortable: false },
        { title: 'ACTIVE', align: 'center', key: 'is_active', sortable: false },
        { title: 'JOINED', align: 'center', key: 'date_joined' },
        { title: 'COUNTRY', align: 'center', key: 'residence_country', sortable: false },
        { title: 'STATE', align: 'center', key: 'residence_state', sortable: false },
        { title: 'ZIP', align: 'center', key: 'residence_zip_code', sortable: false },
        { title: 'CITY', align: 'center', key: 'residence_city', sortable: false },
        { title: 'STREET', align: 'center', key: 'residence_street', sortable: false },
        { title: 'HOME', align: 'center', key: 'residence_home_number', sortable: false },
        { title: 'APARTAMENT', align: 'center', key: 'residence_apartament_number', sortable: false },
        { title: 'ACTIONS', align: 'center', key: 'action', sortable: false },
      ],
      PayrollHeaders: [
        { title: 'EMAIL', align: 'center', key: 'email', sortable: false },
        { title: 'PHONE NUMBER', align: 'center', key: 'phone', sortable: false },
        { title: 'ACTIVE', align: 'center', key: 'is_active', sortable: false },
        { title: 'JOINED', align: 'center', key: 'date_joined' },
        { title: 'COUNTRY', align: 'center', key: 'residence_country', sortable: false },
        { title: 'STATE', align: 'center', key: 'residence_state', sortable: false },
        { title: 'ZIP', align: 'center', key: 'residence_zip_code', sortable: false },
        { title: 'CITY', align: 'center', key: 'residence_city', sortable: false },
        { title: 'STREET', align: 'center', key: 'residence_street', sortable: false },
        { title: 'HOME', align: 'center', key: 'residence_home_number', sortable: false },
        { title: 'APARTAMENT', align: 'center', key: 'residence_apartament_number', sortable: false },
        { title: 'ACTIONS', align: 'center', key: 'action', sortable: false },
      ],
      ClientsHeaders: [
        { title: 'EMAIL', align: 'center', key: 'email', sortable: false },
        { title: 'PHONE NUMBER', align: 'center', key: 'phone', sortable: false },
        { title: 'ACTIVE', align: 'center', key: 'is_active', sortable: false },
        { title: 'JOINED', align: 'center', key: 'date_joined' },
        { title: 'COUNTRY', align: 'center', key: 'residence_country', sortable: false },
        { title: 'STATE', align: 'center', key: 'residence_state', sortable: false },
        { title: 'ZIP', align: 'center', key: 'residence_zip_code', sortable: false },
        { title: 'CITY', align: 'center', key: 'residence_city', sortable: false },
        { title: 'STREET', align: 'center', key: 'residence_street', sortable: false },
        { title: 'HOME', align: 'center', key: 'residence_home_number', sortable: false },
        { title: 'APARTAMENT', align: 'center', key: 'residence_apartament_number', sortable: false },
        { title: 'ACTIONS', align: 'center', key: 'action', sortable: false },
      ],

    };
  },

  computed: {
    updatedColumns() {
      return [...this.necessaryHeaders, ...this.selectedColumns];
    },
  },

  created() {
    this.reloadComponent();
    this.chooseRole('All')
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

        this.page_flip = {
          count: response.data.count,
          next: response.data.next,
          previous: response.data.previous,
        }

        this.users = response.data.results;
        console.log(response.data.results);

        // Add number for each row
        this.users.forEach((user, index) => {
          user.rownumber = index + 1;
        });



        this.tableLoading = false;
      }
      catch (error) {

        const messageData = {
          message: `Error, please try again`,
          type: 'error'
        };

        localStorage.setItem('message', JSON.stringify(messageData));
        emit('message', '');
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

    chooseRole(role) {
      this.selectedRole = role;

      switch (role) {
        case 'All':
          this.selectedColumns = this.allHeaders;
          this.avaliableColumns = this.allHeaders;
          break;

        case 'Driver':
          this.selectedColumns = this.DriverHeaders;
          this.avaliableColumns = this.DriverHeaders;
          break;

        case 'HR':
          this.selectedColumns = this.HRHeaders;
          this.avaliableColumns = this.HRHeaders;
          break;

        case 'Asset':
          this.selectedColumns = this.AssetHeaders;
          this.avaliableColumns = this.AssetHeaders;
          break;

        case 'Payroll':
          this.selectedColumns = this.PayrollHeaders;
          this.avaliableColumns = this.PayrollHeaders;
          break;

        case 'Clients':
          this.selectedColumns = this.ClientsHeaders;
          this.avaliableColumns = this.ClientsHeaders;
          break;

        case 'Manager':
          this.selectedColumns = this.ManagerHeaders;
          this.avaliableColumns = this.ManagerHeaders;
          break;
      }
      this.reloadComponent();
    },

    chooseStatus(status) {
      this.selectedActive = status;
      this.reloadComponent();
    },


    deleteConfirm(username) {
      this.usernameDelete = username;
      this.dialogDelete = true;
    },

    async deleteUser() {
      try {
        const response = await axios.delete('api/users/delete/' + this.usernameDelete + '/');
        const delUsername = this.usernameDelete;
        this.usernameDelete = '';
        this.dialogDelete = false;
        this.reloadComponent()


        if (response.status == 204) {
          // Call message
          const messageData = {
            message: `Successfully deleted ${delUsername}`,
            type: 'success'
          };

          localStorage.setItem('message', JSON.stringify(messageData));
          emit('message', '');

        }
        else {
          const messageData = {
            message: 'Error, please try again',
            type: 'error'
          };

          localStorage.setItem('message', JSON.stringify(messageData));
          emit('message', '');


          this.reloadComponent()
        }

      }
      catch (error) {
        const messageData = {
          message: 'Error, please try again',
          type: 'error'
        };

        localStorage.setItem('message', JSON.stringify(messageData));
        emit('message', '');
      }
    },

    editUser(username, user_role) {
      localStorage.setItem('username', username)
      localStorage.setItem('user_role', user_role)

      this.$root.changeCurrentComponent('AddUserComponent');


      switch (user_role) {
        case 'Driver':
          this.$root.changeCurrentComponent('AddDriverComponent');
          break;

        default:
          this.$root.changeCurrentComponent('AddUserComponent');
          break;
      }
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

      // Call message
      const messageData = {
        message: `Successfully changed state of ${username}`,
        type: 'success'
      };

      localStorage.setItem('message', JSON.stringify(messageData));
      emit('message', '');

    },

    async userDetails(username, role) {
      const response = await axios.get(`api/users/get/${username}/${role}/`);
      this.userDetailData = response.data;
      this.UserDetailsDialog = true;

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