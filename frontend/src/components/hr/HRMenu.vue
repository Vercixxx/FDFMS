<template>
    <p align="center" class="text-blue">HR</p>
    <v-list>
        <v-list-item prepend-icon="mdi-home" @click="homeButton('HomeComponent')"
            class="rounded-xl bg-teal-darken-2 font-weight-bold">
            Home
        </v-list-item>
    </v-list>


    <!-- Users -->
    <v-menu transition="slide-y-transition">
        <template v-slot:activator="{ props }">
            <v-list-item prepend-icon="mdi-account-multiple" v-bind="props" class="my-3 font-weight-bold">
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
                            :title="option.name" @click="addUserButtonClick(option)">
                        </v-list-item>
                    </v-list>
                </v-menu>
            </v-list-item>
            <!-- Add -->

            <!-- Manage -->
            <v-list-item prepend-icon="mdi-list-status" @click="manageUsersClick()">
                Manage
            </v-list-item>
            <!-- Manage -->

        </v-list>
    </v-menu>
    <!-- Users -->




    <v-menu transition="slide-y-transition" v-for="button in buttons" :key="button.name" :disabled="button.disabled">
        <template v-slot:activator="{ props }">
            <v-list-item :prepend-icon="button.mainIcon" v-bind="props" class="my-3 font-weight-bold">
                {{ button.name }}
            </v-list-item>
        </template>

        <v-list density="compact" nav>

            <v-list-item v-for="option in button.options" :key="option.name" :prepend-icon="option.icon"
                :title="option.name" @click="handleButtonClick(option)">
            </v-list-item>

        </v-list>
    </v-menu>




    <!-- Messages -->
    <v-menu transition="slide-y-transition">
        <template v-slot:activator="{ props }">
            <v-list-item prepend-icon="mdi-forum" v-bind="props" class="my-3 font-weight-bold">
                Messages
            </v-list-item>

        </template>
        <v-list density="compact" nav>

            <!-- Add -->
            <v-list-item prepend-icon="mdi-plus" title="Add" @click="createMessage()">
            </v-list-item>
            <!-- Add -->

            <!-- Manage -->
            <v-list-item prepend-icon="mdi-list-status" title="Manage" @click="showMessages()">
            </v-list-item>
            <!-- Manage -->

        </v-list>
    </v-menu>
    <!-- Messages -->
</template>


<script>
import { closeDrawer } from '../../store/store.js'
import useEventsBus from '../../plugins/eventBus.js'
import { ref, watch } from "vue";
const { emit } = useEventsBus()

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
                    disabled: true,
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
                    mainIcon: 'mdi-account-group',
                    disabled: true,
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
                    name: 'Other',
                    mainIcon: 'mdi-lightning-bolt',
                    disabled: false,
                    options: [
                        {
                            name: 'Country/state',
                            click: '',
                            icon: 'mdi-city-variant',
                        },

                    ],
                },
            ]

        };
    },

    methods: {
        handleButtonClick(option) {
            closeDrawer();
            this.$root.changeCurrentComponent(option.name);
        },

        homeButton(functionName) {
            closeDrawer();
            this.$root.changeCurrentComponent(functionName);
        },

        addUserButtonClick(option) {
            if (option.name === 'Driver') {
                closeDrawer();
                this.$root.changeCurrentComponent('AddDriverComponent');
            }
            else {
                closeDrawer();
                localStorage.setItem('addingRole', option.name);
                emit('forceReload', '');
                this.$root.changeCurrentComponent('AddUserComponent');
            }
        },

        manageUsersClick() {
            closeDrawer();
            this.$root.changeCurrentComponent('ModifyUserComponent');
        },


        createMessage() {
            closeDrawer();
            emit('showAddMessage', '');
        },


        showMessages() {
            closeDrawer();
            emit('showMessageManager', '');
        },
    },

};
</script>