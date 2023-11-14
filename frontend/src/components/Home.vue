<template>
    <v-row>

        <v-col class="text-h5">
            {{ date }}
        </v-col>
        <v-col align="end">
            <v-btn variant="plain" prepend-icon="mdi-plus" class="bg-teal-darken-2" @click="addPost()"> Add post</v-btn>
        </v-col>

    </v-row>


    <v-card v-for="post in posts" :key="post.id" class="mx-auto my-8 pa-5 border-2">


        <v-card-item>
            <v-card-title class="text-h4 text-md-h5 text-lg-h4"
                :class="isDarkModeEnabled ? 'text-teal-lighten-2' : 'text-teal-darken-3'">
                <v-row>
                    <v-col class="text-wrap">
                        {{ post.title }}
                    </v-col>
                    <v-col align="end">
                        <!-- Detele button -->
                        <v-btn v-if="post.author_username === logged_username || logged_role === 'Administrator'"
                            variant="plain" icon="mdi-delete" color="red"></v-btn>
                        <!-- Detele button -->
                    </v-col>
                </v-row>
            </v-card-title>
            <v-card-subtitle>
                Added by {{ post.author_username }}, {{ post.posted_date }}
            </v-card-subtitle>
        </v-card-item>

        <v-card-text>
            {{ post.content }}
        </v-card-text>

    </v-card>


    <v-pagination v-model="page" class="my-4" :length="pageAmount" :total-visible="5"></v-pagination>
</template>


<script>
import axios from 'axios'
import useEventsBus from '../plugins/eventBus.js'
const { emit } = useEventsBus()
import { watch } from "vue";
import { useTheme } from 'vuetify'


export default {


    data() {
        return {
            date: '',
            posts: [],
            logged_username: '',
            logged_role: '',
            isDarkModeEnabled: false,

            page: 1,
            pageAmount: 25,

        }
    },


    mounted() {
        this.getDate();

        this.intervalId = setInterval(() => {
            this.getDate();
        }, 60000);

        this.getPosts();
        this.logged_username = this.$store.getters.responseData.username;
        this.logged_role = this.$store.getters.responseData.user_role;

        // Dark mode
        const { bus } = useEventsBus();

        watch(
            () => bus.value.get('theme'),
            (val) => {
                const [themeBus] = val ?? [];
                this.isDarkModeEnabled = themeBus;
            }
        );

        const theme = useTheme();
        this.isDarkModeEnabled = theme.global.current.value.dark;
        // Dark mode

    },


    beforeDestroy() {
        clearInterval(this.intervalId);
    },


    methods: {


        // Get date
        getDate() {
            const now = new Date();

            const daysOfWeek = ['Niedziela', 'Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota'];
            const dayOfWeek = daysOfWeek[now.getDay()];

            const hours = now.getHours();
            const minutes = now.getMinutes();

            const day = now.getDate();
            const month = now.getMonth() + 1
            const year = now.getFullYear();

            this.date = `${dayOfWeek}, ${hours}:${minutes < 10 ? '0' : ''}${minutes}, ${day}-${month}-${year}`;
        },
        // Get date



        // Add post
        addPost() {
            emit('showAddPost', true)
        },
        // Add post



        // Get posts
        async getPosts() {
            const response = await axios.get('api/posts/get/')
            console.log(response)
            this.posts = response.data
        },
        // Get posts
    },


}
</script>