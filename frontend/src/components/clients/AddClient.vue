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







    <div>
        <div class="containter m-2 p-2 d-flex justify-content-center">
            <div class="col-12 col-md-9">

                <p v-if="res_name === null" class="fs-4 text-center fw-bolder">Add new Restaurant</p>
                <div v-else class="d-flex justify-content-between">
                    <div>
                        <button type="button" class="btn btn-outline-primary mb-3 " @click="goBack">
                            <span class="d-flex align-items-center">
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                                    class="bi bi-arrow-left me-2 " viewBox="0 0 16 16">
                                    <path fill-rule="evenodd"
                                        d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z" />

                                </svg>
                                Back
                            </span>
                        </button>
                    </div>
                    <div class="fs-4 text-center fw-bolder">Edit Restaurant</div>
                    <div></div>

                </div>

                <form action="" method="post" class="border rounded-3 p-3" @submit.prevent="createUser">


                    <!-- Basic information -->
                    <div class="border border-2 p-2 text-center mb-5 mt-2 fw-bolder shadow">
                        Basic information
                    </div>

                    <!-- First name -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Restaurant name
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="name"
                                aria-describedby="name" v-model="name"
                                :class="{ 'border border-danger': dataError && dataError['name'] }">
                        </div>
                    </div>
                    <!-- First name -->


                    <!-- Phone number -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Phone number
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="phone" class="form-control rounded-0 rounded-end" aria-label="phone"
                                aria-describedby="phone" v-model="phone"
                                :class="{ 'border border-danger': dataError && dataError['phone'] }">
                        </div>
                    </div>
                    <!-- Phone number -->


                    <!-- Location  -->
                    <div class="border border-2 p-2 text-center my-5 fw-bolder shadow">
                        Location
                    </div>


                    <!-- Residence address Country -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Country
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="country"
                                aria-describedby="country" v-model="country"
                                :class="{ 'border border-danger': dataError && dataError['country'] }">
                        </div>
                    </div>
                    <!-- Residence address Country -->


                    <!-- Residence address City -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            City
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="city"
                                aria-describedby="city" v-model="city"
                                :class="{ 'border border-danger': dataError && dataError['city'] }">
                        </div>
                    </div>
                    <!-- Residence address City -->


                    <!-- Residence address State -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            State
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="state"
                                aria-describedby="state" v-model="state"
                                :class="{ 'border border-danger': dataError && dataError['state'] }">
                        </div>
                    </div>
                    <!-- Residence address State -->


                    <!-- Residence address Street -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Street
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="street"
                                aria-describedby="street" v-model="street"
                                :class="{ 'border border-danger': dataError && dataError['street'] }">
                        </div>
                    </div>
                    <!-- Residence address Street -->


                    <div class="input-group mb-3 gx-0">

                        <!-- Residence address Home number -->
                        <div class="input-group">
                            <div
                                class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                Home
                            </div>
                            <div class="col-3 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end me-2" aria-label="home_number"
                                    aria-describedby="home_number" v-model="home_number"
                                    :class="{ 'border border-danger': dataError && dataError['home_number'] }">
                            </div>
                            <!-- Residence address Home number -->


                            <!-- Residence address Apartament number -->
                            <div
                                class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                Apartament
                            </div>
                            <div class="col-3 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end" aria-label="apartament_number"
                                    aria-describedby="apartament_number" v-model="apartament_number"
                                    :class="{ 'border border-danger': dataError && dataError['apartament_number'] }">
                            </div>
                            <!-- Residence address Apartament number -->
                        </div>

                    </div>


                    <!-- Residence Zip code -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Zip code
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="zip_code"
                                aria-describedby="zip_code" v-model="zip_code"
                                :class="{ 'border border-danger': dataError && dataError['zip_code'] }">
                        </div>
                    </div>
                    <!-- Residence Zip code -->


                    <!-- Managers  -->
                    <div class="border border-2 p-2 text-center my-5 fw-bolder shadow">
                        Managers
                    </div>



                    <!-- Managers -->
                    <div class="d-flex justify-content-center text-center mb-5 gap-5">

                        <!-- Avalible managers -->
                        <div class="col-5">
                            <div class="border rounded border-2 p-2" style="height: 40vh; overflow-y: auto;">
                                <p class="fw-bolder fs5">Available managers</p>
                                <hr>
                                <!-- search bar -->
                                <form role="search" method="POST" action="" @submit.prevent="search"
                                    class="d-flex justify-content-center mb-4">

                                    <div class="input-group w-75">

                                        <input class="form-control border-success" type="search"
                                            placeholder="Search managers" aria-label="Search" v-model="query"
                                            @keyup.enter="getAllUsernames">

                                    </div>
                                </form>
                                <!-- search bar -->


                                <div class="d-flex flex-column justify-content-center">
                                    <!-- Users list -->
                                    <button v-for="username in managersUsernames" :key="username.username" type="button"
                                        class="btn btn-outline-secondary mb-2 fw-bolder" @click="toggleUser(username)"
                                        :style="{ 'display': isSelected(username) ? 'none' : 'block' }">
                                        {{ username.username }}
                                    </button>
                                    <!-- Users list -->
                                </div>


                            </div>
                        </div>
                        <!-- Avalible managers -->

                        <!-- Choosen managers -->
                        <div class="col-5">
                            <div class="border border-success border-2 rounded p-2" style="height: 40vh; overflow-y: auto;">
                                <p class="fw-bolder fs5">Choosen managers</p>
                                <hr>


                                <!-- Users list -->
                                <button v-for="username in choosenUsernames" :key="username.username" type="button"
                                    class="btn btn-success w-75 mb-2 fw-bolder" @click="toggleUser(username)"
                                    :class="{ '': isSelected(username) }">
                                    {{ username.username }}
                                </button>
                                <!-- Users list -->



                            </div>
                        </div>
                        <!-- Choosen managers -->


                    </div>
                    <!-- Managers -->



                    <div class="text-center">
                        <button v-if="res_name === null" type="button" class="btn btn-success shadow"
                            @click="createRestaurant" :disabled="!isFormValid"
                            :class="{ 'btn-outline-danger': !isFormValid }">
                            <span class="d-flex align-items-center">
                                Create
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                                    class="bi bi-person-add ms-2" viewBox="0 0 16 16">
                                    <path
                                        d="M12.5 16a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Zm.5-5v1h1a.5.5 0 0 1 0 1h-1v1a.5.5 0 0 1-1 0v-1h-1a.5.5 0 0 1 0-1h1v-1a.5.5 0 0 1 1 0Zm-2-6a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM8 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4Z" />
                                    <path
                                        d="M8.256 14a4.474 4.474 0 0 1-.229-1.004H3c.001-.246.154-.986.832-1.664C4.484 10.68 5.711 10 8 10c.26 0 .507.009.74.025.226-.341.496-.65.804-.918C9.077 9.038 8.564 9 8 9c-5 0-6 3-6 4s1 1 1 1h5.256Z" />
                                </svg>
                            </span>
                        </button>


                        <!-- Button when editing existing user -->
                        <button v-else type="button" class="btn btn-success shadow" @click="updateUser">
                            <span class="d-flex align-items-center">
                                Save
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                                    class="bi bi-floppy ms-2" viewBox="0 0 16 16">
                                    <path d="M11 2H9v3h2V2Z" />
                                    <path
                                        d="M1.5 0h11.586a1.5 1.5 0 0 1 1.06.44l1.415 1.414A1.5 1.5 0 0 1 16 2.914V14.5a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 0 14.5v-13A1.5 1.5 0 0 1 1.5 0ZM1 1.5v13a.5.5 0 0 0 .5.5H2v-4.5A1.5 1.5 0 0 1 3.5 9h9a1.5 1.5 0 0 1 1.5 1.5V15h.5a.5.5 0 0 0 .5-.5V2.914a.5.5 0 0 0-.146-.353l-1.415-1.415A.5.5 0 0 0 13.086 1H13v4.5A1.5 1.5 0 0 1 11.5 7h-7A1.5 1.5 0 0 1 3 5.5V1H1.5a.5.5 0 0 0-.5.5Zm3 4a.5.5 0 0 0 .5.5h7a.5.5 0 0 0 .5-.5V1H4v4.5ZM3 15h10v-4.5a.5.5 0 0 0-.5-.5h-9a.5.5 0 0 0-.5.5V15Z" />
                                </svg>
                            </span>
                        </button>
                        <!-- Button when editing existing user -->
                    </div>
                </form>
            </div>

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

            // Inputs definisions
            basicInfoInputs: [
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

        this.getAllUsernames()

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

