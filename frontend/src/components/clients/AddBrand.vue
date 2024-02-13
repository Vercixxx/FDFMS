<template>
    <div class="containter m-2 p-2 d-flex justify-content-center">
        <div class="col-12 col-md-9">


            <v-btn v-if="editing" @click="goBack" prepend-icon="mdi-undo" color="danger"
                :variant="theme ? undefined : 'outlined'">
                Back
            </v-btn>

            <div class="d-flex justify-center mb-5">
                <div v-if="!editing" class="text-h6 text-md-h5 text-lg-h4 fw-bold">Add new brand
                </div>
                <div v-else class="text-h6 text-md-h5 text-lg-h4">Edit {{ editingBrand.name }}</div>
            </div>


            <!-- Form -->
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


                    <!-- Button submit -->
                    <span v-if="!editing">
                        <v-tooltip v-if="!form" activator="parent" location="top" no-overflow>
                            Fill all required fields first
                        </v-tooltip>
                        <span>
                            <v-btn :disabled="!form" :loading="loading" :color="!form ? 'danger' : 'success'" size="large"
                                type="submit" class="mt-10 mb-5 font-weight-black" block>
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
                            <v-btn :disabled="!form" :loading="loading" :color="!form ? 'danger' : 'success'" size="large"
                                type="submit" class="mt-10 mb-5 font-weight-black" block>
                                Save
                            </v-btn>
                        </span>
                    </span>
                    <!-- Button submit when editing -->

                </v-container>
            </v-form>
            <!-- Form -->

        </div>
    </div>
</template>

<script>
import axios from 'axios';
import useEventsBus from '../../plugins/eventBus.js'
import { watch } from "vue";
import { useTheme } from 'vuetify'
import { drawer } from '../../store/store.js';

export default {
    data() {
        return {

            form: false,
            loading: false,
            input_data: {},
            theme: true,

            fieldRequired: [v => !!v || 'Field is required',],

            editing: false,

            editingBrand: {},
            brandID: null,

            allCountries: [],
            selectedCountry: null,

            allStates: [],
            selectedState: null,


            basicInfoInputs: [
                {
                    name: 'Name',
                    model: 'name',
                    required: true,
                    icon: 'mdi-account',
                    rules: [
                        v => !!v || 'Name is required',
                        v => (v && v.length >= 2) || 'Name must containt at least 2 characters',
                        v => /^[a-zA-Z0-9 -'"]+$/.test(v) || 'Name can only contain letters and numbers',
                    ],
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
    },


    mounted() {

        // Check if editing existing brand
        this.brandID = localStorage.getItem('brandID');

        if (this.brandID !== null) {
            this.getBrandData(this.brandID);
            localStorage.removeItem('brandID');
            this.editing = true;
        }
        // Check if editing existing brand



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
        // Dark mode


        // Get list of available countries
        this.getCountries()
    },


    methods: {
        // On submit
        onSubmit() {
            if (!this.form) return;

            this.loading = true;

            if (!this.editing) {
                this.createBrand();
            }
            else {
                this.updateBrand();
            }

        },
        // On submit



        // Go back
        goBack() {
            this.$root.changeCurrentComponent('ManageBrandsComponent');
        },
        // Go back



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



        // Get data from form
        getDataFromInputs() {
            for (const field of this.allInputs) {
                if (typeof this.input_data[field.model] === 'string') {
                    this.input_data[field.model] = this.input_data[field.model].trim();
                }
                if (!this.input_data[field.model]) {
                    this.input_data[field.model] = null;
                }
            }

            // Adding country and state
            this.input_data['country'] = this.selectedCountry;
            this.input_data['state'] = this.selectedState;

        },
        // Get data from form



        // Create Brand
        async createBrand() {
            this.getDataFromInputs();

            try {
                const response = await axios.post('api/brands/create/', this.input_data);
                this.$root.changeCurrentComponent('ManageBrandsComponent');
                this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'success' });
            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error.response.data, type: 'error' });
            }
            this.loading = false;

        },
        // Create Brand



        // Update brand
        async updateBrand() {
            this.getDataFromInputs();
            const input_data = this.input_data;

            try {
                const response = await axios.put(`api/brands/update/${this.brandID}/`, input_data);
                this.$root.changeCurrentComponent('ManageBrandsComponent');
                this.$store.dispatch('triggerAlert', { message: `Successfully updated ${input_data.name}`, type: 'success' });
            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error.response.data, type: 'error' });
            }
            this.loading = false;

        },
        // Update brand



        // Get brand data
        async getBrandData(brandID) {
            const response = await axios.get(`api/brands/get-info/${brandID}`)
            this.editingBrand = response.data;

            for (const field of this.allInputs) {
                this.input_data[field.model] = this.editingBrand[field.model];
            }

            this.selectedCountry = this.editingBrand['country'];
            this.selectedState = this.editingBrand['state'];

        },
        // Get brand data




    }
}

</script>
