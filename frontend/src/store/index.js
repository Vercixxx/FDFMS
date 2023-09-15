import { createStore } from 'vuex'

export default createStore({
  state: {
    responseData: null
  },
  getters: {
    responseData: state => state.responseData
  },
  mutations: {
    setResponseData(state, data) {
      state.responseData = data;
    }
  },
  actions: {
    fetchAndSetResponseData({ commit }, response) {
      commit('setResponseData', response);
    }
  },
  modules: {
  }
})
