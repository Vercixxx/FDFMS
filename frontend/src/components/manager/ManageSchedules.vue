<template>
    <v-row>
        <v-col cols="auto">
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
                    <v-col cols="auto">
                        <v-table density="compact" hover>
                            <thead>
                                <tr>
                                    <th class="text-left font-weight-black">
                                        Hours
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="hour in hoursList" :key="hour.hour">
                                    <td>{{ hour }}</td>
                                </tr>
                            </tbody>
                        </v-table>
                    </v-col>

                    <v-col cols='2' v-for="schedule in shiftSchedules" :key="schedule.id">
                        <v-table density="compact" hover>
                            <thead>
                                <tr>

                                    <th class="text-center font-weight-black" style="margin-right: 10px;">
                                        Shift {{ schedule.id }}
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="hour in hoursList" :key="hour.hour">
                                    <td :class="isDriverScheduled(schedule, hour) ? 'bg-teal' : ''">

                                    </td>
                                </tr>
                            </tbody>
                        </v-table>
                    </v-col>



                </v-row>



            </v-row>
        </v-col>
    </v-row>



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
            shiftSchedules: [],

            hoursListDict: {},
            id: 1,
            scheduleId: 1,




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
                    const scheduleId = appliedScheduleHours[0][2];

                    const newSingleSchedule = {
                        scheduleId: scheduleId,
                        id: this.id,
                        driver: 'empty',
                        start: start,
                        end: end,
                    };

                    this.id += 1;
                    this.shiftSchedules.push(newSingleSchedule);

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
                this.shiftSchedules,
            ]
            console.log(data)
            emit('showScheduleSelector', data)
        },

        isDriverScheduled(schedule, hour) {
            const scheduleStart = new Date(`2000-01-01 ${schedule.start}`);
            const scheduleEnd = new Date(`2000-01-01 ${schedule.end}`);
            const currentHour = new Date(`2000-01-01 ${hour}`);

            if (currentHour >= scheduleStart && currentHour <= scheduleEnd) {
                return schedule.driver !== 'empty' ? schedule.driver : 'free';
            } else {
                return '';
            }
        },

        // formatTime(date) {
        //     const hours = date.getHours().toString().padStart(2, '0');
        //     const minutes = date.getMinutes().toString().padStart(2, '0');
        //     return `${hours}:${minutes}`;
        // },


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
