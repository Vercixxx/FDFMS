<!-- <template>
  <div>
    <b-alert show :dismiss-sec="dismissSecs" dismissible fade>
      This alert will dismiss after {{ dismissSecs }} seconds...
    </b-alert>

    <b-button @click="showAlert" variant="info" class="m-1">
      Show alert with count-down timer
    </b-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dismissSecs: 5,
    };
  },
  methods: {
    showAlert() {
      // Pokaż alert
      this.$bvToast.toast("This is a timed alert!", {
        title: "Alert",
        variant: "info",
        solid: true,
        noCloseButton: true,
        appendToast: true,
      });

      // Rozpocznij odliczanie
      let countDown = this.dismissSecs;
      const intervalId = setInterval(() => {
        if (countDown <= 0) {
          clearInterval(intervalId);
          this.$bvToast.hide("my-toast");
        } else {
          countDown--;
        }
      }, 1000);
    },
  },
};
</script> -->
