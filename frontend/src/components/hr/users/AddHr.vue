<template>
    <div>
        <div class="containter m-2 p-2 d-flex justify-content-center">

            <div class="col-12 col-md-9">
                <p class="fs-4">Add new HR user</p>
                <form action="" method="post" class="border rounded-3 p-3" @submit.prevent="createUser">

                    <div class="input-group mb-3">
                        <span class="input-group-text" id="first_name">First name</span>
                        <input type="text" class="form-control" placeholder="First name" aria-label="first_name"
                            aria-describedby="first_name" v-model="firstName" @input="updateUsername"
                            :class="{ 'border border-danger': dataError && dataError['first_name'] }">
                    </div>

                    <div class="input-group mb-3">
                        <span class="input-group-text" id="last_name">Last name</span>
                        <input type="text" class="form-control" placeholder="Last name" aria-label="last_name"
                            aria-describedby="last_name" v-model="lastName" @input="updateUsername"
                            :class="{ 'border border-danger': dataError && dataError['last_name'] }">
                    </div>


                    <div class="input-group mb-3">
                        <span class="input-group-text" id="email">Email</span>
                        <input type="email" class="form-control" placeholder="Email" aria-label="email"
                            aria-describedby="email" v-model="email"
                            :class="{ 'border border-danger': dataError && dataError['email'] }">
                    </div>

                    <div class="input-group mb-3">
                        <span class="input-group-text" id="phone">Phone number</span>
                        <input type="text" class="form-control" placeholder="Phone number" aria-label="phone"
                            aria-describedby="phone" v-model="phone"
                            :class="{ 'border border-danger': dataError && dataError['phone'] }">
                    </div>

                    <div class="input-group mb-3">
                        <span class="input-group-text" id="test_field">test_field</span>
                        <input type="number" class="form-control" placeholder="test_field" aria-label="test_field"
                            aria-describedby="test_field" v-model="test_field"
                            :class="{ 'border border-danger': dataError && dataError['test_field'] }">
                    </div>

                    <!-- Password -->
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="password">Password</span>
                        <input type="password" class="form-control" placeholder="Password" aria-label="password"
                            aria-describedby="password" v-model="password"
                            :class="{ 'border border-danger': dataError && dataError['password'] }">
                    </div>

                    <div class="input-group mb-3">
                        <span class="input-group-text" id="password2">Repeat password</span>
                        <input type="password" class="form-control" placeholder="Password" aria-label="password2"
                            aria-describedby="password2" v-model="password2"
                            :class="{ 'border border-danger': dataError && dataError['password'] || dataError && dataError['password2'] }">
                    </div>
                    <!-- Password -->

                    <div class="input-group mb-3">
                        <span class="input-group-text" id="username">Username</span>
                        <input type="text" class="form-control" placeholder="Username" aria-label="Username"
                            aria-describedby="username" v-model="username" disabled
                            :class="{ 'border border-danger': dataError && dataError['username'] }">
                    </div>

                    <div class="text-center">
                        <button type="button" class="btn btn-success shadow" @click="createUser" :disabled="!isFormValid"
                            :class="{ 'btn-outline-danger': !isFormValid }">
                            <span class="d-flex align-items-center">
                                Create
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                                    class="bi bi-person-add ms-2" viewBox="0 0 16 16">
                                    <path
                                        d="M12.5 16a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Zm.5-5v1h1a.5.5 0 0 1 0 1h-1v1a.5.5 0 0 1-1 0v-1h-1a.5.5 0 0 1 0-1h1v-1a.5.5 0 0 1 1 0Zm-2-6a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM8 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4Z" />
                                    <path
                                        d="M8.256 14a4.474 4.474 0 0 1-.229-1.004H3c.001-.246.154-.986.832-1.664C4.484 10.68 5.711 10 8 10c.26 0 .507.009.74.025.226-.341.496-.65.804-.918C9.077 9.038 8.564 9 8 9c-5 0-6 3-6 4s1 1 1 1h5.256Z" />
                                </svg>
                            </span>
                        </button>
                    </div>
                </form>
            </div>
        </div>

        <!-- Message modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#ErrorModal" id="hiddenButton"
            style="display: none;">
        </button>
        <div class="modal fade" id="ErrorModal" tabindex="-1" aria-labelledby="ErrorModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <!-- Error -->
                    <div v-if="dataError" class="modal-header d-flex justify-content-between">
                        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="red"
                            class="bi bi-exclamation-triangle" viewBox="0 0 16 16">
                            <path
                                d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
                            <path
                                d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
                        </svg>
                        <h1 class="modal-title fs-5 text-danger" id="confirmModalLabel">
                            Error
                        </h1>
                        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="red"
                            class="bi bi-exclamation-triangle" viewBox="0 0 16 16">
                            <path
                                d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
                            <path
                                d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
                        </svg>
                    </div>
                    <!-- Error -->

                    <!-- Success -->
                    <div v-else class="modal-header">
                        <h1 class="modal-title fs-5" id="ErrorModalLabel">
                            <p>Success!</p>
                        </h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <!-- Success -->

                    <div class="modal-body text-center text-danger">
                        <div v-for="(messages, field) in dataError" :key="field">
                            <p v-for="message in messages" :key="message">{{ field }} - {{ message }}</p>
                        </div>

                        <div v-if="dataCorrect">
                            <p class="text-success">
                                Succesfully created {{ dataCorrect.username }} account
                            </p>
                        </div>


                    </div>
                    <div class="modal-footer d-flex justify-content-center">
                        <button type="button" class="btn btn-secondary fs-5 w-25" data-bs-dismiss="modal">
                            Ok
                        </button>
                    </div>

                </div>
            </div>
        </div>
        <!-- Message modal -->

    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            firstName: '',
            lastName: '',
            username: '',
            email: '',
            phone: '',
            test_field: '',
            password: '',
            password2: '',
            fetched_data: {},
            dataError: null,
            dataCorrect: null,
        };
    },

    computed: {
        isFormValid() {
            return (
                this.firstName &&
                this.lastName &&
                this.email &&
                this.phone &&
                this.test_field &&
                this.password &&
                this.password2
            );
        },
    },

    methods: {
        generateRandomDigits() {
            return Math.floor(100 + Math.random() * 900);
        },
        updateUsername() {
            const firstThreeChars = this.firstName.slice(0, 3).toLowerCase();
            const lastThreeChars = this.lastName.slice(0, 3).toLowerCase();
            const randomDigits = this.generateRandomDigits();
            this.username = firstThreeChars + lastThreeChars + randomDigits;
        },
        async createUser() {
            const fetched_data = {
                first_name: this.firstName,
                last_name: this.lastName,
                email: this.email,
                // phone : this.phone,
                test_field: this.test_field,
                username: this.username,
                password: this.password,
                password2: this.password2,
                user_role: 'HR',
            }
            console.log(fetched_data)

            this.dataError = ''
            const response = await axios.post('api/create/', fetched_data);


            if (response.data.message) {
                this.dataCorrect = response.data;
                document.getElementById('hiddenButton').click();
                console.log('success!', response.data);
                this.resetForm();
            }
            else {
                this.dataError = response.data;
                document.getElementById('hiddenButton').click();
                console.error(response.data);
            }

        },
        resetForm() {
            this.firstName = '';
            this.lastName = '';
            this.email = '';
            this.test_field = '';
            this.username = '';
            this.password = '';
            this.password2 = '';
        },
    }
};
</script>