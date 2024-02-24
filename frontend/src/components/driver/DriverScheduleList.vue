<template>
  <div>
    <v-card class="mb-2">
      <v-card-title>
        <v-icon>mdi-calendar</v-icon>
        <span>My Work Schedule</span>
        <span v-if="selectedRestaurant != null"> at {{ restaurants.find(restaurant => restaurant.id ==
          selectedRestaurant).name }}</span>
      </v-card-title>


      <v-card-text>
        <v-autocomplete v-model="selectedRestaurant" :items="restaurants" variant="solo-filled" item-title="name"
          item-value="id" label="Select Restaurant" @update:model-value="getShifts()"></v-autocomplete>
      </v-card-text>
    </v-card>

    <div class="is-light-mode" v-if="selectedRestaurant != null">
      <Qalendar :events="shifts" :config="config" :key="calendarKey" @updated-period="periodUpdated">
        <template #dayCell="{ dayData }">
          <div>

            <!-- MOBILE -->
            <div v-if="mobile">
              <span v-if="dayData.events.length > 0">
                <div>{{ dayData.dateTimeString.substring(8, 10) }}</div>
                <v-icon color="success" class="text-h6">mdi-truck</v-icon>
              </span>

              <span v-else>
                <span class="font-weight-thin"> {{ dayData.dateTimeString.substring(8, 10) }}</span>
              </span>
            </div>
            <!-- MOBILE -->

            <!-- DESKTOP -->
            <div v-else style="min-height: 10dvh;">
              <span v-if="dayData.events.length > 0">
                <v-row>
                  <v-col cols="12" align="center">
                    {{ dayData.dateTimeString.substring(8, 10) }}
                  </v-col>
                </v-row>

                <table v-if="dayData.events.length > 0">
                  <tbody>
                    <tr v-for="event in dayData.events" :key="event.id">
                      <td>
                        <v-icon :color="event.color">mdi-truck</v-icon>&nbsp
                      </td>
                      <td align="center">
                        {{ event.time.start.substring(event.time.start.length - 5) }}
                      </td>
                      <td align="center">
                        &nbsp-&nbsp
                      </td>
                      <td align="center">
                        {{ event.time.end.substring(event.time.start.length - 5) }}
                      </td>
                    </tr>
                  </tbody>
                </table>
              </span>

              <span v-else>
                <span class="font-weight-thin"> {{ dayData.dateTimeString.substring(8, 10) }}</span>
              </span>
            </div>
            <!-- DESKTOP -->


          </div>
        </template>
      </Qalendar>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { Qalendar } from "qalendar";

export default {
  name: 'DriverScheduleList',
  components: {
    Qalendar,
  },
  data() {
    return {
      mobile: false,
      loggedUserUsername: null,
      date: null,

      selectedRestaurant: null,
      restaurants: [],

      shifts: [],

      config: {
        defaultMode: 'month',
        disableModes: ['day'],
        showCurrentTime: true,
        locale: 'pl-PL',
        isSilent: true,
        eventDialog: {
          isDisabled: true,
        },

        dayBoundaries: {
          start: 9,
          end: 23,
        },
      },
    };
  },

  computed: {
    mobile() {
      return this.$vuetify.display.mobile;
    },
  },

  methods: {

    // Get restaurants for user
    async getRestaurants() {
      try {
        const response = await axios.get('api/drivers/get/restaurants/', {
          params: {
            username: this.loggedUserUsername,
          }
        });

        this.restaurants = response.data
      } catch (error) {
        this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
      }
    },
    // Get restaurants for user


    // Get shifts for restaurant
    async getShifts() {
      try {
        const response = await axios.get('api/restaurant/driver-shifts/', {
          params: {
            restaurant: this.selectedRestaurant,
            date: this.date,
            driver: this.loggedUserUsername,
          }
        });
        this.shifts = response.data;

        this.shifts.forEach(shift => {
          if (shift.with === null) {
            shift.with = 'No driver';
            shift.color = 'red';
          }
        });


      } catch (error) {
        this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
      }
    },
    // Get shifts for restaurant

    // Period updated
    periodUpdated(data) {
      this.date = data;
      this.getShifts()
    },
    // Period updated


    // Get current week
    async getCurrentWeek() {
      let now = new Date();
      let dayOfWeek = now.getDay();
      let diffToMonday = (dayOfWeek >= 1 ? dayOfWeek - 1 : 6);
      let dateStart = new Date(now.getFullYear(), now.getMonth(), now.getDate() - diffToMonday);
      dateStart.setHours(23, 0, 0, 0);
      let dateEnd = new Date(now.getFullYear(), now.getMonth(), now.getDate() + (7 - dayOfWeek));
      dateEnd.setHours(22, 59, 59, 999);
      let isoDateStart = dateStart.toISOString().slice(0, 24);
      let isoDateEnd = dateEnd.toISOString().slice(0, 24);
      this.date = { start: isoDateStart, end: isoDateEnd };
    },
    // Get current week


    // Get current month
    async getCurrentMonth() {
      let now = new Date();
      let firstDayOfMonth = new Date(now.getFullYear(), now.getMonth(), 1);
      firstDayOfMonth.setHours(0, 0, 0, 0);
      let lastDayOfMonth = new Date(now.getFullYear(), now.getMonth() + 1, 0);
      lastDayOfMonth.setHours(23, 59, 59, 999);
      let isoDateStart = firstDayOfMonth.toISOString().slice(0, 24);
      let isoDateEnd = lastDayOfMonth.toISOString().slice(0, 24);
      this.date = { start: isoDateStart, end: isoDateEnd };
    },
    // Get current month

  },

  created() {
    this.mobile = this.$vuetify.display.mobile;
  },

  async mounted() {
    this.loggedUserUsername = this.$store.getters.userData.username;
    this.date = new Date().toISOString().slice(0, 10);
    await this.getRestaurants();
    this.selectedRestaurant = this.restaurants[0].id;
    await this.getCurrentMonth();
    this.getShifts();

  },
};
</script>

<style>
@import "qalendar/dist/style.css";
</style>