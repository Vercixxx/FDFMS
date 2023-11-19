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
                Brands
            </h1>
        </div>

        <!-- Table -->
        <v-data-table :headers="updatedColumns" :items="brands" :search="searchTable" :loading="tableLoading"
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


            <template #item="{ item }">
                <tr>
                    <td v-for="(cell, columnIndex) in item.columns" :key="item.columns.id" class="text-center">
                        <span v-if="cell === null">
                            <v-icon icon="mdi-minus-thick" color="red-lighten-2"></v-icon>
                        </span>
                        <span v-else-if="cell === true">
                            <v-icon icon="mdi-check-bold" style="color:green"></v-icon>
                        </span>
                        <span v-else-if="cell === false">
                            <v-icon icon="mdi-close-thick" style="color:red"></v-icon>
                        </span>
                        <span v-else>
                            {{ cell }}
                        </span>

                        <!-- Actions -->
                        <template v-if="columnIndex === 'action'">
                            <v-btn variant="plain" color="blue" @click="brandDetailsFunct(item.columns.id )">
                                <span class="material-symbols-outlined">
                                    description
                                </span>
                                <v-tooltip activator="parent" location="top">Show brand details</v-tooltip>
                            </v-btn>

                            <v-btn variant="plain" color="green" @click="editBrand(item.columns.id )">
                                <span class="material-symbols-outlined d-flex">
                                    edit
                                </span>
                                <v-tooltip activator="parent" location="top">Edit</v-tooltip>
                            </v-btn>

                            <v-btn variant="plain" color="red" @click="deleteConfirm(item.columns.id )">
                                <span class="material-symbols-outlined d-flex">
                                    delete
                                </span>
                                <v-tooltip activator="parent" location="top">Delete</v-tooltip>
                            </v-btn>
                        </template>
                        <!-- Actions -->
                    </td>
                </tr>
            </template>

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

                You are trying to delete brand id -
                <span class='fw-bolder'>
                    {{ deleteBrandId }}
                </span>
                , this operation is <span class="fw-bold">irreversible</span>.
                Are you sure?

            </div>
            <hr>

            <div class="justify-center d-flex align-items-center mb-3">
                <v-btn variant="outlined" width="150" class="mr-5" @click="dialogDelete = false">No</v-btn>
                <v-btn width="150" @click="deleteBrand(deleteBrandId)" color="red">Yes</v-btn>
            </div>

        </v-card>
    </v-dialog>
    <!-- Delete car confirm -->


    <!-- Dialog details -->
    <v-dialog v-model="brandDetailsDialog" width="auto">
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
                        <tr v-for="(value, key) in brandDetails" :key="key">
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
                <v-btn color="primary" block @click="brandDetailsDialog = false">Close</v-btn>
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
            brands: [],
            columns: [],
            itemsPerPage: 25,
            searchInput: '',
            searchTable: '',
            tableLoading: false,
            selectedColumns: [],
            avaliableColumns: [],

            dialogDelete: false,
            deleteBrandId: '',

            brandDetailsDialog: false,
            brandDetails: [],


            // Headers
            necessaryHeaders: [
                { title: 'Id', align: 'center', sortable: true, key: 'id' },
            ],
            columns: [
                { title: 'Name', key: 'name', align: 'center', sortable: true },
                { title: 'Phone', key: 'phone', align: 'center', sortable: false },
                { title: 'Country', key: 'country', align: 'center', sortable: false },
                { title: 'City', key: 'city', align: 'center', sortable: true },
                { title: 'State', key: 'state', align: 'center', sortable: false },
                { title: 'Street', key: 'street', align: 'center', sortable: false },
                { title: 'Home', key: 'home', align: 'center', sortable: false },
                { title: 'Apartament', key: 'apartament', align: 'center', sortable: false },
                { title: 'Zip code', key: 'zip', align: 'center', sortable: false },
                { title: 'Actions', key: 'action', align: 'center', sortable: false },
            ],
            // Headers

        }
    },



    computed: {
        updatedColumns() {
            return [...this.necessaryHeaders, ...this.selectedColumns];
        },
    },



    created() {
        this.loadBrands();

        this.selectedColumns = this.columns;
        this.avaliableColumns = this.columns;
    },



    methods: {

        // Load all brands
        async loadBrands() {
            try {
                const response = await axios.get('api/brands/get-all/');

                this.brands = response.data;

                this.tableLoading = false;

            }
            catch (error) {
                console.error('Error when fetching', error);
            }
        },
        // Load all brands



        // Deleting brand confirmation
        deleteConfirm(carid) {
            this.deleteBrandId = carid;
            this.dialogDelete = true;
        },
        // Deleting brand confirmation



        // Deleting brand method
        async deleteBrand() {
            this.dialogDelete = false;
            try {
                const response = await axios.delete(`api/brands/delete/${this.deleteBrandId}`);


                if (response.status === 204) {
                    this.loadBrands()

                    const messageData = {
                        message: `Successfully deleted brand id - ${this.deleteBrandId}`,
                        type: 'success'
                    };

                    localStorage.setItem('message', JSON.stringify(messageData));
                    emit('message', '');

                }
                else {
                    this.loadBrands();
                    this.dataError = 'Error!'
                    document.getElementById('hiddenButton').click();
                }


            }
            catch (error) {
                console.error('Error when fetching', error);
            }
        },
        // Deleting brand method



        // Editing brand
        editBrand(brandID) {
            localStorage.setItem('brandID', brandID);
            this.$root.changeCurrentComponent('AddBrandComponent');
        },
        // Editing brand



        // Brand details
        async brandDetailsFunct(brandID) {
            const response = await axios.get(`api/brands/get-info/${brandID}/`);
            this.brandDetails = response.data;
            this.brandDetailsDialog = true;

        },
        // Brand details


    },

}
</script>