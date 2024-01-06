import { createStore } from 'vuex'

export default createStore({
  state: {
    userData: null,
    jwt: {
      accessToken: null,
      refreshToken: null,
    },
  },



  getters: {
    userData: state => state.userData,
    jwt: state => state.jwt,
    isAuthenticated(state) {
      return state.jwt.accessToken !== null;
    },

  },



  mutations: {
    setuserData(state, data) {
      state.userData = data;
    },
    setAccessToken(state, accessToken) {
      if (!state.jwt) {
        state.jwt = {};
      }
      state.jwt.accessToken = accessToken;
    },
    setRefreshToken(state, refreshToken) {
      state.jwt.refreshToken = refreshToken;
    },
    resetState(state) {
      state.userData = null;
      state.jwt = null;
    },
  },



  actions: {
    setuserData({ commit }, data) {
      commit('setuserData', data);
    },
  },



  modules: {
  }
})
