<template>
    <div>



        <v-card align='center' justify="center" class="pa-5">

            <v-card-title>
                <h1>Daily driver report</h1>
            </v-card-title>

            <!-- Nav -->
            <v-row class="mb-2">

                <v-col cols='2' v-for="button in buttons" :key="button.id">

                    <v-btn variant="plain" :icon="button.icon" :color="button.active ? 'teal' : 'red'"
                        @click="card = button.id" :disabled="!button.active">
                    </v-btn>
                </v-col>

            </v-row>
            <!-- Nav -->



            <!-- Cards -->

            <span v-if="card == 1">
                <v-autocomplete variant="solo-filled" v-model="selectedRestaurant" :items="restaurants"
                    label="Select restaurant" no-data-text="There isn't available restaurants"
                    @update:model-value="getDrivers()"></v-autocomplete>
            </span>



            <span v-if="card == 2">
                <v-autocomplete v-model="selectedDriver" :items="drivers" item-title="username" item-value="username"
                    label="Select driver" no-data-text="There isn't available drivers for selected restaurant"
                    :disabled="selectedRestaurant == null">

                    <template v-slot:item="{ props, item }">
                        <v-list-item v-bind="props" :title="item.raw.last_name + ' ' + item.raw.first_name"
                            :subtitle="item.raw.username"></v-list-item>
                    </template>

                </v-autocomplete>
            </span>



            <span v-if="card == 3">
                <v-text-field v-model="ordersAmout" variant="solo-filled" label="Type amount of orders"
                    :rules="[value => !!value || 'Field is required', value => (/^\d+$/.test(value)) || 'Only numbers are allowed', value => (value && value.length <= 3 || 'Reached max length')]">
                </v-text-field>
            </span>
            <!-- Cards -->



            <!-- Buttons -->
            <v-row class="mt-3 mb-3">
                <v-col cols="6" align="start">
                    <v-btn variant="outlined" color="red" v-if="card > 1" @click="card--" prepend-icon="mdi-arrow-left">
                        {{ buttons[card - 2].text }}
                    </v-btn>
                </v-col>

                <v-col cols="6" align="end">
                    <v-btn v-if="card < 6" variant="outlined" color="teal" @click="card++"
                        :disabled="!buttons[card].active">
                        {{ buttons[card].text }}
                        <v-icon icon="mdi-arrow-right"></v-icon>
                    </v-btn>
                    <v-btn v-else :variant="!allButtonsActive ? 'outlined' : 'elevated'"
                        :color="!allButtonsActive ? 'red' : 'teal'" :disabled="!allButtonsActive" @click="sendReport()"
                        append-icon="mdi-send">
                        Send
                    </v-btn>
                </v-col>
            </v-row>
            <!-- Buttons -->

        </v-card>
















    </div>
</template>

<script>
import axios from 'axios';
import { createWebHistory } from 'vue-router';

export default {
    name: 'DailyDriverReport',

    data() {
        return {
            loggedUserUsername: null,
            card: 1,

            buttons: [
                {
                    id: 1,
                    text: 'Select restaurant',
                    active: true,
                    icon: 'mdi-numeric-1-circle',
                },
                {
                    id: 2,
                    text: 'Select driver',
                    active: false,
                    icon: 'mdi-numeric-2-circle',
                },
                {
                    id: 3,
                    text: 'Type amount of orders',
                    active: false,
                    icon: 'mdi-numeric-3-circle',
                },
                {
                    id: 4,
                    text: 'Type amount of orders',
                    active: false,
                    icon: 'mdi-numeric-4-circle',
                },
            ],







            restaurants: [],
            selectedRestaurant: null,

            drivers: [],
            selectedDriver: null,

            ordersAmout: null,
        }
    },

    mounted() {
        this.loggedUserUsername = this.$store.getters.userData.username;

        this.getRestaurants()
    },


    watch: {
        selectedRestaurant() {
            this.buttons[1].active = this.selectedRestaurant != null;
        },

        selectedDriver() {
            this.buttons[2].active = this.selectedDriver != null;
        },

        ordersAmout(ordersAmout) {
            this.buttons[3].active = ordersAmout && /^\d+$/.test(ordersAmout);
        },
        carCondition(newCondition) {
            this.buttons[4].active = !!newCondition;
        },
        cleanliness(newCleanliness) {
            this.buttons[5].active = !!newCleanliness;
        },
    },

    methods: {

        // Get restaurants
        async getRestaurants() {
            try {
                const response = await axios.get('api/rest_manager/get_restaurants/', {
                    params: {
                        username: this.loggedUserUsername,
                    }
                });

                this.restaurants = response.data.map(restaurant => restaurant.name);

            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }
        },
        // Get restaurants


        // Get drivers
        async getDrivers() {
            try {
                const response = await axios.get('api/drivers/get/usernames/', {
                    params: {
                        restaurant: this.selectedRestaurant,
                    }
                });

                this.drivers = response.data;
                console.log(this.drivers)
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }
        }
        // Get drivers

    },
}
</script>

