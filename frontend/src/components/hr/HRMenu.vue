<template>
    <v-list-item>
        <v-btn block variant="text" @click="handleButtonClick('HomeComponent')">
            <span class="material-symbols-outlined">
                home
            </span>
            Home
        </v-btn>
    </v-list-item>

    <v-menu transition="scale-transition" v-for="button in buttons" :key="button.name">
        <template v-slot:activator="{ props }">
            <v-btn block color="primary" v-bind="props" variant="tonal" class="my-5">
                {{ button.name }}
            </v-btn>
        </template>

        <v-list>
            <v-list-item v-for="option in button.options" :key="option.name">
                <v-list-item-title>
                    <v-btn block @click="handleButtonClick(option.click)" :prepend-icon="option.icon">
                        {{ option.name }}
                    </v-btn>
                </v-list-item-title>
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
                    name: 'users',
                    options: [
                        {
                            name: 'add',
                            click: 'AddUserComponent',
                            icon: 'mdi-plus',
                        },
                        {
                            name: 'manage',
                            click: 'ModifyUserComponent',
                            icon: ' mdi-database-edit',
                        },
                    ],
                },

                {
                    name: 'Statistics',
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