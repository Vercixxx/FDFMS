<template>
    <div>


        <v-card align='center' justify="center">
            <v-row class="mb-2">

                <v-col cols='3' v-for="button in buttons" :key="button.id">

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

                <v-textarea v-model="description" label="Describe damages" variant="solo-filled" class="mt-3" rows="3"
                    auto-grow clearable counter="1000"
                    :rules="[value => !!value || 'Field is required', value => (value && value.length <= 1000) || 'Max 1000 characters']"
                    append-icon="mdi-chat-alert"></v-textarea>
            </span>



            <span v-else-if="card == 4">
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



            </span>

            <!-- Buttons -->
            <v-row class="mt-3 mb-3">
                <v-col cols="6" align="start">
                    <v-btn variant="outlined" color="red" v-if="card > 1" @click="card--" prepend-icon="mdi-arrow-left">
                        {{ buttons[card - 2].text }}
                    </v-btn>
                </v-col>

                <v-col cols="6" align="end">
                    <v-btn v-if="card < 4" variant="outlined" color="teal" @click="card++"
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
    name: 'CarDamage',
    data() {
        return {
            loggedUser: null,

            availableRestaurants: [],
            selectedRestaurant: null,

            availableCars: [],
            selectedCar: null,

            objects: [],

            mileage: null,
            description: null,


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
                    text: 'Details',
                    active: false,
                    icon: 'mdi-numeric-3-circle',
                },
                {
                    id: 4,
                    text: 'Summary',
                    active: false,
                    icon: 'mdi-numeric-4-circle',
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
            this.buttons[1].active = this.selectedRestaurant != null;
        },

        selectedCar() {
            this.buttons[2].active = this.selectedCar != null;
        },

        mileage(newMileage) {
            this.buttons[3].active = newMileage && newMileage.length <= 7 && /^\d+$/.test(newMileage) && this.description && this.description.length <= 1000;
        },
        description(newDescription) {
            this.buttons[3].active = this.mileage && this.mileage.length <= 7 && /^\d+$/.test(this.mileage) && newDescription && newDescription.length <= 1000;
        },
    },


    computed: {
        allButtonsActive() {
            return this.buttons.every(button => button.active);
        },
    },

}
</script>
