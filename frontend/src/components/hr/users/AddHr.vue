<template>
    <!-- image="https://picsum.photos/1920/1080?random" -->
    <div class="containter m-2 p-2 d-flex justify-content-center">
        <div class="col-12 col-md-9">

            <div class="d-flex justify-content-between mb-5">
                <div>
                    <button type="button" class="btn btn-outline-primary mb-3 " @click="goBack">
                        <span class="d-flex align-items-center">
                            <span class="material-symbols-outlined">
                                arrow_back
                            </span>
                            Back
                        </span>
                    </button>
                </div>
                <div v-if="user_role === null" class="text-h6 text-md-h5 text-lg-h4 fw-bold">Add new HR user</div>
                <div v-else class="text-h6 text-md-h5 text-lg-h4">Edit user</div>
                <div></div>

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
                    </v-row>

                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mt-10' : 'border-opacity-50 rounded-xl mt-10'"
                        :color="theme ? '' : 'info'"></v-divider>
                    <p align="center" class="text-h4 text-md-h5 text-lg-h5">Tax, Health and Bank account info</p>
                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mb-10' : 'border-opacity-50 rounded-xl mb-10'"
                        :color="theme ? '' : 'info'"></v-divider>


                    <v-row>
                        <v-col cols="12" sm="6" v-for="input in taxAndHealth" :key="input.name">

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
                    <p align="center" class="text-h4 text-md-h5 text-lg-h5">Addresses</p>
                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mb-10' : 'border-opacity-50 rounded-xl mb-10'"
                        :color="theme ? '' : 'info'"></v-divider>

                    <p align="center" class="text-h6 text-md-h5 text-lg-h5">Residence address</p>
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


                    
                    
                    <!-- Show correspondence -->
                    <v-row class="d-flex justify-center my-5">
                        <v-col cols="auto">
                            <v-switch v-model="show_corespondece" hide-details inset color="success"></v-switch>
                        </v-col>

                        <v-col cols="auto" class="d-flex align-center">
                            Correspodence address same as residence address
                        </v-col>
                    </v-row>
                    <!-- Show correspondence -->


                    <!-- Correspondence address -->
                    <span v-if="!show_corespondece">

                        <p align="center" class="text-h4 text-md-h5 text-lg-h5">Correspondence address</p>

                        <v-row>

                            <!-- Country and City -->
                            <v-col cols="12" sm="6">
                                <v-autocomplete label="Country" :items="allCountries" variant="outlined"
                                    v-model="corSelectedCountry" @update:search="getCities('correspodence')" :rules="show_corespondece ?  [] : fieldRequired">
                                </v-autocomplete>
                            </v-col>

                            <v-col cols="12" sm="6">
                                <v-autocomplete label="State" :items="corCitiesList" variant="outlined"
                                    v-model="corSelectedState" :disabled="corSelectedCountry === ''" :rules="show_corespondece ?  [] : fieldRequired">
                                </v-autocomplete>
                                
                            </v-col>
                            <!-- Country and City -->

                            <v-col cols="12" sm="6" v-for="input in correspodenceAddress" :key="input.name">

                                <v-text-field variant="outlined" v-model="input_data[input.model]" :label="input.name"
                                    :readonly="input.readonly || false" :hint="input.hint || undefined"
                                    :rules="show_corespondece ? [] : input.rules">

                                    <!-- Icons -->
                                    <template v-slot:append-inner>
                                        <span v-if="!show_corespondece && input.required" class="filled-star">
                                        </span>
                                        <v-icon v-if="input.icon" class="icon" style="opacity: 0.4;">{{ input.icon
                                        }}</v-icon>
                                    </template>
                                    <!-- Icons -->

                                    

                                </v-text-field>

                            </v-col>
                        </v-row>
                    </span>
                    <!-- Correspondence address -->


                    <!-- Show Registered -->
                    <v-row class="d-flex justify-center my-5">
                        <v-col cols="auto">
                            <v-switch v-model="show_registered" hide-details inset color="success"></v-switch>
                        </v-col>

                        <v-col cols="auto" class="d-flex align-center">
                            Registered address same as residence address
                        </v-col>
                    </v-row>
                    <!-- Show Registered -->


                    <!-- Registered address -->
                    <span v-if="!show_registered">
                        <p align="center" class="text-h4 text-md-h5 text-lg-h5">Registered address</p>
                        <v-row>

                            <!-- Country and City -->
                            <v-col cols="12" sm="6">
                                <v-autocomplete label="Country" :items="allCountries" variant="outlined"
                                    v-model="regSelectedCountry" @update:search="getCities('registered')" :rules="show_registered ?  [] : fieldRequired">
                                </v-autocomplete>
                            </v-col>

                            <v-col cols="12" sm="6">
                                <v-autocomplete label="State" :items="regCitiesList" variant="outlined"
                                    v-model="regSelectedState" :disabled="regSelectedCountry === ''" :rules="show_registered ?  [] : fieldRequired">
                                </v-autocomplete>
                                
                            </v-col>
                            <!-- Country and City -->

                            <v-col cols="12" sm="6" v-for="input in registeredAddress" :key="input.name">

                                <v-text-field variant="outlined" v-model="input_data[input.model]" :label="input.name"
                                    :readonly="input.readonly || false" :hint="input.hint || undefined"
                                    :rules="show_registered ? [] : input.rules">

                                    <!-- Icons -->
                                    <template v-slot:append-inner>
                                        <span v-if="!show_registered && input.required" class="filled-star">
                                        </span>
                                        <v-icon v-if="input.icon" class="icon" style="opacity: 0.4;">{{ input.icon
                                        }}</v-icon>
                                    </template>
                                    <!-- Icons -->

                                </v-text-field>

                            </v-col>
                        </v-row>
                    </span>
                    <!-- Registered address -->



                    <!-- Button submit -->
                    <span>
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

                </v-container>
            </v-form>

        </div>

    </div>

    <!-- Error -->
    <v-snackbar v-model="alert" :timeout="3000" location="top" color="orange-darken-4">
        <p class="fs-6" v-for="(content, field) in errorContent" :key="name">
            {{ field }} : {{ content.join(', ') }}
        </p>
        <template v-slot:actions>
            <v-btn variant="tonal" @click="alert = false">
                Close
            </v-btn>
        </template>
    </v-snackbar>
    <!-- Error -->
    <!-- Message -->
