<template>
  <div>
    <h1>Reports for {{ driver.first_name + ' ' + driver.last_name }}</h1>

    <v-select v-model="reportType" :items="['Billing period', 'Select settlement time manually']"
      label="Select report type" variant="underlined"></v-select>

    <v-container v-if="reportType == 'Select settlement time manually'">

      <v-row>

        <v-col cols="12" sm="6">
          <v-text-field v-model="startDate" label="Start date" type="date"></v-text-field>
        </v-col>

        <v-col cols="12" sm="6">
          <v-text-field v-model="endDate" label="End date" type="date"></v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col align="center">
          <v-btn :variant="!datesValid ? 'outlined' : 'tonal'" @click="generateReport()" append-icon="mdi-file-account"
            :disabled="!datesValid" size="large">
            Generate report
          </v-btn>
        </v-col>
      </v-row>

    </v-container>

    <v-container v-else>
      <v-btn block size="large" :variant="!datesValid ? 'outlined' : 'tonal'" @click="generateReport()"
        append-icon="mdi-file-account" :disabled="!datesValid">
        Generate report
      </v-btn>
    </v-container>


    <v-overlay :model-value="overlay" class="align-center justify-center" persistent>
      <v-progress-circular color="primary" indeterminate size="64"></v-progress-circular>
    </v-overlay>

  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      driver: null,

      reportType: null,

      startDate: null,
      endDate: null,

      overlay: false,

    };
  },

  methods: {

    // Generate report
    async generateReport() {
      // this.overlay = true;

      const response = await axios.get(`api/drivers/generate_report/${this.driver.username}`, {
        params: {
          start_date: this.startDate,
          end_date: this.endDate,
        },
        responseType: 'blob' // to tell axios to download the response as a blob
      });

      // Create a new Blob object from the response data
      const blob = new Blob([response.data], { type: 'text/csv' });

      // Create a new object URL for the blob
      const url = window.URL.createObjectURL(blob);

      // Create a new link element
      const link = document.createElement('a');

      // Set the href and download attributes of the link
      link.href = url;
      link.setAttribute('download', `${this.driver.username}_${this.startDate}-${this.endDate}.csv`);

      // Append the link to the body
      document.body.appendChild(link);

      // Programmatically click the link to start the download
      link.click();

      // Remove the link from the body
      document.body.removeChild(link);

      this.overlay = false;

    },
    // Generate report


  },

  computed: {
    datesValid() {
      return this.startDate && this.endDate;
    },
  },

  created() {
    this.driver = this.$store.getters.busData;
  },

  mounted() {


  },
};
</script>
