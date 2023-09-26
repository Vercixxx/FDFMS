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
                                <v-text-field v-model="username" placeholder="Username" :readonly="loading"
                                    :rules="[required]" class="mb-2" clearable density="compact">

                                    <template v-slot:prepend>
                                        <v-icon>
                                            <span class="material-symbols-outlined">
                                                person
                                            </span>
                                        </v-icon>
                                    </template>

                                </v-text-field>

                                <v-text-field v-model="password" :readonly="loading" :rules="[required]"
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

                                    <a href="#" class="link-danger link-offset-2 text-decoration-none">
                                        Forgot password
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                            class="bi bi-arrow-counterclockwise" viewBox="0 0 16 16">
                                            <path fill-rule="evenodd"
                                                d="M8 3a5 5 0 1 1-4.546 2.914.5.5 0 0 0-.908-.417A6 6 0 1 0 8 2v1z" />
                                            <path
                                                d="M8 4.466V.534a.25.25 0 0 0-.41-.192L5.23 2.308a.25.25 0 0 0 0 .384l2.36 1.966A.25.25 0 0 0 8 4.466z" />
                                        </svg>
                                    </a>
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

            <v-snackbar v-model="alert" :timeout="3000" location="top" color="warning">
                {{ errorContent }}
                <template v-slot:actions>
                    <v-btn color="pink" variant="text" @click="alert = false">
                        Close
                    </v-btn>
                </template>
            </v-snackbar>





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


    }),

    computed: {
        passwordIcon() {
            return this.passwordVisible ? this.eyeIcon : this.eyeOffIcon;
        },
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



        async login() {

            const username = this.username;
            const password = this.password;

            const data = {
                username: username.trim(),
                password: password.trim(),

            };

            const response = await axios.post('api/v1/login/', data)
            console.log(response.data)

            if (response.data.error) {
                this.isButtonDisabled = false;
                this.dataError = response.data.error;

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