import Vue from "vue";
import Vuex from "vuex";
import Numbers from "./modules/numbers";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: { Numbers },
});
