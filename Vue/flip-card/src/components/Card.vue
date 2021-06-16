<template>
  <div>
    <vue-flip active-click width="auto" height="auto">
      <template v-slot:front>
        <card-content
          class="w-56 h-auto absolute bg-white shadow-lg rounded-lg my-auto mx-5"
        >
          Front card
          <template slot="text"><slot name="front"></slot></template>
        </card-content>
      </template>
      <template v-slot:back>
        <card-content
          class="w-56 h-auto absolute bg-white shadow-lg rounded-lg my-auto mx-5"
        >
          Back card
          <template slot="text"><slot name="back"></slot></template>
        </card-content>
      </template>
    </vue-flip>
  </div>
</template>

<script>
import CardContent from "./CardContent.vue";
import VueFlip from "vue-flip";

export default {
  components: { CardContent, VueFlip },
  name: "FlipCard",
  data: function() {
    return {
      flipped: false,
    };
  },
};
</script>

<style type="text/css" scoped></style>
