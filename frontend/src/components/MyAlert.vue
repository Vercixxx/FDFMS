<template>
    <!-- Snackbar -->
    <v-snackbar v-model="alert" :timeout="3000" location="top" :color="snackContent.type" style="position: fixed; top: 8vh;"
        rounded="pill" variant="elevated">

        <span class="font-weight-bold">
            {{ snackContent.message }}
        </span>

        <template v-slot:actions>
            <v-btn @click="alert = false" variant="plain" class="ma-1">
                Close
            </v-btn>
        </template>
    </v-snackbar>
    <!-- Snackbar -->
</template>

<script>
export default {
    name: 'MyAlert',

    data() {
        return {
            alert: false,
            snackContent: {},
        };
    },

    computed: {
        alertData() {
            return this.$store.state.alertData;
        },
    },

    watch: {
        alertData(newData) {
            if (newData.show) {
                this.alert = true;
                this.snackContent = newData;
            }
        },
    },
};
</script>
