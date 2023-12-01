<template>
    <div class="containter m-2 p-2 d-flex justify-content-center">
        <div class="col-12 col-md-9">


            <!-- Top -->
            <div class="d-flex justify-content-between mb-5">
                <v-btn @click="goBack" prepend-icon="mdi-undo" color="danger" :variant="theme ? undefined : 'outlined'">
                    Manage
                </v-btn>


                <div v-if="!editing" class="text-h6 text-md-h5 text-lg-h4 fw-bold">
                    <v-icon icon="mdi-silverware-fork-knife"></v-icon>
                    Add Restaurant
                </div>
                <div v-else class="text-h6 text-md-h5 text-lg-h4 fw-bold">
                    <v-icon icon="mdi-silverware-fork-knife"></v-icon>
                    Edit ?
                </div>
                <div></div>

            </div>
            <!-- Top -->




            <v-form v-model="form" @submit.prevent="onSubmit">
                <v-container class=" mb-5  rounded-xl elevation-5"
                    :class="{ 'bg-green-lighten-5': !theme, 'bg-grey-darken-4': theme }">

                    <div class="fw-light">
                        <v-icon icon="mdi-star" color="red" style="font-size:medium"></v-icon> - field required
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
                                v-model="selectedCountry" @update:search="getCities('residence')" :rules="fieldRequired">
                            </v-autocomplete>
                        </v-col>

                        <v-col cols="12" sm="6">
                            <v-autocomplete label="State" :items="allStates" variant="outlined" v-model="selectedState"
                                :disabled="selectedCountry === null" :rules="fieldRequired">
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
                        <v-col cols="12" sm="6" align="center">

                            <v-card class="pa-3 ma-1 border-xl rounded-xl" :color="theme ? 'grey-darken-3' : ''">
                                <v-col cols="10" align="center">

                                    <p class="text-h4 text-md-h5 text-lg-h5">Available managers</p>

                                    <!-- Search bar -->
                                    <v-text-field variant="solo-filled" v-model="searchQueryAvailable"
                                        @keydown.enter="searchTableAvailable = searchQueryAvailable" label="Search"
                                        class="px-1 " prepend-inner-icon="mdi-magnify" hide-actions
                                        hint="Press enter to search" />
                                    <!-- Search bar -->

                                    <!-- Available managers -->
                                    <v-data-table :headers="tableHeaders" :items="availableManagers"
                                        :search="searchTableAvailable" :loading="tableLoading"
                                        class="elevation-4 rounded-xl" item-value="id" v-model:items-per-page="itemsPerPage"
                                        hover select-strategy="all" show-current-page>



                                        <!-- No data -->
                                        <template v-slot:no-data>
                                            <p class="text-h6 pa-5 text-danger">
                                                <v-icon icon="mdi-database-alert-outline"></v-icon>
                                                No available managers
                                            </p>
                                        </template>
                                        <!-- No data -->


                                        <template v-slot:item="{ item }">
                                            <tr align="center" @click="selectUser(item.id)" role="button">
                                                <v-tooltip v-if="!form" activator="parent" location="top" no-overflow>
                                                    Click to select
                                                </v-tooltip>
                                                <td v-for="header in tableHeaders" :key="header.key">
                                                    {{ item[header.key] }}
                                                </td>
                                            </tr>
                                        </template>

                                    </v-data-table>
                                    <!-- Available managers -->
                                </v-col>
                            </v-card>

                        </v-col>

                        <v-col cols="12" sm="6" align="center">

                            <v-card class="pa-3 ma-1 border-xl rounded-xl" :color="theme ? 'grey-darken-3' : ''">
                                <v-col cols="10" align="center">

                                    <p align="center" class="text-h4 text-md-h5 text-lg-h5">Selected managers</p>

                                    <!-- Search bar -->
                                    <v-text-field variant="solo-filled" v-model="searchQuerySelected"
                                        @keydown.enter="searchTableSelected = searchQuerySelected" label="Search"
                                        class="px-1 " prepend-inner-icon="mdi-magnify" hide-actions
                                        hint="Press enter to search" />
                                    <!-- Search bar -->


                                    <!-- Selected managers -->
                                    <v-data-table :headers="tableHeaders" :items="selectedManagers"
                                        :search="searchTableSelected" :loading="tableLoading" class="elevation-4 rounded-xl"
                                        item-value="id" v-model:items-per-page="itemsPerPage" hover select-strategy="all"
                                        show-current-page>



                                        <!-- No data -->
                                        <template v-slot:no-data>
                                            <p class="text-h6 pa-5 text-danger">
                                                <v-icon icon="mdi-database-alert-outline"></v-icon>
                                                No selected managers
                                            </p>
                                        </template>
                                        <!-- No data -->

                                        <template v-slot:item="{ item }">
                                            <tr align="center" @click="unselectUser(item.id)" role="button">
                                                <v-tooltip v-if="!form" activator="parent" location="top" no-overflow>
                                                    Click to unselect
                                                </v-tooltip>
                                                <td v-for="header in tableHeaders" :key="header.key">
                                                    {{ item[header.key] }}
                                                </td>
                                            </tr>
                                        </template>

                                    </v-data-table>
                                    <!-- Selected managers -->
                                </v-col>
                            </v-card>

                        </v-col>
                    </v-row>
                    <!-- Managers -->


                    <!-- Button submit -->
                    <span v-if="!editing">
                        <v-tooltip v-if="!form" activator="parent" location="top" no-overflow>
                            Fill all required fields first
                        </v-tooltip>
                        <span>
                            <v-btn :disabled="!form" :loading="loading" block :color="!form ? 'danger' : 'success'"
                                size="large" type="submit" class="mt-10 mb-5">
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
                            <v-btn :disabled="!form" :loading="loading" block :color="!form ? 'danger' : 'success'" size="large" type="submit"
                                class="mt-10 mb-5">
                                Save
                            </v-btn>
                        </span>
                    </span>
                    <!-- Button submit when editing -->

                </v-container>
            </v-form>

        </div>

    </div>
