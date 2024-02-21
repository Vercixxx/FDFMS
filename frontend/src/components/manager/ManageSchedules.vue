<template>
    <div class="is-light-mode">

        <v-autocomplete v-model="selectedRestaurant" :items="restaurants" variant="solo-filled" item-title="name"
            item-value="id" label="Select Restaurant" @update:model-value="getShifts()"></v-autocomplete>

        {{ editingShift }}

        <Qalendar v-if="selectedRestaurant != null" :events="shifts" :config="config" @delete-event="deleteEvent"
            @datetime-was-clicked="handleDatetimeClicked" :key="calendarKey" @event-was-clicked="objectSelected">

            <!-- Dialog when clicked on scheduled -->
            <template #eventDialog="props">

                <v-card v-if="props.eventDialogData">
                    <v-card-title>
                        <v-row>
                            <v-col cols="10">
                                <v-autocomplete v-model="props.eventDialogData.with" :items="drivers" variant="underlined"
                                    label="Driver" item-title="username" item-value="username"
                                    @update:model-value="updateSchedule(props.eventDialogData)">

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
                                <v-text-field v-model="editingShiftStart" label="Start" variant="underlined"
                                    @keydown.enter="updateSchedule(props.eventDialogData)" hint="Press enter to save"
                                    persistent-hint />
                            </v-col>
                            <v-col>
                                <v-text-field v-model="editingShiftEnd" label="End" variant="underlined"
                                    @keydown.enter="updateSchedule(props.eventDialogData)" hint="Press enter to save"
                                    persistent-hint />
                            </v-col>
                        </v-row>
                    </v-card-text>

                    <v-card-actions>
                        <v-btn block @click="props.closeEventDialog" color="danger">Delete</v-btn>
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
                    first_name: '',
                    last_name: 'This option is for unassigned shifts',
                }
            ],
            selectedRestaurant: null,
            selectedDate: null,

            calendarKey: 0,
            shifts: [],

            editingShift: null,
            editingShiftStart: null,
            editingShiftEnd: null,

            tempId: 'new999999',
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

        deleteEvent(event) {
            console.log(event);
        },

        objectSelected(event) {
            this.editingShift = event.clickedEvent;
            this.editingShiftStart = event.clickedEvent.time.start.slice(-5);
            this.editingShiftEnd = event.clickedEvent.time.end.slice(-5);
        },

        handleDatetimeClicked(datetime) {
            let end = new Date(datetime);
            end.setHours(end.getHours() + 2);
            end = end.toISOString().slice(0, 16).replace('T', ' ');

            this.newShift = {
                id: this.tempId,
                with: this.drivers[0].username,
                time: {
                    start: datetime,
                    end: end,
                },
                color: 'yellow',
                isEditable: true,
            };

            this.shifts.push(this.newShift);
            this.calendarKey += 1;

            let numberPart = this.tempId.slice(3);
            numberPart = Number(numberPart) - 1;
            this.tempId = 'new' + numberPart;
        },

        async updateSchedule(props) {
            try {
                // Map start and end time to the shift
                props.time.start = props.time.start.slice(0, -5) + this.editingShiftStart;
                props.time.end = props.time.end.slice(0, -5) + this.editingShiftEnd;

                if (typeof props.id === 'string') {
                    props.restaurant = this.selectedRestaurant;

                    const response = await axios.post('api/restaurant/driver-shifts/create-update/', {
                        shift: props,
                    });
                    this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'success' });
                } else {
                    const response = await axios.put('api/restaurant/driver-shifts/create-update/', {
                        shift: props,
                    });
                    this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'success' });
                }

                this.getShifts();
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }

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