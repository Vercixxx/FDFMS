<template>
    <p align="center" class="text-blue">Manager</p>
    <v-list>
        <v-list-item prepend-icon="mdi-home" @click="handleButtonClick('HomeComponent')"
            class="rounded-xl bg-teal-darken-2 font-weight-bold">
            Home
        </v-list-item>
    </v-list>

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

    <v-list-item @click="handleButtonClick('ManageScheduleComponent')" prepend-icon="mdi-store-clock-outline" class="my-3 font-weight-bold">
        Schedule
    </v-list-item>
</template>



<script>
export default {
    data() {
        return {
            buttons: [
                {
                    name: 'Drivers',
                    mainIcon: 'mdi-truck-delivery',
                    disabled: false,
                    options: [
                        {
                            name: 'Daily driver report',
                            click: 'AddUserComponent',
                            icon: 'mdi-plus',
                        },
                        {
                            name: 'Show drivers',
                            click: 'ModifyUserComponent',
                            icon: 'mdi-list-status',
                        },
                    ],
                },
                {
                    name: 'Cars',
                    mainIcon: 'mdi-car-multiple',
                    disabled: true,
                    options: [
                        {
                            name: 'Car management',
                            click: 'ModifyUserComponent',
                            icon: 'mdi-list-status',
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
                    name: 'Work',
                    mainIcon: 'mdi-briefcase',
                    disabled: true,
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
            this.$root.changeCurrentComponent(functionName);
        },
    },

};
</script>