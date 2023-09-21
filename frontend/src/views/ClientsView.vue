<template>
    <div class="ClientsView">
        <div class="containter rounded-3 p-1 m-2 border shadow text-white" :style="{
            'background-image': 'url(' + backgroundImage + ')',
            'background-size': 'cover',
            'background-position': 'center 50%',
        }">
            <div class="d-flex justify-content-between">

                <div class="p-2">

                    <!-- Title -->
                    <div class="my-text-container rounded-3">

                        <p class="fs-2 fst-italic mb-4 px-2">FDFMS - Clients Management console</p>
                    </div>

                </div>
                <div class="p-2 d-flex align-items-center">

                    <p class="fs-3 mb-1 px-2 my-text-container me-2">
                        Hi,
                        {{ userData.first_name }}
                    </p>
                    <button type="submit" class="btn btn-outline-danger shadow" @click="logoutConfirmFunc">
                        <span class="d-flex align-items-center">
                            Logout
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                                class="bi bi-box-arrow-right ms-2" viewBox="0 0 16 16">
                                <path fill-rule="evenodd"
                                    d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0v2z" />
                                <path fill-rule="evenodd"
                                    d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z" />
                            </svg>
                        </span>
                    </button>
                </div>

            </div>
            <!-- Navbar -->
            <nav class="navbar navbar-expand-lg ">
                <div class="container-fluid">
                    <button class="navbar-toggler custom-button " type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav">


                            <!-- Home button -->
                            <li class="nav-item me-3">
                                <button class="nav-link btn btn-outline p-2 fs-5 my-2 border shadow custom-button" role="button" 
                                    aria-expanded="false" @click="showHomeComponent">
                                    <span class="d-flex align-items-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                                            class="bi bi-house me-2" viewBox="0 0 16 16">
                                            <path
                                                d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L2 8.207V13.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V8.207l.646.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5ZM13 7.207V13.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V7.207l5-5 5 5Z" />
                                        </svg>
                                        Home
                                    </span>
                                </button>
                            </li>
                            <!-- Home button -->





                            <!-- Option 1 -->
                            <li class="nav-item dropdown me-3">
                                <button class="nav-link  btn btn-outline p-2 fs-5 my-2 border shadow custom-button " role="button"
                                    data-bs-toggle="dropdown" aria-expanded="false">
                                    <span class="d-flex align-items-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                                            class="bi bi-buildings me-2" viewBox="0 0 16 16">
                                            <path
                                                d="M14.763.075A.5.5 0 0 1 15 .5v15a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5V14h-1v1.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V10a.5.5 0 0 1 .342-.474L6 7.64V4.5a.5.5 0 0 1 .276-.447l8-4a.5.5 0 0 1 .487.022ZM6 8.694 1 10.36V15h5V8.694ZM7 15h2v-1.5a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 .5.5V15h2V1.309l-7 3.5V15Z" />
                                            <path
                                                d="M2 11h1v1H2v-1Zm2 0h1v1H4v-1Zm-2 2h1v1H2v-1Zm2 0h1v1H4v-1Zm4-4h1v1H8V9Zm2 0h1v1h-1V9Zm-2 2h1v1H8v-1Zm2 0h1v1h-1v-1Zm2-2h1v1h-1V9Zm0 2h1v1h-1v-1ZM8 7h1v1H8V7Zm2 0h1v1h-1V7Zm2 0h1v1h-1V7ZM8 5h1v1H8V5Zm2 0h1v1h-1V5Zm2 0h1v1h-1V5Zm0-2h1v1h-1V3Z" />
                                        </svg>
                                        Restaurants
                                    </span>
                                </button>
                                <ul class="dropdown-menu shadow">
                                    <li><a class="dropdown-item " @click="AddClientsComponent" role="button">
                                            <span class="d-flex align-items-center">

                                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                    fill="currentColor" class="bi bi-plus-square me-2" viewBox="0 0 16 16">
                                                    <path
                                                        d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z" />
                                                    <path
                                                        d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z" />
                                                </svg>
                                                Add
                                            </span>
                                        </a></li>
                                    <li><a class="dropdown-item" @click="ShowClientsComponent" role="button">
                                            <span class="d-flex align-items-center">

                                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                    fill="currentColor" class="bi bi-pencil  me-2" viewBox="0 0 16 16">
                                                    <path
                                                        d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z" />
                                                </svg>
                                                Modify
                                            </span>
                                        </a></li>

                                </ul>
                            </li>
                            <!-- Option 1 -->




                        </ul>
                    </div>
                </div>
            </nav>
            <!-- Navbar -->
        </div>
    </div>
    <!-- content -->
    <div class="cointainter m-2 p-2">
        <component :is="currentComponent"></component>
    </div>
    <!-- content -->

    <!-- Confirmation modal -->
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#confirmLogout"
        id="confirmLogoutButton" style="display: none;">
    </button>

    <!-- Modal -->
    <div class="modal fade" id="confirmLogout" tabindex="-1" aria-labelledby="confirmLogoutLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header d-flex justify-content-between text-warning">
                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor"
                        class="bi bi-exclamation-triangle" viewBox="0 0 16 16">
                        <path
                            d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
                        <path
                            d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
                    </svg>
                    <h1 class="modal-title fs-5" id="confirmLogoutLabel">

                        Logout
                    </h1>
                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor"
                        class="bi bi-exclamation-triangle" viewBox="0 0 16 16">
                        <path
                            d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z" />
                        <path
                            d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z" />
                    </svg>

                </div>
                <div class="modal-body fs-5 text-center">
                    <p>
                        Are you sure?
                    </p>
                </div>
                <div class="mb-4 d-flex justify-content-center">
                    <button type="button" class="btn btn-secondary w-25 me-2 fs-4" data-bs-dismiss="modal">No</button>
                    <button type="button" class="btn btn-danger w-25 fs-4" data-bs-dismiss="modal"
                        @click="logout">Yes</button>
                </div>
            </div>
        </div>
    </div>
    <!-- Confirmation modal -->
</template>

<script>
import backgroundImage from '../assets/bg.jpg';

// components
import Home from '../components/Home.vue';
import AddClient from '../components/clients/AddClient.vue';
import ShowClients from '../components/clients/ShowClients.vue';

export default {
    name: "ClientsView",

    data() {
        return {
            backgroundImage: backgroundImage,
            userData: this.$store.getters.responseData,
            currentComponent: null,
            confirmLogout: null,
        };
    },



    methods: {

        logoutConfirmFunc() {
            document.getElementById('confirmLogoutButton').click();
        },

        async logout() {
            this.$store.commit('resetState');
            this.$router.push('/');
        },

        showHomeComponent() {
            this.currentComponent = Home;
        },
        AddClientsComponent() {
            this.currentComponent = AddClient;
        },
        ShowClientsComponent() {
            this.currentComponent = ShowClients;
        },

    },

    components: {},
};
</script>

<style>

.custom-button {
  background: rgba(200, 200, 200, 0.3); 
  backdrop-filter: blur(5px); 
  transition: background-color 0.3s;
  color:rgb(239, 239, 228);
}

.custom-button:hover {
  background-color: rgba(200, 200, 200, 0.7);
  backdrop-filter: blur(5px); 
  color:rgb(239, 239, 228);
}

.my-text-container {
  backdrop-filter: blur(3px);
}
</style>