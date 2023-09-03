
<template>
  <div id="wrapper">
    <ColorModes /> <!-- ColorModes button -->
    


    <router-view/>
  </div>
</template>

<script>
import './color-modes.js';
import ColorModes from './components/ColorModes.vue'; // Import ColorModes

export default {
  name: 'App',
  components: {
    ColorModes,
  },
};
</script>

<style lang="scss">

</style>
