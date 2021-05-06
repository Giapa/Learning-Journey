<template>
  <div class="home">
    <h1>Home</h1>
    <p>{{ name }}</p>
    <p>{{ age }}</p>
    <button @click="handleClick">Click me</button>
    <button @click="age++">Add 1 to age</button>
    <input type="text" v-model="name" />
  </div>
</template>

<script>
import { ref } from "@vue/reactivity";
export default {
  name: "Home",
  setup() {
    console.log("Setup");

    const name = ref("Mario");
    const age = ref(30);

    const handleClick = () => {
      age.value = 40;
      name.value = "Luigi";
    };

    return { name, age, handleClick };
  },
};
</script>
