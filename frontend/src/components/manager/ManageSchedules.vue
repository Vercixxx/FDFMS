<template>
    <v-row>
        <v-col cols="auto">
            <v-autocomplete label="Select restaurant" :items="['Sosnowiec plaza KFC']" variant="outlined"></v-autocomplete>

            <v-date-picker v-model="date" border="2" rounded=4 elevation="4" hide-header></v-date-picker>

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
                    <!-- <v-col cols="auto">
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
                    </v-col> -->

                    <!-- <v-col v-for="car in cars" :key="car.carId">
                        <span v-if="car.schedules.length > 0">
                            
                            <table>
                                <thead>
                                    <tr align="center">
                                        <th class="text-center font-weight-black">
                                            Car {{ car.carId }}
                                            
                                        </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="hour in hoursList" :key="hour" align="center">
                                        <td align="center" v-if="isHourScheduled(hour, car.schedules) === true"
                                        class="bg-teal" style="width: 200px;" role="button" @click="editSchedule(car.schedules)">
                                        &nbsp
                                    </td>
                                    <td v-else>
                                        {{ isHourScheduled(hour, car.schedules) }}
                                        &nbsp
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                        </span>
                    </v-col>
                     -->



                    <!-- Alternative -->

                    <v-col cols="auto">
                        <table>
                            <thead>
                                <tr align="center">
                                    <th class="text-left font-weight-black">
                                        Hours
                                    </th>
                                </tr>
                            </thead>
                            <tbody class="custom-table">
                                <tr v-for="hour in hoursList" :key="hour.hour" align="center">
                                    <td>{{ hour }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </v-col>


                    <v-col v-for="car in cars" :key="car.carId">
                        <v-row>
                            <v-col align="center">
                                Car {{ car.carId }}
                            </v-col>
                        </v-row>
                        <v-card color="teal" class="elevation-20" v-for="schedule in car.schedules" :style="{
                            'height': `${((hourToMinutes(schedule.end) - hourToMinutes(schedule.start)) / 30) * 2.48}vh`,
                            'margin-top': `${((hourToMinutes(schedule.start) - hourToMinutes('9:00')) / 30) * 2.48}vh`
                        }">
                            <v-row align="center">
                                <v-col>
                                    <div class="text-center">
                                        start {{ schedule.start }}
                                        end {{ schedule.end }}


                                        margin top: {{((hourToMinutes(schedule.start) - hourToMinutes('9:00')) / 30) * 2.48}}
                                    </div>
                                </v-col>
                            </v-row>
                        </v-card>

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
            cars: [
                {
                    carId: 1,
                    schedules: [

                    ],
                },
                {
                    carId: 2,
                    schedules: [

                    ],
                },
                {
                    carId: 3,
                    schedules: [

                    ],
                },
                {
                    carId: 4,
                    schedules: [

                    ],
                },
            ],


            hoursListDict: {},




        }
    },


    components: {
        ScheduleSelector,
    },


    computed: {
        formattedDate() {
            return this.date ? format(this.date, 'EEEE, dd/LL/yyyy') : "Select date"
        },
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
                this.handleAppliedScheduleHours(appliedScheduleHours);
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
            emit('showScheduleSelector', data)
        },


        editSchedule(carSchedules) {
            console.log(carSchedules)
        },


        handleAppliedScheduleHours(appliedScheduleHours) {
            if (appliedScheduleHours) {
                const start = appliedScheduleHours[0][0];
                const end = appliedScheduleHours[0][1];
                const carId = appliedScheduleHours[0][2];

                const carIndex = this.cars.findIndex(car => car.carId === carId);

                if (carIndex !== -1) {
                    if (!this.cars[carIndex].schedules) {
                        this.cars[carIndex].schedules = [];
                    }

                    const newSingleSchedule = {
                        driver: true,
                        start: start,
                        end: end,
                        blockHeight: (this.hourToMinutes(end) - this.hourToMinutes(start) / 30) * 2.48,
                        blockMarginTop: (this.hourToMinutes(start) - this.hourToMinutes('9:00') / 30) * 2.48,
                    };

                    this.cars[carIndex].schedules.push(newSingleSchedule);
                }
            }
        },


        isHourScheduled(hour, schedule) {
            const hourInMinutes = this.hourToMinutes(hour);

            for (const singleSchedule of schedule) {
                const startInMinutes = this.hourToMinutes(singleSchedule.start);
                const endInMinutes = this.hourToMinutes(singleSchedule.end);

                if (hourInMinutes >= startInMinutes && hourInMinutes <= endInMinutes) {
                    if (singleSchedule.breaks) {
                        for (const breakTime of singleSchedule.breaks) {
                            const breakStart = this.hourToMinutes(breakTime.start);
                            const breakEnd = this.hourToMinutes(breakTime.end);

                            if (hourInMinutes >= breakStart && hourInMinutes < breakEnd) {
                                return '';
                            }
                        }
                    }

                    return singleSchedule.driver;
                }
            }

            return '';
        },


        hourToMinutes(hour) {
            const [hourPart, minutePart] = hour.split(":");
            return parseInt(hourPart) * 60 + parseInt(minutePart);
        },


    },
};
</script>



<style scoped>
.custom-table {
    height: 65vh;
}
</style>