<template>
    <v-list>
        <v-list-item prepend-icon="mdi-home" @click="handleButtonClick('HomeComponent')" title="Home" class="rounded-xl text-h5 bg-teal-darken-2">
        </v-list-item>
    </v-list>

    <v-menu transition="scale-transition" v-for="button in buttons" :key="button.name">
        <template v-slot:activator="{ props }">
            <v-list-item :prepend-icon="button.mainIcon" v-bind="props" class="my-3">
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
import { drawer, closeDrawer } from '../../store/store.js'

export default {
    data() {
        return {
            buttons: [
                {
                    name: 'Cars',
                    mainIcon: 'mdi-car',
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
            closeDrawer();
            this.$root.changeCurrentComponent(functionName);
        },
    },

};
</script>