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
                <v-btn disabled variant="plain" color="blue"
                    @click="userDetails(item.columns.username, item.columns.user_role)">
                    <span class="material-symbols-outlined">
                        description
                    </span>
                    <v-tooltip activator="parent" location="top">Show user details</v-tooltip>
                </v-btn>
                <!-- Button show info -->



                <!-- Button edit -->
                <v-btn disabled variant="plain" color="green"
                    @click="editUser(item.columns.username, item.columns.user_role)">
                    <span class="material-symbols-outlined d-flex">
                        edit
                    </span>
                    <v-tooltip activator="parent" location="top">Edit</v-tooltip>
                </v-btn>
                <!-- Button edit -->



                <!-- Button delete -->
                <v-btn disabled variant="plain" color="red" @click="deleteConfirm(item.columns.username)">
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





<!-- 
    <div> -->




        <!-- <div v-if="cars.length === 0" class="text-danger fs-2">
            No records.
        </div>

        <div v-else class="table-responsive">
            <table class="table table-hover table-striped">
                <thead>
                    <tr class="text-center">
                        <th v-for="column in columns" :key="column.attribute">{{ column.label }}</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody class="table-group-divider">
                    <tr v-for="car in cars" :key="car.vin" class="text-center align-middle">
                        <td v-for="column in columns" :key="column.attribute">



                            <span v-if="car[column.attribute] === true">
                                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="green"
                                    class="bi bi-check-lg" viewBox="0 0 16 16">
                                    <path
                                        d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z" />
                                </svg>
                            </span>


                            <span v-else-if="car[column.attribute] === false">
                                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="red" class="bi bi-x-lg"
                                    viewBox="0 0 16 16">
                                    <path
                                        d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z" />
                                </svg>
                            </span>


                            <span v-else-if="car[column.attribute] === null">

                            </span>


                            <span v-else>
                                {{ car[column.attribute] }}
                            </span>
                        </td>
                        <td>

                            <button class="btn btn-outline-success m-3" @click="editCar(car.id)">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                    class="bi bi-pencil" viewBox="0 0 16 16">
                                    <path
                                        d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z" />
                                </svg>
                            </button>


                            <button class="btn btn-outline-danger" @click="deleteConfirm(car.vin)">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                    class="bi bi-trash3" viewBox="0 0 16 16">
                                    <path
                                        d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5ZM11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H2.506a.58.58 0 0 0-.01 0H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1h-.995a.59.59 0 0 0-.01 0H11Zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5h9.916Zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47ZM8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5Z" />
                                </svg>
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>



        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#confirmModal"
            id="confirm_modal_button" style="display: none;">
        </button>


        <div class="modal fade" id="confirmModal" tabindex="-1" aria-labelledby="confirmModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header d-flex justify-content-between text-warning">
                        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor"
                            class="bi bi-exclamation-triangle" viewBox="0 0 16 16">
                            <path
                                d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
                            <path
                                d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
                        </svg>
                        <h1 class="modal-title fs-5" id="confirmModalLabel">
                            Caution
                        </h1>
                        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor"
                            class="bi bi-exclamation-triangle" viewBox="0 0 16 16">
                            <path
                                d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
                            <path
                                d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
                        </svg>
                    </div>
                    <div class="modal-body text-danger fs-5">
                        <p>
                            You are trying to delete car - <span class="fw-bolder">vin {{ delete_vin }}</span> this
                            operation is <span class="fw-bold">irreversible</span>. Are you sure?
                        </p>
                    </div>
                    <div class="modal-footer d-flex justify-content-center">
                        <button type="button" class="btn btn-outline-secondary fs-5 w-25"
                            data-bs-dismiss="modal">No</button>
                        <button type="button" class="btn btn-danger fs-5 w-25" data-bs-dismiss="modal"
                            @click="deleteCar(vin)">Yes</button>
                    </div>
                </div>
            </div>
        </div>




    </div> -->
</template>

<script setup>
import { VDataTable } from 'vuetify/labs/VDataTable'
</script>


<script>
import axios from 'axios';

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


            delete_vin: '',
            necessaryHeaders: [
                { title: 'NO', align: 'center', sortable: false, key: 'rownumber' },
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

                // Add number for each row
                this.cars.forEach((car, index) => {
                    car.rownumber = index + 1;
                });

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


        deleteConfirm(vin) {
            this.delete_vin = vin;
            document.getElementById('confirm_modal_button').click();
        },

        async deleteCar() {
            try {
                const response = await axios.delete(`api/car/delete/${this.delete_vin}`);


                console.log(response)


                if (response.status === 204) {
                    this.loadcars();
                    this.dataSuccess = 'Success!'
                    document.getElementById('hiddenButton').click();

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
            localStorage.setItem('carid', carid)
            this.$parent.AddCarComponent()
        },

        search() {
            this.loadCars();
        },

        reloadComponent() {
            this.loadCars();
        },


    },
};
</script>