<template>
    <div>

        <v-card elevation="1" class="pa-5 rounded-xl" color="teal-darken-2">

            <p class="p-2 fw-bolder text-h4">Options</p>

            <v-row>
                <v-col cols="4">

                    <v-btn id="role-activator" variant="tonal" class="rounded-xl rounded-0 bg-teal-darken-4">
                        <span class="pr-2">City - </span>
                        {{ selectedCity }}

                        <v-icon icon="mdi-menu-down"></v-icon>
                    </v-btn>

                    <v-menu activator="#role-activator" transition="slide-y-transition">
                        <v-list>
                            <v-list-item v-for="option in availableCities" :value="option" @click="selectCity(option)">
                                {{ option }}
                            </v-list-item>
                        </v-list>
                    </v-menu>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="5">
                    <!-- Combobox columns selection -->

                    <v-expansion-panels>
                        <v-expansion-panel title="Choose columns" elevation="1">

                            <v-expansion-panel-text>

                                <v-combobox variant="outlined" v-model="selectedColumns" :items="avaliableColumns"
                                    label="Select columns" prepend-icon="mdi-table-edit" multiple chips>

                                </v-combobox>
                            </v-expansion-panel-text>

                        </v-expansion-panel>
                    </v-expansion-panels>

                    <!-- Combobox columns selection -->
                </v-col>

                <v-col cols="2">

                </v-col>

                <v-col cols="5">
                    <!-- Search bar -->
                    <v-text-field variant="solo-filled" v-model="searchInput" @keydown.enter="searchTable = searchInput"
                        label="Search" class="px-1 " prepend-inner-icon="mdi-magnify" hide-actions clearable
                        hint="Press enter to search" />
                    <!-- Search bar -->
                </v-col>
            </v-row>

        </v-card>


        <v-divider thickness="12" class="rounded-xl my-7"></v-divider>


        <div class="text-h4 ma-5 font-weight-bold">
            Restaurants
        </div>


        <!-- Table -->
        <v-data-table :headers="updatedColumns" :items="restaurants" :search="searchTable" :loading="tableLoading"
            class="elevation-4 rounded-xl" item-value="id" v-model:items-per-page="itemsPerPage" hover select-strategy="all"
            show-current-page>



            <!-- No data -->
            <template v-slot:no-data>
                <p class="text-h4 pa-5">
                    <v-icon icon="mdi-database-alert-outline" color="red"></v-icon>
                    No data
                </p>
            </template>
            <!-- No data -->



            <!-- Accessing table cells -->
            <template v-slot:item="{ item }">
                <tr align="center">
                    <td v-for="header in updatedColumns" :key="header.key">

                        <template v-if="header.key === 'action'">
                            <span>
                                <v-btn variant="plain" color="blue" @click="restaurantDetailsFunct(item.id)">
                                    <v-icon icon="mdi-book-open-page-variant-outline" class="text-h5"></v-icon>
                                    <v-tooltip activator="parent" location="top">Show {{ item.name }}
                                        details</v-tooltip>
                                </v-btn>

                                <v-btn variant="plain" color="green" @click="editRestaurant(item.id)">
                                    <v-icon icon="mdi-pencil-outline" class="text-h5"></v-icon>
                                    <v-tooltip activator="parent" location="top">Edit {{ item.name }}</v-tooltip>
                                </v-btn>

                                <v-btn variant="plain" color="red" @click="deleteConfirm(item.name, item.id)">
                                    <v-icon icon="mdi-delete-empty" class="text-h5"></v-icon>
                                    <v-tooltip activator="parent" location="top">Delete {{ item.name }}</v-tooltip>
                                </v-btn>
                            </span>
                        </template>


                        <template v-else>
                            <span v-if="item[header.key] === null || item[header.key] === ''">
                                <v-icon icon="mdi-minus-thick" color="red-lighten-2" />
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

        </v-data-table>
        <!-- Table -->


    </div>

    <!-- Dialaogs section -->

    <!-- Delete car confirm -->
    <v-dialog v-model="dialogDelete" width="400">
        <v-card>
            <div class="text-danger text-h6 text-md-h5 text-lg-h4">
                <div class="d-flex justify-content-between align-items-center px-4 pt-4">
                    <v-icon icon="mdi-alert" class="text-h4" />
                    Warning
                    <v-icon icon="mdi-alert" class="text-h4" />
                </div>

                <hr />
            </div>

            <div class="pa-3" align="center">

                You are trying to delete
                <span class='fw-bolder'>
                    {{ deleteRestName }}
                </span>
                , this operation is <span class="fw-bold">irreversible</span>.
                Are you sure?

            </div>
            <hr>

            <div class="justify-center d-flex align-items-center mb-3">
                <v-btn variant="outlined" width="150" class="mr-5" @click="dialogDelete = false">No</v-btn>
                <v-btn width="150" @click="deleteRestaurant(deleteRestId)" color="red">
                    <v-icon icon="mdi-delete-empty"></v-icon>
                    Yes
                </v-btn>
            </div>

        </v-card>
    </v-dialog>
    <!-- Delete car confirm -->


    <!-- Dialog details -->
    <v-dialog v-model="restaurantDetailsDialog" width="auto">
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
                        <tr v-for="(value, key) in restaurantDetails" :key="key">
                            <td>{{ key }}</td>
                            <td v-if="value === null">
                                <v-icon icon="mdi-minus-thick"></v-icon>
                            </td>

                            <td v-else-if="value === ''">
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
                <v-btn color="primary" block @click="restaurantDetailsDialog = false">Close</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
    <!-- dialog -->

    <!-- Dialog details -->
