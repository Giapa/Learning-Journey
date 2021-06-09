<template>
  <div v-if="loading">
    <card-display :dimensions="['w-48', 'h-48']" :loop="5"
      >The unlucky numbers are:</card-display
    >
    <beat-loader
      loading="loading"
      color="black"
      class="my-10"
      v-if="loading"
    ></beat-loader>
    <card-display
      :dimensions="['w-36', 'h-36']"
      :loop="getNumbers"
      class="mt-10"
      >Your numbers</card-display
    >
  </div>
  <div v-else>You lost. What did you expect?</div>
</template>

<script>
import CardDisplay from "../components/CardDisplay.vue";
import BeatLoader from "vue-spinner/src/BeatLoader.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  components: { CardDisplay, BeatLoader },
  data() {
    return {
      loading: true,
      randomNumbers: [],
    };
  },
  methods: {
    ...mapActions(["deleteNumbers"]),
    async getUnluckuNumbers(inputs, timer) {
      for (const input of inputs) {
        await timer(4000);
        var randomNumber = Math.floor(Math.random() * 30) + 1;
        this.randomNumbers.push(randomNumber);
        input.placeholder = randomNumber;
      }
      this.loading = false;
      this.deleteNumbers();
      console.log(this.randomNumbers);
    },
  },
  mounted() {
    if (this.getNumbers.length > 0) {
      setTimeout(() => {
        const timer = (ms) => new Promise((res) => setTimeout(res, ms));
        var inputs = [...document.getElementsByTagName("input")].splice(0, 5);
        this.getUnluckuNumbers(inputs, timer);
      }, 3000);
    }
  },
  computed: {
    ...mapGetters(["getNumbers"]),
  },
  destroyed() {
    this.deleteNumbers();
  },
};
</script>

<style></style>
