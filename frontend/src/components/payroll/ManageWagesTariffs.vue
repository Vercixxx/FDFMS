<template>
  <div>

    <h4>
      Manage wages tariffs
    </h4>

    <v-btn class="my-5" variant="tonal" prepend-icon="mdi-plus" color="teal" @click="tariffDialog = true">Add new
      tariff</v-btn>

    <v-data-table :items="tariffs" :headers="headers" :loading="loading" no-data-text="There isn't any tariffs yet"
      show-current-page  density="compact">


      <!-- Loading -->
      <template v-slot:loading>
        <v-skeleton-loader type="table-row@5"></v-skeleton-loader>
      </template>
      <!-- Loading -->

      <template v-slot:item.action="{ item }">

        <v-btn variant="plain" color="green" @click="editItem(item)">
          <v-icon icon="mdi-pencil-outline" class="text-h5"></v-icon>
          <v-tooltip activator="parent" location="top">Edit {{ item.name }}</v-tooltip>
        </v-btn>

        <v-btn variant="plain" color="red" @click="deleteItem(item)">
          <v-icon icon="mdi-delete-empty" class="text-h5"></v-icon>
          <v-tooltip activator="parent" location="top">Delete {{ item.name }}</v-tooltip>
        </v-btn>

      </template>

    </v-data-table>



    <!-- Tariff -->
    <v-dialog persistent v-model="tariffDialog" fullscreen :scrim="false" transition="dialog-bottom-transition">
      <v-card>
        <v-card-title class="bg-deep-purple-lighten-1">
          <v-row>
            <v-col class="text-h5">
              {{ editing ? 'Edit' : 'Add new' }} wage tariff
            </v-col>
            <v-col align="end">
              <v-btn variant="outlined" color="red" @click="closeAddEditDialog()" icon="mdi-close">
              </v-btn>
            </v-col>
          </v-row>
        </v-card-title>

        <v-card-text>
          <v-form v-model="form">
            <v-row>
              <v-col cols="12" sm="6" v-for="field in fields" :key="field.key">
                <v-text-field v-model="tariff[field.key]" :label="field.label" variant="underlined" :rules="field.rules"
                  :hint="field.hint"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-select v-model="tariff[startingDayOfNewPeriod.key]"
                  :items="['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']"
                  :label="startingDayOfNewPeriod.label" variant="underlined"
                  :rules="startingDayOfNewPeriod.rules"></v-select>
              </v-col>
            </v-row>
          </v-form>

        </v-card-text>

        <v-card-actions>
          <v-btn color="success" block :disabled="!form" @click="addSaveTariff()"
            :text="editing ? 'Save' : 'Add'"></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <!-- Tariff -->




    <!-- Confirm delte -->
    <v-dialog v-model="dialogDelete" width="500" persistent>
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

          You are trying to delete
          <span class='fw-bolder'>
            {{ deletingItem.name }} tariff
          </span>
          , this operation is <span class="fw-bold">irreversible</span>.
          Are you sure?

        </div>
        <hr>

        <div class="justify-center d-flex align-items-center mb-3">
          <v-btn variant="outlined" width="150" class="mr-5" @click="dialogDelete = false">No</v-btn>
          <v-btn width="150" @click="deleteTariff()" color="red">
            <v-icon icon="mdi-delete-empty"></v-icon>
            Yes
          </v-btn>
        </div>

      </v-card>
    </v-dialog>
    <!-- Confirm delte -->

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ManageDriverSalaries',
  data() {
    return {
      loading: true,
      form: false,

      tariffDialog: false,

      dialogDelete: false,
      deletingItem: {
        id: null,
        name: null,
      },

      showCard: false,

      editing: false,

      tariffs: [],
      tariff: {
        name: null,
        basic_hourly_rate: null,
        orders_bonus: null,
        fuel_bonus: null,
        starting_new_billing_period: null,
      },

      fields:
        [
          {
            key: 'name',
            label: 'Name',
            rules: [
              v => !!v || 'Name is required',
              v => v.length <= 20 || 'Maximum length is 50 characters',
            ]
          },
          {
            key: 'basic_hourly_rate',
            label: 'Hourly rate',
            hint: 'Seperate with a dot, e.g 12.50',
            rules: [
              v => !!v || 'Hourly rate is required',
              v => /^(\d{1,4}(\.\d{0,2})?)?$/.test(v) || 'Invalid format. Only numbers and dot allowed, maximum length is 4 characters',
            ]
          },
          {
            key: 'orders_bonus',
            label: 'Exceeded orders bonus',
            hint: 'Seperate with a dot, e.g 12.50',
            rules: [
              v => !!v || 'Exceeded orders bonus is required',
              v => /^(\d{1,4}(\.\d{0,2})?)?$/.test(v) || 'Invalid format. Only numbers and dot allowed, maximum length is 4 characters',
            ]
          },
          {
            key: 'fuel_bonus',
            label: 'Fuel bonus',
            hint: 'Seperate with a dot, e.g 12.50',
            rules: [
              v => !!v || 'Fuel bonus is required',
              v => /^(\d{1,4}(\.\d{0,2})?)?$/.test(v) || 'Invalid format. Only numbers and dot allowed, maximum length is 4 characters',
            ]
          },
        ],

      startingDayOfNewPeriod:
      {
        key: 'starting_new_billing_period',
        label: 'Day of starting new billing period',
        rules: [
          v => !!v || 'Fuel bonus is required',
        ]
      },


      headers: [
        { title: 'Name', key: 'name', align: 'center' },
        { title: 'Hourly rate', key: 'basic_hourly_rate', align: 'center' },
        { title: 'Exceeded orders bonus', key: 'orders_bonus', align: 'center' },
        { title: 'Fuel bonus', key: 'fuel_bonus', align: 'center' },
        { title: 'Starting day of new period', sortable: false, key: 'starting_new_billing_period', align: 'center' },
        { title: 'Actions', key: 'action', sortable: false, align: 'center' },
      ],

    };
  },

  methods: {

    // Get all tariffs
    async fetchTariffs() {
      this.loading = true;
      try {
        const response = await axios.get('api/drivers/wage_tariff/get/all/')
        this.tariffs = response.data;
      } catch (error) {
        this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
      }
      this.loading = false;
    },
    // Get all tariffs

    showAddNew() {
      this.showCard = true;
    },

    // Close add/edit dialog
    closeAddEditDialog() {
      this.tariff = {
        name: null,
        basic_hourly_rate: null,
        orders_bonus: null,
        fuel_bonus: null,
        starting_new_billing_period: null,
      };
      this.editing = false;
      this.tariffDialog = false;
    },
    // Close add/edit dialog


    // Edit item
    editItem(item) {
      this.tariff = item;
      this.editing = true;
      this.tariffDialog = true;
    },
    // Edit item

    // Delete item confirm
    deleteItem(item) {
      this.deletingItem = {
        id: item.id,
        name: item.name,
      }
      this.dialogDelete = true;
    },
    // Delete item confirm



    // Delete item
    async deleteTariff() {
      try {
        const response = await axios.delete(`api/drivers/wage_tariff/delete/${this.deletingItem.id}/`);
        this.dialogDelete = false;
        this.$store.dispatch('triggerAlert', { message: 'Tariff deleted', type: 'success' });
        this.fetchTariffs();
      } catch (error) {
        this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
      }
    },
    // Delete item



    // Add or save tariff
    async addSaveTariff() {
      if (this.editing) {
        try {
          const response = await axios.put(`api/drivers/wage_tariff/edit/${this.tariff.id}/`, this.tariff);
          this.$store.dispatch('triggerAlert', { message: 'Tariff updated', type: 'success' });
          this.closeAddEditDialog();
          this.fetchTariffs();
        } catch (error) {
          this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });

        }
      }
      else {
        try {
          const response = await axios.post('api/drivers/wage_tariff/create/', this.tariff);
          this.$store.dispatch('triggerAlert', { message: 'Tariff added', type: 'success' });
          this.closeAddEditDialog();
          this.fetchTariffs();
        } catch (error) {
          this.$store.dispatch('triggerAlert', { message: 'Error, please try again', type: 'error' });
        }
      }
    },
    // Add or save tariff

  },

  mounted() {
    this.fetchTariffs();
  },
};
</script>

