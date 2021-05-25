import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'

// axios.defaults.baseURL = 'http://localhost:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movielist: [],
    userInfo: {},
    battleList: [],
    
    token: localStorage.getItem('token'),
  },
  getters: {
    getBattleList(state) {
      return state.battleList
    }
  },
  mutations: {
    FETCH_BATTLE_LIST(state, battlelist){
      state.battleList = battlelist
    },
    CREATE_USER(state, userInfo) {
      state.userInfo = userInfo
    },
    AUTH_USER(state, token) {
      state.token = token
    },
  },
  actions: {
    async FETCH_BATTLE_LIST({ commit }) {
      const BATTLE_LIST_URL = 'http://localhost:8000/api/v1/community/post_list/'
      const response = await axios.get(BATTLE_LIST_URL)
      const battlelist = response.data
      // console.log(movielist)
      commit('FETCH_BATTLE_LIST', battlelist)
    },
 
    AUTH_USER({ commit }, userInfo) {
      return new Promise((resolve) => {
        
        const AUTH_USER_URL = 'http://localhost:8000/api/v1/api-token-auth/'
        const data = userInfo
        axios.post(AUTH_USER_URL, data)
        .then((response) => {

          const token = response.data.access
    
          localStorage.setItem('token', token)
          commit('AUTH_USER', token)
          resolve()
        })

      })

    }
    
  },
  modules: {
  }
})
