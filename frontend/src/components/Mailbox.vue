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
                    

                    <span v-if="mailVersion === 'all'">
                        <p class="text-h4 my-5">
                            All messages
                        </p>
                    </span>
                    <span v-else-if="mailVersion === 'inbox'">
                        <p class="text-h4 my-5">
                            Inbox
                        </p>
                    </span>
                    <span v-else-if="mailVersion === 'sent'">
                        <p class="text-h4 my-5">
                            Sent
                        </p>
                    </span>

                    <v-data-table v-model="selected" :items="mails" :headers="headers" :loading="loading" item-value="id"
                        show-select show-expand v-model:expanded="expanded">

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

                    </v-data-table>
                </v-col>
                {{ selected }}, {{ expanded }}
            </v-row>


        </v-col>
    </v-row>
</template>



<script>
import axios from 'axios'

export default {
    name: 'App',


    data() {
        return {

            mailVersion: 'inbox',

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
            ]
        }
    },



    mounted() {
        this.fetchData();
    },



    methods: {
        menuClickHandle(component) {
            this.mailVersion = component
            this.fetchData()
        },



        //Get data
        async fetchData() {
            this.loading = true
            try {
                this.mails = [];
                const response = await axios.get(`api/messages/get/?version=${this.mailVersion}&query=${this.search}`);
                console.log(response);
                this.mails = response.data;
                
            } catch(error) {
                
            }
            this.loading = false;
        },
        //Get data

    },

}

</script>