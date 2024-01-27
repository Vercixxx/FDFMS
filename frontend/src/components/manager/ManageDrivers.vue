<template>
    <div>

        <h2 v-if="selectedRestaurant == null">
            Select restaurant first
        </h2>

        <v-autocomplete variant="outlined" v-model="selectedRestaurant" :items="avaliableRestaurants"
            label="Select restaurant" prepend-icon="mdi-store" no-data-text="Sorry, you don't belong to any restaurants"
            @update:model-value="loadUsers()"></v-autocomplete>


        <span v-if="selectedRestaurant != null">

            <div class="mt-5 mb-5">


                <!-- Search bar section -->
                <v-row>

                    <v-col cols="12" sm="12">
                        <v-expansion-panels>
                            <v-expansion-panel title="Filters" elevation="1" style="border: 1px solid teal;">

                                <v-expansion-panel-text>
                                    <v-row justify="center" align="center">
                                        <v-col cols="auto">
                                            <!-- User status -->
                                            <v-menu transition="slide-y-transition">
                                                <template v-slot:activator="{ props }">
                                                    <v-btn color="grey" v-bind="props" variant="outlined">
                                                        <span class="pr-2">User status - </span>
                                                        <span v-if="selectedActive === 'True'">Active</span>
                                                        <span v-else-if="selectedActive === 'False'">Not active</span>
                                                        <span v-else>All</span>
                                                    </v-btn>
                                                </template>
                                                <v-list>
                                                    <v-list-item v-for="option in userStatusList" :key="option.name">
                                                        <v-list-item-title role="button"
                                                            @click="chooseStatus(option.property)">
                                                            {{ option.name }}
                                                        </v-list-item-title>
                                                    </v-list-item>
                                                </v-list>
                                            </v-menu>
                                            <!-- User status -->
                                        </v-col>

                                        <v-col cols="12" sm="3">
                                            <v-combobox variant="outlined" v-model="selectedColumns"
                                                :items="avaliableColumns" label="Select columns"
                                                prepend-icon="mdi-table-edit" multiple chips>
                                            </v-combobox>
                                        </v-col>

                                        <v-col cols="12" sm="2">
                                            <v-select v-model="itemsPerPage" variant="solo-filled"
                                                :items="[5, 10, 25, 50, 100]" :label="`Items per page - ${itemsPerPage}`"
                                                @update:model-value="loadUsers()"></v-select>
                                        </v-col>
                                    </v-row>

                                </v-expansion-panel-text>
                            </v-expansion-panel>
                        </v-expansion-panels>

                    </v-col>


                </v-row>

            </div>





            <v-row>
                <v-col justify="start">
                    <div class="text-h4 ma-5 font-weight-bold">
                        Drivers
                    </div>
                </v-col>
                <v-col justify="end" cols="12" sm="4">

                    <!-- Search bar -->
                    <v-text-field variant="solo-filled" v-model="query" @keydown.enter="loadUsers()" label="Search"
                        class="px-1 " prepend-inner-icon="mdi-magnify" hide-actions clearable
                        hint="Press enter to search" />
                    <!-- Search bar -->

                </v-col>
            </v-row>

            <!-- Table -->
            <v-data-table :headers="updatedColumns" :items="users" :loading="loading" density="compact"
                class="elevation-4 rounded-xl" item-value="username" v-model:items-per-page="itemsPerPage" hover
                show-current-page>



                <!-- No data -->
                <template v-slot:no-data>
                    <p class="text-h4 pa-5">
                        <v-icon icon="mdi-database-alert-outline" color="red"></v-icon>
                        <span>
                            No data for selected restaurant
                        </span>
                    </p>
                </template>
                <!-- No data -->



                <!-- Accessing table cells -->
                <template v-slot:item="{ item }">
                    <tr align="center" :style="item.is_active ? '' : 'color: red'">
                        <td v-for="header in updatedColumns" :key="header.key">

                            <template v-if="header.key === 'action'">
                                <span>
                                    <v-btn variant="plain" color="blue" @click="userDetails(item.username, item.user_role)">
                                        <v-icon icon="mdi-book-open-page-variant-outline" class="text-h5"></v-icon>
                                        <v-tooltip activator="parent" location="top">Show {{ item.username }}
                                            details</v-tooltip>
                                    </v-btn>
                                </span>
                            </template>

                            <template v-else-if="header.key === 'is_active'">

                                <v-tooltip location="top"
                                    :text="item.is_active ? `Make ${item.username} not active` : `Make ${item.username} active`">
                                    <template v-slot:activator="{ props }">
                                        <v-btn v-bind="props" variant="plain"
                                            :icon="item.is_active ? 'mdi-check-bold' : 'mdi-close-thick'"
                                            :style="item.is_active ? 'color:green' : 'color:red'"
                                            @click="changeStateConfirm(item.username, item.user_role, item.is_active)"></v-btn>
                                    </template>
                                </v-tooltip>

                            </template>

                            <template v-else-if="header.key === 'email'">

                                <span v-if="item[header.key] === null || item[header.key] === ''">
                                    <v-icon icon="mdi-minus-thick" color="red-lighten-2" />
                                </span>

                                <span v-else>
                                    <v-tooltip location="top" text="Click to copy email">
                                        <template v-slot:activator="{ props }">
                                            <v-btn v-bind="props" variant="plain" @click="copyElement(item.email)">
                                                {{ item.email }}
                                            </v-btn>
                                        </template>
                                    </v-tooltip>
                                </span>

                            </template>


                            <template v-else>
                                <span
                                    v-if="item[header.key] === null || item[header.key] === undefined || item[header.key] === ''">
                                    <v-icon icon="mdi-minus" />
                                </span>
                                <span v-else-if="item[header.key] === true">
                                    <v-icon icon="mdi-check-bold" style="color:green" />
                                </span>
                                <span v-else-if="item[header.key] === false">
                                    <v-icon icon="mdi-close-thick" style="color:red" />
                                </span>
                                <span v-else>
                                    {{ item[header.key] }}
                                </span>
                            </template>

                        </td>
                    </tr>
                </template>
                <!-- Accessing table cells -->


                <template v-slot:bottom="{ page, itemsPerPage }">
                    <v-row>
                        <v-col align="center">
                            <v-pagination v-model="paginationPage" :length="pagiController.total_pages" @next="nextPage()"
                                @prev="prevPage()">
                                <template v-slot:item="{ key, page }">
                                    <v-btn class="mt-1" variant="text" disabled rounded="xl">{{ key }}</v-btn>
                                </template>
                            </v-pagination>
                            <p>Page {{ pagiController.currentPage }} of {{ pagiController.total_pages }}</p>
                            <p>{{ pagiController.totalRecors }} Records total</p>
                        </v-col>
                    </v-row>
                </template>



            </v-data-table>
            <!-- Table -->

        </span>


        <!-- Dialaogs section -->

        <!-- Change state of user dialog -->
        <v-dialog v-model="dialogState" width="400">
            <v-card>
                <div class="text-warning text-h6 text-md-h5 text-lg-h4">
                    <div class="d-flex justify-content-between align-items-center px-4 pt-4">
                        <v-icon icon="mdi-alert" class="text-h4" />
                        Warning
                        <v-icon icon="mdi-alert" class="text-h4" />
                    </div>

                    <hr />
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
                                <td v-if="value === null || value === undefined || value === ''">
                                    <v-icon icon="mdi-minus" />
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
  


