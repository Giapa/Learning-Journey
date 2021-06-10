<template>
  <div class="flex items-center justify-center mt-48">
    <div
      class="
        bg-gray-500
        text-white
        font-bold
        rounded-lg
        border
        shadow-lg
        p-10
        gap-5
      "
    >
      <logo></logo>
      <p
        class="
          text-lg
          sm:text-2xl sm:leading-10
          font-medium
          mt-5
          sm:mt-5
          text-center
          mb-5
        "
        v-if="price > 0"
      >
        Somehow you won. You always lose but this time you managed to win
        {{ price }} &#36;
      </p>
      <p
        class="
          text-lg
          sm:text-2xl sm:leading-10
          font-medium
          mt-5
          sm:mt-5
          text-center
          mb-5
        "
        v-else
      >
        What did you expect? Of course you lost all your money. Good luck next
        time nerd.
      </p>
      <router-link to="/">
        <black-button class="mr-5">Play again</black-button>
      </router-link>
      <black-button @click.native="saveHistory">Save game</black-button>
    </div>
  </div>
</template>

<script>
import Logo from "./Logo.vue";
import BlackButton from "./BlackButton.vue";

export default {
  components: { Logo, BlackButton },
  props: ["winnings"],
  data() {
    return {
      price: 0,
    };
  },
  methods: {
    saveHistory() {
      this.$emit("save-history", this.price);
    },
  },
  created() {
    if (this.winnings.length == 3) {
      this.price = 5;
    } else if (this.winnings.length == 4) {
      this.price = 10;
    } else if (this.winnings.length == 5) {
      this.price = 15;
    } else {
      this.price = 0;
    }
  },
};
</script>

<style></style>
