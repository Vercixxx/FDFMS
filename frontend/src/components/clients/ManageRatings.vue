<template>
    <div>

        <v-btn @click="addEditDialog = true" color="primary" append-icon="mdi-plus">Add Rating</v-btn>

        <v-data-table :items="ratings" :headers="headers" :items-per-page="25">

            <template v-slot:item.actions="{ item }">
                <v-btn @click="editRating(item)" variant="plain">
                    <v-icon icon="mdi-pencil" color="success" class="text-h5"></v-icon>
                    <v-tooltip activator="parent" location="top">Edit {{ item.rating }}</v-tooltip>
                </v-btn>
                <v-btn @click="deleteRating(item.id)" color="danger" icon="mdi-delete" variant="plain">
                    <v-icon icon="mdi-delete" color="danger" class="text-h5"></v-icon>
                    <v-tooltip activator="parent" location="top">Delete {{ item.rating }}</v-tooltip>
                </v-btn>
            </template>

        </v-data-table>

        <v-dialog v-model="addEditDialog" persistent>
            <v-card>
                <v-card-title>
                    <v-row>
                        <v-col cols="2"></v-col>
                        <v-col cols="8" align="center">
                            <span class="headline">{{ editMode ? 'Edit' : 'Add' }} Rating</span>
                        </v-col>
                        <v-col cols="2" align="end">
                            <v-btn icon="mdi-close" @click="closeDialog()"></v-btn>
                        </v-col>
                    </v-row>
                </v-card-title>

                <v-card-text>
                    <v-form v-model="form">
                        <v-row>
                            <v-col cols="12" sm="6">
                                <v-text-field v-model="rating.rating" label="Rating" required type="number"
                                    :rules="rules.rating"></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6">
                                <v-text-field v-model="rating.day" label="Day" required type="number"
                                    :rules="rules.day"></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6">
                                <v-text-field v-model="rating.hour" label="Hour" required
                                    :rules="rules.hour"></v-text-field>
                            </v-col>
                        </v-row>
                    </v-form>
                </v-card-text>

                <v-card-actions>

                    <v-btn block @click="addEditRating()" color="success" :disabled="!form">{{ editMode ? 'Save' :
                        'Add'
                    }}</v-btn>
                </v-card-actions>

            </v-card>
        </v-dialog>



    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ManageRatings',

    data() {
        return {


            addEditDialog: false,
            editMode: false,
            form: false,
            rating: {
                id: '',
                rating: '',
                day: '',
                hour: ''
            },
            ratings: [],
            headers: [
                { title: 'Id', key: 'id', align: 'center', sortable: false },
                { title: 'Rating', key: 'rating', align: 'center', sortable: false },
                { title: 'Day', key: 'day', align: 'center', sortable: false },
                { title: 'Hour', key: 'hour', align: 'center', sortable: false },
                { title: 'Actions', key: 'actions', align: 'center', sortable: false }
            ],

            // Rules
            rules: {
                rating: [
                    v => !!v || 'Rating is required',
                    v => !isNaN(v) || 'Must be a number',
                    v => (v >= 1 && v <= 5) || 'Rating must be between 1 and 5',
                ],
                day: [
                    v => !!v || 'Day is required',
                    v => !isNaN(v) || 'Must be a number',
                    v => (v >= 1 && v <= 31) || 'Day must be between 1 and 31',
                ],
                hour: [
                    v => !!v || 'Hour is required',
                    v => /^([0-1][0-9]|2[0-3]):[0-5][0-9]$/.test(v) || 'Hour must be in the format HH:MM',
                ],
            },

        }
    },

    mounted() {
        this.getRatings()
    },

    methods: {

        // Get ratings
        async getRatings() {
            try {
                const response = await axios.get('api/drivers/ratings/get/ratings/')
                this.ratings = response.data
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
        },
        // Get ratings



        // Edit rating
        editRating(object) {
            this.editMode = true
            this.addEditDialog = true
            this.rating = {
                id: object.id,
                rating: object.rating,
                day: object.day,
                hour: object.hour,
            }
        },
        // Edit rating



        // Close dialog
        closeDialog() {
            this.addEditDialog = false
            this.editMode = false
        },
        // Close dialog



        // Add or edit rating
        async addEditRating() {
            try {
                if (this.editMode) {
                    const response = await axios.put(`api/drivers/ratings/edit/${this.rating.id}/`, this.rating)
                    this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'success' });
                } else {
                    const response = await axios.post('api/drivers/ratings/add/', this.rating)
                    this.$store.dispatch('triggerAlert', { message: response.data.message, type: 'success' });
                }
                this.getRatings()
                this.addEditDialog = false
                this.editMode = false
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
        },
        // Add or edit rating



        // Delete rating
        async deleteRating(id) {
            try {
                const response = await axios.delete(`api/drivers/ratings/delete/${id}/`)
                this.$store.dispatch('triggerAlert', { message: 'Successfully deleted', type: 'success' });
                this.getRatings()
            } catch (error) {
                this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
            }
        }
        // Delete rating
    }
}
</script>

