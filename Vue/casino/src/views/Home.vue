<template>
  <div>
    <logo class="text-black"></logo>
    <p
      class="
        text-lg
        sm:text-2xl sm:leading-10
        font-medium
        mb-5
        sm:mb-5
        text-center
      "
    >
      Click the button and pick 5 number to start losing.
    </p>
    <a
      v-show="!play"
      class="
        w-full
        sm:w-auto
        flex-none
        bg-gray-900
        hover:bg-gray-700
        text-white text-lg
        leading-6
        font-semibold
        py-3
        px-6
        border border-transparent
        rounded-xl
        focus:ring-2
        focus:ring-offset-2
        focus:ring-offset-white
        focus:ring-gray-900
        focus:outline-none
        transition-colors
        duration-200
        cursor-pointer
      "
      @click="play = true"
      >Click to choose 5 numbers</a
    >
    <div class="flex items-center justify-center gap-1" v-show="play">
      <number-input
        v-for="index in 5"
        :key="index"
        v-on:number-check="checkValue"
        :id="index"
      ></number-input>
      <a
        class="
          sm:w-auto
          flex-none
          bg-gray-900
          hover:bg-gray-700
          text-white text-lg
          leading-6
          font-semibold
          py-3
          px-6
          border border-transparent
          rounded-xl
          focus:ring-2
          focus:ring-offset-2
          focus:ring-offset-white
          focus:ring-gray-900
          focus:outline-none
          transition-colors
          duration-200
          cursor-pointer
        "
        @click="saveNumbers"
        >Submit numbers</a
      >
    </div>
    <error-modal v-on:close-modal="error = false" v-if="error"
      >You can only choose between 1-30. Invalid inputs.</error-modal
    >
    <h1 class="my-10">
      More than 100.000.000 people have lost their entire property. Don't miss
      out on the feeling.
    </h1>
    <p
      class="
        text-lg
        sm:text-2xl sm:leading-10
        font-medium
        mb-2
        sm:mb-2
        text-center
      "
    >
      Our users say:
    </p>
    <div class="justify-center items-stretch flex space-x-20">
      <user-card v-for="user in users" :key="user.name">
        <template v-slot:name>{{ user.name }}</template>
        <q> {{ user.testimony }} </q>
        <template v-slot:price>{{ user.lost }} &#36;</template>
      </user-card>
    </div>
  </div>
</template>

<script>
import UserCard from "../components/UserCard.vue";
import firebase from "firebase";
import Logo from "../components/Logo.vue";
import NumberInput from "../components/NumberInput.vue";
import ErrorModal from "../components/ErrorModal.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "Home",
  components: { UserCard, Logo, NumberInput, ErrorModal },
  data() {
    return {
      users: [],
      placeholder: "",
      isLoggedIn: false,
      numbers: [],
      play: false,
      error: false,
    };
  },
  mounted() {
    firebase
      .firestore()
      .collection("testimony")
      .get()
      .then((querySnapshot) => {
        this.users = querySnapshot.docs.map((doc) => doc.data());
      });
  },
  created() {
    if (firebase.auth().currentUser) {
      this.isLoggedIn = true;
      this.play = true;
    }
  },
  methods: {
    ...mapActions(["addNumbers"]),
    checkValue(val) {
      const value = parseInt(val.value);
      const id = val.id;
      if (value <= 30 && value >= 1) {
        if (this.numberExists(id)) {
          const index = this.numbers.findIndex((num) => num.id == id);
          this.numbers[index].value = value;
        } else {
          this.numbers.push({ id: id, value: value });
        }
      }
    },
    numberExists(id) {
      return this.numbers.some((num) => {
        return num.id === id;
      });
    },
    saveNumbers() {
      if (this.numbers.length == 5) {
        this.addNumbers(
          this.numbers.map((item) => {
            return item.value;
          })
        );
        this.$router.push({ name: "Draw" });
      } else {
        this.error = true;
      }
    },
  },
  computed: {
    ...mapGetters(["getNumbers"]),
  },
};
</script>
