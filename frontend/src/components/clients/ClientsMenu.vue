<template>
    <div>

        <v-menu transition="scale-transition">
            <template v-slot:activator="{ props }">
                <v-btn block color="success" v-bind="props" variant="tonal">
                    Restaurants
                </v-btn>
            </template>

            <v-list>
                <v-list-item>
                    <v-list-item-title>
                        <v-btn block @click="handleButtonClick('AddClientComponent')">
                            <span class="material-symbols-outlined">
                                add
                            </span>
                            Add
                        </v-btn>
                    </v-list-item-title>
                    <v-list-item-title>
                        <v-btn block @click="handleButtonClick('ModifyClientComponent')">
                            <span class="material-symbols-outlined">
                                edit
                            </span>
                            Modify
                        </v-btn>
                    </v-list-item-title>


                </v-list-item>
            </v-list>
        </v-menu>

    </div>
</template>
  
<script>
export default {
    methods: {
        handleButtonClick(functionName) {
            this.$root.changeCurrentComponent(functionName);
        },
    },

};
</script>
  