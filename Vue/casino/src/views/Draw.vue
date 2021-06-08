<template>
  <div>
    <p
      class="
        text-lg
        sm:text-2xl sm:leading-10
        font-medium
        mb-5
        mt-20
        sm:mb-5
        text-center
      "
    >
      Wait for the unlucky numbers
    </p>
    <div class="flex items-center justify-center gap-1">
      <number-input
        v-for="index in 5"
        :key="index"
        :id="index"
        readonly
        class="w-48 h-48 mt-20"
      ></number-input>
    </div>
  </div>
</template>

<script>
import NumberInput from "../components/NumberInput.vue";
export default {
  components: { NumberInput },
};
</script>

<style></style>