</template>

<script>
import axios from 'axios';
import useEventsBus from '../../../plugins/eventBus.js'
import { ref, watch } from "vue";
const { emit } = useEventsBus()
import { useTheme } from 'vuetify'

export default {
    data() {
        return {

            user_role: null,

            basicInfoInputs: [
                {
                    name: 'Username',
                    model: 'username',
                    readonly: true,
                    hint: 'Username is generated automatically',
                    icon: 'mdi-lock',
                },
                {
                    name: 'First name',
                    model: 'first_name',
                    required: true,
                    icon: 'mdi-account',
                    rules: [
                        v => !!v || 'First name is required',
                        v => (v && v.length >= 3) || 'First name must containt at least 3 characters',
                        v => /^[a-zA-Z]+$/.test(v) || 'First name can only contain letters',
                    ],


                },
                {
                    name: 'Last name',
                    model: 'last_name',
                    required: true,
                    icon: 'mdi-account',
                    rules: [
                        v => !!v || 'Last name is required',
                        v => (v.length >= 3) || 'Last name name must containt at least 3 characters',
                        v => /^[a-zA-Z]+$/.test(v) || 'Last name can only contain letters',
                    ]

                },
                {
                    name: 'Email',
                    model: 'email',
                    required: true,
                    icon: 'mdi-email',
                    rules: [
                        v => !!v || 'Email is required',
                        v => /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(v) || 'Invalid email address',
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
                {
                    name: 'PESEL/NIP',
                    model: 'pesel_nip',
                    required: true,
                    icon: 'mdi-identifier',
                    rules: [
                        v => !!v || 'PESEL/NIP is required',
                        v => /^[0-9]+$/.test(v) || 'Only digits are allowed',
                    ]

                },
            ],

            taxAndHealth: [
                {
                    name: 'Tax office name',
                    model: 'tax_office_name',
                    required: true,
                    icon: 'mdi-bank',
                    rules: [

                        v => /^[a-zA-Z 0-9]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Tax office address',
                    model: 'tax_office_address',
                    required: true,
                    icon: 'mdi-bank',
                    rules: [
                        v => !!v || 'Tax office address is required',
                        v => /^[a-zA-Z 0-9]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'NFZ branch',
                    model: 'nfz',
                    required: true,
                    icon: 'mdi-bank',
                    rules: [
                        v => !!v || 'NFZ branch is required',
                        v => /^[a-zA-Z 0-9]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Bank Account Number',
                    model: 'bank_account_number',
                    required: true,
                    icon: 'mdi-card-account-details',
                    rules: [
                        v => !!v || 'Bank Account Number is required',
                        v => /^[0-9]+$/.test(v) || 'Only digits are allowed',
                    ]
                },
            ],

            residenceAddress: [
                {
                    name: 'City',
                    model: 'residence_city',
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
                    model: 'residence_street',
                    required: true,
                    icon: 'mdi-map-marker',
                    rules: [
                        v => !!v || 'Street is required',
                        v => /^[a-zA-Z0-9-]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Home',
                    model: 'residence_home_number',
                    required: true,
                    icon: 'mdi-home',
                    rules: [
                        v => !!v || 'Home is required',
                        v => /^[a-zA-Z0-9]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Apartament',
                    model: 'residence_apartament_number',
                    icon: 'mdi-home',
                    rules: [
                        v => /^[a-zA-Z0-9-]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Zip code',
                    model: 'residence_zip_code',
                    required: true,
                    icon: 'mdi-earth',
                    rules: [
                        v => !!v || 'Zip code is required',
                        v => /^[0-9-]+$/.test(v) || 'Only numbers and "-" are allowed',
                    ]
                },
            ],

            correspodenceAddress: [
                {
                    name: 'City',
                    model: 'correspondence_city',
                    icon: 'mdi-map-marker',
                    required: true,
                    rules: [
                        v => !!v || 'City is required',
                        v => (v.length >= 3) || 'City name must containt at least 3 characters',
                        v => /^[a-zA-Z-]+$/.test(v) || 'City can only contain letters',
                    ]
                },
                {
                    name: 'Street',
                    model: 'correspondence_street',
                    icon: 'mdi-map-marker',
                    required: true,
                    rules: [
                        v => !!v || 'Street is required',
                        v => /^[a-zA-Z0-9-]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Home',
                    model: 'correspondence_home_number',
                    icon: 'mdi-home',
                    required: true,
                    rules: [
                        v => !!v || 'Home is required',
                        v => /^[a-zA-Z0-9]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Apartament',
                    model: 'correspondence_apartament_number',
                    icon: 'mdi-home',
                    rules: [
                        v => /^[a-zA-Z0-9-]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Zip code',
                    model: 'correspondence_zip_code',
                    icon: 'mdi-earth',
                    required: true,
                    rules: [
                        v => !!v || 'Zip code is required',
                        v => /^[0-9-]+$/.test(v) || 'Only numbers and "-" are allowed',
                    ]
                },
            ],

            registeredAddress: [
                {
                    name: 'City',
                    model: 'registered_city',
                    icon: 'mdi-map-marker',
                    required: true,
                    rules: [
                        v => !!v || 'City is required',
                        v => (v.length >= 3) || 'City name must containt at least 3 characters',
                        v => /^[a-zA-Z-]+$/.test(v) || 'City can only contain letters',
                    ]
                },
                {
                    name: 'Street',
                    model: 'registered_street',
                    icon: 'mdi-map-marker',
                    required: true,
                    rules: [
                        v => !!v || 'Street is required',
                        v => /^[a-zA-Z0-9-]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Home',
                    model: 'registered_home_number',
                    icon: 'mdi-home',
                    required: true,
                    rules: [
                        v => !!v || 'Home is required',
                        v => /^[a-zA-Z0-9]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Apartament',
                    model: 'registered_apartament_number',
                    icon: 'mdi-home',
                    rules: [
                        v => /^[a-zA-Z0-9-]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Zip code',
                    model: 'registered_zip_code',
                    icon: 'mdi-earth',
                    required: true,
                    rules: [
                        v => !!v || 'Zip code is required',
                        v => /^[0-9-]+$/.test(v) || 'Only numbers and "-" are allowed',
                    ]
                },
            ],

            show_corespondece: true,
            show_registered: true,

            form: false,
            loading: false,
            input_data: {},
            theme: true,

            alert: false,
            errorContent: '',

            allCountries: [],

            resSelectedCountry: '',
            corSelectedCountry: '',
            regSelectedCountry: '',

            resCitiesList: [],
            corCitiesList: [],
            regCitiesList: [],

            resSelectedState: '',
            corSelectedState: '',
            regSelectedState: '',

            fieldRequired: [v => !!v || 'Field is required',],


        };
    },

    computed: {
        allInputs() {
            return [...this.basicInfoInputs, ...this.taxAndHealth, ...this.residenceAddress, ...this.correspodenceAddress, ...this.registeredAddress];
        },
    },


    mounted() {
        this.username = localStorage.getItem('username')

        if (this.username !== null) {
            this.user_role = localStorage.getItem('user_role')
            this.getUserData(this.username, this.user_role);

            // Correspodence and Register forms
            var switch1 = document.getElementById("switch1");
            var switch2 = document.getElementById("switch2");

            switch1.style.display = 'none';
            switch2.style.display = 'none';

            this.show_corespondece_form = false;
            this.show_registered_form = false;
            // Correspodence and Register forms

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

        // Get all Countries
        this.getCountries();


    },

    watch: {
        'input_data.first_name': 'generateUsername',
        'input_data.last_name': 'generateUsername',
    },



    methods: {

        onSubmit() {
            if (!this.form) return;

            this.loading = true;
            this.createUser();


        },
        required(v) {
            return !!v || 'Field is required';
        },

        copyResidenceToCorrespondence() {
            if (this.show_corespondece) {
                for (let i = 0; i < this.residenceAddress.length; i++) {
                    const fieldRes = this.residenceAddress[i];
                    const fieldCor = this.correspodenceAddress[i];
                    this.input_data[fieldCor.model] = this.input_data[fieldRes.model];
                }
                // Adding country and state
                this.input_data['correspondence_country'] = this.resSelectedCountry;
                this.input_data['correspondence_state'] = this.resSelectedState;

            }
            else {
                // Adding country and state
                this.input_data['correspondence_country'] = this.corSelectedCountry;
                this.input_data['correspondence_state'] = this.corSelectedState;
            }
        },

        copyResidenceToRegistered() {
            if (this.show_registered) {
                for (let i = 0; i < this.residenceAddress.length; i++) {
                    const fieldRes = this.residenceAddress[i];
                    const fieldReg = this.registeredAddress[i];
                    this.input_data[fieldReg.model] = this.input_data[fieldRes.model];
                }
                // Adding country and state
                this.input_data['registered_country'] = this.resSelectedCountry;
                this.input_data['registered_state'] = this.resSelectedState;

            }
            else {
                // Adding country and state
                this.input_data['registered_country'] = this.regSelectedCountry;
                this.input_data['registered_state'] = this.regSelectedState;
            }
        },

        getDataFromInputs() {
            this.copyResidenceToCorrespondence();
            this.copyResidenceToRegistered();

            for (const field of this.allInputs) {
                if (typeof this.input_data[field.model] === 'string') {
                    this.input_data[field.model] = this.input_data[field.model].trim();
                }
                if (!this.input_data[field.model]) {
                    this.input_data[field.model] = null;
                }
            }

            // Adding country and state
            this.input_data['residence_country'] = this.resSelectedCountry;
            this.input_data['residence_state'] = this.resSelectedState;

            // console.log(JSON.stringify(this.input_data, null, 2));
        },
        generateUsername() {
            let firstName = '';
            let lastName = '';

            if (this.input_data.first_name) {
                firstName = this.input_data.first_name.slice(0, 3).toLowerCase();
            }
            if (this.input_data.last_name) {
                lastName = this.input_data.last_name.slice(0, 3).toLowerCase();
            }

            let randomDigits = '';

            if (this.input_data.first_name && this.input_data.first_name.length >= 3 && this.input_data.last_name && this.input_data.last_name.length >= 3) {
                randomDigits = this.generateRandomDigits();
            }

            this.input_data.username = `${firstName}${lastName}${randomDigits}`;
        },


        generateRandomDigits() {
            return Math.floor(100 + Math.random() * 900);
        },

        async getCountries() {
            const response = await axios.get("api/users/get-countries/");
            this.allCountries = response.data;
        },

        async getCities(country) {
            const propertyMap = {
                residence: this.resSelectedCountry,
                correspodence: this.corSelectedCountry,
                registered: this.regSelectedCountry,
            };

            const choosen_country = propertyMap[country];
            const response = await axios.get(`api/users/get-cities/${choosen_country}/`);

            switch (country) {
                case ('residence'):
                    this.resCitiesList = response.data
                    break;
                case ('correspodence'):
                    this.corCitiesList = response.data
                    break;
                case ('registered'):
                    this.regCitiesList = response.data
                    break;
            }
        },


        async createUser() {
            this.getDataFromInputs();

            this.input_data['user_role'] = 'HR'

            const response = await axios.post('api/create/', this.input_data);

            console.log(response);

            if (response.status === 200) {

                emit('message', '');
                localStorage.setItem('message', response.data.message);

                this.$root.changeCurrentComponent('AddUserComponent');

            }
            else {
                this.errorContent = response.message;
                this.alert = true;
            }

        },
        resetForm() {
            for (const field of this.allInputs) {
                this.input_data[field.model] = '';
            }
        },

        async getUserData(username, user_role) {

            const response = await axios.get(`api/users/get/${username}/${user_role}`);
            console.log(response.data);

            localStorage.removeItem('username');
            localStorage.removeItem('user_role');

            // Set input data
            this.username = response.data.username;

            this.firstName = response.data.first_name;
            this.lastName = response.data.last_name;
            this.email = response.data.email;
            this.phone = response.data.phone;
            this.identity = response.data.pesel_nip;
            this.taxName = response.data.tax_office_name;
            this.tax_address = response.data.tax_office_address;
            this.nfz = response.data.nfz;
            this.bankAccount = response.data.bank_account_number;

            this.resCountry = response.data.residence_country;
            this.resCity = response.data.residence_city;
            this.resState = response.data.residence_state;
            this.resStreet = response.data.residence_street;
            this.resHomeNumber = response.data.residence_home_number;
            this.resApartamentNumber = response.data.residence_apartament_number;
            this.resZipCode = response.data.residence_zip_code;

            this.corCountry = response.data.correspondence_country;
            this.corCity = response.data.correspondence_city;
            this.corState = response.data.correspondence_state;
            this.corStreet = response.data.correspondence_street;
            this.corHomeNumber = response.data.correspondence_home_number;
            this.corApartamentNumber = response.data.correspondence_apartament_number;
            this.corZipCode = response.data.correspondence_zip_code;

            this.regCountry = response.data.registered_country;
            this.regCity = response.data.registered_city;
            this.regState = response.data.registered_state;
            this.regStreet = response.data.registered_street;
            this.regHomeNumber = response.data.registered_home_number;
            this.regApartamentNumber = response.data.registered_apartament_number;
            this.regZipCode = response.data.registered_zip_code;
            // Set input data


        },

        async updateUser() {
            // Generate dict for sending
            const fetched_data = {
                first_name: this.firstName,
                last_name: this.lastName,
                email: this.email,
                phone: this.phone,
                username: this.username,
                password: this.password,

                pesel_nip: this.identity,
                tax_office_name: this.taxName,
                tax_office_address: this.tax_address,
                nfz: this.nfz,
                bank_account_number: this.bankAccount,
                residence_country: this.resCountry,
                residence_city: this.resCity,
                residence_state: this.resState,
                residence_street: this.resStreet,
                residence_home_number: this.resHomeNumber,
                residence_apartament_number: this.resApartamentNumber,
                residence_zip_code: this.resZipCode,

                correspondence_country: this.corCountry,
                correspondence_city: this.corCity,
                correspondence_state: this.corState,
                correspondence_street: this.corStreet,
                correspondence_home_number: this.corHomeNumber,
                correspondence_apartament_number: this.corApartamentNumber,
                correspondence_zip_code: this.corZipCode,

                registered_country: this.regCountry,
                registered_city: this.regCity,
                registered_state: this.regState,
                registered_street: this.regStreet,
                registered_home_number: this.regHomeNumber,
                registered_apartament_number: this.regApartamentNumber,
                registered_zip_code: this.regZipCode,
            };

            // Send put request
            const response2 = await axios.put(`api/users/save/${this.username}/${this.user_role}/`, fetched_data);
            const message = `Successfully updated ${this.username}`;
            // localStorage.setItem('message', message)


            // Finish
            this.goBack()
        },

        goBack() {
            if (this.user_role === null) {
                this.$root.changeCurrentComponent('AddUserComponent');
            } else {
                this.$root.changeCurrentComponent('ModifyUserComponent');
            }
        },

    }
};
</script>

<style >
.filled-star::before {
    content: '\2605';
    color: #ff6666;
    font-weight: bold;
    position: absolute;
    left: 3px;
    top: 0px;
}

.filled-star-example::before {
    content: '\2605';
    color: #ff0000;

}
</style>