<template>
    <v-app>
        <v-layout class="rounded rounded-md">

            <v-app-bar app :elevation="3" class="bg-teal-darken-2">


                <v-row align="center" no-gutters>

                    <!-- Menu button -->
                    <v-col cols="auto" align="start">
                        <v-app-bar-nav-icon @click.stop="drawer = !drawer">
                            <v-icon icon="mdi-menu" />
                        </v-app-bar-nav-icon>
                    </v-col>
                    <!-- Menu button -->


                    <!-- Title and location -->
                    <v-col>

                        <v-row class="ms-2 text-h6" align="center" justify="center">



                            <v-col>
                                <!-- Visible on larger devices -->
                                <v-breadcrumbs :items="path" v-if="!$vuetify.display.smAndDown" class="mt-3 text-body-1">
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


                    <!-- Right menu -->
                    <v-col cols="auto" align="end">
                        <v-col cols="auto">

                            <v-tooltip text="Help" location="bottom">
                                <template v-slot:activator="{ props }">
                                    <v-btn :ripple="false" variant="plain" v-bind="props" icon="mdi-help"
                                        color="blue-darken-4" @click="showHelp">

                                    </v-btn>
                                </template>
                            </v-tooltip>


                            <v-tooltip :text="isDarkModeEnabled ? 'Enable light mode' : 'Enable dark mode'"
                                location="bottom">
                                <template v-slot:activator="{ props }">
                                    <v-btn :ripple="false" variant="plain" v-bind="props"
                                        :icon="isDarkModeEnabled ? 'mdi-weather-night' : 'mdi-white-balance-sunny'"
                                        @click="toggleTheme">

                                    </v-btn>
                                </template>
                            </v-tooltip>

                            <v-tooltip text="Logout" location="bottom">
                                <template v-slot:activator="{ props }">
                                    <v-btn :ripple="false" variant="plain" v-bind="props" icon="mdi-logout"
                                        @click="logoutDialog = true">
                                    </v-btn>
                                </template>
                            </v-tooltip>


                            <v-dialog v-model="logoutDialog" width="400">
                                <v-card>
                                    <div class="text-warning text-h6 text-md-h5 text-lg-h4">
                                        <div class="d-flex justify-content-between align-items-center px-4 pt-4">
                                            <v-icon icon="mdi-alert" class="text-h4" />
                                            Logout
                                            <v-icon icon="mdi-alert" class="text-h4" />
                                        </div>
                                        <hr>
                                    </div>

                                    <div class="h2 text-h6 text-md-h5 text-lg-h4" align="center">
                                        Are you sure?
                                    </div>
                                    <hr>

                                    <div class="d-flex align-items-center justify-content-evenly mb-3">
                                        <v-btn variant="outlined" width="130" class="mr-5"
                                            @click="logoutDialog = false">No</v-btn>
                                        <v-btn variant="outlined" width="130" @click="logout" color="red"
                                            append-icon="mdi-logout">Yes</v-btn>
                                    </div>
                                </v-card>
                            </v-dialog>


                        </v-col>

                    </v-col>
                    <!-- Right menu -->


                </v-row>


            </v-app-bar>


            <!-- Menu -->
            <v-navigation-drawer v-model="drawer" location="left" expand-on-hover rail
                :class="{ '': !isDarkModeEnabled, 'bg-grey-darken-4': isDarkModeEnabled }">

                <v-list density="compact" nav class="pa-3">

                    <component :is="getNavigationComponent(userData.user_role)" />

                </v-list>


            </v-navigation-drawer>
            <!-- Menu -->


            <!-- Content -->
            <v-main :class="{ '': !isDarkModeEnabled, 'bg-grey-darken-4': isDarkModeEnabled }">

                <!-- content -->
                <div class="cointainter m-2 p-2" :key="forceReload">
                    <component :is="currentComponent"></component>
                </div>
                <!-- content -->

            </v-main>
            <!-- Content -->


        </v-layout>

        <footer>
            <div class="" align=center justify=center :class="isDarkModeEnabled ? 'bg-grey-darken-4' : ''">

                <span v-for="social in socials" :key="social.id" class="pa-3">
                    <a :href="social.link" target="_blank"
                        class="link-secondary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover">
                        <v-icon :icon="social.icon" />
                    </a>
                </span>

                {{ new Date().getFullYear() }} — Krzysztof Służałek

            </div>
        </footer>


        <CreateMessage ref="createMessage" style="display: none;" :key="forceReload" />

        <!-- Help dialog -->
        <HelpDialog ref="helpDialog" style="display: none;" :key="forceReload" />
        <!-- Help dialog -->

        <!-- Add post dialog -->
        <AddPost ref="addPost" style="display: none;" :key="forceReload" />
        <!-- Add post dialog -->

        <!-- Alert -->
        <MyAlert></MyAlert>
        <!-- Alert -->


    </v-app>
