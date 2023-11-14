<template>
    <v-app>
        <v-layout class="rounded rounded-md">

            <v-app-bar app :elevation="3" class="bg-teal-darken-2">


                <v-row align="center" no-gutters>

                    <!-- Menu button -->
                    <v-col cols="auto" align="start">
                        <v-app-bar-nav-icon @click.stop="drawer = !drawer" @mouseenter="drawer = true" >
                            <v-icon icon="mdi-menu" />
                        </v-app-bar-nav-icon>
                    </v-col>
                    <!-- Menu button -->


                    <!-- Title and location -->
                    <v-col>

                        <v-row class="ms-2 text-h6" align="center" justify="center">
                            <v-col cols="auto">
                                <v-btn icon="mdi-truck-fast" @click="changeComponent('HomeComponent')" ></v-btn>
                                <span class="font-weight-medium" v-if="!$vuetify.display.smAndDown">
                                    FDFMS
                                </span>
                            </v-col>
               

                            <v-col>
                                <!-- Visible on larger devices -->
                                <v-breadcrumbs :items="path" v-if="!$vuetify.display.smAndDown">
                                    <template v-slot:divider>
                                        <v-icon icon="mdi-chevron-right"></v-icon>
                                    </template>
                                    <template v-slot:title="{ item }">
                                        <span v-if="!item.disabled" @click="changeComponent(item.component)" role="button">
                                            {{ item.title.toUpperCase() }}
                                        </span>
                                        <span v-else>
                                            {{ item.title.toUpperCase() }}
                                        </span>
                                    </template>
                                </v-breadcrumbs>
                                <!-- Visible on larger devices -->


                                <!-- Visible on smaller devices -->
                                <span v-if="$vuetify.display.smAndDown">
                                    <v-select variant="underlined" :items="reversedPath" v-model="reversedPath[0]"
                                        :disabled="reversedPath.length === 1">
                                        <template #item="{ item }">

                                            <v-list-item align="center" justify="center">

                                                <p v-if="!item.raw.disabled" @click="changeComponent(item.raw.component)"
                                                    role="button" class="font-weight-bold"
                                                    :class="isDarkModeEnabled ? 'text-teal-lighten-2' : 'text-teal-darken-3'">
                                                    {{ item.title }}
                                                </p>
                                                <p v-else>
                                                    {{ item.title }}
                                                </p>

                                            </v-list-item>
                                        </template>
                                    </v-select>
                                </span>
                                <!-- Visible on smaller devices -->



                            </v-col>

                        </v-row>


                    </v-col>
                    <!-- Title and location -->


                    <!-- Log out -->
                    <v-col cols="auto" align="end">
                        <v-col cols="auto">

                            <v-tooltip :text="isDarkModeEnabled ? 'Enable light mode' : 'Enable dark mode'"
                                location="bottom">
                                <template v-slot:activator="{ props }">
                                    <v-btn :ripple="false" variant="plain" v-bind="props"
                                        :icon="isDarkModeEnabled ? 'mdi-weather-night' : 'mdi-white-balance-sunny'"
                                        @click="toggleTheme">

                                    </v-btn>
                                </template>
                            </v-tooltip>




                            <v-menu transition="slide-y-transition">
                                <template v-slot:activator="{ props }">

                                    <v-btn v-bind="props" ripple="false" variant="plain" icon="mdi-account-circle-outline">
                                    </v-btn>

                                </template>

                                <v-list class="p-0">
                                    <v-list-item class="p-0">

                                        <v-list-item-title class="text-center">
                                            Hi, {{ userData.username }}
                                        </v-list-item-title>

                                    </v-list-item>

                                    <v-list-item class="p-0">
                                        <v-btn block variant="flat" prepend-icon="mdi-email">Messages</v-btn>
                                    </v-list-item>

                                    <v-list-item class="p-0">
                                        <v-dialog transition="dialog-top-transition" width="400">
                                            <template v-slot:activator="{ props }">
                                                <v-btn v-bind="props" block variant="flat" append-icon="mdi-logout">
                                                    Logout
                                                </v-btn>
                                            </template>
                                            <template v-slot:default="{ isActive }">
                                                <v-card>
                                                    <div class="text-warning text-h6 text-md-h5 text-lg-h4">

                                                        <div
                                                            class="d-flex justify-content-between align-items-center px-4 pt-4">
                                                            <v-icon icon="mdi-alert" class="text-h4"/>
                                                            Logout
                                                            <v-icon icon="mdi-alert" class="text-h4"/>
                                                        </div>
                                                        <hr>
                                                    </div>

                                                    <div class="h2 text-h6 text-md-h5 text-lg-h4" align="center">
                                                        Are you sure?
                                                    </div>
                                                    <hr>

                                                    <div class="d-flex align-items-center justify-content-evenly mb-3">
                                                        <v-btn variant="outlined" width="130" class="mr-5"
                                                            @click="isActive.value = false">No</v-btn>
                                                        <v-btn variant="outlined" width="130" @click="logout" color="red" append-icon="mdi-logout">Yes</v-btn>
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
            <v-navigation-drawer app v-model="drawer" location="left"
                :class="{ '': !isDarkModeEnabled, 'bg-grey-darken-4': isDarkModeEnabled }">

                <v-list density="compact" nav class="pa-3">

                    <component :is="getNavigationComponent(userData.user_role)" />

                </v-list>


            </v-navigation-drawer>
            <!-- Menu -->


            <!-- Content -->
            <v-main :class="{ '': !isDarkModeEnabled, 'bg-grey-darken-4': isDarkModeEnabled }" @click="drawer = false">

                <!-- content -->
                <div class="cointainter m-2 p-2" :key="forceReload">
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

        <v-sheet app>
            <div class="pa-1 text-center w-100 " :class="isDarkModeEnabled ? 'bg-grey-darken-4' : ''">


                <span v-for="social in socials" :key="social.id" class="pa-3">
                    <a :href="social.link" target="_blank"
                        class="link-secondary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover">
                        <v-icon :icon="social.icon" />
                    </a>
                </span>

                {{ new Date().getFullYear() }} — Krzysztof Służałek

            </div>
        </v-sheet>


        <CreateMessage ref="createMessage" style="display: none;" :key="forceReload" />


        <!-- Add post dialog -->
        <AddPost ref="addPost" style="display: none;" :key="forceReload" />
        <!-- Add post dialog -->

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
let isDarkModeEnabled = theme.global.current.value.dark

