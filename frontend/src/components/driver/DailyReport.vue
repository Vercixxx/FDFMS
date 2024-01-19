<template>
    <div>


        <v-card align='center' justify="center">
            <v-row class="mb-2">

                <v-col cols='2' v-for="button in buttons" :key="button.id">

                    <v-btn variant="plain" :icon="button.icon" :color="button.active ? 'teal' : 'red'"
                        @click="card = button.id" :disabled="!button.active">
                    </v-btn>
                </v-col>

            </v-row>



            <span v-if="card == 1">
                <v-autocomplete variant="solo-filled" :items="availableRestaurants" v-model="selectedRestaurant"
                    label="Select restaurant" @update:model-value="getCars()"></v-autocomplete>
            </span>



            <span v-else-if="card == 2">
                <v-autocomplete variant="solo-filled" :disabled="selectedRestaurant == null" :items="availableCars"
                    label="Select car" v-model="selectedCar"></v-autocomplete>
            </span>


            <span v-else-if="card == 3">
                <v-text-field v-model="mileage" variant="solo-filled" label="Type mileage"
                    :rules="[value => !!value || 'Mileage is required', value => (value && value.length <= 7 && /^\d+$/.test(value)) || 'Mileage must be a number up to 7 digits']">
                    <template v-slot:append>km</template>
                </v-text-field>
            </span>



            <span v-else-if="card == 4">
                <h5>Car condition</h5>
                <v-rating v-model="carCondition" hover class="ma-2" :length="3" :item-labels="['Bad', '', 'Good']"
                    item-label-position="top" active-color="teal"></v-rating>
            </span>



            <span v-else-if="card == 5">
                <h5>Cleanliness</h5>
                <v-rating v-model="cleanliness" hover class="ma-2" :length="5"
                    :item-labels="['Bad', '', '', '', 'Excellent']" item-label-position="top"
                    active-color="teal"></v-rating>
            </span>




            <span v-else-if="card == 6">
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
                                <v-rating readonly hover :length="3" :model-value="carCondition" item-label-position="top"
                                    active-color="teal"></v-rating>
                            </td>
                        </tr>
                        <tr>
                            <td>Cleanliness</td>
                            <td>
                                <v-rating readonly hover :length="5" :model-value="cleanliness" item-label-position="top"
                                    active-color="teal"></v-rating>
                            </td>
                        </tr>
                    </tbody>
                </v-table>

                <v-textarea v-model="additional_remarks" label="Comments" variant="solo-filled" class="mt-3" rows="3"
                    auto-grow clearable counter="200"
                    :rules="[value => (value && value.length <= 200) || 'Max 200 characters']" append-icon="mdi-chat-alert"></v-textarea>

            </span>

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

export default {
    name: 'DailyReport',
    data() {
        return {
            loggedUser: null,

            availableRestaurants: [],
            selectedRestaurant: null,

            availableCars: [],
            selectedCar: null,

            objects: [],

            mileage: null,
            carCondition: null,
            cleanliness: null,
            additional_remarks: '',

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
                    text: 'Select car',
                    active: false,
                    icon: 'mdi-numeric-2-circle',
                },
                {
                    id: 3,
                    text: 'Type mileage',
                    active: false,
                    icon: 'mdi-numeric-3-circle',
                },
                {
                    id: 4,
                    text: 'Car condition',
                    active: false,
                    icon: 'mdi-numeric-4-circle',
                },
                {
                    id: 5,
                    text: 'Cleanliness',
                    active: false,
                    icon: 'mdi-numeric-5-circle',
                },
                {
                    id: 6,
                    text: 'Summary',
                    active: false,
                    icon: 'mdi-numeric-6-circle',
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
                this.availableRestaurants = Object.keys(this.objects)
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
        },
        // Get restaurants for logged user


        // Get cars for selected restaurant
        getCars() {
            this.availableCars = this.objects[this.selectedRestaurant];
        },
        // Get cars for selected restaurant


        // Send daily car report
        async sendReport() {
            try {
                const response = await axios.post(`api/car/dailyreport/add/`, {
                    driver: this.loggedUser,
                    car: this.selectedCar,
                    mileage: this.mileage,
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
            this.buttons[1].active = this.selectedRestaurant != null;
        },

        selectedCar() {
            this.buttons[2].active = this.selectedCar != null;
        },

        mileage(newMileage) {
            this.buttons[3].active = newMileage && newMileage.length <= 7 && /^\d+$/.test(newMileage);
        },
        carCondition(newCondition) {
            this.buttons[4].active = !!newCondition;
        },
        cleanliness(newCleanliness) {
            this.buttons[5].active = !!newCleanliness;
        },
    },


    computed: {
        allButtonsActive() {
            return this.buttons.every(button => button.active) && this.additional_remarks.length <= 200;
        },
    },

}
</script>
