const state = {
  numbers: [],
};

const getters = {
  getNumbers: (state) => state.numbers,
};

const actions = {
  addNumbers({ commit }, numbers) {
    commit("setNumbers", numbers);
  },
  deleteNumbers({ commit }) {
    commit("removeNumbers");
  },
};

const mutations = {
  setNumbers: (state, numbers) => {
    state.numbers = numbers;
  },
  deleteNumbers: (state) => {
    state.numbers = [];
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