function toggleTheme() {
    theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
    isDarkModeEnabled = theme.global.current.value.dark
    emit('theme', isDarkModeEnabled)
}

</script>


<script>
import { markRaw } from 'vue';
import useEventsBus from '../plugins/eventBus.js'

// Messages
import CreateMessage from '../components/SendMessage.vue'
// Messages

// Posts
import AddPost from '../components/AddPost.vue'
// Posts

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
import AddUser from '../components/hr/users/AddUser.vue';
import DriverUser from '../components/hr/users/AddDriver.vue';
import ManageUsers from '../components/hr/ManageUsers.vue'
// HR

// Clients
import AddClient from '../components/clients/AddClient.vue';
import ManageClients from '../components/clients/ManageClients.vue';
import AddBrand from '../components/clients/AddBrand.vue';
import ManageBrands from '../components/clients/ManageBrands.vue';
// Clients


// Asset
import AddCar from '../components/asset/AddCar.vue';
import ManageCars from '../components/asset/ManageCars.vue';
// Asset



export default {
    data() {
        return {
            userData: this.$store.getters.responseData,
            currentComponent: NonReactiveHome,
            path: [
                {
                    title: "Home",
                    component: 'HomeComponent',
                }
            ],
            confirmLogout: null,
            drawer: false,
            group: null,
            darkModeEnabled: true,

            alert: false,
            snackContent: '',

            forceReload: 0,

            isSmallScreen: false,


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

    components: {
        CreateMessage,
        AddPost,
    },

    computed: {
        reversedPath() {
            return this.path.slice().reverse();
        },

    },


    mounted() {
        this.$root.changeCurrentComponent = (functionName) => {
            if (this[functionName] && typeof this[functionName] === 'function') {
                this[functionName]();
            }
        };

        const { bus } = useEventsBus();
        watch(
            () => [bus.value.get('message'), bus.value.get('forceReload')],
            ([message, forceReload]) => {
                if (message) {
                    this.showSnackBar();
                }
                if (forceReload) {
                    this.forceReload += 1;
                }
            }
        );


    },


    watch: {
        group() {
            this.drawer = false
        },

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
                    title: "Home",
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
                    title: "Home",
                    component: 'HomeComponent',
                    disabled: false,
                },
                {
                    title: "Users",
                    component: '',
                    disabled: true,
                },
                {
                    title: 'Add user',
                    component: '',
                    disabled: true,
                },
            ];
        },
        ModifyUserComponent() {
            this.currentComponent = ManageUsers;
            this.path = [
                {
                    title: "Home",
                    component: 'HomeComponent',
                    disabled: false,
                },
                {
                    title: "Users",
                    component: '',
                    disabled: true,
                },
                {
                    title: 'Manage Users',
                    component: 'ManageUsers',
                    disabled: true,
                },
            ];
        },
        AddDriverComponent() {
            this.path = [
                {
                    title: "Home",
                    component: 'HomeComponent',
                    disabled: false,
                },
                {
                    title: "Users",
                    component: '',
                    disabled: true,
                },
                {
                    title: 'Add Driver User',
                    component: 'AddDriverComponent',
                    disabled: true,
                },
            ];
            this.currentComponent = DriverUser;
        },


        // Clients
        AddRestaurantComponent() {
            this.path = [
                {
                    title: "Home",
                    component: 'HomeComponent',
                    disabled: false,
                },
                {
                    title: "Restaurant",
                    component: '',
                    disabled: true,
                },
                {
                    title: 'Add restaurant',
                    component: '',
                    disabled: true,
                },
            ],
                this.currentComponent = AddClient
        },
        ManageRestaurantComponent() {
            this.path = [
                {
                    title: "Home",
                    component: 'HomeComponent',
                    disabled: false,
                },
                {
                    title: "Restaurant",
                    component: '',
                    disabled: true,
                },
                {
                    title: 'Manage restaurants',
                    component: '',
                    disabled: true,
                },
            ],
                this.currentComponent = ManageClients
        },
        AddBrandComponent() {
            this.path = [
                {
                    title: "Home",
                    component: 'HomeComponent',
                    disabled: false,
                },
                {
                    title: "Brands",
                    component: '',
                    disabled: true,
                },
                {
                    title: 'Add brand',
                    component: '',
                    disabled: true,
                },
            ],
                this.currentComponent = AddBrand
        },
        ManageBrandsComponent() {
            this.path = [
                {
                    title: "Home",
                    component: 'HomeComponent',
                    disabled: false,
                },
                {
                    title: "Brands",
                    component: '',
                    disabled: true,
                },
                {
                    title: 'Manage brands',
                    component: '',
                    disabled: true,
                },
            ],
                this.currentComponent = ManageBrands
        },


        // Assets
        AddCarsComponent() {
            this.path = [
                {
                    title: "Home",
                    component: 'HomeComponent',
                    disabled: false,
                },
                {
                    title: "Cars",
                    component: '',
                    disabled: true,
                },
                {
                    title: 'Add Car',
                    component: '',
                    disabled: true,
                },
            ];
            this.currentComponent = AddCar;
        },
        ShowCarsComponent() {
            this.path = [
                {
                    title: "Home",
                    component: 'HomeComponent',
                    disabled: false,
                },
                {
                    title: "Cars",
                    component: '',
                    disabled: true,
                },
                {
                    title: 'Manage Cars',
                    component: '',
                    disabled: true,
                },
            ];
            this.currentComponent = ManageCars;
        },
        // Assets




        showSnackBar() {
            const messageFromLocalStorage = localStorage.getItem('message');
            this.snackContent = JSON.parse(messageFromLocalStorage);
            this.alert = true;
            localStorage.removeItem('message')
        },




    },





}


</script>



<style>
html {
    scroll-behavior: smooth;
}
</style>