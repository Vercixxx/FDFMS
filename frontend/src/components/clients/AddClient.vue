<template>
    <div class="containter m-2 p-2 d-flex justify-content-center">
        <div class="col-12 col-md-9">

            <div class="d-flex justify-content-between mb-5">

                <v-row class="text-h4">
                    <v-col cols="5">
                        <v-btn @click="goBack" prepend-icon="mdi-undo" color="danger"
                            :variant="theme ? undefined : 'outlined'">
                            Back
                        </v-btn>
                    </v-col>

                    <v-col>
                        <span v-if="!editing">
                            Add Restaurant
                        </span>
                        <span v-else>
                            Edit Restaurant
                        </span>
                        <v-icon icon="mdi-silverware-fork-knife"></v-icon>
                    </v-col>

                </v-row>

            </div>


            <v-form v-model="form" @submit.prevent="onSubmit">
                <v-container class=" mb-5  rounded-xl elevation-5"
                    :class="{ 'bg-green-lighten-5': !theme, 'bg-grey-darken-4': theme }">

                    <div class="fw-light">
                        <span class="filled-star-example"></span> - field required
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
                                    <span v-if="input.required" class="filled-star">
                                    </span>
                                    <v-icon v-if="input.icon" class="icon" style="opacity: 0.4;">{{ input.icon }}</v-icon>
                                </template>
                                <!-- Icons -->

                            </v-text-field>
                        </v-col>

                        <v-col cols="12" sm="6">
                            <v-autocomplete label="Brand" :items="brands" variant="outlined"
                                v-model="selectedBrand" @update:search="getBrands()" :rules="fieldRequired">
                            </v-autocomplete>
                        </v-col>
                    </v-row>

                    {{ brands }}


                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mt-10' : 'border-opacity-50 rounded-xl mt-10'"
                        :color="theme ? '' : 'info'"></v-divider>
                    <p align="center" class="text-h4 text-md-h5 text-lg-h5">Address</p>
                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mb-10' : 'border-opacity-50 rounded-xl mb-10'"
                        :color="theme ? '' : 'info'"></v-divider>

                    <v-row>

                        <!-- Country and City -->
                        <v-col cols="12" sm="6">
                            <v-autocomplete label="Country" :items="allCountries" variant="outlined"
                                v-model="resSelectedCountry" @update:search="getCities('residence')" :rules="fieldRequired">
                            </v-autocomplete>
                        </v-col>

                        <v-col cols="12" sm="6">
                            <v-autocomplete label="State" :items="resCitiesList" variant="outlined"
                                v-model="resSelectedState" :disabled="resSelectedCountry === ''" :rules="fieldRequired">
                            </v-autocomplete>

                        </v-col>
                        <!-- Country and City -->

                        <v-col cols="12" sm="6" v-for="input in residenceAddress" :key="input.name">

                            <v-text-field variant="outlined" v-model="input_data[input.model]" :label="input.name"
                                :readonly="input.readonly || false" :hint="input.hint || undefined" :rules="input.rules">

                                <!-- Icons -->
                                <template v-slot:append-inner>
                                    <span v-if="input.required" class="filled-star">
                                    </span>
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



                    <v-row>
                        <v-col cols="12" sm="6">
                            <v-card>
                                available
                            </v-card>
                        </v-col>
                        <v-col cols="12" sm="6">
                            <v-card>
                                choosen
                            </v-card>
                        </v-col>
                    </v-row>




                    <!-- Button submit -->
                    <span v-if="!editing">
                        <v-tooltip v-if="!form" activator="parent" location="top" no-overflow>
                            Fill all required fields first
                        </v-tooltip>
                        <span>
                            <v-btn :disabled="!form" :loading="loading" block color="success" size="large" type="submit"
                                class="mt-10 mb-5">
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
                            <v-btn :disabled="!form" :loading="loading" block color="success" size="large" type="submit"
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
            managersUsernames: [],
            choosenUsernames: [],

            theme: true,
            form: false,
            loading: false,
            editing: false,

            input_data: {},

            brands: [],
            availableBrands: [],
            selectedBrand: null,

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

        this.getAllUsernames();

        // Get brands
        this.loadBrands();

    },

    methods: {
        onSubmit() {
            if (!this.form) return;

            this.loading = true;

            if (!this.editing) {
                this.createUser();
            }
            else {
                this.updateUser();
            }


        },



        
        // Load all brands
        async loadBrands() {
            try {
                const response = await axios.get('api/brands/get-all/');
                this.brands = response.data;
            }
            catch (error) {
                console.error('Error when fetching', error);
            }
        },
        // Load all brands

        async getAllUsernames() {
            const response = await axios.get('api/managers/get_username_all/', {
                params: {
                    search: this.query,
                }
            });

            this.managersUsernames = response.data.filter(username => !this.choosenUsernames.includes(username));

            console.log(response);

        },
        toggleUser(user) {
            if (this.isSelected(user)) {
                this.choosenUsernames = this.choosenUsernames.filter(u => u !== user);
            } else if (!this.choosenUsernames.includes(user)) {
                this.choosenUsernames.push(user);
            }
        },

        isSelected(user) {
            return this.choosenUsernames.some(u => u.username === user.username);
        },

        async createRestaurant() {
            const userList = this.choosenUsernames.map(user => user.username);

            const fetched_data = {
                name: this.name,
                phone: this.phone,

                country: this.country,
                city: this.city,
                state: this.state,
                street: this.street,
                home_number: this.home_number,
                apartament_number: this.apartament_number,
                zip_code: this.zip_code,

                managers: userList,
            };

            // post data
            const response = await axios.post('api/restaurant/create/', fetched_data)

            if (response.data.message) {
                this.dataCorrect = response.data;
                document.getElementById('hiddenButton').click();
                this.resetForm();
            }
            else {
                this.dataError = response.data;
                document.getElementById('hiddenButton').click();
            }

        },

        resetForm() {
            this.name = '';
            this.phone = '';

            this.country = '';
            this.city = '';
            this.state = '';
            this.street = '';
            this.home_number = '';
            this.apartament_number = '';
            this.zip_code = '';
        },

    },

}
</script>

