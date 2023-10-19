<template>
    <v-app>
        <!-- <v-sheet class="rounded p-2 mt-2 mx-2 bg-teal-darken-2">

            <v-row justify="space-between">

                <v-col align="start">


                    <p class="text-h4 fst-italic  px-2">
                        <v-icon icon="mdi-truck-fast" />
                        &nbsp
                        <span class="fw-bold">F</span>ood
                        <span class="fw-bold">D</span>elivery
                        <span class="fw-bold">F</span>leet
                        <span class="fw-bold">M</span>anagement
                        <span class="fw-bold">S</span>ystem
                        - Log in
                    </p>
              
                </v-col>

                <v-col cols="3" class="d-flex align-center justify-end">

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



                </v-col>
            </v-row>


        </v-sheet> -->




        <v-list-item class="mx-auto pa-12" max-width="700" rounded="lg" align="center" justify="center">
            
            <v-row>
                <v-col cols="12">
                    <v-icon icon="mdi-truck-fast" class="text-h1" />
                </v-col>
            </v-row>

            <v-row>
                
                <v-col class="text-h3">
                    <span class="fw-bold ">F</span>ood
                    <span class="fw-bold">D</span>elivery
                    <span class="fw-bold">F</span>leet
                    <span class="fw-bold">M</span>anagement
                    <span class="fw-bold">S</span>ystem
                  
                </v-col>
            </v-row>
        </v-list-item>



        <v-main>


            <v-container fluid fill-height>
                <v-row align="center" justify="center">
                    <v-col cols="12" sm="8" md="6">

                        <v-card class="mx-auto pa-5" elevation="8" max-width="520" rounded="lg">

                            <v-row justify="end" class="mb-4">
                                <v-btn :ripple="false" variant="plain"
                                    :icon="actualTheme ? 'mdi-weather-night' : 'mdi-white-balance-sunny'"
                                    @click="toggleTheme">
                                </v-btn>
                            </v-row>

                            <div class="px-12 pb-12 pt-5">


                                <v-form v-model="form" @submit.prevent="onSubmit"  class="text-h5">

                                    <!-- Username field -->
                                    <v-text-field v-model="username" variant="outlined" label="Username"
                                        ref="usernameInput" :readonly="loading" :rules="usernameRules" class="mb-2" clearable
                                        density="compact" prepend-icon="mdi-account-tie">
                                    </v-text-field>
                                    <!-- Username field -->


                                    <div
                                        class="text-subtitle-1 text-medium-emphasis d-flex align-end justify-space-between">
                                        &nbsp

                                        <v-btn variant="plain" size="x-small" @click="passwordRecoverDialog = true"
                                            class="text-cyan-darken-4" prepend-icon="mdi-restore">
                                            Forgot password?
                                        </v-btn>
                                    </div>

                                    <!-- Password field -->
                                    <v-text-field v-model="password" variant="outlined" label="Password"
                                        ref="passwordInput" :readonly="loading" :rules="passwordRules" density="compact"
                                        :type="passwordVisible ? 'text' : 'password'" prepend-icon="mdi-key"
                                        :append-inner-icon="passwordVisible ? 'mdi-eye' : ' mdi-eye-off'"
                                        @click:append-inner="passwordVisible = !passwordVisible">
                                    </v-text-field>
                                    <!-- Password field -->


                                    <!-- Password remember/ password recover -->

                                    <v-row class="d-flex align-end justify-space-between">


                                        <v-checkbox v-model="rememberMe" hide-details label="Remember me"
                                            class="text-cyan-darken-4">
                                        </v-checkbox>


                                    </v-row>


                                    <br>

                                    <v-btn :disabled="!form" :loading="loading" block class="bg-teal-darken-2" size="large"
                                        type="submit" append-icon="mdi-login">
                                        Login
                                    </v-btn>
                                </v-form>
                            </div>

                        </v-card>


                    </v-col>
                </v-row>
            </v-container>

            <v-snackbar v-model="alert" :timeout="3000" location="top" color="red">
                <span class="fs-5">{{ errorContent }}</span>
                <template v-slot:actions>
                    <v-btn variant="tonal" @click="alert = false">
                        Close
                    </v-btn>
                </template>
            </v-snackbar>



            <!-- Password recovery -->
            <v-dialog v-model="passwordRecoverDialog" width="400">
                <v-card>
                    <v-card-text>
                        <p>Type your email below</p>
                        <v-text-field v-model="emailPasswordRecover" density="compact" hide-details="auto"
                            label="Email address" placeholder="example@example.com" type="email" class="mb-3">

                            <template v-slot:prepend>
                                <v-icon>
                                    <span class="material-symbols-outlined">
                                        mail
                                    </span>
                                </v-icon>
                            </template>

                        </v-text-field>
                        <v-btn block color="success" @click="passwordReset()">Recover password</v-btn>
                    </v-card-text>
                    <v-card-actions>
                        <v-btn color="primary" block @click="passwordRecoverDialog = false">Close</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>

            <v-dialog v-model="passwordRecoverDialogConfirm" width="auto">
                <v-card>
                    <v-card-text>
                        Email has been sent to {{ emailPasswordRecover }}. Please check your email box (mail might be in
                        spam).
                    </v-card-text>
                    <v-card-actions>
                        <v-btn color="primary" block @click="passwordRecoverDialogConfirm = false">Close</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <!-- Password recovery -->

        </v-main>
    </v-app>
