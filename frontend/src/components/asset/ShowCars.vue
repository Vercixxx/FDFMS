<template>
    <div>

        <v-card elevation="1" class="pa-5 rounded-xl" color="teal-darken-2">

            <p class="p-2 fw-bolder text-h4">Options</p>

            <v-row>
                <v-col cols="7">
                    <!-- Combobox columns selection -->

                    <v-expansion-panels>
                        <v-expansion-panel title="Choose columns" elevation="1">

                            <v-expansion-panel-text>

                                <v-combobox variant="outlined" v-model="selectedColumns" :items="avaliableColumns"
                                    label="Select columns" prepend-icon="mdi-table-edit" multiple chips>

                                </v-combobox>
                            </v-expansion-panel-text>

                        </v-expansion-panel>
                    </v-expansion-panels>

                    <!-- Combobox columns selection -->
                </v-col>
                <v-col cols="5">
                    <!-- Search bar -->
                    <v-text-field variant="solo-filled" v-model="searchInput" @keydown.enter="searchTable = searchInput"
                        label="Search" class="px-1 " prepend-inner-icon="mdi-magnify" hide-actions clearable
                        hint="Press enter to search" />
                    <!-- Search bar -->
                </v-col>
            </v-row>

        </v-card>


        <v-divider thickness="12" class="rounded-xl my-7"></v-divider>

        <div>
            <h1>
                List of cars
            </h1>
        </div>

        <!-- Table -->
        <v-data-table :headers="updatedColumns" :items="cars" :search="searchTable" :loading="tableLoading"
            class="elevation-4 rounded-xl" item-value="id" v-model:items-per-page="itemsPerPage" hover select-strategy="all"
            show-current-page>



            <!-- No data -->
            <template v-slot:no-data>
                <p class="text-h4 pa-5">
                    <span class="material-symbols-outlined">
                        database
                    </span>
                    No data
                </p>
            </template>
            <!-- No data -->



            <!-- Maping oc -->
            <template #item.is_oc="{ item }">
                <v-icon v-if="item.columns.is_oc" icon="mdi-check-bold" style="color:green"></v-icon>
                <v-icon v-else icon="mdi-close-thick" style="color:red"></v-icon>
            </template>
            <!-- Maping oc -->

            <!-- Maping ac -->
            <template #item.is_ac="{ item }">
                <v-icon v-if="item.columns.is_ac" icon="mdi-check-bold" style="color:green"></v-icon>
                <v-icon v-else icon="mdi-close-thick" style="color:red"></v-icon>
            </template>
            <!-- Maping ac -->


            <!-- Action column -->
            <template v-slot:item.action="{ item }">
                <!-- Button show info -->
                <v-btn variant="plain" color="blue" @click="carDetailsFunct(item.columns.id)">
                    <span class="material-symbols-outlined">
                        description
                    </span>
                    <v-tooltip activator="parent" location="top">Show Car details</v-tooltip>
                </v-btn>
                <!-- Button show info -->



                <!-- Button edit -->
                <v-btn variant="plain" color="green" @click="editCar(item.columns.id)">
                    <span class="material-symbols-outlined d-flex">
                        edit
                    </span>
                    <v-tooltip activator="parent" location="top">Edit</v-tooltip>
                </v-btn>
                <!-- Button edit -->



                <!-- Button delete -->
                <v-btn variant="plain" color="red" @click="deleteConfirm(item.columns.id)">
                    <span class="material-symbols-outlined d-flex">
                        delete
                    </span>
                    <v-tooltip activator="parent" location="top">Delete</v-tooltip>
                </v-btn>
                <!-- Button delete -->
            </template>
            <!-- Buttons -->
            <!-- Action column -->

        </v-data-table>
        <!-- Table -->


    </div>


    <!-- Dialaogs section -->

    <!-- Delete car confirm -->
    <v-dialog v-model="dialogDelete" width="400">
        <v-card>
            <div class="text-warning text-h6 text-md-h5 text-lg-h4">

                <div class="d-flex justify-content-between align-items-center px-4 pt-4">
                    <span class="material-symbols-outlined">
                        warning
                    </span>
                    <span>
                        Warning
                    </span>
                    <span class="material-symbols-outlined">
                        warning
                    </span>
                </div>
                <hr>
            </div>

            <div class="pa-3" align="center">

                You are trying to delete car vin -
                <span class='fw-bolder'>
                    {{ deleteCarId }}
                </span>
                , this operation is <span class="fw-bold">irreversible</span>.
                Are you sure?

            </div>
            <hr>

            <div class="justify-center d-flex align-items-center mb-3">
                <v-btn variant="outlined" width="150" class="mr-5" @click="dialogDelete = false">No</v-btn>
                <v-btn width="150" @click="deleteCar(deleteCarId)" color="red">Yes</v-btn>
            </div>

        </v-card>
    </v-dialog>
    <!-- Delete car confirm -->


    <!-- Dialog details -->
    <v-dialog v-model="carDetailsDialog" width="auto">
        <v-card>
            <v-card-text>
                <v-table>
                    <thead>
                        <tr>
                            <th class="text-left">
                                Name
                            </th>
                            <th class="text-left">
                                Value
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(value, key) in carDetails" :key="key">
                            <td>{{ key }}</td>
                            <td v-if="value === null">
                                <v-icon icon="mdi-minus-thick"></v-icon>
                            </td>

                            <td v-else-if="value === true">
                                <v-icon icon="mdi-check-bold" style="color:green"></v-icon>
                            </td>

                            <td v-else-if="value === false">
                                <v-icon icon="mdi-close-thick" style="color:red"></v-icon>
                            </td>

                            <td v-else>
                                {{ value }}
                            </td>

                        </tr>
                    </tbody>
                </v-table>

            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" block @click="carDetailsDialog = false">Close</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
    <!-- dialog -->

    <!-- Dialog details -->

