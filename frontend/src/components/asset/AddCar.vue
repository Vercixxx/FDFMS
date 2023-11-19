<template>
    <div class="containter m-2 p-2 d-flex justify-content-center">
        <div class="col-12 col-md-9">

            <div class="d-flex justify-content-between mb-5">

                <v-row class="text-h4" prepend-icon="mdi-car">
                    <v-col cols="5">
                        <v-btn @click="goBack" prepend-icon="mdi-undo" color="danger"
                            :variant="theme ? undefined : 'outlined'">
                            Back
                        </v-btn>
                    </v-col>

                    <v-col>
                        <span v-if="!editing">
                            Add Car
                        </span>
                        <span v-else>
                            Edit Car
                        </span>
                        <v-icon icon="mdi-car"></v-icon>
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



                        <!-- Year of production -->
                        <v-col cols="6" sm="6">

                            <v-combobox variant="outlined" v-model="year_of_prod" :items="avaliableYears"
                                label="Year of production" prepend-inner-icon="mdi-calendar" :rules="fieldRequired">

                            </v-combobox>

                        </v-col>
                        <!-- Year of production -->

                        <v-col cols="6" sm="6">
                            <!-- Transmission -->
                            <v-combobox variant="outlined" v-model="transmission" :items="avaliableTransmission"
                                label="Select Transmission" prepend-inner-icon="mdi-car-shift-pattern"
                                :rules="fieldRequired">

                            </v-combobox>
                            <!-- Transmission -->
                        </v-col>


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

                    <v-row class="d-flex justify-center">
                        <!-- OC and AC -->
                        <v-col>
                            <v-switch v-model="oc" label="Does car has OC" inset :color="oc ? 'green' : ''"></v-switch>
                        </v-col>
                        <v-col>
                            <v-switch v-model="ac" label="Does car has AC" inset :color="ac ? 'green' : ''"></v-switch>
                        </v-col>
                        <!-- OC and AC -->
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
import { drawer } from '../../store/store.js';

export default {
    data() {
        return {

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
                    ]

                },
                {
                    name: 'Engine capacity',
                    model: 'engine_cap',
                    required: true,
                    rules: [
                        v => !!v || 'Engine capacity is required',
                        v => /^[0-9,.]+$/.test(v) || 'Only digits are allowed',
                    ]

                },
                {
                    name: 'Engine power',
                    model: 'engine_pow',
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
                    model: 'policy_number',
                    required: true,
                    icon: 'mdi-bank',
                    rules: [
                        v => !!v || 'Policy number is required',
                        v => /^[a-zA-Z 0-9]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
                },
                {
                    name: 'Insurance phone number',
                    model: 'phone_policy_contact',
                    required: true,
                    icon: 'mdi-bank',
                    rules: [
                        v => !!v || 'Insurance phone number address is required',
                        v => /^[0-9+ -]+$/.test(v) || 'Only numbers, "+" and "-" are allowed',
                    ]
                },
            ],

            transmission: '',
            avaliableTransmission: [
                { title: 'Manual' },
                { title: 'Automatic' },
            ],

            oc: true,
            ac: true,


            form: false,
            loading: false,
            input_data: {},
            theme: true,

            alert: false,
            errorContent: '',

            fieldRequired: [v => !!v || 'Field is required',],

            editing: false,
            editingCar: {},

            carid: null,
            year_of_prod: null,
            avaliableYears: [],


        };
    },

    computed: {
        allInputs() {
            return [...this.basicInfoInputs, ...this.insuranceInfo];
        },

    },


    mounted() {
        this.carid = localStorage.getItem('carid')

        if (this.carid !== null) {
            this.getCarData(this.carid);
            localStorage.removeItem('carid');
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

        this.yearsList();

    },


    methods: {

        onSubmit() {
            if (!this.form) return;

            this.loading = true;

            if (!this.editing) {
                this.createCar();
            }
            else {
                this.updateCar();
            }


        },
        required(v) {
            return !!v || 'Field is required';
        },

        yearsList() {
            const currentYear = new Date().getFullYear();

            const yearsList = this.avaliableYears;
            for (let year = 1990; year <= currentYear; year++) {
                yearsList.push(year);
            }

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

            this.input_data['year_of_prod'] = this.year_of_prod;
            this.input_data['transmission'] = this.transmission.title;
            this.input_data['is_oc'] = this.oc;
            this.input_data['is_ac'] = this.ac;

            try {

                const response = await axios.post('api/car/create/', this.input_data);
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
        resetForm() {
            for (const field of this.allInputs) {
                this.input_data[field.model] = '';
            }
        },

        async getCarData(carid) {

            const response = await axios.get(`api/car/get/${carid}/`);
            this.editingCar = response.data;
            console.log(response.data);

            for (const field of this.allInputs) {
                this.input_data[field.model] = this.editingCar[field.model];
            }

            this.year_of_prod = this.editingCar['year_of_prod'];
            this.transmission = this.editingCar['transmission'];
            this.oc = this.editingCar['is_oc'];
            this.ac = this.editingCar['is_ac'];


        },

        async updateCar() {
            // Generate dict for sending
            this.input_data['year_of_prod'] = this.year_of_prod;
            this.input_data['transmission'] = this.transmission.title;
            this.input_data['is_oc'] = this.oc;
            this.input_data['is_ac'] = this.ac;

        


            // Send put request
            try {
                const response = await axios.put(`api/car/edit/${this.editingCar.id}/`, this.input_data);

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

        goBack() {
            if (!this.editing) {
                this.$root.changeCurrentComponent('HomeComponent');
                drawer.value = !drawer.value;
            } else {
                this.$root.changeCurrentComponent('ShowCarsComponent');
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