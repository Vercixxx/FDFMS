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



            <span v-if="card == 4">
                <v-row align="center" justify="center">
                    <v-col cols="6" sm="2">
                        <h4>Start</h4>
                        <v-autocomplete variant="solo" :items="hoursList" v-model="startShift"></v-autocomplete>
                    </v-col>
                    
                    <v-col cols="6" sm=2>
                        <h4>End</h4>
                        <v-autocomplete variant="solo" :items="hoursList" v-model="endShift" :disabled="startShift == null"></v-autocomplete>
                    </v-col>
                </v-row>

            </span>



            <span v-if="card == 5">
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
                        <tr>
                            <td>Restaurant</td>
                            <td>{{ selectedRestaurant }}</td>
                        </tr>
                        <tr>
                            <td>Driver</td>
                            <td>{{ drivers.find(user => user.username == selectedDriver).last_name + ' ' +
                                drivers.find(user => user.username == selectedDriver).first_name }}</td>
                        </tr>
                        <tr>
                            <td>Orders</td>
                            <td>{{ ordersAmout }}</td>
                        </tr>
                        <tr>
                            <td>Shift details</td>
                            <td>
                                {{ startShift }} - {{ endShift }}
                            </td>
                        </tr>
                    </tbody>
                </v-table>
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
                    <v-btn v-if="card < 5" variant="outlined" color="teal" @click="card++"
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
                    text: 'Orders amount',
                    active: false,
                    icon: 'mdi-numeric-3-circle',
                },
                {
                    id: 4,
                    text: 'Shift details',
                    active: false,
                    icon: 'mdi-numeric-4-circle',
                },
                {
                    id: 5,
                    text: 'Summary',
                    active: true,
                    icon: 'mdi-numeric-5-circle',
                },
            ],







            restaurants: [],
            selectedRestaurant: null,

            drivers: [],
            selectedDriver: null,

            ordersAmout: null,

            hoursList: [],
            startShift: null,
            endShift: null,
        }
    },

    mounted() {
        this.loggedUserUsername = this.$store.getters.userData.username;

        this.getRestaurants()

        this.generateHoursList();
    },



    computed: {
        allButtonsActive() {
            return this.buttons.every(button => button.active);
        },
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

        shiftDetails() {
            this.buttons[4].active = true;
            this.buttons[5].active = true;
            // this.buttons[4].active = this.shiftDetails != null;
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

            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }
        },
        // Get drivers


        // Send report
        async sendReport() {
            const data = {
                restaurant: this.selectedRestaurant,
                driver: this.selectedDriver,
                orders: this.ordersAmout,
                start_shift: this.startShift,
                end_shift: this.endShift,
            }

            try {
                const response = await axios.post('api/drivers/daily_report/add/', data);
                
                this.$store.dispatch('triggerAlert', { message: 'Succesully send report', type: 'teal' });
                this.$root.changeCurrentComponent('HomeComponent');
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error.response, type: 'error' });
            }
        },
        // Send report


        async generateHoursList() {
            for (let i = 0; i < 24 * 12; i++) {
                await new Promise(resolve => setTimeout(resolve, 0));
                let hour = Math.floor(i / 12);
                let minutes = i % 12 * 5;
                this.hoursList.push(`${hour.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`);
            }
        },


    },
}
</script>

