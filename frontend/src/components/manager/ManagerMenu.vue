<template>
    <v-sheet>

        <v-list-item>
            <v-btn block @click="handleButtonClick('HomeComponent')">
                <span class="material-symbols-outlined">
                    home
                </span>
                Home
            </v-btn>
        </v-list-item>

        <v-menu transition="scale-transition" v-for="button in buttons" :key="button.name">
            <template v-slot:activator="{ props }">
                <v-btn block color="success" v-bind="props" variant="tonal" class="my-5">
                    {{ button.name }}
                </v-btn>
            </template>

            <v-list>
                <v-list-item v-for="option in button.options" :key="option">
                    <v-list-item-title>
                        <v-btn block @click="handleButtonClick(option.click)">
                            <span v-html="option.icon"></span>
                            {{ option.name }}
                        </v-btn>
                    </v-list-item-title>

                </v-list-item>
            </v-list>
        </v-menu>

    </v-sheet>
</template>


<script>
import { closeDrawer } from '../../store/store.js'

export default {
    data() {
        return {
            buttons: [
                {
                    name: 'Drivers',
                    options: [
                        {
                            name: 'Daily driver report',
                            click: 'AddUserComponent',
                            icon: '<span class="material-symbols-outlined">add</span>',
                        },
                        {
                            name: 'Show drivers',
                            click: 'ModifyUserComponent',
                            icon: ' <span class="material-symbols-outlined">edit</span>',
                        },
                    ],
                },
                {
                    name: 'Cars',
                    options: [
                        {
                            name: 'Car management',
                            click: 'ModifyUserComponent',
                            icon: ' <span class="material-symbols-outlined">edit</span>',
                        },
                        {
                            name: 'Add car damage',
                            click: 'ModifyUserComponent',
                            icon: ' <span class="material-symbols-outlined">edit</span>',
                        },
                        {
                            name: 'Show car damage',
                            click: 'ModifyUserComponent',
                            icon: ' <span class="material-symbols-outlined">edit</span>',
                        },
                    ],
                },
                {
                    name: 'Schedule',
                    options: [
                        {
                            name: 'Modify Schedule',
                            click: 'AddUserComponent',
                            icon: '<span class="material-symbols-outlined">add</span>',
                        },
                    ],
                },
                {
                    name: 'Work',
                    options: [
                        {
                            name: 'Statut',
                            click: 'AddUserComponent',
                            icon: '<span class="material-symbols-outlined">add</span>',
                        },
                        {
                            name: 'Contracts',
                            click: 'ModifyUserComponent',
                            icon: ' <span class="material-symbols-outlined">edit</span>',
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