<template>
    <div>
        <v-autocomplete label="Select restaurant" variant="underlined" :items="restaurants" item-title="name" item-value="id" v-model="selectedRestaurant"></v-autocomplete>
{{ restaurants }}
{{ selectedRestaurant }}
        <v-btn color="primary" @click="getDrivers">Get Drivers</v-btn>

        <v-data-table no-data-text="Restaurant hasn't assign drivers">

        </v-data-table>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'SettleRestaurants',
    data() {
        return {

            restaurants: [],
            selectedRestaurant: null,

        }
    },

    mounted() {
        this.getRestaurants();
    },

    methods: {

        
        // Get all restaunrants
        async getRestaurants(restaurant_name) {
            try {
                const response = await axios.get('api/restaurant/get/name-id/');
                console.log(response.data);
                this.restaurants = response.data;
            } catch(error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }
        },
        // Get all restaunrants


        // Get drivers
        async getDrivers() {
            try {
                const response = await axios.get(`api/restaurant/get/drivers/${restaurant_name}/`);
                console.log(response.data);
            } catch(error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }
        },


    },
}
</script>

