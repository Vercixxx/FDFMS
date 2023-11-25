<template>
    <v-row>
        <v-col cols="auto">
            <v-date-picker v-model="date" border="2" rounded=4 elevation="4" hide-header></v-date-picker>
        </v-col>
        <v-col>
            <v-row>
                <v-col align="center">
                    {{ formattedDate }}
                </v-col>
            </v-row>
            <v-row border="2" class="pa-2">

                <v-row>
                    <v-col v-for="schedule in dailySchedules" :key="schedule.id">
                        <v-col align="center">
                            <span class="text-h4">
                                Shift {{ schedule.id }}
                            </span>
                            <span v-if="schedule.free === true">
                                <v-row>
                                    <v-col class="font-weight-thin">
                                        No shifts yet
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col>
                                        <v-btn variant="outlined" class="bg-teal" @click="showScheduleSelector(schedule.id)"
                                            prepend-icon="mdi-plus">
                                            Add shift
                                        </v-btn>
                                    </v-col>
                                </v-row>
                            </span>


                        </v-col>
                    </v-col>
                </v-row>



            </v-row>
        </v-col>
    </v-row>

    {{ shiftSchedules }}

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

import ScheduleSelector from '../manager/ScheduleSelector.vue';

export default {
    name: 'App',


    data() {
        return {

            date: null,
            hoursList: [],

            hoursListDict: {},
            dailySchedules: [
                {
                    id: 1,
                    free: true,
                    schedules: [
                        // {
                        //     start: this.formatTime(new Date(0, 0, 0, 9, 0)),
                        //     end: this.formatTime(new Date(0, 0, 0, 19, 0)),
                        //     driver: 'Christopher',
                        // },
                        // {
                        //     start: this.formatTime(new Date(0, 0, 0, 19, 0)),
                        //     end: this.formatTime(new Date(0, 0, 0, 23, 0)),
                        //     driver: 'Adam',
                        // },
                    ]
                },
            ],

            id: 1,
            // singleSchedule: {
            //     id: null,
            //     driver: null,
            //     start: null,
            //     end: null,
            // },
            shiftSchedules: [],




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
                        driver: null,
                        start: start,
                        end: end,
                    };

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

        showScheduleSelector(scheduleId) {
            const data = [
                scheduleId,
            ]
            emit('showScheduleSelector', data)
        },



        formatTime(date) {
            const hours = date.getHours().toString().padStart(2, '0');
            const minutes = date.getMinutes().toString().padStart(2, '0');
            return `${hours}:${minutes}`;
        },


        checkHourAvailability(currentHour, schedule) {
            const startHour = parseInt(schedule.start.split(':')[0]);
            const startMinute = parseInt(schedule.start.split(':')[1]);
            const endHour = parseInt(schedule.end.split(':')[0]);
            const endMinute = parseInt(schedule.end.split(':')[1]);

            const currentHourParsed = parseInt(currentHour.split(':')[0]);
            const currentMinuteParsed = parseInt(currentHour.split(':')[1]);

            const startTimeInMinutes = startHour * 60 + startMinute;
            const endTimeInMinutes = endHour * 60 + endMinute;
            const currentTimeInMinutes = currentHourParsed * 60 + currentMinuteParsed;

            if (currentTimeInMinutes >= startTimeInMinutes && currentTimeInMinutes < endTimeInMinutes) {
                return schedule.driver;
            }

            return 'free';
        },

    },
};
</script>

