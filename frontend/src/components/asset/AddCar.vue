<template>
    <div class="containter m-2 p-2 d-flex justify-content-center">
        <div class="col-12 col-md-9">

            <v-btn v-if="editing" @click="goBack" prepend-icon="mdi-undo" color="danger"
                :variant="theme ? undefined : 'outlined'">
                Back
            </v-btn>

            <div class="d-flex justify-center mb-5">
                <div v-if="!editing" class="text-h6 text-md-h5 text-lg-h4 fw-bold">
                    <v-icon icon="mdi-car"></v-icon>
                    Add new car
                    <v-icon icon="mdi-car"></v-icon>
                </div>
                <div v-else class="text-h6 text-md-h5 text-lg-h4">
                    <v-icon icon="mdi-car"></v-icon>
                    Edit car vin
                    <span class="font-weight-bold">
                        {{ carVin }}
                    </span>
                    <v-icon icon="mdi-car"></v-icon>
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
                        <!-- Vin -->
                        <v-col cols="12" sm="6">
                            <v-text-field variant="outlined" v-model="vin" label="Vin" :readonly="editing"
                                hint="Vin is immutable when set" :rules="vinRules">

                                <!-- Icons -->
                                <template v-slot:append-inner v-if="!editing">
                                    <v-icon icon="mdi-star" color="red"
                                        style="font-size:medium; position: absolute; top:3px; right: 3px;"></v-icon>
                                </template>
                                <!-- Icons -->

                            </v-text-field>
                        </v-col>
                        <!-- Vin -->


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



                        <!-- Year of production -->
                        <v-col cols="6" sm="6">

                            <v-combobox variant="outlined" v-model="year_of_prod" :items="avaliableYears"
                                label="Year of production" prepend-inner-icon="mdi-calendar" :rules="fieldRequired">

                                <!-- Icons -->
                                <template v-slot:append-inner>
                                    <v-icon icon="mdi-star" color="red"
                                        style="font-size:medium; position: absolute; top:3px; right: 3px;"></v-icon>
                                </template>
                                <!-- Icons -->

                            </v-combobox>

                        </v-col>
                        <!-- Year of production -->

                        <v-col cols="6" sm="6">
                            <!-- Transmission -->
                            <v-combobox variant="outlined" v-model="transmission" :items="avaliableTransmission"
                                label="Select Transmission" prepend-inner-icon="mdi-car-shift-pattern"
                                :rules="fieldRequired">

                                <!-- Icons -->
                                <template v-slot:append-inner>
                                    <v-icon icon="mdi-star" color="red"
                                        style="font-size:medium; position: absolute; top:3px; right: 3px;"></v-icon>
                                </template>
                                <!-- Icons -->

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
                                    <v-icon v-if="input.required" icon="mdi-star" color="red"
                                        style="font-size:medium; position: absolute; top:3px; right: 3px;"></v-icon>
                                    <v-icon v-if="input.icon" class="icon" style="opacity: 0.4;">{{ input.icon }}</v-icon>
                                </template>
                                <!-- Icons -->

                            </v-text-field>

                        </v-col>

                    </v-row>



                    <!-- OC and AC -->
                    <v-row class="d-flex justify-center" v-if="!editing">
                        <v-col cols="auto">
                            <v-switch v-model="oc" label="Does car has OC" inset :color="oc ? 'green' : ''"></v-switch>
                        </v-col>
                    </v-row>

                    <v-row class="d-flex justify-center" v-if="!editing">
                        <v-col cols="auto">
                            <v-switch v-model="ac" label="Does car has AC" inset :color="ac ? 'green' : ''">
                            </v-switch>

                        </v-col>
                    </v-row>
                    <!-- OC and AC -->



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
</template>



<script>
import axios from 'axios';
import useEventsBus from '../../plugins/eventBus.js'
import { watch } from "vue";
import { useTheme } from 'vuetify'

