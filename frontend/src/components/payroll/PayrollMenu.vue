<template>
    <v-list-item prepend-icon="mdi-truck-fast" @click="changeComponent('HomeComponent')" class="font-weight-bold" disabled>
        FDFMS
    </v-list-item>

    <v-divider></v-divider>

    <!-- Temporary -->
    <p align="center">Payroll</p>
    <!-- Temporary -->

    <!-- Home -->
    <v-menu transition="slide-y-transition">
        <template v-slot:activator="{ props }">

            <v-list-item @click="homeButton()" v-bind="props" class=" font-weight-bold text-teal">
                <template v-slot:prepend>
                    <v-icon icon="mdi-home" color="teal"></v-icon>
                </template>
                Home
            </v-list-item>

        </template>

    </v-menu>
    <!-- Home -->


    <!-- Other -->
    <v-menu transition="slide-y-transition" v-for="button in buttons" :key="button.name" :disabled="button.disabled">
        <template v-slot:activator="{ props }">
            <v-list-item :prepend-icon="button.mainIcon" v-bind="props" class="font-weight-bold">
                {{ button.name }}
            </v-list-item>
        </template>

        <v-list density="compact" nav>

            <v-list-item v-for="option in button.options" :key="option.name" :prepend-icon="option.icon"
                :title="option.name" @click="handleButtonClick(option.click)">
            </v-list-item>

        </v-list>
    </v-menu>
    <!-- Other -->
</template>


<script>
export default {
    data() {
        return {
            buttons: [
                {
                    name: 'Users',
                    mainIcon: 'mdi-account-group',
                    disabled: false,
                    options: [
                        {
                            name: 'Drivers working hours',
                            click: 'DriversWorkingHoursComponent',
                            icon: 'mdi-calendar-clock',
                        },
                        {
                            name: 'Drivers daily reports',
                            click: 'DriverDailyReportsComponent',
                            icon: ' mdi-list-box',
                        },
                        {
                            name: 'Drivers statistics',
                            click: '',
                            icon: 'mdi-chart-line',
                        },
                    ],
                },
                {
                    name: 'Finance',
                    mainIcon: 'mdi-cash-multiple',
                    disabled: false,
                    options: [
                        {
                            name: 'Manage wages tariffs',
                            click: 'ManageWagesTariffsComponent',
                            icon: 'mdi-cash-edit',
                        },
                    ],
                },
            ]

        };
    },

    methods: {
        handleButtonClick(functionName) {
            this.$root.changeCurrentComponent(functionName);
        },

        homeButton() {
            this.$root.changeCurrentComponent('HomeComponent');
        },
    },

};
</script>