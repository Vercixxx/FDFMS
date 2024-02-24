<template>
  <div>
    <v-card class="mb-2">
      <v-card-title>
        <v-icon>mdi-calendar</v-icon>
        <span>Work Schedule</span>
        <span v-if="selectedRestaurant != null"> for {{ restaurants.find(restaurant => restaurant.id ==
          selectedRestaurant).name }}</span>
      </v-card-title>

      <v-card-text>
        <v-autocomplete v-model="selectedRestaurant" :items="restaurants" variant="solo-filled" item-title="name"
          item-value="id" label="Select Restaurant" @update:model-value="getShifts()"></v-autocomplete>
      </v-card-text>
    </v-card>


    <div class="is-light-mode" v-if="selectedRestaurant != null">
      <Qalendar :events="shifts" :config="config" @delete-event="deleteEvent" :key="calendarKey"
        @event-was-clicked="objectSelected" @updated-period="periodUpdated">

      </Qalendar>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { Qalendar } from "qalendar";

export default {
  name: 'DriverSchedule',
  components: {
    Qalendar,
  },
  data() {
    return {
      loggedUserUsername: null,
      date: null,

      selectedRestaurant: null,
      restaurants: [],

      shifts: [],

      config: {
        defaultMode: 'week',
        showCurrentTime: true,
        locale: 'pl-PL',
        isSilent: true,
        eventDialog: {
          isCustom: true,
        },

        dayBoundaries: {
          start: 9,
          end: 23,
        },
      },
    };
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

  },

  async mounted() {
    this.loggedUserUsername = this.$store.getters.userData.username;
    this.date = new Date().toISOString().slice(0, 10);
    await this.getRestaurants();
    this.selectedRestaurant = this.restaurants[0].id;
    await this.getCurrentWeek();
    this.getShifts();
  },
};
</script>

<style>
@import "qalendar/dist/style.css";
</style>