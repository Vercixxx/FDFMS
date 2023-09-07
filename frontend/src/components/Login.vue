<template>
    <div class="rounded p-2 m-2 bg-success">

        <!-- Title -->
        <p class="display-5 fst-italic mb-4 px-2">FDFMS - Log in</p>

    </div>

    <div class="p-2 row d-flex justify-content-center align-items-start min-vh-50" style="margin-top: 5%;">
        <div class="col-12 col-md-4">

            <form action="" method="POST" class="mx-auto w-100 mb-4 p-2 text-center " @submit.prevent="login">





                <!-- Username section -->
                <div class="row mb-5">
                    <!-- SVG image of user -->
                    <div class="col-2 d-flex justify-content-end align-items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor"
                            class="bi bi-person" viewBox="0 0 16 16">
                            <path
                                d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4Zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10Z" />
                        </svg>
                    </div>
                    <!-- Input form for username -->
                    <div class="col-10 form-floating d-flex justify-content-center align-items-center">
                        <input type="text" class="form-control" name="username" id="username" ref="usernameInput"
                            placeholder="username" v-model="formData.username" :minlength="4"
                            :class="{ 'border border-danger': dataError }" required />
                        <label for="username" class="text-center">Username</label>
                    </div>
                </div>


                <!-- Password section -->
                <div class="row mb-2">
                    <!-- SVG image of key -->
                    <div class="col-2 d-flex justify-content-end align-items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-key"
                            viewBox="0 0 16 16">
                            <path
                                d="M0 8a4 4 0 0 1 7.465-2H14a.5.5 0 0 1 .354.146l1.5 1.5a.5.5 0 0 1 0 .708l-1.5 1.5a.5.5 0 0 1-.708 0L13 9.207l-.646.647a.5.5 0 0 1-.708 0L11 9.207l-.646.647a.5.5 0 0 1-.708 0L9 9.207l-.646.647A.5.5 0 0 1 8 10h-.535A4 4 0 0 1 0 8zm4-3a3 3 0 1 0 2.712 4.285A.5.5 0 0 1 7.163 9h.63l.853-.854a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .708 0l.646.647.793-.793-1-1h-6.63a.5.5 0 0 1-.451-.285A3 3 0 0 0 4 5z" />
                            <path d="M4 8a1 1 0 1 1-2 0 1 1 0 0 1 2 0z" />
                        </svg>
                    </div>

                    <!-- Input form for password -->
                    <div class="col-10 form-floating d-flex justify-content-center align-items-center">
                        <input type="password" class="form-control" name="password" id="password" placeholder="********"
                            ref="passwordInput" v-model="formData.password" :minlength="4" required />
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                            @click="togglePasswordVisibility"
                            style="cursor: pointer; position: absolute; right: 6%; top: 50%; transform: translateY(-50%);">
                            <template v-if="showPassword">
                                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor"
                                    class="bi bi-eye" viewBox="0 0 16 16">
                                    <path
                                        d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z" />
                                    <path
                                        d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z" />
                                </svg>
                            </template>
                            <template v-else>
                                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor"
                                    class="bi bi-eye-slash" viewBox="0 0 16 16">
                                    <path
                                        d="M13.359 11.238C15.06 9.72 16 8 16 8s-3-5.5-8-5.5a7.028 7.028 0 0 0-2.79.588l.77.771A5.944 5.944 0 0 1 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.134 13.134 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755-.165.165-.337.328-.517.486l.708.709z" />
                                    <path
                                        d="M11.297 9.176a3.5 3.5 0 0 0-4.474-4.474l.823.823a2.5 2.5 0 0 1 2.829 2.829l.822.822zm-2.943 1.299.822.822a3.5 3.5 0 0 1-4.474-4.474l.823.823a2.5 2.5 0 0 0 2.829 2.829z" />
                                    <path
                                        d="M3.35 5.47c-.18.16-.353.322-.518.487A13.134 13.134 0 0 0 1.172 8l.195.288c.335.48.83 1.12 1.465 1.755C4.121 11.332 5.881 12.5 8 12.5c.716 0 1.39-.133 2.02-.36l.77.772A7.029 7.029 0 0 1 8 13.5C3 13.5 0 8 0 8s.939-1.721 2.641-3.238l.708.709zm10.296 8.884-12-12 .708-.708 12 12-.708.708z" />
                                </svg>
                            </template>
                        </svg>


                        <label for="password" class="text-center">
                            Password
                        </label>

                        <div>

                        </div>

                    </div>
                </div>

                <div class="row">
                    <div class="col-2">

                    </div>
                    <div class="col-10 d-flex justify-content-between">
                        <div>
                            <div class="mb-3 form-check">
                                <input type="checkbox" class="form-check-input" id="remember_me_checkbox">
                                <label class="form-check-label" for="remember_me_checkbox">Remember me</label>
                            </div>
                        </div>

                        <div class="form-text" id="basic-addon4">
                            <p><a href="#" class="link-danger link-offset-2 text-decoration-none">
                                    Forgot password
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                        class="bi bi-arrow-counterclockwise" viewBox="0 0 16 16">
                                        <path fill-rule="evenodd"
                                            d="M8 3a5 5 0 1 1-4.546 2.914.5.5 0 0 0-.908-.417A6 6 0 1 0 8 2v1z" />
                                        <path
                                            d="M8 4.466V.534a.25.25 0 0 0-.41-.192L5.23 2.308a.25.25 0 0 0 0 .384l2.36 1.966A.25.25 0 0 0 8 4.466z" />
                                    </svg>
                                </a></p>

                        </div>
                    </div>

                </div>

                <!-- Buuttons section -->
                <div class="d-flex mt-5 flex-column align-items-center justify-content-center">

                    <button class="btn btn-success btn-lg" @click="login" :disabled="!isFormValid || isButtonDisabled">
                        Log in
                        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor"
                            class="bi bi-box-arrow-in-right" viewBox="0 0 16 16">
                            <path fill-rule="evenodd"
                                d="M6 3.5a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-2a.5.5 0 0 0-1 0v2A1.5 1.5 0 0 0 6.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-8A1.5 1.5 0 0 0 5 3.5v2a.5.5 0 0 0 1 0v-2z" />
                            <path fill-rule="evenodd"
                                d="M11.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H1.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z" />
                        </svg>
                    </button>

                </div>
                <!-- Buuttons section -->

            </form>

        </div>

        <!-- modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#ErrorModal" id="hiddenButton"
            style="display: none;">
            
        </button>

        <div class="modal fade" id="ErrorModal" tabindex="-1" aria-labelledby="ErrorModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="ErrorModalLabel">Error</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body text-center text-danger fs-4">
                        {{ dataError }}
                    </div>

                </div>
            </div>
        </div>
        <!-- modal -->



    </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
    name: 'Login',

    created() {
        this.isButtonDisabled = false;
    },

    mounted() {
        const cookie_username = Cookies.get('username');
        const cookie_password = Cookies.get('password');
        
        if (cookie_username && cookie_password) {
            this.isButtonDisabled = false;
 
            this.$refs.usernameInput.value = cookie_username;
            this.$refs.passwordInput.value = cookie_password;

            this.$refs.usernameInput.dispatchEvent(new Event('input'));
            this.$refs.passwordInput.dispatchEvent(new Event('input'));
        }
    },
    data() {
        return {
            showPassword: false,
            formData: {
                username: '',
                password: '',
            },
            dataError: null,
            isButtonDisabled: false,
            errorContent: '', // Treść błędu do wyświetlenia w modalu
        };
    },
    computed: {
        isFormValid() {
            return this.formData.username.length >= 4 && this.formData.password.length >= 1;
        },
    },
    methods: {
        togglePasswordVisibility() {
            this.showPassword = !this.showPassword;
            const input = this.$refs.passwordInput;
            if (this.showPassword) {
                input.type = 'text';
            } else {
                input.type = 'password';
            }
        },
        async login() {
            if (this.isFormValid) {
                this.isButtonDisabled = true;

                const username = this.$refs.usernameInput.value;
                const password = this.$refs.passwordInput.value;

                const data = {
                    username: username,
                    password: password,

                };

                const response = await axios.post('log-in/', data, { timeout: 5000 })


                if (response.data.error) {
                    this.isButtonDisabled = false; // Włącz przycisk po otrzymaniu odpowiedzi lub błędzie
                    this.dataError = response.data.error;

                    // modal
                    this.errorContent = response.data.error;
                    document.getElementById('hiddenButton').click();
                }
                else {
                    // Authentication was successfull
                    const token = response.data.token;
                    Cookies.set('token', token, { expires: 7 });
                    localStorage.setItem('user_role', response.data.user_role)

                    // check if remeber_me is checked
                    const checkbox = document.getElementById("remember_me_checkbox");
                    if (checkbox.checked) {
                        Cookies.set('username', username, { expires: new Date('9999-12-31') });
                        Cookies.set('password', password, { expires: new Date('9999-12-31') });

                    }
                    await this.$router.push('/hr');
                }
            }
        },


    },
};
</script>