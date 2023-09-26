<template>
    <v-app>
        <v-layout class="rounded rounded-md">
            <!-- image="https://picsum.photos/1920/1080?random" -->
            <v-app-bar app :elevation="3" class="bg-success">


                <v-row align="center" no-gutters>

                    <!-- Menu button -->
                    <v-col cols="1" align="start">
                        <v-app-bar-nav-icon @click.stop="drawer = !drawer" class="ml-1">
                            <span class="material-symbols-outlined">
                                menu
                            </span>
                        </v-app-bar-nav-icon>
                    </v-col>
                    <!-- Menu button -->


                    <!-- Title -->
                    <v-col class="text-start">
                        <p class="text-h6 font-weight-bold">FDFMS - {{ userData.user_role }} Management console</p>
                    </v-col>

                    <!-- Title -->


                    <!-- Log out -->
                    <v-col cols="4" align="end">
                        <v-col cols="auto">
                            <v-dialog transition="dialog-top-transition" width="auto">
                                <template v-slot:activator="{ props }">
                                    <v-btn v-bind="props" variant="tonal">
                                        <span class="material-symbols-outlined">
                                            logout
                                        </span>
                                        Logout
                                    </v-btn>
                                </template>
                                <template v-slot:default="{ isActive }">
                                    <v-card>
                                        <v-toolbar>
                                            <v-row no-gutters class="text-warning">
                                                <!-- Lewa skrajna kolumna -->
                                                <v-col cols="2" class="text-start">
                                                    <span class="material-symbols-outlined">
                                                        warning
                                                    </span>
                                                </v-col>

                                                <!-- Środkowa kolumna -->
                                                <v-col cols="8"
                                                    class="text-center d-flex align-items-center justify-content-center fs-4">
                                                    <div>Logout</div>
                                                </v-col>

                                                <!-- Prawa skrajna kolumna -->
                                                <v-col cols="2" class="text-end">
                                                    <span class="material-symbols-outlined">
                                                        warning
                                                    </span>
                                                </v-col>
                                            </v-row>
                                        </v-toolbar>
                                        <v-card-text>
                                            <div class="text-h2 pa-12">Are you sure?</div>
                                        </v-card-text>
                                        <v-card-actions class="justify-center">
                                            <v-btn variant="outlined" @click="isActive.value = false">No</v-btn>
                                            <v-btn variant="outlined" @click="logout" color="red">Yes</v-btn>
                                        </v-card-actions>
                                    </v-card>
                                </template>
                            </v-dialog>
                        </v-col>

                    </v-col>
                    <!-- Log out -->


                </v-row>


            </v-app-bar>


            <!-- Menu -->
            <v-navigation-drawer app v-model="drawer" location="left" temporary>
                <!-- image="https://picsum.photos/1920/1080?random" -->
                <v-list density="compact" nav>
                    <v-list-item :title="`${userData.first_name} ${userData.last_name}`"
                        :subtitle="userData.email"></v-list-item>

                    <v-divider></v-divider>

                    <component :is="getNavigationComponent(userData.user_role)" />

                </v-list>

                <template v-slot:append>
                    <div class="d-flex align-center justify-center">
                        <v-btn block :style="{ display: actualTheme ? 'none' : 'block' }" @click="toggleTheme"
                            variant="plain">
                            <span class="material-symbols-outlined">
                                dark_mode
                            </span>
                        </v-btn>
                        <v-btn block :style="{ display: actualTheme ? 'block' : 'none' }" @click="toggleTheme"
                            variant="plain">
                            <span class="material-symbols-outlined">
                                light_mode
                            </span>
                        </v-btn>
                    </div>
                </template>

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
// import { isDarkMode } from '../plugins/theme.js';

const toggleDrawer = () => {
    drawer.value = !drawer.value
}

const theme = useTheme()
let actualTheme = theme.global.current.value.dark

function toggleTheme() {
    theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
    actualTheme = theme.global.current.value.dark
    // isDarkMode.value = actualTheme;

}

</script>


<script>
import { markRaw } from 'vue';

// Home components
import Home from '../components/Home.vue';
const NonReactiveHome = markRaw(Home);
// Home components

// Navigation Bars
import ClientsNav from "../components/clients/ClientsMenu.vue"
import HRNav from "../components/hr/HRMenu.vue"
// Navigation Bars

// HR
import AddUser from '../components/hr/AddUser.vue';
import ModifyUser from '../components/hr/ModifyUser.vue';
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
                    return HRNav;

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

        // Clients
        AddClientComponent() {
            this.currentComponent = AddClient
        },
        ModifyClientComponent() {
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