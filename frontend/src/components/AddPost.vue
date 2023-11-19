<template>
    <v-row justify="center">
        <v-dialog v-model="dialog" persistent width="800">

            <v-form v-model="form" @submit.prevent="onSubmit">

                <v-card class="pa-5">
                    <v-card-title class="text-h5">
                        Add post
                    </v-card-title>
                    <v-card-text>

                        <!-- Destiny -->
                        <v-select label="Choose destiny" variant="solo-filled" :items="targetOptions" v-model="target"
                            :disabled="target"></v-select>
                        <!-- Destiny -->


                        <!-- Title -->
                        <span>
                            <v-tooltip v-if="!target" activator="parent" location="bottom" no-overflow>
                                Choose destiny first
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
                                Choose destiny first
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
import { watch } from "vue";
const { emit } = useEventsBus()
export default {
    data() {
        return {
            dialog: false,
            loading: false,
            form: false,

            targetOptions: [
                'Users',
                'Drivers'
            ],
            target: null,
            creatorId: '',
            title: '',
            content: '',
        }
    },



    mounted() {
        const { bus } = useEventsBus();
        watch(
            () => [bus.value.get('showAddPost')],
            ([showAddPost]) => {
                if (showAddPost) {
                    this.dialog = true
                }
            }
        );

        this.creatorId = this.$store.getters.responseData.id;
    },

    methods: {

        onSubmit() {
            if (!this.form) return

            this.loading = true
            this.addPost()
        },
        required(v) {
            return !!v || 'Field is required'
        },


        // Close dialog
        close() {
            this.dialog = false;
            this.target = null;
            this.loading = false,
            this.title = '';
            this.content = '';
        },
        // Close dialog


        // Send message
        async addPost() {
            const data = {
                'author': this.creatorId,
                'title': this.title,
                'content': this.content,
            }
            const target = this.target;

            const response = await axios.post(`api/posts/create/${target}`, data);
            this.loading = false;

            if (response.status === 201) {
                this.close();
                emit('forceReload', '');

                const messageData = {
                    message: response.data.message,
                    type: 'success'
                };

                localStorage.setItem('message', JSON.stringify(messageData));
                emit('message', '');

            }

            else {
                const messageData = {
                    message: response.error,
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