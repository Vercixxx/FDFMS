<template>
    <div>
        <div class="containter m-2 p-2 d-flex justify-content-center">
            <div class="col-12 col-md-9">
                <p class="fs-4 text-center">Add new HR user</p>
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
                        <input type="phone" class="form-control" placeholder="Phone number" aria-label="phone"
                            aria-describedby="phone" v-model="phone"
                            :class="{ 'border border-danger': dataError && dataError['phone'] }">
                    </div>
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="identity">PESEL / NIP</span>
                        <input type="text" class="form-control" placeholder="PESEL / NIP" aria-label="identity"
                            aria-describedby="identity" v-model="identity"
                            :class="{ 'border border-danger': dataError && dataError['identity'] }">
                    </div>


                    <!-- Dane rozliczeniowe i zdrowotne -->
                    <div class="border border-2 p-2 text-center my-5 fw-bolder shadow">
                        Tax and health information
                    </div>

                    <div class="input-group mb-3">
                        <span class="input-group-text" id="tax_name">Tax office name</span>
                        <input type="text" class="form-control" placeholder="Tax office name" aria-label="tax_name"
                            aria-describedby="tax_name" v-model="taxName"
                            :class="{ 'border border-danger': dataError && dataError['taxName'] }">
                    </div>
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="tax_address">Tax office address</span>
                        <input type="text" class="form-control" placeholder="Tax office address" aria-label="tax_address"
                            aria-describedby="tax_address" v-model="tax_address"
                            :class="{ 'border border-danger': dataError && dataError['tax_address'] }">
                    </div>
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="nfz">NFZ branch</span>
                        <input type="text" class="form-control" placeholder="NFZ branch" aria-label="nfz"
                            aria-describedby="nfz" v-model="nfz"
                            :class="{ 'border border-danger': dataError && dataError['nfz'] }">
                    </div>
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="bank_account">Bank Account Number</span>
                        <input type="text" class="form-control" placeholder="Bank Account Number" aria-label="bank_account"
                            aria-describedby="bank_account" v-model="bankAccount"
                            :class="{ 'border border-danger': dataError && dataError['bankAccount'] }">
                    </div>


                    <div class="border border-2 p-2 text-center my-5 fw-bolder shadow">
                        Residence address
                    </div>

                    <div class="input-group mb-3">
                        <span class="input-group-text" id="res_country">Country</span>
                        <input type="text" class="form-control" placeholder="Country" aria-label="res_country"
                            aria-describedby="res_country" v-model="resCountry"
                            :class="{ 'border border-danger': dataError && dataError['resCountry'] }">
                    </div>

                    <div class="input-group mb-3">
                        <span class="input-group-text" id="res_city">City</span>
                        <input type="text" class="form-control" placeholder="City" aria-label="res_city"
                            aria-describedby="res_city" v-model="resCity"
                            :class="{ 'border border-danger': dataError && dataError['resCity'] }">
                    </div>

                    <div class="input-group mb-3">
                        <span class="input-group-text" id="res_state">State</span>
                        <input type="text" class="form-control" placeholder="State" aria-label="res_state"
                            aria-describedby="res_state" v-model="resState"
                            :class="{ 'border border-danger': dataError && dataError['resState'] }">
                    </div>

                    <div class="input-group mb-3">
                        <span class="input-group-text" id="res_street">Street</span>
                        <input type="text" class="form-control" placeholder="Street" aria-label="res_street"
                            aria-describedby="res_street" v-model="resStreet"
                            :class="{ 'border border-danger': dataError && dataError['resStreet'] }">
                    </div>

                    <div class="input-group mb-3 row gx-0">
                        <div class="d-flex col-6">
                            <span class="input-group-text rounded-0 rounded-start" id="res_homeNumber">Home</span>
                            <input type="text" class="form-control rounded-0 rounded-end me-2" placeholder="Home number"
                                aria-label="res_homeNumber" aria-describedby="res_homeNumber" v-model="resHomeNumber"
                                :class="{ 'border border-danger': dataError && dataError['resHomeNumber'] }">
                        </div>

                        <div class="d-flex col-6">
                            <span class="input-group-text rounded-0 rounded-start"
                                id="res_apartamentNumber">Apartament</span>
                            <input type="text" class="form-control rounded-0 rounded-end" placeholder="Apartament number"
                                aria-label="res_apartamentNumber" aria-describedby="res_apartamentNumber"
                                v-model="resApartamentNumber"
                                :class="{ 'border border-danger': dataError && dataError['resApartamentNumber'] }">

                        </div>
                    </div>

                    <div class="input-group mb-3">
                        <span class="input-group-text" id="res_zipCode">Zip code</span>
                        <input type="text" class="form-control" placeholder="Zip code" aria-label="res_zipCode"
                            aria-describedby="res_zipCode" v-model="resZipCode"
                            :class="{ 'border border-danger': dataError && dataError['resZipCode'] }">
                    </div>

                    <div>
                        <div class="form-check form-switch">
                            <input class="form-check-input toggleSwitch" type="checkbox" v-model="show_corespondece_form">
                            <div class="fs-6 ms-2 fw-semibold mx-auto p-2">
                                Correspodence address same as residence address
                            </div>
                            <div class="slider" :class="{ active: show_corespondece_form }"></div>
                        </div>
                    </div>

                    <!-- Registered address form -->
                    <div :style="{ display: show_corespondece_form ? 'none' : 'block' }">
                        <div class="border border-2 p-2 text-center my-5 fw-bolder shadow">
                            Addres for correspodence
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="cor_country">Country</span>
                            <input type="text" class="form-control" placeholder="Country" aria-label="cor_country"
                                aria-describedby="cor_country" v-model="corCountry"
                                :class="{ 'border border-danger': dataError && dataError['corCountry'] }">
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="cor_city">City</span>
                            <input type="text" class="form-control" placeholder="City" aria-label="cor_city"
                                aria-describedby="cor_city" v-model="corCity"
                                :class="{ 'border border-danger': dataError && dataError['corCity'] }">
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="cor_state">State</span>
                            <input type="text" class="form-control" placeholder="State" aria-label="cor_state"
                                aria-describedby="cor_state" v-model="corState"
                                :class="{ 'border border-danger': dataError && dataError['corState'] }">
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="cor_street">Street</span>
                            <input type="text" class="form-control" placeholder="Street" aria-label="cor_street"
                                aria-describedby="cor_street" v-model="corStreet"
                                :class="{ 'border border-danger': dataError && dataError['corStreet'] }">
                        </div>

                        <div class="input-group mb-3 row gx-0">
                            <div class="d-flex col-6">
                                <span class="input-group-text rounded-0 rounded-start" id="cor_homeNumber">Home</span>
                                <input type="text" class="form-control rounded-0 rounded-end me-2" placeholder="Home number"
                                    aria-label="cor_homeNumber" aria-describedby="cor_homeNumber" v-model="corHomeNumber"
                                    :class="{ 'border border-danger': dataError && dataError['corHomeNumber'] }">
                            </div>

                            <div class="d-flex col-6">
                                <span class="input-group-text rounded-0 rounded-start"
                                    id="cor_apartamentNumber">Apartament</span>
                                <input type="text" class="form-control rounded-0 rounded-end"
                                    placeholder="Apartament number" aria-label="cor_apartamentNumber"
                                    aria-describedby="cor_apartamentNumber" v-model="corApartamentNumber"
                                    :class="{ 'border border-danger': dataError && dataError['corApartamentNumber'] }">

                            </div>
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="cor_zipCode">Zip code</span>
                            <input type="text" class="form-control" placeholder="Zip code" aria-label="cor_zipCode"
                                aria-describedby="cor_zipCode" v-model="corZipCode"
                                :class="{ 'border border-danger': dataError && dataError['corZipCode'] }">
                        </div>
                    </div>

                    <!-- Registered address form -->
                    <div>
                        <div class="form-check form-switch">
                            <input class="form-check-input toggleSwitch" type="checkbox" v-model="show_registered_form">
                            <div class="fs-6 ms-2 text-wrap fw-semibold mx-auto p-2">
                                Registered address same as residence address
                            </div>
                            <div class="slider" :class="{ active: show_registered_form }"></div>
                        </div>
                    </div>
                    <!-- Registered address form -->
                    <div :style="{ display: show_registered_form ? 'none' : 'block' }">
                        <div class="border border-2 p-2 text-center my-5 fw-bolder shadow">
                            Registered address
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="reg_country">Country</span>
                            <input type="text" class="form-control" placeholder="Country" aria-label="reg_country"
                                aria-describedby="reg_country" v-model="regCountry"
                                :class="{ 'border border-danger': dataError && dataError['regCountry'] }">
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="reg_city">City</span>
                            <input type="text" class="form-control" placeholder="City" aria-label="reg_city"
                                aria-describedby="reg_city" v-model="regCity"
                                :class="{ 'border border-danger': dataError && dataError['regCity'] }">
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="reg_state">State</span>
                            <input type="text" class="form-control" placeholder="State" aria-label="reg_state"
                                aria-describedby="reg_state" v-model="regState"
                                :class="{ 'border border-danger': dataError && dataError['regState'] }">
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="reg_street">Street</span>
                            <input type="text" class="form-control" placeholder="Street" aria-label="reg_street"
                                aria-describedby="reg_street" v-model="regStreet"
                                :class="{ 'border border-danger': dataError && dataError['regStreet'] }">
                        </div>

                        <div class="input-group mb-3 row gx-0">
                            <div class="d-flex col-6">
                                <span class="input-group-text rounded-0 rounded-start" id="reg_homeNumber">Home</span>
                                <input type="text" class="form-control rounded-0 rounded-end me-2" placeholder="Home number"
                                    aria-label="reg_homeNumber" aria-describedby="reg_homeNumber" v-model="regHomeNumber"
                                    :class="{ 'border border-danger': dataError && dataError['regHomeNumber'] }">
                            </div>

                            <div class="d-flex col-6">
                                <span class="input-group-text rounded-0 rounded-start"
                                    id="reg_apartamentNumber">Apartament</span>
                                <input type="text" class="form-control rounded-0 rounded-end"
                                    placeholder="Apartament number" aria-label="reg_apartamentNumber"
                                    aria-describedby="reg_apartamentNumber" v-model="regApartamentNumber"
                                    :class="{ 'border border-danger': dataError && dataError['regApartamentNumber'] }">

                            </div>
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="reg_zipCode">Zip code</span>
                            <input type="text" class="form-control" placeholder="Zip code" aria-label="reg_zipCode"
                                aria-describedby="reg_zipCode" v-model="regZipCode"
                                :class="{ 'border border-danger': dataError && dataError['regZipCode'] }">
                        </div>
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
            password: '',
            password2: '',
            username: '',

            firstName: '',
            lastName: '',
            email: '',
            phone: '',
            identity: '',
            taxName: '',
            tax_address: '',
            nfz: '',
            bankAccount: '',

            resCountry: '',
            resCity: '',
            resState: '',
            resStreet: '',
            resHomeNumber: '',
            resApartamentNumber: '',
            resZipCode: '',

            corCountry: '',
            corCity: '',
            corState: '',
            corStreet: '',
            corHomeNumber: '',
            corApartamentNumber: '',
            corZipCode: '',

            regCountry: '',
            regCity: '',
            regState: '',
            regStreet: '',
            regHomeNumber: '',
            regApartamentNumber: '',
            regZipCode: '',


            fetched_data: {},
            dataError: null,
            dataCorrect: null,
            show_corespondece_form: true,
            show_registered_form: true,
        };
    },

    computed: {
        isFormValid() {
            return (
                this.firstName &&
                this.lastName &&
                this.email &&
                this.phone &&
                this.identity &&
                this.taxName &&
                this.tax_address &&
                this.nfz &&
                this.bankAccount &&
                this.resCountry &&
                this.resCity &&
                this.resState &&
                this.resStreet &&
                this.resHomeNumber &&
                this.resZipCode
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
        generatePassword() {
            const length = 8;
            const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=";
            let result = '';

            for (let i = 0; i < length; i++) {
                const randomIndex = Math.floor(Math.random() * charset.length);
                result += charset.charAt(randomIndex);
            }
            this.password = result;
            this.password2 = result;
        },
        async createUser() {
            this.generatePassword()

            const fetched_data = {
                first_name: this.firstName,
                last_name: this.lastName,
                email: this.email,
                phone_number: this.phone,
                username: this.username,
                password: this.password,
                password2: this.password2,
                user_role: 'HR',

                pesel_nip: this.identity,
                tax_office_name: this.taxName,
                tax_office_address: this.tax_address,
                nfz: this.nfz,
                bank_account_number: this.bankAccount,
                residence_country: this.resCountry,
                residence_city: this.resCity,
                residence_state: this.resState,
                residence_street: this.resStreet,
                residence_home_number: this.resHomeNumber,
                residence_apartament_number: this.resApartamentNumber,
                residence_zip_code: this.resZipCode,
            }

            //Corespondence addres
            if(this.show_corespondece_form){
                fetched_data.correspondence_country = this.resCountry;
                fetched_data.correspondence_city = this.resCity;
                fetched_data.correspondence_state = this.resState;
                fetched_data.correspondence_street = this.resStreet;
                fetched_data.correspondence_home_number = this.resHomeNumber;
                fetched_data.correspondence_apartament_number = this.resApartamentNumber;
                fetched_data.correspondence_zip_code = this.resZipCode;
            }
            else {
                fetched_data.correspondence_country = this.corCountry;
                fetched_data.correspondence_city = this.corCity;
                fetched_data.correspondence_state = this.corState;
                fetched_data.correspondence_street = this.corStreet;
                fetched_data.correspondence_home_number = this.corHomeNumber;
                fetched_data.correspondence_apartament_number = this.corApartamentNumber;
                fetched_data.correspondence_zip_code = this.corZipCode;
            }

            //Registered addres
            if(this.show_registered_form){
                fetched_data.registered_country = this.resCountry;
                fetched_data.registered_city = this.resCity;
                fetched_data.registered_state = this.resState;
                fetched_data.registered_street = this.resStreet;
                fetched_data.registered_home_number = this.resHomeNumber;
                fetched_data.registered_apartament_number = this.resApartamentNumber;
                fetched_data.registered_zip_code = this.resZipCode;
            }
            else {
                fetched_data.registered_country = this.regCountry;
                fetched_data.registered_city = this.regCity;
                fetched_data.registered_state = this.regState;
                fetched_data.registered_street = this.regStreet;
                fetched_data.registered_home_number = this.regHomeNumber;
                fetched_data.registered_apartament_number = this.regApartamentNumber;
                fetched_data.registered_zip_code = this.regZipCode;
            }


            this.dataError = ''
            const response = await axios.post('api/create/', fetched_data);


            if (response.data.message) {
                this.dataCorrect = response.data;
                document.getElementById('hiddenButton').click();
                this.resetForm();
            }
            else {
                this.dataError = response.data;
                document.getElementById('hiddenButton').click();
            }

        },
        resetForm() {
            this.password = '';
            this.password2 = '';
            this.username = '';

            this.firstName = '';
            this.lastName = '';
            this.email = '';
            this.phone = '';
            this.identity = '';
            this.taxName = '';
            this.tax_address = '';
            this.nfz = '';
            this.bankAccount = '';

            this.resCountry = '';
            this.resCity = '';
            this.resState = '';
            this.resStreet = '';
            this.resHomeNumber = '';
            this.resApartamentNumber = '';
            this.resZipCode = '';

            this.corCountry = '';
            this.corCity = '';
            this.corState = '';
            this.corStreet = '';
            this.corHomeNumber = '';
            this.corApartamentNumber = '';
            this.corZipCode = '';

            this.regCountry = '';
            this.regCity = '';
            this.regState = '';
            this.regStreet = '';
            this.regHomeNumber = '';
            this.regApartamentNumber = '';
            this.regZipCode = '';
        },
    }
};
</script>

<style scoped>
.container {
    text-align: center;
}

.form-switch {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.5rem;
}

.form-check-input:checked {
    background-color: #0d6efd;
    transition: background-color 0.5s;

}

.form-check-input:checked+.form-check-label::before {
    background-color: #fff;
    transition: background-color 0.5s;
}

.form-check-input:checked+.form-check-label::after {
    left: 24px;
    transition: left 0.5s;
}
</style>