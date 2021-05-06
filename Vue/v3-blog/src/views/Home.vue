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
    <br />
    <h2>Computed values</h2>
    <p>{{ computedname }}</p>
    <h2>Ref list</h2>
    <div v-for="lname in matchinaNames" :key="lname">
      <p>{{ lname }}</p>
    </div>
    <input type="text" v-model="search" />
    <button @click="stopWatchers">Click to stop watch</button>
  </div>
</template>

<script>
import { ref, reactive, computed } from "@vue/reactivity";
import { watch, watchEffect } from "@vue/runtime-core";
export default {
  name: "Home",
  setup() {
    const computedname = computed(() => {
      return "Shaun";
    });

    const names = ref(["mario", "luigi", "yoshi", "browser", "toad"]);
    const search = ref("");

    const stopWatch = watch(search, () => {
      console.log("Watch run");
    });

    const stopEffect = watchEffect(() => {
      console.log("WatchEffect function ran", search.value);
    });

    const stopWatchers = () => {
      stopWatch();
      stopEffect();
    };

    const name = ref("Mario");
    const age = ref(30);

    // Reactive cannot use primative values.
    const reactivename = reactive({ name: "Peach", age: 25 });

    const handleClick = () => {
      age.value = 40;
      name.value = "Luigi";
    };

    const updateReactive = () => {
      reactivename.name = "Daisy";
      reactivename.age = "27";
    };

    const matchinaNames = computed(() => {
      return names.value.filter((name) => name.includes(search.value));
    });

    return {
      name,
      age,
      handleClick,
      reactivename,
      updateReactive,
      computedname,
      search,
      matchinaNames,
      stopWatchers,
    };
  },
};
</script>
