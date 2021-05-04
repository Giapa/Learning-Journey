<template>
  <div class="home">
    <h1>Home</h1>
    <p ref="p">{{ name }}</p>
    <p>{{ age }}</p>
    <button @click="handleClick">Click me</button>
  </div>
</template>

<script>
import { ref } from "@vue/reactivity";
export default {
  name: "Home",
  setup() {
    console.log("Setup");

    const p = ref(null);

    let name = "Mario";
    let age = 30;

    const handleClick = () => {
      console.log(p, p.value);
      p.value.classList.add("test");
      p.value.textContent = "This text is replaced by reference";
    };

    return { name, age, handleClick, p };
  },
};
</script>
