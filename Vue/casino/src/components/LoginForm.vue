<template>
  <div class="container">
    <form class="bg-blue text-center px-3 py-4 text-white mx-auto rounded">
      <input
        type="text"
        placeholder="Email"
        v-model="email"
        class="
          block
          w-full
          mx-auto
          text-sm
          py-2
          px-3
          rounded
          my-3
          text-black
          focus:outline-none
          focus:ring-2
          focus:ring-black
          focus:border-transparent
        "
      />
      <input
        type="password"
        placeholder="Password"
        v-model="password"
        class="
          block
          w-full
          mx-auto
          text-sm
          py-2
          px-3
          rounded
          my-3
          text-black
          focus:outline-none
          focus:ring-2
          focus:ring-black
          focus:border-transparent
        "
      />
      <black-button class="block w-full" @click.native="login">
        Login
      </black-button>
    </form>
  </div>
</template>

<script>
import firebase from "firebase";
import BlackButton from "./BlackButton.vue";

export default {
  components: { BlackButton },
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    login(e) {
      firebase
        .auth()
        .signInWithEmailAndPassword(this.email, this.password)
        .then(
          (result) => {
            alert(`You are logged in as ${result.user.email}`);
            this.$router.push("/");
          },
          (err) => alert(err.message)
        );
      e.preventDefault();
    },
  },
};
</script>

<style></style>
