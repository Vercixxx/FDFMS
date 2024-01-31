<template>
    <div>

        <div class="mt-5 mb-5">


            <v-row>
                <v-col cols="12" sm="12">
                    <v-expansion-panels>
                        <v-expansion-panel title="Filters" elevation="1" style="border: 1px solid teal;">

                            <v-expansion-panel-text>

                                <v-row justify="center" align="center">
                                    <v-col cols="auto">
                                        <v-combobox variant="outlined" v-model="selectedColumns" :items="avaliableColumns"
                                            label="Select columns" prepend-icon="mdi-table-edit" multiple chips>
                                        </v-combobox>
                                    </v-col>

                                    <v-col cols="12" sm="2">
                                        <v-select v-model="itemsPerPage" variant="solo-filled" :items="[5, 10, 25, 50, 100]"
                                            :label="`Items per page - ${itemsPerPage}`"
                                            @update:model-value="loadCars()"></v-select>
                                    </v-col>
                                </v-row>

                            </v-expansion-panel-text>

                        </v-expansion-panel>
                    </v-expansion-panels>
                </v-col>

            </v-row>

        </div>

        <v-row>
            <v-col justify="start">
                <div class="text-h4 ma-5 font-weight-bold">
                    Cars
                </div>
            </v-col>
            <v-col justify="end" cols="12" sm="4">

                <!-- Search bar -->
                <v-text-field variant="solo-filled" v-model="query" @keydown.enter="loadCars()" label="Search"
                    prepend-inner-icon="mdi-magnify" hide-actions clearable hint="Press enter to search" />
                <!-- Search bar -->

            </v-col>
        </v-row>


        <!-- Table -->
        <v-data-table :headers="updatedColumns" :items="cars" :loading="loading" density="compact"
            class="elevation-4 rounded-xl" item-value="vin" v-model:items-per-page="itemsPerPage" hover show-current-page>



            <!-- No data -->
            <template v-slot:no-data>
                <p class="text-h4 pa-5">
                    <v-icon icon="mdi-database-alert-outline" color="red"></v-icon>
                    No data
                </p>
            </template>
            <!-- No data -->



            <!-- Accessing table cells -->
            <template v-slot:item="{ item }">
                <tr align="center" :style="item.active ? '' : 'color: red'">
                    <td v-for="header in updatedColumns" :key="header.key">
                        <template v-if="header.key === 'action'">
                            <span>
                                <v-btn variant="plain" color="danger" @click="showCarDamages(item.vin)">
                                    <v-icon icon="mdi-car-wrench" class="text-h5"></v-icon>
                                    <v-tooltip activator="parent" location="top">Show {{ item.brand }} {{ item.model }}
                                        damages</v-tooltip>
                                </v-btn>

                                <v-btn variant="plain" color="blue" @click="carDetailsFunct(item.vin)">
                                    <v-icon icon="mdi-book-open-page-variant-outline" class="text-h5"></v-icon>
                                    <v-tooltip activator="parent" location="top">Show {{ item.brand }} {{ item.model }}
                                        details</v-tooltip>
                                </v-btn>

                                <v-btn variant="plain" color="green" @click="editCar(item.vin)">
                                    <v-icon icon="mdi-pencil-outline" class="text-h5"></v-icon>
                                    <v-tooltip activator="parent" location="top">Edit {{ item.brand }} {{ item.model }}
                                    </v-tooltip>
                                </v-btn>

                                <v-btn variant="plain" color="red" @click="deleteConfirm(item.vin)">
                                    <v-icon icon="mdi-delete-empty" class="text-h5"></v-icon>
                                    <v-tooltip activator="parent" location="top">Delete {{ item.brand }} {{ item.model }}
                                    </v-tooltip>
                                </v-btn>
                            </span>
                        </template>


                        <template v-else>
                            <span
                                v-if="item[header.key] === null || item[header.key] === undefined || item[header.key] === ''">
                                <v-icon icon="mdi-minus" />
                            </span>
                            <span v-else-if="item[header.key] === true">
                                <v-icon icon="mdi-check-bold" style="color:green" />
                            </span>
                            <span v-else-if="item[header.key] === false">
                                <v-icon icon="mdi-close-thick" style="color:red" />
                            </span>
                            <span v-else>
                                {{ item[header.key] }}
                            </span>
                        </template>

                    </td>
                </tr>
            </template>
            <!-- Accessing table cells -->


            <template v-slot:bottom="{ page, itemsPerPage }">
                <v-row>
                    <v-col align="center">
                        <v-pagination v-model="paginationPage" :length="pagiController.total_pages" @next="nextPage()"
                            @prev="prevPage()">
                            <template v-slot:item="{ key, page }">
                                <v-btn class="mt-1" variant="text" disabled rounded="xl">{{ key }}</v-btn>
                            </template>
                        </v-pagination>
                        <p>Page {{ pagiController.currentPage }} of {{ pagiController.total_pages }}</p>
                        <p>{{ pagiController.totalRecors }} Records total</p>
                    </v-col>
                </v-row>
            </template>


        </v-data-table>
        <!-- Table -->



    </div>


    <!-- Dialaogs section -->

    <!-- Delete car confirm -->
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

                You are trying to delete car vin -
                <span class='fw-bolder'>
                    {{ deleteCarVin }}
                </span>
                , this operation is <span class="fw-bold">irreversible</span>.
                Are you sure?

            </div>
            <hr>

            <div class="justify-center d-flex align-items-center mb-3">
                <v-btn variant="outlined" width="150" class="mr-5" @click="dialogDelete = false">No</v-btn>
                <v-btn width="150" @click="deleteCar(deleteCarVin)" color="red">Yes</v-btn>
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
                            <td v-if="value === null || value === undefined || value === ''">
                                <v-icon icon="mdi-minus" />
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

    <!-- Car Damages  -->
    <v-dialog persistent v-model="carDamagesDialog" fullscreen :scrim="false" transition="dialog-bottom-transition">
        <v-card>
            <v-card-title class="bg-deep-purple-lighten-1">
                <v-row>
                    <v-col class="text-h4">
                        Car Damages for [BRAND MODEL License plate]
                    </v-col>
                    <v-col align="end">
                        <v-btn variant="outlined" color="red" @click="carDamagesDialog = false" icon="mdi-close">
                        </v-btn>
                    </v-col>
                </v-row>
            </v-card-title>

            <v-card-text>
                <v-data-table :headers="carDamagesHeaders">

                </v-data-table>
            </v-card-text>

        </v-card>
    </v-dialog>
    <!-- Car Damages  -->
