<template>
  <div id="app" class="grid grid-cols-1 justify-items-center text-center">
    <card
      ><template slot="front">
        Hey user.This is some sample text
      </template>
      <template slot="back">
        Thought u could get rid of me user? This is some more sample text in
        order to check the height of the div if it's changing according to the
        content. This is some lorem ipsum text to test the height of the
        element.
      </template></card
    >
  </div>
</template>

<script>
import Card from "./components/Card.vue";

export default {
  name: "App",
  components: {
    Card,
  },
  data() {
    return {};
  },
};
</script>

<style></style>
