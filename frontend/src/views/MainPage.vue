<template>
    <v-app>
        <v-layout class="rounded rounded-md">
            <!-- image="https://picsum.photos/1920/1080?random" -->
            <v-app-bar app :elevation="3" class="bg-blue-accent-3">


                <v-row align="center" no-gutters>

                    <!-- Menu button -->
                    <v-col cols="auto" align="start">
                        <v-app-bar-nav-icon @click.stop="drawer = !drawer">
                            <span class="material-symbols-outlined">
                                menu
                            </span>
                        </v-app-bar-nav-icon>
                    </v-col>
                    <!-- Menu button -->


                    <!-- Title -->
                    <v-col class="text-start">
                        FDFMS
                        <!-- <p class="text-h6 font-weight-bold">FDFMS - {{ userData.user_role }} Management console</p> -->
                    </v-col>

                    <!-- Title -->


                    <!-- Log out -->
                    <v-col cols="auto" align="end">
                        <v-col cols="auto">

                            <v-btn :ripple="false" variant="plain">
                                <span :style="{ display: actualTheme ? 'none' : 'block' }" @click="toggleTheme" role="button">
                                    <span class="material-symbols-outlined">
                                        dark_mode
                                    </span>
                                </span>
                                <span :style="{ display: actualTheme ? 'block' : 'none' }" @click="toggleTheme" role="button">
                                    <span class="material-symbols-outlined">
                                        light_mode
                                    </span>
                                </span>
                            </v-btn>





                            <v-btn variant="text">
                                <span class="material-symbols-outlined">
                                    search
                                </span>
                            </v-btn>


                            <v-menu transition="slide-x-transition">
                                <template v-slot:activator="{ props }">
                                    <v-btn v-bind="props">
                                        <span class="material-symbols-outlined">
                                            account_circle
                                        </span>
                                    </v-btn>
                                </template>

                                <v-list class="p-0">
                                    <v-list-item class="p-0">
                                        <v-btn block variant="flat">Profile</v-btn>
                                    </v-list-item>

                                    <v-list-item class="p-0">
                                        <v-dialog transition="dialog-top-transition" width="400">
                                            <template v-slot:activator="{ props }">
                                                <v-btn v-bind="props" block variant="flat">
                                                    <span class="material-symbols-outlined">
                                                        logout
                                                    </span>
                                                </v-btn>
                                            </template>
                                            <template v-slot:default="{ isActive }">
                                                <v-card>
                                                    <div class="text-warning text-h6 text-md-h5 text-lg-h4">

                                                        <div
                                                            class="d-flex justify-content-between align-items-center px-4 pt-4">
                                                            <span class="material-symbols-outlined">
                                                                warning
                                                            </span>
                                                            <span>
                                                                Logout
                                                            </span>
                                                            <span class="material-symbols-outlined">
                                                                warning
                                                            </span>
                                                        </div>
                                                        <hr>
                                                    </div>

                                                    <div class="h2 text-h6 text-md-h5 text-lg-h4" align="center">
                                                        Are you sure?
                                                    </div>
                                                    <hr>

                                                    <div class="justify-center d-flex align-items-center mb-3">
                                                        <v-btn variant="outlined" width="150" class="mr-5"
                                                            @click="isActive.value = false">No</v-btn>
                                                        <v-btn width="150" @click="logout" color="red">Yes</v-btn>
                                                    </div>
                                                </v-card>
                                            </template>
                                        </v-dialog>
                                    </v-list-item>

                                </v-list>
                            </v-menu>


                        </v-col>

                    </v-col>
                    <!-- Log out -->


                </v-row>


            </v-app-bar>


            <!-- Menu -->
            <v-navigation-drawer app v-model="drawer" location="left" temporary>
                <!-- image="https://picsum.photos/1920/1080?random" -->
                <v-list density="compact" nav>
                    <p class="fw-bold text-center fs-5">FDFMS</p>
                    <p class="fw-lighter">Food Delivery Fleet Management System</p>

                    <v-divider></v-divider>

                    <p class="text-center fw-bolder">Menu</p>
                    <component :is="getNavigationComponent(userData.user_role)" />

                </v-list>


            </v-navigation-drawer>
            <!-- Menu -->


            <!-- Content -->
            <v-main>
                <!-- content -->
                <div class="cointainter m-2 p-2">
                    <component :is="currentComponent"></component>
                </div>
                <!-- content -->
            </v-main>
            <!-- Content -->
        </v-layout>
    </v-app>
