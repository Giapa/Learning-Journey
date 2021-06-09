<template>
  <div>
    <p
      class="
        text-lg
        sm:text-2xl sm:leading-10
        font-medium
        mb-2
        mt-10
        sm:mb-2
        text-center
      "
    >
      <slot></slot>
    </p>
    <div class="flex items-center justify-center gap-1">
      <number-input
        v-for="index in loop"
        :placeholder="Array.isArray(loop) ? index : ''"
        :key="index"
        readonly
        :class="[
          dimensions[0],
          dimensions[1],
          'mt-10',
          'text-4xl',
          'text-bold',
        ]"
      ></number-input>
    </div>
  </div>
</template>

<script>
import NumberInput from "./NumberInput.vue";
export default {
  components: { NumberInput },
  props: ["dimensions", "loop"],
};
</script>

<style></style>
