<template>
    <v-app>

        <div class="text-center">
            <h1>Add new user </h1>
        </div>

        <v-card title="Choose user role" variant="tonal">
            <v-card-item class="d-flex justify-center pa-3">
                <v-btn v-for="button in buttons" :key="button.name" @click="setrole(button.component)" color="success mx-2" variant="tonal">
                    {{ button.name }}
                </v-btn>
            </v-card-item>
        </v-card>

    </v-app>
</template>
  
<script>
import axios from 'axios';

export default {
    name: 'App',

    data() {
        return {
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
            this.$root.changeCurrentComponent(role);
        }

    }

};
</script>
  