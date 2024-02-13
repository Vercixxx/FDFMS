<template>
    <v-card-title align="center">
        Countries and states
    </v-card-title>
    <v-card-text>
        <v-row>
            <v-col cols="12" md="2">
                <v-select label="Choose type" variant="solo-filled" :items="options" v-model="type"
                    @update:modelValue="handleChange"></v-select>
            </v-col>
        </v-row>

        <v-row v-if="type != null">
            <v-btn @click="addItem()" color="success" variant="outlined"
                :text="type === 'Country' ? 'Add Country' : 'Add State'" prepend-icon="mdi-plus" class="mb-2"></v-btn>
        </v-row>


        <!-- Adding and editing -->
        <v-dialog v-model="countryDialog" max-width="500" persistent>
            <v-card align="center">

                <v-form v-model="form">
                    <v-card-title>
                        Add Country
                    </v-card-title>

                    <v-card-text>
                        <v-row>
                            <v-col>
                                <v-text-field label="Country name" v-model="addingCountryName"
                                    :rules="rules"></v-text-field>
                            </v-col>
                        </v-row>
                    </v-card-text>

                    <v-card-actions>
                        <v-row class="ma-1">
                            <v-col>
                                <v-btn color="primary" block @click="closeCountryDialog()">Close</v-btn>
                            </v-col>
                            <v-col>
                                <v-btn color="success" block @click="addEditCountry()" :disabled="!form" text="Add"></v-btn>
                            </v-col>
                        </v-row>
                    </v-card-actions>
                </v-form>

            </v-card>
        </v-dialog>

        <v-dialog v-model="addStateDialog" max-width="500" persistent>
            <v-card align="center">

                <v-form v-model="form">
                    <v-card-title>
                        <span v-if="editing">
                            Edit {{ editingItem.name }} in {{ editingItem.country }}
                        </span>
                        <span v-else>
                            Add State
                        </span>
                    </v-card-title>

                    <v-card-text>
                        <v-row>
                            <v-col cols="12" md="6">
                                <v-select label="Choose country" variant="solo-filled" :items="countries" item-title="name"
                                    item-value="id" v-model="addingStateCountryName"
                                    @update:modelValue="handleChange"></v-select>
                            </v-col>

                            <v-col cols="12" md="6">
                                <v-text-field label="State name" v-model="addingStateName"
                                    :disabled="addingStateCountryName === null" :rules="rules"></v-text-field>
                            </v-col>
                        </v-row>
                    </v-card-text>

                    <v-card-actions>
                        <v-row class="ma-1">
                            <v-col>
                                <v-btn color="primary" block @click="closeStateDialog()">Close</v-btn>
                            </v-col>
                            <v-col>
                                <v-btn color="success" block @click="addEditState()" :disabled="!form"
                                    :text="editing ? 'Save' : 'Add'"></v-btn>
                            </v-col>
                        </v-row>
                    </v-card-actions>
                </v-form>

            </v-card>
        </v-dialog>
        <!-- Adding and editing -->

        <v-row v-if="type !== null">

            <!-- Country -->
            <v-col cols="12" v-if="type == 'Country'">
                <v-data-table :headers="countryHeaders" :items="countries" :items-per-page="5" class="elevation-1"
                    :loading="tableLoading" item-value="name">

                    <!-- Loading -->
                    <template v-slot:loading>
                        <v-skeleton-loader type="table-row@5"></v-skeleton-loader>
                    </template>
                    <!-- Loading -->

                    <template v-slot:item.action="{ item }">

                        <v-btn variant="plain" color="red" @click="deleteConfirm(item)">
                            <v-icon icon="mdi-delete-empty" class="text-h5"></v-icon>
                            <v-tooltip activator="parent" location="top">Delete {{ item.name }}</v-tooltip>
                        </v-btn>

                    </template>
                </v-data-table>

            </v-col>
            <!-- Country -->

            <!-- State -->
            <v-col cols="12" v-else>
                <v-data-table :headers="statesHeaders" :items="states" :items-per-page="5" class="elevation-1"
                    :loading="tableLoading" item-value="name">

                    <!-- Loading -->
                    <template v-slot:loading>
                        <v-skeleton-loader type="table-row@5"></v-skeleton-loader>
                    </template>
                    <!-- Loading -->

                    <template v-slot:item.action="{ item }">

                        <v-btn variant="plain" color="green" @click="editItem(item)">
                            <v-icon icon="mdi-pencil-outline" class="text-h5"></v-icon>
                            <v-tooltip activator="parent" location="top">Edit {{ item.name }}</v-tooltip>
                        </v-btn>

                        <v-btn variant="plain" color="red" @click="deleteConfirm(item)">
                            <v-icon icon="mdi-delete-empty" class="text-h5"></v-icon>
                            <v-tooltip activator="parent" location="top">Delete {{ item.name }}</v-tooltip>
                        </v-btn>

                    </template>
                </v-data-table>
            </v-col>
            <!-- State -->
        </v-row>

    </v-card-text>


    <!-- Delete dialog -->
    <v-dialog v-model="dialogDelete" width="400" persistent>
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
                    {{ deleteItem.name }}
                </span>
                , this operation is <span class="fw-bold">irreversible</span>.
                Are you sure?

            </div>
            <hr>

            <div class="justify-center d-flex align-items-center mb-3">
                <v-btn variant="outlined" width="150" class="mr-5" @click="dialogDelete = false">No</v-btn>
                <v-btn width="150" @click="delteItem(deleteItem)" color="red">Yes</v-btn>
            </div>

        </v-card>
    </v-dialog>
    <!-- Delete dialog -->