</template>

<script setup>
import { useTheme } from 'vuetify'
import { drawer, closeDrawer } from '../store/store.js';
import useEventsBus from '../plugins/eventBus.js'
const { emit } = useEventsBus()

const toggleDrawer = () => {
    drawer.value = !drawer.value
}

const theme = useTheme()
let actualTheme = theme.global.current.value.dark

function toggleTheme() {
    theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
    actualTheme = theme.global.current.value.dark
    emit('theme', actualTheme)
}

</script>


<script>
import { markRaw } from 'vue';

// Home components
import Home from '../components/Home.vue';
const NonReactiveHome = markRaw(Home);
// Home components

// Navigation Bars
import AdminNav from '../components/admin/AdminMenu.vue'
import ClientsNav from "../components/clients/ClientsMenu.vue"
import HRNav from "../components/hr/HRMenu.vue"
// Navigation Bars

// HR
import AddUser from '../components/hr/AddUser.vue';
import ModifyUser from '../components/hr/ModifyUser.vue';
import HrUser from '../components/hr/users/AddHr.vue';
import PayrollUser from '../components/hr/users/AddPayroll.vue';
import AssetUser from '../components/hr/users/AddAsset.vue';
import ClientUser from '../components/hr/users/AddClient.vue';
import ManagerUser from '../components/hr/users/AddManager.vue';
import DriverUser from '../components/hr/users/AddDriver.vue';
// HR

// Clients
import AddClient from '../components/clients/AddClient.vue';
import ShowClients from '../components/clients/ShowClients.vue';
// Clients

export default {
    data() {
        return {
            userData: this.$store.getters.responseData,
            currentComponent: NonReactiveHome,
            confirmLogout: null,
            drawer: false,
            group: null,
            darkModeEnabled: true,




        };
    },


    mounted() {
        this.$root.changeCurrentComponent = (functionName) => {
            if (this[functionName] && typeof this[functionName] === 'function') {
                this[functionName]();
            }
        };

        // Check for messages
        const message = localStorage.getItem('message');
        if (message) {
            console.log(message);
            localStorage.removeItem('message');
        }
    },


    methods: {
        toggleDarkMode() {
            this.darkModeEnabled = !this.darkModeEnabled;
            this.$vuetify.theme.dark = this.darkModeEnabled;
        },

        logoutConfirmFunc() {
            document.getElementById('confirmLogoutButton').click();
        },

        async logout() {
            this.$store.commit('resetState');
            this.$router.push('/');
        },
        getNavigationComponent(userRole) {
            switch (userRole) {
                case "Clients":
                    return ClientsNav;
                case "HR":
                    return AdminNav;

                default:
                    return null;
            }
        },


        HomeComponent() {
            this.currentComponent = NonReactiveHome;
        },

        // HR
        AddUserComponent() {
            this.currentComponent = AddUser
        },
        ModifyUserComponent() {
            this.currentComponent = ModifyUser
        },
        AddHrComponent() {
            this.currentComponent = HrUser;
        },
        AddPayrollComponent() {
            this.currentComponent = PayrollUser;
        },
        AddAssetComponent() {
            this.currentComponent = AssetUser;
        },
        AddClientComponent() {
            this.currentComponent = ClientUser;
        },
        AddManagerComponent() {
            this.currentComponent = ManagerUser;
        },
        AddDriverComponent() {
            this.currentComponent = DriverUser;
        },


        // Clients
        ClientsAddClientComponent() {
            this.currentComponent = AddClient
        },
        ClientsModifyClientComponent() {
            this.currentComponent = ShowClients
        },








    },


    watch: {
        group() {
            this.drawer = false
        },
    },

}


</script>



<style>
html {
    scroll-behavior: smooth;
}
</style>