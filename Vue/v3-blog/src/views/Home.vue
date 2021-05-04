<template>
  <div class="home">
    <h1>Home</h1>
    <p>{{ name }}</p>
    <p>{{ age }}</p>
    <button @click="handleClick">Click me</button>
  </div>
</template>

<script>
export default {
  name: "Home",
  setup() {
    console.log("Setup");

    let name = "Mario";
    let age = 30;

    const handleClick = () => {
      console.log("you clicked the button");
    };

    return { name, age, handleClick };
  },
};
</script>
