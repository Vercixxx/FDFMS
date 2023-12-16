<template>
    <v-row justify="center">
        <v-dialog v-model="dialog" persistent width="800">

            <v-form v-model="form" @submit.prevent="onSubmit">

                <v-card class="pa-5">
                    <v-card-title class="text-h5 font-weight-bold">
                        Create message
                    </v-card-title>
                    <v-card-text>

                        <!-- Target -->
                        <v-select label="Choose recivers" variant="solo-filled" :items="['Users', 'Groups']"
                            v-model="target" :disabled="target"></v-select>
                        <!-- Target -->



                        <!-- If Target is group -->
                        <v-select v-if="target === 'Groups'" chips label="Select groups" :items="groups" multiple
                            variant="solo-filled" v-model="selectedGroups" :disabled="loading"
                            :rules="[required]"></v-select>
                        <!-- If Target is group -->


                        <!-- If Users selected -->
                        <v-select v-else-if="target === 'Users'" chips multiple label="Selected users"
                            :items="selectedUsers" v-model="selectedUsers" variant="solo-filled" @click="dialogUsers = true"
                            item-title="username" readonly immediate>

                        </v-select>
                        <!-- If Users selected -->


                        <!-- If Target are users -->
                        <v-dialog persistent v-model="dialogUsers" width="1400">
                            <v-card class="pa-5">
                                <v-card-title>
                                    Select users
                                </v-card-title>
                                <v-card-text>


                                    <v-row>
                                        <v-col cols="12" sm="6" align="center">

                                            <v-card class="pa-3 ma-1 border-xl rounded-xl"
                                                :color="theme ? 'grey-darken-3' : ''">
                                                <v-col cols="10" align="center">

                                                    <p class="text-h4 text-md-h5 text-lg-h5">Available Users</p>


                                                    <!-- Search bar -->
                                                    <v-text-field variant="solo-filled" v-model="searchUsers"
                                                        @keydown.enter="getUsers" label="Search" class="px-1 "
                                                        prepend-inner-icon="mdi-magnify" hide-actions
                                                        hint="Press enter to search" />
                                                    <!-- Search bar -->


                                                    <v-data-table-server :headers="tableHeaders" :items="availableUsers"
                                                        :loading="loading" class="elevation-4 rounded-xl" hover>


                                                        <template v-slot:no-data>
                                                            <p class="text-h6 pa-5">
                                                                <v-icon icon="mdi-database-alert-outline"
                                                                    color="red"></v-icon>
                                                                No available users
                                                            </p>
                                                        </template>

                                                        <template v-slot:item="{ item }">
                                                            <tr align="center" @click="selectUser(item.username)"
                                                                role="button">
                                                                <v-tooltip v-if="!form" activator="parent" location="top"
                                                                    no-overflow>
                                                                    Click to select
                                                                </v-tooltip>
                                                                <td v-for="header in tableHeaders" :key="header.key">
                                                                    {{ item.username }}
                                                                </td>
                                                            </tr>
                                                        </template>

                                                    </v-data-table-server>
                                                </v-col>
                                            </v-card>
                                        </v-col>


                                        <v-col cols="12" sm="6" align="center">

                                            <v-card class="pa-3 ma-1 border-xl rounded-xl"
                                                :color="theme ? 'grey-darken-3' : ''">
                                                <v-col cols="10" align="center">

                                                    <p align="center" class="text-h4 text-md-h5 text-lg-h5">Selected users
                                                    </p>

                                                    <v-data-table :headers="tableHeaders" :items="selectedUsers"
                                                        class="elevation-4 rounded-xl" item-value="username"
                                                        v-model:items-per-page="itemsPerPage" hover select-strategy="all"
                                                        show-current-page>




                                                        <template v-slot:no-data>
                                                            <p class="text-h6 pa-5">
                                                                <v-icon icon="mdi-database-alert-outline"
                                                                    color="red"></v-icon>
                                                                No selected users
                                                            </p>
                                                        </template>



                                                        <template v-slot:item="{ item }">
                                                            <tr align="center" @click="unselectUser(item.username)"
                                                                role="button">
                                                                <v-tooltip v-if="!form" activator="parent" location="top"
                                                                    no-overflow>
                                                                    Click to unselect
                                                                </v-tooltip>
                                                                <td v-for="header in tableHeaders" :key="header.key">
                                                                    {{ item.username }}
                                                                </td>
                                                            </tr>
                                                        </template>

                                                    </v-data-table>

                                                </v-col>
                                            </v-card>
                                        </v-col>
                                    </v-row>




                                </v-card-text>
                                <v-row>
                                    <v-col cols="6">
                                        <v-btn block color="red-darken-1" variant="text" @click="dialogUsers = false">
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
                                                <v-btn block :disabled="selectedUsers === null" color="green-darken-1"
                                                    variant="text" @click="dialogUsers = false">
                                                    Select
                                                </v-btn>
                                            </span>
                                        </span>
                                    </v-col>
                                </v-row>
                            </v-card>
                        </v-dialog>
                        <!-- If Target are users -->



                        <!-- Title -->
                        <span>
                            <v-tooltip v-if="!target" activator="parent" location="bottom" no-overflow>
                                Choose recipient first
                            </v-tooltip>
                            <span>
                                <v-text-field :disabled="!target" label="Title" variant="solo-filled" v-model="title"
                                    :readonly="loading" :rules="[required]">
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
                                <v-textarea :disabled="!target" label="Content" variant="solo-filled" v-model="content"
                                    :readonly="loading" :rules="[required]"></v-textarea>
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
                                <v-tooltip v-if="!form" activator="parent" location="top" no-overflow>
                                    Fill all fields first
                                </v-tooltip>
                                <span>
                                    <v-btn block type="submit" :disabled="!form" :loading="loading" color="green-darken-1"
                                        variant="text">
                                        Send
                                    </v-btn>
                                </span>
                            </span>
                        </v-col>
                    </v-row>
                    <!-- Buttons at the bottom -->
                </v-card>
            </v-form>
        </v-dialog>
    </v-row>
