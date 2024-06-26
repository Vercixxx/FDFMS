<template>
    <div>

        <div class="mt-5 mb-5">


            <!-- Search bar section -->
            <v-row>

                <v-col cols="12" sm="12">
                    <v-expansion-panels>
                        <v-expansion-panel title="Filters" elevation="1" style="border: 1px solid teal;">

                            <v-expansion-panel-text>
                                <v-row justify="center" align="center">

                                    <v-col cols="12" sm="4">
                                        <v-autocomplete v-model="selectedRestaurant" :items="restaurants" item-title="name"
                                            item-value="id" label="Select restaurant" prepend-icon="mdi-store"
                                            @update:model-value="loadUsers()">

                                            <template v-slot:item="{ props, item }">
                                                <v-list-item v-bind="props" :title="item.raw.name"
                                                    :subtitle="item.raw.id == 'All' ? '' : `Restaurant id - ${item.raw.id}`"></v-list-item>
                                            </template>

                                        </v-autocomplete>
                                    </v-col>

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
                                                    <v-list-item-title role="button" @click="chooseStatus(option.property)">
                                                        {{ option.name }}
                                                    </v-list-item-title>
                                                </v-list-item>
                                            </v-list>
                                        </v-menu>
                                        <!-- User status -->
                                    </v-col>

                                    <v-col cols="auto">
                                        <v-combobox variant="outlined" v-model="selectedColumns" :items="avaliableColumns"
                                            label="Select columns" prepend-icon="mdi-table-edit" multiple chips>
                                        </v-combobox>
                                    </v-col>

                                    <v-col cols="12" sm="2">
                                        <v-select v-model="itemsPerPage" variant="solo-filled" :items="[5, 10, 25, 50, 100]"
                                            :label="`Items per page - ${itemsPerPage}`"
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
                    Users
                </div>
            </v-col>
            <v-col justify="end" cols="12" sm="4">

                <!-- Search bar -->
                <v-text-field variant="solo-filled" v-model="query" @keydown.enter="loadUsers()" label="Search"
                    class="px-1 " prepend-inner-icon="mdi-magnify" hide-actions clearable hint="Press enter to search" />
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
                    No data
                </p>
            </template>
            <!-- No data -->

            <!-- Loading -->
            <template v-slot:loading>
                <v-skeleton-loader type="table-row@10"></v-skeleton-loader>
            </template>
            <!-- Loading -->



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

                                <v-btn variant="plain" color="green" @click="assignTariff(item)">
                                    <v-icon icon="mdi-cash-edit" class="text-h5"></v-icon>
                                    <v-tooltip activator="parent" location="top">Assign tariff for {{ item.username
                                    }}</v-tooltip>
                                </v-btn>

                                <v-btn variant="plain" color="error" @click="goToReports(item)">
                                    <v-icon icon="mdi-file-chart" class="text-h5"></v-icon>
                                    <v-tooltip activator="parent" location="top">Reports for {{ item.username }}</v-tooltip>
                                </v-btn>

                            </span>
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



        <!-- Dialaogs section -->

        <!-- Tariff -->
        <v-dialog persistent v-model="tariffDialog" transition="dialog-bottom-transition">
            <v-card>
                <v-card-title class="bg-deep-purple-lighten-1">
                    <v-row>
                        <v-col class="text-h5">
                            Assign tariff for {{ tariffUser }}
                        </v-col>
                        <v-col align="end">
                            <v-btn variant="outlined" color="red" @click="tariffDialog = false" icon="mdi-close">
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-card-title>

                <v-card-text>
                    <v-form v-model="form">

                        <v-row>
                            <v-col cols="12" sm="12">
                                <v-select :items="tariffs" v-model="selectedTariff" label="Select tariff"
                                    :rules="fieldRequired" variant="outlined" no-data-text="There aren't any tariffs yet"
                                    item-title="name" item-value="id">

                                    <template v-slot:item="{ props, item }">
                                        <v-list-item v-bind="props"
                                            :subtitle="'Basic hourly wage - ' + item.raw.basic_hourly_rate + ',  ' + 'Orders bouns - ' + item.raw.orders_bonus + ',  ' + 'Fuel bouns - ' + item.raw.fuel_bonus"></v-list-item>
                                    </template>

                                </v-select>
                            </v-col>
                        </v-row>
                    </v-form>
                </v-card-text>

                <v-card-actions>
                    <v-btn color="success" block @click="saveTariff(tariffUser)" :disabled="!form">Assign</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <!-- Tariff -->


        <!-- dialog -->
        <v-dialog v-model="UserDetailsDialog" width="auto">
            <v-card>
                <v-card-text>
                    <v-row>
                        <v-col cols="3">
                        </v-col>
                        <v-col cols="6" sm="6">
                            <div class="text-h5 text-center">
                                User details
                            </div>
                        </v-col>
                        <!-- Download -->
                        <v-col cols="3" align="end">
                            <span>
                                <v-btn icon="mdi-download" variant="pain"
                                    @click="downloadUserInfo(userDetailData['Username'], userDetailData['User Role'])">
                                </v-btn>
                                <v-tooltip activator="parent" location="top">Download user info</v-tooltip>
                            </span>
                        </v-col>
                        <!-- Download -->
                    </v-row>

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
            loading: true,
            users: [],

            itemsPerPage: 10,
            paginationPage: 1,
            pagiController: {},
            query: '',

            restaurants: [
                { name: 'All', id: 'All' },
            ],
            selectedRestaurant: 'All',

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

            tariffDialog: false,
            tariffUser: null,
            selectedTariff: null,
            tariffs: [],

            form: false,
            fieldRequired: [v => !!v || 'Field is required',],

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
                { title: 'RESTAURANT', align: 'center', key: 'restaurant_name', sortable: true },
                { title: 'Tariff', align: 'center', key: 'wage_tariff', sortable: true },
            ],

            actions: [
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

        this.loadUsers();

        this.getRestaurants();

        this.getTariffs();


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

            let restaurant = this.selectedRestaurant === 'All' ? null : this.restaurants.find(restaurant => restaurant.id === this.selectedRestaurant);
            if (restaurant) restaurant = restaurant.name;

            try {
                const response = url
                    ? await axios.get(url)
                    : await axios.get('api/drivers/get/all/', {
                        params: {
                            limit: this.itemsPerPage,
                            search: this.query,
                            status: this.selectedActive,
                            restaurant: restaurant,
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


        // Get all restaurants
        async getRestaurants() {
            try {
                const response = await axios.get('api/restaurant/get/name-id/');
                this.restaurants.push(...response.data);
            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }
        },
        // Get all restaurants


        // Go to reports
        async goToReports(user) {
            try {
                const tariff = await this.getNewBillingPeriodStartDay(user.wage_tariff)
                
                const data = {
                    username: user.username,
                    first_name: user.first_name,
                    last_name: user.last_name,
                    user_role: 'driver',
                    tariff_name: tariff.name,
                    tariff_starting_day: tariff.starting_new_billing_period,
                }
                this.$store.dispatch('setBusData', data);
                this.$root.changeCurrentComponent('DriverReportsComponent');
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }
        },
        // Go to reports

        // Get new billing period start day
        async getNewBillingPeriodStartDay(tariffName) {
            try {
                const response = await axios.get(`api/drivers/wage_tariff/get/new_billing_period/${tariffName}/`);
                return response.data;
            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error.response.error, type: 'error' });
            }
        },
        // Get new billing period start day


        // Assign tariff
        assignTariff(user) {
            this.tariffUser = user.username;
            this.selectedTariff = user.wage_tariff;
            this.tariffDialog = true;
        },
        // Assign tariff


        // Download user info
        async downloadUserInfo(username, role) {
            try {
                const response = await axios.get(`api/users/get-info-csv/${username}/${role}/`);
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', `${username}_info.csv`);
                document.body.appendChild(link);
                link.click();
            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }
        },
        // Download user info


        // Fetch tariffs
        async getTariffs() {
            try {
                const response = await axios.get('api/drivers/wage_tariff/get/all/');
                this.tariffs = response.data;
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error.response.data, type: 'error' });
            }
        },
        // Fetch tariffs


        // Save tariff
        async saveTariff(username) {
            try {
                const response = await axios.post(`api/drivers/wage_tariff/assign/${username}/`, {
                    wage_tariff: this.selectedTariff,
                });
                this.$store.dispatch('triggerAlert', { message: response.data, type: 'success' });
                this.tariffDialog = false;
                this.loadUsers();
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error.response.data, type: 'error' });
            }
        },
        // Save tariff


    },

};
</script>
  