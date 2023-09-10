<template>
    <div id="app">
        <div class="text-center">
            <h1>Add new user </h1>
        </div>

        <form action="" method="post" @submit.prevent="setrole">
            <!-- User role -->
            <div class="btn-group-horizontal border rounded p-2 mb-3 " role="group"
                aria-label="Horizontal radio toggle button group">
                <p class="fs-3">Choose user role</p>

                <div class="containter">
                    <input type="radio" class="btn-check" name="vbtn-radio" id="HR" autocomplete="off" value="HR" checked>
                    <label class="btn btn-outline-secondary m-2" for="HR">HR</label>

                    <input type="radio" class="btn-check" name="vbtn-radio" id="Payroll" value="Payroll" autocomplete="off">
                    <label class="btn btn-outline-secondary m-2" for="Payroll">Payroll</label>

                    <input type="radio" class="btn-check" name="vbtn-radio" id="Asset" value="Asset" autocomplete="off">
                    <label class="btn btn-outline-secondary m-2" for="Asset">Asset</label>

                    <input type="radio" class="btn-check" name="vbtn-radio" id="Client" value="Client" autocomplete="off">
                    <label class="btn btn-outline-secondary m-2" for="Client">Client</label>

                    <input type="radio" class="btn-check" name="vbtn-radio" id="Manager" value="Manager" autocomplete="off">
                    <label class="btn btn-outline-secondary m-2" for="Manager">Restaurant manager</label>

                    <input type="radio" class="btn-check" name="vbtn-radio" id="Driver" value="Driver" autocomplete="off">
                    <label class="btn btn-outline-secondary m-2" for="Driver">Driver</label>
                </div>

            </div>

            <div class="text-center">

                <button type="button" name="" id="" class="btn btn-success " @click="setrole">
                    Add
                    <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor"
                        class="bi bi-plus-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z" />
                        <path
                            d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z" />
                    </svg>
                </button>
            </div>


        </form>


    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    name: 'App',

    data() {
        return {

        };
    },

    methods: {
        setrole() {
            const selectedRole = document.querySelector('input[name="vbtn-radio"]:checked').value;
            switch (selectedRole) {
                case 'HR':
                    this.$parent.showAddHrComponent();
                    break;
                case 'Payroll':
                    this.$parent.showAddPayrollComponent();
                    break;
                case 'Asset':
                    this.$parent.showAddAssetComponent();
                    break;
                case 'Client':
                    this.$parent.showAddClientComponent();
                    break;
                case 'Manager':
                    this.$parent.showAddManagerComponent();
                    break;
                case 'Driver':
                    this.$parent.showAddDriverComponent();
                    break;
                default:
                    break
            }

        }

    }

};
</script>
  