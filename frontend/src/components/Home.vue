<template>

  <!-- Variant -->
  <v-row v-if="logged_role !== 'Driver'">
    <v-col cols="5">
      <v-select class="ma-5" label="Choose home variant" v-model="version"
        :items="versions" variant="outlined"></v-select>
    </v-col>
    <v-col align="end">
      <v-btn variant="plain" prepend-icon="mdi-plus" class="bg-teal-darken-2" @click="addPost()">
        Add post</v-btn>
    </v-col>
  </v-row>
  <!-- Variant -->

  <p v-if="posts.length === 0">
    No data
  </p>

  <v-card v-for="post in posts" :key="post.id" class="mx-auto my-8 pa-5 border-2">
    <v-card-item>
      <v-card-title class="text-md-h5 text-lg-h4" :class="isDarkModeEnabled ? 'text-teal-lighten-2' : 'text-teal-darken-3'
        ">
        <v-row>
          <v-col class="text-wrap font-weight-bold">
            {{ post.title }}
          </v-col>
          <v-col align="end">
            <!-- Detele button -->
            <v-btn v-if="post.author_username === logged_username ||
              logged_role === 'Administrator'
              " variant="plain" icon="mdi-delete" color="red" @click="deletePostDialog(post.id)"></v-btn>
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

  <v-pagination v-if="posts.length > 0" v-model="page" class="my-3" :length="pageAmount" :total-visible="5" @next="nextPage()"
    @prev="prevPage()"></v-pagination>

  <!-- Delete post dialog -->
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
        You are trying to delete post id
        <span class="fw-bolder">
          {{ deleteId }}
        </span>
        , this operation is <span class="fw-bold">irreversible</span>. Are you
        sure?
      </div>
      <hr />

      <div class="justify-center d-flex align-items-center mb-3">
        <v-btn variant="outlined" width="150" class="mr-5" @click="dialogDelete = false">No</v-btn>
        <v-btn width="150" @click="deletePost()" color="red">Yes</v-btn>
      </div>
    </v-card>
  </v-dialog>
  <!-- Delete post dialog -->
</template>

<script>
import axios from "axios";
import useEventsBus from "../plugins/eventBus.js";
const { emit } = useEventsBus();
import { watch } from "vue";
import { useTheme } from "vuetify";

export default {
  data() {
    return {
      posts: [],
      logged_username: "",
      logged_role: "",
      isDarkModeEnabled: false,

      versions: ['Users', 'Drivers'],
      version: '',

      page: 1,
      pageAmount: 0,
      prev: null,
      next: null,

      dialogDelete: false,
      deleteId: null,
    };
  },


  watch: {
    version: 'handleVersionChange',
  },

  mounted() {

    this.logged_username = this.$store.getters.userData.username;
    this.logged_role = this.$store.getters.userData.user_role;

    if (this.logged_role === 'Driver') {
      this.version = 'Driver';
    }
    else {
      this.version = 'Users'
    }
    this.getPosts();


    // Dark mode
    const { bus } = useEventsBus();

    watch(
      () => bus.value.get("theme"),
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

    // Add post
    addPost() {
      emit("showAddPost", true);
    },
    // Add post

    // Delete post
    deletePostDialog(postId) {
      this.dialogDelete = true;
      this.deleteId = postId;
    },

    async deletePost() {
      this.dialogDelete = false;
      try {
        const response = await axios.delete(
          `api/posts/delete/${this.version}/${this.deleteId}/`
        );
        emit("forceReload", "");
        this.$store.dispatch('triggerAlert', { message: 'Succesfully deleted post', type: 'success' });
      } catch (error) {
        this.$store.dispatch('triggerAlert', { message: error, type: 'error' });
        }
    },
    // Delete post

    // Get posts
    async getPosts(url) {

      let response;

      if (this.version === 'Users') {
        response = await axios.get(url || `api/posts/get/${this.version}/`);
      } else {
        response = await axios.get(url || `api/posts/get/${this.version}/`);
      }

      this.posts = response.data.results;
      this.pageAmount = response.data.total_pages;
      this.prev = response.data.previous;
      this.next = response.data.next;
    },

    handleVersionChange() {
      this.getPosts();
    },
    // Get posts

    // Previous page
    async prevPage() {
      await this.getPosts(this.prev);
    },
    // Previous page

    // Next page
    async nextPage() {
      await this.getPosts(this.next);
    },
    // Next page
  },
};
</script>
