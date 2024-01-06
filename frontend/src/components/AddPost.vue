<template>
    <v-row justify="center">
        <v-dialog v-model="dialog" persistent width="800">

            <v-form v-model="form" @submit.prevent="onSubmit">

                <v-card class="pa-5">
                    <v-card-title class="text-h5 font-weight-bold">
                        Add post
                    </v-card-title>
                    <v-card-text>

                        <!-- Reciver -->
                        <v-select label="Choose Reciver" variant="solo-filled" :items="targetOptions" v-model="target"
                            :disabled="target"></v-select>
                        <!-- Reciver -->


                        <!-- Title -->
                        <span>
                            <v-tooltip v-if="!target" activator="parent" location="bottom" no-overflow>
                                Choose Reciver first
                            </v-tooltip>
                            <span>
                                <v-textarea clearable auto-grow counter rows="1" :disabled="!target" label="Title" variant="solo-filled" v-model="title"
                                    :readonly="loading" :rules="[v => v.length <= maxTitleLen || 'Max 200 characters', required]">
                                </v-textarea>

                            </span>
                        </span>
                        <!-- Title -->




                        <!-- Content -->
                        <span>
                            <v-tooltip v-if="!target" activator="parent" location="bottom" no-overflow>
                                Choose Reciver first
                            </v-tooltip>
                            <span>
                                <v-textarea clearable auto-grow counter rows="5" :disabled="!target" label="Content" variant="solo-filled" v-model="content"
                                    :readonly="loading" :rules="[v => v.length <= maxContentLen || 'Max 400 characters', required]"></v-textarea>
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

            maxTitleLen: 200,
            content: '',
            contentCounter: 0,
            maxContentLen: 400,
        }
    },



    computed: {
        titleCounter() {
            return this.title.length;
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

        this.creatorId = this.$store.getters.userData.id;
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