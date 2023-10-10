<template>
    <div class="text-center text-h4">
        Add new user
    </div>

    <div>

        <p class="text-h5">
            Choose user role
        </p>

        <v-btn block v-for="button in buttons" :key="button.name" :loading="loading" @click="setrole(button.component)"
            class="my-4 pa-6 text-h5 rounded-xl bg-teal-darken-3"  variant="elevated" style="letter-spacing:7px !important">
            {{ button.name }}
        </v-btn>

    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    name: 'App',

    data() {
        return {

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

    }

};
</script>
  