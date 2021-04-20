<template>
  <h1>{{ title }}</h1>
  <div v-if="showmodal">
    <Modal :header="header" :text="text" :theme="theme" />
  </div>
</template>

<script>
import Modal from "./components/Modal.vue";

export default {
  name: "App",
  components: {
    Modal,
  },
  data() {
    return {
      title: "My first Vue app",
      header: "This is a prop",
      text: "This is another prop",
      theme: "sale",
      showmodal: false,
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1 {
  border-bottom: 1px solid white;
  display: inline-block;
  padding-bottom: 10px;
}
</style>
