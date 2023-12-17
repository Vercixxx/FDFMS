<template>
    <div class="containter m-2 p-2 d-flex justify-content-center">
        <div class="col-12 col-md-9">

            <v-btn v-if="editing" @click="goBack" prepend-icon="mdi-undo" color="danger"
                :variant="theme ? undefined : 'outlined'">
                Back
            </v-btn>

            <div class="d-flex justify-center mb-5">
                <div v-if="user_role === null" class="text-h6 text-md-h5 text-lg-h4 fw-bold">Add new {{ addingRole }} user
                </div>
                <div v-else class="text-h6 text-md-h5 text-lg-h4">Edit {{ editUser.username }} user</div>
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
                    <p align="center" class="text-h4 text-md-h5 text-lg-h5">Addresses</p>
                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mb-10' : 'border-opacity-50 rounded-xl mb-10'"
                        :color="theme ? '' : 'info'"></v-divider>

                    <p align="center" class="text-h6 text-md-h5 text-lg-h5">Residence address</p>
                    <v-row>

                        <!-- Country and State -->
                        <v-col cols="12" sm="6">
                            <v-autocomplete label="Country" :items="allCountries" variant="outlined"
                                v-model="resSelectedCountry" @update:search="getStates('residence')" :rules="fieldRequired">

                            </v-autocomplete>

                        </v-col>

                        <v-col cols="12" sm="6">
                            <v-autocomplete label="State" :items="resStatesList" variant="outlined"
                                v-model="resSelectedState" :disabled="resSelectedCountry === null" :rules="fieldRequired">
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




                    <!-- Show correspondence -->
                    <v-row class="d-flex justify-center my-5" v-if="!editing">
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
                                    v-model="corSelectedCountry" @update:search="getStates('correspodence')"
                                    :rules="show_corespondece ? [] : fieldRequired">
                                </v-autocomplete>
                            </v-col>

                            <v-col cols="12" sm="6">
                                <v-autocomplete label="State" :items="corStatesList" variant="outlined"
                                    v-model="corSelectedState" :disabled="corSelectedCountry === null"
                                    :rules="show_corespondece ? [] : fieldRequired">
                                </v-autocomplete>

                            </v-col>
                            <!-- Country and City -->

                            <v-col cols="12" sm="6" v-for="input in correspodenceAddress" :key="input.name">

                                <v-text-field variant="outlined" v-model="input_data[input.model]" :label="input.name"
                                    :readonly="input.readonly || false" :hint="input.hint || undefined"
                                    :rules="show_corespondece ? [] : input.rules">

                                    <!-- Icons -->
                                    <template v-slot:append-inner>
                                        <v-icon v-if="!show_corespondece && input.required" icon="mdi-star" color="red"
                                            style="font-size:medium; position: absolute; top:3px; right: 3px;"></v-icon>
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
                    <v-row class="d-flex justify-center my-5" v-if="!editing">
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
                                    v-model="regSelectedCountry" @update:search="getStates('registered')"
                                    :rules="show_registered ? [] : fieldRequired">
                                </v-autocomplete>
                            </v-col>

                            <v-col cols="12" sm="6">
                                <v-autocomplete label="State" :items="regStatesList" variant="outlined"
                                    v-model="regSelectedState" :disabled="regSelectedCountry === null"
                                    :rules="show_registered ? [] : fieldRequired">
                                </v-autocomplete>

                            </v-col>
                            <!-- Country and City -->

                            <v-col cols="12" sm="6" v-for="input in registeredAddress" :key="input.name">

                                <v-text-field variant="outlined" v-model="input_data[input.model]" :label="input.name"
                                    :readonly="input.readonly || false" :hint="input.hint || undefined"
                                    :rules="show_registered ? [] : input.rules">

                                    <!-- Icons -->
                                    <template v-slot:append-inner>
                                        <v-icon v-if="!show_registered && input.required" icon="mdi-star" color="red"
                                            style="font-size:medium; position: absolute; top:3px; right: 3px;"></v-icon>
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

            resSelectedCountry: null,
            corSelectedCountry: null,
            regSelectedCountry: null,

            resStatesList: [],
            corStatesList: [],
            regStatesList: [],

            resSelectedState: null,
            corSelectedState: null,
            regSelectedState: null,

            fieldRequired: [v => !!v || 'Field is required',],

            editing: false,
            editUser: {},

            addingRole: null,


        };
    },

    computed: {
        allInputs() {
            return [...this.basicInfoInputs, ...this.taxAndHealth, ...this.residenceAddress, ...this.correspodenceAddress, ...this.registeredAddress];
        },
    },


    mounted() {
        // Check for user class
        this.addingRole = localStorage.getItem('addingRole');
        localStorage.removeItem('addingRole');

        this.username = localStorage.getItem('username');


        if (this.username !== null) {
            this.user_role = localStorage.getItem('user_role')
            this.getUserData(this.username, this.user_role);

            localStorage.removeItem('username');
            localStorage.removeItem('user_role');

            this.editing = true;

            this.show_corespondece = false;
            this.show_registered = false;
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
        'input_data.first_name': function (newVal, oldVal) {
            if (!this.editing) {
                this.generateUsername(newVal, oldVal);
            }
        },
        'input_data.last_name': function (newVal, oldVal) {
            if (!this.editing) {
                this.generateUsername(newVal, oldVal);
            }
        },
    },




    methods: {



        // Method called on submiting form
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
        // Method called on submiting form



        // Field required rule
        required(v) {
            return !!v || 'Field is required';
        },
        // Field required rule



        // Adding correspondence form
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
        // Adding correspondence form



        // Adding registered form
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
        // Adding registered form



        // Getting data from inputs
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

        },
        // Getting data from inputs



        // Generate username based on first and last name
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
        // Generate username based on first and last name



        // Random digits generator
        generateRandomDigits() {
            return Math.floor(100 + Math.random() * 900);
        },
        // Random digits generator



        // Get countries
        async getCountries() {
            const response = await axios.get("api/countries/get/");
            this.allCountries = response.data.map(country => country.name);
        },
        // Get countries



        // Get States
        async getStates(country) {
            const propertyMap = {
                residence: this.resSelectedCountry,
                correspodence: this.corSelectedCountry,
                registered: this.regSelectedCountry,
            };

            const choosen_country = propertyMap[country];
            const response = await axios.get(`api/states/get/?country=${choosen_country}`);
            const result = response.data.map(state => state.name)

            switch (country) {
                case ('residence'):
                    this.resStatesList = result
                    break;
                case ('correspodence'):
                    this.corStatesList = result
                    break;
                case ('registered'):
                    this.regStatesList = result
                    break;
            }
        },
        // Get States



        // Create user function
        async createUser() {
            this.getDataFromInputs();

            this.input_data['user_role'] = this.addingRole;

            const response = await axios.post('api/create/', this.input_data);

            if (response.status === 200) {

                const messageData = {
                    message: `Successfully added ${this.input_data.username}`,
                    type: 'success'
                };

                localStorage.setItem('message', JSON.stringify(messageData));
                emit('message', '');


                this.$root.changeCurrentComponent('AddUserComponent');

            }
            else {
                this.errorContent = response.message;
                this.alert = true;
            }

        },
        // Create user function



        // Get user data from server when editing
        async getUserData(username, user_role) {

            const response = await axios.get(`api/users/get/${username}/${user_role}`);
            this.editUser = response.data;

            for (const field of this.allInputs) {
                this.input_data[field.model] = this.editUser[field.model];
            }

            // Country and States
            this.resSelectedCountry = this.editUser['residence_country'];
            this.corSelectedCountry = this.editUser['correspondence_country'];
            this.regSelectedCountry = this.editUser['registered_country'];

            this.resSelectedState = this.editUser['residence_state'];
            this.corSelectedState = this.editUser['correspondence_state'];
            this.regSelectedState = this.editUser['registered_state'];
        },
        // Get user data from server when editing



        // Update user function
        async updateUser() {
            // Generate dict for sending
            this.input_data['user_role'] = this.user_role;
            const ready_data = this.input_data;


            // Send put request
            try {
                const response = await axios.put(`api/users/save/${ready_data.username}/${ready_data.user_role}/`, ready_data);

                const messageData = {
                    message: `Successfully modified ${ready_data.username}`,
                    type: 'success'
                };

                localStorage.setItem('message', JSON.stringify(messageData));

                emit('message', '');
                this.loading = false;
                this.$root.changeCurrentComponent('ModifyUserComponent');

            }
            catch (error) {
                this.loading = false;
                const messageData = {
                    message: error.response.data.error,
                    type: 'danger'
                };
                localStorage.setItem('message', JSON.stringify(messageData));
                emit('message', '');
                this.$root.changeCurrentComponent('ModifyUserComponent');
            }


        },
        // Update user function



        // Go back
        goBack() {
            this.$root.changeCurrentComponent('ModifyUserComponent');
        },
        // Go back

    }
};
</script>
