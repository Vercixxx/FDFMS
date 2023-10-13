<template>
    <v-app>
        <v-layout class="rounded rounded-md">

            <v-app-bar app :elevation="3" class="bg-teal-darken-2">


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

                        <div>

                            <span v-for="component in path" :key="component.name">

                                <v-btn :disabled="component.disabled" variant="plain"
                                    @click="changeComponent(component.component)">
                                    {{ component.name }}
                                </v-btn>
                                /
                            </span>
                        </div>

                    </v-col>

                    <!-- Title -->


                    <!-- Log out -->
                    <v-col cols="auto" align="end">
                        <v-col cols="auto">

                            <v-btn :ripple="false" variant="plain"
                                :icon="actualTheme ? 'mdi-weather-night' : 'mdi-white-balance-sunny'" @click="toggleTheme">
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

                                        <v-list-item-title class="text-center">
                                            Hi, {{ userData.username }}
                                        </v-list-item-title>

                                    </v-list-item>

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
            <v-navigation-drawer app v-model="drawer" location="left" temporary
                :class="{ '': !actualTheme, 'bg-grey-darken-3': actualTheme }">
                <v-list density="compact" nav class="pa-3">
                    <v-row>
                        <v-col cols="auto">
                            <v-icon icon="mdi-truck-fast" class="text-h3" />
                        </v-col>
                        <v-col class="text-h5">
                            FDFMS
                        </v-col>
                    </v-row>

                    <v-divider></v-divider>

                    <component :is="getNavigationComponent(userData.user_role)" />

                </v-list>


            </v-navigation-drawer>
            <!-- Menu -->


            <!-- Content -->
            <v-main :class="{ '': !actualTheme, 'bg-grey-darken-3': actualTheme }">
                <!-- content -->
                <div class="cointainter m-2 p-2">
                    <component :is="currentComponent"></component>
                </div>
                <!-- content -->
            </v-main>
            <!-- Content -->





            <!-- Snackbar -->
            <v-snackbar v-model="alert" :timeout="3000" location="bottom" :color="snackContent.type">
                {{ snackContent.message }}
                <template v-slot:actions>
                    <v-btn @click="alert = false">
                        Close
                    </v-btn>
                </template>
            </v-snackbar>
            <!-- Snackbar -->


        </v-layout>

        <v-sheet app class="elevation-4">
            <div class="pa-1 bg-grey-darken-3 text-center w-100 ">


                <span v-for="social in socials" :key="social.id" class="pa-3">
                    <a :href="social.link" target="_blank"
                        class="link-secondary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover">
                        <v-icon :icon="social.icon" />
                    </a>
                </span>

                {{ new Date().getFullYear() }} — Krzysztof Służałek

            </div>
        </v-sheet>


    </v-app>
</template>

<script setup>
import { useTheme } from 'vuetify'
import { drawer, closeDrawer } from '../store/store.js';
import useEventsBus from '../plugins/eventBus.js'
import { ref, watch } from "vue";
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
import useEventsBus from '../plugins/eventBus.js'

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


// Asset
import ShowCars from '../components/asset/ShowCars.vue';
import AddCar from '../components/asset/AddCar.vue';
// Asset



