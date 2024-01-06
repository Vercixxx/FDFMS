<template>
    <v-list-item prepend-icon="mdi-truck-fast" @click="changeComponent('HomeComponent')" class="font-weight-bold" disabled>
        FDFMS
    </v-list-item>

    <v-divider></v-divider>

    <!-- Temporary -->
    <p align="center">Asset</p>
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
</template>


<script>
export default {
    data() {
        return {
            buttons: [
                {
                    name: 'Cars',
                    mainIcon: 'mdi-car-multiple',
                    disabled: false,
                    options: [
                        {
                            name: 'Add',
                            click: 'AddCarsComponent',
                            icon: 'mdi-plus',
                        },
                        {
                            name: 'Manage',
                            click: 'ShowCarsComponent',
                            icon: 'mdi-list-status',
                        },
                    ],
                },
                {
                    name: 'Fleet',
                    mainIcon: 'mdi-bus-multiple',
                    disabled: true,
                    options: [
                        {
                            name: 'Add',
                            click: 'AddUserComponent',
                            icon: 'mdi-plus',
                        },
                        {
                            name: 'Manage',
                            click: 'ModifyUserComponent',
                            icon: 'mdi-list-status',
                        },
                        {
                            name: 'Transfer cars',
                            click: 'ModifyUserComponent',
                            icon: 'mdi-transfer',
                        },
                    ],
                },
                {
                    name: 'Messages',
                    mainIcon: 'mdi-forum',
                    disabled: true,
                    options: [
                        {
                            name: 'Create',
                            click: 'AddUserComponent',
                            icon: 'mdi-plus',
                        },
                        {
                            name: 'Show log',
                            click: 'ModifyUserComponent',
                            icon: 'mdi-database',
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