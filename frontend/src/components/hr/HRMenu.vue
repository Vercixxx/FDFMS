<template>
     <v-list>
        <v-list-item prepend-icon="mdi-home" @click="handleButtonClick('HomeComponent')" title="Home" class="rounded-xl text-h5 bg-teal-darken-2" elevation="2">
        </v-list-item>
    </v-list>

    <v-menu transition="slide-y-transition" v-for="button in buttons" :key="button.name">
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
import { closeDrawer } from '../../store/store.js'

export default {
    data() {
        return {
            buttons: [
                {
                    name: 'Users',
                    mainIcon: 'mdi-account-multiple',
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
                    ],
                },

                {
                    name: 'Statistics',
                    mainIcon: 'mdi-presentation',
                    options: [
                        {
                            name: 'Drivers statistics',
                            click: 'AddUserComponent',
                            icon: 'mdi-database-edit',
                        },
                        {
                            name: 'Managers statistics',
                            click: 'ModifyUserComponent',
                            icon: ' mdi-database-edit',
                        },
                    ],
                },

                {
                    name: 'Hr data',
                    mainIcon: 'mdi-party-popper',
                    options: [
                        {
                            name: 'Overtime',
                            click: 'AddUserComponent',
                            icon: 'mdi-database-edit',
                        },
                        {
                            name: 'Vacation',
                            click: 'ModifyUserComponent',
                            icon: ' mdi-database-edit',
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
                            icon: 'mdi-database-edit',
                        },
                        {
                            name: 'Show log',
                            click: 'ModifyUserComponent',
                            icon: ' mdi-database-edit',
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