<template>
    <div class="is-light-mode">

        <v-autocomplete v-model="selectedRestaurant" :items="restaurants" variant="solo-filled" item-title="name"
            item-value="id" label="Select Restaurant" @update:model-value="getShifts()"></v-autocomplete>

        <v-row v-if="selectedRestaurant != null">
            <v-col>
                <v-btn append-icon="mdi-plus" @click="addNewSchedule()" color="success" variant="elevated" class="mb-5">Add
                    Shift</v-btn>
            </v-col>
        </v-row>

        <!-- {{ shifts }} -->
        {{ shifts }}

        <Qalendar v-if="selectedRestaurant != null" :events="shifts" :config="config" @delete-event="deleteEvent"
            :key="calendarKey" @event-was-clicked="objectSelected" @updated-period="periodUpdated">
           
        </Qalendar>


        <!-- Dialog add schedule -->
        <v-dialog v-model="modifyShiftDialog" max-width="500px" persistent>
            <v-card>
                <v-card-title>
                    <v-row>
                        <v-col cols="10">
                            <v-autocomplete v-model="singleSchedule.with" :items="drivers" variant="underlined"
                                label="Driver" item-title="username" item-value="username">

                                <template v-slot:item="{ props, item }">
                                    <v-list-item v-bind="props" :title="item.raw.username"
                                        :subtitle="item.raw.last_name + ' ' + item.raw.first_name"></v-list-item>
                                </template>

                            </v-autocomplete>
                        </v-col>
                        <v-col cols="2" align="end">
                            <v-btn icon="mdi-close" @click="closeDialog()" variant="plain" />
                        </v-col>
                    </v-row>
                </v-card-title>

                <v-card-text>
                    <v-form v-model="form" @submit-prevent="updateSchedule(singleSchedule)">
                        <v-row>
                            <v-col>
                                <v-text-field v-model="editingShiftStart" label="Start" variant="underlined"
                                    hint="HH:MM 24h" persistent-hint :rules="rules" />
                            </v-col>
                            <v-col>
                                <v-text-field v-model="editingShiftEnd" label="End" variant="underlined" hint="HH:MM 24h"
                                    persistent-hint :rules="rules" />
                            </v-col>
                        </v-row>
                    </v-form>
                </v-card-text>

                <v-card-actions class="mb-1">
                    <v-row>
                        <v-col cols="6">
                            <v-btn block @click="deleteSchedule(singleSchedule)" color="error" text="Delete"
                                :disabled="adding"></v-btn>
                        </v-col>
                        <v-col cols="6">
                            <v-btn block @click="updateSchedule(singleSchedule)" color="success"
                                :text="adding ? 'Add' : 'Save'" :disabled="!form"></v-btn>
                        </v-col>
                    </v-row>
                </v-card-actions>

            </v-card>
        </v-dialog>
        <!-- Dialog add schedule -->

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
            date: null,

            restaurants: [],
            drivers: [
                {
                    username: 'No driver',
                    first_name: '',
                    last_name: 'This option is for unassigned shifts',
                }
            ],
            selectedRestaurant: null,
            selectedDate: null,
            isPeriodUpdated: false,

            calendarKey: 0,
            shifts: [],

            editingShift: null,
            editingShiftStart: null,
            editingShiftEnd: null,

            modifyShiftDialog: false,
            form: false,
            rules: [
                v => !!v || 'Time is required',
                v => /^([01]?[0-9]|2[0-3]):[0-5][0-9]$/.test(v) || 'Invalid time format. Use HH:MM 24h format',
            ],
            adding: false,
            tempId: 'new999999',
            singleSchedule: {
                id: null,
                with: null,
                time: {
                    start: null,
                    end: null,
                },
                color: 'red',
                isEditable: true,
            },

            config: {
                defaultMode: 'day',
                showCurrentTime: true,
                locale: 'pl-PL',
                isSilent: true,
                eventDialog: {
                    isCustom: true,
                },

                dayBoundaries: {
                    start: 9,
                    end: 23,
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
                        date: this.date,
                    }
                });
                this.shifts = response.data;

                this.shifts.forEach(shift => {
                    if (shift.with === null) {
                        shift.with = 'No driver';
                        shift.color = 'red';
                    }
                });

                let newDrivers = this.restaurants.find(restaurant => restaurant.id === this.selectedRestaurant).drivers;
                this.drivers = [...new Set([...this.drivers, ...newDrivers])];
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
        },
        // Get shifts

        // Period updated
        periodUpdated(data) {
            this.date = data;
            this.getShifts()
        },
        // Period updated

        async deleteSchedule(event) {
            const id = event.id;

            try {
                const response = await axios.delete(`api/restaurant/driver-shifts/delete/${id}/`);
                this.$store.dispatch('triggerAlert', { message: 'Successfully deleted', type: 'success' });
                this.getShifts();
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
            this.modifyShiftDialog = false;
        },

        objectSelected(event) {
            this.singleSchedule = {
                id: event.clickedEvent.id,
                with: event.clickedEvent.with,
                time: {
                    start: event.clickedEvent.time.start,
                    end: event.clickedEvent.time.end,
                },
                color: event.clickedEvent.color,
                isEditable: true,
            }
            this.editingShiftStart = event.clickedEvent.time.start.slice(-5);
            this.editingShiftEnd = event.clickedEvent.time.end.slice(-5);
            this.modifyShiftDialog = true;
        },

        addNewSchedule() {

            const start = new Date().toISOString().slice(0, 10);
            const end = new Date().toISOString().slice(0, 10);

            this.editingShiftStart = '09:00';
            this.editingShiftEnd = '16:00';

            this.singleSchedule = {
                id: this.tempId,
                with: this.drivers[0].username,
                time: {
                    start: this.editingShiftStart,
                    end: this.editingShiftEnd,
                },
                color: 'red',
                isEditable: true,
            };

            this.adding = true;
            this.modifyShiftDialog = true;
        },

        closeDialog() {
            this.modifyShiftDialog = false;
            this.adding = false;
        },

        async updateSchedule(props) {
            try {

                if (typeof props.id === 'string') {
                    props.restaurant = this.selectedRestaurant;

                    // Map start and end time to the shift
                    let currentDate = new Date();
                    let formattedDate = currentDate.toISOString().slice(0, 10);
                    props.time.start = formattedDate + ' ' + this.editingShiftStart;
                    props.time.end = formattedDate + ' ' + this.editingShiftEnd;

                    const response = await axios.post('api/restaurant/driver-shifts/create-update/', {
                        shift: props,
                    });
                    this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'success' });
                } else {
                    // Map start and end time to the shift
                    props.time.start = props.time.start.slice(0, -5) + this.editingShiftStart;
                    props.time.end = props.time.end.slice(0, -5) + this.editingShiftEnd;
                    const response = await axios.put('api/restaurant/driver-shifts/create-update/', {
                        shift: props,
                    });
                    this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'success' });
                }
                this.modifyShiftDialog = false;
                this.getShifts();
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }

        },

    },
    mounted() {
        this.loggedUserUsername = this.$store.getters.userData.username;
        this.date = new Date().toISOString().slice(0, 10);
        this.getRestaurants();
    },
};
</script>



<style>
@import "qalendar/dist/style.css";
</style>