</template>



<script>
import axios from 'axios';
import useEventsBus from '../../plugins/eventBus.js'
import { ref, watch } from "vue";
const { emit } = useEventsBus()
import { useTheme } from 'vuetify'


export default {
    data() {
        return {
            theme: true,
            form: false,
            loading: false,
            editing: false,

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

            itemsPerPage: 10,
            tableHeaders: [
                { title: 'Username', key: 'username', align: 'center', sortable: true },
                { title: 'Id', key: 'id', align: 'center', sortable: true },
            ],

            // Search
            searchTableAvailable: '',

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
                        v => /^[0-9+ -]+$/.test(v) || 'Only numbers, "+" and "-" are allowed',
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
    },


    mounted() {
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
            this.input_data['managers'] = this.selectedManagers.map(manager => manager.id);
            this.input_data['brand'] = this.selectedBrand;

        },
        // Getting data from inputs



        // Country
        async getCountries() {
            const response = await axios.get("api/users/get-countries/");
            this.allCountries = response.data;
        },
        // Country



        // City
        async getCities(country) {
            const response = await axios.get(`api/users/get-cities/${this.selectedCountry}/`);
            this.allStates = response.data
        },
        // City



        // Move user to selected
        selectUser(userID) {
            const userIndex = this.availableManagers.findIndex(user => user.id === userID);
            if (userIndex !== -1) {
                const selectedUser = this.availableManagers.splice(userIndex, 1)[0];
                this.selectedManagers.push(selectedUser);
            }
        },
        // Move user to selected



        // Move user to unselected
        unselectUser(userID) {
            const userIndex = this.selectedManagers.findIndex(user => user.id === userID);
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
                this.availableBrands = response.data.map(item => item.name);
            }
            catch (error) {
                console.error('Error when fetching', error);
            }
        },
        // Load all brands



        // Get all managers
        async getManagers() {
            const response = await axios.get('api/managers/get_username_all/', {
                params: {
                    search: this.query,
                }
            });
            this.availableManagers = response.data;

        },
        // Get all managers



        // Create restaurant
        async createRestaurant() {

            this.getDataFromInputs();

            try {
                const response = await axios.post('api/restaurant/create/', this.input_data);
                console.log(response);

                const messageData = {
                    message: response.data.message,
                    type: 'success'
                };

                localStorage.setItem('message', JSON.stringify(messageData));

                emit('message', '');
                this.goBack()
            }
            catch (error) {
                this.loading = false;
                const messageData = {
                    message: error.response.data.error,
                    type: 'danger'
                };
                localStorage.setItem('message', JSON.stringify(messageData));
                emit('message', '');
            }
        },
        // Create restaurant



        // Go back
        goBack() {
            this.$root.changeCurrentComponent('ManageRestaurantComponent');
        },
        // Go back

    },

}
</script>

