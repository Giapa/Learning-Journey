<template>
  <h1>{{ title }}</h1>
  <p>Welcome</p>
  <div v-if="showmodal">
    <Modal :theme="theme" @close="toggleModal">
      <template v-slot:links>
        <a href="#">sign up now</a>
        <a href="#">more info</a>
      </template>
      <h1>{{ header }}</h1>
      <p>{{ text }}</p>
    </Modal>
  </div>
  <div v-if="showmodaltwo">
    <Modal theme="none" @close="toggleModalTwo">
      <template v-slot:links>
        <a href="#">sign up now</a>
        <a href="#">more info</a>
      </template>
    </Modal>
  </div>
  <button @click.alt="toggleModal">Open modal(alt)</button>
  <button @click="toggleModalTwo">Open second modal</button>
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
      showmodaltwo: false,
    };
  },
  methods: {
    toggleModal() {
      this.showmodal = !this.showmodal;
    },
    toggleModalTwo() {
      this.showmodaltwo = !this.showmodaltwo;
    },
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
