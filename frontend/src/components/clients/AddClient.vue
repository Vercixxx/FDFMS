<template>
    <div>
        <div class="containter m-2 p-2 d-flex justify-content-center">
            <div class="col-12 col-md-9">

                <p v-if="res_name === null" class="fs-4 text-center fw-bolder">Add new Restaurant</p>
                <div v-else class="d-flex justify-content-between">
                    <div>
                        <button type="button" class="btn btn-outline-primary mb-3 " @click="goBack">
                            <span class="d-flex align-items-center">
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                                    class="bi bi-arrow-left me-2 " viewBox="0 0 16 16">
                                    <path fill-rule="evenodd"
                                        d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z" />

                                </svg>
                                Back
                            </span>
                        </button>
                    </div>
                    <div class="fs-4 text-center fw-bolder">Edit Restaurant</div>
                    <div></div>

                </div>

                <form action="" method="post" class="border rounded-3 p-3" @submit.prevent="createUser">


                    <!-- Basic information -->
                    <div class="border border-2 p-2 text-center mb-5 mt-2 fw-bolder shadow">
                        Basic information
                    </div>

                    <!-- First name -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Restaurant name
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="name"
                                aria-describedby="name" v-model="name"
                                :class="{ 'border border-danger': dataError && dataError['name'] }">
                        </div>
                    </div>
                    <!-- First name -->


                    <!-- Phone number -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Phone number
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="phone" class="form-control rounded-0 rounded-end" aria-label="phone"
                                aria-describedby="phone" v-model="phone"
                                :class="{ 'border border-danger': dataError && dataError['phone'] }">
                        </div>
                    </div>
                    <!-- Phone number -->


                    <!-- Location  -->
                    <div class="border border-2 p-2 text-center my-5 fw-bolder shadow">
                        Location
                    </div>


                    <!-- Residence address Country -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Country
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="country"
                                aria-describedby="country" v-model="country"
                                :class="{ 'border border-danger': dataError && dataError['country'] }">
                        </div>
                    </div>
                    <!-- Residence address Country -->


                    <!-- Residence address City -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            City
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="city"
                                aria-describedby="city" v-model="city"
                                :class="{ 'border border-danger': dataError && dataError['city'] }">
                        </div>
                    </div>
                    <!-- Residence address City -->


                    <!-- Residence address State -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            State
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="state"
                                aria-describedby="state" v-model="state"
                                :class="{ 'border border-danger': dataError && dataError['state'] }">
                        </div>
                    </div>
                    <!-- Residence address State -->


                    <!-- Residence address Street -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Street
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="street"
                                aria-describedby="street" v-model="street"
                                :class="{ 'border border-danger': dataError && dataError['street'] }">
                        </div>
                    </div>
                    <!-- Residence address Street -->


                    <div class="input-group mb-3 gx-0">

                        <!-- Residence address Home number -->
                        <div class="input-group">
                            <div
                                class="col-2 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                Home
                            </div>
                            <div class="col-4 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end me-2"
                                    aria-label="home_number" aria-describedby="home_number" v-model="home_number"
                                    :class="{ 'border border-danger': dataError && dataError['home_number'] }">
                            </div>
                            <!-- Residence address Home number -->


                            <!-- Residence address Apartament number -->
                            <div
                                class="col-2 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                Apartament
                            </div>
                            <div class="col-4 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end"
                                    aria-label="apartament_number" aria-describedby="apartament_number"
                                    v-model="apartament_number"
                                    :class="{ 'border border-danger': dataError && dataError['apartament_number'] }">
                            </div>
                            <!-- Residence address Apartament number -->
                        </div>

                    </div>


                    <!-- Residence Zip code -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Zip code
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="zip_code"
                                aria-describedby="zip_code" v-model="zip_code"
                                :class="{ 'border border-danger': dataError && dataError['zip_code'] }">
                        </div>
                    </div>
                    <!-- Residence Zip code -->


                    <!-- Managers  -->
                    <div class="border border-2 p-2 text-center my-5 fw-bolder shadow">
                        Managers
                    </div>



                    <!-- Managers -->
                    <div class="d-flex justify-content-center text-center mb-5 gap-5">

                        <!-- Avalible managers -->
                        <div class="col-5">
                            <div class="border rounded border-2 p-2" style="height: 40vh; overflow-y: auto;">
                                <p class="fw-bolder fs5">Available managers</p>
                                <hr>
                                <!-- search bar -->
                                <form role="search" method="POST" action="" @submit.prevent="search"
                                    class="d-flex justify-content-center mb-4">

                                    <div class="input-group w-75">

                                        <input class="form-control border-success" type="search"
                                            placeholder="Search managers" aria-label="Search" v-model="query" @keyup.enter="getAllUsernames">

                                    </div>
                                </form>
                                <!-- search bar -->


                                <!-- Users list -->
                                <button v-for="username in managersUsernames" :key="username.username" type="button"
                                    class="btn btn-outline-secondary w-75 mb-2" @click="toggleUser(username)"
                                    :class="{ 'btn-secondary text-white': isSelected(username) }">
                                    {{ username.username }}
                                </button>
                                <!-- Users list -->


                            </div>
                        </div>
                        <!-- Avalible managers -->

                        <!-- Choosen managers -->
                        <div class="col-5">
                            <div class="border border-success border-2 rounded p-2" style="height: 40vh; overflow-y: auto;">
                                <p class="fw-bolder fs5">Choosen managers</p>
                                <hr>
      

                                <!-- Users list -->
                                <button v-for="username in choosenUsernames" :key="username.username" type="button"
                                    class="btn btn-success w-75 mb-2" @click="toggleUser(username)"
                                    :class="{ '': isSelected(username) }">
                                    {{ username.username }}
                                </button>
                                <!-- Users list -->



                            </div>
                        </div>
                        <!-- Choosen managers -->


                    </div>
                    <!-- Managers -->



                    <div class="text-center">
                        <button v-if="res_name === null" type="button" class="btn btn-success shadow" @click="test"
                            :disabled="!isFormValid" :class="{ 'btn-outline-danger': !isFormValid }">
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


                        <!-- Button when editing existing user -->
                        <button v-else type="button" class="btn btn-success shadow" @click="updateUser">
                            <span class="d-flex align-items-center">
                                Save
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                                    class="bi bi-floppy ms-2" viewBox="0 0 16 16">
                                    <path d="M11 2H9v3h2V2Z" />
                                    <path
                                        d="M1.5 0h11.586a1.5 1.5 0 0 1 1.06.44l1.415 1.414A1.5 1.5 0 0 1 16 2.914V14.5a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 0 14.5v-13A1.5 1.5 0 0 1 1.5 0ZM1 1.5v13a.5.5 0 0 0 .5.5H2v-4.5A1.5 1.5 0 0 1 3.5 9h9a1.5 1.5 0 0 1 1.5 1.5V15h.5a.5.5 0 0 0 .5-.5V2.914a.5.5 0 0 0-.146-.353l-1.415-1.415A.5.5 0 0 0 13.086 1H13v4.5A1.5 1.5 0 0 1 11.5 7h-7A1.5 1.5 0 0 1 3 5.5V1H1.5a.5.5 0 0 0-.5.5Zm3 4a.5.5 0 0 0 .5.5h7a.5.5 0 0 0 .5-.5V1H4v4.5ZM3 15h10v-4.5a.5.5 0 0 0-.5-.5h-9a.5.5 0 0 0-.5.5V15Z" />
                                </svg>
                            </span>
                        </button>
                        <!-- Button when editing existing user -->
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
            managersUsernames: [],
            choosenUsernames: [],

            res_name: null,
            query: '',

            isFormValid: true,

            name: '',
            phone: '',
            country: '',
            city: '',
            state: '',
            street: '',
            home_number: '',
            apartament_number: '',
            zip_code: '',

            dataCorrect: '',
            dataError: '',

        }
    },


    mounted() {
        this.getAllUsernames()
    },

    methods: {
        async getAllUsernames() {
            const response = await axios.get('api/managers/get_username_all/', {
                params: {
                    search: this.query,
                }
            });

            this.managersUsernames = response.data
            console.log(response)

        },
        toggleUser(user) {
            if (this.isSelected(user)) {
                this.choosenUsernames = this.choosenUsernames.filter(u => u !== user);
            } else {
                this.choosenUsernames.push(user);
            }
        },
        isSelected(user) {
            return this.choosenUsernames.includes(user);
        },

        test() {
            console.log(this.choosenUsernames)
        },


    },

}
</script>