</template>

<script setup>
import { useTheme } from 'vuetify'
import useEventsBus from '../plugins/eventBus.js'
import { watch } from "vue";
const { emit } = useEventsBus()

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
const { emit } = useEventsBus()

// MyAlert
import MyAlert from '../components/MyAlert.vue'
// MyAlert

// Help dialog
import HelpDialog from '../components/HelpDialog.vue'
// Help dialog

// Messages
import CreateMessage from '../components/SendMessage.vue'
import MailBox from '../components/Mailbox.vue'
// Messages

// Posts
import AddPost from '../components/AddPost.vue'
// Posts

// Country and state
import ManageCountryState from '../components/ManageCountryState.vue'
// Country and state

// Home components
import Home from '../components/Home.vue';
const NonReactiveHome = markRaw(Home);
// Home components

// Navigation Bars
import AdminNav from '../components/admin/AdminMenu.vue'
import ClientsNav from "../components/clients/ClientsMenu.vue"
import HRNav from "../components/hr/HRMenu.vue"
import DriverNav from "../components/driver/DriverMenu.vue"
import RestManagerNav from "../components/manager/ManagerMenu.vue"
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


// Managers
import CreateSchedule from '../components/manager/ManageSchedules.vue';
import ManageDrivers from '../components/manager/ManageDrivers.vue';
import DailyDriverReport from '../components/manager/DailyDriverReport.vue';
import ManagerManageCars from '../components/manager/ManageCars.vue';
// Managers


// Drivers
import DailyReport from '..//components/driver/DailyReport.vue';
import AddCarDamage from '../components/driver/AddCarDamage.vue';
// Drivers



export default {
    data() {
        return {
            userData: this.$store.getters.userData,
            currentComponent: NonReactiveHome,
            path: [
                {
                    title: "Home",
                    component: 'HomeComponent',
                }
            ],
            logoutDialog: false,
            drawer: true,
            group: null,
            darkModeEnabled: true,

            alert: false,
            snackContent: { type: 'success' },

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
        HelpDialog,
        MyAlert,
        ManageCountryState,
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
                case "Driver":
                    return DriverNav;
                case "Manager":
                    return RestManagerNav;

                default:
                    return null;
            }
        },

        showHelp() {
            emit('showHelpDialog')
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




        // Messages
        MailBoxComponent() {
            this.currentComponent = MailBox;
            this.path = [
                {
                    title: "Home",
                    component: 'HomeComponent',
                    disabled: false,
                },
                {
                    title: "Messages",
                    component: '',
                    disabled: true,
                },
                {
                    title: 'Mail Box',
                    component: '',
                    disabled: true,
                },
            ];
        },
        // Messages


        // Country and state
        ModifyCountryStateComponent() {
            this.currentComponent = ManageCountryState;
            this.path = [
                {
                    title: "Home",
                    component: 'HomeComponent',
                    disabled: false,
                },
                {
                    title: "Country and state",
                    component: '',
                    disabled: true,
                },
                {
                    title: 'Manage country and state',
                    component: '',
                    disabled: true,
                },
            ];
        },
        // Country and state


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


        // Managers
        ManageScheduleComponent() {
            this.path = [
                {
                    title: "Home",
                    component: 'HomeComponent',
                    disabled: false,
                },
                {
                    title: "Schedule",
                    component: '',
                    disabled: true,
                },
            ];
            this.currentComponent = CreateSchedule;
        },

        ManageDriversComponent() {
            this.path = [
                {
                    title: "Home",
                    component: 'HomeComponent',
                    disabled: false,
                },
                {
                    title: "Drivers",
                    component: '',
                    disabled: true,
                },
                {
                    title: 'Manage Drivers',
                    component: '',
                    disabled: true,
                },
            ];
            this.currentComponent = ManageDrivers;
        },

        DailyDriverReportComponent() {
            this.path = [
                {
                    title: "Home",
                    component: 'HomeComponent',
                    disabled: false,
                },
                {
                    title: "Drivers",
                    component: '',
                    disabled: true,
                },
                {
                    title: 'Daily Report',
                    component: '',
                    disabled: true,
                },
            ];
            this.currentComponent = DailyDriverReport;
        },
        ManagerManageCarsComponent() {
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
            this.currentComponent = ManagerManageCars;
        },
        // Managers



        // Drivers
        DailyReportComponent() {
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
                    title: "Daily Report",
                    component: '',
                    disabled: true,
                },
            ];
            this.currentComponent = DailyReport;
        },

        AddCarDamageComponent() {
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
                    title: "Add Car Damage",
                    component: '',
                    disabled: true,
                },
            ];
            this.currentComponent = AddCarDamage;
        },
        // Drivers




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