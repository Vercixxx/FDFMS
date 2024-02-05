<template>
    <v-list-item prepend-icon="mdi-truck-fast" @click="changeComponent('HomeComponent')" class="font-weight-bold" disabled>
        FDFMS
    </v-list-item>

    <v-divider></v-divider>

    <!-- Temporary -->
    <p align="center">Driver</p>
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

    <!-- Other buttons -->
    <v-menu transition="slide-y-transition" v-for="button in buttons" :key="button.name">
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
    <!-- Other buttons -->


    <!-- Messages -->
    <v-menu transition="slide-y-transition">
        <template v-slot:activator="{ props }">
            <v-list-item prepend-icon="mdi-email" v-bind="props" class="font-weight-bold">
                Messages
            </v-list-item>

        </template>

        <v-list density="compact" nav>

            <!-- Manage -->
            <v-list-item prepend-icon="mdi-email-multiple-outline" title="Mailbox" @click="showMessages()">
            </v-list-item>
            <!-- Manage -->

        </v-list>
    </v-menu>
    <!-- Messages -->
</template>


<script>
export default {
    data() {
        return {
            buttons: [
                {
                    name: 'Cars',
                    disabled: true,
                    mainIcon: 'mdi-car',
                    options: [
                        {
                            name: 'Daily report',
                            click: 'DailyReportComponent',
                            icon: 'mdi-plus',
                        },
                        {
                            name: 'Add car damage',
                            click: 'AddCarDamageComponent',
                            icon: 'mdi-car-wrench',
                        },
                        // {
                        //     name: 'Show car damage',
                        //     click: '',
                        //     icon: 'mdi-list-status',
                        // },
                    ],
                },
                {
                    name: 'Schedule',
                    disabled: true,
                    mainIcon: 'mdi-calendar',
                    options: [
                        {
                            name: 'Show my shifts',
                            click: '',
                            icon: 'mdi-calendar-clock',
                        },
                        {
                            name: 'Sign up for shift',
                            click: '',
                            icon: 'mdi-calendar-plus',
                        },
                    ],
                },
                {
                    name: 'Work',
                    disabled: true,
                    mainIcon: 'mdi-briefcase',
                    options: [
                        {
                            name: 'Statut',
                            click: '',
                            icon: 'mdi-file-document-outline',
                        },
                        {
                            name: 'Contracts',
                            click: '',
                            icon: 'mdi-file-document-outline',
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

        showMessages() {
            this.$root.changeCurrentComponent('MailBoxComponent');
        },
    },

};
</script>