<template>
    <v-card class="pa-4 rounded-xl" color="">
        <h1>Manage Fleets</h1>

        <h4>Select restaurant</h4>

        <v-autocomplete variant="solo-filled" v-model="selectedRestaurant" :items="restaurants.map(item => item.name)" label="Select Restaurant"
            item-text="name" item-value="id" @update:model-value="getFleet()">
        </v-autocomplete>



        <span v-if="selectedRestaurant !== null">

            <v-divider></v-divider>

            <h4>Select Cars</h4>

            <v-row>
                <v-col cols="12" sm="12">
                    <v-text-field variant="solo-filled" v-model="query" label="Search by Vin or License plate"
                        hint="Click enter to serach" clearable hide-actions @keydown.enter="getCars()"></v-text-field>
                </v-col>
            </v-row>

            <v-row>

                <!-- Available -->
                <v-col cols="12" sm="5" class="border border-3">
                    <h5 justify="center" align="center">Available cars</h5>
                    <v-data-table :headers="headers" :items="getAvailableCars" density="compact" :loading="loading" hover>

                        <!-- No data -->
                        <template v-slot:no-data>
                            <p class="text-h6 pa-5 text-danger">
                                <v-icon icon="mdi-database-alert-outline"></v-icon>
                                No available cars
                            </p>
                        </template>
                        <!-- No data -->


                        <template v-slot:item="{ item }">
                            <tr align="center" @click="selectCar(item.vin)" role="button">
                                <v-tooltip v-if="!form" activator="parent" location="top" no-overflow>
                                    Click to select
                                </v-tooltip>
                                <td v-for="header in headers" :key="header.key">
                                    {{ item[header.key] }}
                                </td>
                            </tr>
                        </template>

                    </v-data-table>
                </v-col>
                <!-- Available -->

                <v-col cols="2"></v-col>

                <!-- Selected -->
                <v-col cols="12" sm="5" class="border border-3">
                    <h5 justify="center" align="center">Selected cars </h5>
                    <v-data-table :headers="headers" :items="selectedCars" density="compact" :search="query" hover>

                        <!-- No data -->
                        <template v-slot:no-data>
                            <p class="text-h6 pa-5 text-danger">
                                <v-icon icon="mdi-database-alert-outline"></v-icon>
                                No available cars
                            </p>
                        </template>
                        <!-- No data -->


                        <template v-slot:item="{ item }">
                            <tr align="center" @click="unselectCar(item.vin)" role="button">
                                <v-tooltip v-if="!form" activator="parent" location="top" no-overflow>
                                    Click to unselect
                                </v-tooltip>
                                <td v-for="header in headers" :key="header.key">
                                    {{ item[header.key] }}
                                </td>
                            </tr>
                        </template>

                    </v-data-table>
                </v-col>
                <!-- Selected -->

                <v-row align="center" justify="center" class="my-2">
                    <v-col cols="6">
                        <v-btn color="success" :disabled="selectedCars.length == 0" block>Save</v-btn>
                    </v-col>
                </v-row>
            </v-row>


        </span>

    </v-card>


    <v-dialog v-model="addDialog" persistent width="500">
        <v-card width="auto">
            <div class="text-info text-h6 text-md-h5 text-lg-h4">
                <div class="d-flex justify-content-between align-items-center px-4 pt-4">
                    <v-icon icon="mdi-alert" class="text-h4" />
                    Alert
                    <v-icon icon="mdi-alert" class="text-h4" />
                </div>

                <hr />
            </div>

            <v-card-text class="text-h5">
                No fleet has beed found for this restaurant. You are about to create a new fleet.
            </v-card-text>

            <v-card-actions>

                <v-btn color="success" block text @click="addDialog = false">Ok</v-btn>

            </v-card-actions>

        </v-card>
    </v-dialog>






    <v-dialog v-model="dialogDelete" width="400">
        <v-card>
            <div class="text-danger text-h6 text-md-h5 text-lg-h4">
                <div class="d-flex justify-content-between align-items-center px-4 pt-4">
                    <v-icon icon="mdi-alert" class="text-h4" />
                    Warning
                    <v-icon icon="mdi-alert" class="text-h4" />
                </div>

                <hr />
            </div>

            <div class="pa-3" align="center">

                You are trying to delete
                <span class='fw-bolder'>
                    {{ deleteRestName }}
                </span>
                , this operation is <span class="fw-bold">irreversible</span>.
                Are you sure?

            </div>
            <hr>

            <div class="justify-center d-flex align-items-center mb-3">
                <v-btn variant="outlined" width="150" class="mr-5" @click="dialogDelete = false">No</v-btn>
                <v-btn width="150" @click="deleteRestaurant(deleteRestId)" color="red">
                    <v-icon icon="mdi-delete-empty"></v-icon>
                    Yes
                </v-btn>
            </div>

        </v-card>
    </v-dialog>
</template>

<script>
import axios from 'axios';

export default {
    name: 'AddFleet',
    data() {
        return {

            restaurants: [],
            selectedRestaurant: null,

            loading: true,
            query: '',

            allCars: [],
            availableCars: [],
            selectedCars: [],

            headers: [
                { title: 'License plate', key: 'license_plate', align: 'center', sortable: false },
                { title: 'Vin', key: 'vin', align: 'center', sortable: false },
            ],

            addDialog: false,

        };
    },

    computed: {
        getAvailableCars() {
            const selectedVins = this.selectedCars.map(car => car.vin);
            return this.allCars.filter(car => !selectedVins.includes(car.vin));
        },
    },

    methods: {


        // Get restaurants
        async getRestaurants() {
            try {
                const response = await axios.get('api/restaurant/get/name-id/');
                this.restaurants = response.data;
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
        },
        // Get restaurants



        // Get cars
        async getCars() {
            this.loading = true;

            try {
                const response = await axios.get('api/cars/get/', {
                    params: {
                        search: this.query,
                    }
                });
                this.allCars = response.data
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }

            this.loading = false;
        },
        // Get cars



        // Fetch fleet
        async getFleet() {

            this.loading = true;
            const rest_id = this.restaurants.find(restaurant => restaurant.name === this.selectedRestaurant).id;

            try {
                const response = await axios.get('api/fleet/get/', {
                    params: {
                        id: rest_id,
                    }
                });
            } catch (error) {
                this.addDialog = true;
            }

            this.loading = false;
        },
        // Fetch fleet



        // Move car to selected
        selectCar(vin) {
            const carIndex = this.allCars.findIndex(car => car.vin === vin);
            if (carIndex !== -1) {
                const selectedCar = this.allCars.splice(carIndex, 1)[0];
                this.selectedCars.push(selectedCar);
            }
        },
        // Move car to selected



        // Move user to unselected
        unselectCar(vin) {
            const carIndex = this.selectedCars.findIndex(car => car.vin === vin);
            if (carIndex !== -1) {
                const unselectedCar = this.selectedCars.splice(carIndex, 1)[0];
                this.allCars.push(unselectedCar);
            }
        },
        // Move user to unselected


    },
    mounted() {

        this.getRestaurants();
        this.getCars();
    },
};
</script>