export default {
    data() {
        return {

            vinRules: [
                v => !!v || 'Vin is required',
                v => (v && v.length >= 3) || 'Vin must containt at least 3 characters',
                v => /^[a-zA-Z0-9]+$/.test(v) || 'Vin can only contain numbers and letters',
            ],
            vin: '',

            basicInfoInputs: [
                {
                    name: 'License plate',
                    model: 'license_plate',
                    required: false,
                    rules: [
                        v => /^[a-zA-Z 0-9]+$/.test(v) || 'Only letters and numbers are allowed',
                    ]
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
                        v => /^\d+$/.test(v) || 'Mileage can only contain digits',
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
                        v => !!v || 'Phone number is required',
                        v => /^[0-9]+$/.test(v) || 'Only digits are allowed',
                        v => v.length >= 9 || 'Phone number must be at least 9 digits',
                        v => v.length <= 15 || 'Phone number must not exceed 15 digits',
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

            fieldRequired: [v => !!v || 'Field is required',],

            editing: false,
            editingCar: {},

            carVin: null,
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

        this.carVin = localStorage.getItem('carVin')

        if (this.carVin !== null) {
            this.getCarData(this.carVin);
            localStorage.removeItem('carVin');
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

        // Method called on submiting form
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
        // Method called on submiting form



        // Field required rule
        required(v) {
            return !!v || 'Field is required';
        },
        // Field required rule


        // Years list
        yearsList() {
            const currentYear = new Date().getFullYear();

            const yearsList = this.avaliableYears;
            for (let year = currentYear; year >= 1990; year--) {
                yearsList.push(year);
            }

        },
        // Years list



        // Get data from inputs
        getDataFromInputs() {
            for (const field of this.allInputs) {
                if (typeof this.input_data[field.model] === 'string') {
                    this.input_data[field.model] = this.input_data[field.model].trim();
                }
                if (!this.input_data[field.model]) {
                    this.input_data[field.model] = null;
                }
            }

            this.input_data['vin'] = this.vin;
        },
        // Get data from inputs



        // Create car
        async createCar() {
            this.getDataFromInputs();

            this.input_data['year_of_prod'] = this.year_of_prod;
            this.input_data['transmission'] = this.transmission.title;
            this.input_data['is_oc'] = this.oc;
            this.input_data['is_ac'] = this.ac;

            try {
                const response = await axios.post('api/car/create/', this.input_data);
                this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'success' });

                this.goBack()
            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error.response.data, type: 'error' });
            }
            this.loading = false;
        },
        // Create car


        // Reset form
        resetForm() {
            for (const field of this.allInputs) {
                this.input_data[field.model] = '';
            }
        },
        // Reset form



        // Get car data
        async getCarData(carVin) {

            try {
                const response = await axios.get(`api/car/get/${carVin}/`);
                this.editingCar = response.data;

                for (const field of this.allInputs) {
                    this.input_data[field.model] = this.editingCar[field.model];
                }

                this.year_of_prod = this.editingCar['year_of_prod'];
                this.transmission = this.editingCar['transmission'];
                this.oc = this.editingCar['is_oc'];
                this.ac = this.editingCar['is_ac'];
                this.vin = this.editingCar['vin'];
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }


        },
        // Get car data



        // Update car
        async updateCar() {
            // Generate dict for sending
            this.input_data['year_of_prod'] = this.year_of_prod;
            this.input_data['transmission'] = this.transmission.title;
            this.input_data['is_oc'] = this.oc;
            this.input_data['is_ac'] = this.ac;
            this.input_data['vin'] = this.vin;

            // Send put request
            try {
                const response = await axios.put(`api/car/edit/${this.carVin}/`, this.input_data);
                this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'success' });
                this.goBack()
            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error.response.data, type: 'error' });
            }
            this.loading = false;
        },
        // Update car



        // Go back
        goBack() {
            this.$root.changeCurrentComponent('ShowCarsComponent');
        },
        // Go back

    }
};
</script>
