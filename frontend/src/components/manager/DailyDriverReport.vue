<template>
    <div>

        <v-stepper v-model="step" :mobile="$vuetify.display.smAndDown">
            <v-stepper-header>
                <v-stepper-item :complete="step1" :title="cards[0].text" value="1"></v-stepper-item>

                <v-divider></v-divider>

                <v-stepper-item :complete="step2" :title="cards[1].text" value="2"></v-stepper-item>

                <v-divider></v-divider>

                <v-stepper-item :complete="step3" :title="cards[2].text" value="3"></v-stepper-item>

                <v-divider></v-divider>

                <v-stepper-item :complete="step4" :title="cards[3].text" value="4"></v-stepper-item>

                <v-divider></v-divider>

                <v-stepper-item :title="cards[4].text" value="5"></v-stepper-item>

            </v-stepper-header>

            <v-stepper-window>

                <v-window-item value="1">
                    <v-autocomplete variant="underlined" v-model="selectedRestaurant" :items="restaurants"
                        label="Select restaurant" no-data-text="There isn't available restaurants"
                        @update:model-value="getDrivers()"></v-autocomplete>
                </v-window-item>



                <v-window-item value="2">
                    <v-autocomplete variant="underlined" v-model="selectedDriver" :items="drivers" item-title="username"
                        item-value="username" label="Select driver"
                        no-data-text="There isn't available drivers for selected restaurant"
                        :disabled="selectedRestaurant == null">

                        <template v-slot:item="{ props, item }">
                            <v-list-item v-bind="props" :title="item.raw.last_name + ' ' + item.raw.first_name"
                                :subtitle="item.raw.username"></v-list-item>
                        </template>

                    </v-autocomplete>
                </v-window-item>



                <v-window-item value="3">
                    <v-text-field v-model="ordersAmout" variant="underlined" label="Type amount of orders"
                        :rules="[value => !!value || 'Field is required', value => (/^\d+$/.test(value)) || 'Only numbers are allowed', value => (value && value.length <= 3 || 'Reached max length')]">
                    </v-text-field>
                </v-window-item>



                <v-window-item value="4">
                    <v-row align="center" justify="center">
                        <v-col cols="6" sm="2">
                            <h4>Start</h4>
                            <v-autocomplete variant="underlined" :items="hoursList" v-model="startShift"></v-autocomplete>
                        </v-col>

                        <v-col cols="6" sm=2>
                            <h4>End</h4>
                            <v-autocomplete variant="underlined" :items="hoursList" v-model="endShift"
                                :disabled="startShift == null"></v-autocomplete>
                        </v-col>
                    </v-row>
                </v-window-item>



                <v-window-item value="5">
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
                </v-window-item>
            </v-stepper-window>

            <v-stepper-actions>
                <template v-slot:next="">

                    <v-btn v-if="step < 4" @click="step++" :disabled="!cards[step].active">
                        Next
                    </v-btn>
                    <v-btn v-else :disabled="!sendReportButtonActive" @click="sendReport()" append-icon="mdi-send-variant"
                        variant="tonal" color="success">
                        Send
                    </v-btn>

                </template>

                <template v-slot:prev="">
                    <v-btn :disabled="step == 0" @click="step--">
                        Back
                    </v-btn>
                </template>
            </v-stepper-actions>

        </v-stepper>


    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'DailyDriverReport',

    data() {
        return {
            loggedUserUsername: null,
            step: 0,

            cards: [
                {
                    id: 1,
                    text: 'Select restaurant',
                    active: false,
                },
                {
                    id: 2,
                    text: 'Select driver',
                    active: false,
                },
                {
                    id: 3,
                    text: 'Orders amount',
                    active: false,
                },
                {
                    id: 4,
                    text: 'Shift details',
                    active: false,
                },
                {
                    id: 5,
                    text: 'Summary',
                    active: false,
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

        summaryButtonActive() {
            return this.startShift != null && this.endShift != null;
        },

        step1() {
            return this.selectedRestaurant != null;
        },

        step2() {
            return this.selectedDriver != null;
        },

        step3() {
            return this.ordersAmout != null;
        },

        step4() {
            return this.startShift != null && this.endShift != null;
        },

        sendReportButtonActive() {
            return this.step1 && this.step2 && this.step3 && this.step4;
        }

    },


    watch: {
        selectedRestaurant() {
            this.cards[0].active = this.selectedRestaurant != null;
        },

        selectedDriver() {
            this.cards[1].active = this.selectedDriver != null;
        },

        ordersAmout(ordersAmout) {
            this.cards[2].active = ordersAmout && /^\d+$/.test(ordersAmout);
        },

        endShift() {
            this.cards[3].active = this.summaryButtonActive;
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


        // Generate hours list
        async generateHoursList() {
            for (let i = 0; i < 24 * 12; i++) {
                await new Promise(resolve => setTimeout(resolve, 0));
                let hour = Math.floor(i / 12);
                let minutes = i % 12 * 5;
                this.hoursList.push(`${hour.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`);
            }
        },
        // Generate hours list


    },
}
</script>

