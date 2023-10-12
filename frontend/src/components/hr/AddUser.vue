<template>
    <div class="text-center text-h4">
        Add new user
    </div>

    <v-sheet class="pa-5 mt-4 rounded-lg" :class="{ 'bg-green-lighten-5': !theme, 'bg-grey-darken-4': theme }">

        <p class="text-h4">
            Choose user role
        </p>

        <div>
            <v-btn v-for="button in buttons" :key="button.name" :loading="loading" @click="setrole(button.component)"
                class="my-4 text-h5 rounded-x bg-teal-darken-3 mx-2" variant="elevated" style="letter-spacing:7px !important">
                {{ button.name }}
            </v-btn>
        </div>

    </v-sheet>
</template>
  
<script>
import axios from 'axios';
import useEventsBus from '../../plugins/eventBus.js'
import { watch } from "vue";
import { useTheme } from 'vuetify'

export default {
    name: 'App',

    data() {
        return {
            theme: true,
            loading: false,

            buttons: [
                {
                    name: 'HR',
                    component: 'AddHrComponent'
                },
                {
                    name: 'Payroll',
                    component: 'AddPayrollComponent'
                },
                {
                    name: 'Assset',
                    component: 'AddAssetComponent'
                },
                {
                    name: 'Client',
                    component: 'AddClientComponent'
                },
                {
                    name: 'Manager',
                    component: 'AddManagerComponent'
                },
                {
                    name: 'Driver',
                    component: 'AddDriverComponent'
                },
            ]
        };
    },

    methods: {
        setrole(role) {
            this.loading = true;
            this.$root.changeCurrentComponent(role);
        }

    },

    mounted() {
        // Dark mode
        const { bus } = useEventsBus();

        watch(
            () => bus.value.get('theme'),
            (val) => {
                const [themeBus] = val ?? [];
                this.theme = themeBus;
            }
        );

        const theme = useTheme();
        this.theme = theme.global.current.value.dark;
    },

};
</script>
  