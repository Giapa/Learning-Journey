<template>
  <div class="home">
    <h1>Home</h1>
    <h2>Refs</h2>
    <p>{{ name }}</p>
    <p>{{ age }}</p>
    <button @click="handleClick">Click me</button>
    <button @click="age++">Add 1 to age</button>
    <input type="text" v-model="name" />
    <br />
    <h2>Reactive</h2>
    <p>{{ reactivename.name }}</p>
    <p>{{ reactivename.age }}</p>
    <button @click="updateReactive">Click here to change hero</button>
  </div>
</template>

<script>
import { ref, reactive } from "@vue/reactivity";
export default {
  name: "Home",
  setup() {
    console.log("Setup");

    const name = ref("Mario");
    const age = ref(30);

    const reactivename = reactive({ name: "Peach", age: 25 });

    const handleClick = () => {
      age.value = 40;
      name.value = "Luigi";
    };

    const updateReactive = () => {
      reactivename.name = "Daisy";
      reactivename.age = "27";
    };

    return { name, age, handleClick, reactivename, updateReactive };
  },
};
</script>