</template>

<script>
import axios from 'axios';

export default {
    name: 'ManageCountryState',
    data() {
        return {
            options: [
                'Country',
                'State',
            ],

            type: null,

            tableLoading: true,

            countryHeaders: [
                { title: 'Name', key: 'name', align: 'center' },
                { title: 'Actions', key: 'action', sortable: false, align: 'center' },
            ],

            statesHeaders: [
                { title: 'Country', key: 'country', align: 'center' },
                { title: 'Name', key: 'name', align: 'center' },
                { title: 'Actions', key: 'action', sortable: false, align: 'center' },
            ],

            items: [],
            countries: [],
            states: [],

            countryDialog: false,
            addStateDialog: false,

            addingCountryName: null,

            addingStateCountryName: null,
            addingStateName: null,

            rules: [
                v => !!v || 'Required',
                v => (v && v.length <= 30) || 'Name must be less than 30 characters',
                v => (v && v.length >= 3) || 'Name must be more than 3 characters',
                v => /^[a-zA-Z ]*$/.test(v) || 'Only letters are allowed',
            ],

            form: false,
            editing: false,
            editingItem: {},

            dialogDelete: false,
            deleteItem: null,

            errorContent: null,

        };
    },

    watch: {
        type() {
            this.handleChange();
        }
    },

    methods: {

        handleChange() {
            if (this.type === 'Country') {
                this.fetchCountries();
            } else if (this.type === 'State') {
                this.fetchStates();
            }
        },


        addItem() {
            if (this.type === 'Country') {
                this.countryDialog = true;
            } else if (this.type === 'State') {
                this.addStateDialog = true;
            }
        },

        // Country

        async fetchCountries() {
            this.tableLoading = true;
            try {
                const response = await axios.get('api/countries/get/');
                this.countries = response.data;
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
            this.tableLoading = false;
        },


        async addEditCountry() {

            try {
                await axios.post('api/countries/add/', {
                    name: this.addingCountryName,
                });
                this.$store.dispatch('triggerAlert', { message: 'Country added', type: 'success' });
                this.fetchCountries();
            } catch (error) {
                const response = error.response;
                this.$store.dispatch('triggerAlert', { message: response.data.error, type: 'error' });
            }

            this.countryDialog = false;
            this.type = 'Country';
            this.stateName = null;

        },

        closeCountryDialog() {
            this.countryDialog = false;
            this.type = 'Country';
            this.addingCountryName = null;
            this.editing = false;
        },
        // Country


        // States

        async fetchStates() {
            this.tableLoading = true;
            try {
                const response = await axios.get('api/states/get/');
                this.states = response.data;
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
            this.tableLoading = false;
        },

        async addEditState() {
            if (this.editing) {
                try {
                    await axios.put(`api/states/edit/${this.editingItem.id}/`, {
                        name: this.addingStateName,
                        country: this.addingStateCountryName,
                    });
                    this.$store.dispatch('triggerAlert', { message: 'State edited', type: 'success' });
                    this.fetchStates();
                } catch (error) {
                    this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
                }
                this.addStateDialog = false;
                this.type = 'State';
                this.addingStateCountryName = null;
                this.addingStateName = null;
                this.editing = false;
            }
            else {
                try {
                    await axios.post('api/states/add/', {
                        name: this.addingStateName,
                        country: this.addingStateCountryName,
                    });
                    this.$store.dispatch('triggerAlert', { message: 'State added', type: 'success' });
                    this.fetchStates();

                } catch (error) {
                    const response = error.response;
                    this.$store.dispatch('triggerAlert', { message: response.data.error, type: 'error' });
                }
                this.addStateDialog = false;
                this.type = 'State';
                this.addingStateCountryName = null;
                this.addingStateName = null;
            }
        },

        closeStateDialog() {
            this.addStateDialog = false;
            this.type = 'State';
            this.addingStateCountryName = null;
            this.addingStateName = null;
            this.editing = false;
        },
        // States


        // Edit item
        editItem(item) {
            this.editing = true;
            this.addStateDialog = true;
            this.editingItem = {
                id: item.id,
                name: item.name,
                country: item.country,
            }
            this.addingStateCountryName = item.country;
            this.addingStateName = item.name;


        },
        // Edit item

        // Delete confirm
        deleteConfirm(item) {
            this.dialogDelete = true;
            this.deleteItem = item;
        },
        // Delete confirm

        // Delete item
        async delteItem(item) {
            if (this.type == 'Country') {
                try {
                    await axios.delete(`api/countries/delete/${item.name}/`);
                    this.$store.dispatch('triggerAlert', { message: 'Country deleted', type: 'success' });
                    this.fetchCountries();
                } catch (error) {
                    this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
                }

            } else if (this.type == 'State') {
                try {
                    await axios.delete(`api/states/delete/${item.id}/`);
                    this.$store.dispatch('triggerAlert', { message: 'State deleted', type: 'success' });
                    this.fetchStates();
                } catch (error) {
                    this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
                }
            }
            this.dialogDelete = false;
        },
        // Delete item

    }

};
</script>
