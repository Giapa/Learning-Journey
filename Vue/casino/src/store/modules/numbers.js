const state = {
  numbers: [],
};

const getters = {
  getNumbers: (state) => state.numbers,
  getSpecificNumber: (state) => (number) => {
    return state.numbers.filter((item) => {
      return item === number;
    });
  },
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
  removeNumbers: (state) => {
    state.numbers = [];
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
