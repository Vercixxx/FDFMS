<template>
    <div class="containter m-2 p-2 d-flex justify-content-center">
        <div class="col-12 col-md-9">


            <v-btn v-if="editing" @click="goBack" prepend-icon="mdi-undo" color="danger"
                :variant="theme ? undefined : 'outlined'">
                Back
            </v-btn>

            <div class="d-flex justify-center mb-5">
                <div v-if="!editing" class="text-h6 text-md-h5 text-lg-h4 fw-bold">
                    <v-icon icon="mdi-silverware-fork-knife"></v-icon>
                    Add Restaurant
                </div>
                <div v-else class="text-h6 text-md-h5 text-lg-h4">
                    <v-icon icon="mdi-silverware-fork-knife"></v-icon>
                    Edit {{ editRest.name }}
                </div>
            </div>

            <v-form v-model="form" @submit.prevent="onSubmit">
                <v-container class=" mb-5  rounded-xl elevation-5"
                    :class="{ 'bg-green-lighten-5': !theme, 'bg-grey-darken-4': theme }">

                    <div class="fw-light">
                        <v-icon icon="mdi-star" color="red" style="font-size:medium;"></v-icon> - field required
                    </div>



                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mt-10' : 'border-opacity-50 rounded-xl mt-10'"
                        :color="theme ? '' : 'info'"></v-divider>
                    <p align="center" class="text-h4 text-md-h5 text-lg-h5">Basic info</p>
                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mb-10' : 'border-opacity-50 rounded-xl mb-10'"
                        :color="theme ? '' : 'info'"></v-divider>


                    <v-row>
                        <v-col cols="12" sm="6" v-for="input in basicInfoInputs" :key="input.name">
                            <v-text-field variant="outlined" v-model="input_data[input.model]" :label="input.name"
                                :readonly="input.readonly || false" :hint="input.hint || undefined" :rules="input.rules">

                                <!-- Icons -->
                                <template v-slot:append-inner>
                                    <v-icon v-if="input.required" icon="mdi-star" color="red"
                                        style="font-size:medium; position: absolute; top:3px; right: 3px;"></v-icon>
                                    <v-icon v-if="input.icon" class="icon" style="opacity: 0.4;">{{ input.icon }}</v-icon>
                                </template>
                                <!-- Icons -->

                            </v-text-field>
                        </v-col>

                        <v-col cols="12" sm="6">
                            <v-autocomplete label="Brand" :items="availableBrands" variant="outlined"
                                v-model="selectedBrand" :rules="fieldRequired">

                                <!-- Icons -->
                                <template v-slot:append-inner>
                                    <v-icon icon="mdi-star" color="red"
                                        style="font-size:medium; position: absolute; top:3px; right: 3px;"></v-icon>
                                </template>
                                <!-- Icons -->

                            </v-autocomplete>
                        </v-col>
                    </v-row>


                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mt-10' : 'border-opacity-50 rounded-xl mt-10'"
                        :color="theme ? '' : 'info'"></v-divider>
                    <p align="center" class="text-h4 text-md-h5 text-lg-h5">Address</p>
                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mb-10' : 'border-opacity-50 rounded-xl mb-10'"
                        :color="theme ? '' : 'info'"></v-divider>

                    <v-row>

                        <!-- Country and State -->
                        <v-col cols="12" sm="6">
                            <v-autocomplete label="Country" :items="allCountries" variant="outlined"
                                v-model="selectedCountry" @update:search="getStates('residence')" :rules="fieldRequired">

                                <!-- Icons -->
                                <template v-slot:append-inner>
                                    <v-icon icon="mdi-star" color="red"
                                        style="font-size:medium; position: absolute; top:3px; right: 3px;"></v-icon>
                                </template>
                                <!-- Icons -->

                            </v-autocomplete>
                        </v-col>

                        <v-col cols="12" sm="6">
                            <v-autocomplete label="State" :items="allStates" variant="outlined" v-model="selectedState"
                                :disabled="selectedCountry === null" :rules="fieldRequired">

                                <!-- Icons -->
                                <template v-slot:append-inner>
                                    <v-icon icon="mdi-star" color="red"
                                        style="font-size:medium; position: absolute; top:3px; right: 3px;"></v-icon>
                                </template>
                                <!-- Icons -->

                            </v-autocomplete>

                        </v-col>
                        <!-- Country and State -->

                        <v-col cols="12" sm="6" v-for="input in residenceAddress" :key="input.name">

                            <v-text-field variant="outlined" v-model="input_data[input.model]" :label="input.name"
                                :readonly="input.readonly || false" :hint="input.hint || undefined" :rules="input.rules">

                                <!-- Icons -->
                                <template v-slot:append-inner>
                                    <v-icon v-if="input.required" icon="mdi-star" color="red"
                                        style="font-size:medium; position: absolute; top:3px; right: 3px;"></v-icon>
                                    <v-icon v-if="input.icon" class="icon" style="opacity: 0.4;">{{ input.icon }}</v-icon>
                                </template>
                                <!-- Icons -->

                            </v-text-field>

                        </v-col>
                    </v-row>




                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mt-10' : 'border-opacity-50 rounded-xl mt-10'"
                        :color="theme ? '' : 'info'"></v-divider>
                    <p align="center" class="text-h4 text-md-h5 text-lg-h5">Managers</p>
                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mb-10' : 'border-opacity-50 rounded-xl mb-10'"
                        :color="theme ? '' : 'info'"></v-divider>



                    <!-- Managers -->

                    <v-row>
                        <v-col cols="12" sm="12">
                            <v-text-field variant="solo-filled" v-model="query" @keydown.enter="getManagers()"
                                label="Search" class="px-1 " prepend-inner-icon="mdi-magnify" hide-actions
                                hint="Press enter to search" @keydown.enter.prevent />
                        </v-col>
                    </v-row>

                    <v-row>
                        <v-col cols="12" sm="6" align="center">


                            <p class="text-h4 text-md-h5 text-lg-h5">Available managers</p>

                            <!-- Available managers -->
                            <v-data-table :headers="tableHeaders" :items="availableManagers" :loading="loading"
                                v-model:items-per-page="itemsPerPage" hover  density="compact" class="border">

                                <!-- Loading -->
                                <template v-slot:loading>
                                    <v-skeleton-loader type="table-row@10"></v-skeleton-loader>
                                </template>
                                <!-- Loading -->


                                <!-- No data -->
                                <template v-slot:no-data>
                                    <p class="text-h6 pa-5 text-danger">
                                        <v-icon icon="mdi-database-alert-outline"></v-icon>
                                        No available managers
                                    </p>
                                </template>
                                <!-- No data -->


                                <template v-slot:item="{ item }">
                                    <tr align="center" @click="selectUser(item)" role="button">
                                        <v-tooltip v-if="!form" activator="parent" location="top" no-overflow>
                                            Click to select
                                        </v-tooltip>
                                        <td v-for="header in tableHeaders" :key="header.key">
                                            {{ item }}
                                        </td>
                                    </tr>
                                </template>


                            </v-data-table>
                            <!-- Available managers -->


                        </v-col>

                        <v-col cols="12" sm="6" align="center">

                            <p align="center" class="text-h4 text-md-h5 text-lg-h5">Selected managers</p>


                            <!-- Selected managers -->
                            <v-data-table :headers="tableHeaders" :items="selectedManagers" :search="query"
                                v-model:items-per-page="itemsPerPage" hover select-strategy="all" show-current-page  density="compact" class="border">

                                <!-- Loading -->
                                <template v-slot:loading>
                                    <v-skeleton-loader type="table-row@10"></v-skeleton-loader>
                                </template>
                                <!-- Loading -->

                                <!-- No data -->
                                <template v-slot:no-data>
                                    <p class="text-h6 pa-5 text-danger">
                                        <v-icon icon="mdi-database-alert-outline"></v-icon>
                                        No selected managers
                                    </p>
                                </template>
                                <!-- No data -->

                                <template v-slot:item="{ item }">
                                    <tr align="center" @click="unselectUser(item)" role="button">
                                        <v-tooltip v-if="!form" activator="parent" location="top" no-overflow>
                                            Click to unselect
                                        </v-tooltip>
                                        <td v-for="header in tableHeaders" :key="header.key">
                                            {{ item }}
                                        </td>
                                    </tr>
                                </template>

                            </v-data-table>
                            <!-- Selected managers -->



                        </v-col>
                    </v-row>
                    <!-- Managers -->



                    <!-- Drivers -->
                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mt-10' : 'border-opacity-50 rounded-xl mt-10'"
                        :color="theme ? '' : 'info'"></v-divider>
                    <p align="center" class="text-h4 text-md-h5 text-lg-h5">Drivers</p>
                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mb-10' : 'border-opacity-50 rounded-xl mb-10'"
                        :color="theme ? '' : 'info'"></v-divider>


                    <v-row>
                        <v-col cols="12" sm="12">
                            <v-text-field variant="solo-filled" v-model="driversQuery" label="Search in users"
                                hint="Click enter to serach" clearable hide-actions @keydown.enter="getDrivers()"
                                @keydown.enter.prevent></v-text-field>
                        </v-col>
                    </v-row>

                    <v-row>
                        <!-- Available -->
                        <v-col cols="12" sm="6">
                            <h5 justify="center" align="center">Available drivers</h5>
                            <v-data-table :headers="tableHeaders" :items="avaiableDrivers" density="compact"
                                :loading="driversLoading" hover class="border">

                                <!-- Loading -->
                                <template v-slot:loading>
                                    <v-skeleton-loader type="table-row@10"></v-skeleton-loader>
                                </template>
                                <!-- Loading -->

                                <!-- No data -->
                                <template v-slot:no-data>
                                    <p class="text-h6 pa-5 text-danger">
                                        <v-icon icon="mdi-database-alert-outline"></v-icon>
                                        No available drivers
                                    </p>
                                </template>
                                <!-- No data -->


                                <template v-slot:item="{ item }">
                                    <tr align="center" @click="selectDriver(item.username)" role="button">
                                        <v-tooltip activator="parent" location="top" no-overflow>
                                            Click to select
                                        </v-tooltip>

                                        <td v-for="header in tableHeaders" :key="header.key">
                                            {{ item[header.key] }}
                                        </td>
                                    </tr>
                                </template>

                            </v-data-table>
                        </v-col>
                        <!-- Available -->



                        <!-- Selected -->
                        <v-col cols="12" sm="6">
                            <h5 justify="center" align="center">Selected drivers </h5>
                            <v-data-table :headers="tableHeaders" :items="selectedDrivers" density="compact"
                                :search="driversQuery" hover  class="border">

                                <!-- Loading -->
                                <template v-slot:loading>
                                    <v-skeleton-loader type="table-row@10"></v-skeleton-loader>
                                </template>
                                <!-- Loading -->

                                <!-- No data -->
                                <template v-slot:no-data>
                                    <p class="text-h6 pa-5 text-danger">
                                        <v-icon icon="mdi-database-alert-outline"></v-icon>
                                        No available drivers
                                    </p>
                                </template>
                                <!-- No data -->


                                <template v-slot:item="{ item }">
                                    <tr align="center" @click="unselectDriver(item.username)" role="button">
                                        <v-tooltip activator="parent" location="top" no-overflow>
                                            Click to unselect
                                        </v-tooltip>
                                        <td v-for="header in tableHeaders" :key="header.key">
                                            {{ item[header.key] }}
                                        </td>
                                    </tr>
                                </template>

                            </v-data-table>
                        </v-col>
                        <!-- Selected -->

                    </v-row>
                    <!-- Drivers -->



                    <v-row>
                        <v-col align="center">

                            <!-- Button submit -->
                            <span v-if="!editing">
                                <v-tooltip v-if="!form" activator="parent" location="top" no-overflow>
                                    Fill all required fields first
                                </v-tooltip>
                                <span>
                                    <v-btn :disabled="!form" :loading="loading" :color="!form ? 'danger' : 'success'"
                                        size="large" type="submit" class="mt-10 mb-5 font-weight-black" block>
                                        Create
                                    </v-btn>
                                </span>
                            </span>
                            <!-- Button submit -->

                            <!-- Button submit when editing -->
                            <span v-else>
                                <v-tooltip v-if="!form" activator="parent" location="top" no-overflow>
                                    Fill all required fields first
                                </v-tooltip>
                                <span>
                                    <v-btn :disabled="!form" :loading="loading" :color="!form ? 'danger' : 'success'"
                                        size="large" type="submit" class="mt-10 mb-5 font-weight-black" block>
                                        Save
                                    </v-btn>
                                </span>
                            </span>
                            <!-- Button submit when editing -->
                        </v-col>
                    </v-row>

                </v-container>
            </v-form>

        </div>
    </div>
