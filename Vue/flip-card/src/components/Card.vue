<template>
  <div
    class="flip-container"
    :class="[flipped ? 'flip-container--clicked' : '']"
    @click="flipped = !flipped"
  >
    <div class="flipper w-80 h-full my-auto">
      <div class="front bg-white shadow-lg rounded-lg">
        <card-content v-if="!flipped">
          Front Card
          <template slot="text"><slot name="front"></slot></template>
        </card-content>
      </div>
      <div class="back bg-white shadow-lg rounded-lg">
        <card-content v-if="flipped">
          Back card
          <template slot="text"><slot name="back"></slot></template>
        </card-content>
      </div>
    </div>
  </div>
</template>

<script>
import CardContent from "./CardContent";
export default {
  name: "Card",
  components: {
    CardContent,
  },
  data() {
    return {
      flipped: false,
    };
  },
};
</script>

<style type="text/css" scoped>
.flip-container {
  -webkit-perspective: 1000;
  -moz-perspective: 1000;
  -o-perspective: 1000;
  perspective: 1000;
}
.flip-container {
  min-height: 120px;
}
.flipper {
  -moz-transform: perspective(1000px);
  -moz-transform-style: preserve-3d;
  position: relative;
}
.front,
.back {
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  -o-backface-visibility: hidden;
  backface-visibility: hidden;
  -webkit-transition: 0.6s;
  -webkit-transform-style: preserve-3d;
  -moz-transition: 0.6s;
  -moz-transform-style: preserve-3d;
  -o-transition: 0.6s;
  -o-transform-style: preserve-3d;
  -ms-transition: 0.6s;
  -ms-transform-style: preserve-3d;
  transition: 0.6s;
  transform-style: preserve-3d;
  top: 0;
  left: 0;
  width: 100%;
}
.back {
  -webkit-transform: rotateY(-180deg);
  -moz-transform: rotateY(-180deg);
  -o-transform: rotateY(-180deg);
  -ms-transform: rotateY(-180deg);
  transform: rotateY(-180deg);
}
.flip-container--clicked .back {
  -webkit-transform: rotateY(0deg);
  -moz-transform: rotateY(0deg);
  -o-transform: rotateY(0deg);
  -ms-transform: rotateY(0deg);
  transform: rotateY(0deg);
}
.flip-container--clicked .front {
  -webkit-transform: rotateY(180deg);
  -moz-transform: rotateY(180deg);
  -o-transform: rotateY(180deg);
  -ms-transform: rotateY(180deg);
  transform: rotateY(180deg);
}
.front {
  z-index: 2;
}
</style>
