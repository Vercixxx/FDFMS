<template>
    <v-row>
        <v-col cols="auto">
            <v-autocomplete label="Select restaurant"
                :items="['Sosnowiec plaza KFC']"
                variant="outlined"></v-autocomplete>

            <v-date-picker v-model="date" border="2" rounded=4 elevation="4" hide-header></v-date-picker>
            {{ date }}
            <v-row>
                <v-col align="center">
                    <v-btn variant="outlined" class="bg-teal my-5" @click="showScheduleSelector()" prepend-icon="mdi-plus">
                        Add shift
                    </v-btn>
                </v-col>
            </v-row>
        </v-col>
        <v-col>
            <v-row>
                <v-col align="center">
                    {{ formattedDate }}
                </v-col>
            </v-row>
            <v-row border="2" class="pa-2">

                <v-row>
                    <v-col cols="auto">
                        <table class="custom-table">
                            <thead>
                                <tr align="center">
                                    <th class="text-left font-weight-black">
                                        Hours
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="hour in hoursList" :key="hour.hour" align="center">
                                    <td>{{ hour }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </v-col>

                    <v-col cols='2' v-for="car in cars" :key="car.id">
                        <table>
                            <thead>
                                <tr align="center">
                                    <th class="text-center font-weight-black">
                                        Car {{ car.id }}
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="hour in hoursList" :key="hour.hour" align="center">
                                    <!-- <td :class="isDriverScheduled(schedule, hour) ? 'bg-teal' : ''">
                                        <span v-if="isDriverScheduled(schedule, hour) === 'null'">
                                        </span>

                                        <span v-else>
                                            {{ isDriverScheduled(schedule, hour) }}a

                                        </span>
                                    </td> -->
                                    test
                                </tr>
                            </tbody>
                        </table>
                    </v-col>



                </v-row>



            </v-row>
        </v-col>
    </v-row>

    {{ cars }}

    <v-row justify="center">
        <v-col cols="3">
            <v-btn block color="teal-darken-3">
                Save
            </v-btn>
        </v-col>
    </v-row>
    <ScheduleSelector ref="sreateMessage" style="display: none;" />
</template>

<script>
import format from 'date-fns/format'
import useEventsBus from '../../plugins/eventBus.js'
import { watch } from "vue";
const { emit } = useEventsBus()

import ScheduleSelector from './ScheduleSelector.vue';

export default {
    name: 'App',


    data() {
        return {

            date: null,
            hoursList: [],
            cars: [],

            hoursListDict: {},
            shiftId: 1,
            car: 1,




        }
    },


    components: {
        ScheduleSelector,
    },


    computed: {
        formattedDate() {
            return this.date ? format(this.date, 'EEEE, dd/LL/yyyy') : "Select date"
        }
    },


    mounted() {

        this.hoursList = this.generateTimeRows().map(item => item.hour);

        this.hoursList.forEach((hour, index) => {
            this.hoursListDict[index] = hour;
        });


        const { bus } = useEventsBus();
        watch(
            () => [bus.value.get('appliedScheduleHours')],
            ([appliedScheduleHours]) => {
                if (appliedScheduleHours) {
                    const start = appliedScheduleHours[0][0];
                    const end = appliedScheduleHours[0][1];
                    const carId = appliedScheduleHours[0][2];

                    const newSingleSchedule = {
                        carId: carId,
                        shiftId: this.shiftId,
                        driver: 'null',
                        start: start,
                        end: end,
                    };

                    this.shiftId += 1;
                    this.cars.push(newSingleSchedule);

                }
            }
        );

    },



    methods: {
        generateTimeRows() {
            const startHour = 9;
            const endHour = 23;
            const timeRows = [];

            for (let hour = startHour; hour < endHour; hour++) {
                timeRows.push({ hour: `${hour}:00` });
                timeRows.push({ hour: `${hour}:30` });
            }

            timeRows.push({ hour: `${endHour}:00` });

            return timeRows;
        },

        showScheduleSelector() {
            const data = [
                this.cars,
            ]
            console.log(data)
            emit('showScheduleSelector', data)
        },

        isDriverScheduled(schedule, hour) {
            const scheduleStart = new Date(`2000-01-01 ${schedule.start}`);
            const scheduleEnd = new Date(`2000-01-01 ${schedule.end}`);
            const currentHour = new Date(`2000-01-01 ${hour}`);

            if (currentHour >= scheduleStart && currentHour <= scheduleEnd) {
                return schedule.driver !== 'null' ? schedule.driver : '';
            } else {
                return '';
            }
        },


        // checkHourAvailability(currentHour, schedule) {
        //     const startHour = parseInt(schedule.start.split(':')[0]);
        //     const startMinute = parseInt(schedule.start.split(':')[1]);
        //     const endHour = parseInt(schedule.end.split(':')[0]);
        //     const endMinute = parseInt(schedule.end.split(':')[1]);

        //     const currentHourParsed = parseInt(currentHour.split(':')[0]);
        //     const currentMinuteParsed = parseInt(currentHour.split(':')[1]);

        //     const startTimeInMinutes = startHour * 60 + startMinute;
        //     const endTimeInMinutes = endHour * 60 + endMinute;
        //     const currentTimeInMinutes = currentHourParsed * 60 + currentMinuteParsed;

        //     if (currentTimeInMinutes >= startTimeInMinutes && currentTimeInMinutes < endTimeInMinutes) {
        //         return schedule.driver;
        //     }

        //     return 'free';
        // },

    },
};
</script>



<style scoped>
.custom-table {
    height: 65vh;
}
</style>