</template>

<script setup>
import { useTheme } from 'vuetify'

const theme = useTheme()
let actualTheme = theme.global.current.value.dark

function toggleTheme() {
    theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
    actualTheme = theme.global.current.value.dark
}
</script>


<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
    data: () => ({
        form: false,
        username: null,
        password: null,
        passwordVisible: false,
        loading: false,
        atempt: 0,

        rememberMe: false,

        alert: false,
        errorContent: '',

        emailPasswordRecover: '',
        passwordRecoverDialog: false,
        passwordRecoverDialogConfirm: false,

        usernameRules: [
            v => !!v || 'Username is required',
            v => (v.length >= 3) || 'Username must containt at least 3 characters',
            v => /^[a-zA-Z0-9]+$/.test(v) || 'Only letters and numbers are allowed',
        ],

        passwordRules: [
            v => !!v || 'Password is required',
            v => (v.length >= 4) || 'Password must containt at least 4 characters',
        ],

    }),

    computed: {
        passwordIcon() {
            return this.passwordVisible ? this.eyeIcon : this.eyeOffIcon;
        },
    },

    mounted() {
        const cookie_username = Cookies.get('username');
        const cookie_password = Cookies.get('password');

        if (cookie_username && cookie_password) {
            this.$refs.usernameInput.value = cookie_username;
            this.$refs.passwordInput.value = cookie_password;

            this.$refs.usernameInput.dispatchEvent(new Event('input'));
            this.$refs.passwordInput.dispatchEvent(new Event('input'));
        }
    },

    methods: {
        onSubmit() {
            if (!this.form) return;
            this.loading = true

            this.login()

        },


        passwordReset() {
            this.passwordRecoverDialog = false;
            this.passwordRecoverDialogConfirm = true;

        },



        async login() {

            const username = this.username;
            const password = this.password;

            const data = {
                username: username.trim(),
                password: password.trim(),

            };

            try {
                const response = await axios.post('api/v1/login/', data)



                if (response.data.error) {
                    // alert
                    this.errorContent = response.data.error;
                    this.alert = true;
                    this.loading = false;
                }
                else {
                    // Authentication was successfull


                    // Vuex
                    this.$store.dispatch('setResponseData', response.data.data);

                    this.$store.commit('setAccessToken', response.data.jwt.access);
                    this.$store.commit('setRefreshToken', response.data.jwt.refresh);

                    axios.defaults.headers.common['Authorization'] = `JWT ${response.data.jwt.access}`;


                    // if (rememberMe) {
                    //     Cookies.set('username', username, { expires: new Date('9999-12-31') });
                    //     Cookies.set('password', password, { expires: new Date('9999-12-31') });
                    // }

                    this.$router.push('/dashboard');

                }
            }
            catch (error) {
                if (error.message === "Network Error") {
                    this.errorContent = "Server Error. Please try again.";
                    this.alert = true;
                    this.loading = false;
                }
            }


        },


    },

}
</script>