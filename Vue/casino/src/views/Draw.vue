<template>
  <div v-if="!finished">
    <card-display :dimensions="['w-48', 'h-48']" :loop="5" ref="draws"
      >The unlucky numbers are:</card-display
    >
    <beat-loader loading="loading" color="black" class="my-10"></beat-loader>
    <card-display
      :dimensions="['w-36', 'h-36']"
      :loop="getNumbers"
      class="mt-10"
      >Your numbers</card-display
    >
  </div>
  <div v-else-if="finished">
    <result-modal
      :winnings="this.winningNumbers"
      v-on:save-history="saveGame"
    ></result-modal>
  </div>
  <div v-else>
    <p
      class="
        text-lg
        sm:text-2xl sm:leading-10
        font-medium
        mt-20
        sm:mt-20
        text-center
      "
    >
      You must play from the Home page. Go back.
    </p>
  </div>
</template>

<script>
import CardDisplay from "../components/CardDisplay.vue";
import BeatLoader from "vue-spinner/src/BeatLoader.vue";
import ResultModal from "../components/ResultModal.vue";
import firebase from "firebase";
import { mapActions, mapGetters } from "vuex";

export default {
  components: { CardDisplay, BeatLoader, ResultModal },
  data() {
    return {
      randomNumbers: [],
      winningNumbers: [],
      finished: false,
    };
  },
  methods: {
    ...mapActions(["deleteNumbers"]),
    saveGame(price) {
      var user = firebase.auth().currentUser.email;
      firebase
        .firestore()
        .collection("history")
        .add({
          amount: price,
          draws: this.randomNumbers,
          status: price > 0 ? true : false,
          user: user,
          date: firebase.firestore.Timestamp.fromDate(new Date()),
          playedNumbers: this.getNumbers,
          winningNumbers: this.winningNumbers,
        })
        .then(alert("Game was saved to history."), this.$router.push("/"))
        .catch((error) => console.log(error));
    },
    checkNumber(number) {
      if (this.getSpecificNumber(number).length >= 1) {
        this.winningNumbers.push(number);
        return true;
      }
      return false;
    },
    async getUnluckuNumbers(timer) {
      for (var i = 0; i < 5; i++) {
        await timer(4000);
        var randomNumber = this.generateRandom();
        this.randomNumbers.push(randomNumber);
        const card = this.$refs.draws.$refs.card[i];
        const input = card.$refs.input;
        input.value = randomNumber;
        if (this.checkNumber(randomNumber)) {
          card.$el.classList.value =
            card.$el.classList.value + " border-green-600 ";
          console.log("green", card.$el.classList);
        } else {
          card.$el.classList.value =
            card.$el.classList.value + " border-red-600 ";
        }
        card.$el.classList.value = card.$el.classList.value + " border-4 ";
      }
      await timer(3000);
      this.finished = true;
    },
    generateRandom() {
      var randomNumber;
      do {
        randomNumber = Math.floor(Math.random() * 30) + 1;
      } while (this.randomNumbers.includes(randomNumber));
      return randomNumber;
    },
  },
  mounted() {
    if (this.getNumbers.length > 0) {
      setTimeout(() => {
        const timer = (ms) => new Promise((res) => setTimeout(res, ms));
        // var inputs = [...document.getElementsByTagName("input")].splice(0, 5);

        this.getUnluckuNumbers(timer);
      }, 3000);
    }
  },
  computed: {
    ...mapGetters(["getNumbers", "getSpecificNumber"]),
  },
  destroyed() {
    this.deleteNumbers();
    this.finished = false;
  },
};
</script>

<style></style>
