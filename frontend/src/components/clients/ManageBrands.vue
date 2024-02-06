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
                                            @update:model-value="loadBrands()"></v-select>
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
                    Brands
                </div>
            </v-col>
            <v-col justify="end" cols="12" sm="4">

                <!-- Search bar -->
                <v-text-field variant="solo-filled" v-model="query" @keydown.enter="loadBrands()" label="Search"
                    prepend-inner-icon="mdi-magnify" hide-actions clearable hint="Press enter to search" />
                <!-- Search bar -->

            </v-col>
        </v-row>


        <!-- Table -->
        <v-data-table :headers="updatedColumns" :items="brands" :loading="loading" density="compact"
            class="elevation-4 rounded-xl" item-value="id" v-model:items-per-page="itemsPerPage" hover select-strategy="all"
            show-current-page>

            <!-- Loading -->
            <template v-slot:loading>
                <v-skeleton-loader type="table-row@10"></v-skeleton-loader>
            </template>
            <!-- Loading -->

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
                <tr align="center">
                    <td v-for="header in updatedColumns" :key="header.key">

                        <template v-if="header.key === 'action'">
                            <span>
                                <v-btn variant="plain" color="blue" @click="brandDetailsFunct(item.id)">
                                    <v-icon icon="mdi-book-open-page-variant-outline" class="text-h5"></v-icon>
                                    <v-tooltip activator="parent" location="top">Show {{ item.name }}
                                        details</v-tooltip>
                                </v-btn>

                                <v-btn variant="plain" color="green" @click="editBrand(item.id)">
                                    <v-icon icon="mdi-pencil-outline" class="text-h5"></v-icon>
                                    <v-tooltip activator="parent" location="top">Edit {{ item.name }}</v-tooltip>
                                </v-btn>

                                <v-btn variant="plain" color="red" @click="deleteConfirm(item.id)">
                                    <v-icon icon="mdi-delete-empty" class="text-h5"></v-icon>
                                    <v-tooltip activator="parent" location="top">Delete {{ item.name }}</v-tooltip>
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
                <v-btn color="primary" block @click="brandDetailsDialog = false">Close</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
    <!-- dialog -->

    <!-- Dialog details -->
</template>



<script>
import axios from 'axios';

export default {
    name: 'App',

    data() {
        return {
            brands: [],
            columns: [],

            itemsPerPage: 10,
            paginationPage: 1,
            pagiController: {},
            query: '',

            loading: true,
            selectedColumns: [],
            avaliableColumns: [],

            dialogDelete: false,
            deleteBrandId: '',

            brandDetailsDialog: false,
            brandDetails: [],


            // Headers
            necessaryHeaders: [
                { title: 'No', align: 'center', sortable: true, key: 'rownumber' },
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
            ],
            actions: [
                { title: 'ACTIONS', align: 'center', key: 'action', sortable: false },
            ],
            // Headers

        }
    },



    computed: {
        updatedColumns() {
            return [...this.necessaryHeaders, ...this.selectedColumns, ...this.actions];
        },
    },



    created() {
        this.loadBrands();

        this.selectedColumns = this.columns;
        this.avaliableColumns = this.columns;
    },



    methods: {

        // Load all brands
        async loadBrands(url) {
            this.loading = true;

            try {
                const response = url
                    ? await axios.get(url)
                    : await axios.get('api/brands/get-all/', {
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

                this.brands = response.data.results;


                // Add number for each row
                this.brands.forEach((brand, index) => {
                    brand.rownumber = index + 1;
                });

            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }

            this.loading = false;
        },
        // Load all brands




        // Previous page
        async prevPage() {
            await this.loadBrands(this.pagiController.previous);
        },
        // Previous page



        // Next page
        async nextPage() {
            await this.loadBrands(this.pagiController.next);
        },
        // Next page



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
                this.loadBrands()
                this.$store.dispatch('triggerAlert', { message: `Successfully deleted brand id - ${this.deleteBrandId}`, type: 'success' });
            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
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

            try {
                const response = await axios.get(`api/brands/get-info/${brandID}/`);

                this.brandDetails = {};
                Object.keys(response.data).forEach(key => {
                    let formattedKey = key.replace(/_/g, ' ');
                    formattedKey = formattedKey.replace(/\b\w/g, firstChar => firstChar.toUpperCase());
                    this.brandDetails[formattedKey] = response.data[key];
                });
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }

            this.brandDetailsDialog = true;

        },
        // Brand details


    },

}
</script>