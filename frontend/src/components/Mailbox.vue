<template>
    <v-row>
        <v-col cols="2">

            <!-- Desktop version -->
            <span v-if="!$vuetify.display.smAndDown">

                <p align="center">
                    {{ loggedUser.first_name + ' ' + loggedUser.last_name }}
                </p>

                <v-btn block v-for="button in buttons" :key="button.name" :text="button.name" :prepend-icon="button.icon"
                    variant="outlined" @click="menuClickHandle(button.component)" class=" pa-2 my-4">
                </v-btn>
            </span>
            <!-- Desktop version -->

        </v-col>

        <v-col cols="12" sm="10">

            <v-row>

                <v-col cols="12">
                    <v-text-field v-model="search" label="Search" prepend-inner-icon="mdi-magnify" variant="outlined"
                        hide-details @keydown.enter="fetchData()"></v-text-field>

                    <!-- Mobile -->
                    <v-row v-if="$vuetify.display.smAndDown">
                        <v-col cols="10">
                            <v-select class="mt-1" v-model="mailVersion" variant="underlined" :items="buttons"
                                item-title="name" @update:model-value="menuClickHandle(mailVersion)">

                                <template v-slot:selection>
                                    <v-row align="center" justify="center">
                                        <v-col cols="12" align="center" justify="center">
                                            {{ mailVersion.toUpperCase() }}
                                        </v-col>
                                    </v-row>
                                </template>

                                <template v-slot:prepend>
                                    Mailbox version
                                </template>
                            </v-select>
                        </v-col>
                        <v-col cols="2" align="center" justify="center" class="mb-10">
                            <v-btn class="mb-3 mt-3" prepend-icon="mdi-refresh" @click="fetchData()"
                                :variant="$vuetify.display.smAndDown ? 'plain' : 'outlined'"
                                :text="$vuetify.display.smAndDown ? '' : 'Reload'">
                            </v-btn>
                        </v-col>
                    </v-row>

                    <!-- Mobile -->

                    <!-- Desktop -->
                    <span align="center" v-if="!$vuetify.display.smAndDown">

                        <p v-if="mailVersion === 'all'" class="text-h4 my-5">
                            All messages
                        </p>
                        <p v-else-if="mailVersion === 'inbox'" class="text-h4 my-5">
                            Inbox
                        </p>
                        <p v-else-if="mailVersion === 'sent'" class="text-h4 my-5">
                            Sent
                        </p>

                    </span>
                    <!-- Desktop -->


                    <v-btn v-if="!$vuetify.display.smAndDown" class="mb-3 mt-3" prepend-icon="mdi-refresh"
                        @click="fetchData()" variant="outlined" text="Reload">
                    </v-btn>


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

                        <!-- Loading -->
                        <template v-slot:loading>
                            <v-skeleton-loader type="table-row@10"></v-skeleton-loader>
                        </template>
                        <!-- Loading -->

                        <template v-slot:bottom v-if="mails.length == 0">
                        </template>

                    </v-data-table-server>
                </v-col>

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
                    name: 'All mails',
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

    created() {
        this.loggedUser = this.$store.getters.userData;
    },

    mounted() {
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
                const response = await axios.get(`api/messages/get/?user=${this.loggedUser.username}&version=${this.mailVersion}&query=${this.search}`);
                this.mails = response.data;

            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
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

                this.$store.dispatch('triggerAlert', { message: `Successfully deleted ${this.selected.length} messages`, type: 'success' });

                this.selected = [];
                this.fetchData();
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
        },
        // Delete messages

    },

}

</script>