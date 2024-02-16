<template>
    <!-- Snackbar -->
    <v-snackbar v-model="alert" location="top" :timeout="time" :color="snackContent.type" style="position: fixed; top: 8vh;" rounded="pill"
        variant="elevated">

        <v-progress-linear v-model="value" :buffer-value="bufferValue" rounded color="white"></v-progress-linear>

        <span class="font-weight-bold">
            {{ snackContent.message }}
        </span>

        <template v-slot:actions>
            <v-btn @click="closeAlert()" variant="plain" class="ma-1">
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
            time: 5000,

            value: 0,
            bufferValue: 0,
            interval: 0,
            
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
                this.startBuffer()


            }
        },
    },


    methods: {
        closeAlert() {
            this.value = 0
            this.bufferValue = 0
            this.alert = false;
            clearInterval(this.interval)
        },

        startBuffer() {
            this.interval = setInterval(() => {
                this.value += 1.85
                this.bufferValue +=  1.85
            }, 90)
        },
    },
};
</script>
