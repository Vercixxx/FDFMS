import { createStore } from 'vuex'

export default createStore({
  state: {
    responseData: null,
    jwt: {
      accessToken: null,
      refreshToken: null,
    },
  },
  getters: {
    responseData: state => state.responseData,
    jwt: state => state.jwt,
    isAuthenticated(state) {
      return state.jwt.accessToken !== null;
    },

  },
  mutations: {
    setResponseData(state, data) {
      state.responseData = data;
    },
    setJwt(state, jwt) {
      state.jwt = jwt;
    },
    resetState(state) {
      state.responseData = null;
      state.jwt = null;
    },
  },
  actions: {
    setResponseData({ commit }, data) {
      commit('setResponseData', data);
    },
  },
  modules: {
  }
})