</template>


<script>
import axios from 'axios';

export default {
    name: 'App',

    data() {
        return {
            loading: true,

            cars: [],
            columns: [],

            itemsPerPage: 10,
            paginationPage: 1,
            pagiController: {},
            query: '',

            selectedColumns: [],
            avaliableColumns: [],

            dialogDelete: false,
            deleteCarVin: '',

            carDetailsDialog: false,
            carDetails: [],

            carDamagesDialog: false,
            carDamagesVin: null,
            carDamages: [],

            necessaryHeaders: [
                { title: 'No', align: 'center', sortable: false, key: 'rownumber' },
                { title: 'VIN', key: 'vin', align: 'center', sortable: false },
            ],
            columns: [
                { title: 'License plate', key: 'license_plate', align: 'center', sortable: false },
                { title: 'Active status', key: 'active', align: 'center', sortable: false },
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
            ],
            actions: [
                { title: 'ACTIONS', align: 'center', key: 'action', sortable: false },
            ],

            carDamagesHeaders: [
                { title: 'Reported by', align: 'center', sortable: false, key: 'rownumber' },
                { title: 'Reported date', align: 'center', sortable: false, key: 'rownumber' },
                { title: 'Car license plate', align: 'center', sortable: false, key: 'rownumber' },
                { title: 'Mileage', align: 'center', sortable: false, key: 'rownumber' },
                { title: 'VIN', key: 'vin', align: 'center', sortable: false },
                { title: 'Description', key: 'vin', align: 'center', sortable: false },
            ],

        };
    },

    computed: {
        updatedColumns() {
            return [...this.necessaryHeaders, ...this.selectedColumns, ...this.actions];
        },
    },

    created() {
        this.loadCars();

        this.selectedColumns = this.columns.filter(column =>
            ['license_plate', 'active', 'mileage'].includes(column.key)
        );
        this.avaliableColumns = this.columns;
    },

    methods: {

        // Show car damages
        async showCarDamages(carVin) {
            this.carDamagesVin = carVin;
            this.carDamagesDialog = true;
        },
        // Show car damages



        // Load cars
        async loadCars(url) {
            this.loading = true;
            try {
                const response = url
                    ? await axios.get(url)
                    : await axios.get('api/car/getall/', {
                        params: {
                            limit: this.itemsPerPage,
                            search: this.query,
                        }
                    });

                this.pagiController = {
                    total_pages: response.data.total_pages,
                    posts_amount: response.data.posts_amount,
                    next: response.data.next,
                    previous: response.data.previous,
                    currentPage: response.data.current_page,
                    totalRecors: response.data.total_results,
                }

                this.cars = response.data.results;

                // Add number for each row
                this.cars.forEach((car, index) => {
                    car.rownumber = index + 1;
                });

            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
            this.loading = false;
        },
        // Load cars



        // Previous page
        async prevPage() {
            await this.loadCars(this.pagiController.previous);
        },
        // Previous page



        // Next page
        async nextPage() {
            await this.loadCars(this.pagiController.next);
        },
        // Next page



        // Delete car confirm
        deleteConfirm(carVin) {
            this.deleteCarVin = carVin;
            this.dialogDelete = true;
        },
        // Delete car confirm



        // Delete car
        async deleteCar() {
            this.dialogDelete = false;

            try {
                const response = await axios.delete(`api/car/delete/${this.deleteCarVin}/`);
                this.loadCars()
                this.$store.dispatch('triggerAlert', { message: `Successfully deleted car Vin - ${this.deleteCarVin}`, type: 'success' });

            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
        },
        // Delete car



        // Edit car
        editCar(carVin) {
            localStorage.setItem('carVin', carVin);
            this.$root.changeCurrentComponent('AddCarsComponent');
        },
        // Edit car



        // Show car details
        async carDetailsFunct(carVin) {
            try {
                const response = await axios.get(`api/car/get/${carVin}/`);

                this.carDetails = {};
                Object.keys(response.data).forEach(key => {
                    let formattedKey = key.replace(/_/g, ' ');
                    formattedKey = formattedKey.replace(/\b\w/g, firstChar => firstChar.toUpperCase());
                    this.carDetails[formattedKey] = response.data[key];
                });
            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
            this.carDetailsDialog = true;
        },
        // Show car details






    },
};
</script>