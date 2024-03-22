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

            </v-stepper-header>



            <v-stepper-window>

                <!-- 1 step -->
                <v-window-item value="1">
                    <v-autocomplete variant="solo-filled" label="Select restaurant" :items="restaurants" item-title="name"
                        item-value="id" v-model="selectedRestaurant"></v-autocomplete>
                </v-window-item>
                <!-- 1 step -->

                <!-- 2 step -->
                <v-window-item value="2">
                    <v-card-title>
                        Drivers working in {{ fetchedData.name }}
                    </v-card-title>

                    <v-data-table variant="solo-filled" no-data-text="Restaurant hasn't assign drivers" density="compact"
                        :items="drivers" :headers="headers" v-model="selectedDrivers" show-select item-value="username">

                    </v-data-table>

                </v-window-item>
                <!-- 2 step -->

                <!-- 3 step -->
                <v-window-item value="3">
                    <v-select variant="solo-filled" v-model="reportType" label="Select type"
                        :items="['Adjust dates or tariff manually', 'Monthly settlement']"></v-select>


                    <v-card v-if="reportType == 'Adjust dates or tariff manually'">
                        <v-card-title>
                            Adjust dates
                        </v-card-title>

                        <v-text-field type="date" v-model="customTariff.start_date" label="Start date"></v-text-field>
                        <v-text-field type="date" v-model="customTariff.end_date" label="End date"></v-text-field>

                        <v-divider></v-divider>

                        <v-card-title>
                            Adjust tariff
                        </v-card-title>

                        <v-switch label="Custom tariff" inset v-model="customTariffSwitch"
                            :color="customTariffSwitch ? 'success' : ''"></v-switch>

                        <span v-if="customTariffSwitch == true">
                            <v-text-field v-model="customTariff.basic_hourly_rate" label="Basic hourly rate" type="number"
                                append-icon="mdi-currency-usd" hint="Example - 22.41" persistent-hint></v-text-field>

                            <v-text-field v-model="customTariff.orders_bonus" label="Orders bonus" type="number"
                                append-icon="mdi-currency-usd" hint="Example - 22.41" persistent-hint></v-text-field>

                            <v-text-field v-model="customTariff.fuel_bonus" label="Fuel bonus" type="number"
                                append-icon="mdi-currency-usd" hint="Example - 22.41" persistent-hint></v-text-field>

                            <v-text-field v-model="customTariff.starting_new_billing_period"
                                label="Starting day of new billing period" hint="Value 1-31" persistent-hint
                                append-icon="mdi-calendar"></v-text-field>
                        </span>

                        <span v-else>
                            <v-autocomplete variant="solo-filled" label="Select tariff" :items="['Standard', 'Premium']"
                                v-model="customTariff"></v-autocomplete>
                        </span>

                    </v-card>


                </v-window-item>
                <!-- 3 step -->

                <!-- 4 step -->
                <v-window-item value="4">
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
                                <td>{{ restaurants.filter(restaurant => restaurant.id === selectedRestaurant)[0].name }}
                                </td>
                            </tr>
                            <tr>
                                <td>Selected drivers</td>
                                <td>{{ selectedDrivers }}</td>
                            </tr>
                            <tr>
                                <td>Selected type of report</td>
                                <td v-if="reportType == 'Adjust dates or tariff manually'">
                                    {{ customTariff }}
                                </td>
                                <td v-else>
                                    {{ reportType }}
                                </td>
                            </tr>
                        </tbody>
                    </v-table>

                </v-window-item>
                <!-- 4 step -->

            </v-stepper-window>


            <v-stepper-actions>
                <template v-slot:next="">

                    <v-btn v-if="step < 3" @click="step++" :disabled="!cards[step].active">
                        Next
                    </v-btn>

                    <v-btn v-else :text="'Generate report for ' + selectedDrivers.length + ' drivers'"
                        :disabled="selectedDrivers.length == 0" variant="tonal" color="success" @click="generateReport()"
                        append-icon="mdi-download"></v-btn>

                </template>

                <template v-slot:prev="">
                    <v-btn :disabled="step == 0" @click="step--">
                        Back
                    </v-btn>
                </template>
            </v-stepper-actions>



        </v-stepper>




        <!-- Overlay -->
        <v-overlay :model-value="overlay" class="align-center justify-center" persistent>
            <v-progress-circular color="primary" indeterminate size="64"></v-progress-circular>
        </v-overlay>
        <!-- Overlay -->
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'SettleRestaurants',
    data() {
        return {

            step: 0,
            cards: [
                {
                    id: 1,
                    text: 'Select restaurant',
                    active: false,
                },
                {
                    id: 2,
                    text: 'Select drivers',
                    active: false,
                },
                {
                    id: 3,
                    text: 'Choose type of report',
                    active: false,
                },
                {
                    id: 4,
                    text: 'Summary',
                    active: false,
                },
            ],

            restaurants: [],
            selectedRestaurant: null,

            fetchedData: {},
            drivers: [],
            selectedDrivers: [],

            reportType: null,
            customTariffSwitch: false,
            customTariff: {
                basic_hourly_rate: null,
                orders_bonus: null,
                fuel_bonus: null,
                starting_new_billing_period: null,
                start_date: null,
                end_date: null,
            },

            headers: [
                { title: 'USERNAME', align: 'center', key: 'username', sortable: false },
                { title: 'FIRST NAME', align: 'center', key: 'first_name', sortable: false },
                { title: 'LAST NAME', align: 'center', key: 'last_name', sortable: false },
            ],

            overlay: false,

        }
    },

    mounted() {
        this.getRestaurants();
    },

    watch: {
        selectedRestaurant() {
            this.getDrivers();
            this.cards[0].active = this.selectedRestaurant != null;
            this.step += 1;
        },

        selectedDrivers() {
            this.cards[1].active = this.selectedDrivers.length > 0;
        },

        reportType() {
            this.cards[2].active = this.reportType != null;
        }

    },


    // watch: {
    //     selectedRestaurant() {
    //         this.cards[0].active = this.selectedRestaurant != null;
    //     },

    //     selectedCar() {
    //         this.cards[1].active = this.selectedCar != null;
    //     },

    //     mileage(newMileage) {
    //         this.cards[2].active = newMileage && newMileage.length <= 7 && /^\d+$/.test(newMileage);
    //     },

    //     carCondition(newCondition) {
    //         this.cards[3].active = !!newCondition;
    //     },

    //     cleanliness(newCleanliness) {
    //         this.cards[4].active = !!newCleanliness;
    //         this.cards[5].active = true;
    //     },

    // },


    computed: {

        step1() {
            return this.selectedRestaurant != null;
        },

        step2() {
            return this.selectedDrivers != null;
        },

        step3() {
            return this.reportType != null;
        },


        basicHourlyRateRules() {
            return [
                v => !!v || 'Basic hourly rate is required',
                v => !isNaN(parseFloat(v)) || 'Basic hourly rate must be a number',
            ];
        },
        ordersBonusRules() {
            return [
                v => !!v || 'Orders bonus is required',
                v => !isNaN(parseFloat(v)) || 'Orders bonus must be a number',
            ];
        },
        fuelBonusRules() {
            return [
                v => !!v || 'Fuel bonus is required',
                v => !isNaN(parseFloat(v)) || 'Fuel bonus must be a number',
            ];
        },
        startingNewBillingPeriodRules() {
            return [
                v => !!v || 'Starting day of new billing period is required',
                v => !isNaN(parseFloat(v)) || 'Fuel bonus must be a number',
                v => v >= 1 && v <= 31 || 'Starting day of new billing period must be between 1 and 31',
            ];
        },

        sendReportButtonActive() {
            return this.step1 && this.step2 && this.step3 && this.step4 && this.step5;
        }
    },





    methods: {


        // Get all restaunrants
        async getRestaurants() {
            try {
                const response = await axios.get('api/restaurant/get/name-id/');
                this.restaurants = response.data;
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }
        },
        // Get all restaunrants


        // Get drivers
        async getDrivers() {
            try {
                const response = await axios.get(`api/restaurant/get/drivers/${this.selectedRestaurant}/`);
                this.fetchedData = response.data[0];
                this.drivers = response.data[0]['drivers'];
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }
        },
        // Get drivers



        // Generate report
        async generateReport() {
            this.overlay = true;
            try {
                const response = await axios.get('api/payroll/generate/report/', { drivers: this.selectedDrivers });

                const blob = new Blob([response.data], { type: 'text/csv' });
                const link = document.createElement('a');
                link.href = window.URL.createObjectURL(blob);
                link.download = 'report.csv';
                link.click();


            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
            }
            this.overlay = false;
        }
        // Generate report

    },
}
</script>

