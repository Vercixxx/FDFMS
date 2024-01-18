<template>
    <v-card>
        <!-- <v-form class="pa-5">
            

            <v-divider></v-divider>


        </v-form> -->


        <v-stepper :mobile="$vuetify.display.smAndDown"
            :items="['Select restaurant', 'Select car', 'Type mileage', 'Car condition', 'Cleanliness', 'Summary']">

            <template v-slot:item.1>
                <v-card title="Select restaurant" flat>
                    <v-autocomplete variant="solo-filled" :items="availableRestaurants" v-model="selectedRestaurant"
                        @update:model-value="getCars()"></v-autocomplete>
                </v-card>
            </template>

            <template v-slot:item.2>
                <v-card title="Select car" flat>
                    <v-autocomplete variant="solo-filled" :disabled="selectedRestaurant == null" :items="availableCars"
                        v-model="selectedCar"></v-autocomplete>
                </v-card>
            </template>

            <template v-slot:item.3>
                <v-card title="Type mileage" flat>
                    <v-text-field v-model="mileage" variant="solo-filled" label="Mileage"></v-text-field>
                </v-card>
            </template>

            <template v-slot:item.4>
                <v-card title="Car condition" flat align="center">
                    <v-rating v-model="carCondition" hover class="ma-2" :length="3" :item-labels="['Bad', '', 'Good']"
                        item-label-position="top" active-color="teal"></v-rating>
                </v-card>
            </template>

            <template v-slot:item.5>
                <v-card title="Cleanliness" flat align="center">
                    <v-rating v-model="cleanliness" hover class="ma-2" :length="5"
                        :item-labels="['Bad', '', '', '', 'Good']" item-label-position="top" active-color="teal"></v-rating>
                </v-card>
            </template>


            <template v-slot:item.6>

                <v-card>
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
                                <td>Car</td>
                                <td>{{ selectedCar }}</td>
                            </tr>
                            <tr>
                                <td>Mileage</td>
                                <td>{{ mileage }}</td>
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
                        </tbody>
                    </v-table>
                </v-card>

            </template>
        </v-stepper>


    </v-card>
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

    },

}
</script>
