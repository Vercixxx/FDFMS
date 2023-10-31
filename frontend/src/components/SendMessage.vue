<template>
    <v-row justify="center">
        <v-dialog v-model="dialog" persistent width="800">
            <v-card class="pa-5">
                <v-card-title class="text-h5">
                    Create message
                </v-card-title>
                <v-card-text>

                    <!-- Destiny -->
                    <v-select label="To" variant="solo-filled" :items="['Users', 'Groups']" v-model="target"
                        :disabled="target"></v-select>
                    <!-- Destiny -->



                    <!-- If Destiny is group -->
                    <v-select v-if="target === 'Groups'" chips label="Select groups" :items="groups" multiple
                        variant="solo-filled" v-model="selectedGroups"></v-select>
                    <!-- If Destiny is group -->



                    <!-- If Destiny are users -->
                    <v-dialog persistent v-model="dialogUsers" width="1400">
                        <v-card class="pa-5">
                            <v-card-title>
                                Select users
                            </v-card-title>
                            <v-card-text>

                                <!-- USERS -->
                                <v-row>
                                    <v-col cols="12" sm="6" align="center">

                                        <v-card class="pa-3 ma-1 border-xl rounded-xl"
                                            :color="theme ? 'grey-darken-3' : ''">
                                            <v-col cols="10" align="center">

                                                <p class="text-h4 text-md-h5 text-lg-h5">Available Users</p>

                                                <!-- Search bar -->
                                                <v-text-field variant="solo-filled" v-model="searchQueryAvailable"
                                                    @keydown.enter="searchTableAvailable = searchQueryAvailable"
                                                    label="Search" class="px-1 " prepend-inner-icon="mdi-magnify"
                                                    hide-actions hint="Press enter to search" />
                                                <!-- Search bar -->

                                                <!-- Available users -->
                                                <v-data-table :headers="tableHeaders" :items="availableUsers"
                                                    :search="searchTableAvailable" :loading="tableLoading"
                                                    class="elevation-4 rounded-xl" item-value="id"
                                                    v-model:items-per-page="itemsPerPage" hover select-strategy="all"
                                                    show-current-page>



                                                    <!-- No data -->
                                                    <template v-slot:no-data>
                                                        <p class="text-h6 pa-5">
                                                            <v-icon icon="mdi-database-alert-outline" color="red"></v-icon>
                                                            No available users
                                                        </p>
                                                    </template>
                                                    <!-- No data -->


                                                    <template #item="{ item }">
                                                        <tr @click="selectUser(item.columns.id)" role="button">
                                                            <td v-for="(cell, columnIndex) in item.columns"
                                                                :key="item.columns.id" class="text-center">

                                                                {{ cell }}

                                                            </td>
                                                        </tr>
                                                    </template>

                                                </v-data-table>
                                                <!-- Available users -->
                                            </v-col>
                                        </v-card>

                                    </v-col>

                                    <v-col cols="12" sm="6" align="center">

                                        <v-card class="pa-3 ma-1 border-xl rounded-xl"
                                            :color="theme ? 'grey-darken-3' : ''">
                                            <v-col cols="10" align="center">

                                                <p align="center" class="text-h4 text-md-h5 text-lg-h5">Selected users
                                                </p>

                                                <!-- Selected users -->
                                                <v-data-table :headers="tableHeaders" :items="selectedUsers"
                                                    :loading="tableLoading" class="elevation-4 rounded-xl" item-value="id"
                                                    v-model:items-per-page="itemsPerPage" hover select-strategy="all"
                                                    show-current-page>



                                                    <!-- No data -->
                                                    <template v-slot:no-data>
                                                        <p class="text-h6 pa-5">
                                                            <v-icon icon="mdi-database-alert-outline" color="red"></v-icon>
                                                            No selected users
                                                        </p>
                                                    </template>
                                                    <!-- No data -->


                                                    <template #item="{ item }">
                                                        <tr @click="unselectUser(item.columns.id)" role="button">
                                                            <td v-for="(cell, columnIndex) in item.columns"
                                                                :key="item.columns.id" class="text-center">

                                                                {{ cell }}

                                                            </td>
                                                        </tr>
                                                    </template>

                                                </v-data-table>
                                                <!-- Selected users -->
                                            </v-col>
                                        </v-card>

                                    </v-col>
                                </v-row>
                                <!-- USERS -->


                            </v-card-text>
                            <v-row>
                                <v-col cols="6">
                                    <v-btn block color="red-darken-1" variant="text" @click="close()">
                                        Close
                                    </v-btn>
                                </v-col>

                                <v-col cols="6">
                                    <span>
                                        <v-tooltip v-if="selectedUser === null" activator="parent" location="top"
                                            no-overflow>
                                            Select users
                                        </v-tooltip>
                                        <span>
                                            <v-btn block :disabled="!sendButton" color="green-darken-1" variant="text"
                                                @click="dialogUsers = false">
                                                Select
                                            </v-btn>
                                        </span>
                                    </span>
                                </v-col>
                            </v-row>
                        </v-card>
                    </v-dialog>
                    <!-- If Destiny are users -->



                    <!-- Title -->
                    <span>
                        <v-tooltip v-if="!target" activator="parent" location="bottom" no-overflow>
                            Choose recipient first
                        </v-tooltip>
                        <span>
                            <v-text-field :disabled="!target" label="Title" variant="solo-filled" v-model="title">
                            </v-text-field>
                        </span>
                    </span>
                    <!-- Title -->




                    <!-- Content -->
                    <span>
                        <v-tooltip v-if="!target" activator="parent" location="bottom" no-overflow>
                            Choose recipient first
                        </v-tooltip>
                        <span>
                            <v-textarea :disabled="!target" label="Content" variant="solo-filled"
                                v-model="content"></v-textarea>
                        </span>
                    </span>
                    <!-- Content -->

                </v-card-text>

                <!-- Buttons at the bottom-->
                <v-row>
                    <v-col cols="6">
                        <v-btn block color="red-darken-1" variant="text" @click="close()">
                            Close
                        </v-btn>
                    </v-col>

                    <v-col cols="6">
                        <span>
                            <v-tooltip v-if="!sendButton" activator="parent" location="top" no-overflow>
                                Fill all fields first
                            </v-tooltip>
                            <span>
                                <v-btn block :disabled="!sendButton" color="green-darken-1" variant="text"
                                    @click="sendMessage()">
                                    Send
                                </v-btn>
                            </span>
                        </span>
                    </v-col>
                </v-row>
                <!-- Buttons at the bottom -->

            </v-card>
        </v-dialog>
    </v-row>
