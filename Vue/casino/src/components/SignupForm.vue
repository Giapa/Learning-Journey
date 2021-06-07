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
      <button
        class="
          bg-blue
          text-white
          font-bold
          py-2
          px-4
          rounded
          border
          block
          mx-auto
          w-full
        "
        @click="register"
      >
        Signup
      </button>
    </form>
  </div>
</template>

<script>
import firebase from "firebase";

export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    register(e) {
      firebase
        .auth()
        .createUserWithEmailAndPassword(this.email, this.password)
        .then(
          (result) => {
            alert(`account created for ${result.user.email}`);
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
