<template>
  <span class="">
    <b-progress
      height="20px"
     
      style="background-color:grey; border-radius:100px; "
      
    >
      <b-progress-bar class="p-1" :value="value" :style="couleur(value)">{{
        value + " %"
      }}</b-progress-bar>
    </b-progress>
  </span>
</template>

<script>
export default {
  props: ["value"],
  data() {
    return {
      items: []
    };
  },
  methods: {
    couleur(x) {
      if (x < 20) {
        return "background-color:#1dae26!important;width:";
      } else if (x >= 20 && x <= 50) {
        return "background-color:#94b77d!important;width:";
      } else if (x > 50 && x < 60) {
        return " background-color:#fcbf00!important;width:";
      } else {
        return "background-color:red!important;width:";
      }
    }
  }
};
</script>