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
      <h5>You can unlock the draw page by playing from the Home page.</h5>
    </div>
  </div>
</template>

<script>
import Logo from "../components/Logo.vue";
export default {
  name: "DrawTab",
  components: { Logo },
};
</script>

<style></style>
