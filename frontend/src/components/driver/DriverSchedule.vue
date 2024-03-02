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

    <h4>Your rate is {{ rateInfo.rating }}, you can assign for shifts at {{ getDayOfWeek(rateInfo.day) }} {{ rateInfo.hour
    }}</h4>

    <div class="is-light-mode" v-if="selectedRestaurant != null">
      <Qalendar :events="shifts" :config="config" @delete-event="deleteEvent" :key="calendarKey"
        @updated-period="periodUpdated" @event-was-clicked="eventClicked">


      </Qalendar>
    </div>


    <!-- Shift dialog -->
    <v-dialog v-model="shiftDialog" persistent max-width="500">
      <v-card>
        <v-card-title>
          <v-row>
            <v-col cols="2"></v-col>
            <v-col cols="8" align="center">
              Shift details
            </v-col>
            <v-col cols="2" align="end">
              <v-btn icon="mdi-close" variant="plain" @click="shiftDialog = false"></v-btn>
            </v-col>
          </v-row>
        </v-card-title>

        <v-card-text>
          <v-form v-model="form" @submit-prevent="assignDriver()">
            <v-row>
              <v-col>
                <v-text-field v-model="shiftStart" label="Start" variant="underlined" hint="HH:MM 24h" persistent-hint
                  :rules="rules" />
              </v-col>
              <v-col>
                <v-text-field v-model="shiftEnd" label="End" variant="underlined" hint="HH:MM 24h" persistent-hint
                  :rules="rules" />
              </v-col>
            </v-row>
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-btn block color="success" @click="assignDriver()" :disabled="!form || !myForm">Assign</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <!-- Shift dialog -->


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
      rateInfo: {
        rating: null,
        day: null,
      },
      date: null,

      selectedRestaurant: null,
      restaurants: [],

      shifts: [],

      config: {
        defaultMode: 'day',
        disableModes: ['week', 'month'],
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

      shift: null,
      shiftStart: null,
      shiftEnd: null,
      shiftDialog: false,
      form: false,
      myForm: false,
      rules: [
        v => !!v || 'Time is required',
        v => /^([01]?[0-9]|2[0-3]):[0-5][0-9]$/.test(v) || 'Invalid time format. Use HH:MM 24h format',
      ],


    };
  },

  computed: {
    getDayOfWeek() {
      return (day) => {
        const daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
        return daysOfWeek[day - 1];
      };
    },
  },

  watch: {
    shiftStart() {
      if (this.shiftStart && this.shift.time_start) {
        const input_data = new Date(`2000-01-01T${this.shiftStart}`);
        const compare_data = new Date(`2000-01-01T${this.shift.time_start}`);
        const timeDiff = input_data - compare_data;
        const hoursDiff = Math.floor(timeDiff / (1000 * 60 * 60));

        if (hoursDiff <= 3  && hoursDiff != 0 || isNaN(hoursDiff)) {
          this.myForm = false;
        } else {
          this.myForm = true;
        }
      } 
    },

    shiftEnd() {
      if (this.shiftEnd && this.shift.time_end) {
        const input_data = new Date(`2000-01-01T${this.shiftEnd}`);
        const compare_data = new Date(`2000-01-01T${this.shift.time_end}`);
        const timeDiff = compare_data - input_data;
        const hoursDiff = Math.floor(timeDiff / (1000 * 60 * 60));

        if (hoursDiff <= 3  && hoursDiff != 0 || isNaN(hoursDiff)) {
          this.myForm = false;
        } else {
          this.myForm = true;
        }
      } 
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


    // Get info about rate
    async getRateInfo() {
      try {
        const response = await axios.get(`api/drivers/ratings/get/rate_info/${this.loggedUserUsername}/`);
        this.rateInfo = response.data;
      } catch (error) {
        this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
      }
    },
    // Get info about rate


    // Event clicked
    eventClicked(event) {
      const singleSchedule = event.clickedEvent;

      // const today = new Date();
      // const weekday = today.getDay();
      // || this.rateInfo.day != weekday
      if (singleSchedule.with !== 'No driver' ) {
        return;
      }

      const time_start = singleSchedule.time.start.slice(-5);
      const time_end = singleSchedule.time.end.slice(-5);
      const date_start = singleSchedule.time.start.slice(0, 10);
      const date_end = singleSchedule.time.end.slice(0, 10);

      this.shiftStart = time_start;
      this.shiftEnd = time_end;

      this.shift = {
        id: singleSchedule.id,
        time_start: time_start,
        time_end: time_end,
        date_start: date_start,
        date_end: date_end,
      }
      this.shiftDialog = true;
    },
    // Event clicked


    // Assign driver for shift
    async assignDriver() {
      const data = {
        driver: this.loggedUserUsername,
        shift: this.shift.id,
        time_start: this.shiftStart,
        time_end: this.shiftEnd,
        date: this.shift.date_end,
      }

      try {
         const response = await axios.post('api/restaurant/assign-driver/', data);
         this.date = response.data.day;
         this.getShifts();
         this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'success' });
      } catch (error) {
        this.$store.dispatch('triggerAlert', { message: error.response.error, type: 'error' });
      }




      this.shiftDialog = false;
    },
    // Assign driver for shift


  },

  async created() {
    this.loggedUserUsername = this.$store.getters.userData.username;
    await this.getRateInfo();
  },

  async mounted() {

    this.date = new Date().toISOString().slice(0, 10);
    await this.getRestaurants();
    this.selectedRestaurant = this.restaurants[0].id;
    this.getShifts();
  },
};
</script>

<style>
@import "qalendar/dist/style.css";
</style>