</template>

<!-- <script setup>
import { VDataTable } from 'vuetify/labs/VDataTable';
</script> -->

<script>
import axios from 'axios';
export default {
    data() {
        return {
            dialog: false,

            target: null,

            groups: [
                'Drivers',
                'Managers',
                'HR',
                'Payroll',
                'Clients',
                'Assets',
            ],
            selectedGroups: [],

            // Users
            dialogUsers: false,
            availableUsers: {},
            selectedUsers: {},
            tableHeaders: [
                { title: 'Username', key: 'username', align: 'center', sortable: true },
                { title: 'Id', key: 'id', align: 'center', sortable: true },
            ],
            // Search
            searchTableAvailable: '',
            // Users

            sendButton: false,

            title: '',
            content: '',
        }
    },

    methods: {
        // Close dialog
        close() {
            this.dialog = false;
            this.target = null;
            this.title = '';
            this.content = '';
            this.selectedGroups = [];
        },
        // Close dialog



        // Get all Usernames
        async getUsers() {
            const response = await axios.get('api/users/get-usernames/');
            this.availableUsers = response.data;
        },
        // Get all Usernames

        sendMessage() {

        },
    },

    watch: {
        target: function (newTarget, oldTarget) {
            if (newTarget === 'Users') {
                this.getUsers();
                this.dialogUsers = true;
            } else {
                this.dialogUsers = false;
            }
        }
    }
}
</script>