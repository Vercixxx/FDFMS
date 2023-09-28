<template>
    <v-app>
        <v-sheet class="rounded p-2 m-2 bg-success">

            <v-row justify="space-between">

                <v-col align="start">
                    <!-- Title -->
                    <p class="display-5 fst-italic mb-4 px-2">
                        <span class="fw-bold">F</span>ood
                        <span class="fw-bold">D</span>elivery
                        <span class="fw-bold">F</span>leet
                        <span class="fw-bold">M</span>anagement
                        <span class="fw-bold">S</span>ystem
                        - Log in
                    </p>
                    <!-- Title -->
                </v-col>

                <v-col cols="3" class="d-flex align-center justify-end">

                    <v-btn :style="{ display: actualTheme ? 'none' : 'block' }" @click="toggleTheme" variant="plain">
                        <span class="material-symbols-outlined">
                            dark_mode
                        </span>
                    </v-btn>
                    <v-btn :style="{ display: actualTheme ? 'block' : 'none' }" @click="toggleTheme" variant="plain">
                        <span class="material-symbols-outlined">
                            light_mode
                        </span>
                    </v-btn>


                </v-col>
            </v-row>


        </v-sheet>

        <v-main>


            <v-container fluid fill-height>
                <v-row align="center" justify="center">
                    <v-col cols="12" sm="8" md="6">

                        <v-card class="mx-auto pa-12 pb-8" elevation="8" max-width="448" rounded="lg">
                            <v-form v-model="form" @submit.prevent="onSubmit">
                                <v-text-field v-model="username" ref="usernameInput" placeholder="Username"
                                    :readonly="loading" :rules="[required]" class="mb-2" clearable density="compact">

                                    <template v-slot:prepend>
                                        <v-icon>
                                            <span class="material-symbols-outlined">
                                                person
                                            </span>
                                        </v-icon>
                                    </template>

                                </v-text-field>

                                <v-text-field v-model="password" ref="passwordInput" :readonly="loading" :rules="[required]"
                                    placeholder="Password" density="compact" :type="passwordVisible ? 'text' : 'password'">
                                    <template v-slot:prepend>
                                        <v-icon>
                                            <span class="material-symbols-outlined">
                                                key
                                            </span>
                                        </v-icon>
                                    </template>

                                    <template v-slot:append-inner>
                                        <v-icon @click="passwordVisible = !passwordVisible"
                                            :style="{ display: passwordVisible ? 'none' : 'block' }">
                                            <span class="material-symbols-outlined">
                                                visibility_off
                                            </span>
                                        </v-icon>

                                        <v-icon @click="passwordVisible = !passwordVisible"
                                            :style="{ display: passwordVisible ? 'block' : 'none' }">
                                            <span class="material-symbols-outlined">
                                                visibility
                                            </span>
                                        </v-icon>
                                    </template>
                                </v-text-field>


                                <!-- Password remember/ password recover -->
                                <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">

                                    <div class="form-check">
                                        <input type="checkbox" class="form-check-input" id="remember_me_checkbox">
                                        <label class="form-check-label" for="remember_me_checkbox">
                                            Remember me
                                        </label>
                                    </div>

                                    <v-btn variant="plain" size="x-small" @click="passwordRecoverDialog = true">
                                        <span class="material-symbols-outlined">
                                            restart_alt
                                        </span>
                                        Forgot password?
                                    </v-btn>
                                </div>

                                <br>

                                <v-btn :disabled="!form" :loading="loading" block color="success" size="large" type="submit"
                                    variant="outlined">
                                    Login
                                </v-btn>
                            </v-form>
                        </v-card>


                    </v-col>
                </v-row>
            </v-container>

            <v-snackbar v-model="alert" :timeout="3000" location="top" color="orange-darken-4">
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

        rememberMe: false,

        alert: false,
        errorContent: '',

        emailPasswordRecover: '',
        passwordRecoverDialog: false,
        passwordRecoverDialogConfirm: false,

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
            if (!this.form) return

            this.loading = true

            this.login()
            // setTimeout(() => (this.loading = false), 2000)
        },

        required(v) {
            return !!v || 'Field is required'
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


                // check if remeber_me is checked
                const checkbox = document.getElementById("remember_me_checkbox");
                if (checkbox.checked) {
                    Cookies.set('username', username, { expires: new Date('9999-12-31') });
                    Cookies.set('password', password, { expires: new Date('9999-12-31') });

                }

                this.$router.push('/dashboard');

            }
        },


    },

}
</script>