</template>


<script>
import axios from 'axios';
import useEventsBus from '../plugins/eventBus.js'
const { emit } = useEventsBus()
import { watch } from "vue";
export default {
    data() {
        return {
            dialog: false,
            loading: false,
            form: false,
            loggedUser: null,

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
            allUsers: [],
            availableUsers: [],
            selectedUsers: [],
            selectedUsersDisplay: [],
            itemsPerPage: 10,
            tableHeaders: [
                { title: 'Username', key: 'username', align: 'center', sortable: false },
            ],
            // Search
            searchUsers: '',
            // Users



            to: [],
            title: '',
            content: '',
        }
    },



    mounted() {
        const { bus } = useEventsBus();
        watch(
            () => [bus.value.get('showAddMessage')],
            ([showAddMessage]) => {
                if (showAddMessage) {
                    this.dialog = true
                    // Get list of users
                    this.getUsers();
                }
            }
        );

        this.loggedUser = this.$store.getters.responseData.username;

    },

    computed: {
        availableUsers() {
            return this.allUsers.filter(user => !this.selectedUsers.some(selectedUser => selectedUser.username === user.username));
        }
    },


    methods: {



        onSubmit() {
            if (!this.form) return

            this.loading = true
            this.sendMessage()
        },
        required(v) {
            return !!v || 'Field is required'
        },


        // Close dialog
        close() {
            this.dialog = false;
            this.target = null;
            this.title = '';
            this.content = '';
            this.selectedGroups = [];
            this.selectedUsers = [];
        },
        // Close dialog



        // Get all Usernames
        async getUsers() {
            this.loading = true
            try {
                const response = await axios.get(`api/users/get-usernames/?role=All&search=${this.searchUsers}`);
                this.allUsers = response.data;
                this.loading = false
            } catch (error) {
                const messageData = {
                    message: error,
                    type: 'error'
                };

                localStorage.setItem('message', JSON.stringify(messageData));
                emit('message', '');
            }

        },
        // Get all Usernames



        // Move user to selected
        selectUser(username) {
            const userIndex = this.allUsers.findIndex(user => user.username === username);
            if (userIndex !== -1) {
                const userToCopy = this.allUsers[userIndex];
                const copiedUser = Object.assign({}, userToCopy);
                this.selectedUsers.push(copiedUser);
            }
        },
        // Move user to selected



        // Move user to unselected
        unselectUser(username) {
            const userIndex = this.selectedUsers.findIndex(user => user.username === username);
            if (userIndex !== -1) {
                this.selectedUsers.splice(userIndex, 1);
            }
        },
        // Move user to unselected



        // Send message
        async sendMessage() {
            const data = {
                'title': this.title,
                'content': this.content,
                'from': this.loggedUser,
            }
            if (this.target === 'Groups') {
                data['taget'] = 'Groups';
                data['to'] = this.selectedGroups;
            }
            else {
                data['taget'] = 'Users';
                data['to'] = this.selectedUsers.map(user => user.username);
            }
            console.log(data);
            this.loading = false;
            this.close();

            try{
                const response = await axios.post('api/messages/create/', data);
                console.log(reponse)
                const messageData = {
                    message: response.data.message,
                    type: 'success'
                };

                localStorage.setItem('message', JSON.stringify(messageData));
                emit('message', '');

            } catch(error) {
                const messageData = {
                    message: error,
                    type: 'error'
                };

                localStorage.setItem('message', JSON.stringify(messageData));
                emit('message', '');
            }

        },
        // Send message
    },

}
</script>