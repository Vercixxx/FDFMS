<template>
    <div>

        <div class="containter m-2 p-2 d-flex justify-content-center">

            <div class="col-12 col-md-9">
                <p v-if="carId !== null" class="fs-4 fw-bolder">Edit Car</p>
                <p v-else class="fs-4 fw-bolder">Add new Car</p>
                <form action="" method="post" class="border rounded-3 p-3" @submit.prevent="createCar">


                    <div class="border border-2 p-2 text-center mb-5 fw-bolder shadow">
                        Basic car information
                    </div>

                    <!-- VIN -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            VIN
                        </div>
                        <div class="col-9">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="vin"
                                aria-describedby="vin" v-model="vin"
                                :class="{ 'border border-danger': dataError && dataError['vin'] }">
                        </div>
                    </div>
                    <!-- VIN -->

                    <!-- Year of production -->
                    <div class="input-group mb-3">
                        <div
                            class="col-auto px-4 d-flex fw-bolder align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Year of production
                        </div>
                        <div class="col-auto">
                            <select class="form-select rounded-0 rounded-end text-center" v-model="selectedYear"
                                aria-label="Select Year of production">
                                <option value="" disabled>Select year</option>
                                <option v-for="year in availableYears" :value="year">{{ year }}</option>
                            </select>
                        </div>

                    </div>
                    <!-- Year of production -->

                    <!-- Brand -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Brand
                        </div>
                        <div class="col-9">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="brand"
                                aria-describedby="brand" v-model="brand"
                                :class="{ 'border border-danger': dataError && dataError['brand'] }">
                        </div>
                    </div>
                    <!-- Brand -->

                    <!-- Model -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Model
                        </div>
                        <div class="col-9">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="model"
                                aria-describedby="model" v-model="model"
                                :class="{ 'border border-danger': dataError && dataError['model'] }">
                        </div>
                    </div>
                    <!-- Model -->

                    <!-- Color -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Color
                        </div>
                        <div class="col-9">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="color"
                                aria-describedby="color" v-model="color"
                                :class="{ 'border border-danger': dataError && dataError['color'] }">
                        </div>
                    </div>
                    <!-- Color -->

                    <!-- Mileage -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Mileage
                        </div>
                        <div class="col-9">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="mileage"
                                aria-describedby="mileage" v-model="mileage"
                                :class="{ 'border border-danger': dataError && dataError['mileage'] }">
                        </div>
                    </div>
                    <!-- Mileage -->

                    <!-- Engine capacity -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Engine capacity
                        </div>
                        <div class="col-9">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="capacity"
                                aria-describedby="capacity" v-model="capacity"
                                :class="{ 'border border-danger': dataError && dataError['capacity'] }">
                        </div>
                    </div>
                    <!-- Engine capacity -->

                    <!-- Engine power -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Engine power
                        </div>
                        <div class="col-9">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="power"
                                aria-describedby="power" v-model="power"
                                :class="{ 'border border-danger': dataError && dataError['power'] }">
                        </div>
                    </div>
                    <!-- Engine power -->

                    <!-- Transsmision -->
                    <div class="input-group mb-3">
                        <div
                            class="col-auto px-4 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Transsmision
                        </div>
                        <div class="col-auto">
                            <select class="form-select rounded-0 rounded-end" v-model="selectedTranssmision"
                                aria-label="selectedTranssmision">
                                <option value="" disabled>Select transsmision</option>
                                <option value="Manual" selected>Manual</option>
                                <option value="Automatic">Automatic</option>
                            </select>
                        </div>
                    </div>
                    <!-- Transsmision -->



                    <div class="border border-2 p-2 text-center my-5 fw-bolder shadow">
                        Insurance info
                    </div>

                    <!-- Policy number -->
                    <div class="input-group mb-3">
                        <div
                            class="col-3 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Policy number
                        </div>
                        <div class="col-9">
                            <input type="text" class="form-control rounded-0 rounded-end" aria-label="policyNumber"
                                aria-describedby="policyNumber" v-model="policyNumber"
                                :class="{ 'border border-danger': dataError && dataError['policyNumber'] }">
                        </div>
                    </div>

                    <!-- Insurance phone number -->

                    <!-- Policy number -->
                    <div class="input-group mb-3">
                        <div
                            class="col-auto px-4 fw-bolder d-flex align-items-center justify-content-center border rounded-start bg-body-tertiary">
                            Insurance phone number
                        </div>
                        <div class="col-auto">
                            <input type="phone" class="form-control rounded-0 rounded-end" aria-label="insurancePhone"
                                aria-describedby="insurancePhone" v-model="insurancePhone"
                                :class="{ 'border border-danger': dataError && dataError['insurancePhone'] }">
                        </div>
                    </div>
                    <!-- Insurance phone number -->

                    <!-- AC and OC -->
                    <div class="input-group mb-3 ">

                        <div
                            class="hstack border rounded-3 p-2 fw-bolder bg-body-tertiary col-6 d-flex align-items-center justify-content-center">

                            Does car has OC

                            <span class="form-check form-switch mx-3">
                                <input class="form-check-input" type="checkbox" role="switch" id="has_oc" v-model="oc"
                                    checked>
                            </span>
                        </div>


                        <div
                            class="hstack border rounded-3 p-2 fw-bolder bg-body-tertiary col-6 d-flex align-items-center justify-content-center">

                            Does car has AC

                            <span class="form-check form-switch mx-3">
                                <input class="form-check-input" type="checkbox" role="switch" id="has_ac" v-model="ac"
                                    checked>
                            </span>
                        </div>

                    </div>
                    <!-- AC and OC -->




                    <div class="text-center">
                        <button v-if="carId === null" type="button" class="btn btn-success shadow" @click="createCar"
                            :disabled="!isFormValid" :class="{ 'btn-outline-danger': !isFormValid }">
                            <span class="d-flex align-items-center">
                                Add
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                                    class="bi bi-plus-square ms-2" viewBox="0 0 16 16">
                                    <path
                                        d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z" />
                                    <path
                                        d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z" />
                                </svg>
                            </span>
                        </button>

                        <!-- Button when editing existing car -->
                        <button v-else type="button" class="btn btn-success shadow" @click="modifyCar">
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
                        <!-- Button when editing existing car -->

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
                                Succesfully created
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
            carId: null,
            vin: '',
            brand: '',
            model: '',
            color: '',
            mileage: '',
            capacity: '',
            power: '',
            policyNumber: '',
            oc: true,
            ac: true,
            insurancePhone: '',
            selectedYear: '',
            selectedTranssmision: '',
            availableYears: [],
            year: '',
            dataError: '',
            dataCorrect: '',
            push_data: ''
        };
    },

    computed: {
        isFormValid() {
            return (
                this.vin &&
                this.brand &&
                this.model &&
                this.selectedYear &&
                this.color &&
                this.mileage &&
                this.capacity &&
                this.power &&
                this.vin &&
                this.selectedTranssmision &&
                this.policyNumber &&
                this.insurancePhone
            );
        },
    },

    mounted() {
        const currentYear = new Date().getFullYear();
        for (let year = currentYear; year >= 1990; year--) {
            this.availableYears.push(year.toString());
        }
        this.carId = localStorage.getItem('carid')
        if (this.carId !== null) {
            this.getCarInfo()
        }
    },


    methods: {
        async createCar() {
            const push_data = {
                vin: this.vin,
                brand: this.brand,
                model: this.model,
                year_of_prod: this.selectedYear,
                color: this.color,
                mileage: this.mileage,
                engine_cap: this.capacity,
                engine_pow: this.power,
                vin: this.vin,
                transmission: this.selectedTranssmision,
                policy_number: this.policyNumber,
                is_oc: this.oc,
                is_ac: this.ac,
                phone_policy_contact: this.insurancePhone,

            }
            console.log(push_data);

            const response = await axios.post('api/car', push_data);

            console.log(response);
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
            this.vin = '';
            this.brand = '';
            this.model = '';
            this.color = '';
            this.mileage = '';
            this.capacity = '';
            this.power = '';
            this.policyNumber = '';
            this.oc = true;
            this.ac = true;
            this.insurancePhone = '';
            this.selectedYear = '';
            this.selectedTranssmision = '';
        },

        async modifyCar() {

            const push_data = {
                vin: this.vin,
                brand: this.brand,
                model: this.model,
                year_of_prod: this.selectedYear,
                color: this.color,
                mileage: this.mileage,
                engine_cap: this.capacity,
                engine_pow: this.power,
                vin: this.vin,
                transmission: this.selectedTranssmision,
                policy_number: this.policyNumber,
                is_oc: this.oc,
                is_ac: this.ac,
                phone_policy_contact: this.insurancePhone,

            }
            console.log(push_data)
            const response = await axios.put(`api/car/save/${this.carId}`, push_data);
            console.log(response)

            localStorage.removeItem('carid')
            this.$parent.ShowCarsComponent()

        },

        async getCarInfo() {
            console.log(this.carId)
            const response = await axios.get(`api/car/edit/${this.carId}`);
            console.log(response.data);

            this.vin = response.data.vin;
            this.brand = response.data.brand;
            this.model = response.data.model;
            this.selectedYear = response.data.year_of_prod;
            this.color = response.data.color;
            this.mileage = response.data.mileage;
            this.capacity = response.data.engine_cap;
            this.power = response.data.engine_pow;
            this.selectedTranssmision = response.data.transmission;
            this.policyNumber = response.data.policy_number;
            this.oc = response.data.is_oc;
            this.ac = response.data.is_ac;
            this.insurancePhone = response.data.phone_policy_contact;

        }
    },


}
</script>