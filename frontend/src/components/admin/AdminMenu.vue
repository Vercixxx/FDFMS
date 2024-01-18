<template>
    <div class="mb-15" v-for="menu in menus" :key="menu.name">
        <!-- <p class="text-center">{{ menu.name }}</p> -->
        <component :is="menu.menu"></component>
        <v-divider></v-divider>
    </div>

</template>

<script>
import AssetMenu from '../asset/AssetMenu.vue';
import HrMenu from '../hr/HRMenu.vue';
import ClientsMenu from '../clients/ClientsMenu.vue';
import PayrollMenu from '../payroll/PayrollMenu.vue';
import ManagerMenu from '../manager/ManagerMenu.vue';
import DriverMenu from '../driver/DriverMenu.vue';


export default {
    data() {
        return {
            assetMenu: AssetMenu,
            hrMenu: HrMenu,
            menus: [
                {
                    name: 'HR menu',
                    menu: HrMenu
                },
                // {
                //     name: 'Asset menu',
                //     menu: AssetMenu
                // },
                // {
                //     name: 'Clients menu',
                //     menu: ClientsMenu
                // },
                // {
                //     name: 'Payroll menu',
                //     menu: PayrollMenu
                // },
                // {
                //     name: 'Manager menu',
                //     menu: ManagerMenu
                // },
                {
                    name: 'Driver menu',
                    menu: DriverMenu
                },
            ]
        };
    },
}

</script>

