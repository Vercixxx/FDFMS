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
      this.overlay = true;

      const response = await axios.get(`api/drivers/generate_report/${this.driver.username}`, {
        params: {
          start_date: this.startDate,
          end_date: this.endDate,
          monthly: this.reportType == 'Billing period',
          monthly_day: this.driver.tariff_starting_day,
        },
        responseType: 'blob'
      });

      const blob = new Blob([response.data], { type: 'text/csv' });
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `${this.driver.username}_${this.startDate}-${this.endDate}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

      this.overlay = false;

    },
    // Generate report


  },

  watch: {
    reportType(newReportType) {
      if (newReportType === 'Billing period') {
        let today = new Date();
        let month = today.getMonth();
        let year = today.getFullYear();

        let currentMonthDate = new Date(year, month + 1, this.driver.tariff_starting_day);
        let previousMonthDate = new Date(year, month , this.driver.tariff_starting_day);

        let currentMonthDateString = `${currentMonthDate.getFullYear()}-${currentMonthDate.getMonth() + 1}-${currentMonthDate.getDate()}`;
        let previousMonthDateString = `${previousMonthDate.getFullYear()}-${previousMonthDate.getMonth() + 1}-${previousMonthDate.getDate()}`;

        let result = `${previousMonthDateString} to ${currentMonthDateString}`;

        const message = `User ${this.driver.first_name} ${this.driver.last_name} has assigned tariff with name ${this.driver.tariff_name}. 
        The report will be generated for the period from ${result}`;

        this.$store.dispatch('triggerAlert', { message: message, type: 'teal' });
      }
    },
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