</template>

<script setup>
import { VDataTable } from 'vuetify/labs/VDataTable'
</script>


<script>
import axios from 'axios';
import useEventsBus from '../../plugins/eventBus.js'
const { emit } = useEventsBus()

export default {
    name: 'App',

    data() {
        return {
            cars: [],
            columns: [],
            itemsPerPage: 25,
            searchInput: '',
            searchTable: '',
            tableLoading: false,
            selectedColumns: [],
            avaliableColumns: [],

            dialogDelete: false,
            deleteCarId: '',

            carDetailsDialog: false,
            carDetails: [],



            necessaryHeaders: [
                { title: 'Id', align: 'center', sortable: false, key: 'id' },
                { title: 'VIN', key: 'vin', align: 'center', sortable: false },
            ],
            columns: [
                { title: 'Brand', key: 'brand', align: 'center', sortable: false },
                { title: 'Model', key: 'model', align: 'center', sortable: false },
                { title: 'Color', key: 'color', align: 'center', sortable: false },
                { title: 'Production year', key: 'year_of_prod', align: 'center', sortable: false },
                { title: 'Mileage', key: 'mileage', align: 'center', sortable: false },
                { title: 'Engine capacity', key: 'engine_cap', align: 'center', sortable: false },
                { title: 'Engine power', key: 'engine_pow', align: 'center', sortable: false },
                { title: 'Transmission', key: 'transmission', align: 'center', sortable: false },
                { title: 'Insurance number', key: 'policy_number', align: 'center', sortable: false },
                { title: 'Insurance phone number', key: 'phone_policy_contact', align: 'center', sortable: false },
                { title: 'OC', key: 'is_oc', align: 'center', sortable: false },
                { title: 'AC', key: 'is_ac', align: 'center', sortable: false },
                { title: 'ACTIONS', align: 'center', key: 'action', sortable: false },
            ],



        };
    },

    computed: {
        updatedColumns() {
            return [...this.necessaryHeaders, ...this.selectedColumns];
        },
    },

    created() {
        this.loadCars();

        this.selectedColumns = this.columns;
        this.avaliableColumns = this.columns;
    },

    methods: {
        async loadCars() {
            try {
                const response = await axios.get('api/cars/get-cars/', {
                    params: {
                        limit: this.cars_per_site,
                        offset: this.currentPage,
                        search: this.query,
                    }
                });

                this.cars = response.data;

                this.tableLoading = false;

            }
            catch (error) {
                console.error('Error when fetching', error);
            }
        },

        previousPage() {
            this.currentPage -= 1;
            this.loadcars();
        },
        nextPage() {
            this.currentPage += 1;
            this.loadcars();
        },


        deleteConfirm(carid) {
            this.deleteCarId = carid;
            this.dialogDelete = true;
        },


        async deleteCar() {
            this.dialogDelete = false;
            try {
                const response = await axios.delete(`api/car/delete/${this.deleteCarId}`);


                if (response.status === 204) {
                    this.loadCars()

                    const messageData = {
                        message: `Successfully deleted car id - ${this.deleteCarId}`,
                        type: 'success'
                    };

                    localStorage.setItem('message', JSON.stringify(messageData));
                    emit('message', '');

                }
                else {
                    this.loadcars();
                    this.dataError = 'Error!'
                    document.getElementById('hiddenButton').click();
                }


            }
            catch (error) {
                console.error('Error when fetching', error);
            }
        },

        editCar(carid) {
            localStorage.setItem('carid', carid);
            this.$root.changeCurrentComponent('AddCarsComponent');
        },

        search() {
            this.loadCars();
        },

        reloadComponent() {
            this.loadCars();
        },

        async carDetailsFunct(car_id) {
            const response = await axios.get(`api/car/get/${car_id}/`);
            console.log(response)
            this.carDetails = response.data;
            this.carDetailsDialog = true;

        },


    },
};
</script>