</template>


<script>
import axios from 'axios';
import useEventsBus from '../../plugins/eventBus.js'
const { emit } = useEventsBus()


export default {
    name: 'App',

    data() {
        return {
            selectedCity: 'All',
            availableCities: [],

            restaurants: [],
            itemsPerPage: 25,
            columns: [],
            searchInput: '',
            searchTable: '',
            tableLoading: false,
            selectedColumns: [],
            avaliableColumns: [],

            dialogDelete: false,
            deleteRestId: '',
            deleteRestName: '',

            restaurantDetailsDialog: false,
            restaurantDetails: [],


            // Headers
            necessaryHeaders: [
                { title: 'Id', align: 'center', sortable: true, key: 'id' },
            ],
            columns: [
                { title: 'Name', key: 'name', align: 'center', sortable: true },
                { title: 'Brand', key: 'brand', align: 'center', sortable: false },
                { title: 'Phone', key: 'phone', align: 'center', sortable: false },
                { title: 'Country', key: 'country', align: 'center', sortable: false },
                { title: 'State', key: 'state', align: 'center', sortable: false },
                { title: 'City', key: 'city', align: 'center', sortable: true },
                { title: 'Street', key: 'street', align: 'center', sortable: false },
                { title: 'Home', key: 'home', align: 'center', sortable: false },
                { title: 'Apartament', key: 'apartament', align: 'center', sortable: false },
                { title: 'Zip code', key: 'zip', align: 'center', sortable: false },
            ],
            actions: [
                { title: 'ACTIONS', align: 'center', key: 'action', sortable: false },
            ],
            // Headers

        }
    },



    computed: {
        updatedColumns() {
            return [...this.necessaryHeaders, ...this.selectedColumns, ...this.actions];
        },
    },



    created() {
        this.loadRestaurants();
        this.getCities()

        this.selectedColumns = this.columns;
        this.avaliableColumns = this.columns;
    },



    methods: {

        // Load all Restaurants
        async loadRestaurants() {
            try {
                const response = await axios.get(`api/restaurants/get/${this.selectedCity}/`);
                this.restaurants = response.data;
                this.tableLoading = false;
            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }

        },
        // Load all Restaurants



        // Get cities
        async getCities() {
            const response = await axios.get('api/restaurants/unique_cities/');
            this.availableCities = ['All', ...response.data];
        },
        // Get cities



        // Select city
        selectCity(city) {
            this.selectedCity = city;
            this.loadRestaurants();
        },
        // Select city



        // Deleting Restaurant confirmation
        deleteConfirm(restName, restId) {
            this.deleteRestName = restName;
            this.deleteRestId = restId;
            this.dialogDelete = true;
        },
        // Deleting Restaurant confirmation



        // Deleting Restaurant method
        async deleteRestaurant() {
            this.dialogDelete = false;
            try {
                const response = await axios.delete(`api/restaurant/delete/${this.deleteRestId}`);
                this.$store.dispatch('triggerAlert', { message: `Successfully deleted ${this.deleteRestName}`, type: 'success' });
                this.loadRestaurants();

            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
        },
        // Deleting Restaurant method



        // Editing Restaurant
        editRestaurant(restaurantID) {
            localStorage.setItem('restaurantID', restaurantID);
            this.$root.changeCurrentComponent('AddRestaurantComponent');
        },
        // Editing Restaurant



        // Restaurant details
        async restaurantDetailsFunct(restaurantID) {
            const response = await axios.get(`api/restaurant/get/${restaurantID}/`);
            this.restaurantDetails = response.data;
            this.restaurantDetailsDialog = true;

        },
        // Restaurant details


    },

}
</script>