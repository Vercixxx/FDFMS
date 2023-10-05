<template>
    <div id="app">
        <div class="text-center">
            <h1>Add new user </h1>
        </div>

        <v-form>
            <v-card class="d-flex justify-center pa-3">
                <v-btn v-for="button in buttons" :key="button.name" @click="setrole(button.component)" color="success mx-2">
                    {{ button.name }}
                </v-btn>
            </v-card>
        </v-form>


    </div>
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
  