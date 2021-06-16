<template>
  <div
    class="w-56 py-4 px-4 h-full relative bg-white shadow-lg rounded-lg my-auto mx-5"
  >
    <div @click="flipped = !flipped">
      <transition name="flip">
        <card-content v-if="!flipped">
          Front card
          <template slot="text"><slot name="front"></slot></template>
        </card-content>
      </transition>
      <transition name="flip-back">
        <card-content v-if="flipped">
          Back card
          <template slot="text"><slot name="back"></slot></template>
        </card-content>
      </transition>
    </div>
  </div>
</template>

<script>
import CardContent from "./CardContent.vue";

export default {
  components: { CardContent },
  name: "FlipCard",
  data: function() {
    return {
      flipped: false,
    };
  },
};
</script>

<style type="text/css" scoped>
.flip-enter-active,
.flip-back-enter-active {
  transition: all 0.8s ease;
}
.flip-enter {
  -webkit-transform: rotateY(90deg);
  -moz-transform: rotateY(90deg);
  -o-transform: rotateY(90deg);
  -ms-transform: rotateY(90deg);
  transform: rotateY(90deg);
  opacity: 0;
}
.flip-back-enter {
  -webkit-transform: rotateY(-90deg);
  -moz-transform: rotateY(90deg);
  -o-transform: rotateY(-90deg);
  -ms-transform: rotateY(-90deg);
  transform: rotateY(-90deg);
  opacity: 0;
}
</style>
