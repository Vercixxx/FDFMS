<template>
    <div class="is-light-mode">
        <Qalendar :events="events" :config="config" @delete-event="deleteEvent" >

        <template #eventDialog="props">

            <v-card v-if="props.eventDialogData && props.eventDialogData.title">
                <v-card-title>
                    <v-row>
                        <v-col>
                            {{ props.eventDialogData.with }}
                        </v-col>
                        <v-col align="end">
                            <v-btn icon="mdi-close" @click="props.closeEventDialog" variant="plain" />
                        </v-col>
                    </v-row>
                </v-card-title>

                <v-card-text>
                    <v-row>
                        <v-col>
                            <v-text-field v-model="props.eventDialogData.time.start" label="Start" variant="underlined" />
                        </v-col>
                        <v-col>
                            <v-text-field v-model="props.eventDialogData.time.end" label="End" variant="underlined" />
                        </v-col>
                    </v-row>
                </v-card-text>

                <v-card-actions>
                    <v-btn block @click="props.saveEvent" color="primary">Save</v-btn>
                </v-card-actions>

            </v-card>

        </template>
        </Qalendar>
    </div>
</template>



<script>
import { Qalendar } from "qalendar";

export default {
    name: 'ManageSchedules',

    components: {
        Qalendar,
    },


    data() {
        return {
            overlay: false,


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

        deleteEvent(event) {
            console.log(event);
        },


    },
    mounted() {

    },
};
</script>



<style>
@import "qalendar/dist/style.css";
</style>