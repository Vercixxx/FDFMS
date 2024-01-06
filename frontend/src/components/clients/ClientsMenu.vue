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
</template>


<script>
export default {
    data() {
        return {
            buttons: [
                {
                    name: 'Restaurants',
                    mainIcon: 'mdi-silverware-fork-knife',
                    options: [
                        {
                            name: 'Add',
                            click: 'AddRestaurantComponent',
                            icon: 'mdi-plus',
                        },
                        {
                            name: 'Manage',
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
                            name: 'Add',
                            click: 'AddBrandComponent',
                            icon: 'mdi-plus',
                        },
                        {
                            name: 'Manage',
                            click: 'ManageBrandsComponent',
                            icon: 'mdi-list-status',
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