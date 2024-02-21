<template>
    <div class="is-light-mode">

        <v-autocomplete v-model="selectedRestaurant" :items="restaurants" variant="solo-filled" item-title="name"
            item-value="id" label="Select Restaurant" @update:model-value="getShifts()"></v-autocomplete>

        {{ shifts }}


        <Qalendar v-if="selectedRestaurant != null" :events="shifts" :config="config" @delete-event="deleteEvent"
            @datetime-was-clicked="handleDatetimeClicked" :key="calendarKey">

            <!-- Dialog when clicked on scheduled -->
            <template #eventDialog="props">

                <v-card v-if="props.eventDialogData">
                    <v-card-title>
                        <v-row>
                            <v-col cols="10">
                                <v-autocomplete v-model="props.eventDialogData.with"
                                    :items="restaurants.find(restaurant => restaurant.id === selectedRestaurant)?.drivers"
                                    variant="solo-filled" label="Driver" item-title="username" item-value="username"
                                    @update:model-value="updateSchedule()">

                                    <template v-slot:item="{ props, item }">
                                        <v-list-item v-bind="props" :title="item.raw.username"
                                            :subtitle="item.raw.last_name + ' ' + item.raw.first_name"></v-list-item>
                                    </template>

                                </v-autocomplete>
                            </v-col>
                            <v-col cols="2" align="end">
                                <v-btn icon="mdi-close" @click="props.closeEventDialog" variant="plain" />
                            </v-col>
                        </v-row>
                    </v-card-title>

                    <v-card-text>
                        <v-row>
                            <v-col>
                                <v-text-field v-model="props.eventDialogData.time.start" label="Start"
                                    variant="underlined" />
                            </v-col>
                            <v-col>
                                <v-text-field v-model="props.eventDialogData.time.end" label="End" variant="underlined" />
                            </v-col>
                        </v-row>
                    </v-card-text>

                    <v-card-actions>
                        <v-row>
                            <v-col cols="6">
                                <v-btn block @click="props.closeEventDialog" color="danger">Delete</v-btn>
                            </v-col>
                            <v-col cols="6">
                                <v-btn block @click="props.saveEvent" color="primary">Save</v-btn>
                            </v-col>
                        </v-row>
                    </v-card-actions>

                </v-card>

            </template>
            <!-- Dialog when clicked on scheduled -->
        </Qalendar>
    </div>
</template>



<script>
import axios from "axios";
import { Qalendar } from "qalendar";

export default {
    name: 'ManageSchedules',

    components: {
        Qalendar,
    },


    data() {
        return {
            loggedUserUsername: null,
            overlay: false,

            restaurants: [],
            drivers: [
                {
                    username: 'No driver',
                    first_name: 'This option is for unassigned shifts',
                }
            ],
            selectedRestaurant: null,
            selectedDate: null,

            calendarKey: 0,
            shifts: [],
            tempId: 9999999999,
            newShift: {
                id: null,
                with: null,
                time: {
                    start: null,
                    end: null,
                },
                color: 'yellow',
                isEditable: true,
            },
            events: [
                {
                    title: "Advanced algebra",
                    with: "Thomas ",
                    time: { start: "2024-02-16 12:05", end: "2024-02-16 13:35" },
                    color: "purple",
                    isEditable: true,
                    id: "1",
                },
                {
                    title: "Advanced algebr23a",
                    with: "Andrew",
                    time: { start: "2024-02-16 12:05", end: "2024-02-16 13:35" },
                    color: "red",
                    isEditable: true,
                    id: "2",
                },
                {
                    with: "Nikola",
                    time: { start: "2024-02-16 12:05", end: "2024-02-16 13:35" },
                    color: "green",
                    isEditable: true,
                    id: "3",
                },

            ],

            config: {
                defaultMode: 'day',
                showCurrentTime: true,

                eventDialog: {
                    isCustom: true,
                },
            },




        };
    },


    methods: {

        // Get restaurants for manager
        async getRestaurants() {
            try {
                const response = await axios.get('api/rest_manager/get_restaurants_and_drivers/', {
                    params: {
                        username: this.loggedUserUsername,
                    }
                });

                this.restaurants = response.data;

            }
            catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
        },
        // Get restaurants for manager


        // Get shifts
        async getShifts() {
            try {
                const response = await axios.get('api/restaurant/driver-shifts/', {
                    params: {
                        restaurant: this.selectedRestaurant,
                        date: this.selectedDate,
                    }
                });
                this.shifts = response.data;
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
        },
        // Get shifts

        deleteEvent(event) {
            console.log(event);
        },

        handleDatetimeClicked(datetime) {
            let end = new Date(datetime);
            end.setHours(end.getHours() + 2);
            end = end.toISOString().slice(0, 16).replace('T', ' ');

            this.newShift = {
                id: this.tempId,
                with: 'Driver not set',
                time: {
                    start: datetime,
                    end: end,
                },
                color: 'yellow',
                isEditable: true,
            };

            this.shifts.push(this.newShift);
            this.calendarKey += 1;
            this.tempId -= 1;
        },

        updateSchedule() {
            console.log(this.newShift);
        },

    },
    mounted() {
        this.loggedUserUsername = this.$store.getters.userData.username;
        this.getRestaurants();
    },
};
</script>



<style>
@import "qalendar/dist/style.css";
</style>