<template>
    <v-app>
        <div
            style="background: linear-gradient(to bottom right, rgba(0, 225, 255, 1), rgb(47, 111, 172), rgb(211, 94, 114))">


            <!-- Mobile -->
            <v-container fill-height fluid v-if="$vuetify.display.smAndDown" style="min-height: 100dvh;">

                <v-row align="center" justify="center">
                    <v-col align="center" style="text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.8);">
                        <v-icon icon="mdi-truck-fast" class="text-h2" />
                    </v-col>

                    <v-col align="center" class="text-h5 pa-4" style="text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);">
                        <span class="fw-bold">F</span>ood
                        <span class="fw-bold">D</span>elivery
                        <span class="fw-bold">F</span>leet
                        <span class="fw-bold">M</span>anagement
                        <span class="fw-bold">S</span>ystem

                    </v-col>
                </v-row>

                <!-- Form -->
                <v-row align="center" justify="center" style="min-height: 70dvh;">

                    <v-card class="bg-blue-grey-darken-3 rounded-xl pa-10 elevation-20" style="width: 90dvw;">
                        <v-form v-model="form" @submit.prevent="onSubmit" class="text-h4"
                        style="text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);">
                        
                        <!-- Username field -->
                        <v-text-field v-model="username" variant="outlined" label="Username" ref="usernameInput"
                                :readonly="loading" :rules="usernameRules" class="mb-2" clearable density="compact"
                                prepend-icon="mdi-account-tie" autocomplete="username">
                            </v-text-field>
                            <!-- Username field -->
                            
                            <!-- Password recovery -->
                            <div class="text-subtitle-1 text-medium-emphasis d-flex align-end justify-space-between">
                                <span></span>
                                
                                <v-btn variant="plain" size="x-small" @click="passwordRecoverDialog = true"
                                class="text-cyan-darken-1 font-weight-bold" prepend-icon="mdi-restore">
                                    Forgot password?
                                </v-btn>
                            </div>
                            <!-- Password recovery -->
                            
                            <!-- Password field -->
                            <v-text-field v-model="password" variant="outlined" label="Password" ref="passwordInput"
                                :readonly="loading" :rules="passwordRules" density="compact"
                                :type="passwordVisible ? 'text' : 'password'" prepend-icon="mdi-key"
                                :append-inner-icon="passwordVisible ? 'mdi-eye' : ' mdi-eye-off'"
                                @click:append-inner="passwordVisible = !passwordVisible" autocomplete="current-password">
                            </v-text-field>
                            <!-- Password field -->
                            
                            <!-- Button login -->
                            <span>
                                <v-tooltip v-if="!form" activator="parent" location="top" no-overflow>
                                    Fill required fields
                                </v-tooltip>
                                <span>
                                    <v-btn :disabled="!form" :loading="loading" block class="mt-10"
                                    :class="form ? 'bg-green-darken-1' : ''" size="large" type="submit"
                                    append-icon="mdi-login" v-autofocus>
                                    Login
                                </v-btn>
                            </span>
                            </span>
                            <!-- Button login -->
                            
                        </v-form>
                    </v-card>

                </v-row>
                <!-- Form -->

            </v-container>
            <!-- Mobile -->
            
            
            
            
            
            
            <!-- Desktop -->
            <v-container fill-height fluid v-else>

                <v-row align="center" justify="center">

                    <!-- Left column -->
                    <v-col align="center">

                        <v-row>
                            <v-col cols="12" style="text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.8);">
                                <v-icon icon="mdi-truck-fast" class="text-h1" />
                            </v-col>

                            <v-col class="text-h2 pa-4" style="text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);">
                                <span class="fw-bold">F</span>ood
                                <span class="fw-bold">D</span>elivery
                                <span class="fw-bold">F</span>leet
                                <span class="fw-bold">M</span>anagement
                                <span class="fw-bold">S</span>ystem

                            </v-col>
                        </v-row>

                    </v-col>
                    <!-- Left column -->

                    <!-- Right column -->
                    <v-col style="height: 99dvh">

                        <v-row align="center" justify="center" style="min-height: 100dvh;">

                            <v-col>
                                <v-card class="bg-blue-grey-darken-3 rounded-xl pa-16 mx-16 elevation-20">

                                    <v-form v-model="form" @submit.prevent="onSubmit" class="text-h4"
                                        style="text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);">

                                        <!-- Username field -->
                                        <v-text-field v-model="username" variant="outlined" label="Username"
                                            ref="usernameInput" :readonly="loading" :rules="usernameRules" class="mb-2"
                                            clearable density="compact" prepend-icon="mdi-account-tie"
                                            autocomplete="username">
                                        </v-text-field>
                                        <!-- Username field -->

                                        <!-- Password recovery -->
                                        <div
                                            class="text-subtitle-1 text-medium-emphasis d-flex align-end justify-space-between">
                                            <span></span>

                                            <v-btn variant="plain" size="x-small" @click="passwordRecoverDialog = true"
                                                class="text-cyan-darken-1 font-weight-bold" prepend-icon="mdi-restore">
                                                Forgot password?
                                            </v-btn>
                                        </div>
                                        <!-- Password recovery -->

                                        <!-- Password field -->
                                        <v-text-field v-model="password" variant="outlined" label="Password"
                                            ref="passwordInput" :readonly="loading" :rules="passwordRules" density="compact"
                                            :type="passwordVisible ? 'text' : 'password'" prepend-icon="mdi-key"
                                            :append-inner-icon="passwordVisible ? 'mdi-eye' : ' mdi-eye-off'"
                                            @click:append-inner="passwordVisible = !passwordVisible"
                                            autocomplete="current-password">
                                        </v-text-field>
                                        <!-- Password field -->

                                        <!-- Button login -->
                                        <span>
                                            <v-tooltip v-if="!form" activator="parent" location="top" no-overflow>
                                                Fill required fields
                                            </v-tooltip>
                                            <span>
                                                <v-btn :disabled="!form" :loading="loading" block class="mt-10"
                                                    :class="form ? 'bg-green-darken-1' : ''" size="large" type="submit"
                                                    append-icon="mdi-login" v-autofocus>
                                                    Login
                                                </v-btn>
                                            </span>
                                        </span>
                                        <!-- Button login -->

                                    </v-form>

                                </v-card>
                            </v-col>
                        </v-row>


                    </v-col>
                    <!-- Right column -->

                </v-row>
            </v-container>
            <!-- Desktop -->


        </div>

        <!-- Alert -->
        <v-snackbar v-model="alert" :timeout="3000" location="top" color="danger">
            <span class="text-white">{{ errorContent }}</span>
            <template v-slot:actions>
                <v-btn variant="tonal" @click="alert = false">
                    Close
                </v-btn>
            </template>
        </v-snackbar>
        <!-- Alert -->

        <!-- Password recovery -->
        <v-dialog v-model="passwordRecoverDialog" width="400">
            <v-card>
                <v-card-text>
                    <p>Type your email below</p>
                    <v-text-field v-model="emailPasswordRecover" density="compact" hide-details="auto" label="Email address"
                        placeholder="example@example.com" type="email" class="mb-3" prepend-icon="mdi-email">
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


    </v-app>
</template>


<script>
import axios from 'axios';

export default {
    data: () => ({
        form: false,
        username: null,
        password: null,
        passwordVisible: false,
        loading: false,
        atempt: 0,


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
        const rememberedUsername = localStorage.getItem('username')
        const rememberedPassword = localStorage.getItem('password')

        if (rememberedUsername && rememberedPassword) {
            this.$refs.usernameInput.value = rememberedUsername;
            this.$refs.passwordInput.value = rememberedPassword;

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
                }
                else {
                    // Authentication was successfull

                    // Vuex
                    this.$store.dispatch('setuserData', response.data.data);

                    this.$store.commit('setAccessToken', response.data.jwt.access);
                    this.$store.commit('setRefreshToken', response.data.jwt.refresh);

                    axios.defaults.headers.common['Authorization'] = `JWT ${response.data.jwt.access}`;

                    this.$router.push('/dashboard');

                }
            }
            catch (error) {
                if (error.message === "Network Error") {
                    this.errorContent = "Server Error. Please try again.";
                    this.alert = true;
                }
                else {
                    this.errorContent = "Error. Please try again.";
                    this.alert = true;
                }
            }

            this.loading = false;
        },


    },

}
</script>