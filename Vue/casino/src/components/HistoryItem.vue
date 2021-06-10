<template>
  <div
    class="
      border-4
      mx-10
      p-1
      my-1
      rounded-xl
      flex
      border-red-300
      w-1/2
      text-left
    "
    :class="{ 'border-green-300': this.game.status }"
  >
    <div class="mx-2 flex">
      <p class="font-bold">Draw numbers:</p>
      <span>&#10098;</span>
      <p
        v-for="draw in game.draws"
        :key="draw"
        class="px-1 font-bold text-red-500"
        :class="{ 'text-green-500': game.winningNumbers.includes(draw) }"
      >
        {{ draw }}
      </p>
      <span>&#10099;</span>
    </div>
    <div class="mx-2 flex">
      <p class="font-bold">Status:</p>
      {{ game.status ? "Won" : "Lost" }}
    </div>
    <div class="mx-2 flex flex-grow">
      <p class="font-bold">Total amount won:</p>
      {{ game.amount > 0 ? game.amount : "-" }}
    </div>
    <button
      class="
        bg-red-500
        text-gray-200
        rounded
        hover:bg-red-400
        px-2
        py-1
        focus:outline-none
        inline-flex
        align-middle
        text-xs
        object-right
      "
      @click="removeGame(game)"
    >
      X
    </button>
  </div>
</template>

<script>
export default {
  components: {},
  props: ["game"],
  methods: {
    removeGame(game) {
      this.$emit("remove-game", game);
    },
  },
};
</script>

<style></style>
