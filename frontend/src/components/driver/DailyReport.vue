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

                <v-stepper-item :complete="step5" :title="cards[4].text" value="5"></v-stepper-item>

                <v-divider></v-divider>

                <v-stepper-item :complete="step5" :title="cards[5].text" value="6"></v-stepper-item>

                <v-divider></v-divider>

                <v-stepper-item :title="cards[6].text" value="7"></v-stepper-item>

            </v-stepper-header>



            <v-stepper-window>

                <!-- 1 step -->
                <v-window-item value="1">
                    <v-autocomplete variant="solo-filled" :items="restaurants" v-model="selectedRestaurant"
                        label="Select restaurant" @update:model-value="getCars()"
                        no-data-text="Sorry, you don't belong to any restaurant"></v-autocomplete>
                </v-window-item>
                <!-- 1 step -->

                <!-- 2 step -->
                <v-window-item value="2">
                    <v-autocomplete variant="solo-filled" :disabled="selectedRestaurant == null" :items="cars"
                        label="Select car" v-model="selectedCar"
                        no-data-text="Sorry, there isn't available cars for selected restaurant"></v-autocomplete>
                </v-window-item>
                <!-- 2 step -->

                <!-- 3 step -->
                <v-window-item value="3">
                    <v-text-field v-model="mileage" variant="solo-filled" label="Type mileage"
                        :rules="[value => !!value || 'Mileage is required', value => (value && value.length <= 7) || 'Mileage must be a number up to 7 digits', value => (value && /^\d+$/.test(value) || 'Only digits are allowed')]">
                        <template v-slot:append>km</template>
                    </v-text-field>
                </v-window-item>
                <!-- 3 step -->

                <!-- 4 step -->
                <v-window-item value="4" align="center" justify="center">
                    <h5>Car condition</h5>
                    <v-rating v-model="carCondition" hover class="ma-2" :length="3" :item-labels="['Bad', '', 'Good']"
                        item-label-position="top" active-color="teal"></v-rating>
                </v-window-item>
                <!-- 4 step -->

                <!-- 5 step -->
                <v-window-item value="5" align="center" justify="center">
                    <h5>Cleanliness</h5>
                    <v-rating v-model="cleanliness" hover class="ma-2" :length="5"
                        :item-labels="['Bad', '', '', '', 'Excellent']" item-label-position="top"
                        active-color="teal"></v-rating>
                </v-window-item>
                <!-- 5 step -->

                <!-- 6 step -->
                <v-window-item value="6">
                    <v-textarea v-model="additional_remarks" label="Comments" variant="solo-filled" class="mt-3" rows="1"
                        auto-grow clearable counter="200"
                        :rules="[value => (value && value.length <= 200) || 'Max 200 characters']"
                        append-icon="mdi-chat-alert"></v-textarea>
                </v-window-item>
                <!-- 6 step -->

                <!-- 7 step -->
                <v-window-item value="7">
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
                                <td>Car license plate</td>
                                <td>{{ selectedCar }}</td>
                            </tr>
                            <tr>
                                <td>Mileage</td>
                                <td>{{ mileage }} km</td>
                            </tr>
                            <tr>
                                <td>Car condition</td>
                                <td>
                                    <v-rating readonly hover :length="3" :model-value="carCondition"
                                        item-label-position="top" active-color="teal"></v-rating>
                                </td>
                            </tr>
                            <tr>
                                <td>Cleanliness</td>
                                <td>
                                    <v-rating readonly hover :length="5" :model-value="cleanliness"
                                        item-label-position="top" active-color="teal"></v-rating>
                                </td>
                            </tr>
                            <tr>
                                <td>Additional remarks</td>
                                <td>{{ additional_remarks ? additional_remarks:'No remarks' }}</td>
                            </tr>
                        </tbody>
                    </v-table>
                </v-window-item>
                <!-- 7 step -->

            </v-stepper-window>


            <v-stepper-actions>
                <template v-slot:next="">

                    <v-btn v-if="step < 6" @click="step++" :disabled="!cards[step].active">
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
    name: 'DailyReport',
    data() {
        return {
            loggedUser: null,

            restaurants: [],
            selectedRestaurant: null,

            cars: [],
            selectedCar: null,

            objects: [],

            mileage: null,
            carCondition: null,
            cleanliness: null,
            additional_remarks: null,

            step: 0,
            cards: [
                {
                    id: 1,
                    text: 'Select restaurant',
                    active: false,
                },
                {
                    id: 2,
                    text: 'Select car',
                    active: false,
                },
                {
                    id: 3,
                    text: 'Type mileage',
                    active: false,
                },
                {
                    id: 4,
                    text: 'Car condition',
                    active: false,
                },
                {
                    id: 5,
                    text: 'Cleanliness',
                    active: false,
                },
                {
                    id: 6,
                    text: 'Additional remarks',
                    active: false,
                },
                {
                    id: 7,
                    text: 'Summary',
                    active: false,
                },
            ],
        }
    },

    mounted() {

        // Get logged user
        this.loggedUser = this.$store.getters.userData.username;
        // Get logged user


        // Get restaurants for logged user
        this.getRestaurants();
        // Get restaurants for logged user

    },

    methods: {

        // Get restaurants for logged user
        async getRestaurants() {
            try {
                const response = await axios.get(`api/drivers/get/restaurants/${this.loggedUser}/`);

                this.objects = response.data;
                this.restaurants = Object.keys(this.objects)
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
        },
        // Get restaurants for logged user


        // Get cars for selected restaurant
        getCars() {
            this.cars = this.objects[this.selectedRestaurant];
        },
        // Get cars for selected restaurant


        // Send daily car report
        async sendReport() {
            try {
                const response = await axios.post(`api/car/dailyreport/add/`, {
                    driver: this.loggedUser,
                    car: this.selectedCar,
                    car_mileage: this.mileage,
                    carCondition: this.carCondition,
                    cleanliness: this.cleanliness,
                    additional_remarks: this.additional_remarks.length > 0 ? this.additional_remarks : null,
                });

                this.$root.changeCurrentComponent('HomeComponent');
                this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'success' });
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error.response.error, type: 'error' });
            }
        },
        // Send daily car report



    },


    watch: {
        selectedRestaurant() {
            this.cards[0].active = this.selectedRestaurant != null;
        },

        selectedCar() {
            this.cards[1].active = this.selectedCar != null;
        },

        mileage(newMileage) {
            this.cards[2].active = newMileage && newMileage.length <= 7 && /^\d+$/.test(newMileage);
        },

        carCondition(newCondition) {
            this.cards[3].active = !!newCondition;
        },

        cleanliness(newCleanliness) {
            this.cards[4].active = !!newCleanliness;
            this.cards[5].active = true;
        },

    },


    computed: {

        step1() {
            return this.selectedRestaurant != null;
        },

        step2() {
            return this.selectedCar != null;
        },

        step3() {
            return this.mileage != null;
        },

        step4() {
            return this.carCondition != null;
        },

        step5() {
            return this.cleanliness != null;
        },

        sendReportButtonActive() {
            return this.step1 && this.step2 && this.step3 && this.step4 && this.step5;
        }
    },

}
</script>
