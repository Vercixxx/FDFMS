<template>
    <v-list-item prepend-icon="mdi-truck-fast" @click="changeComponent('HomeComponent')" class="font-weight-bold" disabled>
        FDFMS
    </v-list-item>

    <v-divider></v-divider>

    <!-- Temporary -->
    <p align="center">Manager</p>
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

    <v-menu transition="slide-y-transition" v-for="button in buttons" :key="button.name" :disabled="button.disabled">
        <template v-slot:activator="{ props }">
            <v-list-item :prepend-icon="button.mainIcon" v-bind="props" class="my-3 font-weight-bold">
                {{ button.name }}
            </v-list-item>
        </template>

        <v-list density="compact" nav>

            <v-list-item v-for="option in button.options" :key="option.name" :prepend-icon="option.icon"
                :title="option.name" @click="handleButtonClick(option.click)">
            </v-list-item>

        </v-list>
    </v-menu>

    <v-list-item @click="handleButtonClick('ManageScheduleComponent')" prepend-icon="mdi-store-clock-outline"
        class="my-3 font-weight-bold">
        Schedule
    </v-list-item>
</template>



<script>
export default {
    data() {
        return {
            buttons: [
                {
                    name: 'Drivers',
                    mainIcon: 'mdi-truck-delivery',
                    disabled: false,
                    options: [
                        {
                            name: 'Daily driver report',
                            click: 'DailyDriverReportComponent',
                            icon: 'mdi-plus',
                        },
                        {
                            name: 'Show drivers',
                            click: 'ManageDriversComponent',
                            icon: 'mdi-list-status',
                        },
                    ],
                },
                {
                    name: 'Fleets',
                    mainIcon: 'mdi-car-multiple',
                    disabled: false,
                    options: [
                        {
                            name: 'Cars management',
                            click: 'ManagerManageCarsComponent',
                            icon: 'mdi-list-status',
                        },
                    ],
                },
                // {
                //     name: 'Work',
                //     mainIcon: 'mdi-briefcase',
                //     disabled: true,
                //     options: [
                //         {
                //             name: 'Statut',
                //             click: 'AddUserComponent',
                //             icon: '<span class="material-symbols-outlined">add</span>',
                //         },
                //         {
                //             name: 'Contracts',
                //             click: 'ModifyUserComponent',
                //             icon: ' <span class="material-symbols-outlined">edit</span>',
                //         },
                //     ],
                // },
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