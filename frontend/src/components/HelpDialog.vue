<template>
    <v-row justify="center">
        <v-dialog v-model="showDialog" width="auto">
            <v-card>
                <v-card-title align="center">
                    Help
                </v-card-title>
                <v-card-text class="text-danger">
                    Not implemented yet 
                    <v-icon icon="mdi-emoticon-sad-outline"></v-icon>
                </v-card-text>
                <v-card-actions>
                    <v-btn color="primary" block @click="showDialog = false">Close</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>


<script>
import useEventsBus from '../plugins/eventBus.js'
import { watch } from "vue";

export default {
    name: 'HelpDialog',


    data() {
        return {
            showDialog: false,

        }
    },

    mounted() {
        const { bus } = useEventsBus();
        watch(
            () => [bus.value.get('showHelpDialog')],
            ([showHelpDialog]) => {
                if (showHelpDialog) {
                    this.showDialog = true;
                }
            }
        );

    },
}
</script>