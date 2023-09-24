<template>
    <v-app>
        <div class="rounded p-2 m-2 bg-success">

            <!-- Title -->
            <p class="display-5 fst-italic mb-4 px-2">
                <span class="fw-bold">F</span>ood
                <span class="fw-bold">D</span>elivery
                <span class="fw-bold">F</span>leet
                <span class="fw-bold">M</span>anagement
                <span class="fw-bold">S</span>ystem
                - Log in
            </p>


        </div>




        <v-main>


            <v-container fluid fill-height>
                <v-row align="center" justify="center">
                    <v-col cols="12" sm="8" md="6">
                        <v-card>
                            <v-sheet rounded>
                                <v-card class="mx-auto px-6 py-8" max-width="400">
                                    <v-form v-model="form" @submit.prevent="onSubmit">
                                        <v-text-field v-model="email" :readonly="loading" :rules="[required]" class="mb-2"
                                            clearable label="Email"></v-text-field>

                                        <v-text-field v-model="password" :readonly="loading" :rules="[required]" clearable
                                            label="Password" placeholder="Enter your password"></v-text-field>

                                        <br>

                                        <v-btn :disabled="!form" 
                                        :loading="loading" 
                                        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                        block color="success" 
                                        size="large"
                                        type="submit" v
                                        ariant="elevated">
                                            Sign In
                                        </v-btn>
                                    </v-form>
                                </v-card>
                            </v-sheet>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>


        </v-main>

        <template v-slot:append>
            <div class="pa-2">
                <v-btn variant="outlined" @click="toggleTheme">Toogle dark mode</v-btn>
            </div>
        </template>





    </v-app>
</template>

<script setup>
import { useTheme } from 'vuetify'

const theme = useTheme()


function toggleTheme() {
    theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
}
</script>


<script>
  export default {
    data: () => ({
      form: false,
      email: null,
      password: null,
      loading: false,
    }),

    methods: {
      onSubmit () {
        if (!this.form) return

        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },
      required (v) {
        return !!v || 'Field is required'
      },
    },
  }
</script>