<template>
    <v-card class="pa-4 rounded-xl" color="">
        <h1>Manage Fleets</h1>

        <h4>Select restaurant</h4>

        <v-autocomplete variant="solo-filled" v-model="selectedRestaurant" :items="restaurants.map(item => item.name)"
            label="Select Restaurant" item-text="name" item-value="id" @update:model-value="getFleet()">
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
                <v-col cols="12" sm="5">
                    <h5 justify="center" align="center">Available cars</h5>
                    <v-data-table :headers="headers" :items="availableCars" density="compact" :loading="loading" hover>

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
                <v-col cols="12" sm="5">

                    <v-row>
                        <v-col align="center" class="text-h4 mb-5">
                            Selected cars ({{ selectedCars.length }})
                        </v-col>
                        <v-col cols="auto">
                            <!-- Delete fleet -->
                            <span>
                                <v-tooltip activator="parent" location="top" no-overflow>
                                    Delete fleet
                                </v-tooltip>
                                <span>
                                    <v-btn v-if="editing" variant="text" type="submit" icon="mdi-delete"
                                        @click="confirmDeleteFleet()" id="deleteButton">
                                    </v-btn>
                                </span>
                            </span>
                            <!-- Delete fleet -->
                        </v-col>
                    </v-row>


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

                        <template v-slot:bottom>
                        </template>

                    </v-data-table>
                </v-col>
                <!-- Selected -->

                <v-row>
                    <v-col align="center" justify="center">
                        <span>
                            <v-tooltip v-if="selectedCars.length == 0" activator="parent" location="top" no-overflow>
                                Fleet must contain at least one car
                            </v-tooltip>
                            <span>
                                <v-btn variant="outlined" :disabled="selectedCars.length == 0" :loading="loading"
                                    :color="selectedCars.length == 0 ? 'danger' : 'success'" size="large" type="submit"
                                    class="mt-10 mb-5 font-weight-black" :text="editing ? 'Save' : 'Add'"
                                    @click="addOrEditFleet()">
                                </v-btn>
                            </span>
                        </span>
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




    <v-dialog v-model="dialogDelete" width="500" persistent>
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
                    {{ selectedRestaurant }} fleet
                </span>
                , this operation is <span class="fw-bold">irreversible</span>.
                Are you sure?

            </div>
            <hr>

            <div class="justify-center d-flex align-items-center mb-3">
                <v-btn variant="outlined" width="150" class="mr-5" @click="dialogDelete = false">No</v-btn>
                <v-btn width="150" @click="deleteFleet()" color="red">
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
    name: 'ManageFleets',
    data() {
        return {

            restaurants: [],
            selectedRestaurant: null,
            selectedFleetId: null,

            loading: true,
            query: '',

            editing: false,

            allCars: [],
            availableCars: [],
            selectedCars: [],

            dialogDelete: false,

            headers: [
                { title: 'License plate', key: 'license_plate', align: 'center', sortable: false },
                { title: 'Vin', key: 'vin', align: 'center', sortable: false },
            ],

            addDialog: false,

        };
    },

    computed: {
        availableCars() {
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


            this.editing = false;
            const rest_id = this.restaurants.find(restaurant => restaurant.name === this.selectedRestaurant).id;
            this.selectedCars = [];

            try {
                const response = await axios.get('api/fleet/get/', {
                    params: {
                        rest_id: rest_id,
                    }
                });

                this.selectedCars = this.allCars.filter(car => response.data.cars.includes(car.vin));
                this.selectedFleetId = response.data.id;
                this.editing = true;


            } catch (error) {
                this.addDialog = true;
            }


        },
        // Fetch fleet



        // Move car to selected
        selectCar(vin) {
            const carIndex = this.allCars.findIndex(car => car.vin === vin);
            if (carIndex !== -1) {
                const selectedCar = this.allCars[carIndex];
                this.selectedCars.push(selectedCar);
            }
        },
        // Move car to selected



        // Move user to unselected
        unselectCar(vin) {
            const carIndex = this.selectedCars.findIndex(car => car.vin === vin);
            if (carIndex !== -1) {
                this.selectedCars.splice(carIndex, 1)[0];
            }
        },
        // Move user to unselected



        // Add Fleet
        async addOrEditFleet() {

            this.loading = true;

            if (this.editing) {
                try {
                    const response = await axios.put('api/fleet/edit/', {
                        fleet_id: this.selectedFleetId,
                        cars: this.selectedCars.map(car => car.vin),
                    });

                    this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'teal' });

                } catch (error) {
                    this.$store.dispatch('triggerAlert', { message: error.response.data, type: 'error' });
                }

                this.editing = false;
            }

            // Add
            else {
                try {
                    const response = await axios.post('api/fleet/add/', {
                        restaurant: this.selectedRestaurant,
                        cars: this.selectedCars.map(car => car.vin),
                    });

                    this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'teal' });

                } catch (error) {
                    this.$store.dispatch('triggerAlert', { message: error.response.data, type: 'error' });
                }
            }

            this.loading = false;
            this.selectedRestaurant = null;
        },
        // Add Fleet



        // Confirm delete fleet
        confirmDeleteFleet() {
            this.dialogDelete = true;
        },
        // Confirm delete fleet



        // Delete fleet
        async deleteFleet() {
            try {
                const response = await axios.delete(`api/fleet/delete/${this.selectedFleetId}/`);
                this.$store.dispatch('triggerAlert', { message: 'Fleet deleted successfully', type: 'teal' });

            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error.response.data, type: 'error' });
            }

            this.dialogDelete = false;
            this.editing = false;
            this.selectedRestaurant = null;
        }
        // Delete fleet

    },
    mounted() {

        this.getRestaurants();
        this.getCars();
    },
};
</script>


<style>
#deleteButton:hover {
    color: red;
}
</style>