<template>
  <div id="app" class="grid grid-cols-1 justify-items-center text-center gap-5">
    <card v-for="card in cards" :key="card.id"
      ><template slot="front">
        {{ card.front }}
      </template>
      <template slot="back">
        {{ card.back }}
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
    return {
      cards: [
        {
          id: 1,
          front: "Pellentesque quis ante arcu. Etiam.",
          back:
            "Ut eros lacus, viverra ac volutpat et, suscipit varius justo. Curabitur bibendum.",
        },
        {
          id: 2,
          front: "Suspendisse finibus feugiat quam eget.",
          back:
            "Pellentesque leo magna, malesuada vel maximus ac, ultrices eu sapien. Proin porttitor ante nec.",
        },
        {
          id: 3,
          front: "Nulla sit amet blandit odio.",
          back:
            "Proin in massa consequat, viverra lorem sit amet, vehicula lorem. Donec in ex eget erat.",
        },
        {
          id: 4,
          front: "Mauris maximus nulla eu maximus.",
          back:
            "Proin sagittis pharetra suscipit. Vestibulum faucibus condimentum pellentesque. Maecenas lobortis ex hendrerit mattis sodales. Integer ornare.",
        },
        {
          id: 5,
          front: "Proin semper ligula tellus, et rhoncus ligula vehicula.",
          back:
            "Vivamus ut urna ac mauris tempus hendrerit. Pellentesque suscipit efficitur dapibus. Nam eleifend, arcu non convallis tincidunt.",
        },
      ],
    };
  },
};
</script>

<style></style>