export default {
    data() {
        return {
            userData: this.$store.getters.responseData,
            currentComponent: NonReactiveHome,
            path: [
                {
                    name: "Home",
                    component: 'HomeComponent',
                }
            ],
            confirmLogout: null,
            drawer: false,
            group: null,
            darkModeEnabled: true,

            alert: false,
            snackContent: '',

            socials: [
                {
                    id: 1,
                    icon: 'mdi-github',
                    link: 'https://github.com/Vercixxx'
                },
                {
                    id: 2,
                    icon: 'mdi-linkedin',
                    link: 'https://www.linkedin.com/in/krzysztof-sluzalek/'
                },
            ]
        };
    },


    mounted() {
        this.$root.changeCurrentComponent = (functionName) => {
            if (this[functionName] && typeof this[functionName] === 'function') {
                this[functionName]();
            }
        };

        const { bus } = useEventsBus();
        watch(
            () => bus.value.get('message'),
            (val) => {
                this.showSnackBar();
            }
        );
    },


    methods: {
        toggleDarkMode() {
            this.darkModeEnabled = !this.darkModeEnabled;
            this.$vuetify.theme.dark = this.darkModeEnabled;
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

        changeComponent(name) {
            this.$root.changeCurrentComponent(name);
        },


        HomeComponent() {
            this.currentComponent = NonReactiveHome;
            this.path = [
                {
                    name: "Home",
                    component: 'NonReactiveHome',
                    disabled: true,
                },

            ];
        },

        // HR
        AddUserComponent() {
            this.currentComponent = AddUser;
            this.path = [
                {
                    name: "Home",
                    component: 'HomeComponent',
                },
                {
                    name: "Users",
                    component: '',
                    disabled: true,
                },
                {
                    name: 'Add User',
                    component: 'AddUserComponent',
                    disabled: true,
                },
            ];
        },
        ModifyUserComponent() {
            this.currentComponent = ModifyUser;
            this.path = [
                {
                    name: "Home",
                    component: 'HomeComponent',
                },
                {
                    name: "Users",
                    component: '',
                    disabled: true,
                },
                {
                    name: 'Show users',
                    component: 'ModifyUserComponent',
                    disabled: true,
                },
            ];
        },
        AddHrComponent() {
            this.currentComponent = HrUser;
            this.path = [
                {
                    name: "Home",
                    component: 'HomeComponent',
                },
                {
                    name: "Users",
                    component: '',
                    disabled: true,
                },
                {
                    name: 'Add User',
                    component: 'AddUserComponent',
                },
                {
                    name: 'Add HR User',
                    component: 'AddHrComponent',
                    disabled: true,
                },
            ];
        },
        AddPayrollComponent() {
            this.path = [
                {
                    name: "Home",
                    component: 'HomeComponent',
                },
                {
                    name: "Users",
                    component: '',
                    disabled: true,

                },
                {
                    name: 'Add User',
                    component: 'AddUserComponent',
                },
                {
                    name: 'Add Payroll user',
                    component: 'AddPayrollComponent',
                    disabled: true,
                },
            ]
            this.currentComponent = PayrollUser;
        },
        AddAssetComponent() {
            this.path = [
                {
                    name: "Home",
                    component: 'HomeComponent',
                },
                {
                    name: "Users",
                    component: '',
                    disabled: true,

                },
                {
                    name: 'Add User',
                    component: 'AddUserComponent',
                },
                {
                    name: 'Add Payroll user',
                    component: 'AddAssetComponent',
                    disabled: true,
                },
            ]
            this.currentComponent = AssetUser;
        },
        AddClientComponent() {
            this.path = [
                {
                    name: "Home",
                    component: 'HomeComponent',
                },
                {
                    name: "Users",
                    component: '',
                    disabled: true,
                },
                {
                    name: 'Add User',
                    component: 'AddUserComponent',
                },
                {
                    name: 'Add Client User',
                    component: 'AddClientComponent',
                    disabled: true,
                },
            ];
            this.currentComponent = ClientUser;
        },
        AddManagerComponent() {
            this.path = [
                {
                    name: "Home",
                    component: 'HomeComponent',
                },
                {
                    name: "Users",
                    component: '',
                    disabled: true,
                },
                {
                    name: 'Add User',
                    component: 'AddUserComponent',
                },
                {
                    name: 'Add Manager User',
                    component: 'AddManagerComponent',
                    disabled: true,
                },
            ];
            this.currentComponent = ManagerUser;
        },
        AddDriverComponent() {
            this.path = [
                {
                    name: "Home",
                    component: 'HomeComponent',
                },
                {
                    name: "Users",
                    component: '',
                    disabled: true,
                },
                {
                    name: 'Add User',
                    component: 'AddUserComponent',
                },
                {
                    name: 'Add Driver User',
                    component: 'AddDriverComponent',
                    disabled: true,
                },
            ];
            this.currentComponent = DriverUser;
        },


        // Clients
        ClientsAddClientComponent() {
            this.currentComponent = AddClient
        },
        ClientsModifyClientComponent() {
            this.currentComponent = ShowClients
        },


        // Assets
        AddCarsComponent() {
            this.currentComponent = AddCar;
        },
        ShowCarsComponent() {
            this.currentComponent = ShowCars;
        },
        // Assets













        showSnackBar() {
            const messageFromLocalStorage = localStorage.getItem('message');
            this.snackContent = JSON.parse(messageFromLocalStorage);
            this.alert = true;
            localStorage.removeItem('message')
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