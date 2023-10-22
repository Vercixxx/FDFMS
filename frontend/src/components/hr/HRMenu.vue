<template>
    <v-list>
        <v-list-item prepend-icon="mdi-home" @click="handleButtonClick('HomeComponent')" title="Home"
            class="rounded-xl text-h5 bg-teal-darken-2" elevation="2">
        </v-list-item>
    </v-list>


    <!-- Users -->
    <v-menu transition="slide-y-transition">
        <template v-slot:activator="{ props }">
            <v-list-item prepend-icon="mdi-account-multiple" v-bind="props" class="my-3">
                Users
            </v-list-item>

        </template>
        <v-list density="compact" nav>

            <!-- Add -->
            <v-list-item>
                <v-menu transition="slide-y-transition">
                    <template v-slot:activator="{ props }">
                        <v-list-item prepend-icon="mdi-plus" v-bind="props">
                            Add
                        </v-list-item>

                    </template>
                    <v-list density="compact" nav>
                        <v-list-item v-for="option in buttonAdd" :key="option.name" :prepend-icon="option.icon"
                            :title="option.name" @click="handleButtonClick(option)">
                        </v-list-item>
                    </v-list>
                </v-menu>
            </v-list-item>
            <!-- Add -->

            <!-- Manage -->
            <v-list-item prepend-icon="mdi-list-status" title="Manage" @click="manageUsersClick()">
            </v-list-item>
            <!-- Manage -->

        </v-list>
    </v-menu>
    <!-- Users -->




    <v-menu transition="slide-y-transition" v-for="button in buttons" :key="button.name">
        <template v-slot:activator="{ props }">
            <v-list-item :prepend-icon="button.mainIcon" v-bind="props" class="my-3">
                {{ button.name }}
            </v-list-item>
        </template>

        <v-list density="compact" nav>

            <v-list-item v-for="option in button.options" :key="option.name" :prepend-icon="option.icon"
                :title="option.name" @click="handleButtonClick(option)">
            </v-list-item>

        </v-list>
    </v-menu>
</template>


<script>
import { closeDrawer } from '../../store/store.js'

export default {
    data() {
        return {
            buttonAdd: [

                {
                    name: 'HR',
                    click: 'AddHrComponent',
                    icon: 'mdi-account-group-outline',
                },
                {
                    name: 'Payroll',
                    click: 'AddPayrollComponent',
                    icon: 'mdi-cash-multiple',
                },
                {
                    name: 'Asset',
                    click: 'AddAssetComponent',
                    icon: 'mdi-car-multiple',
                },
                {
                    name: 'Client',
                    click: 'AddClientComponent',
                    icon: 'mdi-silverware-fork-knife',
                },
                {
                    name: 'Manager',
                    click: 'AddManagerComponent',
                    icon: 'mdi-account-hard-hat-outline',
                },
                {
                    name: 'Driver',
                    click: 'AddDriverComponent',
                    icon: 'mdi-truck-delivery-outline',
                },

            ],


            buttons: [
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
        handleButtonClick(option) {
            closeDrawer();
            this.$root.changeCurrentComponent(option.click);
        },
        manageUsersClick() {
            closeDrawer();
            this.$root.changeCurrentComponent('ModifyUserComponent');
        }
    },

};
</script>