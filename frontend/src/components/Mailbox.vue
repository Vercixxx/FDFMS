<template>
    <v-row>
        <v-col cols="2">

            <p align="center">Menu</p>

            <v-btn block v-for="button in buttons" :key="button.name" :text="button.name" :prepend-icon="button.icon"
                variant="outlined" @click="menuClickHandle(button.component)" class=" pa-2 my-4">
            </v-btn>

        </v-col>



        <v-col cols="10">

            <v-row>

                <v-col cols="12" align="center">

                    <v-text-field v-model="search" label="Search" prepend-inner-icon="mdi-magnify" variant="outlined"
                        hide-details @keydown.enter="fetchData()"></v-text-field>

                    <v-row class="my-3">
                        <v-col></v-col>
                        <v-col>
                            <p v-if="mailVersion === 'all'" class="text-h4 my-5">
                                All messages
                            </p>
                            <p v-else-if="mailVersion === 'inbox'" class="text-h4 my-5">
                                Inbox
                            </p>
                            <p v-else-if="mailVersion === 'sent'" class="text-h4 my-5">
                                Sent
                            </p>
                        </v-col>

                        <v-col align="end">
                            <v-tooltip :text="`Delete selected messages (${selected.length})`"
                                v-if="mailVersion === 'inbox'">
                                <template v-slot:activator="{ props }">
                                    <v-btn icon="mdi-delete" color="red" variant="plain" v-bind="props"
                                        :disabled="selected.length < 1" @click="dialogDelete = true"></v-btn>
                                </template>
                            </v-tooltip>
                        </v-col>
                    </v-row>


                    <v-data-table-server v-model="selected" :items="mails" :headers="headers" :loading="loading"
                        item-value="id" show-select show-expand v-model:expanded="expanded"
                        loading-text="Loading... Please wait">

                        <template v-slot:expanded-row="{ columns, item }">
                            <tr>
                                <td :colspan="columns.length">

                                    <v-card class="my-2">
                                        <v-card-item>
                                            <v-card-title> {{ item.title }} </v-card-title>

                                            <v-card-subtitle>From {{ item.sender }}, to {{ item.receiver }}. {{
                                                item.posted_date }}</v-card-subtitle>
                                        </v-card-item>

                                        <v-card-text>
                                            {{ item.content }}
                                        </v-card-text>
                                    </v-card>

                                </td>
                            </tr>
                        </template>

                        <template v-slot:loading>
                            <v-skeleton-loader type="table-row@10"></v-skeleton-loader>
                        </template>

                        <!-- <template v-slot:header.data-table-select="{ selectAll, getSortIcon }">
                           <v-btn @click="selectAll" variant="plain">Select all</v-btn>
                           <v-btn @click="getSortIcon" variant="plain">Select all</v-btn>
                        </template> -->

                    </v-data-table-server>
                </v-col>
                selected {{ selected }}
            </v-row>

        </v-col>


        <!-- Delete messages confirm -->
        <v-dialog v-model="dialogDelete" width="400">
            <v-card>
                <div class="text-danger text-h6 text-md-h5 text-lg-h4">
                    <div class="d-flex justify-content-between align-items-center px-4 pt-4">
                        <v-icon icon="mdi-alert" class="text-h4" />
                        Warning
                        <v-icon icon="mdi-alert" class="text-h4" />
                    </div>

                    <hr />
                </div>

                <div class="pa-3" align="center">

                    You are trying to delete
                    <span class='fw-bolder'>
                        {{ selected.length }}
                    </span>
                    messages, this operation is <span class="fw-bold">irreversible</span>.
                    Are you sure?

                </div>
                <hr>

                <div class="justify-center d-flex align-items-center mb-3">
                    <v-btn variant="outlined" width="150" class="mr-5" @click="dialogDelete = false">No</v-btn>
                    <v-btn width="150" @click="deleteMessages()" color="red">
                        <v-icon icon="mdi-delete-empty"></v-icon>
                        Yes
                    </v-btn>
                </div>

            </v-card>
        </v-dialog>
        <!-- Delete messages confirm -->




    </v-row>
</template>



<script>
import axios from 'axios'
import useEventsBus from '../plugins/eventBus.js'
const { emit } = useEventsBus()

export default {
    name: 'App',


    data() {
        return {

            mailVersion: 'inbox',
            loggedUser: null,

            loading: true,

            selected: [],
            expanded: [],
            mails: [],
            search: '',
            headers: [
                {
                    title: 'From',
                    align: 'start',
                    sortable: true,
                    key: 'sender',
                },
                {
                    title: 'To',
                    align: 'start',
                    sortable: true,
                    key: 'receiver',
                },
                {
                    title: 'Title',
                    align: 'start',
                    sortable: true,
                    key: 'title',
                },
                {
                    title: 'Date',
                    align: 'start',
                    sortable: true,
                    key: 'posted_date',
                },
            ],

            buttons: [
                {
                    name: 'All mail',
                    icon: 'mdi-email-multiple-outline',
                    component: 'all'
                },
                {
                    name: 'Inbox',
                    icon: 'mdi-email-arrow-left-outline',
                    component: 'inbox'
                },
                {
                    name: 'Sent',
                    icon: 'mdi-send-variant-outline',
                    component: 'sent'
                },
            ],

            dialogDelete: false,
        }
    },



    mounted() {
        this.loggedUser = this.$store.getters.responseData.username;
        this.fetchData();
    },



    methods: {
        menuClickHandle(component) {
            this.mailVersion = component
            this.fetchData()
            this.selected = []
        },



        //Get data
        async fetchData() {
            this.loading = true
            try {
                this.mails = [];
                const response = await axios.get(`api/messages/get/?user=${this.loggedUser}&version=${this.mailVersion}&query=${this.search}`);
                this.mails = response.data;

            } catch (error) {
                const messageData = {
                    message: error,
                    type: 'error'
                };

                localStorage.setItem('message', JSON.stringify(messageData));
                emit('message', '');
            }
            this.loading = false;
        },
        //Get data



        // Delete messages
        async deleteMessages() {
            this.dialogDelete = false
            try {
                const response = await axios.delete('/api/messages/delete/', {
                    data: { message_ids: this.selected },
                })

                const messageData = {
                    message: `Successfully deleted ${this.selected.length} messages`,
                    type: 'success'
                };

                localStorage.setItem('message', JSON.stringify(messageData));
                emit('message', '');
                this.selected = [];
            } catch (error) {
                const messageData = {
                    message: error,
                    type: 'error'
                };

                localStorage.setItem('message', JSON.stringify(messageData));
                emit('message', '');
            }
        },
        // Delete messages

    },

}

</script>