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
            creatorUsername: '',
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
            this.title = '';
            this.content = '';
        },
        // Close dialog


        // Send message
        async addPost() {
            const data = {
                'target': this.target,
                'title': this.title,
                'content': this.content,
            }
            
            console.log(data);
            this.loading = false;
            this.close();
        },
        // Send message


    },

}
</script>