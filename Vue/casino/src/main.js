import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./assets/css/index.css";
import config from "../firebaseConfig";
import firebase from "firebase";

Vue.config.productionTip = false;

firebase.initializeApp(config);

let app;
firebase.auth().onAuthStateChanged(() => {
  if (!app) {
    new Vue({
      router,
      store,
      render: function (h) {
        return h(App);
      },
    }).$mount("#app");
  }
});
