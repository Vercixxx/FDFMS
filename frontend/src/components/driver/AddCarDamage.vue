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

                <!-- Step 1 -->
                <v-window-item value="1">
                    <v-autocomplete variant="solo-filled" :items="restaurants" v-model="selectedRestaurant"
                        label="Select restaurant" @update:model-value="getCars()"
                        no-data-text="Sorry, you don't belong to any restaurant">
                    </v-autocomplete>
                </v-window-item>
                <!-- Step 1 -->

                <!-- Step 2 -->
                <v-window-item value="2">
                    <v-autocomplete variant="solo-filled" :disabled="selectedRestaurant == null" :items="cars"
                        label="Select car" v-model="selectedCar"
                        no-data-text="Sorry, there isn't available cars for selected restaurant">
                    </v-autocomplete>
                </v-window-item>
                <!-- Step 2 -->

                <!-- Step 3 -->
                <v-window-item value="3">
                    <v-text-field v-model="mileage" variant="solo-filled" label="Type mileage"
                        :rules="[value => !!value || 'Mileage is required', value => (value && value.length <= 7) || 'Mileage must be a number up to 7 digits', value => (value && /^\d+$/.test(value)) || 'Only digits are allowed']">
                        <template v-slot:append>km</template>
                    </v-text-field>

                    <v-textarea v-model="description" label="Describe damages" variant="solo-filled" class="mt-3" rows="3"
                        auto-grow clearable counter="1000"
                        :rules="[value => !!value || 'Field is required', value => (value && value.length <= 1000) || 'Max 1000 characters']"
                        append-icon="mdi-chat-alert"></v-textarea>
                </v-window-item>
                <!-- Step 3 -->

                <!-- Step 4 -->
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
                                <td>Description</td>
                                <td>
                                    {{ description }}
                                </td>
                            </tr>
                        </tbody>
                    </v-table>
                </v-window-item>
                <!-- Step 4 -->

            </v-stepper-window>



            <v-stepper-actions>
                <template v-slot:next="">

                    <v-btn v-if="step < 3" @click="step++" :disabled="!cards[step].active">
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
    name: 'CarDamage',
    data() {
        return {
            loggedUser: null,

            restaurants: [],
            selectedRestaurant: null,

            cars: [],
            selectedCar: null,

            objects: [],

            mileage: null,
            description: null,


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
                    text: 'Details',
                    active: false,
                },
                {
                    id: 4,
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
                const response = await axios.post(`api/car/damage/add/`, {
                    driver: this.loggedUser,
                    car: this.selectedCar,
                    car_mileage: this.mileage,
                    description: this.description,
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
    },


    computed: {
        step1() {
            return this.selectedRestaurant != null;
        },

        step2() {
            return this.selectedCar != null;
        },

        step3() {
            if (this.mileage && this.description && this.mileage.length <= 7 && /^\d+$/.test(this.mileage) && this.description.length <= 1000) {
                this.cards[2].active = true;
                return true;
            } else {
                this.cards[2].active = false;
                return false;
            }
        },

        sendReportButtonActive() {
            return this.step1 && this.step2 && this.step3;
        }
    },

}
</script>
