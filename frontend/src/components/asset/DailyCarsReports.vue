<template>
    <div>


        <v-row>

            <v-col cols="12" sm="12">
                <v-expansion-panels>
                    <v-expansion-panel title="Options" elevation="1" style="border: 1px solid teal;">

                        <v-expansion-panel-text>
                            <v-row justify="center" align="center">
                                <v-col cols="12" sm="6">
                                    <v-select v-model="itemsPerPage" variant="solo-filled" :items="[5, 10, 25, 50, 100]"
                                        :label="`Items per page - ${itemsPerPage}`"
                                        @update:model-value="getReports()"></v-select>
                                </v-col>

                                <v-col cols="12" sm="6">

                                    <v-btn text="Download" block @click="getReports(undefined, true)" color="primary"
                                        variant="outlined" append-icon="mdi-download">
                                    </v-btn>
                                </v-col>

                            </v-row>

                        </v-expansion-panel-text>
                    </v-expansion-panel>
                </v-expansion-panels>

            </v-col>


        </v-row>



        <v-row>
            <v-col justify="start">
                <div class="text-h4 ma-5 font-weight-bold">
                    Daily Cars Reports
                </div>
            </v-col>
            <v-col justify="end" cols="12" sm="4">

                <!-- Search bar -->
                <v-text-field variant="solo-filled" v-model="query" @keydown.enter="getReports()" label="Search"
                    class="px-1 " prepend-inner-icon="mdi-magnify" hide-actions clearable hint="Press enter to search" />
                <!-- Search bar -->

            </v-col>
        </v-row>


        <v-data-table :items="reports" :headers="headers" show-current-page :loading="loading" show-expand
            v-model:expanded="expanded" item-value="id" density="compact">


            <!-- Expanded rows -->
            <template v-slot:expanded-row="{ columns, item }">
                <tr>
                    <td :colspan="columns.length">

                        <v-card-item>
                            <v-item-title>
                                {{ item.additional_remarks }}

                            </v-item-title>
                        </v-card-item>


                    </td>
                </tr>
            </template>

            <template v-slot:header.data-table-expand="{ text }">
                Additional remarks
            </template>
            <!-- Expanded rows -->


            <!-- No data -->
            <template v-slot:no-data>
                <p class="text-h4 pa-5">
                    <v-icon icon="mdi-database-alert-outline" color="red"></v-icon>
                    No data
                </p>
            </template>
            <!-- No data -->

            <!-- Loading -->
            <template v-slot:loading>
                <v-skeleton-loader type="table-row@10"></v-skeleton-loader>
            </template>
            <!-- Loading -->


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
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'DailyCarsReports',
    data() {
        return {
            loading: true,

            reports: [],
            expanded: [],

            itemsPerPage: 10,
            paginationPage: 1,
            pagiController: {},
            query: '',

            headers: [
                { title: 'ID', align: 'center', sortable: false, key: 'id' },
                { title: 'Reported date', align: 'center', sortable: true, key: 'date' },
                { title: 'Reported by', align: 'center', sortable: false, key: 'driver' },
                { title: 'Car', align: 'center', sortable: false, key: 'car' },
                { title: 'At mileage', align: 'center', sortable: false, key: 'car_mileage' },
                { title: 'Car condition', align: 'center', sortable: false, key: 'car_condition' },
                { title: 'Car clanliness', align: 'center', sortable: false, key: 'car_cleanliness' },
            ],

        }
    },

    mounted() {
        this.getReports();
    },

    methods: {


        // Get reports
        async getReports(url, download = false) {
            this.loading = true;

            try {
                const response = url
                    ? await axios.get(url)
                    : await axios.get('api/car/dailyreport/get/', {
                        params: {
                            limit: this.itemsPerPage,
                            query: this.query,
                            download: download
                        }
                    });



                if (download) {

                    const url = window.URL.createObjectURL(new Blob([response.data]));
                    const link = document.createElement('a');
                    link.href = url;
                    link.setAttribute('download', 'daily_reports.csv');
                    document.body.appendChild(link);
                    link.click();
                }
                else {
                    this.pagiController = {
                        total_pages: response.data.total_pages,
                        posts_amount: response.data.posts_amount,
                        next: response.data.next,
                        previous: response.data.previous,
                        currentPage: response.data.current_page,
                        totalRecors: response.data.total_results,
                    }

                    this.reports = response.data.results;

                }
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }

            this.loading = false;
        },
        // Get reports


        // Previous page
        async prevPage() {
            await this.getReports(this.pagiController.previous);
        },
        // Previous page

        // Next page
        async nextPage() {
            await this.getReports(this.pagiController.next);
        },
        // Next page


    },
}
</script>
