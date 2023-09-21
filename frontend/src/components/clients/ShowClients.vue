<template>
    <div>

        <h1>
            List of restaurants
        </h1>


        <!-- Options and search bar section -->
        <div class="d-flex justify-content-between mt-3 mb-5">
            <!-- Options -->
            <div class="p2">
                <p class="fw-bolder fs-5">Filters</p>

                <div class="btn-group dropdown mx-2">
                    <span class="input-group-text rounded-0 rounded-start" id="basic-addon1">
                        City
                    </span>

                    <button type="button" class="btn btn-outline-secondary dropdown-toggle" data-bs-toggle="dropdown"
                        aria-expanded="false">
                        <span>{{ selectedCity.toUpperCase() }}</span>

                    </button>

                    <ul class="dropdown-menu">

                        <li @click="selectCity('all')"><a class="dropdown-item fw-bolder " role="button">All</a></li>
                        <li>
                            <hr class="dropdown-divider">
                        </li>
                        <li v-for="city in possible_cities" :key="city" @click="selectCity(city)"><a class="dropdown-item "
                                role="button">{{ city
                                }}</a></li>

                    </ul>
                </div>
            </div>
            <!-- Options -->

            <!-- Search bar -->
            <div>
                <form role="search" method="POST" action="" @submit.prevent="search">
                    <div class="input-group">

                        <input class="form-control " type="search" placeholder="Search" aria-label="Search" v-model="query">
                        <button type="button" class="btn btn-outline-success d-flex align-items-center px-3"
                            @click="search">

                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-search me-2" viewBox="0 0 16 16">
                                <path
                                    d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z" />
                            </svg>
                        </button>

                    </div>
                </form>
            </div>
            <!-- Search bar -->

        </div>
        <!-- Options and search bar section -->




        <!-- Table -->
        <div v-if="restaurants.length === 0" class="text-danger fs-2">
            No records.
        </div>

        <div v-else class="table-responsive">
            <table class="table table-hover table-striped">
                <thead>
                    <tr class="text-center">
                        <th v-for="column in columns" :key="column.attribute">{{ column.label }}</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody class="table-group-divider">
                    <tr v-for="restaurant in restaurants" :key="restaurant.name" class="text-center align-middle">
                        <td v-for="column in columns" :key="column.attribute">

                            <!-- null -->
                            <span v-if="restaurant[column.attribute] === null || restaurant[column.attribute] === ''">
                                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor"
                                    class="bi bi-x" viewBox="0 0 16 16">
                                    <path
                                        d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 1 1 .708.708L8.707 8l2.647 2.646a.5.5 0 1 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z" />
                                </svg>
                            </span>

                            <!-- default -->
                            <span v-else>
                                {{ restaurant[column.attribute] }}
                            </span>
                        </td>
                        <td>
                            <!-- Button edit -->
                            <button class="btn btn-outline-success m-3" @click="editRestaurant(restaurant.name)"
                                v-b-tooltip="'Edit'">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                    class="bi bi-pencil" viewBox="0 0 16 16">
                                    <path
                                        d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z" />
                                </svg>
                            </button>

                            <!-- Button delete -->
                            <button class="btn btn-outline-danger" @click="deleteConfirm(restaurant.name)"
                                v-b-tooltip="'Delete'">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                    class="bi bi-trash3" viewBox="0 0 16 16">
                                    <path
                                        d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5ZM11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H2.506a.58.58 0 0 0-.01 0H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1h-.995a.59.59 0 0 0-.01 0H11Zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5h9.916Zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47ZM8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5Z" />
                                </svg>
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <!-- Table -->

        <!-- Pagination -->
        <div class="d-flex justify-content-between mb-4">
            <div class="mt-1">
                <span class="fw-lighter border rounded-3 p-2"> Finded {{ page_flip.count }} records</span>
            </div>


            <div class="border rounded-2 d-flex align-items-center">

                <!-- Button previous -->
                <button type="button" class="btn btn-outline-secondary border-0 ms-2" @click="previousPage"
                    :disabled="!page_flip.previous">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-caret-left" viewBox="0 0 16 16">
                        <path
                            d="M10 12.796V3.204L4.519 8 10 12.796zm-.659.753-5.48-4.796a1 1 0 0 1 0-1.506l5.48-4.796A1 1 0 0 1 11 3.204v9.592a1 1 0 0 1-1.659.753z" />
                    </svg>
                </button>

                <!-- Current page -->
                <p class="fw-bolder mx-2 text-center mt-3">Page {{ currentPage + 1 }}</p>


                <!-- Button next -->
                <button type="button" class="btn btn-outline-secondary border-0 me-2" @click="nextPage"
                    :disabled="!page_flip.next">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-caret-right" viewBox="0 0 16 16">
                        <path
                            d="M6 12.796V3.204L11.481 8 6 12.796zm.659.753 5.48-4.796a1 1 0 0 0 0-1.506L6.66 2.451C6.011 1.885 5 2.345 5 3.204v9.592a1 1 0 0 0 1.659.753z" />
                    </svg>
                </button>

            </div>

        </div>
        <!-- Pagination -->





        <!-- Confirmation modal -->
        <!-- Button trigger modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#confirmModal"
            id="confirm_modal_button" style="display: none;">
        </button>

        <!-- Modal -->
        <div class="modal fade" id="confirmModal" tabindex="-1" aria-labelledby="confirmModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header d-flex justify-content-between text-warning">
                        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor"
                            class="bi bi-exclamation-triangle" viewBox="0 0 16 16">
                            <path
                                d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
                            <path
                                d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
                        </svg>
                        <h1 class="modal-title fs-5" id="confirmModalLabel">
                            Caution
                        </h1>
                        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor"
                            class="bi bi-exclamation-triangle" viewBox="0 0 16 16">
                            <path
                                d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
                            <path
                                d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
                        </svg>
                    </div>
                    <div class="modal-body text-danger fs-5">
                        <p>
                            You are trying to delete <span class="fw-bolder"> {{ delete_name }}</span> this
                            operation is <span class="fw-bold">irreversible</span>. Are you sure?
                        </p>
                    </div>
                    <div class="modal-footer d-flex justify-content-center">
                        <button type="button" class="btn btn-outline-secondary fs-5 w-25"
                            data-bs-dismiss="modal">No</button>
                        <button type="button" class="btn btn-danger fs-5 w-25" data-bs-dismiss="modal"
                            @click="deleteRestaurant()">Yes</button>
                    </div>
                </div>
            </div>
        </div>
        <!-- Confirmation modal -->


        <!-- Message modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#ErrorModal" id="hiddenButton"
            style="display: none;">
        </button>
        <div class="modal fade" id="ErrorModal" tabindex="-1" aria-labelledby="ErrorModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <!-- Error -->
                    <div v-if="dataError" class="modal-header d-flex justify-content-between  text-danger">
                        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor"
                            class="bi bi-exclamation-triangle" viewBox="0 0 16 16">
                            <path
                                d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
                            <path
                                d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
                        </svg>
                        <h1 class="modal-title fs-5" id="confirmModalLabel">
                            Error
                        </h1>
                        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor"
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
                                Succesfully deleted
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
    name: 'App',

    data() {
        return {
            restaurants: [],
            columns: [],
            currentPage: 0,
            restaurants_per_site: 20,
            page_flip: {},
            query: '',
            dataError: null,
            dataSuccess: null,
            delete_name: '',
            possible_cities: [],
            selectedCity: 'all',



            columns: [
                { label: 'NAME', attribute: 'name' },
                { label: 'PHONE NUMBER', attribute: 'phone' },
                { label: 'COUNTRY', attribute: 'country' },
                { label: 'CITY', attribute: 'city' },
                { label: 'STATE', attribute: 'state' },
                { label: 'STREET', attribute: 'street' },
                { label: 'HOME', attribute: 'home_number' },
                { label: 'APARTAMENT', attribute: 'apartament_number' },
                { label: 'ZIP CODE', attribute: 'zip_code' },
            ],


        };
    },

    created() {
        this.loadRestaurants();
        this.getPossibleCities()
        // check for messages in local storage
        if (localStorage.getItem('message')) {
            const message = localStorage.getItem('message');
            console.log(message);

        }
    },

    methods: {
        async loadRestaurants() {
            try {
                const response = await axios.get('api/restaurants/get-restaurants/', {
                    params: {
                        limit: this.restaurants_per_site,
                        offset: this.currentPage,
                        search: this.query,
                        city: this.selectedCity,
                    }
                });
                console.log(response)
                console.log(response.data)

                this.page_flip = {
                    count: response.data.count,
                    next: response.data.next,
                    previous: response.data.previous,
                }

                this.restaurants = response.data.results;
            }
            catch (error) {
                console.error('Error when fetching', error);
            }
        },

        previousPage() {
            this.currentPage -= 1;
            this.loadRestaurants();
        },
        nextPage() {
            this.currentPage += 1;
            this.loadRestaurants();
        },

        async getPossibleCities() {
            const response = await axios.get('api/restaurants/unique_cities/');
            this.possible_cities = response.data;
            console.log(this.possible_cities);

        },

        selectCity(city) {
            this.selectedCity = city;
            this.loadRestaurants();
        },


        deleteConfirm(name) {
            this.delete_name = name;
            document.getElementById('confirm_modal_button').click();
        },

        async deleteRestaurant() {
            try {
                const response = await axios.delete(`api/restaurant/delete/${this.delete_name}`);
                this.reloadComponent()
                console.log(response)

                if (response.status === 204) {
                    this.loadRestaurants();
                    this.dataSuccess = 'Success!'
                    document.getElementById('hiddenButton').click();

                }
                else {
                    this.loadRestaurants();
                    this.dataError = 'Error!'
                    document.getElementById('hiddenButton').click();
                }


            }
            catch (error) {
                console.error('Error when fetching', error);
            }
        },

        editRestaurant() {
            // localStorage.setItem('restaurantid', restaurantid)
            // this.$parent.AddRestaurantComponent()
        },

        search() {
            this.loadRestaurants();
        },

        reloadComponent() {
            this.loadRestaurants();
        },


    },
};
</script>