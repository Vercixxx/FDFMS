<template>
    <v-dialog v-model="showDialog" persistent max-width="500px">
        <v-card>
            <v-card-title align="center">
                Countries and states
            </v-card-title>
            <v-card-text>
                <v-row>
                    <v-col cols="12" md="6">
                        <v-select label="Choose type" variant="solo-filled" :items="options" v-model="type" 
                            @update:modelValue="handleChange"></v-select>
                    </v-col>
                </v-row>

                <v-row v-if="type !== null">
                    <!-- Table -->
                    <v-col cols="12">
                        <v-data-table :headers="headers" :items="items" :items-per-page="5" class="elevation-1"
                            :loading="tableLoading" item-value="name">
                            <template v-slot:item.action="{ item }">
                                <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
                                <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
                            </template>
                        </v-data-table>
                        <!-- Table -->
                    </v-col>
                </v-row>
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" text @click="closeDialog()">Close</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
import { mapState } from 'vuex';
import axios from 'axios';

export default {
    name: 'ManageCountryState',
    data() {
        return {
            showDialog: false,

            options: [
                'Country',
                'State',
            ],

            type: null,

            tableLoading: true,

            headers: [
                { title: 'Name', key: 'name', align: 'center' },
                { title: 'Action', key: 'action', sortable: false, align: 'center' },
            ],

            items: [],
        };
    },
    computed: {
        ...mapState(['modifyStateDialog']),
    },
    watch: {
        modifyStateDialog(newVal) {
            this.showDialog = newVal;
        },
    },
    methods: {
        closeDialog() {
            this.$store.commit('setModifyStateDialog', false);
        },

        async fetchCountries() {
            this.tableLoading = true;
            try {
                const response = await axios.get('api/countries/get/');
                console.log(response);
                this.items = response.data;
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
            this.tableLoading = false;
        },

        async fetchStates() {
            this.tableLoading = true;
            try {
                const response = await axios.get('api/states/get/');
                this.items = response.data;
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
            this.tableLoading = false;
        },

        handleChange() {
            if (this.type === 'Country') {
                this.fetchCountries();
            } else if (this.type === 'State') {
                this.fetchStates();
            }
        },
    },
    mounted() {

    },
};
</script>
