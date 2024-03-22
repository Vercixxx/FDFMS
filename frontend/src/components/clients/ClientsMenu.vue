<template>
    <v-list-item prepend-icon="mdi-truck-fast" @click="changeComponent('HomeComponent')" class="font-weight-bold" disabled>
        FDFMS
    </v-list-item>

    <v-divider></v-divider>

    <!-- Temporary -->
    <p align="center">Clients</p>
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

            <!-- Add -->
            <v-list-item prepend-icon="mdi-plus" title="Send message" @click="createMessage()">
            </v-list-item>
            <!-- Add -->

            <!-- Manage -->
            <v-list-item prepend-icon="mdi-email-multiple-outline" title="Mailbox" @click="showMessages()">
            </v-list-item>
            <!-- Manage -->

        </v-list>
    </v-menu>
    <!-- Messages -->
</template>


<script>
import useEventsBus from '../../plugins/eventBus.js'
const { emit } = useEventsBus()

export default {
    data() {
        return {
            buttons: [
                {
                    name: 'Restaurants',
                    mainIcon: 'mdi-silverware-fork-knife',
                    options: [
                        {
                            name: 'Add restaurant',
                            click: 'AddRestaurantComponent',
                            icon: 'mdi-plus',
                        },
                        {
                            name: 'Manage restaurants',
                            click: 'ManageRestaurantComponent',
                            icon: 'mdi-list-status',
                        },
                    ],
                },

                {
                    name: 'Brands',
                    mainIcon: 'mdi-domain',
                    options: [
                        {
                            name: 'Add brand',
                            click: 'AddBrandComponent',
                            icon: 'mdi-plus',
                        },
                        {
                            name: 'Manage brands',
                            click: 'ManageBrandsComponent',
                            icon: 'mdi-list-status',
                        },
                    ],
                },

                {
                    name: 'Ratings',
                    mainIcon: 'mdi-star-circle-outline',
                    disabled: true,
                    options: [
                        {
                            name: 'Manage ratings',
                            click: 'ManageRatingsComponent',
                            icon: 'mdi-database-edit',
                        },
                    ],
                },

                {
                    name: 'Other',
                    mainIcon: 'mdi-lightning-bolt',
                    disabled: false,
                    options: [
                        {
                            name: 'Manage countries/states',
                            click: 'ModifyCountryStateComponent',
                            icon: 'mdi-city-variant',
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

        createMessage() {
            emit('showAddMessage', '');
        },
    },

};
</script>