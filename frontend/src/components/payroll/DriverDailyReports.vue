<template>
  <div>

    <!-- Top section -->
    <div class="mt-5 mb-5">

      <v-row>

        <v-col cols="12" sm="12">
          <v-expansion-panels>
            <v-expansion-panel title="Options" elevation="1" style="border: 1px solid teal;">

              <v-expansion-panel-text>
                <v-row justify="center" align="center">

                  <v-col cols="12" sm="3">
                    <v-autocomplete :items="restaurants" v-model="selectedRestaurant" item-title="name" item-value="id"
                      label="Select restaurant" variant="solo-filled" @update:model-value="getReports()"></v-autocomplete>
                  </v-col>

                  <v-col cols="12" sm="3">
                    <v-text-field type="date" v-model="startDate" label="Start date" variant="solo-filled"
                      @input="getReports()"></v-text-field>
                  </v-col>

                  <v-col cols="12" sm="3">
                    <v-text-field type="date" v-model="endDate" label="End date" variant="solo-filled"
                      @input="getReports()"></v-text-field>
                  </v-col>

                  <v-col cols="12" sm="3">
                    <v-select v-model="itemsPerPage" variant="solo-filled" :items="[5, 10, 25, 50, 100]"
                      :label="`Items per page - ${itemsPerPage}`" @update:model-value="getReports()"></v-select>
                  </v-col>
                </v-row>

                <v-btn variant="outlined" text="Download reports" @click="downloadReport()" class="my-5" color="primary"
                  append-icon="mdi-download">
                </v-btn>

              </v-expansion-panel-text>
            </v-expansion-panel>
          </v-expansion-panels>

        </v-col>

      </v-row>

    </div>
    <!-- Top section -->


    <v-row>
      <v-col justify="start">
        <div class="text-h4 my-1 font-weight-bold">
          Reports
        </div>
      </v-col>
      <v-col justify="end" cols="12" sm="4">

        <!-- Search bar -->
        <v-text-field variant="solo-filled" v-model="query" @keydown.enter="getReports()" label="Search" class="px-1 "
          prepend-inner-icon="mdi-magnify" hide-actions clearable
          hint="Press enter to search. Search in date (YYYY-MM-DD) and drivers" persistentHint />
        <!-- Search bar -->

      </v-col>
    </v-row>




    <v-data-table :headers="tableHeaders" :items="reports" :loading="loading" density="compact"
      class="elevation-4 rounded-xl" item-value="id" v-model:items-per-page="itemsPerPage" hover show-current-page>


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


      <!-- Accessing table cells -->
      <template v-slot:item="{ item }">
        <tr align="center">
          <td v-for="header in tableHeaders" :key="header.key">

            <span v-if="item[header.key] === null || item[header.key] === undefined || item[header.key] === ''">
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

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'DriverDailyReports',
  data() {
    return {

      loading: true,
      reports: [],

      selectedRestaurant: null,
      restaurants: [
        {
          name: 'All',
          id: 'All'
        },
      ],

      startDate: null,
      endDate: null,

      itemsPerPage: 10,
      paginationPage: 1,
      pagiController: {},
      query: '',


      necessaryHeaders: [
        { title: 'ID', align: 'center', sortable: false, key: 'id' },

      ],

      driverHeaders: [
        { title: 'DATE', align: 'center', sortable: true, key: 'date' },
        { title: 'DRIVER', align: 'center', sortable: false, key: 'driver' },
        { title: 'ORDERS', align: 'center', sortable: false, key: 'orders' },
        { title: 'Start', align: 'center', sortable: false, key: 'start_work' },
        { title: 'End', align: 'center', sortable: false, key: 'end_work' },
        { title: 'Working time', align: 'center', sortable: false, key: 'working_time' },

      ]

    };
  },

  computed: {
    tableHeaders() {
      return [
        ...this.necessaryHeaders,
        ...this.driverHeaders,
      ];
    }
  },

  methods: {

    // Fetch drivers daily reports
    async getReports(url) {
      this.loading = true;

      if (this.selectedRestaurant === 'All') {
        this.selectedRestaurant = null;
      }

      try {
        const response = url
          ? await axios.get(url)
          : await axios.get('api/drivers/daily_report/get/all/', {
            params: {
              limit: this.itemsPerPage,
              search: this.query,
              restaurant: this.selectedRestaurant,
              start_date: this.startDate,
              end_date: this.endDate,
              download: false,
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

        this.reports = response.data.results;

      } catch (error) {
        this.$store.dispatch('triggerAlert', { message: error.response, type: 'error' });
      }

      this.loading = false;
    },
    // Fetch drivers daily reports



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



    // Download report
    async downloadReport() {

      if (this.selectedRestaurant === 'All') {
        this.selectedRestaurant = null;
      }

      try {
        const response = await axios.get('api/drivers/daily_report/get/all/', {
          params: {
            limit: this.itemsPerPage,
            search: this.query,
            restaurant: this.selectedRestaurant,
            start_date: this.startDate,
            end_date: this.endDate,
            download: true,
          }
        });

        const blob = new Blob([response.data], { type: 'text/csv' });
        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        link.download = 'report.csv';
        link.click();

      } catch (error) {
        this.$store.dispatch('triggerAlert', { message: error.response, type: 'error' });
      }
    },
    // Download report



    // Get restaurants
    async getRestaurants() {
      try {
        const response = await axios.get('api/restaurant/get/name-id/')
        this.restaurants = [...this.restaurants, ...response.data]
      } catch (error) {
        this.$store.dispatch('triggerAlert', { message: error.response, type: 'error' });
      }
    },
    // Get restaurants

  },
  mounted() {
    this.getReports();
    this.getRestaurants();
    this.selectedRestaurant = this.restaurants[0];
  },
};
</script>
