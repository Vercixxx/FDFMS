<template>
    <v-list>
        <v-list-item prepend-icon="mdi-home" @click="handleButtonClick('HomeComponent')" class="rounded-xl bg-teal-darken-2 font-weight-bold">
            Home
        </v-list-item>
    </v-list>

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
import { closeDrawer } from '../../store/store.js'

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
            closeDrawer();
            this.$root.changeCurrentComponent(functionName);
        },
    },

};
</script>