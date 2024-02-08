
import { createStore } from 'vuex'

export default createStore({
  state: {
    userData: null,
    jwt: {
      accessToken: null,
      refreshToken: null,
    },

    alertData : {
      show: false,
      message: '',
      type: '',
    },

    busData: {},

  },



  getters: {
    userData: state => state.userData,
    jwt: state => state.jwt,
    isAuthenticated(state) {
      return state.jwt.accessToken !== null;
    },

    alertData: state => state.alertData,

    busData: state => state.busData,

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

    setAlertData(state, data) {
      state.alertData = data;
    },

    setBusData(state, data) {
      state.busData = data;
    },

  },



  actions: {
    setuserData({ commit }, data) {
      commit('setuserData', data);
    },

    triggerAlert({ commit }, data) {
      commit('setAlertData', { show: true, ...data});
    },

    setBusData({ commit }, data) {
      commit('setBusData', data);
    },

  },



  modules: {
  }
})
