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
                    <v-col v-for="schedule in dailySchedules">
                        <v-row>
                            <v-col align="center" class="text-h4">
                                Car {{ schedule.id }}
                            </v-col>
                        </v-row>
                        <v-data-table class="mx-2 border border-2 pa-4" hover :headers="headers" :items="generateTimeRows()"
                              hide-default-footer
  disable-pagination no-filter show-expand>

                            <template v-slot:item="{ item }">
                                <!-- <v-row>
                                    <v-col>
                                        {{ item.hour }}
                                    </v-col>
                                    <v-col>
                                        <v-btn block>
                                            -
                                        </v-btn>
                                    </v-col>
                                </v-row> -->
                                <tr>
                                    <td>
                                        {{ item.hour }}
                                    </td>
                                    <td>
                                        -
                                    </td>
                                </tr>
                              
                            </template>


                        </v-data-table>
                    </v-col>
                </v-row>






<!-- 
                <v-col v-for="schedule in dailySchedules" class="mx-3">
                    <v-row>
                        <v-col align="center">
                            Schedule {{ schedule.id }}
                        </v-col>
                    </v-row>

                    <v-row v-for="hour in hours" :key="hour" class="rounded-xl">
                        <v-col cols="3">{{ hour }}</v-col>
                        <v-col class="bg-teal" align="center">Krzysztof</v-col>
                    
                    </v-row>
                </v-col> -->

            </v-row>
        </v-col>
    </v-row>

    <div id="container" :style="{ height: containerHeight + 'px' }">
        <div id="resizable-box"></div>
        <div id="handler" @mousedown="startResize"></div>
    </div>
</template>

<script>
import format from 'date-fns/format'

export default {
    name: 'App',


    data() {
        return {
            myArray: [
                { id: 1, name: 'Treść elementu 1' },
                { id: 2, name: 'Treść elementu 2' },
                { id: 3, name: 'Treść elementu 3' },
            ],
            drag: false,
            date: null,
            dailySchedules: [
                {
                    id: 1,
                },
                // {
                //     id: 2,

                // },
            ],
            headers: [
                { text: 'Godzina', value: 'hour' },
                { text: 'User', value: 'working_user' },
            ],
            itemsPerPage: 25,
            containerHeight: 200, // Początkowa wysokość kontenera
            isResizing: false,
            startHeight: 0,
            startY: 0,
            snapHeight: 1, // Skok co 2% wysokości strony

        }


    },


    computed: {
        formattedDate() {
            return this.date ? format(this.date, 'EEEE, dd/LL/yyyy') : "Select date"
        }
    },



    methods: {
        generateTimeRows() {
            const startHour = 9;
            const endHour = 23;
            const timeRows = [];

            for (let hour = startHour; hour <= endHour; hour++) {
                timeRows.push({ hour: `${hour}:00` });
            }

            return timeRows;
        },
        startResize(e) {
            this.isResizing = true;
            this.startHeight = this.containerHeight;
            this.startY = e.clientY;

            document.addEventListener('mousemove', this.handleMouseMove);
            document.addEventListener('mouseup', this.stopResize);
        },
        handleMouseMove(e) {
            if (this.isResizing) {
                const newHeight = this.startHeight + e.clientY - this.startY;
                this.containerHeight = this.calculateSnapHeight(newHeight);
            }
        },
        stopResize() {
            this.isResizing = false;
            document.removeEventListener('mousemove', this.handleMouseMove);
            document.removeEventListener('mouseup', this.stopResize);
        },
        calculateSnapHeight(newHeight) {
            const windowHeight = window.innerHeight;
            const snapValue = Math.round(newHeight / (windowHeight * 0.05)) * (windowHeight * 0.05);
            return Math.max(snapValue, this.snapHeight);
        },
    },
};
</script>





<style scoped>
#container {
    position: relative;
    width: 200px;
    overflow: hidden;
}

#resizable-box {
    width: 100%;
    height: 100%;
    background: #FFF;
    border-radius: 10px;
}

#handler {
    position: absolute;
    height: 3%;
    width: 100%;
    border: 1px solid #000;
    background: #fff;
    cursor: ns-resize;
    bottom: 0;
    box-sizing: border-box;
}
</style>