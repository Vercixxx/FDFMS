<template>
    <v-row justify="center">
        <v-dialog v-model="showDialog" persistent width="400">

            <v-form @submit.prevent="applySelection">

                <v-card class="pa-5">
                    <v-card-title class="text-h5 font-weight-bold">
                        Choose hours
                    </v-card-title>
                    <v-card-text>

                        <v-select label="Select car" variant="outlined" :items="availableCars"
                            v-model="selectedCar">

                        </v-select>


                        <v-range-slider :disabled="selectedCar === null" reverse direction="vertical" v-model="selectedHours" strict min="0"
                            :max="hoursList.length - 1" :step="1" show-ticks="always" thumb-label="always"
                            thumb-color="green-darken-4" track-fill-color="green" track-size="20" density="comfortable">

                            <template v-slot:thumb-label="{ modelValue }">
                                <span class="text-h5">
                                    {{ hoursList[modelValue] }}
                                </span>
                            </template>

                        </v-range-slider>


                        
                        <p align="center">
                            Selected hours: <br>
                            {{ hoursListDict[selectedHours[0]] }} -
                            {{ hoursListDict[selectedHours[1]] }}
                        </p>



                    </v-card-text>

                    <!-- Buttons at the bottom-->
                    <v-row>
                        <v-col cols="6">
                            <v-btn block color="red-darken-1" variant="text" @click="closeDialog()">
                                Close
                            </v-btn>
                        </v-col>

                        <v-col cols="6">
                            <span>
                                <v-tooltip v-if="selectedCar === null" activator="parent" location="top" no-overflow>
                                    Select car
                                </v-tooltip>
                                <span>
                                    <v-btn block type="submit" color="green-darken-1" prepend-icon="mdi-check"
                                        variant="text" :disabled="selectedCar === null">
                                        Apply
                                    </v-btn>
                                </span>
                            </span>


                        </v-col>
                    </v-row>
                    <!-- Buttons at the bottom -->
{{ availableCars }}
                </v-card>
            </v-form>
        </v-dialog>
    </v-row>
</template>


<script>
import useEventsBus from '../../plugins/eventBus.js'
import { watch } from "vue";
const { emit } = useEventsBus()

export default {
    name: 'App',


    data() {
        return {
            showDialog: false,
            availableCars: [],
            selectedCar: 1,
            hoursListDict: {},
            hoursList: [],
            selectedHours: [0, 28],
        }
    },



    mounted() {
        this.hoursList = this.generateTimeRows().map(item => item.hour);

        this.hoursList.forEach((hour, index) => {
            this.hoursListDict[index] = hour;
        });

        const { bus } = useEventsBus();
        watch(
            () => [bus.value.get('showScheduleSelector')],
            ([showScheduleSelector]) => {
                if (showScheduleSelector) {
                    this.showDialog = true;

                    const carIds = showScheduleSelector[0][0];
                    this.availableCars = carIds.map(item => item.carId)
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


        closeDialog() {
            this.showDialog = false;
            this.selectedHours = [0, 28];
        },

        applySelection() {
            const selected = [
                this.hoursListDict[this.selectedHours[0]],
                this.hoursListDict[this.selectedHours[1]],
                this.selectedCar
            ]

            emit('appliedScheduleHours', selected);
            this.closeDialog();
        },

    },
};
</script>