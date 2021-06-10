<template>
  <div>
    <h1
      class="
        text-6xl
        sm:text-6xl sm:leading-10
        font-medium
        mb-5
        mt-10
        sm:mb-5
        text-center
      "
    >
      Draw History
    </h1>
    <div class="grid justify-items-center">
      <history-item
        v-for="(game, index) in games"
        :key="index"
        :game="game"
        v-on:remove-game="deleteGame"
      ></history-item>
    </div>
  </div>
</template>

<script>
import firebase from "firebase";
import HistoryItem from "../components/HistoryItem.vue";
export default {
  components: { HistoryItem },
  data() {
    return {
      games: [],
    };
  },
  methods: {
    deleteGame(g) {
      this.games = this.games.filter(
        (game) => game.date.seconds !== g.date.seconds
      );
      firebase
        .firestore()
        .collection("history")
        .where("date", "==", g.date)
        .get()
        .then((querySnapshot) => {
          querySnapshot.forEach((doc) => {
            doc.ref.delete();
          });
        });
    },
  },
  created() {
    var user = firebase.auth().currentUser.email;
    firebase
      .firestore()
      .collection("history")
      .where("user", "==", user)
      .orderBy("date", "desc")
      .get()
      .then((querySnapshot) => {
        this.games = querySnapshot.docs.map((doc) => doc.data());
      });
  },
};
</script>

<style></style>
