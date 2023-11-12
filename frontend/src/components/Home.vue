<template>
    <v-row>
        <v-col class="text-h5">
            {{ date }}
        </v-col>
        <v-col>

        </v-col>

    </v-row>

    



    <article class="p-2 m-2 border rounded mb-10">
        <h3>
            Hi from
            <span class="badge bg-secondary">
                <v-icon icon="mdi-apple"></v-icon>
                <v-icon icon="mdi-apple-ios"></v-icon>
            </span>
        </h3>
        <hr>

        <div class="text-wrap fs-5">
            <v-icon icon="mdi-android" class="text-h1"></v-icon>
            Content
        </div>

    </article>

    <article class="p-2 m-2 border rounded">
        <h3>
            Welcome to home page
        </h3>
        <hr>

        <div class="text-wrap fs-5">
            Hi, it's an honor to present you home page of <span class="fw-bolder">FDFMS</span> system.
            Check options in menu to proceed some actions.
        </div>

    </article>
</template>

<script>
export default {
    data() {
        return {
            date: '',
        }
    },



    mounted() {
        this.getDate();

        this.intervalId = setInterval(() => {
            this.getDate();
        }, 60000);
    },


    beforeDestroy() {
        clearInterval(this.intervalId);
    },


    methods: {
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
    },


}
</script>