</template>



<script>
import axios from 'axios';
import useEventsBus from '../../plugins/eventBus.js'
import { watch } from "vue";
import { useTheme } from 'vuetify'


export default {
    data() {
        return {
            theme: true,
            form: false,
            loading: true,
            editing: false,
            restId: null,
            editRest: {},

            input_data: {},

            availableBrands: [],
            selectedBrand: null,

            // Country, state
            allCountries: [],
            allStates: [],
            selectedCountry: null,
            selectedState: null,

            // Managers
            availableManagers: [],
            selectedManagers: [],

            itemsPerPage: 5,
            tableHeaders: [
                { title: 'Username', key: 'username', align: 'center', sortable: false },
            ],
            // Managers


            // Drivers
            allDrivers: [],
            avaiableDrivers: [],
            selectedDrivers: [],
            driversQuery: '',
            driversLoading: true,
            // Drivers

            // Search
            query: '',
            searchTableSelected: '',

            // Inputs definisions
            basicInfoInputs: [
                {
                    name: 'Name',
                    model: 'name',
                    required: true,
                    icon: 'mdi-account',
                    rules: [
                        v => !!v || 'Name is required',
                        v => /^[a-zA-Z0-9 -]+$/.test(v) || 'Only numbers, letters and "-" are allowed',
                    ]

                },
                {
                    name: 'Phone number',
                    model: 'phone',
                    required: true,
                    icon: 'mdi-phone',
                    rules: [
                        v => !!v || 'Phone number is required',
                        v => /^[0-9]+$/.test(v) || 'Only digits are allowed',
                        v => v.length >= 9 || 'Phone number must be at least 9 digits',
                        v => v.length <= 15 || 'Phone number must not exceed 15 digits',
                    ]

                },
            ],

            residenceAddress: [
                {
                    name: 'City',
                    model: 'city',
                    required: true,
                    icon: 'mdi-map-marker',
                    rules: [
                        v => !!v || 'City is required',
                        v => (v.length >= 3) || 'City name must containt at least 3 characters',
                        v => /^[a-zA-Z-]+$/.test(v) || 'City can only contain letters',
                    ]
                },
                {
                    name: 'Street',
                    model: 'street',
                    required: true,
                    icon: 'mdi-map-marker',
                    rules: [
                        v => !!v || 'Street is required',
                        v => /^[a-zA-Z0-9 -]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Home',
                    model: 'home',
                    required: true,
                    icon: 'mdi-home',
                    rules: [
                        v => !!v || 'Home is required',
                        v => /^[a-zA-Z0-9]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Apartament',
                    model: 'apartament',
                    icon: 'mdi-home',
                    rules: [
                        v => /^[a-zA-Z0-9-]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Zip code',
                    model: 'zip',
                    required: true,
                    icon: 'mdi-earth',
                    rules: [
                        v => !!v || 'Zip code is required',
                        v => /^[0-9-]+$/.test(v) || 'Only numbers and "-" are allowed',
                    ]
                },
            ],
        }
    },

    computed: {
        allInputs() {
            return [...this.basicInfoInputs, ...this.residenceAddress];
        },
        avaiableDrivers() {
            const selectedUsers = this.selectedDrivers.map(user => user.username);
            return this.allDrivers.filter(user => !selectedUsers.includes(user.username));
        },
    },


    mounted() {


        // Check for editing or creating
        this.restId = localStorage.getItem('restaurantID')

        if (this.restId !== null) {
            this.getRestInfo();
            localStorage.removeItem('restaurantID');
            this.editing = true;
        }


        // Dark mode
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

        // Get managers
        this.getManagers();

        // Get Drivers
        this.getDrivers();

        // Get brands
        this.loadBrands();

        // Get countries
        this.getCountries();

    },

    methods: {
        // On submit behavior
        onSubmit() {
            if (!this.form) return;

            this.loading = true;

            if (!this.editing) {
                this.createRestaurant();
            }
            else {
                this.updateRestaurant();
            }
        },
        // On submit behavior



        // Getting data from inputs
        getDataFromInputs() {
            for (const field of this.allInputs) {
                if (typeof this.input_data[field.model] === 'string') {
                    this.input_data[field.model] = this.input_data[field.model].trim();
                }
                if (!this.input_data[field.model]) {
                    this.input_data[field.model] = null;
                }
            }

            // Adding country, state and choosen managers
            this.input_data['country'] = this.selectedCountry;
            this.input_data['state'] = this.selectedState;
            this.input_data['managers'] = this.selectedManagers;
            this.input_data['brand'] = this.selectedBrand;

            // Add drivers
            this.input_data['drivers'] = this.selectedDrivers.map(driver => driver.username);

        },
        // Getting data from inputs



        // Get restaurant info
        async getRestInfo() {
            try {
                const response = await axios.get(`api/restaurant/get/${this.restId}/`);
                this.editRest = response.data;


                for (const field of this.allInputs) {
                    this.input_data[field.model] = this.editRest[field.model];
                }

                this.selectedCountry = this.editRest['country'];
                this.selectedState = this.editRest['state'];
                this.selectedManagers = this.editRest['managers'];
                this.selectedBrand = this.editRest['brand_name']

                this.selectedDrivers = this.editRest['drivers'].map(driver => {
                    return { username: driver };
                });
            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
        },
        // Get restaurant info



        // Country
        async getCountries() {
            const response = await axios.get("api/countries/get/");
            this.allCountries = response.data.map(country => country.name);
        },
        // Country



        // State
        async getStates(country) {
            const response = await axios.get(`api/states/get/?country=${this.selectedCountry}`);
            this.allStates = response.data.map(state => state.name)
        },
        // State



        // Move user to selected
        selectUser(username) {
            const userIndex = this.availableManagers.findIndex(user => user === username);

            if (userIndex !== -1) {
                const selectedUser = this.availableManagers.splice(userIndex, 1)[0];
                this.selectedManagers.push(selectedUser);
            }
        },
        // Move user to selected



        // Move user to unselected
        unselectUser(username) {
            const userIndex = this.selectedManagers.findIndex(user => user === username);
            if (userIndex !== -1) {
                const unselectedUser = this.selectedManagers.splice(userIndex, 1)[0];
                this.availableManagers.push(unselectedUser);
            }
        },
        // Move user to unselected



        // Load all brands
        async loadBrands() {
            try {
                const response = await axios.get('api/brands/get-all/');
                this.availableBrands = response.data.results.map(item => item.name);
            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
        },
        // Load all brands



        // Get all managers
        async getManagers() {

            this.loading = true;

            try {
                const response = await axios.get('api/users/get-usernames/', {
                    params: {
                        role: 'Manager',
                        search: this.query,
                    }
                });

                this.availableManagers = response.data.map(user => user.username);
                this.availableManagers = this.availableManagers.filter(username => !this.selectedManagers.includes(username));


            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            };

            this.loading = false;

        },
        // Get all managers



        // Get all Drivers
        async getDrivers() {

            this.driversLoading = true;

            try {
                const response = await axios.get('api/users/get-usernames/', {
                    params: {
                        role: 'Driver',
                        search: this.driversQuery,
                    }
                });

                this.allDrivers = response.data;

            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            };

            this.driversLoading = false;

        },
        // Get all Drivers


        // Drivers selecting and unselecting
        selectDriver(username) {
            const userIndex = this.allDrivers.findIndex(user => user.username === username);

            if (userIndex !== -1) {
                const selectedUser = this.allDrivers[userIndex];
                this.selectedDrivers.push(selectedUser);
            }
        },

        unselectDriver(username) {
            const userIndex = this.selectedDrivers.findIndex(user => user.username === username);
            if (userIndex !== -1) {
                this.selectedDrivers.splice(userIndex, 1)[0];
            }
        },
        // Drivers selecting and unselecting


        // Create restaurant
        async createRestaurant() {
            this.loading = true;

            this.getDataFromInputs();

            try {
                const response = await axios.post('api/restaurant/create/', this.input_data);
                this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'success' });
                this.goBack()
            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error.response.data, type: 'error' });
            }
            this.loading = false;
        },
        // Create restaurant



        // Update restaurant
        async updateRestaurant() {
            this.loading = true;

            this.getDataFromInputs();

            try {
                const response = await axios.put(`api/restaurant/update/${this.editRest['name']}/`, this.input_data);
                this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'success' });
                this.goBack()
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error.response.data, type: 'error' });
            }
            this.loading = false;
        },
        // Update restaurant



        // Go back
        goBack() {
            this.$root.changeCurrentComponent('ManageRestaurantComponent');
        },
        // Go back

    },

}
</script>

