<template>
    <div class="containter m-2 p-2 d-flex justify-content-center">
        <div class="col-12 col-md-9">

            <div class="d-flex justify-content-between mb-5">
                <v-btn @click="goBack" prepend-icon="mdi-undo" color="danger" :variant="theme ? undefined : 'outlined'">
                    Back
                </v-btn>

                <div v-if="user_role === null" class="text-h6 text-md-h5 text-lg-h4 fw-bold">Add Car</div>
                <div v-else class="text-h6 text-md-h5 text-lg-h4">Edit {{ editUser.username }}</div>
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

                        <!-- Year of production -->
                        <v-col cols="12" sm="12">

                            <v-text-field variant="outlined" :value="formattedExpireDate" v-model="firstRegistration"
                                label="Year of production" readonly @click="showfirstRegistration = !showfirstRegistration"
                                :rules="fieldRequired">

                                <!-- Icons -->
                                <template v-slot:append-inner>
                                    <span class="filled-star">
                                    </span>
                                    <v-icon class="icon" style="opacity: 0.4;" icon="mdi-calendar"></v-icon>
                                </template>
                                <!-- Icons -->
                            </v-text-field>

                            <v-date-picker v-if="showfirstRegistration" ok-text="Select" v-model="firstRegistration"
                                title="Year of production" view-mode="year" min="01-01-1960"
                                color="success" @click:save="showfirstRegistration = !showfirstRegistration"
                                @click:cancel="showfirstRegistration = !showfirstRegistration" class="mb-4"></v-date-picker>
    
                        </v-col>
                        <!-- Year of production -->
                       

                    </v-row>

                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mt-10' : 'border-opacity-50 rounded-xl mt-10'"
                        :color="theme ? '' : 'info'"></v-divider>
                    <p align="center" class="text-h4 text-md-h5 text-lg-h5">Insurance info</p>
                    <v-divider :thickness="3"
                        :class="theme ? 'border-opacity-75 rounded-xl mb-10' : 'border-opacity-50 rounded-xl mb-10'"
                        :color="theme ? '' : 'info'"></v-divider>


                    <v-row>
                        <v-col cols="12" sm="6" v-for="input in insuranceInfo" :key="input.name">

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

<script setup>
import { VDatePicker } from 'vuetify/labs/VDatePicker'
</script>

<script>
import axios from 'axios';
import useEventsBus from '../../plugins/eventBus.js'
import { ref, watch } from "vue";
const { emit } = useEventsBus()
import { useTheme } from 'vuetify'
import format from 'date-fns/format'

export default {
    data() {
        return {

            user_role: null,

            basicInfoInputs: [
                {
                    name: 'Vin',
                    model: 'vin',
                    required: true,
                    rules: [
                        v => !!v || 'Vin is required',
                        v => (v && v.length >= 3) || 'Vin must containt at least 3 characters',
                        v => /^[a-zA-Z0-9]+$/.test(v) || 'Vin can only contain numbers and letters',
                    ],
                },
                {
                    name: 'Brand',
                    model: 'brand',
                    required: true,
                    rules: [
                        v => !!v || 'Brand is required',
                        v => (v && v.length >= 3) || 'Brand must containt at least 3 characters',
                        v => /^[a-zA-Z]+$/.test(v) || 'Brand can only contain letters',
                    ],


                },
                {
                    name: 'Model',
                    model: 'model',
                    required: true,
                    rules: [
                        v => !!v || 'Model is required',
                        v => (v.length >= 3) || 'Model name must containt at least 3 characters',
                        v => /^[a-zA-Z0-9- ]+$/.test(v) || 'Character not allowed',
                    ]

                },
                {
                    name: 'Color',
                    model: 'color',
                    required: true,
                    rules: [
                        v => !!v || 'Color is required',
                        v => /^[a-zA-Z]+$/.test(v) || 'Color can only contain letters',
                    ]

                },
                {
                    name: 'Mileage',
                    model: 'mileage',
                    required: true,
                    rules: [
                        v => !!v || 'Mileage is required',
                        v => (v && v.length >= 1) || 'Mileage must containt at least 1 character',
                    ]

                },
                {
                    name: 'Engine capacity',
                    model: 'capacity',
                    required: true,
                    rules: [
                        v => !!v || 'Engine capacity is required',
                        v => /^[0-9,.]+$/.test(v) || 'Only digits are allowed',
                    ]

                },
                {
                    name: 'Engine power',
                    model: 'power',
                    required: true,
                    rules: [
                        v => !!v || 'Engine power is required',
                        v => /^[0-9,.]+$/.test(v) || 'Only digits are allowed',
                    ]

                },

            ],

            insuranceInfo: [
                {
                    name: 'Policy number',
                    model: 'tax_office_name',
                    required: true,
                    icon: 'mdi-bank',
                    rules: [

                        v => /^[a-zA-Z 0-9]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Insurance phone number',
                    model: 'tax_office_address',
                    required: true,
                    icon: 'mdi-bank',
                    rules: [
                        v => !!v || 'Tax office address is required',
                        v => /^[a-zA-Z 0-9]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
            ],

            firstRegistration: null,
            showfirstRegistration: false,

            form: false,
            loading: false,
            input_data: {},
            theme: true,

            alert: false,
            errorContent: '',

            fieldRequired: [v => !!v || 'Field is required',],

            editing: false,
            editUser: {},


        };
    },

    computed: {
        allInputs() {
            return [...this.basicInfoInputs, ...this.insuranceInfo];
        },

        formattedFirstRegistration() {
            return this.firstRegistration ? format(this.firstRegistration, 'yyyy-M-d') : '';
        },
    },


    mounted() {
        this.username = localStorage.getItem('username')


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

        onSubmit() {
            if (!this.form) return;

            this.loading = true;

            if (!this.editing) {
                this.createCar();
            }
            else {
                this.updateUser();
            }


        },
        required(v) {
            return !!v || 'Field is required';
        },


        getDataFromInputs() {
            for (const field of this.allInputs) {
                if (typeof this.input_data[field.model] === 'string') {
                    this.input_data[field.model] = this.input_data[field.model].trim();
                }
                if (!this.input_data[field.model]) {
                    this.input_data[field.model] = null;
                }
            }

        },

        async createCar() {
            this.getDataFromInputs();

            this.input_data['user_role'] = 'HR'

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
        resetForm() {
            for (const field of this.allInputs) {
                this.input_data[field.model] = '';
            }
        },

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

        async updateUser() {
            // Generate dict for sending
            this.input_data['user_role'] = 'HR'
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

            }


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