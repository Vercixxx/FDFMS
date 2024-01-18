<template>

    <v-card>
        <v-form class="pa-5">
            <v-autocomplete :items="['a','b']" label="Select car" v-model="car"></v-autocomplete>
        </v-form>
    </v-card>

</template>

<script>
export default {
    name: 'DailyReport',
    data() {
        return {

        }
    },
    methods: {

    },
    mounted() {

    }
}
</script>
