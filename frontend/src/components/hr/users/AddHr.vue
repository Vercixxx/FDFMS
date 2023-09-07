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
                        <button type="button" class="btn btn-success" @click="createUser"
                            :disabled="!isFormValid">Create</button>
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
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="ErrorModalLabel">
                            <p v-if="dataError">Error</p>
                            <p v-else>Success</p>
                        </h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
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

            const response = await axios.post('add-user/', fetched_data);


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