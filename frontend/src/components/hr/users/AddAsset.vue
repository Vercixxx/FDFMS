<template>
    <div>
        <div class="containter m-2 p-2 d-flex justify-content-center">
            <div class="col-12 col-md-9">

                <p v-if="user_role === null" class="fs-4 text-center fw-bolder">Add new Asset user</p>
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
                    <div class="fs-4 text-center fw-bolder">Edit user</div>
                    <div></div>

                </div>

                <form action="" method="post" class="border rounded-3 p-3" @submit.prevent="createUser">

                    <!-- Username field visible only when editing existing user -->
                    <div v-if="username !== null" class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Username
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" disabled aria-label="username"
                                aria-describedby="username" v-model="username"
                                :class="{ 'border border-danger': dataError && dataError['username'] }">
                        </div>
                    </div>
                    <!-- Username field visible only when editing existing user -->


                    <!-- First name -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            First name
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="first_name"
                                aria-describedby="first_name" v-model="firstName" @input="updateUsername"
                                :class="{ 'border border-danger': dataError && dataError['first_name'] }">
                        </div>
                    </div>
                    <!-- First name -->


                    <!-- Last name -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Last name
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="last_name"
                                aria-describedby="last_name" v-model="lastName" @input="updateUsername"
                                :class="{ 'border border-danger': dataError && dataError['last_name'] }">
                        </div>
                    </div>
                    <!-- Last name -->


                    <!-- Email -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Email
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="email" class="form-control rounded-0 rounded-end" aria-label="email"
                                aria-describedby="email" v-model="email"
                                :class="{ 'border border-danger': dataError && dataError['email'] }">
                        </div>
                    </div>
                    <!-- Email -->


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


                    <!-- PESEL / NIP -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            PESEL / NIP
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="identity"
                                aria-describedby="identity" v-model="identity"
                                :class="{ 'border border-danger': dataError && dataError['identity'] }">
                        </div>
                    </div>
                    <!-- PESEL / NIP -->


                    <!-- Dane rozliczeniowe i zdrowotne -->
                    <div class="border border-2 p-2 text-center my-5 fw-bolder shadow">
                        Tax and health information
                    </div>


                    <!-- Tax office name -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Tax office name
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="tax_name"
                                aria-describedby="tax_name" v-model="taxName"
                                :class="{ 'border border-danger': dataError && dataError['taxName'] }">
                        </div>
                    </div>
                    <!-- Tax office name -->


                    <!-- Tax office address -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Tax office address
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="tax_address"
                                aria-describedby="tax_address" v-model="tax_address"
                                :class="{ 'border border-danger': dataError && dataError['tax_address'] }">
                        </div>
                    </div>
                    <!-- Tax office address -->


                    <!-- NFZ branch -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            NFZ branch
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="nfz"
                                aria-describedby="nfz" v-model="nfz"
                                :class="{ 'border border-danger': dataError && dataError['nfz'] }">
                        </div>
                    </div>
                    <!-- NFZ branch -->


                    <!-- Bank Account Number -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Bank Account Number
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="bank_account"
                                aria-describedby="bank_account" v-model="bankAccount"
                                :class="{ 'border border-danger': dataError && dataError['bankAccount'] }">
                        </div>
                    </div>
                    <!-- Bank Account Number -->



                    <div class="border border-2 p-2 text-center my-5 fw-bolder shadow">
                        Residence address
                    </div>



                    <!-- Residence address Country -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Country
                        </div>
                        <div class="col-9 d-flex align-items-center">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="res_country"
                                aria-describedby="res_country" v-model="resCountry"
                                :class="{ 'border border-danger': dataError && dataError['resCountry'] }">
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
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="res_city"
                                aria-describedby="res_city" v-model="resCity"
                                :class="{ 'border border-danger': dataError && dataError['resCity'] }">
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
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="res_state"
                                aria-describedby="res_state" v-model="resState"
                                :class="{ 'border border-danger': dataError && dataError['resState'] }">
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
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="res_street"
                                aria-describedby="res_street" v-model="resStreet"
                                :class="{ 'border border-danger': dataError && dataError['resStreet'] }">
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
                                    aria-label="res_homeNumber" aria-describedby="res_homeNumber" v-model="resHomeNumber"
                                    :class="{ 'border border-danger': dataError && dataError['resHomeNumber'] }">
                            </div>
                            <!-- Residence address Home number -->


                            <!-- Residence address Apartament number -->
                            <div
                                class="col-2 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                Apartament
                            </div>
                            <div class="col-4 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end"
                                    aria-label="res_apartamentNumber" aria-describedby="res_apartamentNumber"
                                    v-model="resApartamentNumber"
                                    :class="{ 'border border-danger': dataError && dataError['resApartamentNumber'] }">
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
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="res_zipCode"
                                aria-describedby="res_zipCode" v-model="resZipCode"
                                :class="{ 'border border-danger': dataError && dataError['resZipCode'] }">
                        </div>
                    </div>
                    <!-- Residence Zip code -->



                    <div class="form-check form-switch" id="switch1">
                        <input class="form-check-input toggleSwitch" type="checkbox" v-model="show_corespondece_form">
                        <div class="fs-6 ms-2 fw-semibold mx-auto p-2">
                            Correspodence address same as residence address
                        </div>
                        <div class="slider" :class="{ active: show_corespondece_form }"></div>
                    </div>


                    <!-- Correspodence address form -->
                    <div :style="{ display: show_corespondece_form ? 'none' : 'block' }">

                        <div class="border border-2 p-2 text-center my-5 fw-bolder shadow">
                            Addres for correspodence
                        </div>


                        <!-- Correspodence address Country -->
                        <div class="input-group mb-3">
                            <div
                                class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                Country
                            </div>
                            <div class="col-9 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end" aria-label="cor_country"
                                    aria-describedby="cor_country" v-model="corCountry"
                                    :class="{ 'border border-danger': dataError && dataError['corCountry'] }">
                            </div>
                        </div>
                        <!-- Correspodence address Country -->


                        <!-- Correspodence address City -->
                        <div class="input-group mb-3">
                            <div
                                class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                City
                            </div>
                            <div class="col-9 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end" aria-label="cor_city"
                                    aria-describedby="cor_city" v-model="corCity"
                                    :class="{ 'border border-danger': dataError && dataError['corCity'] }">
                            </div>
                        </div>
                        <!-- Correspodence address City -->


                        <!-- Correspodence address State -->
                        <div class="input-group mb-3">
                            <div
                                class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                State
                            </div>
                            <div class="col-9 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end" aria-label="cor_state"
                                    aria-describedby="cor_state" v-model="corState"
                                    :class="{ 'border border-danger': dataError && dataError['corState'] }">
                            </div>
                        </div>
                        <!-- Correspodence address State -->


                        <!-- Correspodence address Street -->
                        <div class="input-group mb-3">
                            <div
                                class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                Street
                            </div>
                            <div class="col-9 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end" aria-label="cor_street"
                                    aria-describedby="cor_street" v-model="corStreet"
                                    :class="{ 'border border-danger': dataError && dataError['corStreet'] }">
                            </div>
                        </div>
                        <!-- Correspodence address Street -->


                        <div class="input-group mb-3 gx-0">

                            <!-- Correspodence address Home number -->
                            <div class="input-group">
                                <div
                                    class="col-2 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                    Home
                                </div>
                                <div class="col-4 d-flex align-items-center">
                                    <input type="text" class="form-control rounded-0 rounded-end me-2"
                                        aria-label="cor_homeNumber" aria-describedby="cor_homeNumber"
                                        v-model="corHomeNumber"
                                        :class="{ 'border border-danger': dataError && dataError['corHomeNumber'] }">
                                </div>
                                <!-- Correspodence address Home number -->


                                <!-- Correspodence address Apartament number -->
                                <div
                                    class="col-2 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                    Apartament
                                </div>
                                <div class="col-4 d-flex align-items-center">
                                    <input type="text" class="form-control rounded-0 rounded-end"
                                        aria-label="cor_apartamentNumber" aria-describedby="cor_apartamentNumber"
                                        v-model="corApartamentNumber"
                                        :class="{ 'border border-danger': dataError && dataError['corApartamentNumber'] }">
                                </div>
                                <!-- Correspodence address Apartament number -->
                            </div>

                        </div>


                        <!-- Correspodence Zip code -->
                        <div class="input-group mb-3">
                            <div
                                class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                Zip code
                            </div>
                            <div class="col-9 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end" aria-label="cor_zipCode"
                                    aria-describedby="cor_zipCode" v-model="corZipCode"
                                    :class="{ 'border border-danger': dataError && dataError['corZipCode'] }">
                            </div>
                        </div>
                        <!-- Correspodence Zip code -->

                    </div>
                    <!-- Correspodence address form -->





                    <div class="form-check form-switch" id="switch2">
                        <input class="form-check-input toggleSwitch" type="checkbox" v-model="show_registered_form">
                        <div class="fs-6 ms-2 text-wrap fw-semibold mx-auto p-2">
                            Registered address same as residence address
                        </div>
                        <div class="slider" :class="{ active: show_registered_form }"></div>
                    </div>

                    <!-- Registered address form -->
                    <div :style="{ display: show_registered_form ? 'none' : 'block' }">

                        <div class="border border-2 p-2 text-center my-5 fw-bolder shadow">
                            Registered address
                        </div>


                        <!-- Registered address Country -->
                        <div class="input-group mb-3">
                            <div
                                class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                Country
                            </div>
                            <div class="col-9 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end" aria-label="reg_country"
                                    aria-describedby="reg_country" v-model="regCountry"
                                    :class="{ 'border border-danger': dataError && dataError['regCountry'] }">
                            </div>
                        </div>
                        <!-- Registered address Country -->


                        <!-- Registered address City -->
                        <div class="input-group mb-3">
                            <div
                                class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                City
                            </div>
                            <div class="col-9 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end" aria-label="reg_city"
                                    aria-describedby="reg_city" v-model="regCity"
                                    :class="{ 'border border-danger': dataError && dataError['regCity'] }">
                            </div>
                        </div>
                        <!-- Registered address City -->


                        <!-- Registered address State -->
                        <div class="input-group mb-3">
                            <div
                                class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                State
                            </div>
                            <div class="col-9 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end" aria-label="reg_state"
                                    aria-describedby="reg_state" v-model="regState"
                                    :class="{ 'border border-danger': dataError && dataError['regState'] }">
                            </div>
                        </div>
                        <!-- Registered address State -->


                        <!-- Registered address Street -->
                        <div class="input-group mb-3">
                            <div
                                class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                Street
                            </div>
                            <div class="col-9 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end" aria-label="reg_street"
                                    aria-describedby="reg_street" v-model="regStreet"
                                    :class="{ 'border border-danger': dataError && dataError['regStreet'] }">
                            </div>
                        </div>
                        <!-- Registered address Street -->


                        <div class="input-group mb-3 gx-0">

                            <!-- Registered address Home number -->
                            <div class="input-group">
                                <div
                                    class="col-2 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                    Home
                                </div>
                                <div class="col-4 d-flex align-items-center">
                                    <input type="text" class="form-control rounded-0 rounded-end me-2"
                                        aria-label="reg_homeNumber" aria-describedby="reg_homeNumber"
                                        v-model="regHomeNumber"
                                        :class="{ 'border border-danger': dataError && dataError['regHomeNumber'] }">
                                </div>
                                <!-- Registered address Home number -->


                                <!-- Registered address Apartament number -->
                                <div
                                    class="col-2 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                    Apartament
                                </div>
                                <div class="col-4 d-flex align-items-center">
                                    <input type="text" class="form-control rounded-0 rounded-end"
                                        aria-label="reg_apartamentNumber" aria-describedby="reg_apartamentNumber"
                                        v-model="regApartamentNumber"
                                        :class="{ 'border border-danger': dataError && dataError['regApartamentNumber'] }">
                                </div>
                                <!-- Registered address Apartament number -->
                            </div>

                        </div>


                        <!-- Registered Zip code -->
                        <div class="input-group mb-3">
                            <div
                                class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                                Zip code
                            </div>
                            <div class="col-9 d-flex align-items-center">
                                <input type="text" class="form-control rounded-0 rounded-end" aria-label="reg_zipCode"
                                    aria-describedby="reg_zipCode" v-model="regZipCode"
                                    :class="{ 'border border-danger': dataError && dataError['regZipCode'] }">
                            </div>
                        </div>
                        <!-- Registered Zip code -->
                    </div>


                    <div class="text-center">
                        <button v-if="user_role === null" type="button" class="btn btn-success shadow" @click="createUser"
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

            user_role: null,

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


    mounted() {
        this.username = localStorage.getItem('username')

        if (this.username !== null) {
            this.user_role = localStorage.getItem('user_role')
            this.getUserData(this.username, this.user_role);

            // Correspodence and Register forms
            var switch1 = document.getElementById("switch1");
            var switch2 = document.getElementById("switch2");

            switch1.style.display = 'none';
            switch2.style.display = 'none';

            this.show_corespondece_form = false;
            this.show_registered_form = false;
            // Correspodence and Register forms

        }
    },


    methods: {
        generateRandomDigits() {
            return Math.floor(100 + Math.random() * 900);
        },
        updateUsername() {
            if (this.user_role === null) {
                const firstThreeChars = this.firstName.slice(0, 3).toLowerCase();
                const lastThreeChars = this.lastName.slice(0, 3).toLowerCase();
                const randomDigits = this.generateRandomDigits();
                this.username = firstThreeChars + lastThreeChars + randomDigits;
            }
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
                phone: this.phone,
                username: this.username,
                password: this.password,
                password2: this.password2,
                user_role: 'Asset',

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
            if (this.show_corespondece_form) {
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
            if (this.show_registered_form) {
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

            console.log(fetched_data)
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

        async getUserData(username, user_role) {

            const response = await axios.get(`api/users/get/${username}/${user_role}`);
            console.log(response.data);

            localStorage.removeItem('username');
            localStorage.removeItem('user_role');
            
            // Set input data
            this.username = response.data.username;

            this.firstName = response.data.first_name;
            this.lastName = response.data.last_name;
            this.email = response.data.email;
            this.phone = response.data.phone;
            this.identity = response.data.pesel_nip;
            this.taxName = response.data.tax_office_name;
            this.tax_address = response.data.tax_office_address;
            this.nfz = response.data.nfz;
            this.bankAccount = response.data.bank_account_number;

            this.resCountry = response.data.residence_country;
            this.resCity = response.data.residence_city;
            this.resState = response.data.residence_state;
            this.resStreet = response.data.residence_street;
            this.resHomeNumber = response.data.residence_home_number;
            this.resApartamentNumber = response.data.residence_apartament_number;
            this.resZipCode = response.data.residence_zip_code;

            this.corCountry = response.data.correspondence_country;
            this.corCity = response.data.correspondence_city;
            this.corState = response.data.correspondence_state;
            this.corStreet = response.data.correspondence_street;
            this.corHomeNumber = response.data.correspondence_home_number;
            this.corApartamentNumber = response.data.correspondence_apartament_number;
            this.corZipCode = response.data.correspondence_zip_code;

            this.regCountry = response.data.registered_country;
            this.regCity = response.data.registered_city;
            this.regState = response.data.registered_state;
            this.regStreet = response.data.registered_street;
            this.regHomeNumber = response.data.registered_home_number;
            this.regApartamentNumber = response.data.registered_apartament_number;
            this.regZipCode = response.data.registered_zip_code;
            // Set input data


        },

        async updateUser() {
            // Generate dict for sending
            const fetched_data = {
                first_name: this.firstName,
                last_name: this.lastName,
                email: this.email,
                phone: this.phone,
                username: this.username,
                password: this.password,

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

                correspondence_country: this.corCountry,
                correspondence_city: this.corCity,
                correspondence_state: this.corState,
                correspondence_street: this.corStreet,
                correspondence_home_number: this.corHomeNumber,
                correspondence_apartament_number: this.corApartamentNumber,
                correspondence_zip_code: this.corZipCode,

                registered_country: this.regCountry,
                registered_city: this.regCity,
                registered_state: this.regState,
                registered_street: this.regStreet,
                registered_home_number: this.regHomeNumber,
                registered_apartament_number: this.regApartamentNumber,
                registered_zip_code: this.regZipCode,
            };

            // Send put request
            console.log("ASDAGRFSE")
            const response2 = await axios.put(`api/users/save/${this.username}/${this.user_role}/`, fetched_data);
            const message = `Successfully updated ${this.username}`;
            localStorage.setItem('message', message);


            // Finish
            this.goBack()
        },

        goBack() {
            this.$root.changeCurrentComponent('ModifyUserComponent');
        }
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