<script>
import axios from 'axios';
import useEventsBus from '../../plugins/eventBus.js'
import { watch } from "vue";
import { useTheme } from 'vuetify'


export default {
    name: 'App',

    data() {
        return {
            loggedUserUsername: null,
            loading: true,
            users: [],

            itemsPerPage: 10,
            paginationPage: 1,
            pagiController: {},
            query: '',


            avaliableRestaurants: [],
            selectedRestaurant: null,

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


            dialogState: false,
            dialogDelete: false,

            selectedColumns: [],
            avaliableColumns: [],


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


            necessaryHeaders: [
                { title: 'NO', align: 'center', sortable: false, key: 'rownumber' },
                { title: 'USERNAME', align: 'center', sortable: false, key: 'username' },
                { title: 'USER ROLE', align: 'center', key: 'user_role', sortable: false },
            ],

            actions: [
                { title: 'ACTIONS', align: 'center', key: 'action', sortable: false },
            ],

            DriverHeaders: [
                { title: 'RESTAURANT', align: 'center', key: 'restaurant_name', sortable: false },
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
            ],

        };
    },

    computed: {
        updatedColumns() {
            return [...this.necessaryHeaders, ...this.selectedColumns, ...this.actions];
        },
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

        this.loggedUserUsername = this.$store.getters.userData.username;

        this.getRestaurants();


    },


    created() {
        this.selectedColumns = this.DriverHeaders.filter(column =>
            ['restaurant_name', 'email', 'is_active'].includes(column.key)
        );

        this.avaliableColumns = this.DriverHeaders;
    },



    methods: {
        async loadUsers(url) {
            this.loading = true;

            try {
                const response = url
                    ? await axios.get(url)
                    : await axios.get('api/drivers/get/all/', {
                        params: {
                            limit: this.itemsPerPage,
                            search: this.query,
                            status: this.selectedActive,
                            restaurant: this.selectedRestaurant,
                        }
                    });

                this.pagiController = {
                    total_pages: response.data.total_pages,
                    posts_amount: response.data.posts_amount,
                    next: response.data.next,
                    previous: response.data.previous,
                    currentPage: response.data.current_page,
                    totalRecors: response.data.total_results,
                }

                this.users = response.data.results;

                // Add number for each row
                this.users.forEach((user, index) => {
                    user.rownumber = index + 1;
                });

            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }
            this.loading = false;
        },

        // Previous page
        async prevPage() {
            await this.loadUsers(this.pagiController.previous);
        },
        // Previous page

        // Next page
        async nextPage() {
            await this.loadUsers(this.pagiController.next);
        },
        // Next page


        // Get restaurants
        async getRestaurants() {
            try {
                const response = await axios.get('api/rest_manager/get_restaurants/', {
                    params: {
                        username: this.loggedUserUsername,
                    }
                });

                this.avaliableRestaurants = response.data.map(restaurant => restaurant.name);

            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }
        },
        // Get restaurants


        copyElement(content) {
            const textarea = document.createElement('textarea');
            textarea.value = content;
            textarea.style.position = 'fixed';
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand('copy');
            document.body.removeChild(textarea);
        },


        chooseStatus(status) {
            this.selectedActive = status;
            this.reloadComponent();
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
            this.$store.dispatch('triggerAlert', { message: `Successfully changed state of ${username}`, type: 'success' });

        },

        async userDetails(username, role) {
            try {
                const response = await axios.get(`api/users/get/${username}/${role}/`);
                this.userDetailData = {};
                Object.keys(response.data).forEach(key => {
                    let formattedKey = key.replace(/_/g, ' ');
                    formattedKey = formattedKey.replace(/\b\w/g, firstChar => firstChar.toUpperCase());
                    this.userDetailData[formattedKey] = response.data[key];
                });
                this.UserDetailsDialog = true;
            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }

        },


    },

};
</script>
